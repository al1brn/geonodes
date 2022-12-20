# class {class_name}

## Color *classmethod* {#Color}

> def Color(cls):

Node [Color](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'color'

## HSL *classmethod* {#HSL}

> def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):

Node [Combine Color](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

### Returns:

  socket 'color'

## HSV *classmethod* {#HSV}

> def HSV(cls, hue=None, saturation=None, value=None, alpha=None):

Node [Combine Color](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

### Returns:

  socket 'color'

## RGB *classmethod* {#RGB}

> def RGB(cls, red=None, green=None, blue=None, alpha=None):

Node [Combine Color](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

### Returns:

  socket 'color'

## alpha *property* {#alpha}

> def alpha(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'alpha'

## blue *property* {#blue}

> def blue(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'blue'

## brighter {#brighter}

> def brighter(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## compare {#compare}

> def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

## darker {#darker}

> def darker(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## equal {#equal}

> def equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## equal {#equal}

> def equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## green *property* {#green}

> def green(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'green'

## hsl *property* {#hsl}

> def hsl(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## hsv *property* {#hsv}

> def hsv(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## hue *property* {#hue}

> def hue(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'red'

## lightness *property* {#lightness}

> def lightness(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'blue'

## mix {#mix}

> def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_add {#mix_add}

> def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_burn {#mix_burn}

> def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_color {#mix_color}

> def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_darken {#mix_darken}

> def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_difference {#mix_difference}

> def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_divide {#mix_divide}

> def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_dodge {#mix_dodge}

> def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_hue {#mix_hue}

> def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_lighten {#mix_lighten}

> def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_linear_light {#mix_linear_light}

> def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_multiply {#mix_multiply}

> def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_overlay {#mix_overlay}

> def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_saturation {#mix_saturation}

> def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_screen {#mix_screen}

> def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_soft_light {#mix_soft_light}

> def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_subtract {#mix_subtract}

> def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_value {#mix_value}

> def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## red *property* {#red}

> def red(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'red'

## rgb *property* {#rgb}

> def rgb(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## rgb_curves *property* {#rgb_curves}

> def rgb_curves(self, fac=None):

Node [RGB Curves](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- node with sockets ['color']

## saturation *property* {#saturation}

> def saturation(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'green'

## switch {#switch}

> def switch(self, switch=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## value *property* {#value}

> def value(self):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'blue'

