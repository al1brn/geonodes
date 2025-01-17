# core



## Content

- **B** : [Boolean](boolean.md#boolean) :black_small_square: [Break](break.md#break)
- **C** : [check_enum_arg](core.md#check_enum_arg) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [CloudPoint](cloudpoint.md#cloudpoint) :black_small_square: [Collection](collection.md#collection) :black_small_square: [Color](color.md#color) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [color_ramp_set_stops](core.md#color_ramp_set_stops) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Curve](curve.md#curve)
- **D** : [del_tree](core.md#del_tree) :black_small_square: [Domain](domain.md#domain)
- **E** : [Edge](edge.md#edge) :black_small_square: [Elif](elif.md#elif) :black_small_square: [Else](else.md#else) :black_small_square: [ensure_uniques](core.md#ensure_uniques)
- **F** : [Face](face.md#face) :black_small_square: [Float](float.md#float) :black_small_square: [ForEachElement](foreachelement.md#foreachelement)
- **G** : [G](g.md#g) :black_small_square: [generated](generated.md#generated) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [GeoNodes](geonodes.md#geonodes) :black_small_square: [get_tree](core.md#get_tree) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Group](group.md#group) :black_small_square: [GroupF](groupf.md#groupf)
- **I** : [If](if.md#if) :black_small_square: [Image](image.md#image) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Integer](integer.md#integer)
- **L** : [Layer](layer.md#layer) :black_small_square: [Layout](layout.md#layout)
- **M** : [Material](material.md#material) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Menu](menu.md#menu) :black_small_square: [Mesh](mesh.md#mesh)
- **N** : [Node](node.md#node)
- **O** : [Object](object.md#object)
- **P** : [Panel](panel.md#panel) :black_small_square: [Point](point.md#point)
- **R** : [Repeat](repeat.md#repeat) :black_small_square: [Rotation](rotation.md#rotation)
- **S** : [Shader](shader.md#shader) :black_small_square: [ShaderNodes](shadernodes.md#shadernodes) :black_small_square: [Simulation](simulation.md#simulation) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Spline](spline.md#spline) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [String](string.md#string)
- **T** : [Texture](texture.md#texture) :black_small_square: [Tree](tree.md#tree)
- **V** : [Vector](vector.md#vector) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Volume](volume.md#volume) :black_small_square: [VolumeShader](volumeshader.md#volumeshader)
- **Z** : [Zone](zone.md#zone)

## Modules



- [generated](generated.md#generated)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [core](core.md#core)</sub>

## Classes



- [Boolean](boolean.md#boolean)
- [Break](break.md#break)
- [Cloud](cloud.md#cloud)
- [CloudPoint](cloudpoint.md#cloudpoint)
- [Collection](collection.md#collection)
- [Color](color.md#color)
- [ColorRamp](colorramp.md#colorramp)
- [Corner](corner.md#corner)
- [Curve](curve.md#curve)
- [Domain](domain.md#domain)
- [Edge](edge.md#edge)
- [Elif](elif.md#elif)
- [Else](else.md#else)
- [Face](face.md#face)
- [Float](float.md#float)
- [ForEachElement](foreachelement.md#foreachelement)
- [G](g.md#g)
- [Geometry](geometry.md#geometry)
- [GeoNodes](geonodes.md#geonodes)
- [GreasePencil](greasepencil.md#greasepencil)
- [Group](group.md#group)
- [GroupF](groupf.md#groupf)
- [If](if.md#if)
- [Image](image.md#image)
- [Instance](instance.md#instance)
- [Instances](instances.md#instances)
- [Integer](integer.md#integer)
- [Layer](layer.md#layer)
- [Layout](layout.md#layout)
- [Material](material.md#material)
- [Matrix](matrix.md#matrix)
- [Menu](menu.md#menu)
- [Mesh](mesh.md#mesh)
- [Node](node.md#node)
- [Object](object.md#object)
- [Panel](panel.md#panel)
- [Point](point.md#point)
- [Repeat](repeat.md#repeat)
- [Rotation](rotation.md#rotation)
- [Shader](shader.md#shader)
- [ShaderNodes](shadernodes.md#shadernodes)
- [Simulation](simulation.md#simulation)
- [Socket](socket.md#socket)
- [Spline](spline.md#spline)
- [SplinePoint](splinepoint.md#splinepoint)
- [String](string.md#string)
- [Texture](texture.md#texture)
- [Tree](tree.md#tree)
- [Vector](vector.md#vector)
- [Vertex](vertex.md#vertex)
- [Volume](volume.md#volume)
- [VolumeShader](volumeshader.md#volumeshader)
- [Zone](zone.md#zone)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [core](core.md#core)</sub>

## Functions



----------
### check_enum_arg()

> function

``` python
check_enum_arg(arg_name: str, arg_value: str, meth_name: str, valids: tuple) -> bool
```

Check the value of an enum param

#### Raises:
- **NodeError** : if arg_value is not in valids



#### Arguments:
- **arg_name** (_str_) : argument name
- **arg_value** (_str_) : argument value
- **meth_name** (_str_) : method name
- **valids** (_tuple_) : tuple of valid values



#### Returns:
- **bool** : True

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [Functions](core.md#functions-2)</sub>

----------
### color_ramp_set_stops()

> function

``` python
color_ramp_set_stops(bnode, *stops)
```

Set the color ramp stops

#### Arguments:
- **bnode** : color ramp node
- **stops** : list of tuple (position, color)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [Functions](core.md#functions-2)</sub>

----------
### del_tree()

> function

``` python
del_tree(btree)
```

Delete a tree

#### Arguments:
- **btree** : (blender Tree or str : Tree or tree name

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [Functions](core.md#functions-2)</sub>

----------
### ensure_uniques()

> function

``` python
ensure_uniques(names: list[str], single_digit: bool = False)
```

Build a list of unique names from a list

Doublons are suffixed by an index:
- ['key', 'key', 'other'] -> ['key', 'key_001', 'other']

#### Arguments:
- **names** (_list_) : list of names with possible doublons
- **single_digit** (_bool_ = False) : 'key_1' rather that 'key_001'



#### Returns:
- **list** : doublons are suffixed by an index

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [Functions](core.md#functions-2)</sub>

----------
### get_tree()

> function

``` python
get_tree(name, tree_type='GeometryNodeTree', create=True)
```

Get or create a new nodes tree

#### Arguments:
- **name** (_str_) : Tree name - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree') - create (bool = False) : Create the tree if it doesn't exist
- **tree_type** ( = GeometryNodeTree)
- **create** ( = True)



#### Returns:
- **Tree** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [Functions](core.md#functions-2)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [core](core.md#core) :black_small_square: [Content](core.md#content) :black_small_square: [core](core.md#core)</sub>