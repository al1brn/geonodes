import numpy as np

pi     = np.pi
tau    = 2*np.pi
halfpi = np.pi/2
d30    = np.pi/6
d45    = np.pi/4
d60    = np.pi/3
d90    = halfpi
d180   = pi
d270   = np.pi*1.5
d360   = tau

from .treeclass import Break, Layout, Node, Group, Tree
from .floatclass import Float
from .socketclass import String
from .vectorclass import Vector, Rotation
from .colorclass import Color
from .shaderclass import Shader
from .textures import Texture
from . import gnmath
from .staticclass_sn import StaticClass

from .scripterror import NodeError


class nd(StaticClass):

    @classmethod
    def sharp_face(cls, attribute_type='GEOMETRY'):
        """ Node 'Attribute' (ShaderNodeAttribute)
        - attribute_type in ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
        """
        return cls.attribute(attribute_name='sharp_face', attribute_type=attribute_type)

    @classmethod
    def uvmap(cls, attribute_type='GEOMETRY'):
        """ Node 'Attribute' (ShaderNodeAttribute)
        - attribute_type in ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
        """
        return cls.attribute(attribute_name='UVMap', attribute_type=attribute_type)

    @classmethod
    def position(cls, attribute_type='GEOMETRY'):
        """ Node 'Attribute' (ShaderNodeAttribute)
        - attribute_type in ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
        """
        return cls.attribute(attribute_name='position', attribute_type=attribute_type)


class ShaderNodes(Tree):
    def __init__(self, tree_name, clear=True, fake_user=False, is_group=False, prefix=None):

        super().__init__(tree_name, tree_type='ShaderNodeTree', clear=clear, fake_user=fake_user, is_group=is_group, prefix=prefix)

    # =============================================================================================================================
    # Input Node

    @property
    def input_node(self):
        if not self._is_group:
            raise NodeError(f"ShaderNodes '{self._material.name}' is not a group, it doesn't have an input node")
        return super().input_node

    # ====================================================================================================
    # Tree output

    @property
    def output_node(self):
        if self._is_group:
            return self.output_node

        for node in self._nodes:
            if node._bnode.bl_idname ==  'ShaderNodeOutputMaterial':
                return node
        return Node('ShaderNodeOutputMaterial')

    def get_output_node(self, target='ALL'):
        # target in ('ALL', 'EEVEE', 'CYCLES')

        for node in self._nodes:
            if node._bnode.bl_idname ==  'ShaderNodeOutputMaterial':
                if node._bnode.target == target:
                    return node
        return Node('ShaderNodeOutputMaterial', target=target)

    def set_surface(self, value, target='ALL'):
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Surface': value})

    def set_volume(self, value, target='ALL'):
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Volume': value})

    def set_displacement(self, value, target='ALL'):
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Displacement': value})

    def set_thickness(self, value, target='ALL'):
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Thickness': value})

    @property
    def surface(self):
        raise NodeError(f"Material 'surface' is write only")

    @surface.setter
    def surface(self, value):
        if isinstance(value, tuple):
            self.set_surface(value[0], target=value[1])
        else:
            self.set_surface(value)

    @property
    def volume(self):
        raise NodeError(f"Material 'volume' is write only")

    @volume.setter
    def volume(self, value):
        if isinstance(value, tuple):
            self.set_volume(value[0], target=value[1])
        else:
            self.set_volume(value)

    @property
    def displacement(self):
        raise NodeError(f"Material 'displacement' is write only")

    @displacement.setter
    def displacement(self, value):
        if isinstance(value, tuple):
            self.set_displacement(value[0], target=value[1])
        else:
            self.set_displacement(value)

    @property
    def thickness(self):
        raise NodeError(f"Material 'displacement' is write only")

    @thickness.setter
    def thickness(self, value):
        if isinstance(value, tuple):
            self.set_thickness(value[0], target=value[1])
        else:
            self.set_thickness(value)

    def aov_output(self, name=None, color=None, value=None):
        node = Node('AOV Output', {'Color': color, 'Value': value}, aov_name=name)
