# Class Color

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Properties

### alpha

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `alpha`



### bl_idname

 Shortcut for `self.bsocket.bl_idname`



### blue

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `blue`



### bnode

 Shortcut for `self.bsocket.node`



### green

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `green`



### hsl

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    tuple ('red', 'green', 'blue', 'alpha')



### hsv

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    tuple ('red', 'green', 'blue', 'alpha')



### hue

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `red`



### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`



### is_output

 Shortcut for `self.bsocket.is_output`



### lightness

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `blue`



### links

 Shortcut for `self.bsocket.links`



### name

 Shortcut for `self.bsocket.name`



### node_chain_label

 Shortcut for *self.node.chain_label*



### red

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `red`



### rgb

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    tuple ('red', 'green', 'blue', 'alpha')



### rgb_curves

 Node RgbCurves.

Node reference [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html)
Developer reference [ShaderNodeRGBCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)

Returns:
    node with sockets ['color']



### saturation

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `green`



### socket_index

 Return the index of the socket within the list of node sockets.

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.




### value

 Node SeparateColor.

Node reference [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
Developer reference [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

Returns:
    socket `blue`



## Class and static methods

### Color

```python
@classmethod
def Color(cls)
```

 Node Color.

Node reference [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/color.html)
Developer reference [FunctionNodeInputColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)

Returns:
    socket `color`



### HSL

```python
@classmethod
def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None)
```

 Node CombineColor.

Node reference [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
Developer reference [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

Returns:
    socket `color`



### HSV

```python
@classmethod
def HSV(cls, hue=None, saturation=None, value=None, alpha=None)
```

 Node CombineColor.

Node reference [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
Developer reference [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

Returns:
    socket `color`



### Input

```python
@classmethod
def Input(cls, value=None, name = "Color", description = "")
```

 Create a Color input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
Returns:
    Color: The Color data socket




### RGB

```python
@classmethod
def RGB(cls, red=None, green=None, blue=None, alpha=None)
```

 Node CombineColor.

Node reference [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
Developer reference [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

Returns:
    socket `color`



### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

:param class_name: The class name
:type class_name: str
:return: The bl_idname associated to this class name
:rtype: str

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to *sub classes*:
    
.. list-table:: 
   :widths: 20 40
   :header-rows: 0

   * - Unsigned
     - Integer sub class (NodeSocketIntUnsigned)
   * - Factor
     - Float sub class (NodeSocketFloatFactor)
   * - Angle
     - Float sub class  (NodeSocketFloatAngle)
   * - Distance
     - Float sub class (NodeSocketFloatDistance)
   * - Rotation
     - Vector sub class (NodeSocketVectorEuler)
   * - xyz
     - Vector sub class (NodeSocketVectorXYZ)
   * - Translation
     - Vector sub class (NodeSocketVectorTranslation)
  
These additional values allow to enter angle, distance, factor... as group input values.




### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

:param socket: The socket to determine the class of
:param with_sub_class: Return the sub class if True
:typ socket: bpy.types.NodeSocket, Socket
:type with_sub_class: bool
:return: The name of the class associated to the bl_idname of the socket
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20 20
   :header-rows: 1
   
   * - NodeSocket
     - class name
     - sub class name
   * - NodeSocketBool 
     - 'Boolean'
     - 
   * - NodeSocketInt 
     - 'Integer'
     - 
   * - NodeSocketIntUnsigned 
     - 'Integer'
     - 'Unsigned'
   * - NodeSocketFloat 
     - 'Float' 
     - 
   * - NodeSocketFloatFactor 
     - 'Float'
     - 'Factor'
   * - NodeSocketFloatAngle  
     - 'Float'
     - 'Angle'
   * - NodeSocketFloatDistance 
     - 'Float'
     - 'Distance'
   * - NodeSocketVector 
     - 'Vector'
     - 
   * - NodeSocketVectorEuler 
     - 'Vector'
     - 'Rotation'
   * - NodeSocketVectorXYZ 
     - 'Vector'
     - 'xyz'
   * - NodeSocketVectorTranslation 
     - 'Vector'
     - 'Translation'
   * - NodeSocketColor 
     - 'Color'
     - 
   * - NodeSocketString' 
     - 'String'
     - 
   * - NodeSocketCollection 
     - 'Collection'
     - 
   * - NodeSocketImage 
     - 'Image'
     - 
   * - NodeSocketMaterial 
     - 'Material'
     - 
   * - NodeSocketObject 
     - 'Object'
     - 
   * - NodeSocketTexture 
     - 'Texture'
     - 
   * - NodeSocketGeometry
     - 'Geometry'
     - 
  
  
If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.



### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

:param value: The value to test
:type value: any
:return: True if *value* is or wraps a socket
:rtype: bool

Returns True if value is:
    
- A Blender Geometry Node Socket
- An instance of Socket        




### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool



### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool




### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color_domain='FLOAT_COLOR')
```

 Returns the domain to which the socket belongs

:param value: The socket
:type value: any
:return: data type in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20
   :header-rows: 1

   * - Socket bl_idname
     - Domain code
   * - NodeSocketBool
     - 'BOOLEAN'
   * - NodeSocketInt               
     - 'INT'
   * - NodeSocketIntUnsigned       
     - 'INT'
   * - NodeSocketFloat            
     - 'FLOAT'
   * - NodeSocketFloatFactor       
     - 'FLOAT'
   * - NodeSocketFloatAngle        
     - 'FLOAT'
   * - NodeSocketFloatDistance     
     - 'FLOAT'         
   * - NodeSocketVector            
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorEuler       
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorXYZ         
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorTranslation
     - 'FLOAT_VECTOR'
   * - NodeSocketColor      
     - 'FLOAT_COLOR'
   * - NodeSocketString           
     - 'FLOAT_COLOR'





## Methods

### brighter

```python
def brighter(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

Returns:
    socket `result`



### connected_sockets

```python
def connected_sockets(self)
```

 Returns the list of Socket instances linked to this socket.




### darker

```python
def darker(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

Returns:
    socket `result`



### equal

```python
def equal(self, b=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

Returns:
    socket `result`



### get_blender_socket

```python
def get_blender_socket(self)
```

 Overrides the standard behavior of :class:DataSocket super class

If the `r`, `g`, `b` properties have been read or modified, a *Combine RGB* node is necessary
to recompose the Color.

.. blid:: ShaderNodeCombineRGB




### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



### mix

```python
def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_add

```python
def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_burn

```python
def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_color

```python
def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_darken

```python
def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_difference

```python
def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_divide

```python
def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_dodge

```python
def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_hue

```python
def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_lighten

```python
def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_linear_light

```python
def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_multiply

```python
def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_overlay

```python
def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_saturation

```python
def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_screen

```python
def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_soft_light

```python
def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_subtract

```python
def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### mix_value

```python
def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

Returns:
    socket `result`



### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

:param values: The output sockets. More than one values can be passed
    if the input socket is multi input.
:type values: array of bpy.types.NodeSocket, Socket, values

see :func:`plug_bsocket`



### reroute

```python
def reroute(self)
```

 Reroute all output links



### reset_properties

```python
def reset_properties(self)
```

 Reset the properties

Properties such as components are cached.

After a node is called, the wrapped socket changes and this makes the cache obsolete.
After a change, the cache is erased.

:example:

.. code-block:: python

    class Vector(...):
        def __init__(self, ...):
             ...
             self.reset_properties()
             ...
    
         def reset_properties(self):
             super().reset_properties()
             self.separate_ = None      # Created by property self.seperate() with node SeparateXyz






### stack

```python
def stack(self, node, socket_name=None)
```

 Change the wrapped socket

:param node: The new node owning the output socket to wrap
:type node: Node
:return: self

Methods are implemented in two modes:

- Creation
- Transformation

In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.

In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
After the method returns, the calling DataSocket instance refers to a new Blender output socket.
The stack method changes the socket the instance refers to and reinitialize properties

.. code-block:: python

    # 1. Creation mode
    # 
    # to_mesh method creates a new mesh from a curve.
    # The curve instance refers to the same output node socket
    # We need to get the result of the method in a new variable
    
    new_mesh = curve.to_mesh(profile_curve=circle)
    
    # 2. Transformation mode
    #
    # set_shade_smooth method transforms the mesh.
    # After the call, the mesh instance refers to the output socket of the
    # newly created node "Set Shade Smooth". There is no need to get the result
    # of the method.
    
    mesh.set_shade_smooth()
    
    # Note that a transformation method returns self and so, the following line
    # is equivallent:
    
    mesh = mesh.set_shade_smooth()





### switch

```python
def switch(self, switch=None, true=None)
```

 Node Switch.

Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Color

Returns:
    socket `output`



### to_output

```python
def to_output(self, name=None)
```

 Plug the data socket to the group output

:param name: The name to give to the modifier output
:type name: str

The socket is added to the outputs of the geometry nodes tree.

.. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.




### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

 Link the data socket to the viewer

If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.

If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
accordingly.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

