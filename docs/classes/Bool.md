# class Bool (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
------
 - Type : BOOLEAN
 - bl_idname : NodeSocketBool

Methods
-------
 - [band](#band) : BooleanMath, boolean=self, operation='AND'
 - [bnot](#bnot) : BooleanMath, boolean=self, operation='NOT'
 - [boolean_math](#boolean_math) : BooleanMath, boolean=self
 - [bor](#bor) : BooleanMath, boolean=self, operation='OR'
 - [curve_handle_positions](#curve_handle_positions) : CurveHandlePositions, relative=self, return node
 - [edge_paths_to_selection](#edge_paths_to_selection) : EdgePathsToSelection, start_vertices=self
 - [edges_to_face_groups](#edges_to_face_groups) : EdgesToFaceGroups, boundary_edges=self, return socket
 - [imply](#imply) : BooleanMath, boolean=self, operation='IMPLY'
 - [nand](#nand) : BooleanMath, boolean=self, operation='NAND'
 - [nimply](#nimply) : BooleanMath, boolean=self, operation='NIMPLY'
 - [nor](#nor) : BooleanMath, boolean=self, operation='NOR'
 - [switch](#switch) : Switch, false=self, input_type='BOOLEAN'
 - [xnor](#xnor) : BooleanMath, boolean=self, operation='XNOR'
 - [xor](#xor) : BooleanMath, boolean=self, operation='XOR'

## Methods

### band

BooleanMath, boolean=self, operation='AND'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### bnot

BooleanMath, boolean=self, operation='NOT'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### boolean_math

BooleanMath, boolean=self

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### bor

BooleanMath, boolean=self, operation='OR'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### curve_handle_positions

CurveHandlePositions, relative=self, return node

Node
----
 - class_name : [CurveHandlePositions](/docs/classes/CurveHandlePositions.md)
 - bl_idname : GeometryNodeInputCurveHandlePositions

### edge_paths_to_selection

EdgePathsToSelection, start_vertices=self

Node
----
 - class_name : [EdgePathsToSelection](/docs/classes/EdgePathsToSelection.md)
 - bl_idname : GeometryNodeEdgePathsToSelection

### edges_to_face_groups

EdgesToFaceGroups, boundary_edges=self, return socket

Node
----
 - class_name : [EdgesToFaceGroups](/docs/classes/EdgesToFaceGroups.md)
 - bl_idname : GeometryNodeEdgesToFaceGroups

### imply

BooleanMath, boolean=self, operation='IMPLY'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### nand

BooleanMath, boolean=self, operation='NAND'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### nimply

BooleanMath, boolean=self, operation='NIMPLY'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### nor

BooleanMath, boolean=self, operation='NOR'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### switch

Switch, false=self, input_type='BOOLEAN'

Node
----
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

### xnor

BooleanMath, boolean=self, operation='XNOR'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

### xor

BooleanMath, boolean=self, operation='XOR'

Node
----
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath
