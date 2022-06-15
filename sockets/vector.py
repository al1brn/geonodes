#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-15
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
from geonodes.core.domains import Domain
from geonodes import Point, Edge, Face, Corner, Curve

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Vector

class Vector(dsock.Vector):
    """ 

    Data socket Vector
    ------------------
        > Inherits from dsock.Vector
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - AlignToVector : rotation (Vector)
            - Combine : vector (Vector)
            - Random : value (Vector)
    

        Properties
        ----------
            - separate : Sockets      [x (Float), y (Float), z (Float)]
            - x : x (Float) = separate.x
            - y : y (Float) = separate.y
            - z : z (Float) = separate.z
    

        Methods
        -------
            - absolute : vector (Vector)
            - accumulate_field : Sockets      [leading (Vector), trailing (Vector), total (Vector)]
            - add : vector (Vector)
            - align_to_vector : rotation (Vector)
            - attribute_statistic : Sockets      [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
            - capture_attribute : Sockets      [geometry (Geometry), attribute (Vector)]
            - ceil : vector (Vector)
            - cos : vector (Vector)
            - cross : vector (Vector)
            - curves : vector (Vector)
            - distance : value (Float)
            - divide : vector (Vector)
            - dot : value (Float)
            - equal : result (Boolean)
            - faceforward : vector (Vector)
            - field_at_index : value (Vector)
            - floor : vector (Vector)
            - fraction : vector (Vector)
            - greater_equal : result (Boolean)
            - greater_than : result (Boolean)
            - length : value (Float)
            - less_equal : result (Boolean)
            - less_than : result (Boolean)
            - map_range : vector (Vector)
            - max : vector (Vector)
            - min : vector (Vector)
            - modulo : vector (Vector)
            - multiply : vector (Vector)
            - multiply_add : vector (Vector)
            - normalize : vector (Vector)
            - not_equal : result (Boolean)
            - project : vector (Vector)
            - raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
            - reflect : vector (Vector)
            - refract : vector (Vector)
            - rotate : vector (Vector)
            - rotate_euler : rotation (Vector)
            - scale : vector (Vector)
            - sin : vector (Vector)
            - snap : vector (Vector)
            - subtract : vector (Vector)
            - tan : vector (Vector)
            - transfer_attribute : attribute (Vector)
            - wrap : vector (Vector)
    """


    def reset_properties(self):

        super().reset_properties()

        self.separate_ = None

        self.x_ = None

        self.y_ = None

        self.z_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None, node_label = None, node_color = None):
        """ > Node: RandomValue
          
        <sub>go to: top index
        blender ref FunctionNodeRandomValue
        node ref Random Value </sub>
                                  
        ```python
        v = Vector.Random(min, max, ID, seed, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - min : Vector
            - max : Vector
            - ID : Integer
            - seed : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR', label=node_label, node_color=node_color).value)

    @classmethod
    def Combine(cls, x=None, y=None, z=None, node_label = None, node_color = None):
        """ > Node: CombineXyz
          
        <sub>go to: top index
        blender ref ShaderNodeCombineXYZ
        node ref Combine XYZ </sub>
                                  
        ```python
        v = Vector.Combine(x, y, z, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - x : Float
            - y : Float
            - z : Float## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CombineXyz(x=x, y=y, z=z, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return cls(nodes.CombineXyz(x=x, y=y, z=z, label=node_label, node_color=node_color).vector)

    @classmethod
    def AlignToVector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label = None, node_color = None):
        """ > Node: AlignEulerToVector
          
        <sub>go to: top index
        blender ref FunctionNodeAlignEulerToVector
        node ref Align Euler to Vector </sub>
                                  
        ```python
        v = Vector.AlignToVector(rotation, factor, vector, axis, pivot_axis, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - rotation : Vector
            - factor : Float
            - vector : Vector## Parameters
            - axis : 'X' in [X, Y, Z]
            - pivot_axis : 'AUTO' in [AUTO, X, Y, Z]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return cls(nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color).rotation)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ > Node: SeparateXyz
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateXYZ
        node ref Separate XYZ </sub>
                                  
        ```python
        v = vector.separate
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector (self)## Fixed parameters
            - label:f"{self.node_chain_label}.separate"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
            ```
    

        Returns
        -------
            Sockets [x (Float), y (Float), z (Float)]
            
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
        return self.separate_

    @property
    def x(self):
        """ > Node: SeparateXyz
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateXYZ
        node ref Separate XYZ </sub>
                                  
        ```python
        v = vector.x
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector (self)## Fixed parameters
            - label:f"{self.node_chain_label}.x"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.x")
            ```
    

        Returns
        -------
            Sockets [x (Float), y (Float), z (Float)]
            
        """

        return self.separate.x

    @x.setter
    def x(self, value):
        self.separate.x = value

    @property
    def y(self):
        """ > Node: SeparateXyz
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateXYZ
        node ref Separate XYZ </sub>
                                  
        ```python
        v = vector.y
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector (self)## Fixed parameters
            - label:f"{self.node_chain_label}.y"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.y")
            ```
    

        Returns
        -------
            Sockets [x (Float), y (Float), z (Float)]
            
        """

        return self.separate.y

    @y.setter
    def y(self, value):
        self.separate.y = value

    @property
    def z(self):
        """ > Node: SeparateXyz
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateXYZ
        node ref Separate XYZ </sub>
                                  
        ```python
        v = vector.z
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector (self)## Fixed parameters
            - label:f"{self.node_chain_label}.z"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.z")
            ```
    

        Returns
        -------
            Sockets [x (Float), y (Float), z (Float)]
            
        """

        return self.separate.z

    @z.setter
    def z(self, value):
        self.separate.z = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: AccumulateField
          
        <sub>go to: top index
        blender ref GeometryNodeAccumulateField
        node ref Accumulate Field </sub>
                                  
        ```python
        v = vector.accumulate_field(group_index, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Vector (self)
            - group_index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [leading (Vector), trailing (Vector), total (Vector)]
            
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)

    def attribute_statistic(self, geometry=None, selection=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: AttributeStatistic
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeStatistic
        node ref Attribute Statistic </sub>
                                  
        ```python
        v = vector.attribute_statistic(geometry, selection, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Vector (self)
            - geometry : Geometry
            - selection : Boolean## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
            
        """

        return nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = vector.transfer_attribute(source, source_position, index, domain, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Vector (self)
            - source : Geometry
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def capture_attribute(self, geometry=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
                                  
        ```python
        v = vector.capture_attribute(geometry, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Vector (self)
            - geometry : Geometry## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Vector)]
            
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, index=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: FieldAtIndex
          
        <sub>go to: top index
        blender ref GeometryNodeFieldAtIndex
        node ref Field at Index </sub>
                                  
        ```python
        v = vector.field_at_index(index, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Vector (self)
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label = None, node_color = None):
        """ > Node: Raycast
          
        <sub>go to: top index
        blender ref GeometryNodeRaycast
        node ref Raycast </sub>
                                  
        ```python
        v = vector.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Vector (self)
            - target_geometry : Geometry
            - source_position : Vector
            - ray_direction : Vector
            - ray_length : Float## Parameters
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
            
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping, label=node_label, node_color=node_color)

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR', node_label = None, node_color = None):
        """ > Node: MapRange
          
        <sub>go to: top index
        blender ref ShaderNodeMapRange
        node ref Map Range </sub>
                                  
        ```python
        v = vector.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector (self)
            - from_min : Vector
            - from_max : Vector
            - to_min : Vector
            - to_max : Vector## Parameters
            - clamp : True
            - interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type, label=node_label, node_color=node_color).vector

    def less_than(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = vector.less_than(b, c, angle, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Vector (self)
            - b : Vector
            - c : Float
            - angle : Float## Parameters
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'VECTOR'
            - operation : 'LESS_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN', label=node_label, node_color=node_color).result

    def less_equal(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = vector.less_equal(b, c, angle, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Vector (self)
            - b : Vector
            - c : Float
            - angle : Float## Parameters
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'VECTOR'
            - operation : 'LESS_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def greater_than(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = vector.greater_than(b, c, angle, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Vector (self)
            - b : Vector
            - c : Float
            - angle : Float## Parameters
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'VECTOR'
            - operation : 'GREATER_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def greater_equal(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = vector.greater_equal(b, c, angle, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Vector (self)
            - b : Vector
            - c : Float
            - angle : Float## Parameters
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'VECTOR'
            - operation : 'GREATER_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = vector.equal(b, c, angle, epsilon, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Vector (self)
            - b : Vector
            - c : Float
            - angle : Float
            - epsilon : Float## Parameters
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'VECTOR'
            - operation : 'EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL', label=node_label, node_color=node_color).result

    def not_equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = vector.not_equal(b, c, angle, epsilon, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Vector (self)
            - b : Vector
            - c : Float
            - angle : Float
            - epsilon : Float## Parameters
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'VECTOR'
            - operation : 'NOT_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def add(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.add(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ADD'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD', label=node_label, node_color=node_color).vector

    def subtract(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.subtract(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SUBTRACT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color).vector

    def multiply(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.multiply(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MULTIPLY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color).vector

    def divide(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.divide(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'DIVIDE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color).vector

    def multiply_add(self, vector1=None, vector2=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.multiply_add(vector1, vector2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector
            - vector2 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MULTIPLY_ADD'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).vector

    def cross(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.cross(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'CROSS_PRODUCT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color).vector

    def project(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.project(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'PROJECT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color).vector

    def reflect(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.reflect(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'REFLECT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color).vector

    def refract(self, vector1=None, scale=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.refract(vector1, scale, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector
            - scale : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'REFRACT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color).vector

    def faceforward(self, vector1=None, vector2=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.faceforward(vector1, vector2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector
            - vector2 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'FACEFORWARD'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color).vector

    def dot(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.dot(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'DOT_PRODUCT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color).value

    def distance(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.distance(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'DISTANCE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color).value

    def length(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.length(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'LENGTH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='LENGTH', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.VectorMath(vector0=self, operation='LENGTH', label=node_label, node_color=node_color).value

    def scale(self, scale=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.scale(scale, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - scale : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SCALE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, scale=scale, operation='SCALE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, scale=scale, operation='SCALE', label=node_label, node_color=node_color).vector

    def normalize(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.normalize(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'NORMALIZE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='NORMALIZE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='NORMALIZE', label=node_label, node_color=node_color).vector

    def absolute(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.absolute(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ABSOLUTE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='ABSOLUTE', label=node_label, node_color=node_color).vector

    def min(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.min(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MINIMUM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color).vector

    def max(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.max(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MAXIMUM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color).vector

    def floor(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.floor(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'FLOOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='FLOOR', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='FLOOR', label=node_label, node_color=node_color).vector

    def ceil(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.ceil(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'CEIL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='CEIL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='CEIL', label=node_label, node_color=node_color).vector

    def fraction(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.fraction(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'FRACTION'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='FRACTION', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='FRACTION', label=node_label, node_color=node_color).vector

    def modulo(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.modulo(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MODULO'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color).vector

    def wrap(self, vector1=None, vector2=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.wrap(vector1, vector2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector
            - vector2 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'WRAP'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color).vector

    def snap(self, vector1=None, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.snap(vector1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)
            - vector1 : Vector## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SNAP'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color).vector

    def sin(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.sin(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='SINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='SINE', label=node_label, node_color=node_color).vector

    def cos(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.cos(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'COSINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='COSINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='COSINE', label=node_label, node_color=node_color).vector

    def tan(self, node_label = None, node_color = None):
        """ > Node: VectorMath
          
        <sub>go to: top index
        blender ref ShaderNodeVectorMath
        node ref Vector Math </sub>
                                  
        ```python
        v = vector.tan(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector0 : Vector (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'TANGENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorMath(vector0=self, operation='TANGENT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorMath(vector0=self, operation='TANGENT', label=node_label, node_color=node_color).vector

    def curves(self, fac=None, node_label = None, node_color = None):
        """ > Node: VectorCurves
          
        <sub>go to: top index
        blender ref ShaderNodeVectorCurve
        node ref Vector Curves </sub>
                                  
        ```python
        v = vector.curves(fac, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector (self)
            - fac : Float## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorCurves(vector=self, fac=fac, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.stack(nodes.VectorCurves(vector=self, fac=fac, label=node_label, node_color=node_color))

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label = None, node_color = None):
        """ > Node: AlignEulerToVector
          
        <sub>go to: top index
        blender ref FunctionNodeAlignEulerToVector
        node ref Align Euler to Vector </sub>
                                  
        ```python
        v = vector.align_to_vector(factor, vector, axis, pivot_axis, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - rotation : Vector (self)
            - factor : Float
            - vector : Vector## Parameters
            - axis : 'X' in [X, Y, Z]
            - pivot_axis : 'AUTO' in [AUTO, X, Y, Z]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.stack(nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color))

    def rotate_euler(self, rotate_by=None, space='OBJECT', node_label = None, node_color = None):
        """ > Node: RotateEuler
          
        <sub>go to: top index
        blender ref FunctionNodeRotateEuler
        node ref Rotate Euler </sub>
                                  
        ```python
        v = vector.rotate_euler(rotate_by, space, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - rotation : Vector (self)
            - rotate_by : Vector## Parameters
            - space : 'OBJECT' in [OBJECT, LOCAL]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.stack(nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space, label=node_label, node_color=node_color))

    def rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label = None, node_color = None):
        """ > Node: VectorRotate
          
        <sub>go to: top index
        blender ref ShaderNodeVectorRotate
        node ref Vector Rotate </sub>
                                  
        ```python
        v = vector.rotate(center, axis, angle, rotation, invert, rotation_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector (self)
            - center : Vector
            - axis : Vector
            - angle : Float
            - rotation : Vector## Parameters
            - invert : False
            - rotation_type : 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type, label=node_label, node_color=node_color).vector


