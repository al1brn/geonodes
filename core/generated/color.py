# Generated 2026-04-05 14:24:03

from __future__ import annotations
from .. sockettype import SocketType
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Color(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    @classmethod
    def CombineRGB(cls,
                    red: Float = None,
                    green: Float = None,
                    blue: Float = None,
                    alpha: Float = None):
        """ > Node <&Node Combine Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Parameter | `mode` | `'RGB'` |

        Parameters
        ----------
        red : Float, optional
            socket 'Red' (id: Red)
        
        green : Float, optional
            socket 'Green' (id: Green)
        
        blue : Float, optional
            socket 'Blue' (id: Blue)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        

        Returns
        -------
        Color
        """
        node = Node('Combine Color', {'Red': red, 'Green': green, 'Blue': blue, 'Alpha': alpha}, mode='RGB')
        return cls(node._out)

    @classmethod
    def CombineHSV(cls,
                    hue: Float = None,
                    saturation: Float = None,
                    value: Float = None,
                    alpha: Float = None):
        """ > Node <&Node Combine Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Parameter | `mode` | `'HSV'` |

        Parameters
        ----------
        hue : Float, optional
            socket 'Hue' (id: Red)
        
        saturation : Float, optional
            socket 'Saturation' (id: Green)
        
        value : Float, optional
            socket 'Value' (id: Blue)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        

        Returns
        -------
        Color
        """
        node = Node('Combine Color', {'Red': hue, 'Green': saturation, 'Blue': value, 'Alpha': alpha}, mode='HSV')
        return cls(node._out)

    @classmethod
    def CombineHSL(cls,
                    hue: Float = None,
                    saturation: Float = None,
                    lightness: Float = None,
                    alpha: Float = None):
        """ > Node <&Node Combine Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Parameter | `mode` | `'HSL'` |

        Parameters
        ----------
        hue : Float, optional
            socket 'Hue' (id: Red)
        
        saturation : Float, optional
            socket 'Saturation' (id: Green)
        
        lightness : Float, optional
            socket 'Lightness' (id: Blue)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        

        Returns
        -------
        Color
        """
        node = Node('Combine Color', {'Red': hue, 'Green': saturation, 'Blue': lightness, 'Alpha': alpha}, mode='HSL')
        return cls(node._out)

    @classmethod
    def Combine(cls,
                    red: Float = None,
                    green: Float = None,
                    blue: Float = None,
                    alpha: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&Node Combine Color>

        Parameters
        ----------
        red : Float, optional
            socket 'Red' (id: Red)
        
        green : Float, optional
            socket 'Green' (id: Green)
        
        blue : Float, optional
            socket 'Blue' (id: Blue)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        
        mode : Literal['RGB', 'HSV', 'HSL']
            parameter `mode`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Combine Color', 'mode', mode, 'Combine', ('RGB', 'HSV', 'HSL'))
        node = Node('Combine Color', {'Red': red, 'Green': green, 'Blue': blue, 'Alpha': alpha}, mode=mode)
        return cls(node._out)

    def equal(self, b: Color = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | A           | `self`      |
        | Parameter | `data_type` | `'RGBA'`    |
        | Parameter | `mode`      | `'ELEMENT'` |
        | Parameter | `operation` | `'EQUAL'`   |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_COL)
        
        epsilon : Float, optional
            socket 'Epsilon' (id: Epsilon)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_COL': self, 'B_COL': b, 'Epsilon': epsilon}, data_type='RGBA', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: Color = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Socket    | A           | `self`        |
        | Parameter | `data_type` | `'RGBA'`      |
        | Parameter | `mode`      | `'ELEMENT'`   |
        | Parameter | `operation` | `'NOT_EQUAL'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_COL)
        
        epsilon : Float, optional
            socket 'Epsilon' (id: Epsilon)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_COL': self, 'B_COL': b, 'Epsilon': epsilon}, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def brighter(self, b: Color = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | A           | `self`       |
        | Parameter | `data_type` | `'RGBA'`     |
        | Parameter | `mode`      | `'ELEMENT'`  |
        | Parameter | `operation` | `'BRIGHTER'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_COL)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_COL': self, 'B_COL': b}, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER')
        return node._out

    def darker(self, b: Color = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | A           | `self`      |
        | Parameter | `data_type` | `'RGBA'`    |
        | Parameter | `mode`      | `'ELEMENT'` |
        | Parameter | `operation` | `'DARKER'`  |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_COL)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_COL': self, 'B_COL': b}, data_type='RGBA', mode='ELEMENT', operation='DARKER')
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Value       | `self`   |
        | Parameter | `data_type` | `'RGBA'` |

        Parameters
        ----------
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='RGBA')
        return node._out

    def separate_RGB(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        node [red (Float), green (Float), blue (Float), alpha (Float)]
        """
        node = self._cache('Separate Color', {'Color': self}, mode='RGB')
        return node

    def separate_HSV(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSV'` |

        Returns
        -------
        node [hue (Float), saturation (Float), value (Float), alpha (Float)]
        """
        node = self._cache('Separate Color', {'Color': self}, mode='HSV')
        return node

    def separate_HSL(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSL'` |

        Returns
        -------
        node [hue (Float), saturation (Float), lightness (Float), alpha (Float)]
        """
        node = self._cache('Separate Color', {'Color': self}, mode='HSL')
        return node

    def separate(self, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        mode : Literal['RGB', 'HSV', 'HSL']
            parameter `mode`
        

        Returns
        -------
        node [red (Float), green (Float), blue (Float), alpha (Float)]
        """
        utils.check_enum_arg('Separate Color', 'mode', mode, 'separate', ('RGB', 'HSV', 'HSL'))
        node = self._cache('Separate Color', {'Color': self}, mode=mode)
        return node

    @property
    def rgb(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        tuple (Float, Float, Float, Float)
        """
        node = self._cache('Separate Color', {'Color': self}, mode='RGB')
        return (node.red, node.green, node.blue, node.alpha)

    @property
    def hsv(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSL'` |

        Returns
        -------
        tuple (Float, Float, Float, Float)
        """
        node = self._cache('Separate Color', {'Color': self}, mode='HSL')
        return (node.hue, node.saturation, node.lightness, node.alpha)

    def separate_color(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        node [red (Float), green (Float), blue (Float), alpha (Float)]
        """
        node = self._cache('Separate Color', {'Color': self}, mode='RGB')
        return node

    @property
    def hue(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSV'` |

        Returns
        -------
        hue
        """
        node = self._cache('Separate Color', {'Color': self}, mode='HSV')
        return node.hue

    @property
    def saturation(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSV'` |

        Returns
        -------
        saturation
        """
        node = self._cache('Separate Color', {'Color': self}, mode='HSV')
        return node.saturation

    @property
    def lightness(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSL'` |

        Returns
        -------
        lightness
        """
        node = self._cache('Separate Color', {'Color': self}, mode='HSL')
        return node.lightness

    @property
    def alpha(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        alpha
        """
        node = self._cache('Separate Color', {'Color': self}, mode='RGB')
        return node.alpha

    @property
    def value(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSV'` |

        Returns
        -------
        value
        """
        node = self._cache('Separate Color', {'Color': self}, mode='HSV')
        return node.value

    @property
    def red(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        red
        """
        node = self._cache('Separate Color', {'Color': self}, mode='RGB')
        return node.red

    @property
    def green(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        green
        """
        node = self._cache('Separate Color', {'Color': self}, mode='RGB')
        return node.green

    @property
    def blue(self):
        """ > Node <&Node Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        blue
        """
        node = self._cache('Separate Color', {'Color': self}, mode='RGB')
        return node.blue

    def blur(self, iterations: Integer = None, weight: Float = None):
        """ > Node <&Node Blur Attribute>

        **Fixed values**

        | Kind      | Name        | Value           |
        | --------- | ----------- | --------------- |
        | Socket    | Value       | `self`          |
        | Parameter | `data_type` | `'FLOAT_COLOR'` |

        Parameters
        ----------
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Color
        """
        node = Node('Blur Attribute', {'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='FLOAT_COLOR')
        return node._out

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value           |
        | --------- | ----------- | --------------- |
        | Parameter | `data_type` | `'FLOAT_COLOR'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Color
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT_COLOR')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value           |
        | --------- | ----------- | --------------- |
        | Parameter | `data_type` | `'FLOAT_COLOR'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Color
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT_COLOR')
        return cls(node._out)

    @classmethod
    def Blackbody(cls, temperature: Float = None):
        """ > Node <&Node Blackbody>

        Parameters
        ----------
        temperature : Float, optional
            socket 'Temperature' (id: Temperature)
        

        Returns
        -------
        Color
        """
        node = Node('Blackbody', {'Temperature': temperature})
        return cls(node._out)

    def mix_mix(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'MIX'`     |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_darken(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'DARKEN'`  |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_multiply(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value        |
        | --------- | ------------- | ------------ |
        | Socket    | A             | `self`       |
        | Parameter | `blend_type`  | `'MULTIPLY'` |
        | Parameter | `data_type`   | `'RGBA'`     |
        | Parameter | `factor_mode` | `'UNIFORM'`  |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_burn(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'BURN'`    |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_lighten(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'LIGHTEN'` |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_screen(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'SCREEN'`  |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_dodge(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'DODGE'`   |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_add(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'ADD'`     |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_overlay(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'OVERLAY'` |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_soft_light(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value          |
        | --------- | ------------- | -------------- |
        | Socket    | A             | `self`         |
        | Parameter | `blend_type`  | `'SOFT_LIGHT'` |
        | Parameter | `data_type`   | `'RGBA'`       |
        | Parameter | `factor_mode` | `'UNIFORM'`    |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_linear_light(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value            |
        | --------- | ------------- | ---------------- |
        | Socket    | A             | `self`           |
        | Parameter | `blend_type`  | `'LINEAR_LIGHT'` |
        | Parameter | `data_type`   | `'RGBA'`         |
        | Parameter | `factor_mode` | `'UNIFORM'`      |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_difference(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value          |
        | --------- | ------------- | -------------- |
        | Socket    | A             | `self`         |
        | Parameter | `blend_type`  | `'DIFFERENCE'` |
        | Parameter | `data_type`   | `'RGBA'`       |
        | Parameter | `factor_mode` | `'UNIFORM'`    |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_exclusion(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value         |
        | --------- | ------------- | ------------- |
        | Socket    | A             | `self`        |
        | Parameter | `blend_type`  | `'EXCLUSION'` |
        | Parameter | `data_type`   | `'RGBA'`      |
        | Parameter | `factor_mode` | `'UNIFORM'`   |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='EXCLUSION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_subtract(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value        |
        | --------- | ------------- | ------------ |
        | Socket    | A             | `self`       |
        | Parameter | `blend_type`  | `'SUBTRACT'` |
        | Parameter | `data_type`   | `'RGBA'`     |
        | Parameter | `factor_mode` | `'UNIFORM'`  |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_divide(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'DIVIDE'`  |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_hue(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'HUE'`     |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_saturation(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value          |
        | --------- | ------------- | -------------- |
        | Socket    | A             | `self`         |
        | Parameter | `blend_type`  | `'SATURATION'` |
        | Parameter | `data_type`   | `'RGBA'`       |
        | Parameter | `factor_mode` | `'UNIFORM'`    |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_color(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'COLOR'`   |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_value(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name          | Value       |
        | --------- | ------------- | ----------- |
        | Socket    | A             | `self`      |
        | Parameter | `blend_type`  | `'VALUE'`   |
        | Parameter | `data_type`   | `'RGBA'`    |
        | Parameter | `factor_mode` | `'UNIFORM'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        

        Returns
        -------
        Color
        """
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False,
                    factor_mode: Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM'):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name         | Value    |
        | --------- | ------------ | -------- |
        | Socket    | A            | `self`   |
        | Parameter | `blend_type` | `'MIX'`  |
        | Parameter | `data_type`  | `'RGBA'` |

        Parameters
        ----------
        b : Color, optional
            socket 'B' (id: B_Color)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        
        factor_mode : Literal['Uniform', 'Non-Uniform']
            parameter `factor_mode`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Mix', 'factor_mode', factor_mode, 'mix', ('UNIFORM', 'NON_UNIFORM'))
        node = Node('Mix', {'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode=factor_mode)
        return node._out

    @classmethod
    def Brick(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2):
        """ > Node <&Node Brick Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        color1 : Color, optional
            socket 'Color1' (id: Color1)
        
        color2 : Color, optional
            socket 'Color2' (id: Color2)
        
        mortar : Color, optional
            socket 'Mortar' (id: Mortar)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        mortar_size : Float, optional
            socket 'Mortar Size' (id: Mortar Size)
        
        mortar_smooth : Float, optional
            socket 'Mortar Smooth' (id: Mortar Smooth)
        
        bias : Float, optional
            socket 'Bias' (id: Bias)
        
        brick_width : Float, optional
            socket 'Brick Width' (id: Brick Width)
        
        row_height : Float, optional
            socket 'Row Height' (id: Row Height)
        
        offset : float
            parameter `offset`
        
        offset_frequency : int
            parameter `offset_frequency`
        
        squash : float
            parameter `squash`
        
        squash_frequency : int
            parameter `squash_frequency`
        

        Returns
        -------
        Color
        """
        node = Node('Brick Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return cls(node._out)

    @classmethod
    def Checker(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None):
        """ > Node <&Node Checker Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        color1 : Color, optional
            socket 'Color1' (id: Color1)
        
        color2 : Color, optional
            socket 'Color2' (id: Color2)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        

        Returns
        -------
        Color
        """
        node = Node('Checker Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})
        return cls(node._out)

    @classmethod
    def Gradient(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR'):
        """ > Node <&Node Gradient Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        gradient_type : Literal['Linear', 'Quadratic', 'Easing', 'Diagonal', 'Spherical', 'Quadratic Sphere', 'Radial']
            parameter `gradient_type`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Gradient Texture', 'gradient_type', gradient_type, 'Gradient', ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'))
        node = Node('Gradient Texture', {'Vector': vector}, gradient_type=gradient_type)
        return cls(node._out)

    @classmethod
    def Magic(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2):
        """ > Node <&Node Magic Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        turbulence_depth : int
            parameter `turbulence_depth`
        

        Returns
        -------
        Color
        """
        node = Node('Magic Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion}, turbulence_depth=turbulence_depth)
        return cls(node._out)

    @classmethod
    def Wave(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS'):
        """ > Node <&Node Wave Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        detail : Float, optional
            socket 'Detail' (id: Detail)
        
        detail_scale : Float, optional
            socket 'Detail Scale' (id: Detail Scale)
        
        detail_roughness : Float, optional
            socket 'Detail Roughness' (id: Detail Roughness)
        
        phase_offset : Float, optional
            socket 'Phase Offset' (id: Phase Offset)
        
        bands_direction : Literal['X', 'Y', 'Z', 'Diagonal']
            parameter `bands_direction`
        
        rings_direction : Literal['X', 'Y', 'Z', 'Spherical']
            parameter `rings_direction`
        
        wave_profile : Literal['Sine', 'Saw', 'Triangle']
            parameter `wave_profile`
        
        wave_type : Literal['Bands', 'Rings']
            parameter `wave_type`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Wave Texture', 'bands_direction', bands_direction, 'Wave', ('X', 'Y', 'Z', 'DIAGONAL'))
        utils.check_enum_arg('Wave Texture', 'rings_direction', rings_direction, 'Wave', ('X', 'Y', 'Z', 'SPHERICAL'))
        utils.check_enum_arg('Wave Texture', 'wave_profile', wave_profile, 'Wave', ('SIN', 'SAW', 'TRI'))
        utils.check_enum_arg('Wave Texture', 'wave_type', wave_type, 'Wave', ('BANDS', 'RINGS'))
        node = Node('Wave Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return cls(node._out)

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Value       | `self`   |
        | Parameter | `data_type` | `'RGBA'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Color
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='RGBA')
        return node._out

    def gamma(self, gamma: Float = None):
        """ > Node <&Node Gamma>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        gamma : Float, optional
            socket 'Gamma' (id: Gamma)
        

        Returns
        -------
        Color
        """
        node = Node('Gamma', {'Color': self, 'Gamma': gamma})
        return node._out

    def ambient_occlusion(self,
                    distance: Float = None,
                    normal: Vector = None,
                    inside = False,
                    only_local = False,
                    samples = 16):
        """ > Node <&ShaderNode Ambient Occlusion>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        distance : Float, optional
            socket 'Distance' (id: Distance)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        inside : bool
            parameter `inside`
        
        only_local : bool
            parameter `only_local`
        
        samples : int
            parameter `samples`
        

        Returns
        -------
        Color
            peer sockets: ao_ (Float)

        """
        node = Node('Ambient Occlusion', {'Color': self, 'Distance': distance, 'Normal': normal}, inside=inside, only_local=only_local, samples=samples)
        return node._out

    def background(self, strength: Float = None):
        """ > Node <&ShaderNode Background>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        strength : Float, optional
            socket 'Strength' (id: Strength)
        

        Returns
        -------
        Shader
        """
        node = Node('Background', {'Color': self, 'Strength': strength})
        return node._out

    def brightness_contrast(self, brightness: Float = None, contrast: Float = None):
        """ > Node <&ShaderNode Brightness/Contrast>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        brightness : Float, optional
            socket 'Brightness' (id: Bright)
        
        contrast : Float, optional
            socket 'Contrast' (id: Contrast)
        

        Returns
        -------
        Color
        """
        node = Node('Brightness/Contrast', {'Color': self, 'Bright': brightness, 'Contrast': contrast})
        return node._out

    def hue_saturation_value(self,
                    hue: Float = None,
                    saturation: Float = None,
                    value: Float = None,
                    factor: Float = None):
        """ > Node <&ShaderNode Hue/Saturation/Value>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        hue : Float, optional
            socket 'Hue' (id: Hue)
        
        saturation : Float, optional
            socket 'Saturation' (id: Saturation)
        
        value : Float, optional
            socket 'Value' (id: Value)
        
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Color
        """
        node = Node('Hue/Saturation/Value', {'Hue': hue, 'Saturation': saturation, 'Value': value, 'Color': self, 'Fac': factor})
        return node._out

    def invert_color(self, factor: Float = None):
        """ > Node <&ShaderNode Invert Color>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Color
        """
        node = Node('Invert Color', {'Color': self, 'Fac': factor})
        return node._out

    def aov_output(self, value: Float = None, aov_name = ''):
        """ > Node <&ShaderNode AOV Output>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        value : Float, optional
            socket 'Value' (id: Value)
        
        aov_name : str
            parameter `aov_name`
        

        Returns
        -------
        None
        """
        node = Node('AOV Output', {'Color': self, 'Value': value}, aov_name=aov_name)
        return node._out

    def line_style_output(self,
                    color_fac: Float = None,
                    alpha: Float = None,
                    alpha_fac: Float = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL',
                    use_alpha = False,
                    use_clamp = False):
        """ > Node <&ShaderNode Line Style Output>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        color_fac : Float, optional
            socket 'Color Fac' (id: Color Fac)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        
        alpha_fac : Float, optional
            socket 'Alpha Fac' (id: Alpha Fac)
        
        blend_type : Literal['Mix', 'Darken', 'Multiply', 'Color Burn', 'Lighten', 'Screen', 'Color Dodge', 'Add', 'Overlay', 'Soft Light', 'Linear Light', 'Difference', 'Exclusion', 'Subtract', 'Divide', 'Hue', 'Saturation', 'Color', 'Value']
            parameter `blend_type`
        
        is_active_output : bool
            parameter `is_active_output`
        
        target : Literal['All', 'EEVEE', 'Cycles']
            parameter `target`
        
        use_alpha : bool
            parameter `use_alpha`
        
        use_clamp : bool
            parameter `use_clamp`
        

        Returns
        -------
        None
        """
        utils.check_enum_arg('Line Style Output', 'blend_type', blend_type, 'line_style_output', ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'))
        utils.check_enum_arg('Line Style Output', 'target', target, 'line_style_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Line Style Output', {'Color': self, 'Color Fac': color_fac, 'Alpha': alpha, 'Alpha Fac': alpha_fac}, blend_type=blend_type, is_active_output=is_active_output, target=target, use_alpha=use_alpha, use_clamp=use_clamp)
        return node._out

    def rgb_to_bw(self):
        """ > Node <&ShaderNode RGB to BW>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Returns
        -------
        Float
        """
        node = Node('RGB to BW', {'Color': self})
        return node._out

    def separate_col_RGB(self):
        """ > Node <&ShaderNode Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'RGB'` |

        Returns
        -------
        node [red (Float), green (Float), blue (Float)]
        """
        node = Node('Separate Color', {'Color': self}, mode='RGB')
        return node

    def separate_col_HSV(self):
        """ > Node <&ShaderNode Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSV'` |

        Returns
        -------
        node [hue (Float), saturation (Float), value (Float)]
        """
        node = Node('Separate Color', {'Color': self}, mode='HSV')
        return node

    def separate_col_HSL(self):
        """ > Node <&ShaderNode Separate Color>

        **Fixed values**

        | Kind      | Name   | Value   |
        | --------- | ------ | ------- |
        | Socket    | Color  | `self`  |
        | Parameter | `mode` | `'HSL'` |

        Returns
        -------
        node [hue (Float), saturation (Float), lightness (Float)]
        """
        node = Node('Separate Color', {'Color': self}, mode='HSL')
        return node

    def separate_col(self, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&ShaderNode Separate Color>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Color | `self` |

        Parameters
        ----------
        mode : Literal['RGB', 'HSV', 'HSL']
            parameter `mode`
        

        Returns
        -------
        node [red (Float), green (Float), blue (Float)]
        """
        utils.check_enum_arg('Separate Color', 'mode', mode, 'separate_col', ('RGB', 'HSV', 'HSL'))
        node = Node('Separate Color', {'Color': self}, mode=mode)
        return node

    @classmethod
    def SkyTexture(cls,
                    aerosol_density = 1.0,
                    air_density = 1.0,
                    altitude = 100.0,
                    ground_albedo = 0.30000001192092896,
                    ozone_density = 1.0,
                    sky_type: Literal['SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE'] = 'MULTIPLE_SCATTERING',
                    sun_disc = True,
                    sun_elevation = 0.2617993950843811,
                    sun_intensity = 1.0,
                    sun_rotation = 0.0,
                    sun_size = 0.009512044489383698,
                    turbidity = 2.200000047683716):
        """ > Node <&ShaderNode Sky Texture>

        Parameters
        ----------
        aerosol_density : float
            parameter `aerosol_density`
        
        air_density : float
            parameter `air_density`
        
        altitude : float
            parameter `altitude`
        
        ground_albedo : float
            parameter `ground_albedo`
        
        ozone_density : float
            parameter `ozone_density`
        
        sky_type : Literal['Single Scattering', 'Multiple Scattering', 'Preetham', 'Hosek / Wilkie']
            parameter `sky_type`
        
        sun_disc : bool
            parameter `sun_disc`
        
        sun_elevation : float
            parameter `sun_elevation`
        
        sun_intensity : float
            parameter `sun_intensity`
        
        sun_rotation : float
            parameter `sun_rotation`
        
        sun_size : float
            parameter `sun_size`
        
        turbidity : float
            parameter `turbidity`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Sky Texture', 'sky_type', sky_type, 'SkyTexture', ('SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE'))
        node = Node('Sky Texture', aerosol_density=aerosol_density, air_density=air_density, altitude=altitude, ground_albedo=ground_albedo, ozone_density=ozone_density, sky_type=sky_type, sun_disc=sun_disc, sun_elevation=sun_elevation, sun_intensity=sun_intensity, sun_rotation=sun_rotation, sun_size=sun_size, turbidity=turbidity)
        return cls(node._out)

    def vector_displacement(self,
                    midlevel: Float = None,
                    scale: Float = None,
                    space: Literal['TANGENT', 'OBJECT', 'WORLD'] = 'TANGENT'):
        """ > Node <&ShaderNode Vector Displacement>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        midlevel : Float, optional
            socket 'Midlevel' (id: Midlevel)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        space : Literal['Tangent Space', 'Object Space', 'World Space']
            parameter `space`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Vector Displacement', 'space', space, 'vector_displacement', ('TANGENT', 'OBJECT', 'WORLD'))
        node = Node('Vector Displacement', {'Vector': self, 'Midlevel': midlevel, 'Scale': scale}, space=space)
        return node._out

    @classmethod
    def ColorAttribute(cls, layer_name = ''):
        """ > Node <&ShaderNode Color Attribute>

        Parameters
        ----------
        layer_name : str
            parameter `layer_name`
        

        Returns
        -------
        Color
        """
        node = Node('Color Attribute', layer_name=layer_name)
        return cls(node._out)

    @classmethod
    def _create_input_socket(cls,
        value: object = (1, 1, 1),
        name: str = 'Color',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Color Input

        New <#Color> input with subtype 'NONE'.

        Parameters
        ----------
        value : object, default=`(1, 1, 1)`
            Default value

        name : str, default=`Color`
            Input socket name

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier

        default_attribute : str, default=`''`
            Property default_attribute_name

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Color
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketColor', default_value = defval, name=name,
            tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default_attribute=default_attribute, shape=shape)

