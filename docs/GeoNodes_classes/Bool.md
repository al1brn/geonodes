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

> BooleanMath, boolean=self, operation='AND'

``` python
def band(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### bnot

> BooleanMath, boolean=self, operation='NOT'

``` python
def bnot(self, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - boolean : self
 - operation : 'NOT'
 - node_label : node_label
 - node_color : node_color

### boolean_math

> BooleanMath, boolean=self

``` python
def boolean_math(self, boolean=None, operation='AND', node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### bor

> BooleanMath, boolean=self, operation='OR'

``` python
def bor(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### curve_handle_positions

> CurveHandlePositions, relative=self, return node

``` python
def curve_handle_positions(self, node_label=None, node_color=None):
```
Node
 - class_name : [CurveHandlePositions](/docs/GeoNodes_classes/CurveHandlePositions.md)
 - bl_idname : GeometryNodeInputCurveHandlePositions

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - relative : self
 - node_label : node_label
 - node_color : node_color

### edge_paths_to_selection

> EdgePathsToSelection, start_vertices=self

``` python
def edge_paths_to_selection(self, next_vertex_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [EdgePathsToSelection](/docs/GeoNodes_classes/EdgePathsToSelection.md)
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

### edges_to_face_groups

> EdgesToFaceGroups, boundary_edges=self, return socket

``` python
def edges_to_face_groups(self, node_label=None, node_color=None):
```
Node
 - class_name : [EdgesToFaceGroups](/docs/GeoNodes_classes/EdgesToFaceGroups.md)
 - bl_idname : GeometryNodeEdgesToFaceGroups

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - boundary_edges : self
 - node_label : node_label
 - node_color : node_color

### imply

> BooleanMath, boolean=self, operation='IMPLY'

``` python
def imply(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### nand

> BooleanMath, boolean=self, operation='NAND'

``` python
def nand(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### nimply

> BooleanMath, boolean=self, operation='NIMPLY'

``` python
def nimply(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### nor

> BooleanMath, boolean=self, operation='NOR'

``` python
def nor(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### switch

> Switch, false=self, input_type='BOOLEAN'

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
Node
 - class_name : [Switch](/docs/GeoNodes_classes/Switch.md)
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

### xnor

> BooleanMath, boolean=self, operation='XNOR'

``` python
def xnor(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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

### xor

> BooleanMath, boolean=self, operation='XOR'

``` python
def xor(self, boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
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
