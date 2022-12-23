from geonodes.nodes import nodes
import geonodes.core.datasockets as geosocks
from geonodes.nodes.domains import Vertex, Edge, Face, Corner, ControlPoint, Spline, CloudPoint, Instance

class Float(geosocks.Float):
    @classmethod
    def Frame(cls):
        """

                """

        return cls(nodes.SceneTime().frame)


    @classmethod
    def Seconds(cls):
        """

                """

        return cls(nodes.SceneTime().seconds)


    @classmethod
    def Value(cls):
        """

                """

        return cls(nodes.Value().value)


    def abs(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


    def absolute(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value



    def arccos(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arccosine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arcsin(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arcsine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arctan(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def arctan2(self, value1=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp).value


    def arctangent(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def ceiling(self):
        """

                """

        return nodes.FloatToInteger(float=self, rounding_mode='CEILING').integer


    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        """

                """

        return nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type).result


    def clamp_min_max(self, min=None, max=None):
        """

                """

        return nodes.Clamp(value=self, min=min, max=max, clamp_type='MINMAX').result


    def clamp_range(self, min=None, max=None):
        """

                """

        return nodes.Clamp(value=self, min=min, max=max, clamp_type='RANGE').result


    @property
    def color_ramp(self):
        """

                """

        return nodes.ColorRamp(fac=self)


    def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation=operation).result


    def cos(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value


    def cosh(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSH', use_clamp=clamp).value


    def cosine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value




    def equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL').result


    def exp(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def exponent(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def fact(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def float_curve(self, factor=None):
        """

                """

        return nodes.FloatCurve(factor=factor, value=self).value


    def floor(self):
        """

                """

        return nodes.FloatToInteger(float=self, rounding_mode='FLOOR').integer


    def fraction(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def greater_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL').result


    def greater_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN').result


    def inverse_sqrt(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp).value


    def less_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL').result


    def less_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN').result


    def log(self, base=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def logarithm(self, base=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """

                """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type).result


    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

                """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='LINEAR').result


    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

                """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='SMOOTHSTEP').result


    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

                """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='SMOOTHERSTEP').result


    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):
        """

                """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='STEPPED').result


    def math_ceil(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='CEIL', use_clamp=clamp).value


    def math_compare(self, value=None, epsilon=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=epsilon, operation='COMPARE', use_clamp=clamp).value


    def math_floor(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FLOOR', use_clamp=clamp).value


    def math_greater_than(self, threshold=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp).value


    def math_less_than(self, threshold=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp).value


    def math_round(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ROUND', use_clamp=clamp).value


    def math_trunc(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def math_truncate(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def max(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def maximum(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def min(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def minimum(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def mix(self, factor=None, value=None, clamp_factor=True):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=value, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM').result


    def modulo(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MODULO', use_clamp=clamp).value



    def mul_add(self, multiplier=None, addend=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value



    def multiply_add(self, multiplier=None, addend=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


    def not_equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL').result


    def ping_pong(self, scale=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp).value


    def pow(self, exponent=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def power(self, exponent=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def round(self):
        """

                """

        return nodes.FloatToInteger(float=self, rounding_mode='ROUND').integer


    def sign(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SIGN', use_clamp=clamp).value


    def sin(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sinh(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINH', use_clamp=clamp).value


    def smooth_maximum(self, value=None, distance=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp).value


    def smooth_minimum(self, value=None, distance=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp).value


    def snap(self, increment=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=increment, value2=None, operation='SNAP', use_clamp=clamp).value


    def sqrt(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SQRT', use_clamp=clamp).value




    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='FLOAT').output


    def tan(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tangent(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tanh(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANH', use_clamp=clamp).value


    def to_degrees(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='DEGREES', use_clamp=clamp).value


    def to_integer(self, rounding_mode='ROUND'):
        """

                """

        return nodes.FloatToInteger(float=self, rounding_mode=rounding_mode).integer


    def to_radians(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='RADIANS', use_clamp=clamp).value


    def to_string(self, decimals=None):
        """

                """

        return nodes.ValueToString(value=self, decimals=decimals).string


    def truncate(self):
        """

                """

        return nodes.FloatToInteger(float=self, rounding_mode='TRUNCATE').integer


    def wrap(self, max=None, min=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=max, value2=min, operation='WRAP', use_clamp=clamp).value




class Integer(geosocks.Integer):
    @classmethod
    def Integer(cls, integer=0):
        """

                """

        return cls(nodes.Integer(integer=integer).integer)


    def abs(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


    def absolute(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value



    def arccos(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arccosine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arcsin(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arcsine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arctan(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def arctan2(self, value1=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp).value


    def arctangent(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def compare(self, b=None, operation='GREATER_THAN'):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation=operation).result


    def cos(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value


    def cosh(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSH', use_clamp=clamp).value


    def cosine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value




    def equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='EQUAL').result


    def exp(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def exponent(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def fact(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def fraction(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def greater_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL').result


    def greater_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='GREATER_THAN').result


    def inverse_sqrt(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp).value


    def less_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL').result


    def less_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='LESS_THAN').result


    def log(self, base=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def logarithm(self, base=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def math_ceil(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='CEIL', use_clamp=clamp).value


    def math_compare(self, value=None, epsilon=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=epsilon, operation='COMPARE', use_clamp=clamp).value


    def math_floor(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FLOOR', use_clamp=clamp).value


    def math_greater_than(self, threshold=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp).value


    def math_less_than(self, threshold=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp).value


    def math_round(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ROUND', use_clamp=clamp).value


    def math_trunc(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def math_truncate(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def max(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def maximum(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def min(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def minimum(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def modulo(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MODULO', use_clamp=clamp).value



    def mul_add(self, multiplier=None, addend=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value



    def multiply_add(self, multiplier=None, addend=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


    def not_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL').result


    def ping_pong(self, scale=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp).value


    def pow(self, exponent=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def power(self, exponent=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def sign(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SIGN', use_clamp=clamp).value


    def sin(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sine(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sinh(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINH', use_clamp=clamp).value


    def smooth_maximum(self, value=None, distance=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp).value


    def smooth_minimum(self, value=None, distance=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp).value


    def snap(self, increment=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=increment, value2=None, operation='SNAP', use_clamp=clamp).value


    def sqrt(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SQRT', use_clamp=clamp).value




    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='INT').output


    def tan(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tangent(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tanh(self, value=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANH', use_clamp=clamp).value


    def to_degrees(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='DEGREES', use_clamp=clamp).value


    def to_radians(self, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=None, value2=None, operation='RADIANS', use_clamp=clamp).value


    def to_string(self):
        """

                """

        return nodes.ValueToString(value=self, decimals=0).string


    def wrap(self, max=None, min=None, clamp=False):
        """

                """

        return nodes.Math(value0=self, value1=max, value2=min, operation='WRAP', use_clamp=clamp).value




class Boolean(geosocks.Boolean):
    @classmethod
    def Boolean(cls, boolean=False):
        """

                """

        return cls(nodes.Boolean(boolean=boolean).boolean)


    def b_and(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean


    def b_not(self):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=None, operation='NOT').boolean


    def b_or(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean


    def imply(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean


    def nand(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean


    def nimply(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean


    def nor(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='BOOLEAN').output


    def xnor(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean


    def xor(self, boolean1=None):
        """

                """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean




class String(geosocks.String):
    @staticmethod
    def LineBreak():
        """

                """

        return nodes.SpecialCharacters().line_break


    @classmethod
    def String(cls, string=''):
        """

                """

        return cls(nodes.String(string=string).string)


    @staticmethod
    def Tab():
        """

                """

        return nodes.SpecialCharacters().tab


    def equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='STRING', mode='ELEMENT', operation='EQUAL').result


    def join(*strings, delimiter=None):
        """

                """

        return nodes.JoinStrings(*strings, delimiter=delimiter).string


    @property
    def length(self):
        """

                """

        return nodes.StringLength(string=self).length


    def not_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL').result


    def replace(self, find=None, replace=None):
        """

                """

        return nodes.ReplaceString(string=self, find=find, replace=replace).string


    def slice(self, position=None, length=None):
        """

                """

        return nodes.SliceString(string=self, position=position, length=length).string


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='STRING').output


    def to_curves(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """

                """

        import geonodes as gn
        node = nodes.StringToCurves(string=string, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
        return gn.Instances(node.curve_instances), node.line, node.pivot_point




class Vector(geosocks.Vector):
    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        """

                """

        return cls(nodes.CombineXyz(x=x, y=y, z=z).vector)


    @classmethod
    def Vector(cls, vector=[0.0, 0.0, 0.0]):
        """

                """

        return cls(nodes.Vector(vector=vector).vector)


    def abs(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='ABSOLUTE').vector


    def absolute(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='ABSOLUTE').vector


    def add(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='ADD').vector


    def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """

                """

        return self.stack(nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis))


    def average_equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='EQUAL').result


    def average_greater_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='GREATER_EQUAL').result


    def average_greater_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='GREATER_THAN').result


    def average_less_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='LESS_EQUAL').result


    def average_less_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='LESS_THAN').result


    def average_not_equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='NOT_EQUAL').result


    def ceil(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='CEIL').vector


    def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN'):
        """

                """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation=operation).result


    def cos(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='COSINE').vector


    def cosine(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='COSINE').vector


    def cross(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='CROSS_PRODUCT').vector


    def cross_product(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='CROSS_PRODUCT').vector


    def curves(self, fac=None):
        """

                """

        return nodes.VectorCurves(fac=fac, vector=self).vector


    def direction_equal(self, b=None, angle=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='EQUAL').result


    def direction_greater_equal(self, b=None, angle=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='GREATER_EQUAL').result


    def direction_greater_than(self, b=None, angle=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='GREATER_THAN').result


    def direction_less_equal(self, b=None, angle=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='LESS_EQUAL').result


    def direction_less_than(self, b=None, angle=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='LESS_THAN').result


    def direction_not_equal(self, b=None, angle=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='NOT_EQUAL').result


    def distance(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DISTANCE').value


    def div(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DIVIDE').vector


    def divide(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DIVIDE').vector


    def dot(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DOT_PRODUCT').value


    def dot_product(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DOT_PRODUCT').value


    def dot_product_equal(self, b=None, c=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='EQUAL').result


    def dot_product_greater_equal(self, b=None, c=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_EQUAL').result


    def dot_product_greater_than(self, b=None, c=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_THAN').result


    def dot_product_less_equal(self, b=None, c=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_EQUAL').result


    def dot_product_less_than(self, b=None, c=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_THAN').result


    def dot_product_not_equal(self, b=None, c=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='NOT_EQUAL').result


    def elements_equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='EQUAL').result


    def elements_greater_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL').result


    def elements_greater_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN').result


    def elements_less_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL').result


    def elements_less_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN').result


    def elements_not_equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL').result


    def face_forward(self, incident=None, reference=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=incident, vector2=reference, scale=None, operation='FACEFORWARD').vector


    def floor(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FLOOR').vector


    def fract(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FRACTION').vector


    def fraction(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FRACTION').vector


    @property
    def length(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='LENGTH').value


    def length_equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='EQUAL').result


    def length_greater_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='GREATER_EQUAL').result


    def length_greater_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='GREATER_THAN').result


    def length_less_equal(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='LESS_EQUAL').result


    def length_less_than(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='LESS_THAN').result


    def length_not_equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='NOT_EQUAL').result


    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """

                """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type).vector


    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

                """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='LINEAR').vector


    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

                """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='SMOOTHSTEP').vector


    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

                """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='SMOOTHERSTEP').vector


    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):
        """

                """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='STEPPED').vector


    def max(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MAXIMUM').vector


    def maximum(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MAXIMUM').vector


    def min(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MINIMUM').vector


    def minimum(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MINIMUM').vector


    def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM'):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=vector, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode=factor_mode).result


    def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=vector, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='NON_UNIFORM').result


    def mix_uniform(self, vector=None, clamp_factor=True):
        """

                """

        return nodes.Mix(factor=None, a=self, b=vector, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='UNIFORM').result


    def modulo(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MODULO').vector


    def mul(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MULTIPLY').vector


    def mul_add(self, multiplier=None, addend=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=multiplier, vector2=addend, scale=None, operation='MULTIPLY_ADD').vector


    def multiply(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MULTIPLY').vector


    def multiply_add(self, multiplier=None, addend=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=multiplier, vector2=addend, scale=None, operation='MULTIPLY_ADD').vector


    def normalize(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='NORMALIZE').vector


    def project(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='PROJECT').vector


    def reflect(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='REFLECT').vector


    def refract(self, vector=None, ior=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=ior, operation='REFRACT').vector


    def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):
        """

                """

        return nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=None, invert=invert, rotation_type='AXIS_ANGLE').vector


    def rotate_euler(self, center=None, rotation=None, invert=False):
        """

                """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=None, rotation=rotation, invert=invert, rotation_type='EULER_XYZ').vector


    def rotate_x(self, center=None, angle=None, invert=False):
        """

                """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='X_AXIS').vector


    def rotate_y(self, center=None, angle=None, invert=False):
        """

                """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='Y_AXIS').vector


    def rotate_z(self, center=None, angle=None, invert=False):
        """

                """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='Z_AXIS').vector


    def scale(self, scale=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=scale, operation='SCALE').vector


    @property
    def separate(self):
        """

                """

        if not hasattr(self, '_c_shadernodeseparatexyz'):
            self._c_shadernodeseparatexyz = nodes.SeparateXyz(vector=self)
        return self._c_shadernodeseparatexyz


    def sin(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='SINE').vector


    def sine(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='SINE').vector


    def snap(self, increment=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=increment, vector2=None, scale=None, operation='SNAP').vector


    def sub(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='SUBTRACT').vector


    def subtract(self, vector=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='SUBTRACT').vector


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='VECTOR').output


    def tan(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='TANGENT').vector


    def tangent(self):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='TANGENT').vector


    def wrap(self, max=None, min=None):
        """

                """

        return nodes.VectorMath(vector0=self, vector1=max, vector2=min, scale=None, operation='WRAP').vector




class Color(geosocks.Color):
    @classmethod
    def Color(cls):
        """

                """

        return cls(nodes.Color().color)


    @classmethod
    def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):
        """

                """

        return cls(nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSV').color)


    @classmethod
    def HSV(cls, hue=None, saturation=None, value=None, alpha=None):
        """

                """

        return cls(nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV').color)


    @classmethod
    def RGB(cls, red=None, green=None, blue=None, alpha=None):
        """

                """

        return cls(nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB').color)


    @property
    def alpha(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='RGB').alpha


    @property
    def blue(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='RGB').blue


    def brighter(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER').result


    def darker(self, b=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='RGBA', mode='ELEMENT', operation='DARKER').result


    def equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL').result


    def equal(self, b=None, epsilon=None):
        """

                """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL').result


    @property
    def green(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='RGB').green


    @property
    def hsl(self):
        """

                """

        node = nodes.SeparateColor(color=self, mode='HSL')
        return node.red, node.green, node.blue, node.alpha


    @property
    def hsv(self):
        """

                """

        node = nodes.SeparateColor(color=self, mode='HSV')
        return node.red, node.green, node.blue, node.alpha


    @property
    def hue(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='HSV').red


    @property
    def lightness(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='HSL').blue


    def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

                """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    @property
    def red(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='RGB').red


    @property
    def rgb(self):
        """

                """

        node = nodes.SeparateColor(color=self, mode='RGB')
        return node.red, node.green, node.blue, node.alpha


    @property
    def rgb_curves(self, fac=None):
        """

                """

        return nodes.RgbCurves(fac=fac, color=self)


    @property
    def saturation(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='HSV').green


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='RGBA').output


    @property
    def value(self):
        """

                """

        return nodes.SeparateColor(color=self, mode='HSV').blue




class Collection(geosocks.Collection):
    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='COLLECTION').output




class Object(geosocks.Object):
    @classmethod
    def Self(cls):
        """

                """

        return cls(nodes.SelfObject().self_object)


    def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):
        """

                """

        return nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space).geometry


    def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):
        """

                """

        return nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space)


    def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):
        """

                """

        return nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space).location


    def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):
        """

                """

        return nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space).rotation


    def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):
        """

                """

        return nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space).scale


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='OBJECT').output




class Image(geosocks.Image):
    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='IMAGE').output


    def texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """

                """

        node = nodes.ImageTexture(image=self, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
        return node.color, node.alpha




class Texture(geosocks.Texture):
    @staticmethod
    def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        """

                """

        node = nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return node.color, node.fac


    @staticmethod
    def checker(vector=None, color1=None, color2=None, scale=None):
        """

                """

        node = nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)
        return node.color, node.fac


    @staticmethod
    def gradient(vector=None, gradient_type='LINEAR'):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type=gradient_type)
        return node.color, node.fac


    @staticmethod
    def gradient_diagonal(vector=None):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type='DIAGONAL')
        return node.color, node.fac


    @staticmethod
    def gradient_easing(vector=None):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type='EASING')
        return node.color, node.fac


    @staticmethod
    def gradient_linear(vector=None):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type='LINEAR')
        return node.color, node.fac


    @staticmethod
    def gradient_quadratic(vector=None):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type='QUADRATIC')
        return node.color, node.fac


    @staticmethod
    def gradient_quadratic_sphere(vector=None):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type='QUADRATIC_SPHERE')
        return node.color, node.fac


    @staticmethod
    def gradient_radial(vector=None):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type='RADIAL')
        return node.color, node.fac


    @staticmethod
    def gradient_spherical(vector=None):
        """

                """

        node = nodes.GradientTexture(vector=vector, gradient_type='SPHERICAL')
        return node.color, node.fac


    @staticmethod
    def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """

                """

        node = nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
        return node.color, node.alpha


    @staticmethod
    def magic(vector=None, scale=None, distortion=None, turbulence_depth=2):
        """

                """

        node = nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)
        return node.color, node.fac


    @staticmethod
    def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        """

                """

        return nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).fac


    @staticmethod
    def noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        """

                """

        node = nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)
        return node.color, node.fac


    @staticmethod
    def noise_1D(w=None, scale=None, detail=None, roughness=None, distortion=None):
        """

                """

        node = nodes.NoiseTexture(vector=None, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='1D')
        return node.color, node.fac


    @staticmethod
    def noise_2D(vector=None, scale=None, detail=None, roughness=None, distortion=None):
        """

                """

        node = nodes.NoiseTexture(vector=vector, w=None, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='2D')
        return node.color, node.fac


    @staticmethod
    def noise_3D(vector=None, scale=None, detail=None, roughness=None, distortion=None):
        """

                """

        node = nodes.NoiseTexture(vector=vector, w=None, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='3D')
        return node.color, node.fac


    @staticmethod
    def noise_4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None):
        """

                """

        node = nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='4D')
        return node.color, node.fac


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='TEXTURE').output


    @staticmethod
    def voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

                """

        node = nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position, node.w


    @staticmethod
    def voronoi_1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

                """

        node = nodes.VoronoiTexture(vector=None, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.w


    @staticmethod
    def voronoi_2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

                """

        node = nodes.VoronoiTexture(vector=vector, w=None, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position


    @staticmethod
    def voronoi_3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

                """

        node = nodes.VoronoiTexture(vector=vector, w=None, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position


    @staticmethod
    def voronoi_4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

                """

        node = nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position, node.w


    @staticmethod
    def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return node.color, node.fac


    @staticmethod
    def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile=wave_profile, wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile='SAW', wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile='SIN', wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile='TRI', wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile=wave_profile, wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile='SAW', wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile='SIN', wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

                """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile='TRI', wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def white_noise(vector=None, w=None, noise_dimensions='3D'):
        """

                """

        node = nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions)
        return node.value, node.color


    @staticmethod
    def white_noise_1D(w=None):
        """

                """

        node = nodes.WhiteNoiseTexture(vector=None, w=w, noise_dimensions='1D')
        return node.value, node.color


    @staticmethod
    def white_noise_2D(vector=None):
        """

                """

        node = nodes.WhiteNoiseTexture(vector=vector, w=None, noise_dimensions='2D')
        return node.value, node.color


    @staticmethod
    def white_noise_3D(vector=None):
        """

                """

        node = nodes.WhiteNoiseTexture(vector=vector, w=None, noise_dimensions='3D')
        return node.value, node.color


    @staticmethod
    def white_noise_4D(vector=None, w=None):
        """

                """

        node = nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions='3D')
        return node.value, node.color




class Material(geosocks.Material):
    @classmethod
    def Material(cls):
        """

                """

        return cls(nodes.Material().material)


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='MATERIAL').output




class Geometry(geosocks.Geometry):
    @classmethod
    def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """

                """

        return cls(nodes.CollectionInfo(collection=collection, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).geometry)


    @property
    def ID(self):
        """

                """

        return self.attribute_node(nodes.ID()).ID


    def attribute_statistic(self, selection=None, attribute=None, domain='POINT'):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type_, domain=domain)


    @property
    def bounding_box(self):
        """

                """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeboundbox'):
            self._c_geometrynodeboundbox = nodes.BoundingBox(geometry=self)
        return gn.Mesh(self._c_geometrynodeboundbox.bounding_box)


    @property
    def bounding_box_min(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeboundbox'):
            self._c_geometrynodeboundbox = nodes.BoundingBox(geometry=self)
        return self._c_geometrynodeboundbox.min


    @property
    def bounding_box_min(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeboundbox'):
            self._c_geometrynodeboundbox = nodes.BoundingBox(geometry=self)
        return self._c_geometrynodeboundbox.max


    def capture_attribute(self, value=None, domain='POINT'):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.stack(nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type_, domain=domain)).node.attribute


    def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT'):
        """

                """

        return nodes.CaptureAttribute(geometry=geometry, value=value, data_type=data_type, domain=domain)


    @property
    def convex_hull(self):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.ConvexHull(geometry=self).convex_hull)


    @property
    def curve_component(self):
        """

                """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Curve(self._c_geometrynodeseparatecomponents.curve)


    def delete(self, selection=None, domain='POINT', mode='ALL'):
        """

                """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))


    @property
    def domain_size(self, component='MESH'):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component=component)
        return self._c_geometrynodeattributedomainsize


    def duplicate(self, selection=None, amount=None, domain='POINT'):
        """

                """

        return self.stack(nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain=domain)).node.duplicate_index


    def field_at_index(self, index=None, value=None, domain='POINT'):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.FieldAtIndex(index=index, value=value, data_type=data_type_, domain=domain)).value


    def get_named_boolean(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='BOOLEAN')).attribute


    def get_named_color(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR')).attribute


    def get_named_float(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT')).attribute


    def get_named_integer(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='INT')).attribute


    def get_named_vector(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR')).attribute


    @property
    def index(self):
        """

                """

        return self.attribute_node(nodes.Index()).index


    @property
    def instances_component(self):
        """

                """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Instances(self._c_geometrynodeseparatecomponents.instances)


    def interpolate_domain(self, value=None, domain='POINT'):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.InterpolateDomain(value=value, data_type=data_type_, domain=domain)).value


    @property
    def is_viewport(self):
        """

                """

        return self.attribute_node(nodes.IsViewport()).is_viewport


    def join(*geometry):
        """

                """

        self = geometry[0]

        return self.stack(nodes.JoinGeometry(*geometry))


    @property
    def material_index(self):
        """

                """

        return self.attribute_node(nodes.MaterialIndex()).material_index


    def material_selection(self, material=None):
        """

                """

        return self.attribute_node(nodes.MaterialSelection(material=material)).selection


    def merge_by_distance(self, selection=None, distance=None, mode='ALL'):
        """

                """

        return self.stack(nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode))


    @property
    def mesh_component(self):
        """

                """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Mesh(self._c_geometrynodeseparatecomponents.mesh)


    def named_attribute(self, name=None, data_type='FLOAT'):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type=data_type)).attribute


    @property
    def normal(self):
        """

                """

        return self.attribute_node(nodes.Normal()).normal


    @property
    def points_component(self):
        """

                """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Points(self._c_geometrynodeseparatecomponents.point_cloud)


    @property
    def position(self):
        """

                """

        return self.attribute_node(nodes.Position()).position


    def proximity(self, target=None, source_position=None, target_element='FACES'):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element=target_element)).distance


    def proximity_edges(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='EDGES')).distance


    def proximity_faces(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='FACES')).distance


    def proximity_points(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='POINTS')).distance


    @property
    def radius(self):
        """

                """

        return self.attribute_node(nodes.Radius()).radius


    def random_boolean(self, probability=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN')).value


    def random_float(self, min=None, max=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT')).value


    def random_integer(self, min=None, max=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT')).value


    def random_vector(self, min=None, max=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR')).value


    def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping=mapping))


    def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping='INTERPOLATED'))


    def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping='NEAREST'))


    def remove_named_attribute(self, name=None):
        """

                """

        return self.stack(nodes.RemoveNamedAttribute(geometry=self, name=name))


    def replace_material(self, old=None, new=None):
        """

                """

        return self.stack(nodes.ReplaceMaterial(geometry=self, old=old, new=new))


    def sample_index(self, value=None, index=None, clamp=False, domain='POINT'):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type=data_type_, domain=domain).value


    def sample_nearest(self, sample_position=None, domain='POINT'):
        """

                """

        return nodes.SampleNearest(geometry=self, sample_position=sample_position, domain=domain).index


    def separate(self, geometry=None, selection=None, domain='POINT'):
        """

                """

        node = nodes.SeparateGeometry(geometry=geometry, selection=selection, domain=domain)
        return node.selection, node.inverted


    @property
    def separate_components(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return self._c_geometrynodeseparatecomponents


    def set_ID(self, selection=None, ID=None):
        """

                """

        return self.stack(nodes.SetID(geometry=self, selection=selection, ID=ID))


    def set_material(self, selection=None, material=None):
        """

                """

        return self.stack(nodes.SetMaterial(geometry=self, selection=selection, material=material))


    def set_material_index(self, selection=None, material_index=None):
        """

                """

        return self.stack(nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index))


    def set_named_boolean(self, name=None, value=None, domain='POINT'):
        """

                """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BOOLEAN', domain=domain))


    def set_named_color(self, name=None, value=None, domain='POINT'):
        """

                """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_COLOR', domain=domain))


    def set_named_float(self, name=None, value=None, domain='POINT'):
        """

                """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT', domain=domain))


    def set_named_integer(self, name=None, value=None, domain='POINT'):
        """

                """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='INT', domain=domain))


    def set_named_vector(self, name=None, value=None, domain='POINT'):
        """

                """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_VECTOR', domain=domain))


    def set_position(self, selection=None, position=None, offset=None):
        """

                """

        return self.stack(nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset))


    def store_named_attribute(self, name=None, value=None, domain='POINT'):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type=data_type_, domain=domain))


    def switch(self, switch=None, true=None):
        """

                """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='GEOMETRY').output


    def to_instance(*geometry):
        """

                """

        import geonodes as gn
        return gn.Instances(nodes.GeometryToInstance(*geometry).instances)


    def transform(self, translation=None, rotation=None, scale=None):
        """

                """

        return self.stack(nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale))


    @property
    def volume_component(self):
        """

                """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Volume(self._c_geometrynodeseparatecomponents.volume)




class Mesh(Geometry):
    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
        """

                """

        return cls(nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).mesh)


    @staticmethod
    def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """

                """

        import geonodes as gn
        node = nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)
        return gn.Mesh(node.mesh), node.top, node.bottom, node.side


    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """

                """

        return cls(nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).mesh)


    @staticmethod
    def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """

                """

        import geonodes as gn
        node = nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)
        return gn.Mesh(node.mesh), node.top, node.bottom, node.side


    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """

                """

        return cls(nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).mesh)


    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        """

                """

        return cls(nodes.IcoSphere(radius=radius, subdivisions=subdivisions).mesh)


    @classmethod
    def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """

                """

        return cls(nodes.MeshLine(count=count, resolution=resolution, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).mesh)


    @classmethod
    def LineEndPoints(cls, count=None, start_location=None, end_location=None):
        """

                """

        return cls(nodes.MeshLine(count=count, resolution=None, start_location=start_location, offset=end_location, count_mode='TOTAL', mode='END_POINTS').mesh)


    @classmethod
    def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):
        """

                """

        return cls(nodes.MeshLine(count=None, resolution=resolution, start_location=start_location, offset=end_location, count_mode='RESOLUTION', mode='END_POINTS').mesh)


    @classmethod
    def LineOffset(cls, count=None, start_location=None, offset=None):
        """

                """

        return cls(nodes.MeshLine(count=count, resolution=None, start_location=start_location, offset=offset, count_mode='TOTAL', mode='OFFSET').mesh)


    @classmethod
    def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None):
        """

                """

        return cls(nodes.MeshLine(count=None, resolution=resolution, start_location=start_location, offset=offset, count_mode='RESOLUTION', mode='OFFSET').mesh)


    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        """

                """

        return cls(nodes.UvSphere(segments=segments, rings=rings, radius=radius).mesh)


    def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """

                """

        return self.stack(nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE')).node.intersecting_edges


    def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):
        """

                """

        self = mesh_2[0]

        return self.stack(nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT')).node.intersecting_edges


    def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):
        """

                """

        self = mesh_2[0]

        return self.stack(nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION')).node.intersecting_edges


    @property
    def corner_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.face_corner_count


    def corners_of_face(self, face_index=None, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.CornersOfFace(face_index=face_index, weights=weights, sort_index=sort_index))
        return node.corner_index, node.total


    def corners_of_vertex(self, vertex_index=None, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.CornersOfVertex(vertex_index=vertex_index, weights=weights, sort_index=sort_index))
        return node.corner_index, node.total


    def delete_all(self, selection=None, domain='POINT'):
        """

                """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='ALL'))


    def delete_edges(self, selection=None, domain='POINT'):
        """

                """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='EDGE_FACE'))


    def delete_faces(self, selection=None, domain='POINT'):
        """

                """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='ONLY_FACE'))


    def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """

                """

        import geonodes as gn
        node = nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method)
        return gn.Points(node.points), node.normal, node.rotation


    @property
    def domain_size(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize


    def dual_mesh(self, mesh=None, keep_boundaries=None):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.DualMesh(mesh=mesh, keep_boundaries=keep_boundaries).dual_mesh)


    @property
    def edge_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.edge_count


    def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """

                """

        import geonodes as gn
        return gn.Curve(self.attribute_node(nodes.EdgePathsToCurves(mesh=self, start_vertices=start_vertices, next_vertex_index=next_vertex_index)).curves)


    def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):
        """

                """

        return nodes.EdgePathsToSelection(start_vertices=start_vertices, next_vertex_index=next_vertex_index).selection


    def edges_of_corner(self, corner_index=None):
        """

                """

        node = self.attribute_node(nodes.EdgesOfCorner(corner_index=corner_index))
        return node.next_edge_index, node.previous_edge_index


    def edges_of_vertex(self, vertex_index=None, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.EdgesOfVertex(vertex_index=vertex_index, weights=weights, sort_index=sort_index))
        return node.edge_index, node.total


    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """

                """

        node = self.stack(nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)).node
        return node.top, node.side


    @property
    def face_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.face_count


    def face_is_planar(self, threshold=None):
        """

                """

        return self.attribute_node(nodes.FaceIsPlanar(threshold=threshold)).planar


    def face_of_corner(self, corner_index=None):
        """

                """

        node = self.attribute_node(nodes.FaceOfCorner(corner_index=corner_index))
        return node.face_index, node.index_in_face


    def face_set_boundaries(self, face_set=None):
        """

                """

        return self.attribute_node(nodes.FaceSetBoundaries(face_set=face_set)).boundary_edges


    def flip_faces(self, selection=None):
        """

                """

        return self.stack(nodes.FlipFaces(mesh=self, selection=selection))


    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def is_shade_smooth(self):
        """

                """

        return self.attribute_node(nodes.IsShadeSmooth()).smooth


    @property
    def island(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland


    @property
    def island_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_count


    @property
    def island_index(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_index


    def offset_corner_in_face(self, corner_index=None, offset=None):
        """

                """

        return self.attribute_node(nodes.OffsetCornerInFace(corner_index=corner_index, offset=offset)).corner_index


    def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):
        """

                """

        return self.attribute_node(nodes.PackUvIslands(uv=uv, selection=selection, margin=margin, rotate=rotate)).uv


    @property
    def point_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.point_count


    def sample_nearest_surface(self, value=None, sample_position=None):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type=data_type_).value


    def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        node = nodes.SampleUvSurface(mesh=self, value=value, source_uv_map=source_uv_map, sample_uv=sample_uv, data_type=data_type_)
        return node.value, node.is_valid


    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """

                """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode))


    def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):
        """

                """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):
        """

                """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=None, domain=domain, scale_mode='UNIFORM'))


    def set_shade_smooth(self, selection=None, shade_smooth=None):
        """

                """

        return self.stack(nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))


    def shortest_edge_paths(self, end_vertex=None, edge_cost=None):
        """

                """

        node = self.attribute_node(nodes.ShortestEdgePaths(end_vertex=end_vertex, edge_cost=edge_cost))
        return node.next_vertex_index, node.total_cost


    def split_edges(self, selection=None):
        """

                """

        return self.stack(nodes.SplitEdges(mesh=self, selection=selection))


    def subdivide(self, level=None):
        """

                """

        return self.stack(nodes.SubdivideMesh(mesh=self, level=level))


    def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """

                """

        return self.stack(nodes.SubdivisionSurface(mesh=self, level=level, edge_crease=edge_crease, vertex_crease=vertex_crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))


    def to_curve(self, selection=None):
        """

                """

        import geonodes as gn
        return gn.Curve(nodes.MeshToCurve(mesh=self, selection=selection).curve)


    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):
        """

                """

        import geonodes as gn
        return gn.Points(nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode).points)


    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):
        """

                """

        import geonodes as gn
        return gn.Volume(nodes.MeshToVolume(mesh=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, exterior_band_width=exterior_band_width, interior_band_width=interior_band_width, fill_volume=fill_volume, resolution_mode=resolution_mode).volume)


    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """

                """

        return self.stack(nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))


    def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """

                """

        return self.attribute_node(nodes.UvUnwrap(selection=selection, seam=seam, margin=margin, fill_holes=fill_holes, method=method)).uv


    def vertex_of_corner(self, corner_index=None):
        """

                """

        return self.attribute_node(nodes.VertexOfCorner(corner_index=corner_index)).vertex_index




class Curve(Geometry):
    @classmethod
    def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """

                """

        return cls(nodes.Arc(resolution=resolution, start=None, middle=None, end=None, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, offset_angle=None, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS').curve)


    @classmethod
    def ArcFromPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """

                """

        return nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, radius=None, start_angle=None, sweep_angle=None, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')


    @classmethod
    def Circle(cls, resolution=None, radius=None):
        """

                """

        return cls(nodes.CurveCircle(resolution=resolution, point_1=None, point_2=None, point_3=None, radius=radius, mode='RADIUS').curve)


    @classmethod
    def CircleFromPoints(cls, resolution=None, point_1=None, point_2=None, point_3=None):
        """

                """

        return nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=None, mode='POINTS')


    @classmethod
    def Line(cls, start=None, end=None):
        """

                """

        return cls(nodes.CurveLine(start=start, end=end, direction=None, length=None, mode='POINTS').curve)


    @classmethod
    def LineDirection(cls, start=None, direction=None, length=None):
        """

                """

        return cls(nodes.CurveLine(start=start, end=None, direction=direction, length=length, mode='DIRECTION').curve)


    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """

                """

        return cls(nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).curve)


    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
        """

                """

        return cls(nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode).curve)


    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """

                """

        return cls(nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).curve)


    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """

                """

        return nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)


    @classmethod
    def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """

                """

        return cls(nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).curve)


    def curve_of_point(self, point_index=None):
        """

                """

        node = self.attribute_node(nodes.CurveOfPoint(point_index=point_index))
        return node.curve_index, node.index_in_curve


    def deform_on_surface(self):
        """

                """

        return self.stack(nodes.DeformCurvesOnSurface(curves=self))


    @property
    def domain_size(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='CURVE')
        return self._c_geometrynodeattributedomainsize


    def fill(self, curve=None, mode='TRIANGLES'):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.FillCurve(curve=curve, mode=mode).mesh)


    def fill_ngons(self, curve=None):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.FillCurve(curve=curve, mode='NGONS').mesh)


    def fill_triangles(self, curve=None):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.FillCurve(curve=curve, mode='TRIANGLES').mesh)


    def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """

                """

        return self.stack(nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode))


    def fillet_bezier(self, radius=None, limit_radius=None):
        """

                """

        return self.stack(nodes.FilletCurve(curve=self, count=1, radius=radius, limit_radius=limit_radius, mode='BEZIER'))


    def fillet_poly(self, count=None, radius=None, limit_radius=None):
        """

                """

        return self.stack(nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode='POLY'))


    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    @property
    def length(self):
        """

                """

        return nodes.CurveLength(curve=self).length


    def offset_point(self, point_index=None, offset=None):
        """

                """

        node = self.attribute_node(nodes.OffsetPointInCurve(point_index=point_index, offset=offset))
        return node.is_valid_offset, node.point_index


    @property
    def point_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='CURVE')
        return self._c_geometrynodeattributedomainsize.point_count


    def points_of_curve(self, curve_index=None, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.PointsOfCurve(curve_index=curve_index, weights=weights, sort_index=sort_index))
        return node.point_index, node.total


    def resample(self, selection=None, count=None, length=None, mode='COUNT'):
        """

                """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode))


    def resample_count(self, selection=None, count=None):
        """

                """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=count, length=0.1, mode='COUNT'))


    def resample_evaluated(self, selection=None):
        """

                """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=10, length=0.1, mode='EVALUATED'))


    def resample_length(self, selection=None, length=None):
        """

                """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=10, length=length, mode='LENGTH'))


    def reverse(self, selection=None):
        """

                """

        return self.stack(nodes.ReverseCurve(curve=self, selection=selection))


    def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):
        """

                """

        return self.stack(nodes.SampleCurve(curves=self, value=value, factor=factor, length=length, curve_index=curve_index, data_type=data_type, mode=mode, use_all_curves=use_all_curves))


    @property
    def spline_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='CURVE')
        return self._c_geometrynodeattributedomainsize.spline_count


    def subdivide(self, cuts=None):
        """

                """

        return self.stack(nodes.SubdivideCurve(curve=self, cuts=cuts))


    def to_mesh(self, profile_curve=None, fill_caps=None):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).mesh)


    def to_points(self, count=None, length=None, mode='COUNT'):
        """

                """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode)
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def to_points_count(self, count=None):
        """

                """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=count, length=0.1, mode='COUNT')
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def to_points_evaluated(self):
        """

                """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=10, length=0.1, mode='EVALUATED')
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def to_points_length(self, length=None):
        """

                """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=10, length=length, mode='LENGTH')
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def trim(self, start=None, end=None, mode='FACTOR'):
        """

                """

        return self.stack(nodes.TrimCurve(curve=self, start0=start, start1=start, end0=start, end1=end, mode=mode))


    def trim_factor(self, start=None, end=None):
        """

                """

        return self.stack(nodes.TrimCurve(curve=self, start0=start, start1=None, end0=end, end1=None, mode='FACTOR'))


    def trim_length(self, start=None, end=None):
        """

                """

        return self.stack(nodes.TrimCurve(curve=self, start0=None, start1=start, end0=None, end1=end, mode='LENGTH'))




class Points(Geometry):
    @classmethod
    def Points(cls, count=None, position=None, radius=None):
        """

                """

        return cls(nodes.Points(count=count, position=position, radius=radius).geometry)


    @property
    def domain_size(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='POINTCLOUD')
        return self._c_geometrynodeattributedomainsize.point_count


    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def set_point_radius(self, selection=None, radius=None):
        """

                """

        return self.stack(nodes.SetPointRadius(points=self, selection=selection, radius=radius))


    def to_vertices(self, points=None, selection=None):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.PointsToVertices(points=points, selection=selection).mesh)


    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """

                """

        import geonodes as gn
        return gn.Volume(nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume)


    def to_volume_amount(self, density=None, voxel_amount=None, radius=None):
        """

                """

        import geonodes as gn
        return gn.Volume(nodes.PointsToVolume(points=self, density=density, voxel_size=None, voxel_amount=voxel_amount, radius=radius, resolution_mode='VOXEL_AMOUNT').volume)


    def to_volume_size(self, density=None, voxel_size=None, radius=None):
        """

                """

        import geonodes as gn
        return gn.Volume(nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=None, radius=radius, resolution_mode='VOXEL_SIZE').volume)




class Instances(Geometry):
    @classmethod
    def InstanceOnPoints(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        return cls(nodes.InstanceOnPoints(points=points, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    @property
    def domain_size(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='INSTANCES')
        return self._c_geometrynodeattributedomainsize.instance_count


    def on_points(self, points=None, selection=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        return nodes.InstanceOnPoints(points=points, selection=selection, instance=self, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def realize(self, geometry=None, legacy_behavior=False):
        """

                """

        return nodes.RealizeInstances(geometry=geometry, legacy_behavior=legacy_behavior).geometry


    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """

                """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))


    @property
    def rotation(self):
        """

                """

        return self.attribute_node(nodes.InstanceRotation()).rotation


    @property
    def scale(self):
        """

                """

        return self.attribute_node(nodes.InstanceScale()).scale


    def set_scale(self, selection=None, scale=None, center=None, local_space=None):
        """

                """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))


    def to_points(self, selection=None, position=None, radius=None):
        """

                """

        import geonodes as gn
        return gn.Points(nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius).points)


    def translate(self, selection=None, translation=None, local_space=None):
        """

                """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))




class Volume(Geometry):
    @classmethod
    def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):
        """

                """

        return cls(nodes.VolumeCube(density=density, background=background, min=min, max=max, resolution_x=resolution_x, resolution_y=resolution_y, resolution_z=resolution_z).volume)


    def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):
        """

                """

        import geonodes as gn
        return gn.Points(nodes.DistributePointsInVolume(volume=self, density=density, seed=seed, spacing=spacing, threshold=threshold, mode=mode).points)


    def distribute_points_grid(self, spacing=None, threshold=None):
        """

                """

        import geonodes as gn
        return gn.Points(nodes.DistributePointsInVolume(volume=self, density=None, seed=None, spacing=spacing, threshold=threshold, mode='DENSITY_GRID').points)


    def distribute_points_random(self, density=None, seed=None):
        """

                """

        import geonodes as gn
        return gn.Points(nodes.DistributePointsInVolume(volume=self, density=density, seed=seed, spacing=None, threshold=None, mode='DENSITY_RANDOM').points)


    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh)




