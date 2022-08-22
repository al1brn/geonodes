#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-21
@author: Generated from generator module
Blender version: 3.2.2
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Vector

class Vector(dsock.Vector):
    """ Data class Vector
    """

    def copy(self):

        return Vector(self)


    def reset_properties(self):

        super().reset_properties()

        self.separate_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None, node_label = None, node_color = None):
        """ Geometry node [*Random Value*].
        
        
            Args:
                min: Vector
                max: Vector
                ID: Integer
                seed: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RandomValue`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: FunctionNodeRandomValue
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR', label=node_label, node_color=node_color)
                
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR', label=node_label, node_color=node_color).value)

    @classmethod
    def Combine(cls, x=None, y=None, z=None, node_label = None, node_color = None):
        """ Geometry node [*Combine XYZ*].
        
        
            Args:
                x: Float
                y: Float
                z: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CombineXyz`
            
            
            .. blid:: ShaderNodeCombineXYZ
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CombineXyz(x=x, y=y, z=z, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.CombineXyz(x=x, y=y, z=z, label=node_label, node_color=node_color).vector)

    @classmethod
    def AlignToVector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label = None, node_color = None):
        """ Geometry node [*Align Euler to Vector*].
        
        
            Args:
                rotation: Vector
                factor: Float
                vector: Vector
                axis (str): 'X' in [X, Y, Z]
                pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.AlignEulerToVector`
            
            
            .. blid:: FunctionNodeAlignEulerToVector
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color).rotation)

    @classmethod
    def RotateEuler(cls, rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', type='EULER', node_label = None, node_color = None):
        """ Geometry node [*Rotate Euler*].
        
        
            Args:
                rotation: Vector
                rotate_by: Vector
                axis: Vector
                angle: Float
                space (str): 'OBJECT' in [OBJECT, LOCAL]
                type (str): 'EULER' in [AXIS_ANGLE, EULER]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RotateEuler`
            
            
            .. blid:: FunctionNodeRotateEuler
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RotateEuler(rotation=rotation, rotate_by=rotate_by, axis=axis, angle=angle, space=space, type=type, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.RotateEuler(rotation=rotation, rotate_by=rotate_by, axis=axis, angle=angle, space=space, type=type, label=node_label, node_color=node_color).rotation)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ Geometry node [*Separate XYZ*].
        
        
        
            Returns:
                Sockets [x (Float), y (Float), z (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateXyz`
            
            
            .. blid:: ShaderNodeSeparateXYZ
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
                
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
        return self.separate_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Accumulate Field*].
        
        
            Args:
                group_index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [leading (Vector), trailing (Vector), total (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.AccumulateField`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: GeometryNodeAccumulateField
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)

    def attribute_statistic(self, geometry=None, selection=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Attribute Statistic*].
        
        
            Args:
                geometry: Geometry
                selection: Boolean
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.AttributeStatistic`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: GeometryNodeAttributeStatistic
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)

    def capture_attribute(self, geometry=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Capture Attribute*].
        
        
            Args:
                geometry: Geometry
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), attribute (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: GeometryNodeCaptureAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, index=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Field at Index*].
        
        
            Args:
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: GeometryNodeFieldAtIndex
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label = None, node_color = None):
        """ Geometry node [*Raycast*].
        
        
            Args:
                target_geometry: Geometry
                source_position: Vector
                ray_direction: Vector
                ray_length: Float
                mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Raycast`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: GeometryNodeRaycast
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping, label=node_label, node_color=node_color)

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'VECTOR'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='VECTOR', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='VECTOR', label=node_label, node_color=node_color).output

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR', node_label = None, node_color = None):
        """ Geometry node [*Map Range*].
        
        
            Args:
                from_min: Vector
                from_max: Vector
                to_min: Vector
                to_max: Vector
                clamp (bool): True
                interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MapRange`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: ShaderNodeMapRange
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type, label=node_label, node_color=node_color)
                
        """

        return nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type, label=node_label, node_color=node_color).vector

    def less_than(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                angle: Float
                mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - operation = 'LESS_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN', label=node_label, node_color=node_color).result

    def less_equal(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                angle: Float
                mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - operation = 'LESS_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def greater_than(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                angle: Float
                mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - operation = 'GREATER_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def greater_equal(self, b=None, c=None, angle=None, mode='ELEMENT', node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                angle: Float
                mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - operation = 'GREATER_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                angle: Float
                epsilon: Float
                mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL', label=node_label, node_color=node_color).result

    def not_equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                angle: Float
                epsilon: Float
                mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def element_less_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'ELEMENT'
                - operation = 'LESS_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def length_less_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'LENGTH'
                - operation = 'LESS_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def average_less_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'AVERAGE'
                - operation = 'LESS_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def dot_product_less_than(self, b=None, c=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DOT_PRODUCT'
                - operation = 'LESS_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def direction_less_than(self, b=None, angle=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                angle: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DIRECTION'
                - operation = 'LESS_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def element_less_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'ELEMENT'
                - operation = 'LESS_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def length_less_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'LENGTH'
                - operation = 'LESS_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='LESS_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def average_less_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'AVERAGE'
                - operation = 'LESS_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='LESS_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def dot_product_less_equal(self, b=None, c=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DOT_PRODUCT'
                - operation = 'LESS_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def direction_less_equal(self, b=None, angle=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                angle: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DIRECTION'
                - operation = 'LESS_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='LESS_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def element_greater_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'ELEMENT'
                - operation = 'GREATER_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def length_greater_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'LENGTH'
                - operation = 'GREATER_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def average_greater_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'AVERAGE'
                - operation = 'GREATER_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def dot_product_greater_than(self, b=None, c=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DOT_PRODUCT'
                - operation = 'GREATER_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def direction_greater_than(self, b=None, angle=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                angle: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DIRECTION'
                - operation = 'GREATER_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def element_greater_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'ELEMENT'
                - operation = 'GREATER_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def length_greater_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'LENGTH'
                - operation = 'GREATER_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def average_greater_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'AVERAGE'
                - operation = 'GREATER_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def dot_product_greater_equal(self, b=None, c=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DOT_PRODUCT'
                - operation = 'GREATER_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def direction_greater_equal(self, b=None, angle=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                angle: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DIRECTION'
                - operation = 'GREATER_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def element_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'ELEMENT'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color).result

    def length_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'LENGTH'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='EQUAL', label=node_label, node_color=node_color).result

    def average_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'AVERAGE'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='EQUAL', label=node_label, node_color=node_color).result

    def dot_product_equal(self, b=None, c=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DOT_PRODUCT'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='EQUAL', label=node_label, node_color=node_color).result

    def direction_equal(self, b=None, angle=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                angle: Float
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DIRECTION'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='EQUAL', label=node_label, node_color=node_color).result

    def element_not_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'ELEMENT'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def length_not_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'LENGTH'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def average_not_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'AVERAGE'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def dot_product_not_equal(self, b=None, c=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                c: Float
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DOT_PRODUCT'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, c=c, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, c=c, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def direction_not_equal(self, b=None, angle=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Vector
                angle: Float
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'VECTOR'
                - mode = 'DIRECTION'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def add(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'ADD'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD', label=node_label, node_color=node_color).vector

    def subtract(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'SUBTRACT'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color).vector

    def multiply(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'MULTIPLY'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color).vector

    def divide(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'DIVIDE'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color).vector

    def multiply_add(self, vector1=None, vector2=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                vector2: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'MULTIPLY_ADD'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).vector

    def cross(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'CROSS_PRODUCT'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color).vector

    def project(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'PROJECT'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color).vector

    def reflect(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'REFLECT'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color).vector

    def refract(self, vector1=None, scale=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                scale: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'REFRACT'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color).vector

    def faceforward(self, vector1=None, vector2=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                vector2: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'FACEFORWARD'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color).vector

    def dot(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'DOT_PRODUCT'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color).value

    def distance(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'DISTANCE'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color).value

    def length(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'LENGTH'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='LENGTH', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='LENGTH', label=node_label, node_color=node_color).value

    def scale(self, scale=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                scale: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'SCALE'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, scale=scale, operation='SCALE', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, scale=scale, operation='SCALE', label=node_label, node_color=node_color).vector

    def normalize(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'NORMALIZE'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='NORMALIZE', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='NORMALIZE', label=node_label, node_color=node_color).vector

    def absolute(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'ABSOLUTE'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='ABSOLUTE', label=node_label, node_color=node_color).vector

    def min(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'MINIMUM'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color).vector

    def max(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'MAXIMUM'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color).vector

    def floor(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'FLOOR'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='FLOOR', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='FLOOR', label=node_label, node_color=node_color).vector

    def ceil(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'CEIL'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='CEIL', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='CEIL', label=node_label, node_color=node_color).vector

    def fraction(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'FRACTION'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='FRACTION', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='FRACTION', label=node_label, node_color=node_color).vector

    def modulo(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'MODULO'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color).vector

    def wrap(self, vector1=None, vector2=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                vector2: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'WRAP'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color).vector

    def snap(self, vector1=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                vector1: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'SNAP'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color).vector

    def sin(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'SINE'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='SINE', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='SINE', label=node_label, node_color=node_color).vector

    def cos(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'COSINE'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='COSINE', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='COSINE', label=node_label, node_color=node_color).vector

    def tan(self, node_label = None, node_color = None):
        """ Geometry node [*Vector Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorMath`
            
                - operation = 'TANGENT'
                  
            .. blid:: ShaderNodeVectorMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorMath(vector0=self, operation='TANGENT', label=node_label, node_color=node_color)
                
        """

        return nodes.VectorMath(vector0=self, operation='TANGENT', label=node_label, node_color=node_color).vector

    def curves(self, fac=None, node_label = None, node_color = None):
        """ Geometry node [*Vector Curves*].
        
        
            Args:
                fac: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorCurves`
            
            
            .. blid:: ShaderNodeVectorCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorCurves(vector=self, fac=fac, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.VectorCurves(vector=self, fac=fac, label=node_label, node_color=node_color))

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label = None, node_color = None):
        """ Geometry node [*Align Euler to Vector*].
        
        
            Args:
                factor: Float
                vector: Vector
                axis (str): 'X' in [X, Y, Z]
                pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.AlignEulerToVector`
            
            
            .. blid:: FunctionNodeAlignEulerToVector
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color))

    def rotate_euler(self, rotate_by=None, axis=None, angle=None, space='OBJECT', type='EULER', node_label = None, node_color = None):
        """ Geometry node [*Rotate Euler*].
        
        
            Args:
                rotate_by: Vector
                axis: Vector
                angle: Float
                space (str): 'OBJECT' in [OBJECT, LOCAL]
                type (str): 'EULER' in [AXIS_ANGLE, EULER]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RotateEuler`
            
            
            .. blid:: FunctionNodeRotateEuler
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, space=space, type=type, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.RotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, space=space, type=type, label=node_label, node_color=node_color))

    def rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label = None, node_color = None):
        """ Geometry node [*Vector Rotate*].
        
        
            Args:
                center: Vector
                axis: Vector
                angle: Float
                rotation: Vector
                invert (bool): False
                rotation_type (str): 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VectorRotate`
            
            
            .. blid:: ShaderNodeVectorRotate
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type, label=node_label, node_color=node_color)
                
        """

        return nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type, label=node_label, node_color=node_color).vector


