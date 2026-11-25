# Comparaison Blender (5, 2, 0) → (5, 3, 0)

## GeometryNodeTree

### Nœuds supprimés (0)

Aucun.


### Nœuds ajoutés (20)

- **Get Vector Component** (`FunctionNodeGetVectorComponent`)
  - `Vector.get_component(self, index: Integer=None)`
- **Combine List** (`GeometryNodeCombineList`)
  - `Boolean.combine_list(self, *items)`
  - `Bundle.combine_list(self, *items)`
  - `Closure.combine_list(self, *items)`
  - `Collection.combine_list(self, *items)`
  - `Color.combine_list(self, *items)`
  - `Float.combine_list(self, *items)`
  - `Font.combine_list(self, *items)`
  - `Geometry.combine_list(self, *items)`
  - `Image.combine_list(self, *items)`
  - `Integer.combine_list(self, *items)`
  - `Material.combine_list(self, *items)`
  - `Matrix.combine_list(self, *items)`
  - `Menu.combine_list(self, *items)`
  - `Object.combine_list(self, *items)`
  - `Rotation.combine_list(self, *items)`
  - `Sound.combine_list(self, *items)`
  - `String.combine_list(self, *items)`
  - `Vector.combine_list(self, *items)`
- **Construct Curves** (`GeometryNodeConstructCurves`)
  - `@classmethod Curve.ConstructCurves(cls, positions: Vector=None, curve_offsets: Integer=None)`
- **Geometry Materials** (`GeometryNodeGeometryMaterials`)
  - `Cloud.materials(self)`
  - `Curve.materials(self)`
  - `Geometry.materials(self, component_type: Menu=None)`
  - `GreasePencil.materials(self)`
  - `Mesh.materials(self)`
- **Get Grid Names** (`GeometryNodeGetGridNames`)
  - `Volume.get_grid_names(self)`
- **Grease Pencil Color** (`GeometryNodeGreasePencilColor`)
  - Static only
- **Grease Pencil Draw Time** (`GeometryNodeGreasePencilDrawTime`)
  - Static only
- **Grease Pencil Fill ID** (`GeometryNodeGreasePencilFillID`)
  - Static only
- **Grease Pencil Opacity** (`GeometryNodeGreasePencilOpacity`)
  - Static only
- **Grease Pencil Stroke Softness** (`GeometryNodeGreasePencilStrokeSoftness`)
  - Static only
- **Grease Pencil Stroke Visibility** (`GeometryNodeGreasePencilStrokeVisibility`)
  - Static only
- **Deactivate Voxels** (`GeometryNodeGridDeactivateVoxels`)
  - `Boolean.deactivate_voxels(self, selection: Boolean=None)`
  - `Float.deactivate_voxels(self, selection: Boolean=None)`
  - `Integer.deactivate_voxels(self, selection: Boolean=None)`
  - `Vector.deactivate_voxels(self, selection: Boolean=None)`
- **Grid Solve Poisson** (`GeometryNodeGridSolvePoisson`)
  - `Float.grid_solve_poisson(self, max_iterations: Integer=None, error_threshold: Float=None, boundary_value: Float=None, boundary_gradient: Vector=None, boundary_factor: Float=None, threshold_mode: Menu=None, boundary: Menu=None)`
- **Grid Topology Boolean** (`GeometryNodeGridTopologyBoolean`)
  - `Boolean.grid_topology_boolean(self, *grid_2: Boolean, operation: Menu=None)`
  - `Float.grid_topology_boolean(self, *grid_2: Float, operation: Menu=None)`
  - `Integer.grid_topology_boolean(self, *grid_2: Integer, operation: Menu=None)`
  - `Vector.grid_topology_boolean(self, *grid_2: Vector, operation: Menu=None)`
- **Import SPZ** (`GeometryNodeImportSPZ`)
  - `@classmethod Cloud.ImportSPZ(cls, path: String=None)`
- **NURBS Order** (`GeometryNodeNURBSOrder`)
  - Static only
- **NURBS Weight** (`GeometryNodeNURBSWeight`)
  - Static only
- **Set Point Cloud Type** (`GeometryNodePointsSetType`)
  - `Cloud.set_point_type(self, type: Menu=None)`
- **Rasterize Points** (`GeometryNodeRasterizePoints`)
  - `Cloud.rasterize_points(self, voxel_size: Float=None, matrix: Matrix=None, position: Vector=None, named_sockets: dict={}, grid_transform_mode: Menu=None, kernel_type: Menu=None, **sockets)`
- **Comment** (`NodeComment`)
  - Static only

### Nœuds modifiés (8)

#### Bone Info

Blender identifier: `GeometryNodeBoneInfo`

##### Old version

- `Object.bone_info(self, bone_name: String=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')`

##### New version

- `Object.bone_info(self, bone_name: String=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')`

##### Changes

- info / outputs / Envelope Distance (added) : nouveau: {'aliases': ['Envelope Distance'], 'bl_idname': 'NodeSocketFloat', 'label': 'Envelope Distance', 'name': 'Envelope Distance', 'socket_type': 'VALUE'}
- info / outputs / Radius Head (added) : nouveau: {'aliases': ['Radius Head'], 'bl_idname': 'NodeSocketFloat', 'label': 'Radius Head', 'name': 'Radius Head', 'socket_type': 'VALUE'}
- info / outputs / Radius Tail (added) : nouveau: {'aliases': ['Radius Tail'], 'bl_idname': 'NodeSocketFloat', 'label': 'Radius Tail', 'name': 'Radius Tail', 'socket_type': 'VALUE'}

#### Curve to Mesh

Blender identifier: `GeometryNodeCurveToMesh`

##### Old version

- `Curve.to_mesh(self, profile_curve: Curve=None, scale: Float=None, fill_caps: Boolean=None)`

##### New version

- `Curve.to_mesh(self, profile_curve: Curve=None, scale: Float=None, fill_caps: Boolean=None, miter_scale: Boolean=None, miter_scale_limit: Float=None)`

##### Argument changes

- `Curve.to_mesh` — arguments appended: `miter_scale`, `miter_scale_limit`
- `nd.curve_to_mesh` — arguments appended: `miter_scale`, `miter_scale_limit`

##### Changes

- info / inputs / Miter Scale (added) : nouveau: {'aliases': ['Miter Scale'], 'bl_idname': 'NodeSocketBool', 'label': 'Miter Scale', 'name': 'Miter Scale', 'socket_type': 'BOOLEAN'}
- info / inputs / Miter Scale Limit (added) : nouveau: {'aliases': ['Miter Scale Limit'], 'bl_idname': 'NodeSocketFloatAngle', 'label': 'Miter Scale Limit', 'name': 'Miter Scale Limit', 'socket_type': 'VALUE'}

#### Import PLY

Blender identifier: `GeometryNodeImportPLY`

##### Old version

- `@classmethod Mesh.ImportPLY(cls, path: String=None)`

##### New version

- `@classmethod Geometry.ImportPLY(cls, path: String=None)`

##### Changes

- info / outputs / Geometry (added) : nouveau: {'aliases': ['Geometry'], 'bl_idname': 'NodeSocketGeometry', 'label': 'Geometry', 'name': 'Geometry', 'socket_type': 'GEOMETRY'}
- info / outputs / Mesh (removed) : ancien: {'aliases': ['Mesh'], 'bl_idname': 'NodeSocketGeometry', 'label': 'Mesh', 'name': 'Mesh', 'socket_type': 'GEOMETRY'}

#### Merge Layers

Blender identifier: `GeometryNodeMergeLayers`

##### Old version

- `GreasePencil.merge_layers(self, group_id: Integer=None, mode: T_MODE_10='MERGE_BY_NAME')`

##### New version

- `GreasePencil.merge_layers(self, group_id: Integer=None, mode_1: Menu=None, mode: T_MODE_10='MERGE_BY_NAME')`

##### Argument changes

- `GreasePencil.merge_layers` — CAUTION: arguments inserted: `mode_1`
- `nd.merge_layers` — CAUTION: arguments inserted: `mode_1`

##### Changes

- info / inputs / Mode (added) : nouveau: {'aliases': ['Mode'], 'bl_idname': 'NodeSocketMenu', 'label': 'Mode', 'name': 'Mode', 'socket_type': 'MENU'}
- info / menu_sockets / Mode (added) : nouveau: {'default': 'By Name', 'values': ('By Name', 'By Group ID')}

#### Realize Instances

Blender identifier: `GeometryNodeRealizeInstances`

##### Old version

- `Geometry.realize(self, realize_all: Boolean=None, depth: Integer=None, realize_to_point_domain: bool=False)`

##### New version

- `Geometry.realize(self, realize_all: Boolean=None, depth: Integer=None, preserve_normals: Boolean=None, realize_to_point_domain: bool=False)`

##### Argument changes

- `Geometry.realize` — CAUTION: arguments inserted: `preserve_normals`
- `nd.realize_instances` — CAUTION: arguments inserted: `preserve_normals`

##### Changes

- info / inputs / Preserve Normals (added) : nouveau: {'aliases': ['Preserve Normals'], 'bl_idname': 'NodeSocketBool', 'label': 'Preserve Normals', 'name': 'Preserve Normals', 'socket_type': 'BOOLEAN'}

#### Sample Grid

Blender identifier: `GeometryNodeSampleGrid`

##### Old version

- `Boolean.sample_grid(self, position: Vector=None, interpolation: Menu=None)`
- `Float.sample_grid(self, position: Vector=None, interpolation: Menu=None)`
- `Integer.sample_grid(self, position: Vector=None, interpolation: Menu=None)`
- `Vector.sample_grid(self, position: Vector=None, interpolation: Menu=None)`

##### New version

- `Boolean.sample_grid(self, position: Vector=None, interpolation: Menu=None)`
- `Float.sample_grid(self, position: Vector=None, interpolation: Menu=None)`
- `Integer.sample_grid(self, position: Vector=None, interpolation: Menu=None)`
- `Vector.sample_grid(self, position: Vector=None, interpolation: Menu=None)`

##### Changes

- info / menu_sockets / Interpolation / values (modified) : ancien: ('Nearest Neighbor', 'Trilinear', 'Triquadratic') → nouveau: ('Nearest Neighbor', 'Trilinear', 'Triquadratic', 'Tricubic')

#### Set Grease Pencil Color

Blender identifier: `GeometryNodeSetGreasePencilColor`

##### Old version

- `GreasePencil.set_grease_pencil_color(self, color: Color=None, opacity: Float=None, mode: T_MODE_16='STROKE')`
- `@setter GreasePencil.stroke_color(self, color: Color=None)`
- `@setter GreasePencil.fill_color(self, color: Color=None)`

##### New version

- `GreasePencil.set_grease_pencil_color(self, color: Color=None, opacity: Float=None, mode_1: Menu=None, mode: T_MODE_16='STROKE')`
- `@setter GreasePencil.stroke_color(self, color: Color=None)`
- `@setter GreasePencil.fill_color(self, color: Color=None)`

##### Argument changes

- `GreasePencil.set_grease_pencil_color` — CAUTION: arguments inserted: `mode_1`
- `nd.set_grease_pencil_color` — CAUTION: arguments inserted: `mode_1`

##### Changes

- info / inputs / Mode (added) : nouveau: {'aliases': ['Mode'], 'bl_idname': 'NodeSocketMenu', 'label': 'Mode', 'name': 'Mode', 'socket_type': 'MENU'}
- info / menu_sockets / Mode (added) : nouveau: {'default': 'Stroke', 'values': ('Stroke', 'Fill', 'Both')}
- info / params / mode / enum (modified) : ancien: ('STROKE', 'FILL') → nouveau: ('STROKE', 'FILL', 'BOTH')

#### Set Grease Pencil Depth

Blender identifier: `GeometryNodeSetGreasePencilDepth`

##### Old version

- `GreasePencil.set_grease_pencil_depth(self, depth_order: T_GABOR_TYPE_1='2D')`
- `@setter GreasePencil.depth(self)`

##### New version

- `GreasePencil.set_grease_pencil_depth(self, depth_order_1: Menu=None, depth_order: T_GABOR_TYPE_1='2D')`
- `@setter GreasePencil.depth(self, depth_order: Menu=None)`

##### Argument changes

- `GreasePencil.depth` — arguments appended: `depth_order`
- `GreasePencil.set_grease_pencil_depth` — CAUTION: arguments inserted: `depth_order_1`
- `nd.set_grease_pencil_depth` — CAUTION: arguments inserted: `depth_order_1`

##### Changes

- info / inputs / Depth Order (added) : nouveau: {'aliases': ['Depth Order'], 'bl_idname': 'NodeSocketMenu', 'label': 'Depth Order', 'name': 'Depth Order', 'socket_type': 'MENU'}
- info / menu_sockets / Depth Order (added) : nouveau: {'default': '2D Layers', 'values': ('2D Layers', '3D Location')}


## ShaderNodeTree

### Nœuds supprimés (0)

Aucun.


### Nœuds ajoutés (27)

- **Boolean Math** (`FunctionNodeBooleanMath`)
  - `Boolean.band(self, boolean: Boolean=None)`
  - `Boolean.__and__(self, other)`
  - `Boolean.__rand__(self, other)`
  - `Boolean.__iand__(self, other)`
  - `Boolean.__mul__(self, other)`
  - `Boolean.__rmul__(self, other)`
  - `Boolean.__imul__(self, other)`
  - `Boolean.bor(self, boolean: Boolean=None)`
  - `Boolean.__or__(self, other)`
  - `Boolean.__ror__(self, other)`
  - `Boolean.__ior__(self, other)`
  - `Boolean.__add__(self, other)`
  - `Boolean.__radd__(self, other)`
  - `Boolean.__iadd__(self, other)`
  - `Boolean.xor(self, boolean: Boolean=None)`
  - `Boolean.__xor__(self, other)`
  - `Boolean.__rxor__(self, other)`
  - `Boolean.__ixor__(self, other)`
  - `Boolean.__sub__(self, other)`
  - `Boolean.__rsub__(self, other)`
  - `Boolean.__isub__(self, other)`
  - `Boolean.bnot(self)`
  - `Boolean.__neg__(self)`
  - `Boolean.__invert__(self)`
  - `Boolean.not_and(self, boolean: Boolean=None)`
  - `Boolean.nor(self, boolean: Boolean=None)`
  - `Boolean.xnor(self, boolean: Boolean=None)`
  - `Boolean.imply(self, boolean: Boolean=None)`
  - `Boolean.nimply(self, boolean: Boolean=None)`
  - `Boolean.boolean_math(self, boolean: Boolean=None, operation: T_OPERATION_1='AND')`
  - `gnmath.band(boolean: Boolean=None, boolean_1: Boolean=None)`
  - `gnmath.bor(boolean: Boolean=None, boolean_1: Boolean=None)`
  - `gnmath.xor(boolean: Boolean=None, boolean_1: Boolean=None)`
  - `gnmath.bnot(boolean: Boolean=None)`
  - `gnmath.not_and(boolean: Boolean=None, boolean_1: Boolean=None)`
  - `gnmath.nor(boolean: Boolean=None, boolean_1: Boolean=None)`
  - `gnmath.xnor(boolean: Boolean=None, boolean_1: Boolean=None)`
  - `gnmath.imply(boolean: Boolean=None, boolean_1: Boolean=None)`
  - `gnmath.nimply(boolean: Boolean=None, boolean_1: Boolean=None)`
- **Find in String** (`FunctionNodeFindInString`)
  - `String.find_in_string(self, search: String=None, mode: Menu=None)`
- **Format String** (`FunctionNodeFormatString`)
  - `String.format(self, named_sockets: dict={}, **sockets)`
- **Get Vector Component** (`FunctionNodeGetVectorComponent`)
  - `Vector.get_component(self, index: Integer=None)`
- **Special Characters** (`FunctionNodeInputSpecialCharacters`)
  - `@classproperty String.line_break(cls)`
  - `@classproperty String.tab(cls)`
- **String** (`FunctionNodeInputString`)
  - Static only
- **Integer Math** (`FunctionNodeIntegerMath`)
  - `Integer.add(self, value: Integer=None)`
  - `Integer.__add__(self, other)`
  - `Integer.__radd__(self, other)`
  - `Integer.__iadd__(self, other)`
  - `Integer.subtract(self, value: Integer=None)`
  - `Integer.__sub__(self, other)`
  - `Integer.__rsub__(self, other)`
  - `Integer.__isub__(self, other)`
  - `Integer.multiply(self, value: Integer=None)`
  - `Integer.__mul__(self, other)`
  - `Integer.__rmul__(self, other)`
  - `Integer.__imul__(self, other)`
  - `Integer.divide(self, value: Integer=None)`
  - `Integer.__floordiv__(self, other)`
  - `Integer.__rfloordiv__(self, other)`
  - `Integer.__ifloordiv__(self, other)`
  - `Integer.power(self, exponent: Integer=None)`
  - `Integer.__pow__(self, other)`
  - `Integer.__rpow__(self, other)`
  - `Integer.__ipow__(self, other)`
  - `Integer.modulo(self, value: Integer=None)`
  - `Integer.__mod__(self, other)`
  - `Integer.__rmod__(self, other)`
  - `Integer.__imod__(self, other)`
  - `Integer.abs(self)`
  - `Integer.__abs__(self)`
  - `Integer.negate(self)`
  - `Integer.__neg__(self)`
  - `Integer.multiply_add(self, multiplier: Integer=None, addend: Integer=None)`
  - `Integer.sign(self)`
  - `Integer.min(self, value: Integer=None)`
  - `Integer.max(self, value: Integer=None)`
  - `Integer.divide_round(self, value: Integer=None)`
  - `Integer.divide_floor(self, value: Integer=None)`
  - `Integer.divide_ceil(self, value: Integer=None)`
  - `Integer.floored_modulo(self, value: Integer=None)`
  - `Integer.gcd(self, value: Integer=None)`
  - `Integer.lcm(self, value: Integer=None)`
  - `Integer.integer_math(self, value: Integer=None, addend: Integer=None, *, multiplier: Integer=None, exponent: Integer=None, operation: T_OPERATION_2='ADD')`
  - `gnmath.iadd(value: Integer=None, value_1: Integer=None)`
  - `gnmath.isubtract(value: Integer=None, value_1: Integer=None)`
  - `gnmath.imultiply(value: Integer=None, value_1: Integer=None)`
  - `gnmath.idivide(value: Integer=None, value_1: Integer=None)`
  - `gnmath.ipower(base: Integer=None, exponent: Integer=None)`
  - `gnmath.imodulo(value: Integer=None, value_1: Integer=None)`
  - `gnmath.iabs(value: Integer=None)`
  - `gnmath.negate(value: Integer=None)`
  - `gnmath.imultiply_add(value: Integer=None, multiplier: Integer=None, addend: Integer=None)`
  - `gnmath.isign(value: Integer=None)`
  - `gnmath.imin(value: Integer=None, value_1: Integer=None)`
  - `gnmath.imax(value: Integer=None, value_1: Integer=None)`
  - `gnmath.divide_round(value: Integer=None, value_1: Integer=None)`
  - `gnmath.divide_floor(value: Integer=None, value_1: Integer=None)`
  - `gnmath.divide_ceil(value: Integer=None, value_1: Integer=None)`
  - `gnmath.ifloored_modulo(value: Integer=None, value_1: Integer=None)`
  - `gnmath.gcd(value: Integer=None, value_1: Integer=None)`
  - `gnmath.lcm(value: Integer=None, value_1: Integer=None)`
- **Match String** (`FunctionNodeMatchString`)
  - `String.match(self, key: String=None, operation: Menu=None)`
- **Replace String** (`FunctionNodeReplaceString`)
  - `String.replace(self, find: String=None, replace: String=None)`
- **Reverse String** (`FunctionNodeReverseString`)
  - `String.reverse(self)`
- **Set String Case** (`FunctionNodeSetStringCase`)
  - `String.set_string_case(self, case: Menu=None)`
- **Slice String** (`FunctionNodeSliceString`)
  - `String.slice(self, position: Integer=None, length: Integer=None)`
- **String Length** (`FunctionNodeStringLength`)
  - `String.length(self)`
- **String to Value** (`FunctionNodeStringToValue`)
  - `@classmethod Float.FromString(cls, string: String=None, base: Integer=None, data_type: T_DATA_TYPE_4='FLOAT')`
  - `String.to_value(self, base: Integer=None, data_type: T_DATA_TYPE_4='FLOAT')`
- **Trim String** (`FunctionNodeTrimString`)
  - `String.trim(self, characters: String=None, whitespace: Boolean=None, start: Boolean=None, end: Boolean=None)`
- **Value to String** (`FunctionNodeValueToString`)
  - `Float.to_string(self, decimals: Integer=None)`
  - `Integer.to_string(self, base: Integer=None, padding: Integer=None)`
  - `@classmethod String.FromValue(cls, value: Integer=None, base: Integer=None, padding: Integer=None)`
- **Index Switch** (`GeometryNodeIndexSwitch`)
  - `Boolean.index_switch(self, *items, index: Integer=None)`
  - `Bundle.index_switch(self, *items, index: Integer=None)`
  - `Closure.index_switch(self, *items, index: Integer=None)`
  - `Color.index_switch(self, *items, index: Integer=None)`
  - `Float.index_switch(self, *items, index: Integer=None)`
  - `Integer.index_switch(self, *items, index: Integer=None)`
  - `Menu.index_switch(self, *items, index: Integer=None)`
  - `Shader.index_switch(self, *items, index: Integer=None)`
  - `String.index_switch(self, *items, index: Integer=None)`
  - `Vector.index_switch(self, *items, index: Integer=None)`
- **Switch** (`GeometryNodeSwitch`)
  - `Boolean.switch(self, switch: Boolean=None, true: Boolean=None)`
  - `Boolean.switch_false(self, switch: Boolean=None, false: Boolean=None)`
  - `@classmethod Boolean.Switch(cls, switch: Boolean=None, false: Boolean=None, true: Boolean=None)`
  - `Bundle.switch(self, switch: Boolean=None, true: Bundle=None)`
  - `Bundle.switch_false(self, switch: Boolean=None, false: Bundle=None)`
  - `@classmethod Bundle.Switch(cls, switch: Boolean=None, false: Bundle=None, true: Bundle=None)`
  - `Closure.switch(self, switch: Boolean=None, true: Closure=None)`
  - `Closure.switch_false(self, switch: Boolean=None, false: Closure=None)`
  - `@classmethod Closure.Switch(cls, switch: Boolean=None, false: Closure=None, true: Closure=None)`
  - `Color.switch(self, switch: Boolean=None, true: Color=None)`
  - `Color.switch_false(self, switch: Boolean=None, false: Color=None)`
  - `@classmethod Color.Switch(cls, switch: Boolean=None, false: Color=None, true: Color=None)`
  - `Float.switch(self, switch: Boolean=None, true: Float=None)`
  - `Float.switch_false(self, switch: Boolean=None, false: Float=None)`
  - `@classmethod Float.Switch(cls, switch: Boolean=None, false: Float=None, true: Float=None)`
  - `Integer.switch(self, switch: Boolean=None, true: Integer=None)`
  - `Integer.switch_false(self, switch: Boolean=None, false: Integer=None)`
  - `@classmethod Integer.Switch(cls, switch: Boolean=None, false: Integer=None, true: Integer=None)`
  - `Menu.switch(self, switch: Boolean=None, true: Menu=None)`
  - `Menu.switch_false(self, switch: Boolean=None, false: Menu=None)`
  - `@classmethod Menu.Switch(cls, switch: Boolean=None, false: Menu=None, true: Menu=None)`
  - `Shader.switch(self, switch: Boolean=None, true: Shader=None)`
  - `Shader.switch_false(self, switch: Boolean=None, false: Shader=None)`
  - `@classmethod Shader.Switch(cls, switch: Boolean=None, false: Shader=None, true: Shader=None)`
  - `String.switch(self, switch: Boolean=None, true: String=None)`
  - `String.switch_false(self, switch: Boolean=None, false: String=None)`
  - `@classmethod String.Switch(cls, switch: Boolean=None, false: String=None, true: String=None)`
  - `Vector.switch(self, switch: Boolean=None, true: Vector=None)`
  - `Vector.switch_false(self, switch: Boolean=None, false: Vector=None)`
  - `@classmethod Vector.Switch(cls, switch: Boolean=None, false: Vector=None, true: Vector=None)`
- **Warning** (`GeometryNodeWarning`)
  - `Boolean.error(self, message: String=None)`
  - `Boolean.warning(self, message: String=None)`
  - `Boolean.info(self, message: String=None)`
- **Comment** (`NodeComment`)
  - Static only
- **Enable Output** (`NodeEnableOutput`)
  - `Boolean.enable_output(self, enable: Boolean=None)`
  - `Bundle.enable_output(self, enable: Boolean=None)`
  - `Closure.enable_output(self, enable: Boolean=None)`
  - `Color.enable_output(self, enable: Boolean=None)`
  - `Float.enable_output(self, enable: Boolean=None)`
  - `Integer.enable_output(self, enable: Boolean=None)`
  - `Menu.enable_output(self, enable: Boolean=None)`
  - `Shader.enable_output(self, enable: Boolean=None)`
  - `String.enable_output(self, enable: Boolean=None)`
  - `Vector.enable_output(self, enable: Boolean=None)`
- **Light Accumulation** (`ShaderNodeLightAccumulation`)
  - `@classmethod Shader.LightAccumulation(cls, diffuse_light: Color=None, diffuse_color: Color=None, glossy_light: Color=None, glossy_color: Color=None, transmission_light: Color=None, transmission_color: Color=None)`
- **Light Evaluation** (`ShaderNodeLightEvaluation`)
  - Static only
- **Light Info** (`ShaderNodeLightInfo`)
  - Static only
- **Light Iter Internal Input** (`ShaderNodeLightIterInternalInput`)
  - `@classmethod Integer.LightIterInternalInput(cls)`
- **Light Iter Internal Output** (`ShaderNodeLightIterInternalOutput`)
  - Static only
- **Shadow Raycast** (`ShaderNodeShadowRaycast`)
  - Static only

### Nœuds modifiés (4)

#### Attribute

Blender identifier: `ShaderNodeAttribute`

##### Old version

- Static only

##### New version

- Static only

##### Changes

- info / params / attribute_type / enum (modified) : ancien: ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER') → nouveau: ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER', 'LIGHT')

#### Glass BSDF

Blender identifier: `ShaderNodeBsdfGlass`

##### Old version

- `@classmethod Shader.Glass(cls, color: Color=None, roughness: Float=None, ior: Float=None, normal: Vector=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_1='MULTI_GGX')`

##### New version

- `@classmethod Shader.Glass(cls, color: Color=None, roughness: Float=None, anisotropy: Float=None, rotation: Float=None, ior: Float=None, normal: Vector=None, tangent: Vector=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_1='MULTI_GGX')`

##### Argument changes

- `Shader.Glass` — CAUTION: arguments inserted: `anisotropy`, `rotation`, `tangent`
- `nd.glass_bsdf` — CAUTION: arguments inserted: `anisotropy`, `rotation`, `tangent`

##### Changes

- info / inputs / Anisotropy (added) : nouveau: {'aliases': ['Anisotropy'], 'bl_idname': 'NodeSocketFloatFactor', 'label': 'Anisotropy', 'name': 'Anisotropy', 'socket_type': 'VALUE'}
- info / inputs / Rotation (added) : nouveau: {'aliases': ['Rotation'], 'bl_idname': 'NodeSocketFloatFactor', 'label': 'Rotation', 'name': 'Rotation', 'socket_type': 'VALUE'}
- info / inputs / Tangent (added) : nouveau: {'aliases': ['Tangent'], 'bl_idname': 'NodeSocketVector', 'label': 'Tangent', 'name': 'Tangent', 'socket_type': 'VECTOR'}

#### Principled BSDF

Blender identifier: `ShaderNodeBsdfPrincipled`

##### Old version

- `@classmethod Shader.Principled(cls, base_color: Color=None, metallic: Float=None, roughness: Float=None, ior: Float=None, alpha: Float=None, thin_wall: Boolean=None, normal: Vector=None, diffuse_roughness: Float=None, subsurface_weight: Float=None, subsurface_radius: Vector=None, subsurface_scale: Float=None, subsurface_ior: Float=None, subsurface_anisotropy: Float=None, specular_ior_level: Float=None, specular_tint: Color=None, anisotropic: Float=None, anisotropic_rotation: Float=None, tangent: Vector=None, transmission_weight: Float=None, coat_weight: Float=None, coat_roughness: Float=None, coat_ior: Float=None, coat_tint: Color=None, coat_normal: Vector=None, sheen_weight: Float=None, sheen_roughness: Float=None, sheen_tint: Color=None, emission_color: Color=None, emission_strength: Float=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_3='MULTI_GGX', subsurface_method: T_SUBSURFACE_METHOD_1='RANDOM_WALK')`

##### New version

- `@classmethod Shader.Principled(cls, base_color: Color=None, metallic: Float=None, roughness: Float=None, ior: Float=None, alpha: Float=None, thin_wall: Boolean=None, normal: Vector=None, diffuse_roughness: Float=None, subsurface_weight: Float=None, subsurface_radius: Vector=None, subsurface_scale: Float=None, subsurface_ior: Float=None, subsurface_anisotropy: Float=None, specular_ior_level: Float=None, specular_tint: Color=None, anisotropic: Float=None, anisotropic_rotation: Float=None, tangent: Vector=None, transmission_weight: Float=None, transmission_dispersion_scale: Float=None, transmission_dispersion_abbe_number: Float=None, coat_weight: Float=None, coat_roughness: Float=None, coat_ior: Float=None, coat_tint: Color=None, coat_normal: Vector=None, sheen_weight: Float=None, sheen_roughness: Float=None, sheen_tint: Color=None, emission_color: Color=None, emission_strength: Float=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_3='MULTI_GGX', subsurface_method: T_SUBSURFACE_METHOD_1='RANDOM_WALK')`

##### Argument changes

- `Shader.Principled` — CAUTION: arguments inserted: `transmission_dispersion_scale`, `transmission_dispersion_abbe_number`
- `nd.principled_bsdf` — CAUTION: arguments inserted: `transmission_dispersion_scale`, `transmission_dispersion_abbe_number`

##### Changes

- info / inputs / Transmission Dispersion Abbe Number (added) : nouveau: {'aliases': ['Transmission Dispersion Abbe Number'], 'bl_idname': 'NodeSocketFloat', 'label': 'Transmission Dispersion Abbe Number', 'name': 'Transmission Dispersion Abbe Number', 'socket_type': 'VALUE'}
- info / inputs / Transmission Dispersion Scale (added) : nouveau: {'aliases': ['Transmission Dispersion Scale'], 'bl_idname': 'NodeSocketFloatFactor', 'label': 'Transmission Dispersion Scale', 'name': 'Transmission Dispersion Scale', 'socket_type': 'VALUE'}

#### Vector Transform

Blender identifier: `ShaderNodeVectorTransform`

##### Old version

- `Vector.vector_transform(self, vector_type: T_VECTOR_TYPE_2='VECTOR', convert_from: T_CONVERT_FROM_1='WORLD', convert_to: T_CONVERT_FROM_1='OBJECT')`

##### New version

- `Vector.vector_transform(self, vector_type: T_VECTOR_TYPE_2='VECTOR', convert_from: T_CONVERT_FROM_1='WORLD', convert_to: T_CONVERT_FROM_1='OBJECT')`

##### Changes

- info / params / convert_from / enum (modified) : ancien: ('WORLD', 'OBJECT', 'CAMERA') → nouveau: ('WORLD', 'OBJECT', 'CAMERA', 'LIGHT')
- info / params / convert_to / enum (modified) : ancien: ('WORLD', 'OBJECT', 'CAMERA') → nouveau: ('WORLD', 'OBJECT', 'CAMERA', 'LIGHT')

