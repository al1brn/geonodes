import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Color

class Color(dsock.Color):
    """ Class Color
    

    | Inherits from: dsock.Color 
    

    Constructors
    ============
    - Combine : CombineRgb image (Color) 
    

    Properties
    ==========
    - separate : SeparateRgb Sockets      [r (Float), g (Float), b (Float)] 
    

    Methods
    =======
    - add                : Mix color (Color) 
    - brighter           : Compare result (Boolean) 
    - burn               : Mix color (Color) 
    - capture_attribute  : CaptureAttribute Sockets      [geometry (Geometry), attribute (Color)] 
    - darken             : Mix color (Color) 
    - darker             : Compare result (Boolean) 
    - difference         : Mix color (Color) 
    - divide             : Mix color (Color) 
    - dodge              : Mix color (Color) 
    - equal              : Compare result (Boolean) 
    - field_at_index     : FieldAtIndex value (Color) 
    - hue                : Mix color (Color) 
    - lighten            : Mix color (Color) 
    - linear_light       : Mix color (Color) 
    - mix                : Mix color (Color) 
    - mix                : Mix color (Color) 
    - mix_color          : Mix color (Color) 
    - multiply           : Mix color (Color) 
    - not_equal          : Compare result (Boolean) 
    - overlay            : Mix color (Color) 
    - raycast            : Raycast Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance
      (Float), attribute (Color)] 
    - saturation         : Mix color (Color) 
    - screen             : Mix color (Color) 
    - soft_light         : Mix color (Color) 
    - subtract           : Mix color (Color) 
    - transfer_attribute : TransferAttribute attribute (Color) 
    - value              : Mix color (Color) 
    

    Stacked methods
    ===============
    - curves : RgbCurves Color 
    """


    def reset_properties(self):
        self.separate_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, r=None, g=None, b=None):
        """ Combine
        

        | Node: CombineRgb 
        

            v = Color.Combine(r, g, b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - r : Float 
            - g : Float 
            - b : Float 
        

        Node creation
        =============
        

            node = nodes.CombineRgb(r=r, g=g, b=b) 
        

        Returns
        =======
                Color 
        """

        return cls(nodes.CombineRgb(r=r, g=g, b=b).image)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ separate
        

        | Node: SeparateRgb 
        

            v = color.separate 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - image : Color (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.separate" 
        

        Node creation
        =============
        

            node = nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate") 
        

        Returns
        =======
                Sockets [r (Float), g (Float), b (Float)] 
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
        return self.separate_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_attribute
        

        | Node: TransferAttribute 
        

            v = color.transfer_attribute(source, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Color (self) 
            - source          : Geometry 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_COLOR' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index,
            data_type='FLOAT_COLOR', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Color 
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ capture_attribute
        

        | Node: CaptureAttribute 
        

            v = color.capture_attribute(geometry, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value    : Color (self) 
            - geometry : Geometry 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_COLOR' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain) 
        

        Returns
        =======
                Sockets [geometry (Geometry), attribute (Color)] 
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """ field_at_index
        

        | Node: FieldAtIndex 
        

            v = color.field_at_index(index, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value : Color (self) 
            - index : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_COLOR' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain) 
        

        Returns
        =======
                Color 
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ raycast
        

        | Node: Raycast 
        

            v = color.raycast(target_geometry, source_position, ray_direction, ray_length, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Color (self) 
            - target_geometry : Geometry 
            - source_position : Vector 
            - ray_direction   : Vector 
            - ray_length      : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_COLOR' 
        

            Parameters arguments
            --------------------
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST] 
        

        Node creation
        =============
        

            node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position,
            ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping) 
        

        Returns
        =======
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute
                (Color)] 
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping)

    def equal(self, b=None, epsilon=None):
        """ equal
        

        | Node: Compare 
        

            v = color.equal(b, epsilon) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a       : Color (self) 
            - b       : Color 
            - epsilon : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'RGBA' 
            - mode      : 'ELEMENT' 
            - operation : 'EQUAL' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL').result

    def not_equal(self, b=None, epsilon=None):
        """ not_equal
        

        | Node: Compare 
        

            v = color.not_equal(b, epsilon) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a       : Color (self) 
            - b       : Color 
            - epsilon : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'RGBA' 
            - mode      : 'ELEMENT' 
            - operation : 'NOT_EQUAL' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL').result

    def brighter(self, b=None):
        """ brighter
        

        | Node: Compare 
        

            v = color.brighter(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Color (self) 
            - b : Color 
        

            Fixed parameters
            ----------------
            - data_type : 'RGBA' 
            - mode      : 'ELEMENT' 
            - operation : 'BRIGHTER' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER').result

    def darker(self, b=None):
        """ darker
        

        | Node: Compare 
        

            v = color.darker(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Color (self) 
            - b : Color 
        

            Fixed parameters
            ----------------
            - data_type : 'RGBA' 
            - mode      : 'ELEMENT' 
            - operation : 'DARKER' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER').result

    def mix(self, color2=None, fac=None, use_alpha=False):
        """ mix
        

        | Node: Mix 
        

            v = color.mix(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'MIX' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha).color

    def darken(self, color2=None, fac=None, use_alpha=False):
        """ darken
        

        | Node: Mix 
        

            v = color.darken(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'DARKEN' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha).color

    def multiply(self, color2=None, fac=None, use_alpha=False):
        """ multiply
        

        | Node: Mix 
        

            v = color.multiply(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'MULTIPLY' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha).color

    def burn(self, color2=None, fac=None, use_alpha=False):
        """ burn
        

        | Node: Mix 
        

            v = color.burn(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'BURN' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha).color

    def lighten(self, color2=None, fac=None, use_alpha=False):
        """ lighten
        

        | Node: Mix 
        

            v = color.lighten(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'LIGHTEN' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha).color

    def screen(self, color2=None, fac=None, use_alpha=False):
        """ screen
        

        | Node: Mix 
        

            v = color.screen(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'SCREEN' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha).color

    def dodge(self, color2=None, fac=None, use_alpha=False):
        """ dodge
        

        | Node: Mix 
        

            v = color.dodge(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'DODGE' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha).color

    def add(self, color2=None, fac=None, use_alpha=False):
        """ add
        

        | Node: Mix 
        

            v = color.add(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'ADD' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha).color

    def overlay(self, color2=None, fac=None, use_alpha=False):
        """ overlay
        

        | Node: Mix 
        

            v = color.overlay(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'OVERLAY' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha).color

    def soft_light(self, color2=None, fac=None, use_alpha=False):
        """ soft_light
        

        | Node: Mix 
        

            v = color.soft_light(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'SOFT_LIGHT' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha).color

    def linear_light(self, color2=None, fac=None, use_alpha=False):
        """ linear_light
        

        | Node: Mix 
        

            v = color.linear_light(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'LINEAR_LIGHT' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha)
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha).color

    def difference(self, color2=None, fac=None, use_alpha=False):
        """ difference
        

        | Node: Mix 
        

            v = color.difference(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'DIFFERENCE' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha).color

    def subtract(self, color2=None, fac=None, use_alpha=False):
        """ subtract
        

        | Node: Mix 
        

            v = color.subtract(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'SUBTRACT' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha).color

    def divide(self, color2=None, fac=None, use_alpha=False):
        """ divide
        

        | Node: Mix 
        

            v = color.divide(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'DIVIDE' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha).color

    def hue(self, color2=None, fac=None, use_alpha=False):
        """ hue
        

        | Node: Mix 
        

            v = color.hue(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'HUE' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha).color

    def saturation(self, color2=None, fac=None, use_alpha=False):
        """ saturation
        

        | Node: Mix 
        

            v = color.saturation(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'SATURATION' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha).color

    def mix_color(self, color2=None, fac=None, use_alpha=False):
        """ mix_color
        

        | Node: Mix 
        

            v = color.mix_color(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'COLOR' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha).color

    def value(self, color2=None, fac=None, use_alpha=False):
        """ value
        

        | Node: Mix 
        

            v = color.value(color2, fac, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Fixed parameters
            ----------------
            - blend_type : 'VALUE' 
        

            Parameters arguments
            --------------------
            - use_alpha : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha).color

    def mix(self, color2=None, fac=None, blend_type='MIX', use_alpha=False):
        """ mix
        

        | Node: Mix 
        

            v = color.mix(color2, fac, blend_type, use_alpha) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color1 : Color (self) 
            - color2 : Color 
            - fac    : Float 
        

            Parameters arguments
            --------------------
            - blend_type : 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE] 
            - use_alpha  : False 
        

        Node creation
        =============
        

            node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha) 
        

        Returns
        =======
                Color 
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha).color


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """ curves
        

        | Node: RgbCurves 
        

            color.curves(fac) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - color : Color (self) 
            - fac   : Float 
        

        Node creation
        =============
        

            node = nodes.RgbCurves(color=self, fac=fac) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.RgbCurves(color=self, fac=fac))


