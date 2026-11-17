"""Contextual wrappers for socket and parameter generation.

NodeInfo prepares names, receiver selection and argument ordering;
NodeImplementation assembles the contributions. The wrappers never mutate their
introspection source. ``NodeParameter`` is currently named ``NodeParam``.
"""
from __future__ import annotations

import re

from dataclasses import dataclass, field, fields
from typing import TYPE_CHECKING, Any, Literal, get_type_hints

from ..kernel import snake_case
from .sourcewriter import SourceWriter, TAB, R0

if TYPE_CHECKING:
    from .node_socket import NodeSocket
    from .node_param import NodeParam
    from .typealiases import TypeAliases

_UNSET = object()
_NO_DEFAULT = "NOPE!"


SOURCES   = ('POSITIONAL', 'KEYWORD', 'KWARGS', 'FIXED', 'COMPUTED')
IN_HEADER = ('POSITIONAL', 'KEYWORD', 'KWARGS')
TARGETS   = ('ARG', 'NAMED_SOCKETS', 'PARAMETERS', 'KWARGS')

# ====================================================================================================
# List of argument names to make them unique
# ====================================================================================================

class NameSolver:
    PATTERN = re.compile(r"__ARG_\d+__")    

    def __init__(self):
        self.names = {}

    def clear(self):
        self.names.clear()

    def token(self, name):
        key = f"__ARG_{len(self.names):03d}__"
        self.names[key] = name
        return key

    def __call__(self, name):
        return self.token(name)

    def get_key(self, name, strict=True):
        keys = [key for key, value in self.names.items() if value == name]

        if strict:
            if len(keys) != 1:
                raise ValueError(
                    f"Argument name {name} is ambiguous : declared more than once: found {len(keys)}"
                )
            return keys[0]

        return keys[0] if len(keys) == 1 else keys    

    def solve(self, text):
        return self.PATTERN.sub(
            lambda m: self.names[m.group(0)],
            text
        )
    
    def make_unique(self, reserved=None):
        reserved = set(reserved or ())
        used = set(reserved)

        for key, name in self.names.items():
            unique = name
            i = 1

            while unique in used:
                unique = f"{name}_{i}"
                i += 1

            self.names[key] = unique
            used.add(unique)    

# ====================================================================================================
# Node Arguments
# ====================================================================================================

@dataclass
class NodeArguments:

    # Header
    header_positionals  : list[str] = field(default_factory=list)
    socket_keywords     : list[str] = field(default_factory=list)
    param_keywords      : list[str] = field(default_factory=list)
    header_kwargs       : list[str] = field(default_factory=list)

    arg_names           : NameSolver = field(default_factory=NameSolver)

    # Doc
    fixed_doc           : list[str] = field(default_factory=list)
    args_doc            : list[str] = field(default_factory=list)

    # Computation
    computations        : list[str] = field(default_factory=list)

    # Node creation
    node_args           : list[str] = field(default_factory=list)
    node_named_sockets  : list[str] = field(default_factory=list)
    node_parameters     : list[str] = field(default_factory=list)
    node_kwargs         : list[str] = field(default_factory=list)

    # control
    has_multi_socket    : bool = False
    reserved_names      : set[str] = field(default_factory=set)

    # ====================================================================================================
    # Feeding the header lists
    # ====================================================================================================

    def set_positional(self, name, typing=""):
        if name != 'self':
            self.header_positionals.append(f"*{name}{typing}")
        return

        count = 0
        for s in self.header_positionals:
            if s[0] == '*':
                count += 1
        if count > 1:
            raise ValueError(f"More than one positional argument for the header: {self.header_positionals}")

    def set_socket_keyword(self, name, typing="", default='None'):
        self.socket_keywords.append(f"{name}{typing} = {default}")

    def set_param_keyword(self, name, typing="", default='None'):
        self.param_keywords.append(f"{name}{typing} = {default}")

    def set_kwargs(self, name):
        self.header_kwargs.append(f"**{name}")
        return
    
        if len(self.header_kwargs) > 1:
            raise ValueError(f"More than one kwargs argument for the header: {self.header_kwargs}")

    # ====================================================================================================
    # Feeding the node call lists
    # ====================================================================================================

    def set_node_arg(self, name):
        if name == "self":
            self.node_args.append("self")
        else:            
            self.node_args.append(f"*{name}")

    def set_named_socket(self, name, value):
        self.node_named_sockets.append(f"'{name}': {value}")

    def set_dict_to_named_sockets(self, name):
        self.node_named_sockets.append(f"**{name}")

    def set_node_parameter(self, name, value):
        self.node_parameters.append(f"{name}={value}")

    def set_node_kwargs(self, name):
        self.node_kwargs.append(f"**{name}")

    # ====================================================================================================
    # Feeding the doc
    # ====================================================================================================

    def set_fixed_doc(self, name, value, description):
        self.fixed_doc.append(
            f"- {description} '{name}' = {value!r}"
        )        

    def set_args_doc(self, name, value_type, default, description):
        self.args_doc.append(
            f"{name} : {value_type}, optional\n"
            f"    {description} (default: {default!r})"
            )        

    def set_args_doc(self, name, value_type, default, description):
        has_default = default != _NO_DEFAULT

        doc = f"{name} : {value_type}"
        if has_default:
            doc += ", optional"

        doc += f"\n    {description}"

        if has_default:
            doc += f" (default: {default!r})"

        self.args_doc.append(doc)

    # ====================================================================================================
    # Triage
    # ====================================================================================================

    def add_parameter(self, node_param: NodeParam):
        name = node_param.name
        self.set_param_keyword(name, "", f"{node_param.value!r}")
        self.set_node_parameter(name, name)
        self.reserved_names.add(name)

        if node_param.param_type in ('ENUM', 'ENUM_FLAG'):
            value_type = '{' + ', '.join(repr(v) for v in node_param.enum_names) + '}'
        else:
            value_type = node_param.param_type

        self.set_args_doc(name, value_type, node_param.value, f"Node parameter '{node_param.name}'")

        return name

    def add_fixed_parameter(self, node_param: NodeParam, value: Any):
        self.set_node_parameter(node_param.name, value)

        self.set_fixed_doc(node_param.name, value, "Node parameter")

    def add_computed_parameter(self, node_param: NodeParam, computation: str, value_name: str | None = None):
        name = node_param.name
        self.computations.append(computation)
        value = name if value_name is None else value_name
        self.set_node_parameter(name, value)

        self.set_fixed_doc(name, value, "Computed node parameter")             

    def add_socket(self, node_socket: NodeSocket, is_self=False):

        # Virtual sockets : items
        if node_socket.is_virtual:
            if node_socket.name == 'NAMED':

                self.set_socket_keyword("named_sockets", ": dict", "{}")
                if is_self:
                    self.computations.append("all_sockets = {'Self': self, **named_sockets}")
                    self.set_dict_to_named_sockets("all_sockets")
                    self.set_args_doc("self", "Socket", _NO_DEFAULT, f"Dynamic socket created with 'Self' name")
                else:
                    self.set_dict_to_named_sockets("named_sockets")

                self.set_args_doc("named_sockets", "dict[str, Any]", {}, f"Dynamic sockets to create")

                self.set_kwargs("sockets")
                self.set_node_kwargs("sockets")

                self.set_args_doc("sockets", "dict[str, Any]", _NO_DEFAULT, f"Dynamic sockets to create passed as keyword arguments")


            elif node_socket.name == 'ANONYMOUS':
                self.set_positional("items")
                if is_self:
                    self.set_node_arg("self")
                    self.set_args_doc("self", "Socket", _NO_DEFAULT, f"First created socket")

                self.set_node_arg("items")
                self.set_args_doc("items", "Socket", _NO_DEFAULT, f"Dynamic sockets to create")

            else:
                assert False, f"Algo error {node_socket}"

            if is_self:
                return "self"
            else:
                return

        socket_id = f"ID_{node_socket.identifier}"

        # Multi input socket
        if node_socket.is_multi_input:
            if self.has_multi_socket:
                return
            self.has_multi_socket = True
            name = self.arg_names(snake_case(node_socket.socket_name))
            self.set_positional(name, f": {node_socket.class_name}")
            if is_self:
                self.set_named_socket(socket_id, f"[self, *{name}]")
                self.set_args_doc("self", node_socket.class_name, _NO_DEFAULT, f"Self feeds the multi input socket '{node_socket.socket_name}'")
                ret_name = "self"
            else:
                self.set_named_socket(socket_id, name)
                ret_name = name

            self.set_args_doc(name, node_socket.class_name, _NO_DEFAULT, f"Multi input socket '{node_socket.socket_name}'")
            return ret_name

        # General case : self
        if is_self:
            self.set_named_socket(socket_id, "self")
            return "self"

        # General case
        if len(node_socket.names) > 1:
            names = node_socket.names
        else:
            names = (node_socket.socket_name,)

        has_aliases = len(names) > 1
        aliases = []
        for name in names:
            name = self.arg_names(snake_case(name))
            self.set_socket_keyword(name, f": {node_socket.class_name}", 'None')

            if has_aliases:
                aliases.append(name)
                self.set_args_doc(name, node_socket.class_name, None, f"Alias of socket identifier: '{node_socket.identifier}'")
            else:
                self.set_named_socket(socket_id, name)
                self.set_args_doc(name, node_socket.class_name, None, f"Socket '{node_socket.socket_name}'")

        if has_aliases:
            self.set_named_socket(socket_id, f"next((v for v in ({', '.join(aliases)}) if v is not None), None)")
            return None
        else:            
            return name

    def add_fixed_socket(self, node_socket: NodeSocket, value: Any):
        socket_id = f"ID_{node_socket.identifier}" 
        self.set_named_socket(socket_id, value)

        self.set_fixed_doc(node_socket.socket_name, value, "Socket")


    def add_computed_socket(self, node_socket: NodeSocket, value_name: str, computation: str):
        socket_id = f"ID_{node_socket.identifier}" 
        self.set_named_socket(socket_id, value_name)
        self.computations.append(computation)

        self.set_fixed_doc(node_socket.socket_name, value_name, "Computed Socket")


    # ====================================================================================================
    # Consolidation
    # ====================================================================================================

    def make_arg_names_unique(self, reserved=None):
        reserved = set(reserved or ())
        reserved.update(self.reserved_names)
        self.arg_names.make_unique(reserved=reserved)

        hints = get_type_hints(type(self))

        for f in fields(self):
            if hints[f.name] == list[str]:
                a = getattr(self, f.name)
                for i, line in enumerate(a):
                    a[i] = self.arg_names.solve(line)

        self.arg_names.clear()

    def get_header(self):
        return self.header_positionals + self.socket_keywords + self.param_keywords + self.header_kwargs

    def get_node_call(self):

        node_call = list(self.node_args)

        if len(self.node_named_sockets):
            node_call.append("named_socket={" + ", ".join(self.node_named_sockets) + "}")

        node_call.extend(self.node_parameters)
        node_call.extend(self.node_kwargs)

        return node_call

    # ====================================================================================================
    # Source code
    # ====================================================================================================

    def get_header_source(self, with_R0=True):
        header = self.get_header()
        if len(header):
            if with_R0:
                return R0 + f",{R0}".join(header)
            else:
                return ", ".join(header)
        else:
            return ""

    def get_doc_source(self):
        source = ""
        if len(self.fixed_doc):
            source += "\n**Fixed inputs**\n"
            source += "\n".join(self.fixed_doc) + "\n"
        
        if len(self.args_doc):
            source += f"\nParameters\n"
            source += f"----------\n"
            source += "\n".join(self.args_doc) + "\n"

        return source

    def get_code_source(self, node_name):

        source = ""
        # Code
        if len(self.computations):
            source += "\n".join(self.computations) + "\n"

        # Node creation
        call = self.get_node_call()

        source += f"node = Node('{node_name}'"
        if len(call):
            source +=", " + ", ".join(call)

        source += ")\n"

        return source

    def get_mockup(self, as_method=True, doc=True):

        sw = SourceWriter(indent=0)

        # Header
        if len(self.get_header()):
            sw.write("def method(", new_line=False)
            if as_method:
                sw.write(f"{R0}self,", new_line=False)
            sw.write(self.get_header_source(), new_line=False)
            sw.write("):")
        else:
            if as_method:
                sw.write("def method(self):")
            else:
                sw.write("def method():")
        sw.indent += 1

        # Doc
        if doc:
            sw.write('"""')
            sw.write(self.get_doc_source())
            sw.write('"""')
        
        # Code

        sw.write(self.get_code_source("Node Name"))

        return sw.source

