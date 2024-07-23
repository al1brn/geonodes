#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : objectclass
------------------
- Object Class

created : 2024/07/21
"""

from geonodes.nodes.socketclass import Socket
from geonodes.nodes.nodeclass import Node
from geonodes.nodes import nodeclasses

class Float(Socket):
    pass

class Integer(Socket):
    pass

class Boolean(Socket):
    pass

class Vector(Socket):
    pass

class Rotation(Socket):
    pass

class String(Socket):
    pass

class Color(Socket):
    pass

class Shader(Socket):
    pass

class Object(Socket):
    def info(self, as_instance=None, transform_space=None):
        return Node('ObjectInfo', object=self, as_instance=as_instance, transform_space=transform_space)

class Image(Socket):
    def info(self, frame=None):
        return Node('ImageInfo', image=self, frame=frame)

class Geometry(Socket):

    @staticmethod
    def get_data_type(value):

        DATA_TYPES = {
            'VALUE'      : 'FLOAT',
            'INT'        : 'INT',
            'BOOLEAN'    : 'BOOLEAN',
            'VECTOR'     : 'FLOAT_VECTOR',
            'ROTATION'   : 'FLOAT_VECTOR',
            'RGBA'       : 'FLOAT_COLOR',
            'QUATERNION' : 'QUATERNION',
            'MATRIX'     : 'FLOAT4X4'}

        if value is None:
            return None

        elif hasattr(value, '_bsocket'):
            if value._bsocket.type in DATA_TYPES.keys():
                return DATA_TYPES[value._bsocket.type]
            else:
                return None

        elif isinstance(value, int):
            return 'INT'

        elif isinstance(value, float):
            return 'FLOAT'

        else:
            return None

    # ----------------------------------------------------------------------------------------------------
    # Sample

    def proximity(self, group_id=None, sample_position=None, sample_group_id=None, target_element=None):
        return Node('GeometryProximity', geometry=self, group_id=group_id, sample_position=sample_position, sample_group_id=sample_group_id, target_element=target_element)

    def point_proximity(self, group_id=None, sample_position=None, sample_group_id=None):
        return self.proximity(group_id=group_id, sample_position=sample_position, sample_group_id=sample_group_id, target_element='POINTS')

    def edge_proximity(self, group_id=None, sample_position=None, sample_group_id=None):
        return self.proximity(group_id=group_id, sample_position=sample_position, sample_group_id=sample_group_id, target_element='EDGES')

    def face_proximity(self, group_id=None, sample_position=None, sample_group_id=None):
        return self.proximity(group_id=group_id, sample_position=sample_position, sample_group_id=sample_group_id, target_element='FACES')

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type=None, mapping=None):
        if data_type is None:
            data_type = Geometry.get_data_type(attribute)
        return Node('GeometryNodeRaycast', target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length,
            data_type=data_type, mapping=mapping)

    def sample_index(self, value=None, index=None, data_type=None, domain=None, clamp=None):
        if data_type is None:
            data_type = Geometry.get_data_type(value)
        return Node('GeometryNodeSampleIndex', geometry=self, value=value, index=index, data_type=data_type, domain=domain, clamp=clamp)

    def point_sample_index(self, value=None, index=None, data_type=None, clamp=None):
        return Node('GeometryNodeSampleIndex', geometry=self, value=value, index=index, data_type=data_type, domain='POINT', clamp=clamp)

    def edge_sample_index(self, value=None, index=None, data_type=None, clamp=None):
        return Node('GeometryNodeSampleIndex', geometry=self, value=value, index=index, data_type=data_type, domain='EDGE', clamp=clamp)

    def face_sample_index(self, value=None, index=None, data_type=None, clamp=None):
        return Node('GeometryNodeSampleIndex', geometry=self, value=value, index=index, data_type=data_type, domain='FACE', clamp=clamp)

    def corner_sample_index(self, value=None, index=None, data_type=None, clamp=None):
        return Node('GeometryNodeSampleIndex', geometry=self, value=value, index=index, data_type=data_type, domain='CORNER', clamp=clamp)

    def curve_sample_index(self, value=None, index=None, data_type=None, clamp=None):
        return Node('GeometryNodeSampleIndex', geometry=self, value=value, index=index, data_type=data_type, domain='CURVE', clamp=clamp)

    def instance_sample_index(self, value=None, index=None, data_type=None, clamp=None):
        return Node('GeometryNodeSampleIndex', geometry=self, value=value, index=index, data_type=data_type, domain='INSTANCE', clamp=clamp)





"""
    'IndexOfNearest' : {
        'blid' : 'GeometryNodeIndexOfNearest',
        'prms' : {},
        'inss' : {'position' : 0, 'group_id' : 1},
        'outs' : {'index' : 0, 'has_neighbor' : 1},
    },

    'SampleNearest' : {
        'blid' : 'GeometryNodeSampleNearest',
        'prms' : {'domain' : ('POINT', 'EDGE', 'FACE', 'CORNER')},
        'inss' : {'geometry' : 0, 'sample_position' : 1},
        'outs' : {'index' : 0},
    },
"""


class Collection(Socket):
    pass

class Texture(Socket):
    pass

class Material(Socket):
    pass

class Menu(Socket):
    pass

class Matrix(Socket):
    pass
