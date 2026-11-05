"""Snapshot of a node socket in its current configuration."""

from ast import literal_eval
from .. import core_module

CLASS_NAMES = {
 'BOOLEAN': 'Boolean',
 'BUNDLE': 'Bundle',
 'CLOSURE': 'Closure',
 'COLLECTION': 'Collection',
 'CUSTOM': 'Input',
 'FONT': 'Font',
 'GEOMETRY': 'Geometry',
 'IMAGE': 'Image',
 'INT': 'Integer',
 'INT_VECTOR': 'IntVector',
 'MATERIAL': 'Material',
 'MATRIX': 'Matrix',
 'MENU': 'Menu',
 'OBJECT': 'Object',
 'RGBA': 'Color',
 'ROTATION': 'Rotation',
 'SHADER': 'Shader',
 'SOUND': 'Sound',
 'STRING': 'String',
 'VALUE': 'Float',
 'VECTOR': 'Vector',
}

ATTR_SOCKETS = ['BOOLEAN', 'INT', 'VALUE', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU']

class NodeSocket:
    def __init__(self, bsocket, index=None):
        self.index = index
        self.identifier = bsocket.identifier
        self.name = bsocket.name
        self.label = bsocket.label
        self.bl_idname = bsocket.bl_idname
        self.socket_type = bsocket.type
        self.enabled = bsocket.enabled
        self.is_output = bsocket.is_output
        self.is_multi_input = bsocket.is_multi_input
        self.inferred = bsocket.inferred_structure_type
        self.is_grid = bsocket.display_shape == 'VOLUME_GRID'
        self.dependencies = {}
        self.names = (self.label or self.name,)
        if self.socket_type not in [None, 'CUSTOM']:
            from .node_info import NodeInfo
            self.class_name = NodeInfo.socket_class_name(self.socket_type, self.name)
        else:
            self.class_name = ""
        self.is_attribute = self.socket_type in ATTR_SOCKETS
 
        self.default_value = getattr(bsocket, 'default_value', None)
        prop = bsocket.bl_rna.properties.get('default_value')
        if prop is not None and prop.type in {'BOOLEAN', 'INT', 'FLOAT'} and prop.is_array:
            value = self.default_value
            self.default_value = value.copy() if hasattr(value, 'copy') else tuple(value)

        self.enums = None
        if self.socket_type == 'MENU' and not self.is_output and prop is not None:
            self.enums = self.get_enum_list(bsocket)

    def __str__(self):
        enums = f" {self.enums}" if self.enums is not None else ""
        return f"<Socket {self.identifier} {self.name} {self.socket_type}{enums}>"

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
