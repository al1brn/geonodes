"""Python argument descriptions for generated node functions."""

from dataclasses import dataclass

from .. import core_module


_UNSET = object()


@dataclass
class Argument:
    """Describe an argument of a generated node function."""

    arg_type: str
    arg_name: str
    arg_value: str | None = None
    node_value: str | None = None
    typing: str | None = None
    comment: str | None = None
    is_argument: bool = True
    is_self: bool = False
    multiple: str = 'NO'
    identifier: str | None = None
    socket_name: str | None = None
    socket_type: str | None = None
    class_name: str | None = None
    inferred: str | None = None
    fixed: tuple | None = None
    check: str | None = None
    dynamic_items: bool = False

    @classmethod
    def from_param(cls, param, *, arg_name=None, value=_UNSET):
        """Build a parameter argument from a NodeParam.

        Supplying value fixes the parameter and removes it from the header.
        Values in arg_value and node_value are Python source expressions.
        """
        name = param.name if arg_name is None else arg_name
        argument = cls(arg_type='PARAM', arg_name=name)
        if value is not _UNSET:
            argument.is_argument = False
            argument.node_value = repr(value)
            argument.fixed = ('Parameter', param.name, f"`{argument.node_value}`")
            return argument

        argument.arg_value = param.arg_value
        argument.node_value = f"utils.get_font({name})" if param.param_type == 'FONT' else name
        argument.comment = param.comment.replace(f"{param.name} :", f"{name} :", 1)
        if param.param_type in {'ENUM', 'ENUM_FLAG'}:
            literal = f"Literal{list(param.enums)}" if param.enums else 'str'
            argument.typing = f"set[{literal}]" if param.param_type == 'ENUM_FLAG' else literal
            if param.param_type == 'ENUM' and param.name != 'data_type':
                argument.check = (
                    f"utils.check_enum_arg({param.bnode.name!r}, {param.name!r}, "
                    f"{name}, 'METH_NAME', {param.enums!r})"
                )
        return argument


    @classmethod
    def from_socket(cls, socket, *, arg_name=None, class_name=None, value=_UNSET):
        """Build a socket argument from a NodeSocket in a chosen configuration.

        Socket arguments default to None, as in get_arguments. Supplying value
        fixes the input instead. Name collisions are resolved by the caller.
        """
        socket_name = socket.label or socket.name
        name = core_module.utils.snake_case(socket_name) if arg_name is None else arg_name
        if class_name is None:
            from .node_info import NodeInfo
            class_name = NodeInfo.socket_class_name(socket.socket_type, socket_name)
        argument = cls(
            arg_type='SOCKET', arg_name=name, arg_value='None',
            node_value=f"list({name})" if socket.is_multi_input else name,
            multiple='ARGS' if socket.is_multi_input else 'NO',
            identifier=socket.identifier, socket_name=socket.name,
            socket_type=socket.socket_type, class_name=class_name,
            inferred=socket.inferred, typing=class_name,
        )
        if value is not _UNSET:
            argument.is_argument = False
            argument.node_value = repr(value)
            argument.fixed = ('Socket', socket_name, argument.node_value)
            argument.typing = "'IGNORED'"
            return argument

        if socket.socket_type == 'MENU':
            argument.typing = f"Literal{list(socket.enums)}" if socket.enums else 'str'
            argument.comment = (
                f"{name} : menu={socket.default_value!r}, optional\n"
                f"    {socket.enums}\n"
            )
        else:
            argument.comment = (
                f"{name} : {class_name}, optional\n"
                f"    socket '{socket_name}' (id: {socket.identifier})\n"
            )
        return argument


class Arguments:
    """Collect arguments and generation options for a NodeInfo."""

    def __init__(self,
                 node,
                 self_socket: str | None = None,
                 expose_selection: bool = True,
                 enabled_only: bool = True,
                 ignore_sockets: list[str] | None = None,
                 func_params: list[str] | None = None,
                 items: str = 'NONE',
                 **parameters):
        self.node = node
        self.self_socket = self_socket
        self.expose_selection = expose_selection
        self.enabled_only = enabled_only
        self.ignore_sockets = [] if ignore_sockets is None else list(ignore_sockets)
        self.func_params = [] if func_params is None else list(func_params)
        self.items = items
        self.parameters = parameters
        self.arguments = []

