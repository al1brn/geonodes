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

module : geonodes
------------------
- GeoNodes class

Methods which are independant of the tree type

created : 2024/07/21
"""

import bpy
import mathutils
import numpy as np

from geonodes.nodes.scripterror import NodeError
from geonodes.nodes import constants
from geonodes.nodes.tree import Tree
from geonodes.nodes.nodeclass import Node

# ====================================================================================================
# Tree

class GeoNodes(Tree):

    def __init__(self,  name, create=True, clear=True, clear_sockets=False, fake_user=False, is_group=False):
        """ Tree of Nodes.

        Arguments
        ---------
            - name (str) : Tree name
            - create (bool = True) : create the tree if it doesn't exist
            - clear (bool = False) : erase the existing nodes
            - clear_sockets(bool = False) : clear sockets (sockets user values are deleted)
            - is_group (bool = False) : initialize as a ground
            - prefix (str = None) : prefix to use in the name
        """

        super().__init__('GeometryNodeTree', name=name, create=create, clear=clear, clear_sockets=clear_sockets, fake_user=fake_user, is_group=is_group)

    # =============================================================================================================================
    # Input nodes

    def boolean(self, value=None):
        return Node('Boolean', boolean=value).boolean

    def color(self, value=None):
        return Node('Color', value=value).color

    def image(self, value=None):
        return Node('Image', image=value).image

    def integer(self, value=None):
        return Node('Integer', integer=value).integer

    def material(self, value=None):
        return Node('Material', material=value).material

    def rotation(self, value=None):
        return Node('Rotation', rotation_euler=value).rotation

    def string(self, value=None):
        return Node('String', string=value).string

    def value(self, value=None):
        node = Node('Value')
        if value is not None:
            node._bnode.outputs[0].default_value = value
        return node.value

    def float(self, value=None):
        return self.value(value)

    def vector(self, value=None):
        return Node('Vector', vector=value).vector

    @property
    def active_camera(self):
        return Node('ActiveCamera').active_camera

    @property
    def is_viewport(self):
        return Node('IsViewport').is_viewport

    @property
    def scene_time(self):
        return Node('SceneTime')

    @property
    def self_object(self):
        return Node('SelfObject').self_object

    def object_info(self, object=None, as_instance=None, transform_space=None):
        return Node('ObjectInfo', object=object, as_instance=as_instance, transform_space=transform_space)

    def collection_info(self, collection=None, separate_children=None, reset_children=None, transform_space=None):
        return Node('CollectionInfo', collection=collection, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space)

    def image_info(self, image=None, frame=None):
        return Node('ImageInfo', image=image, frame=frame)

    # =============================================================================================================================
    # Geometry

    # -----------------------------------------------------------------------------------------------------------------------------
    # Read

    @property
    def ID(self):
        return Node('ID').ID

    @property
    def index(self):
        return Node('Index').index

    def named_attribute(self, name=None, data_type=None):
        return Node('NamedAttribute', name=name, data_type=data_type)

    def named_float(self, name=None):
        return self.named_attribute(name, 'FLOAT')

    def named_int(self, name=None):
        return self.named_attribute(name, 'INT')

    def named_integer(self, name=None):
        return self.named_int(name)

    def named_vector(self, name=None):
        return self.named_attribute(name, 'FLOAT_VECTOR')

    def named_color(self, name=None):
        return self.named_attribute(name, 'FLOAT_COLOR')

    def named_bool(self, name=None):
        return self.named_attribute(name, 'BOOLEAN')

    def named_boolean(self, name=None):
        return self.named_bool(name)

    def named_quaternion(self, name=None):
        return self.named_attribute(name, 'QUATERNION')

    def named_matrix(self, name=None):
        return self.named_attribute(name, 'FLOAT4X4')

    @property
    def normal(self):
        return Node('Normal').normal

    @property
    def position(self):
        return Node('Position').position

    @property
    def radius(self):
        return Node('Radius').radius

    # =============================================================================================================================
    # Math operations
    def add(self, value=None, value_1=None, use_clamp=None):
        """ Math operation ADD

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='ADD').value

    def subtract(self, value=None, value_1=None, use_clamp=None):
        """ Math operation SUBTRACT

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='SUBTRACT').value

    def multiply(self, value=None, value_1=None, use_clamp=None):
        """ Math operation MULTIPLY

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MULTIPLY').value

    def divide(self, value=None, value_1=None, use_clamp=None):
        """ Math operation DIVIDE

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='DIVIDE').value

    def multiply_add(self, value=None, multiplier=None, addend=None, use_clamp=None):
        """ Math operation MULTIPLY_ADD

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - multiplier : multiplier
        - addend : addend

        Returns
        -------
        value
        """

        return Node('Math', value=value, multiplier=multiplier, addend=addend, use_clamp=use_clamp, operation='MULTIPLY_ADD').value

    def power(self, base=None, exponent=None, use_clamp=None):
        """ Math operation POWER

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - base : base
        - exponent : exponent

        Returns
        -------
        value
        """

        return Node('Math', base=base, exponent=exponent, use_clamp=use_clamp, operation='POWER').value

    def log(self, value=None, use_clamp=None):
        """ Math operation LOGARITHM

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='LOGARITHM').value

    def sqrt(self, value=None, use_clamp=None):
        """ Math operation SQRT

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='SQRT').value

    def inverse_sqrt(self, value=None, use_clamp=None):
        """ Math operation INVERSE_SQRT

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='INVERSE_SQRT').value

    def abs(self, value=None, use_clamp=None):
        """ Math operation ABSOLUTE

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='ABSOLUTE').value

    def exp(self, value=None, use_clamp=None):
        """ Math operation EXPONENT

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='EXPONENT').value

    def min(self, value=None, value_1=None, use_clamp=None):
        """ Math operation MINIMUM

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MINIMUM').value

    def max(self, value=None, value_1=None, use_clamp=None):
        """ Math operation MAXIMUM

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MAXIMUM').value

    def less_than(self, value=None, value_1=None, threshold=None, use_clamp=None):
        """ Math operation LESS_THAN

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1
        - threshold : threshold

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, threshold=threshold, use_clamp=use_clamp, operation='LESS_THAN').value

    def greater_than(self, value=None, value_1=None, threshold=None, use_clamp=None):
        """ Math operation GREATER_THAN

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1
        - threshold : threshold

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, threshold=threshold, use_clamp=use_clamp, operation='GREATER_THAN').value

    def sign(self, value=None, use_clamp=None):
        """ Math operation SIGN

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='SIGN').value

    def compare(self, value=None, value_1=None, epsilon=None, use_clamp=None):
        """ Math operation COMPARE

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1
        - epsilon : epsilon

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, epsilon=epsilon, use_clamp=use_clamp, operation='COMPARE').value

    def smooth_min(self, value=None, value_1=None, distance=None, use_clamp=None):
        """ Math operation SMOOTH_MIN

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1
        - distance : distance

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, distance=distance, use_clamp=use_clamp, operation='SMOOTH_MIN').value

    def smooth_max(self, value=None, value_1=None, distance=None, use_clamp=None):
        """ Math operation SMOOTH_MAX

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1
        - distance : distance

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, distance=distance, use_clamp=use_clamp, operation='SMOOTH_MAX').value

    def round(self, value=None, use_clamp=None):
        """ Math operation ROUND

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='ROUND').value

    def floor(self, value=None, use_clamp=None):
        """ Math operation FLOOR

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='FLOOR').value

    def ceil(self, value=None, use_clamp=None):
        """ Math operation CEIL

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='CEIL').value

    def trunc(self, value=None, use_clamp=None):
        """ Math operation TRUNC

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='TRUNC').value

    def fract(self, value=None, use_clamp=None):
        """ Math operation FRACT

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='FRACT').value

    def modulo(self, value=None, value_1=None, use_clamp=None):
        """ Math operation MODULO

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MODULO').value

    def floored_modulo(self, value=None, value_1=None, use_clamp=None):
        """ Math operation FLOORED_MODULO

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='FLOORED_MODULO').value

    def wrap(self, value=None, max=None, min=None, use_clamp=None):
        """ Math operation WRAP

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - max : max
        - min : min

        Returns
        -------
        value
        """

        return Node('Math', value=value, max=max, min=min, use_clamp=use_clamp, operation='WRAP').value

    def snap(self, value=None, increment=None, use_clamp=None):
        """ Math operation SNAP

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - increment : increment

        Returns
        -------
        value
        """

        return Node('Math', value=value, increment=increment, use_clamp=use_clamp, operation='SNAP').value

    def pingpong(self, value=None, scale=None, use_clamp=None):
        """ Math operation PINGPONG

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - scale : scale

        Returns
        -------
        value
        """

        return Node('Math', value=value, scale=scale, use_clamp=use_clamp, operation='PINGPONG').value

    def sin(self, value=None, use_clamp=None):
        """ Math operation SINE

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='SINE').value

    def cos(self, value=None, use_clamp=None):
        """ Math operation COSINE

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='COSINE').value

    def tan(self, value=None, use_clamp=None):
        """ Math operation TANGENT

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='TANGENT').value

    def asin(self, value=None, use_clamp=None):
        """ Math operation ARCSINE

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='ARCSINE').value

    def acos(self, value=None, use_clamp=None):
        """ Math operation ARCCOSINE

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='ARCCOSINE').value

    def atan(self, value=None, use_clamp=None):
        """ Math operation ARCTANGENT

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='ARCTANGENT').value

    def atan2(self, value=None, value_1=None, use_clamp=None):
        """ Math operation ARCTAN2

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value
        - value_1 : value_1

        Returns
        -------
        value
        """

        return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='ARCTAN2').value

    def sinh(self, value=None, use_clamp=None):
        """ Math operation SINH

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='SINH').value

    def cosh(self, value=None, use_clamp=None):
        """ Math operation COSH

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='COSH').value

    def tanh(self, value=None, use_clamp=None):
        """ Math operation TANH

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='TANH').value

    def radians(self, value=None, use_clamp=None):
        """ Math operation RADIANS

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='RADIANS').value

    def degrees(self, value=None, use_clamp=None):
        """ Math operation DEGREES

        Node 'Math' (ShaderNodeMath)

        Arguments
        ---------
        - value : value

        Returns
        -------
        value
        """

        return Node('Math', value=value, use_clamp=use_clamp, operation='DEGREES').value
