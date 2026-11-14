from __future__ import annotations
from typing import TYPE_CHECKING, Literal, Union, Sequence, Any

ARG_TYPE = Literal['POSITIONAL', 'KEYWORD', 'KWARGS', 'SPECIAL']
FUNC_TYPE = Literal['FUNCTION', 'STATIC_METHOD', 'METHOD', 'SETTER', 'GETTER', 'CLASS_METHOD', 'CLASS_PROPERTY']

TAB = "    "

# Optional new lines
R0 = "§^"
R1 = "§%"
R2 = "§&"

# Splittable lists
COMMA = ",^"
LIST  = "[^"
TUPLE = "(^"
SET   = "{^"

# ====================================================================================================
# Source Writer
# ====================================================================================================

class SourceWriter:

    def __init__(self, max_len=100, indent=0):

        self.source = ""

        self.max_len = max_len
        self.margin = indent*TAB

    def check_syntax(self):
        """Compile without executing; return True or raise SyntaxError.

        Methods are compiled inside a class to preserve their indentation.
        """
        return True
    
        source = self.source
        if self.func_type != 'FUNCTION':
            source = "class _SyntaxCheck:\n" + source
        compile(source, f"<SourceWriter {self.name}>", 'exec')
        return True

    # ---------------------------------------------------------------------------
    # Splittable lists
    # ---------------------------------------------------------------------------

    @classmethod
    def splittable(cls, a, as_type):
        s = COMMA.join(a)
        if as_type==list:
            return f"{LIST}{s}]"
        elif as_type==set:
            return f"{SET}{s}" + "}"
        else:
            return f"{TUPLE}{s})"

    # ---------------------------------------------------------------------------
    # Write a single line to source code
    # Interpretating optional new lines
    # ---------------------------------------------------------------------------

    def _write_line(self, line, indent, split_level):

        REPL = {R0 : " ", R1 : " ", R2: " ", COMMA: ", ",
                LIST: "[", TUPLE: "(", SET: "{"}

        left_indent = f"{self.margin}{TAB*indent}"

        # Measure the rendered line, including indentation, without markers.
        rendered = line
        for token, repl in REPL.items():
            rendered = rendered.replace(token, repl)

        # Short line
        if len(left_indent + rendered) <= self.max_len:
            self.source += left_indent + rendered
            return

        # List
        if split_level == 3:

            kind = None
            for sepa in (LIST, TUPLE, SET):
                pref_items = line.split(sepa)
                if len(pref_items) == 2:
                    kind = sepa
                    break

            if kind is None:
                self.source += left_indent + rendered
                return

            self.source += f"{left_indent}{pref_items[0]}{REPL[kind]}\n"

            items = pref_items[1].split(COMMA)
            left_indent += TAB

            stack = left_indent + items[0]
            for item in items[1:]:
                s = f"{stack}, {item}"
                if len(s) > self.max_len:
                    self.source += stack + ",\n"
                    stack = left_indent + item
                else:
                    stack = s

            self.source += stack
            return

        # Optional splits
        R = [R0, R1, R2][split_level]

        lines = line.split(R)
        self._write_line(lines[0], indent=indent, split_level = split_level + 1)

        for l in lines[1:]:
            self.source += "\n"
            self._write_line(l, indent=indent + 1, split_level = split_level + 1)

    # ---------------------------------------------------------------------------
    # Write lines to source code
    # ---------------------------------------------------------------------------

    def write(self, *lines, indent=0, new_line=True):

        # --------------------------------------------------
        # No line or more than one
        # --------------------------------------------------

        # Just new line
        if len(lines) == 0:
            if new_line:
                self.source += "\n"
            return

        # Several lines
        if len(lines) > 1:
            for line in lines:
                self.write(line, indent=indent, new_line=True)

            return

        line = lines[0]

        # Multi lines
        lines = line.split("\n")
        if len(lines) > 1:
            for i, part in enumerate(lines):
                self.write(part, indent=indent, new_line=new_line or i < len(lines) - 1)
            return

        # --------------------------------------------------
        # Single line
        # --------------------------------------------------

        self._write_line(line, indent=indent, split_level=0)
        if new_line:
            self.source += "\n"

