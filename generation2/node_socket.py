"""Snapshot of a node socket in its current configuration."""

from ast import literal_eval
from .. import core_module

ATTR_SOCKETS = ['BOOLEAN', 'INT', 'VALUE', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU']

# ====================================================================================================
# Node Socket
# ====================================================================================================

class NodeSocket:
    def __init__(self, bsocket, index=None):

        self.index = index
        self.dependencies = {}

        self.identifier     = bsocket.identifier
        self.name           = bsocket.name 
        self.label          = bsocket.label
        self.socket_name    = self.label if bool(self.label) else self.name
        self.group_name     = None
        self.group_sockets  = None
        self.bl_idname      = bsocket.bl_idname
        self.socket_type    = bsocket.type
        self.enabled        = bsocket.enabled
        self.is_output      = bsocket.is_output
        self.is_multi_input = bsocket.is_multi_input
        self.is_multi       = self.is_multi_input
        self.inferred       = bsocket.inferred_structure_type
        self.is_grid        = bsocket.display_shape == 'VOLUME_GRID'
        self.default_value  = getattr(bsocket, 'default_value', None)

        prop = bsocket.bl_rna.properties.get('default_value')
        self.is_menu = self.socket_type == 'MENU' and not self.is_output and prop is not None
        if self.is_menu:
            self.enums = self.get_enum_list(bsocket)
        else:
            self.enums = None

        self.names = set((self.socket_name,))
        
        if self.socket_type not in [None, 'CUSTOM']:
            from .node_info import NodeInfo
            self.class_name = NodeInfo.socket_class_name(self.socket_type, self.name)
        else:
            self.class_name = ""

        self.is_attribute = self.socket_type in ATTR_SOCKETS
 
        """
        self.default_value = getattr(bsocket, 'default_value', None)
        prop = bsocket.bl_rna.properties.get('default_value')
        if prop is not None and prop.type in {'BOOLEAN', 'INT', 'FLOAT'} and prop.is_array:
            value = self.default_value
            self.default_value = value.copy() if hasattr(value, 'copy') else tuple(value)
        """

    def __str__(self):
        enums = f" {self.enums}" if self.enums is not None else ""
        return f"<Socket '{self.identifier}' '{self.name}' {self.names} {enums=} {self.dependencies=}>"

    # ====================================================================================================
    # Add a possible socket
    # ====================================================================================================

    def add_possible_socket(self, node_socket):
        """ Combine with another socket configuration

        node_socket is computed on the same socket in a different configuration
        """
        assert self.identifier == node_socket.identifier, "Algo error"

        if node_socket.enabled:
            self.enabled = True
            self.names = self.names.union((node_socket.socket_name,))

            if node_socket.socket_type != self.socket_type:
                #assert False, "Shouldn't exist ?"
                self.socket_type = 'SOCKET'
                self.class_name = 'Socket'


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
