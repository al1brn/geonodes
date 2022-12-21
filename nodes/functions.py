from geonodes.nodes import nodes

def abs(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


def absolute(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


def add(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='ADD', use_clamp=clamp).value


def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
    """ Node AlignEulerToVector.

    Node reference [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html)
    Developer reference [FunctionNodeAlignEulerToVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

    Args:
        rotation: Vector
        factor: Float
        vector: Vector
        axis (str): 'X' in [X, Y, Z]
        pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

    Returns:
        socket `rotation`
    """
    return nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).rotation


def arccos(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


def arccosine(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


def arcsin(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ARCSINE', use_clamp=clamp).value


def arcsine(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ARCSINE', use_clamp=clamp).value


def arctan(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


def arctan2(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp).value


def arctangent(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


def b_and(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='AND').boolean


def b_not(boolean0=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=None, operation='NOT').boolean


def b_or(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='OR').boolean


def clamp(value=None, min=None, max=None, clamp_type='MINMAX'):
    """ Node Clamp.

    Node reference [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
    Developer reference [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

    Args:
        value: Float
        min: Float
        max: Float
        clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

    Returns:
        socket `result`
    """
    return nodes.Clamp(value=value, min=min, max=max, clamp_type=clamp_type).result


def clamp_min_max(value=None, min=None, max=None):
    """ Node Clamp.

    Node reference [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
    Developer reference [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

    Args:
        value: Float
        min: Float
        max: Float

    Returns:
        socket `result`
    """
    return nodes.Clamp(value=value, min=min, max=max, clamp_type='MINMAX').result


def clamp_range(value=None, min=None, max=None):
    """ Node Clamp.

    Node reference [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
    Developer reference [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

    Args:
        value: Float
        min: Float
        max: Float

    Returns:
        socket `result`
    """
    return nodes.Clamp(value=value, min=min, max=max, clamp_type='RANGE').result


def color_add(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_burn(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_color(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_darken(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_difference(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_divide(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_dodge(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_hue(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_lighten(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_linear_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_multiply(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_overlay(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_ramp(fac=None):
    """ Node ColorRamp.

    Node reference [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html)
    Developer reference [ShaderNodeValToRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)

    Args:
        fac: Float

    Returns:
        node with sockets ['color', 'alpha']
    """
    return nodes.ColorRamp(fac=fac)


def color_saturation(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_screen(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_soft_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_subtract(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def color_value(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        clamp_result (bool): False

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM').result


def combine_hsl(hue=None, saturation=None, lightness=None, alpha=None):
    """ Node CombineColor.

    Node reference [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
    Developer reference [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

    Args:
        hue: Float
        saturation: Float
        lightness: Float
        alpha: Float

    Returns:
        socket `color`
    """
    return nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSL').color


def combine_hsv(hue=None, saturation=None, value=None, alpha=None):
    """ Node CombineColor.

    Node reference [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
    Developer reference [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

    Args:
        hue: Float
        saturation: Float
        value: Float
        alpha: Float

    Returns:
        socket `color`
    """
    return nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV').color


def combine_rgb(red=None, green=None, blue=None, alpha=None):
    """ Node CombineColor.

    Node reference [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
    Developer reference [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

    Args:
        red: Float
        green: Float
        blue: Float
        alpha: Float

    Returns:
        socket `color`
    """
    return nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB').color


def compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):
    """ Node Compare.

    Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
    Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

    Args:
        a: ['Float', 'Integer', 'Vector', 'Color', 'String']
        b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        c: Float
        angle: Float
        epsilon: Float
        data_type (str): 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
        mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
        operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

    Returns:
        socket `result`
    """
    return nodes.Compare(a=a, b=b, c=c, angle=angle, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation).result


def cos(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='COSINE', use_clamp=clamp).value


def cosh(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='COSH', use_clamp=clamp).value


def cosine(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='COSINE', use_clamp=clamp).value


def div(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='DIVIDE', use_clamp=clamp).value


def divide(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='DIVIDE', use_clamp=clamp).value


def exp(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


def exponent(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


def float_mix(factor=None, a=None, b=None, clamp_factor=True):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM').result


def fraction(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


def geometry_to_instance(*geometry):
    """ Node GeometryToInstance.

    Node reference [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)
    Developer reference [GeometryNodeGeometryToInstance](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

    Args:
        geometry: <m>Geometry

    Returns:
        socket `instances` [Instances](Instances.md)
    """
    return Instances(nodes.GeometryToInstance(*geometry).instances)


def imply(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='IMPLY').boolean


def inverse_sqrt(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp).value


def join_geometry(*geometry):
    """ Node JoinGeometry.

    Node reference [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)
    Developer reference [GeometryNodeJoinGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

    Args:
        geometry: <m>Geometry

    Returns:
        socket `geometry`
    """
    return nodes.JoinGeometry(*geometry).geometry


def join_strings(*strings, delimiter=None):
    """ Node JoinStrings.

    Node reference [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html)
    Developer reference [GeometryNodeStringJoin](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)

    Args:
        strings: <m>String
        delimiter: String

    Returns:
        socket 'string'
    """
    return nodes.JoinStrings(*strings, delimiter=delimiter).string


def log(value=None, base=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        base: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


def logarithm(value=None, base=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        base: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


def math(value0=None, value1=None, value2=None, operation='ADD', clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        value2: Float
        operation (str): 'ADD' in [ADD, SUBTRACT, MULTIPLY, DIVIDE,... , TANH, RADIANS, DEGREES]
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp).value


def math_ceil(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='CEIL', use_clamp=clamp).value


def math_compare(value0=None, value1=None, epsilon=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        epsilon: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=epsilon, operation='COMPARE', use_clamp=clamp).value


def math_floor(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='FLOOR', use_clamp=clamp).value


def math_greater_than(value=None, threshold=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        threshold: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp).value


def math_less_than(value=None, threshold=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        threshold: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp).value


def math_round(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='ROUND', use_clamp=clamp).value


def math_trun(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


def math_truncate(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


def max(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='MAXIMUM', use_clamp=clamp).value


def maximum(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='MAXIMUM', use_clamp=clamp).value


def min(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='MINIMUM', use_clamp=clamp).value


def minimum(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='MINIMUM', use_clamp=clamp).value


def modulo(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='MODULO', use_clamp=clamp).value


def mul(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='MULTIPLY', use_clamp=clamp).value


def mul_add(value=None, multiplier=None, addend=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        multiplier: Float
        addend: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


def multiply(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='MULTIPLY', use_clamp=clamp).value


def multiply_add(value=None, multiplier=None, addend=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        multiplier: Float
        addend: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


def nand(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NAND').boolean


def nimply(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NIMPLY').boolean


def nor(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NOR').boolean


def ping_pong(value=None, scale=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        scale: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp).value


def power(base=None, exponent=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        base: Float
        exponent: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=base, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


def random_boolean(probability=None, ID=None, seed=None):
    """ Node RandomValue.

    Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
    Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

    Args:
        probability: Float
        ID: Integer
        seed: Integer

    Returns:
        socket `value`
    """
    return nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value


def random_float(min=None, max=None, ID=None, seed=None):
    """ Node RandomValue.

    Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
    Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

    Args:
        min: ['Vector', 'Float', 'Integer']
        max: ['Vector', 'Float', 'Integer']
        ID: Integer
        seed: Integer

    Returns:
        socket `value`
    """
    return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT').value


def random_integer(min=None, max=None, ID=None, seed=None):
    """ Node RandomValue.

    Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
    Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

    Args:
        min: ['Vector', 'Float', 'Integer']
        max: ['Vector', 'Float', 'Integer']
        ID: Integer
        seed: Integer

    Returns:
        socket `value`
    """
    return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT').value


def random_vector(min=None, max=None, ID=None, seed=None):
    """ Node RandomValue.

    Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
    Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

    Args:
        min: ['Vector', 'Float', 'Integer']
        max: ['Vector', 'Float', 'Integer']
        ID: Integer
        seed: Integer

    Returns:
        socket `value`
    """
    return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value


def replace_string(string=None, find=None, replace=None):
    """ Node ReplaceString.

    Node reference [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html)
    Developer reference [FunctionNodeReplaceString](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)

    Args:
        string: String
        find: String
        replace: String

    Returns:
        socket 'string'
    """
    return nodes.ReplaceString(string=string, find=find, replace=replace).string


def rgb_curves(fac=None, color=None):
    """ Node RgbCurves.

    Node reference [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html)
    Developer reference [ShaderNodeRGBCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)

    Args:
        fac: Float
        color: Color

    Returns:
        node with sockets ['color']
    """
    return nodes.RgbCurves(fac=fac, color=color)


def rotate_axis_angle(rotation=None, axis=None, angle=None, space='OBJECT'):
    """ Node RotateEuler.

    Node reference [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html)
    Developer reference [FunctionNodeRotateEuler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)

    Args:
        rotation: Vector
        axis: Vector
        angle: Float
        space (str): 'OBJECT' in [OBJECT, LOCAL]

    Returns:
        socket `rotation`
    """
    return nodes.RotateEuler(rotation=rotation, rotate_by=None, axis=axis, angle=angle, space=space, type=AXIS_ANGLE).rotation


def rotate_euler(rotation=None, rotate_by=None, space='OBJECT'):
    """ Node RotateEuler.

    Node reference [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html)
    Developer reference [FunctionNodeRotateEuler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)

    Args:
        rotation: Vector
        rotate_by: Vector
        space (str): 'OBJECT' in [OBJECT, LOCAL]

    Returns:
        socket `rotation`
    """
    return nodes.RotateEuler(rotation=rotation, rotate_by=rotate_by, axis=None, angle=None, space=space, type=EULER).rotation


def separate_hsl(color=None):
    """ Node SeparateColor.

    Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
    Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

    Args:
        color: Color

    Returns:
        tuple ('red', 'green', 'blue', 'alpha')
    """
    node = nodes.SeparateColor(color=color, mode='HSL')
    return node.red, node.green, node.blue, node.alpha


def separate_hsv(color=None):
    """ Node SeparateColor.

    Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
    Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

    Args:
        color: Color

    Returns:
        tuple ('red', 'green', 'blue', 'alpha')
    """
    node = nodes.SeparateColor(color=color, mode='HSV')
    return node.red, node.green, node.blue, node.alpha


def separate_rgb(color=None):
    """ Node SeparateColor.

    Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
    Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

    Args:
        color: Color

    Returns:
        tuple ('red', 'green', 'blue', 'alpha')
    """
    node = nodes.SeparateColor(color=color, mode='RGB')
    return node.red, node.green, node.blue, node.alpha


def sign(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='SIGN', use_clamp=clamp).value


def sin(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='SINE', use_clamp=clamp).value


def sine(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='SINE', use_clamp=clamp).value


def sinh(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='SINH', use_clamp=clamp).value


def slice_string(string=None, position=None, length=None):
    """ Node SliceString.

    Node reference [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html)
    Developer reference [FunctionNodeSliceString](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)

    Args:
        string: String
        position: Integer
        length: Integer

    Returns:
        socket 'string'
    """
    return nodes.SliceString(string=string, position=position, length=length).string


def smooth_maximum(value0=None, value1=None, distance=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        distance: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp).value


def smooth_minimum(value0=None, value1=None, distance=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        distance: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp).value


def snap(value=None, increment=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        increment: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=increment, value2=None, operation='SNAP', use_clamp=clamp).value


def sqrt(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='SQRT', use_clamp=clamp).value


def string_length(string=None):
    """ Node StringLength.

    Node reference [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html)
    Developer reference [FunctionNodeStringLength](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)

    Args:
        string: String

    Returns:
        socket 'length'
    """
    return nodes.StringLength(string=string).length


def string_to_curves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
    """ Node StringToCurves.

    Node reference [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html)
    Developer reference [GeometryNodeStringToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)

    Args:
        string: String
        size: Float
        character_spacing: Float
        word_spacing: Float
        line_spacing: Float
        text_box_width: Float
        text_box_height: Float
        align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
        align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
        overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
        pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]

    Returns:
        tuple ('curve_instances', 'line', 'pivot_point')
    """
    node = nodes.StringToCurves(string=string, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
    return Instances(node.curve_instances), node.line, node.pivot_point


def sub(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='SUBTRACT', use_clamp=clamp).value


def subtract(value0=None, value1=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value0: Float
        value1: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value0, value1=value1, value2=None, operation='SUBTRACT', use_clamp=clamp).value


def switch(switch=None, false=None, true=None, input_type='GEOMETRY'):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        input_type (str): 'GEOMETRY' in [FLOAT, INT, BOOLEAN, VECTOR, STRING,... , COLLECTION, TEXTURE, MATERIAL]

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type=input_type).output


def switch_boolean(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='BOOLEAN').output


def switch_collection(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='COLLECTION').output


def switch_color(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='RGBA').output


def switch_float(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='FLOAT').output


def switch_geometry(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='GEOMETRY').output


def switch_image(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='IMAGE').output


def switch_integer(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='INT').output


def switch_material(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='MATERIAL').output


def switch_object(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='OBJECT').output


def switch_string(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='STRING').output


def switch_texture(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='TEXTURE').output


def switch_vector(switch=None, false=None, true=None):
    """ Node Switch.

    Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
    Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

    Args:
        switch: ['Boolean', 'Boolean']
        false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
        true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

    Returns:
        socket `output`
    """
    return nodes.Switch(switch=switch, false=false, true=true, input_type='VECTOR').output


def tan(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='TANGENT', use_clamp=clamp).value


def tangent(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='TANGENT', use_clamp=clamp).value


def tanh(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='TANH', use_clamp=clamp).value


def to_degrees(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='DEGREES', use_clamp=clamp).value


def to_radians(value=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=None, value2=None, operation='RADIANS', use_clamp=clamp).value


def value_to_string(value=None, decimals=None):
    """ Node ValueToString.

    Node reference [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html)
    Developer reference [FunctionNodeValueToString](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

    Args:
        value: Float
        decimals: Integer

    Returns:
        socket 'string'
    """
    return nodes.ValueToString(value=value, decimals=decimals).string


def vector_mix(factor=None, a=None, b=None, clamp_factor=True, factor_mode='UNIFORM'):
    """ Node Mix.

    Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
    Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

    Args:
        factor: ['Float', 'Vector']
        a: ['Float', 'Vector', 'Color']
        b: ['Float', 'Vector', 'Color']
        clamp_factor (bool): True
        factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

    Returns:
        socket `result`
    """
    return nodes.Mix(factor=factor, a=a, b=b, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode=factor_mode).result


def wrap(value=None, max=None, min=None, clamp=False):
    """ Node Math.

    Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
    Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

    Args:
        value: Float
        max: Float
        min: Float
        clamp (bool): False

    Returns:
        socket `value`
    """
    return nodes.Math(value0=value, value1=max, value2=min, operation='WRAP', use_clamp=clamp).value


def xnor(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XNOR').boolean


def xor(boolean0=None, boolean1=None):
    """ Node BooleanMath.

    Node reference [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
    Developer reference [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

    Args:
        boolean0: Boolean
        boolean1: Boolean

    Returns:
        socket `boolean`
    """
    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XOR').boolean




