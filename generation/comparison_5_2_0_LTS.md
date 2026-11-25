# Comparaison Blender (5, 3, 0) → (5, 2, 0)

## GeometryNodeTree

### Nœuds supprimés (20)

- **Get Vector Component** (`FunctionNodeGetVectorComponent`)
- **Combine List** (`GeometryNodeCombineList`)
- **Construct Curves** (`GeometryNodeConstructCurves`)
- **Geometry Materials** (`GeometryNodeGeometryMaterials`)
- **Get Grid Names** (`GeometryNodeGetGridNames`)
- **Grease Pencil Color** (`GeometryNodeGreasePencilColor`)
- **Grease Pencil Draw Time** (`GeometryNodeGreasePencilDrawTime`)
- **Grease Pencil Fill ID** (`GeometryNodeGreasePencilFillID`)
- **Grease Pencil Opacity** (`GeometryNodeGreasePencilOpacity`)
- **Grease Pencil Stroke Softness** (`GeometryNodeGreasePencilStrokeSoftness`)
- **Grease Pencil Stroke Visibility** (`GeometryNodeGreasePencilStrokeVisibility`)
- **Deactivate Voxels** (`GeometryNodeGridDeactivateVoxels`)
- **Grid Solve Poisson** (`GeometryNodeGridSolvePoisson`)
- **Grid Topology Boolean** (`GeometryNodeGridTopologyBoolean`)
- **Import SPZ** (`GeometryNodeImportSPZ`)
- **NURBS Order** (`GeometryNodeNURBSOrder`)
- **NURBS Weight** (`GeometryNodeNURBSWeight`)
- **Set Point Cloud Type** (`GeometryNodePointsSetType`)
- **Rasterize Points** (`GeometryNodeRasterizePoints`)
- **Comment** (`NodeComment`)

### Nœuds ajoutés (0)

Aucun.


### Nœuds modifiés (8)

- **Bone Info** (`GeometryNodeBoneInfo`)
  - info / outputs / Envelope Distance (removed) : ancien: {'aliases': ['Envelope Distance'], 'bl_idname': 'NodeSocketFloat', 'label': 'Envelope Distance', 'name': 'Envelope Distance', 'socket_type': 'VALUE'}
  - info / outputs / Radius Head (removed) : ancien: {'aliases': ['Radius Head'], 'bl_idname': 'NodeSocketFloat', 'label': 'Radius Head', 'name': 'Radius Head', 'socket_type': 'VALUE'}
  - info / outputs / Radius Tail (removed) : ancien: {'aliases': ['Radius Tail'], 'bl_idname': 'NodeSocketFloat', 'label': 'Radius Tail', 'name': 'Radius Tail', 'socket_type': 'VALUE'}
- **Curve to Mesh** (`GeometryNodeCurveToMesh`)
  - info / inputs / Miter Scale (removed) : ancien: {'aliases': ['Miter Scale'], 'bl_idname': 'NodeSocketBool', 'label': 'Miter Scale', 'name': 'Miter Scale', 'socket_type': 'BOOLEAN'}
  - info / inputs / Miter Scale Limit (removed) : ancien: {'aliases': ['Miter Scale Limit'], 'bl_idname': 'NodeSocketFloatAngle', 'label': 'Miter Scale Limit', 'name': 'Miter Scale Limit', 'socket_type': 'VALUE'}
- **Import PLY** (`GeometryNodeImportPLY`)
  - info / outputs / Geometry (removed) : ancien: {'aliases': ['Geometry'], 'bl_idname': 'NodeSocketGeometry', 'label': 'Geometry', 'name': 'Geometry', 'socket_type': 'GEOMETRY'}
  - info / outputs / Mesh (added) : nouveau: {'aliases': ['Mesh'], 'bl_idname': 'NodeSocketGeometry', 'label': 'Mesh', 'name': 'Mesh', 'socket_type': 'GEOMETRY'}
- **Merge Layers** (`GeometryNodeMergeLayers`)
  - info / inputs / Mode (removed) : ancien: {'aliases': ['Mode'], 'bl_idname': 'NodeSocketMenu', 'label': 'Mode', 'name': 'Mode', 'socket_type': 'MENU'}
  - info / menu_sockets / Mode (removed) : ancien: {'default': 'By Name', 'values': ('By Name', 'By Group ID')}
- **Realize Instances** (`GeometryNodeRealizeInstances`)
  - info / inputs / Preserve Normals (removed) : ancien: {'aliases': ['Preserve Normals'], 'bl_idname': 'NodeSocketBool', 'label': 'Preserve Normals', 'name': 'Preserve Normals', 'socket_type': 'BOOLEAN'}
- **Sample Grid** (`GeometryNodeSampleGrid`)
  - info / menu_sockets / Interpolation / values (modified) : ancien: ('Nearest Neighbor', 'Trilinear', 'Triquadratic', 'Tricubic') → nouveau: ('Nearest Neighbor', 'Trilinear', 'Triquadratic')
- **Set Grease Pencil Color** (`GeometryNodeSetGreasePencilColor`)
  - info / inputs / Mode (removed) : ancien: {'aliases': ['Mode'], 'bl_idname': 'NodeSocketMenu', 'label': 'Mode', 'name': 'Mode', 'socket_type': 'MENU'}
  - info / menu_sockets / Mode (removed) : ancien: {'default': 'Stroke', 'values': ('Stroke', 'Fill', 'Both')}
  - info / params / mode / enum (modified) : ancien: ('STROKE', 'FILL', 'BOTH') → nouveau: ('STROKE', 'FILL')
- **Set Grease Pencil Depth** (`GeometryNodeSetGreasePencilDepth`)
  - info / inputs / Depth Order (removed) : ancien: {'aliases': ['Depth Order'], 'bl_idname': 'NodeSocketMenu', 'label': 'Depth Order', 'name': 'Depth Order', 'socket_type': 'MENU'}
  - info / menu_sockets / Depth Order (removed) : ancien: {'default': '2D Layers', 'values': ('2D Layers', '3D Location')}

## ShaderNodeTree

### Nœuds supprimés (27)

- **Boolean Math** (`FunctionNodeBooleanMath`)
- **Find in String** (`FunctionNodeFindInString`)
- **Format String** (`FunctionNodeFormatString`)
- **Get Vector Component** (`FunctionNodeGetVectorComponent`)
- **Special Characters** (`FunctionNodeInputSpecialCharacters`)
- **String** (`FunctionNodeInputString`)
- **Integer Math** (`FunctionNodeIntegerMath`)
- **Match String** (`FunctionNodeMatchString`)
- **Replace String** (`FunctionNodeReplaceString`)
- **Reverse String** (`FunctionNodeReverseString`)
- **Set String Case** (`FunctionNodeSetStringCase`)
- **Slice String** (`FunctionNodeSliceString`)
- **String Length** (`FunctionNodeStringLength`)
- **String to Value** (`FunctionNodeStringToValue`)
- **Trim String** (`FunctionNodeTrimString`)
- **Value to String** (`FunctionNodeValueToString`)
- **Index Switch** (`GeometryNodeIndexSwitch`)
- **Switch** (`GeometryNodeSwitch`)
- **Warning** (`GeometryNodeWarning`)
- **Comment** (`NodeComment`)
- **Enable Output** (`NodeEnableOutput`)
- **Light Accumulation** (`ShaderNodeLightAccumulation`)
- **Light Evaluation** (`ShaderNodeLightEvaluation`)
- **Light Info** (`ShaderNodeLightInfo`)
- **Light Iter Internal Input** (`ShaderNodeLightIterInternalInput`)
- **Light Iter Internal Output** (`ShaderNodeLightIterInternalOutput`)
- **Shadow Raycast** (`ShaderNodeShadowRaycast`)

### Nœuds ajoutés (0)

Aucun.


### Nœuds modifiés (4)

- **Attribute** (`ShaderNodeAttribute`)
  - info / params / attribute_type / enum (modified) : ancien: ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER', 'LIGHT') → nouveau: ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
- **Glass BSDF** (`ShaderNodeBsdfGlass`)
  - info / inputs / Anisotropy (removed) : ancien: {'aliases': ['Anisotropy'], 'bl_idname': 'NodeSocketFloatFactor', 'label': 'Anisotropy', 'name': 'Anisotropy', 'socket_type': 'VALUE'}
  - info / inputs / Rotation (removed) : ancien: {'aliases': ['Rotation'], 'bl_idname': 'NodeSocketFloatFactor', 'label': 'Rotation', 'name': 'Rotation', 'socket_type': 'VALUE'}
  - info / inputs / Tangent (removed) : ancien: {'aliases': ['Tangent'], 'bl_idname': 'NodeSocketVector', 'label': 'Tangent', 'name': 'Tangent', 'socket_type': 'VECTOR'}
- **Principled BSDF** (`ShaderNodeBsdfPrincipled`)
  - info / inputs / Transmission Dispersion Abbe Number (removed) : ancien: {'aliases': ['Transmission Dispersion Abbe Number'], 'bl_idname': 'NodeSocketFloat', 'label': 'Transmission Dispersion Abbe Number', 'name': 'Transmission Dispersion Abbe Number', 'socket_type': 'VALUE'}
  - info / inputs / Transmission Dispersion Scale (removed) : ancien: {'aliases': ['Transmission Dispersion Scale'], 'bl_idname': 'NodeSocketFloatFactor', 'label': 'Transmission Dispersion Scale', 'name': 'Transmission Dispersion Scale', 'socket_type': 'VALUE'}
- **Vector Transform** (`ShaderNodeVectorTransform`)
  - info / params / convert_from / enum (modified) : ancien: ('WORLD', 'OBJECT', 'CAMERA', 'LIGHT') → nouveau: ('WORLD', 'OBJECT', 'CAMERA')
  - info / params / convert_to / enum (modified) : ancien: ('WORLD', 'OBJECT', 'CAMERA', 'LIGHT') → nouveau: ('WORLD', 'OBJECT', 'CAMERA')
