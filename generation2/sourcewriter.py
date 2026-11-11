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
# A single argument
# ====================================================================================================

class Argument:
    """ Argument

    Used to build function signature and to build doc string
    """
    def __init__(self, name: str, arg_type: ARG_TYPE, *, value: str | None = None, typing=None, comment: str | None = None, type_aliases=None):

        self.type    = arg_type
        self.name    = name
        self.value   = value
        self.comment = comment

        if isinstance(typing, (list, tuple)):
            if not typing:
                raise ValueError('A Literal annotation requires at least one value')
            if type_aliases is None:
                self.typing  = f"Literal{list(typing)}"
                self.doc_typing = '{' + ', '.join(repr(value) for value in typing) + '}'
            else:
                self.typing  = type_aliases.literal(typing, prefix=f"T_{name.lstrip('*').upper()}")
                self.doc_typing = type_aliases.get_doc_string(self.typing)
        else:
            self.typing = typing
            self.doc_typing = typing if type_aliases is None else type_aliases.get_doc_string(typing)


    def __str__(self):
        return f"<Argument {self.name} {self.type}>"

    @property
    def is_positional(self):
        return self.type == 'POSITIONAL'

    @property
    def is_first(self):
        return self.name in ['cls', 'self']
    
    @property
    def header(self):

        if self.type == 'KWARGS':
            return f"**{self.name}"

        s = self.name

        if bool(self.typing):
            s += f": {self.typing}"

        if self.type == 'KEYWORD':
            s += f" = {self.value}"

        return s

    @property
    def doc_string(self):

        if self.name in ['cls', 'self']:
            return None

        s = f"{self.name} : "
        sep = ""
        if self.doc_typing:
            s += self.doc_typing
            sep = ", "
        if self.type == 'KEYWORD':
            s += f"{sep}optional"

        if self.comment:
            s += f"\n{TAB}{self.comment}"

        return s

# ====================================================================================================
# Source Writer
# ====================================================================================================

class SourceWriter:

    def __init__(self, name, func_type: FUNC_TYPE = 'FUNCTION', type_aliases=None):

        self.type_aliases = type_aliases

        self.arguments = []
        self.source = ""
        self.max_len = 100

        self.doc = []
        self.returns = None

        self.name = name
        self.func_type = func_type
        if self.func_type == 'FUNCTION':
            self.margin = ""
        else:
            self.margin = TAB

        if self.func_type in ('METHOD', 'SETTER', 'GETTER'):
            self.arguments.append(Argument('self', 'SPECIAL'))
        elif self.func_type in ('CLASS_METHOD', 'CLASS_PROPERTY'):
            self.arguments.append(Argument('cls', 'SPECIAL'))

    def check_syntax(self):
        """Compile without executing; return True or raise SyntaxError.

        Methods are compiled inside a class to preserve their indentation.
        """
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
    # Add arguments
    # ---------------------------------------------------------------------------

    def positional_argument(self, name: str, typing: str | None =None, comment: str | None =None):
        self.arguments.append(Argument(name, 'POSITIONAL', typing=typing, comment=comment, type_aliases=self.type_aliases))

    def keyword_argument(self, name: str, value, typing: str | None =None, comment: str | None =None):
        self.arguments.append(Argument(name, 'KEYWORD', value=value, typing=typing, comment=comment, type_aliases=self.type_aliases))

    def kwargs_argument(self, name: str, comment: str | None =None):
        self.arguments.append(Argument(name, 'KWARGS', comment=comment))

    # ---------------------------------------------------------------------------
    # Add comment
    # ---------------------------------------------------------------------------

    def add_doc(self, doc):
        self.doc.extend(doc.split("\n"))

    # ---------------------------------------------------------------------------
    # Write line to source code
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

    # ---------------------------------------------------------------------------
    # Sorted arguments
    # ---------------------------------------------------------------------------

    @property
    def sorted_arguments(self):

        first = []
        pos = []
        args = []
        kws = []
        kwargs = []

        for arg in self.arguments:
            if arg.name in ['cls', 'self']:
                first.append(arg)
            elif arg.type == 'POSITIONAL':
                if arg.name.startswith('*'):
                    args.append(arg)
                else:
                    pos.append(arg)
            elif arg.type == 'KEYWORD':
                kws.append(arg)
            elif arg.type == 'KWARGS':
                kwargs.append(arg)
            else:
                assert False, "Algo error: {arg}"

        if (len(first) > 1) or (len(args) > 1) or (len(kwargs) > 1):
            assert False, "Algo error: {first=}, {args=}, {kwargs=}"

        return first + pos + args + kws + kwargs

    # ---------------------------------------------------------------------------
    # Write header
    # ---------------------------------------------------------------------------

    def write_header(self):

        if self.func_type == 'CLASS_METHOD':
            self.write("@classmethod")
        elif self.func_type == 'STATIC_METHOD':
            self.write("@staticmethod")
        elif self.func_type == 'CLASS_PROPERTY':
            self.write("@utils.classproperty")
        elif self.func_type == 'GETTER':
            self.write("@property")
        elif self.func_type == 'SETTER':
            self.write(f"@{self.name}.setter")


        s = f"def {self.name}("

        args = [arg.header for arg in self.sorted_arguments]
        args_str = s + ", ".join(args)

        if len(args_str) > self.max_len:
            self.write(s)
            self.write(*(arg + "," for arg in args), indent=1)
            self.write("):")
        else:
            self.write(args_str + "):")

    # ---------------------------------------------------------------------------
    # Write doc string
    # ---------------------------------------------------------------------------

    def write_doc_string(self):

        if len(self.doc):
            first_line = self.doc[0]
            doc = self.doc[1:]
        else:
            first_line = self.name
            doc = []

        self.write(f'""" {first_line}', indent=1)
        self.write()
        if len(doc):
            self.write(*doc, indent=1)

        args = self.sorted_arguments
        if args and args[0].type == 'SPECIAL':
            args.remove(args[0])

        if len(args):
            self.write()

            self.write("Parameters", indent=1)
            self.write("----------", indent=1)

            for arg in args:
                self.write(*(arg.doc_string.split("\n")), indent=1)

        if bool(self.returns):
            self.write()

            self.write("Returns", indent=1)
            self.write("-------", indent=1)
            
            self.write(*(self.returns.split("\n")), indent=1)

        self.write('"""', indent=1)

    # ====================================================================================================
    # Node call
    # ====================================================================================================

    def write_node_call(self, node_name, args=None, named_sockets=None, parameters=None):

        # Arguments and parameters contain Python source expressions.
        positional = list(args) if args is not None else []
        parameters = list(parameters) if parameters is not None else []
        sockets = list(named_sockets) if named_sockets is not None else None

        socket_expr = "None" if sockets is None else "{" + ", ".join(sockets) + "}"
        call_args = [repr(node_name), *positional, f"named_sockets={socket_expr}", *parameters]
        line = "node = Node(" + ", ".join(call_args) + ")"

        if len(self.margin + TAB + line) <= self.max_len:
            self.write(line, indent=1)
            return

        self.write("node = Node(", indent=1)
        self.write(*(arg + "," for arg in [repr(node_name), *positional]), indent=2)
        if sockets is None:
            self.write("named_sockets=None,", indent=2)
        else:
            self.write("named_sockets={", indent=2)
            if sockets:
                self.write(*(socket + "," for socket in sockets), indent=3)
            self.write("},", indent=2)
        if parameters:
            self.write(*(parameter + "," for parameter in parameters), indent=2)
        self.write(")", indent=1)

