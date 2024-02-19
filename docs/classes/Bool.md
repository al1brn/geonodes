# class Bool (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : BOOLEAN
 - bl_idname : NodeSocketBool

Methods
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
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'AND'
 - node_label : node_label
 - node_color : node_color

``` python
def band(self, boolean=None, node_label=None, node_color=None):
```
### bnot

BooleanMath, boolean=self, operation='NOT'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - operation : 'NOT'
 - node_label : node_label
 - node_color : node_color

``` python
def bnot(self, node_label=None, node_color=None):
```
### boolean_math

BooleanMath, boolean=self

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - operation : 'AND'
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : operation
 - node_label : node_label
 - node_color : node_color

``` python
def boolean_math(self, boolean=None, operation='AND', node_label=None, node_color=None):
```
### bor

BooleanMath, boolean=self, operation='OR'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'OR'
 - node_label : node_label
 - node_color : node_color

``` python
def bor(self, boolean=None, node_label=None, node_color=None):
```
### curve_handle_positions

CurveHandlePositions, relative=self, return node

Node
 - class_name : [CurveHandlePositions](/docs/classes/CurveHandlePositions.md)
 - bl_idname : GeometryNodeInputCurveHandlePositions

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - relative : self
 - node_label : node_label
 - node_color : node_color

``` python
def curve_handle_positions(self, node_label=None, node_color=None):
```
### edge_paths_to_selection

EdgePathsToSelection, start_vertices=self

Node
 - class_name : [EdgePathsToSelection](/docs/classes/EdgePathsToSelection.md)
 - bl_idname : GeometryNodeEdgePathsToSelection

Arguments
 - next_vertex_index : None
 - node_label : None
 - node_color : None

Node initialization
 - start_vertices : self
 - next_vertex_index : next_vertex_index
 - node_label : node_label
 - node_color : node_color

``` python
def edge_paths_to_selection(self, next_vertex_index=None, node_label=None, node_color=None):
```
### edges_to_face_groups

EdgesToFaceGroups, boundary_edges=self, return socket

Node
 - class_name : [EdgesToFaceGroups](/docs/classes/EdgesToFaceGroups.md)
 - bl_idname : GeometryNodeEdgesToFaceGroups

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - boundary_edges : self
 - node_label : node_label
 - node_color : node_color

``` python
def edges_to_face_groups(self, node_label=None, node_color=None):
```
### imply

BooleanMath, boolean=self, operation='IMPLY'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'IMPLY'
 - node_label : node_label
 - node_color : node_color

``` python
def imply(self, boolean=None, node_label=None, node_color=None):
```
### nand

BooleanMath, boolean=self, operation='NAND'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'NAND'
 - node_label : node_label
 - node_color : node_color

``` python
def nand(self, boolean=None, node_label=None, node_color=None):
```
### nimply

BooleanMath, boolean=self, operation='NIMPLY'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'NIMPLY'
 - node_label : node_label
 - node_color : node_color

``` python
def nimply(self, boolean=None, node_label=None, node_color=None):
```
### nor

BooleanMath, boolean=self, operation='NOR'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'NOR'
 - node_label : node_label
 - node_color : node_color

``` python
def nor(self, boolean=None, node_label=None, node_color=None):
```
### switch

Switch, false=self, input_type='BOOLEAN'

Node
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

Arguments
 - switch : None
 - true : None
 - node_label : None
 - node_color : None

Node initialization
 - switch : switch
 - false : self
 - true : true
 - input_type : 'BOOLEAN'
 - node_label : node_label
 - node_color : node_color

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
### xnor

BooleanMath, boolean=self, operation='XNOR'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'XNOR'
 - node_label : node_label
 - node_color : node_color

``` python
def xnor(self, boolean=None, node_label=None, node_color=None):
```
### xor

BooleanMath, boolean=self, operation='XOR'

Node
 - class_name : [BooleanMath](/docs/classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - boolean_1 : boolean
 - operation : 'XOR'
 - node_label : node_label
 - node_color : node_color

``` python
def xor(self, boolean=None, node_label=None, node_color=None):
```