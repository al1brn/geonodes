from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Color(Socket):

    @classmethod
    def CombineRGB(cls, red=None, green=None, blue=None, alpha=None):
        """ > Constructor <&Node Combine Color>

        Information
        -----------
        - Parameter 'mode' : 'RGB'

        Arguments
        ---------
        - red (Float) : socket 'Red' (id: Red)
        - green (Float) : socket 'Green' (id: Green)
        - blue (Float) : socket 'Blue' (id: Blue)
        - alpha (Float) : socket 'Alpha' (id: Alpha)

        Returns
        -------
        - Color
        """
        node = Node('Combine Color', sockets={'Red': red, 'Green': green, 'Blue': blue, 'Alpha': alpha}, mode='RGB')
        return cls(node._out)

    @classmethod
    def CombineHSV(cls, hue=None, saturation=None, value=None, alpha=None):
        """ > Constructor <&Node Combine Color>

        Information
        -----------
        - Parameter 'mode' : 'HSV'

        Arguments
        ---------
        - hue (Float) : socket 'Hue' (id: Red)
        - saturation (Float) : socket 'Saturation' (id: Green)
        - value (Float) : socket 'Value' (id: Blue)
        - alpha (Float) : socket 'Alpha' (id: Alpha)

        Returns
        -------
        - Color
        """
        node = Node('Combine Color', sockets={'Red': hue, 'Green': saturation, 'Blue': value, 'Alpha': alpha}, mode='HSV')
        return cls(node._out)

    @classmethod
    def CombineHSL(cls, hue=None, saturation=None, lightness=None, alpha=None):
        """ > Constructor <&Node Combine Color>

        Information
        -----------
        - Parameter 'mode' : 'HSL'

        Arguments
        ---------
        - hue (Float) : socket 'Hue' (id: Red)
        - saturation (Float) : socket 'Saturation' (id: Green)
        - lightness (Float) : socket 'Lightness' (id: Blue)
        - alpha (Float) : socket 'Alpha' (id: Alpha)

        Returns
        -------
        - Color
        """
        node = Node('Combine Color', sockets={'Red': hue, 'Green': saturation, 'Blue': lightness, 'Alpha': alpha}, mode='HSL')
        return cls(node._out)

    @classmethod
    def Combine(cls, red=None, green=None, blue=None, alpha=None, mode='RGB'):
        """ > Constructor <&Node Combine Color>

        Arguments
        ---------
        - red (Float) : socket 'Red' (id: Red)
        - green (Float) : socket 'Green' (id: Green)
        - blue (Float) : socket 'Blue' (id: Blue)
        - alpha (Float) : socket 'Alpha' (id: Alpha)
        - mode (str): parameter 'mode' in ('RGB', 'HSV', 'HSL')

        Returns
        -------
        - Color
        """
        node = Node('Combine Color', sockets={'Red': red, 'Green': green, 'Blue': blue, 'Alpha': alpha}, mode=mode)
        return cls(node._out)

    def equal(self, b=None, epsilon=None):
        """ > Method <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'EQUAL'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_COL)
        - epsilon (Float) : socket 'Epsilon' (id: Epsilon)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_COL': self, 'B_COL': b, 'Epsilon': epsilon}, data_type='RGBA', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b=None, epsilon=None):
        """ > Method <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'NOT_EQUAL'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_COL)
        - epsilon (Float) : socket 'Epsilon' (id: Epsilon)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_COL': self, 'B_COL': b, 'Epsilon': epsilon}, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def brighter(self, b=None):
        """ > Method <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'BRIGHTER'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_COL)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_COL': self, 'B_COL': b}, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER')
        return node._out

    def darker(self, b=None):
        """ > Method <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'DARKER'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_COL)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_COL': self, 'B_COL': b}, data_type='RGBA', mode='ELEMENT', operation='DARKER')
        return node._out

    def hash_value(self, seed=None):
        """ > Method <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'RGBA'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', sockets={'Value': self, 'Seed': seed}, data_type='RGBA')
        return node._out

    @property
    def separate_RGB(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'RGB'

        Returns
        -------
        - Float [green_ (Float), blue_ (Float), alpha_ (Float)]
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='RGB')
        return node._out

    @property
    def separate_HSV(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'HSV'

        Returns
        -------
        - Float [saturation_ (Float), value_ (Float), alpha_ (Float)]
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='HSV')
        return node._out

    @property
    def separate_HSL(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'HSL'

        Returns
        -------
        - Float [saturation_ (Float), lightness_ (Float), alpha_ (Float)]
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='HSL')
        return node._out

    @property
    def separate(self, mode='RGB'):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self

        Arguments
        ---------
        - mode (str): parameter 'mode' in ('RGB', 'HSV', 'HSL')

        Returns
        -------
        - Float [green_ (Float), blue_ (Float), alpha_ (Float)]
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode=mode)
        return node._out

    @property
    def rgb(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'RGB'

        Returns
        -------
        - tuple (Float, Float, Float, Float)
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='RGB')
        return (node.red, node.green, node.blue, node.alpha)

    @property
    def hsv(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'HSL'

        Returns
        -------
        - tuple (Float, Float, Float, Float)
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='HSL')
        return (node.hue, node.saturation, node.lightness, node.alpha)

    @property
    def separate_color(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'RGB'

        Returns
        -------
        - node [red (Float), green (Float), blue (Float), alpha (Float)]
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='RGB')
        return node

    @property
    def hue(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'HSV'

        Returns
        -------
        - hue
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='HSV')
        return node.hue

    @property
    def saturation(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'HSV'

        Returns
        -------
        - saturation
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='HSV')
        return node.saturation

    @property
    def lightness(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'HSL'

        Returns
        -------
        - lightness
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='HSL')
        return node.lightness

    @property
    def alpha(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'RGB'

        Returns
        -------
        - alpha
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='RGB')
        return node.alpha

    @property
    def value(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'HSV'

        Returns
        -------
        - value
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='HSV')
        return node.value

    @property
    def red(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'RGB'

        Returns
        -------
        - red
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='RGB')
        return node.red

    @property
    def green(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'RGB'

        Returns
        -------
        - green
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='RGB')
        return node.green

    @property
    def blue(self):
        """ > Property Get <&Node Separate Color>

        Information
        -----------
        - Socket 'Color' : self
        - Parameter 'mode' : 'RGB'

        Returns
        -------
        - blue
        """
        node = self._cache('Separate Color', sockets={'Color': self}, mode='RGB')
        return node.blue

    def blur(self, iterations=None, weight=None):
        """ > Method <&Node Blur Attribute>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'FLOAT_COLOR'

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Color
        """
        node = Node('Blur Attribute', sockets={'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='FLOAT_COLOR')
        return node._out

    @classmethod
    def ImageTexture(cls, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """ > Constructor <&Node Image Texture>

        Arguments
        ---------
        - image (Image) : socket 'Image' (id: Image)
        - vector (Vector) : socket 'Vector' (id: Vector)
        - frame (Integer) : socket 'Frame' (id: Frame)
        - extension (str): parameter 'extension' in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')
        - interpolation (str): parameter 'interpolation' in ('Linear', 'Closest', 'Cubic')

        Returns
        -------
        - Color
        """
        node = Node('Image Texture', sockets={'Image': image, 'Vector': vector, 'Frame': frame}, extension=extension, interpolation=interpolation)
        return cls(node._out)

    @classmethod
    def Named(cls, name=None):
        """ > Constructor <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT_COLOR'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Color
        """
        node = Node('Named Attribute', sockets={'Name': name}, data_type='FLOAT_COLOR')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name=None):
        """ > Constructor <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT_COLOR'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Color
        """
        node = Node('Named Attribute', sockets={'Name': name}, data_type='FLOAT_COLOR')
        return cls(node._out)

    @classmethod
    def Blackbody(cls, temperature=None):
        """ > Constructor <&Node Blackbody>

        Arguments
        ---------
        - temperature (Float) : socket 'Temperature' (id: Temperature)

        Returns
        -------
        - Color
        """
        node = Node('Blackbody', sockets={'Temperature': temperature})
        return cls(node._out)

    def mix_mix(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_darken(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'DARKEN'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_multiply(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MULTIPLY'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_burn(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'BURN'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_lighten(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'LIGHTEN'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_screen(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'SCREEN'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_dodge(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'DODGE'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_add(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'ADD'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_overlay(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'OVERLAY'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_soft_light(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'SOFT_LIGHT'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_linear_light(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'LINEAR_LIGHT'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_difference(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'DIFFERENCE'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_exclusion(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'EXCLUSION'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='EXCLUSION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_subtract(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'SUBTRACT'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_divide(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'DIVIDE'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_hue(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'HUE'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_saturation(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'SATURATION'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_color(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'COLOR'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def mix_value(self, b=None, factor=None, clamp_factor=True, clamp_result=False):
        """ > Method <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'VALUE'
        - Parameter 'data_type' : 'RGBA'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Color) : socket 'B' (id: B_Color)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'

        Returns
        -------
        - Color
        """
        node = Node('Mix', sockets={'A_Color': self, 'B_Color': b, 'Factor_Float': factor}, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM')
        return node._out

    def rgb_curves(self, fac=None):
        """ > Method <&Node RGB Curves>

        Information
        -----------
        - Socket 'Color' : self

        Arguments
        ---------
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Color
        """
        node = Node('RGB Curves', sockets={'Color': self, 'Fac': fac})
        return node._out

    @classmethod
    def Brick(cls, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        """ > Constructor <&Node Brick Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - color1 (Color) : socket 'Color1' (id: Color1)
        - color2 (Color) : socket 'Color2' (id: Color2)
        - mortar (Color) : socket 'Mortar' (id: Mortar)
        - scale (Float) : socket 'Scale' (id: Scale)
        - mortar_size (Float) : socket 'Mortar Size' (id: Mortar Size)
        - mortar_smooth (Float) : socket 'Mortar Smooth' (id: Mortar Smooth)
        - bias (Float) : socket 'Bias' (id: Bias)
        - brick_width (Float) : socket 'Brick Width' (id: Brick Width)
        - row_height (Float) : socket 'Row Height' (id: Row Height)
        - offset (float): parameter 'offset'
        - offset_frequency (int): parameter 'offset_frequency'
        - squash (float): parameter 'squash'
        - squash_frequency (int): parameter 'squash_frequency'

        Returns
        -------
        - Color
        """
        node = Node('Brick Texture', sockets={'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return cls(node._out)

    @classmethod
    def Checker(cls, vector=None, color1=None, color2=None, scale=None):
        """ > Constructor <&Node Checker Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - color1 (Color) : socket 'Color1' (id: Color1)
        - color2 (Color) : socket 'Color2' (id: Color2)
        - scale (Float) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Color
        """
        node = Node('Checker Texture', sockets={'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})
        return cls(node._out)

    @classmethod
    def Gradient(cls, vector=None, gradient_type='LINEAR'):
        """ > Constructor <&Node Gradient Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - gradient_type (str): parameter 'gradient_type' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')

        Returns
        -------
        - Color
        """
        node = Node('Gradient Texture', sockets={'Vector': vector}, gradient_type=gradient_type)
        return cls(node._out)

    @classmethod
    def Magic(cls, vector=None, scale=None, distortion=None, turbulence_depth=2):
        """ > Constructor <&Node Magic Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - turbulence_depth (int): parameter 'turbulence_depth'

        Returns
        -------
        - Color
        """
        node = Node('Magic Texture', sockets={'Vector': vector, 'Scale': scale, 'Distortion': distortion}, turbulence_depth=turbulence_depth)
        return cls(node._out)

    @classmethod
    def Wave(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """ > Constructor <&Node Wave Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - detail (Float) : socket 'Detail' (id: Detail)
        - detail_scale (Float) : socket 'Detail Scale' (id: Detail Scale)
        - detail_roughness (Float) : socket 'Detail Roughness' (id: Detail Roughness)
        - phase_offset (Float) : socket 'Phase Offset' (id: Phase Offset)
        - bands_direction (str): parameter 'bands_direction' in ('X', 'Y', 'Z', 'DIAGONAL')
        - rings_direction (str): parameter 'rings_direction' in ('X', 'Y', 'Z', 'SPHERICAL')
        - wave_profile (str): parameter 'wave_profile' in ('SIN', 'SAW', 'TRI')
        - wave_type (str): parameter 'wave_type' in ('BANDS', 'RINGS')

        Returns
        -------
        - Color
        """
        node = Node('Wave Texture', sockets={'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return cls(node._out)

