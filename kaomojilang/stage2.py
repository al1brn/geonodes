"""Stage 2: parse the Python produced by stage 1 with `ast`, validate it, then run it.

The validator only accepts a small, side-effect free subset of Python: assignments, function defs,
calls, literals, comprehensions, arithmetic. No imports, attribute access, classes, lambdas, while loops
or names starting with a double underscore (except the helpers that stage 1 generates).
"""

import ast
import math
import random as _random
import traceback

from . import runtime
from .errors import RunError, Stage2Error
from .stage1 import demangle, mangle_symbols, translate

HELPERS = ("__shape__", "__defaults__", "__kaomoji__")

ALLOWED = (
    ast.Module, ast.FunctionDef, ast.arguments, ast.arg, ast.Return, ast.Assign, ast.AugAssign, ast.Expr,
    ast.If, ast.For, ast.Pass, ast.Call, ast.keyword, ast.Name, ast.Constant, ast.Dict, ast.List, ast.Tuple,
    ast.Set, ast.ListComp, ast.DictComp, ast.GeneratorExp, ast.comprehension, ast.BinOp, ast.UnaryOp, ast.BoolOp,
    ast.Compare, ast.IfExp, ast.Subscript, ast.Slice, ast.Starred,
    ast.operator, ast.unaryop, ast.boolop, ast.cmpop, ast.expr_context,
)

MAX_RANGE = 100_000


def _safe_range(*args):
    r = range(*args)
    if len(r) > MAX_RANGE:
        raise ValueError(f"range() is limited to {MAX_RANGE} items")
    return r


SAFE_BUILTINS = {
    "range": _safe_range, "len": len, "min": min, "max": max, "abs": abs, "round": round, "int": int,
    "float": float, "str": str, "bool": bool, "list": list, "dict": dict, "tuple": tuple, "zip": zip,
    "enumerate": enumerate, "sum": sum, "sorted": sorted, "reversed": reversed,
    "True": True, "False": False, "None": None,
}

MATH = {"pi": math.pi, "sin": math.sin, "cos": math.cos, "sqrt": math.sqrt, "radians": math.radians}


class Validator(ast.NodeVisitor):
    def __init__(self, res, filename):
        self.res, self.filename = res, filename

    def fail(self, node, message):
        line = self.res.original_line(getattr(node, "lineno", 0))
        text = self.res.original[line - 1] if line else None
        raise Stage2Error(message, line, text, self.filename)

    def generic_visit(self, node):
        if not isinstance(node, ALLOWED):
            self.fail(node, f"{type(node).__name__} is not allowed in kaomojilang")
        super().generic_visit(node)

    def visit_Name(self, node):
        if node.id.startswith("__") and (node.id not in HELPERS or not isinstance(node.ctx, ast.Load)):
            self.fail(node, f"name '{demangle(node.id)}' is reserved")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if node.name.startswith("__") or node.decorator_list:
            self.fail(node, "reserved name or decorator in def")
        self.generic_visit(node)

    def visit_arg(self, node):
        if node.arg.startswith("__"):
            self.fail(node, f"parameter name '{node.arg}' is reserved")
        self.generic_visit(node)

    def visit_keyword(self, node):
        if node.arg and node.arg.startswith("__"):
            self.fail(node, f"keyword '{node.arg}' is reserved")
        self.generic_visit(node)

    def visit_Constant(self, node):
        if not isinstance(node.value, (str, int, float, bool, type(None))):
            self.fail(node, "unsupported literal")


def parse_python(res, filename="<kaomoji>"):
    """ast.parse the stage 1 output; syntax errors are reported on the original line."""
    try:
        return ast.parse(res.source, filename)
    except SyntaxError as e:
        line = res.original_line(e.lineno or 0)
        text = res.original[line - 1] if line else None
        raise Stage2Error(e.msg, line, text, filename) from None


# ====================================================================================================
# Program
# ====================================================================================================

class Kaomoji:
    def __init__(self, text, label="", line=None):
        self.text, self.label, self.line = text, label, line

    def __repr__(self):
        return f"<Kaomoji {self.text} ({self.label})>"


class Program:
    """A loaded kaomojilang program."""

    def __init__(self, res, namespace, kaomoji, filename):
        self.stage1 = res
        self.python = res.source
        self.namespace = namespace
        self.kaomoji = kaomoji
        self.filename = filename

    @property
    def shape_names(self):
        """Display names of the grid drawings (defs)."""
        return list(self.stage1.shapes.values())

    def __getitem__(self, name):
        return self.namespace[mangle_symbols(name)[0]]

    def __contains__(self, name):
        return mangle_symbols(name)[0] in self.namespace

    def call(self, name, *args, **kwargs):
        try:
            return self[name](*args, **kwargs)
        except runtime.ShapeError as e:
            raise RunError(str(e), filename=self.filename) from None

    def variables(self):
        """User defined top-level variables (not helpers, not defs)."""
        skip = set(self.stage1.shapes) | set(self.namespace.get("__builtins__", {}))
        return {k: v for k, v in self.namespace.items()
                if not k.startswith("__") and k not in skip and not callable(v) and k not in self._base}

    _base = frozenset(runtime.COLORS) | frozenset(runtime.SIZES) | frozenset(MATH) | {"random"}

    def shapes(self):
        """Everything this program can draw, as {name: Shape or [Shape]}:
        top-level Shape values, lists of Shapes, and every grid def called without arguments."""
        found = {}
        for name, value in self.variables().items():
            if isinstance(value, runtime.Shape):
                found[demangle(name)] = value
            elif isinstance(value, (list, tuple)) and value and all(isinstance(v, runtime.Shape) for v in value):
                found[demangle(name)] = list(value)
        for display in self.shape_names:
            if display not in found:
                found[display] = self.call(display)
        return found

    def render_svgs(self, folder, cell=10.0, margin=1.0):
        """Write every drawing to `folder`; lists become name_000.svg ... with a shared framing."""
        import os
        os.makedirs(folder, exist_ok=True)
        written = []
        for name, value in self.shapes().items():
            safe = "".join(c if c.isalnum() or c in "_-" else f"_{ord(c):x}" for c in name)
            if isinstance(value, list):
                box = runtime.union_bbox(value)
                for k, s in enumerate(value):
                    path = os.path.join(folder, f"{safe}_{k:03d}.svg")
                    s.save_svg(path, cell=cell, margin=margin, bbox=box)
                    written.append(path)
            else:
                path = os.path.join(folder, f"{safe}.svg")
                value.save_svg(path, cell=cell, margin=margin)
                written.append(path)
        return written


def make_namespace(kaomoji_list, res):
    ns = {"__builtins__": dict(SAFE_BUILTINS)}
    ns.update(runtime.COLORS)
    ns.update(runtime.SIZES)
    ns.update(MATH)
    ns["random"] = _random.random
    ns["__shape__"] = runtime.build_shape
    ns["__defaults__"] = runtime.defaults_of
    ns["__kaomoji__"] = lambda text, label="": kaomoji_list.append(
        Kaomoji(text, label, next((l for t, lb, l in res.kaomoji if t == text and lb == label), None)))
    return ns


def run(source, filename="<kaomoji>"):
    """Translate (stage 1), parse + validate (stage 2), execute. Returns a Program."""
    res = translate(source, filename)
    tree = parse_python(res, filename)
    Validator(res, filename).visit(tree)
    code_name = f"<kaomoji:{filename}>"
    code = compile(tree, code_name, "exec")
    kaomoji = []
    ns = make_namespace(kaomoji, res)
    try:
        exec(code, ns)
    except Exception as e:
        line = None
        for fr in reversed(traceback.extract_tb(e.__traceback__)):
            if fr.filename == code_name:
                line = res.original_line(fr.lineno)
                break
        text = res.original[line - 1] if line else None
        raise RunError(f"{type(e).__name__}: {e}", line, text, filename) from None
    return Program(res, ns, kaomoji, filename)


def run_file(path):
    with open(path, encoding="utf-8") as f:
        return run(f.read(), path)
