import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Color

class Color(dsock.Color):
    """ 

    Data socket Color
    -----------------
        > Inherits from dsock.Color
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - Combine : image (Color)
    

        Properties
        ----------
            - b : b (Float) = separate.b
            - g : g (Float) = separate.g
            - r : r (Float) = separate.r
            - separate : Sockets      [r (Float), g (Float), b (Float)]
    

        Methods
        -------
            - add : color (Color)
            - brighter : result (Boolean)
            - burn : color (Color)
            - capture_attribute : Sockets      [geometry (Geometry), attribute (Color)]
            - curves : color (Color)
            - darken : color (Color)
            - darker : result (Boolean)
            - difference : color (Color)
            - divide : color (Color)
            - dodge : color (Color)
            - equal : result (Boolean)
            - field_at_index : value (Color)
            - hue : color (Color)
            - lighten : color (Color)
            - linear_light : color (Color)
            - mix : color (Color)
            - mix : color (Color)
            - mix_color : color (Color)
            - multiply : color (Color)
            - not_equal : result (Boolean)
            - overlay : color (Color)
            - raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
            - saturation : color (Color)
            - screen : color (Color)
            - soft_light : color (Color)
            - subtract : color (Color)
            - transfer_attribute : attribute (Color)
            - value : color (Color)
    """


    def reset_properties(self):
        self.separate_ = None
        self.r_ = None
        self.g_ = None
        self.b_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, r=None, g=None, b=None):
        """ > Node: CombineRgb
          
        <sub>go to: top index
        blender ref ShaderNodeCombineRGB
        node ref Combine RGB </sub>
        ```python
        v = Color.Combine(r, g, b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - r : Float
                    - g : Float
                    - b : Float
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.CombineRgb(r=r, g=g, b=b)
                        ```
    

        Returns
        -------
            Color
            
        """

        return cls(nodes.CombineRgb(r=r, g=g, b=b).image)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ > Node: SeparateRgb
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateRGB
        node ref Separate RGB </sub>
        ```python
        v = color.separate
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - image : Color (self)## Fixed parameters
                    - label:f"{self.node_chain_label}.separate"
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
                        ```
    

        Returns
        -------
            Sockets [r (Float), g (Float), b (Float)]
            
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
        return self.separate_

    @property
    def r(self):
        """ > Node: SeparateRgb
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateRGB
        node ref Separate RGB </sub>
        ```python
        v = color.r
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - image : Color (self)## Fixed parameters
                    - label:f"{self.node_chain_label}.r"
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.r")
                        ```
    

        Returns
        -------
            Sockets [r (Float), g (Float), b (Float)]
            
        """

        return self.separate.r

    @r.setter
    def r(self, value):
        self.separate.r = value

    @property
    def g(self):
        """ > Node: SeparateRgb
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateRGB
        node ref Separate RGB </sub>
        ```python
        v = color.g
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - image : Color (self)## Fixed parameters
                    - label:f"{self.node_chain_label}.g"
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.g")
                        ```
    

        Returns
        -------
            Sockets [r (Float), g (Float), b (Float)]
            
        """

        return self.separate.g

    @g.setter
    def g(self, value):
        self.separate.g = value

    @property
    def b(self):
        """ > Node: SeparateRgb
          
        <sub>go to: top index
        blender ref ShaderNodeSeparateRGB
        node ref Separate RGB </sub>
        ```python
        v = color.b
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - image : Color (self)## Fixed parameters
                    - label:f"{self.node_chain_label}.b"
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.b")
                        ```
    

        Returns
        -------
            Sockets [r (Float), g (Float), b (Float)]
            
        """

        return self.separate.b

    @b.setter
    def b(self, value):
        self.separate.b = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
        ```python
        v = color.transfer_attribute(source, source_position, index, domain, mapping)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - attribute : Color (self)
                    - source : Geometry
                    - source_position : Vector
                    - index : Integer## Parameters
                    - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                    - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]## Fixed parameters
                    - data_type : 'FLOAT_COLOR'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
        ```python
        v = color.capture_attribute(geometry, domain)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value : Color (self)
                    - geometry : Geometry## Parameters
                    - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]## Fixed parameters
                    - data_type : 'FLOAT_COLOR'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain)
                        ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Color)]
            
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """ > Node: FieldAtIndex
          
        <sub>go to: top index
        blender ref GeometryNodeFieldAtIndex
        node ref Field at Index </sub>
        ```python
        v = color.field_at_index(index, domain)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - value : Color (self)
                    - index : Integer## Parameters
                    - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]## Fixed parameters
                    - data_type : 'FLOAT_COLOR'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ > Node: Raycast
          
        <sub>go to: top index
        blender ref GeometryNodeRaycast
        node ref Raycast </sub>
        ```python
        v = color.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - attribute : Color (self)
                    - target_geometry : Geometry
                    - source_position : Vector
                    - ray_direction : Vector
                    - ray_length : Float## Parameters
                    - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]## Fixed parameters
                    - data_type : 'FLOAT_COLOR'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping)
                        ```
    

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
            
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping)

    def equal(self, b=None, epsilon=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        ```python
        v = color.equal(b, epsilon)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Color (self)
                    - b : Color
                    - epsilon : Float## Fixed parameters
                    - data_type : 'RGBA'
                    - mode : 'ELEMENT'
                    - operation : 'EQUAL'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL')
                        ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL').result

    def not_equal(self, b=None, epsilon=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        ```python
        v = color.not_equal(b, epsilon)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Color (self)
                    - b : Color
                    - epsilon : Float## Fixed parameters
                    - data_type : 'RGBA'
                    - mode : 'ELEMENT'
                    - operation : 'NOT_EQUAL'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL')
                        ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL').result

    def brighter(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        ```python
        v = color.brighter(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Color (self)
                    - b : Color## Fixed parameters
                    - data_type : 'RGBA'
                    - mode : 'ELEMENT'
                    - operation : 'BRIGHTER'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER')
                        ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER').result

    def darker(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        ```python
        v = color.darker(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : Color (self)
                    - b : Color## Fixed parameters
                    - data_type : 'RGBA'
                    - mode : 'ELEMENT'
                    - operation : 'DARKER'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER')
                        ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER').result

    def mix(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.mix(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'MIX'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha).color

    def darken(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.darken(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'DARKEN'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha).color

    def multiply(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.multiply(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'MULTIPLY'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha).color

    def burn(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.burn(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'BURN'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha).color

    def lighten(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.lighten(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'LIGHTEN'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha).color

    def screen(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.screen(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'SCREEN'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha).color

    def dodge(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.dodge(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'DODGE'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha).color

    def add(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.add(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'ADD'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha).color

    def overlay(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.overlay(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'OVERLAY'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha).color

    def soft_light(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.soft_light(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'SOFT_LIGHT'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha).color

    def linear_light(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.linear_light(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'LINEAR_LIGHT'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha).color

    def difference(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.difference(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'DIFFERENCE'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha).color

    def subtract(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.subtract(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'SUBTRACT'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha).color

    def divide(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.divide(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'DIVIDE'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha).color

    def hue(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.hue(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'HUE'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha).color

    def saturation(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.saturation(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'SATURATION'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha).color

    def mix_color(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.mix_color(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'COLOR'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha).color

    def value(self, color2=None, fac=None, use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.value(color2, fac, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - use_alpha : False## Fixed parameters
                    - blend_type : 'VALUE'
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha).color

    def curves(self, fac=None):
        """ > Node: RgbCurves
          
        <sub>go to: top index
        blender ref ShaderNodeRGBCurve
        node ref RGB Curves </sub>
        ```python
        v = color.curves(fac)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color : Color (self)
                    - fac : Float
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.RgbCurves(color=self, fac=fac)
                        ```
    

        Returns
        -------
            Color
            
        """

        return self.stack(nodes.RgbCurves(color=self, fac=fac))

    def mix(self, color2=None, fac=None, blend_type='MIX', use_alpha=False):
        """ > Node: Mix
          
        <sub>go to: top index
        blender ref ShaderNodeMixRGB
        node ref Mix </sub>
        ```python
        v = color.mix(color2, fac, blend_type, use_alpha)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - color1 : Color (self)
                    - color2 : Color
                    - fac : Float## Parameters
                    - blend_type : 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
                    - use_alpha : False
                      
                        Node creation
                        -------------
                        ```python
                        from geondes import nodes
                        nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha)
                        ```
    

        Returns
        -------
            Color
            
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha).color


