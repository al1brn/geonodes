import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Integer

class Integer(dsock.Integer):
    """ 

    Data socket Integer
    -------------------
        > Inherits from dsock.Integer
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - Random : value (Integer)
    

        Methods
        -------
            - abs : value (Float)
            - accumulate_field : Sockets      [leading (Integer), trailing (Integer), total (Integer)]
            - add : value (Float)
            - arccos : value (Float)
            - arcsin : value (Float)
            - arctan : value (Float)
            - arctan2 : value (Float)
            - capture_attribute : Sockets      [geometry (Geometry), attribute (Integer)]
            - ceil : value (Float)
            - compare : value (Float)
            - cos : value (Float)
            - cosh : value (Float)
            - degrees : value (Float)
            - divide : value (Float)
            - equal : result (Boolean)
            - exp : value (Float)
            - field_at_index : value (Integer)
            - floor : value (Float)
            - fract : value (Float)
            - greater_equal : result (Boolean)
            - greater_than : result (Boolean)
            - greater_than : value (Float)
            - inverse_sqrt : value (Float)
            - less_equal : result (Boolean)
            - less_than : result (Boolean)
            - less_than : value (Float)
            - log : value (Float)
            - max : value (Float)
            - min : value (Float)
            - modulo : value (Float)
            - multiply : value (Float)
            - multiply_add : value (Float)
            - not_equal : result (Boolean)
            - pingpong : value (Float)
            - pow : value (Float)
            - radians : value (Float)
            - raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
            - round : value (Float)
            - sign : value (Float)
            - sin : value (Float)
            - sinh : value (Float)
            - smooth_max : value (Float)
            - smooth_min : value (Float)
            - snap : value (Float)
            - sqrt : value (Float)
            - subtract : value (Float)
            - switch : output (Integer)
            - tan : value (Float)
            - tanh : value (Float)
            - transfer_attribute : attribute (Integer)
            - trunc : value (Float)
            - wrap : value (Float)
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ > Node: RandomValue
          
        <sub>go to: top index
        blender ref FunctionNodeRandomValue
        node ref Random Value </sub>
                                  
        ```python
        v = Integer.Random(min, max, ID, seed)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - min : Integer
                    - max : Integer
                    - ID : Integer
                    - seed : Integer## Fixed parameters
                    - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT')
            ```
    

        Returns
        -------
            Integer
            
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ > Node: AccumulateField
          
        <sub>go to: top index
        blender ref GeometryNodeAccumulateField
        node ref Accumulate Field </sub>
                                  
        ```python
        v = integer.accumulate_field(group_index, domain)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value : Integer (self)
                    - group_index : Integer## Parameters
                    - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]## Fixed parameters
                    - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain)
            ```
    

        Returns
        -------
            Sockets [leading (Integer), trailing (Integer), total (Integer)]
            
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain)

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = integer.transfer_attribute(source, source_position, index, domain, mapping)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - attribute : Integer (self)
                    - source : Geometry
                    - source_position : Vector
                    - index : Integer## Parameters
                    - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                    - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]## Fixed parameters
                    - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping)
            ```
    

        Returns
        -------
            Integer
            
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
                                  
        ```python
        v = integer.capture_attribute(geometry, domain)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value : Integer (self)
                    - geometry : Geometry## Parameters
                    - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]## Fixed parameters
                    - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Integer)]
            
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain)

    def field_at_index(self, value=None, domain='POINT'):
        """ > Node: FieldAtIndex
          
        <sub>go to: top index
        blender ref GeometryNodeFieldAtIndex
        node ref Field at Index </sub>
                                  
        ```python
        v = integer.field_at_index(value, domain)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - index : Integer (self)
                    - value : Integer## Parameters
                    - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]## Fixed parameters
                    - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain)
            ```
    

        Returns
        -------
            Integer
            
        """

        return nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ > Node: Raycast
          
        <sub>go to: top index
        blender ref GeometryNodeRaycast
        node ref Raycast </sub>
                                  
        ```python
        v = integer.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - attribute : Integer (self)
                    - target_geometry : Geometry
                    - source_position : Vector
                    - ray_direction : Vector
                    - ray_length : Float## Parameters
                    - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]## Fixed parameters
                    - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping)
            ```
    

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
            
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping)

    def switch(self, switch0=None, true=None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = integer.switch(switch0, true)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - false : Integer (self)
                    - switch0 : Boolean
                    - true : Integer## Fixed parameters
                    - input_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch0=switch0, true=true, input_type='INT')
            ```
    

        Returns
        -------
            Integer
            
        """

        return nodes.Switch(false=self, switch0=switch0, true=true, input_type='INT').output

    def less_than(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.less_than(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Integer (self)
                    - b : Integer## Fixed parameters
                    - data_type : 'INT'
                    - mode : 'ELEMENT'
                    - operation : 'LESS_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN').result

    def less_equal(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.less_equal(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Integer (self)
                    - b : Integer## Fixed parameters
                    - data_type : 'INT'
                    - mode : 'ELEMENT'
                    - operation : 'LESS_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL').result

    def greater_than(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.greater_than(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Integer (self)
                    - b : Integer## Fixed parameters
                    - data_type : 'INT'
                    - mode : 'ELEMENT'
                    - operation : 'GREATER_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN').result

    def greater_equal(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.greater_equal(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Integer (self)
                    - b : Integer## Fixed parameters
                    - data_type : 'INT'
                    - mode : 'ELEMENT'
                    - operation : 'GREATER_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL').result

    def equal(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.equal(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Integer (self)
                    - b : Integer## Fixed parameters
                    - data_type : 'INT'
                    - mode : 'ELEMENT'
                    - operation : 'EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL').result

    def not_equal(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.not_equal(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Integer (self)
                    - b : Integer## Fixed parameters
                    - data_type : 'INT'
                    - mode : 'ELEMENT'
                    - operation : 'NOT_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL').result

    def add(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.add(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'ADD'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='ADD')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='ADD').value

    def subtract(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.subtract(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'SUBTRACT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='SUBTRACT')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='SUBTRACT').value

    def multiply(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.multiply(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'MULTIPLY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MULTIPLY')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MULTIPLY').value

    def divide(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.divide(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'DIVIDE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='DIVIDE')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='DIVIDE').value

    def multiply_add(self, value1=None, value2=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.multiply_add(value1, value2)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float
                    - value2 : Float## Fixed parameters
                    - operation : 'MULTIPLY_ADD'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

    def pow(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.pow(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'POWER'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='POWER')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='POWER').value

    def log(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.log(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'LOGARITHM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='LOGARITHM')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='LOGARITHM').value

    def sqrt(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sqrt()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'SQRT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SQRT')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SQRT').value

    def inverse_sqrt(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.inverse_sqrt()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'INVERSE_SQRT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='INVERSE_SQRT')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='INVERSE_SQRT').value

    def abs(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.abs()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'ABSOLUTE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ABSOLUTE')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ABSOLUTE').value

    def exp(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.exp()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'EXPONENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='EXPONENT')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='EXPONENT').value

    def min(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.min(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'MINIMUM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MINIMUM')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MINIMUM').value

    def max(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.max(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'MAXIMUM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MAXIMUM')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MAXIMUM').value

    def less_than(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.less_than(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'LESS_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='LESS_THAN')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='LESS_THAN').value

    def greater_than(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.greater_than(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'GREATER_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='GREATER_THAN')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='GREATER_THAN').value

    def sign(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sign()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'SIGN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SIGN')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SIGN').value

    def compare(self, value1=None, value2=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.compare(value1, value2)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float
                    - value2 : Float## Fixed parameters
                    - operation : 'COMPARE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE').value

    def smooth_min(self, value1=None, value2=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.smooth_min(value1, value2)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float
                    - value2 : Float## Fixed parameters
                    - operation : 'SMOOTH_MIN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN').value

    def smooth_max(self, value1=None, value2=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.smooth_max(value1, value2)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float
                    - value2 : Float## Fixed parameters
                    - operation : 'SMOOTH_MAX'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX').value

    def round(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.round()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'ROUND'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ROUND')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ROUND').value

    def floor(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.floor()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'FLOOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='FLOOR')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='FLOOR').value

    def ceil(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.ceil()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'CEIL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='CEIL')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='CEIL').value

    def trunc(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.trunc()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'TRUNC'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='TRUNC')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='TRUNC').value

    def fract(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.fract()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'FRACT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='FRACT')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='FRACT').value

    def modulo(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.modulo(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'MODULO'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MODULO')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MODULO').value

    def wrap(self, value1=None, value2=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.wrap(value1, value2)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float
                    - value2 : Float## Fixed parameters
                    - operation : 'WRAP'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP').value

    def snap(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.snap(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'SNAP'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='SNAP')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='SNAP').value

    def pingpong(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.pingpong(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'PINGPONG'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='PINGPONG')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='PINGPONG').value

    def sin(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sin()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'SINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SINE')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SINE').value

    def cos(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.cos()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'COSINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='COSINE')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='COSINE').value

    def tan(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.tan()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'TANGENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='TANGENT')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='TANGENT').value

    def arcsin(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arcsin()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'ARCSINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ARCSINE')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ARCSINE').value

    def arccos(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arccos()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'ARCCOSINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ARCCOSINE')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ARCCOSINE').value

    def arctan(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arctan()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'ARCTANGENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ARCTANGENT')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ARCTANGENT').value

    def arctan2(self, value1=None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arctan2(value1)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)
                    - value1 : Float## Fixed parameters
                    - operation : 'ARCTAN2'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='ARCTAN2')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='ARCTAN2').value

    def sinh(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sinh()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'SINH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SINH')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SINH').value

    def cosh(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.cosh()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'COSH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='COSH')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='COSH').value

    def tanh(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.tanh()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'TANH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='TANH')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='TANH').value

    def radians(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.radians()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'RADIANS'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='RADIANS')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='RADIANS').value

    def degrees(self):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.degrees()
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value0 : Float (self)## Fixed parameters
                    - operation : 'DEGREES'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='DEGREES')
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='DEGREES').value


