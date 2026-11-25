from dataclasses import dataclass, field, fields, replace as dataclass_replace, KW_ONLY
from typing import Any, ClassVar

from ast import literal_eval

ATTR_SOCKETS = ['BOOLEAN', 'INT', 'VALUE', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU']


from dataclasses import dataclass, field
from typing import Any

from dataclasses import dataclass, field
from typing import Any

@dataclass
class NodeSocket:
    index           : int | None = None
    identifier      : str = ""
    name            : str = ""
    label           : str = ""
    socket_name     : str = ""
    group_name      : str | None = None
    group_sockets   : Any = None
    bl_idname       : str = ""
    socket_type     : str | None = None
    subtype_label   : str | None = None
    enabled         : bool = True
    is_output       : bool = False
    is_multi_input  : bool = False
    is_multi        : bool = False
    inferred        : str | None = None
    is_grid         : bool = False
    default_value   : Any = None
    is_menu         : bool = False
    enums           : Any = None
    names           : list[str] = field(default_factory=list)
    class_name      : str = ""
    is_attribute    : bool = False

    @classmethod
    def from_socket(cls, bsocket, index=None) -> "NodeSocket":

        socket_type = bsocket.type
        name        = bsocket.name
        label       = bsocket.label
        socket_name = label or name

        prop = bsocket.bl_rna.properties.get('default_value')
        is_menu = (
            socket_type == 'MENU'
            and not bsocket.is_output
            and prop is not None
        )

        if socket_type is None:
            class_name == ""
        elif socket_type == 'CUSTOM':
            class_name = ""
            name = "NAMED"
        else:
            from .node_info import NodeInfo
            class_name = NodeInfo.socket_class_name(socket_type, name)

        return cls(
            index           = index,
            identifier      = bsocket.identifier,
            name            = name,
            label           = label,
            socket_name     = socket_name,
            bl_idname       = bsocket.bl_idname,
            socket_type     = socket_type,
            subtype_label   = getattr(bsocket, 'bl_subtype_label', None),
            enabled         = bsocket.enabled,
            is_output       = bsocket.is_output,
            is_multi_input  = bsocket.is_multi_input,
            is_multi        = bsocket.is_multi_input,
            inferred        = bsocket.inferred_structure_type,
            is_grid         = bsocket.display_shape == 'VOLUME_GRID',
            default_value   = getattr(bsocket, 'default_value', None),
            is_menu         = is_menu,
            enums           = cls.get_enum_list(bsocket) if is_menu else None,
            names           = [socket_name],
            class_name      = class_name,
            is_attribute    = socket_type in ATTR_SOCKETS,
        )

    def __str__(self):
        enums = f" {self.enums}" if self.enums is not None else ""
        return f"<Socket '{self.identifier}' '{self.name}' {self.names} {enums=}>"

    @property
    def is_virtual(self):
        return self.socket_type == 'CUSTOM'

    # ====================================================================================================
    # Add a possible socket
    # ====================================================================================================

    def add_possible_socket(self, node_sockets):
        """ Combine with another socket configuration

        node_socket is computed on the same socket in a different configuration
        """

        for node_socket in node_sockets:
            if node_socket.identifier == self.identifier:
                if node_socket.enabled:
                    self.enabled = True
                    #self.names = self.names.union((node_socket.socket_name,))
                    if node_socket.socket_name not in self.names:
                        self.names.append(node_socket.socket_name)

                    if node_socket.socket_type != self.socket_type:
                        #assert False, "Shouldn't exist ?"
                        self.socket_type = 'SOCKET'
                        self.class_name = 'Socket'

                    break

        #assert self.identifier == node_socket.identifier, f"Algo error: {self.names=}, {self.identifier=}, {node_socket.socket_name=}, {node_socket.identifier=}"



    # ====================================================================================================
    # Utilities
    # ====================================================================================================

    @staticmethod
    def get_enum_list(bsocket):
        """Read the menu choices allowed in the socket's current state."""
        value = bsocket.default_value
        choices = None
        try:
            bsocket.default_value = 'GERR'
        except TypeError as error:
            token = '"GERR" not found in '
            message = str(error)
            position = message.find(token)
            if position < 0:
                return None
            values = literal_eval(message[position + len(token):])
            choices = (values,) if isinstance(values, str) else tuple(values)
            return choices
        finally:
            if choices != ():
                bsocket.default_value = value
        return None
