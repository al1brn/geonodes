"""Stage 1: translate kaomojilang source into valid Python source, line by line.

What it does
------------
1. Symbols as identifiers. Any non-ASCII character that Python cannot use in a name (like the square
   glyph or a fullwidth parenthesis) becomes `_uXXXX_`, so `def <glyph>(...)` and `<glyph>(smooth=1)` are valid.
   Strings and comments are left alone.
2. Grid blocks. The body of a `def` made only of integers is a drawing: every number is a point whose
   position is its place in the text. The def is rewritten into a normal function that returns
   `__shape__(points, name, params, defaults)`, `points` being a list of `(number, x, row)`.
3. Kaomoji lines. A line at column 0 that is not Python (not a def, assignment, comment, ...)
   becomes `__kaomoji__(text, label)`, the label being the comment on the next line.
4. Everything else is Python and is passed through (after symbol mangling).

The result keeps a `line_map` (output line -> original line) for error messages.
"""

import ast
import re
from dataclasses import dataclass, field

from .errors import Stage1Error

TAB = 4
GRID_PARAMS = ("fill", "stroke", "width", "sizes", "smooth", "shift", "rotate", "scale")     # forwarded to the shape builder

_DEF = re.compile(r"^def\s+(?P<name>[^\s(]+)\s*\((?P<params>.*)\)\s*:\s*(?:#.*)?$")
_PY_START = re.compile(
    r"^(?:#|@|(?:def|class|for|if|elif|else|while|return|import|from|with|try|except|finally|pass|del)\b"
    r"|[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*\s*(?:=(?!=)|\+=|-=|\*=|/=))")
_GRID_LINE = re.compile(r"^[\s\d~]*$")


# ====================================================================================================
# Symbol mangling
# ====================================================================================================

def mangle_char(c):
    return f"_u{ord(c):04x}_"


_MANGLED = re.compile(r"_u([0-9a-f]{4,6})_")


def demangle(name):
    """`_u25a2_` -> the original glyph (for display)."""
    return _MANGLED.sub(lambda m: chr(int(m.group(1), 16)), name)


def mangle_symbols(line, triple=None):
    """Mangle symbol characters outside strings / comments. Returns (new_line, triple_delimiter_state)."""
    out = []
    i, n, quote = 0, len(line), None
    while i < n:
        c = line[i]
        if triple:
            j = line.find(triple, i)
            if j < 0:
                out.append(line[i:])
                break
            out.append(line[i:j + 3])
            i, triple = j + 3, None
            continue
        if quote:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(line[i + 1])
                i += 2
                continue
            if c == quote:
                quote = None
            i += 1
            continue
        if c == "#":
            out.append(line[i:])
            break
        if line.startswith(('"""', "'''"), i):
            triple = line[i:i + 3]
            out.append(triple)
            i += 3
            continue
        if c in "'\"":
            quote = c
            out.append(c)
        elif ord(c) < 128:
            out.append(c)
        elif c.isspace():
            out.append(" ")
        elif ("_" + c).isidentifier():
            out.append(c)
        else:
            out.append(mangle_char(c))
        i += 1
    return "".join(out), triple


def bracket_delta(code):
    """Net number of open brackets in a (mangled) line, ignoring strings and comments."""
    depth, quote, i = 0, None, 0
    while i < len(code):
        c = code[i]
        if quote:
            if c == "\\":
                i += 1
            elif c == quote:
                quote = None
        elif c == "#":
            break
        elif c in "'\"":
            quote = c
        elif c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        i += 1
    return depth


# ====================================================================================================
# Result
# ====================================================================================================

@dataclass
class Stage1Result:
    source: str                                   # valid Python
    line_map: list                                # output line (0-based index) -> original line (1-based)
    original: list                                # original lines
    kaomoji: list = field(default_factory=list)   # (text, label, line)
    shapes: dict = field(default_factory=dict)    # python name -> display name, for grid defs

    def original_line(self, out_line):
        """1-based output line -> 1-based original line."""
        if 1 <= out_line <= len(self.line_map):
            return self.line_map[out_line - 1]
        return None


# ====================================================================================================
# Translator
# ====================================================================================================

def _strip_comment(line):
    return line.split("#", 1)[0]


def _is_grid(body):
    code = [_strip_comment(l) for l in body]
    code = [c for c in code if c.strip()]
    return bool(code) and all(_GRID_LINE.match(c) for c in code)


def _grid_points(body, first_line, filename):
    """Numbers of a grid block with their position: (number, x, row, open). x is the center of the number;
    a trailing `~` (as in `5~`) sets open=True: the run ends here and is not closed."""
    points, row0, seen = [], None, {}
    for k, raw in enumerate(body):
        code = _strip_comment(raw).expandtabs(TAB)
        if not code.strip():
            continue
        if row0 is None:
            row0 = k
        if "~" in re.sub(r"\d+~", "", code):
            raise Stage1Error("'~' must come right after a number (as in 5~)", first_line + k, raw, filename)
        for m in re.finditer(r"(\d+)(~?)", code):
            number = int(m.group(1))
            if number in seen:
                raise Stage1Error(f"number {number} is used twice in the same drawing "
                                  f"(first at line {seen[number]})", first_line + k, raw, filename)
            seen[number] = first_line + k
            points.append((number, m.start() + (len(m.group(1)) - 1) / 2, k - row0, bool(m.group(2))))
    return points


def translate(source, filename="<kaomoji>"):
    lines = source.splitlines()
    out, line_map = [], []
    result = Stage1Result("", line_map, lines)

    def emit(text, orig):
        out.append(text)
        line_map.append(orig)

    i, triple, depth, open_line = 0, None, 0, 0
    while i < len(lines):
        raw = lines[i]
        lineno = i + 1

        # -- inside a triple quoted string, or a bracketed continuation -------------------------------
        if triple or depth > 0:
            if depth > 0 and not triple and raw[:1] not in (" ", "\t", "", ")", "]", "}") and \
                    (raw.startswith("def ") or re.match(r"[A-Za-z_]\w*\s*=(?!=)", raw)):
                raise Stage1Error(f"bracket opened at line {open_line} is never closed "
                                  f"(a new statement starts here)", open_line, lines[open_line - 1], filename)
            code, triple = mangle_symbols(raw, triple)
            if not triple:
                depth = max(0, depth + bracket_delta(code))
            emit(code, lineno)
            i += 1
            continue

        stripped = raw.strip()
        if not stripped:
            emit("", lineno)
            i += 1
            continue
        if stripped.startswith("#"):
            emit(raw, lineno)
            i += 1
            continue

        indented = raw[:1] in (" ", "\t")

        # -- def header ---------------------------------------------------------------------------------
        if not indented and raw.startswith("def "):
            i = _translate_def(lines, i, emit, result, filename)
            continue

        # -- python statement or kaomoji ----------------------------------------------------------------
        if indented or _PY_START.match(raw) or raw.startswith(('"""', "'''")):
            code, triple = mangle_symbols(raw, None)
            depth = max(0, bracket_delta(code)) if not triple else 0
            open_line = lineno
            emit(code, lineno)
            i += 1
            continue

        # column 0 and not Python: a kaomoji line; the next comment line is its label
        label = ""
        for j in range(i + 1, len(lines)):
            nxt = lines[j].strip()
            if not nxt:
                continue
            if nxt.startswith("#"):
                label = nxt.lstrip("#").strip()
            break
        text = stripped
        result.kaomoji.append((text, label, lineno))
        emit(f"__kaomoji__({text!r}, {label!r})", lineno)
        i += 1

    if depth > 0:      # first: an unclosed bracket is usually the root cause of an unclosed string too
        raise Stage1Error(f"bracket opened at line {open_line} is never closed", open_line,
                          lines[open_line - 1], filename)
    if triple:
        raise Stage1Error("triple quoted string is never closed", len(lines), lines[-1] if lines else "", filename)
    result.source = "\n".join(out) + "\n"
    return result


def _translate_def(lines, i, emit, result, filename):
    """Translate the def at lines[i]; returns the index of the first line after its body."""
    lineno = i + 1
    header = lines[i]
    m = _DEF.match(header.rstrip())
    if not m:
        raise Stage1Error("malformed def, expected: def name(params):", lineno, header, filename)
    name_raw, params_raw = m.group("name"), m.group("params")
    name, _ = mangle_symbols(name_raw)
    params, _ = mangle_symbols(params_raw)
    if not name.isidentifier():
        raise Stage1Error(f"'{name_raw}' cannot be used as a name", lineno, header, filename)

    # body = following blank / indented lines
    j = i + 1
    while j < len(lines) and (not lines[j].strip() or lines[j][:1] in (" ", "\t")):
        j += 1
    end = j
    while end > i + 1 and not lines[end - 1].strip():
        end -= 1                                          # trailing blank lines are not part of the body
    body = lines[i + 1:end]

    if not _is_grid(body):
        # a regular python function: pass through
        emit(f"def {name}({params}):", lineno)
        triple = None
        for k, raw in enumerate(body):
            code, triple = mangle_symbols(raw, triple)
            emit(code, i + 2 + k)
        if not any(l.strip() and not l.strip().startswith("#") for l in body):
            emit("    pass", lineno)
        return end

    try:
        tree = ast.parse(f"def {name}({params}): pass")
    except SyntaxError as e:
        raise Stage1Error(f"invalid parameters: {e.msg}", lineno, header, filename) from None
    args = tree.body[0].args
    arg_names = [a.arg for a in args.posonlyargs + args.args + args.kwonlyargs]
    if args.vararg or args.kwarg:
        raise Stage1Error("drawings do not accept *args / **kwargs", lineno, header, filename)

    points = _grid_points(body, i + 2, filename)
    # every drawing accepts all the standard parameters: add the ones the header does not declare
    missing = [k for k in GRID_PARAMS if k not in arg_names]
    signature = params
    if missing:
        extra = ", ".join(f"{k}=None" for k in missing)
        star = "" if args.kwonlyargs else "*, "
        signature = f"{params}, {star}{extra}" if params.strip() else f"*, {extra}"
    forwarded = ", ".join(f"{k!r}: {k}" for k in GRID_PARAMS)
    display = demangle(name)
    result.shapes[name] = display
    emit(f"def {name}({signature}):", lineno)
    emit(f"    return __shape__({points!r}, {display!r}, {{{forwarded}}}, __defaults__({name}))", i + 2)
    return end
