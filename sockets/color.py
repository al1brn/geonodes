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
    - Combine : image (Color) 
    

    Properties
    ==========
    - separate : Sockets      [r (Float), g (Float), b (Float)] 
    

    Methods
    =======
    - add                : color (Color) 
    - brighter           : result (Boolean) 
    - burn               : color (Color) 
    - capture_attribute  : Sockets      [geometry (Geometry), attribute (Color)] 
    - darken             : color (Color) 
    - darker             : result (Boolean) 
    - difference         : color (Color) 
    - divide             : color (Color) 
    - dodge              : color (Color) 
    - equal              : result (Boolean) 
    - field_at_index     : value (Color) 
    - hue                : color (Color) 
    - lighten            : color (Color) 
    - linear_light       : color (Color) 
    - mix                : color (Color) 
    - mix                : color (Color) 
    - mix_color          : color (Color) 
    - multiply           : color (Color) 
    - not_equal          : result (Boolean) 
    - overlay            : color (Color) 
    - raycast            : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float),
      attribute (Color)] 
    - saturation         : color (Color) 
    - screen             : color (Color) 
    - soft_light         : color (Color) 
    - subtract           : color (Color) 
    - transfer_attribute : attribute (Color) 
    - value              : color (Color) 
    

    Stacked methods
    ===============
    - curves : Color 
    """


    def reset_properties(self):
        self.separate_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, r=None, g=None, b=None):
        """Call node CombineRgb (ShaderNodeCombineRGB)

        Sockets arguments
        -----------------
            r              : Float
            g              : Float
            b              : Float

        Returns
        -------
            Color
        """

        return cls(nodes.CombineRgb(r=r, g=g, b=b).image)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """Call node SeparateRgb (ShaderNodeSeparateRGB)

        Sockets arguments
        -----------------
            image          : Color (self)

        Returns
        -------
            Sockets [r (Float), g (Float), b (Float)]
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
        return self.separate_


    @property
    def r(self):
        return self.separate.r

    @r.setter
    def r(self, value):
        self.separate.r = value

    @property
    def g(self):
        return self.separate.g

    @g.setter
    def g(self, value):
        self.separate.g = value

    @property
    def b(self):
        return self.separate.b

    @b.setter
    def b(self, value):
        self.separate.b = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            attribute      : Color (self)
            source         : Geometry
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_COLOR'

        Returns
        -------
            Color
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """Call node CaptureAttribute (GeometryNodeCaptureAttribute)

        Sockets arguments
        -----------------
            value          : Color (self)
            geometry       : Geometry

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_COLOR'

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Color)]
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """Call node FieldAtIndex (GeometryNodeFieldAtIndex)

        Sockets arguments
        -----------------
            value          : Color (self)
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_COLOR'

        Returns
        -------
            Color
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """Call node Raycast (GeometryNodeRaycast)

        Sockets arguments
        -----------------
            attribute      : Color (self)
            target_geometry: Geometry
            source_position: Vector
            ray_direction  : Vector
            ray_length     : Float

        Parameters arguments
        --------------------
            mapping        : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_COLOR'

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping)

    def equal(self, b=None, epsilon=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Color (self)
            b              : Color
            epsilon        : Float

        Fixed parameters
        ----------------
            data_type      : 'RGBA'
            mode           : 'ELEMENT'
            operation      : 'EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL').result

    def not_equal(self, b=None, epsilon=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Color (self)
            b              : Color
            epsilon        : Float

        Fixed parameters
        ----------------
            data_type      : 'RGBA'
            mode           : 'ELEMENT'
            operation      : 'NOT_EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL').result

    def brighter(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Color (self)
            b              : Color

        Fixed parameters
        ----------------
            data_type      : 'RGBA'
            mode           : 'ELEMENT'
            operation      : 'BRIGHTER'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER').result

    def darker(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Color (self)
            b              : Color

        Fixed parameters
        ----------------
            data_type      : 'RGBA'
            mode           : 'ELEMENT'
            operation      : 'DARKER'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER').result

    def mix(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'MIX'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha).color

    def darken(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DARKEN'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha).color

    def multiply(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'MULTIPLY'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha).color

    def burn(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'BURN'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha).color

    def lighten(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'LIGHTEN'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha).color

    def screen(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SCREEN'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha).color

    def dodge(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DODGE'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha).color

    def add(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'ADD'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha).color

    def overlay(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'OVERLAY'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha).color

    def soft_light(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SOFT_LIGHT'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha).color

    def linear_light(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'LINEAR_LIGHT'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha).color

    def difference(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DIFFERENCE'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha).color

    def subtract(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SUBTRACT'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha).color

    def divide(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DIVIDE'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha).color

    def hue(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'HUE'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha).color

    def saturation(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SATURATION'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha).color

    def mix_color(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'COLOR'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha).color

    def value(self, color2=None, fac=None, use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'VALUE'

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha).color

    def mix(self, color2=None, fac=None, blend_type='MIX', use_alpha=False):
        """Call node Mix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            blend_type     : 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
            use_alpha      : False

        Returns
        -------
            Color
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha).color


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """Call node RgbCurves (ShaderNodeRGBCurve)

        Sockets arguments
        -----------------
            color          : Color (self)
            fac            : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.RgbCurves(color=self, fac=fac))


