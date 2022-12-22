**Domain** is the root class for:
- [Vertex](Vertex.md), node domain *'POINT'*
- [Edge](Edge.md), node domain *'EDGE'*
- [Face](Face.md), node domain *'FACE'*
- [Corner](Corner.md), node domain *'CORNER'*
- [ControlPoint](ControlPoint.md), node domain *'POINT'*
- [Spline](Spline.md), node domain *'SPLINE' (or *'CURVE'*)
- [CloudPoint](CloudPoint.md), node domain *'POINT'*
- [Instance](Instance.md), node domain *'INSTANCE'*


**Domain** provides mechanism to keep the context, by maintaining:
- the `selection`
- the node domain value in *'POINT'*, *'EDGE'*, *'FACE'*, *'CORNER'*, *'SPLINE'*, *'INSTANCE'*
- the geometry it is a domain of

> By keeping the context geometry, it is not necessary to explicitly create **Capture Attribute**.
  **Domain** class determines if it is necessary or not to create this node.

**Domains** are not initialized directly but by geometries:
- [Mesh](Mesh.md) initializes 4 domains:
  - `verts` property of type [Vertex](Vertex.md)
  - `edges` property of type [Edge](Edge.md)
  - `faces` property of type [Face](Face.md)
  - `corners` property of type [Corner](Corner.md)
- [Curve](Curve.md) initializes 2 domains:
  - `points` property of type [ControlPoint](ControlPoint.md)
  - `splines` property of type [Spline](Spline.md)
- [Instances](Instances.md) initializes 1 domain: 
  - `insts` property of type [Instance](Instance.md)
- [Points](Points.md) initializes 1 domain: 
  - `points` property of type [CloudPoint](CloudPoint.md)

> Note that the node domain *'POINT'* is used by 3 **Domains**.

## Selection mechanism

One important feature of **Domain** is the selection mechanism. The selection is expressed using the array syntax:
- `mesh.verts[1]` : select the `index == 1`
- `mesh.faces[10:20]` : select the `index` in the range 10 to 20 (exc)
- `mesh.faces[8, 17]` : select the `index` equal to 8 or 17
- `mesh.edges[(mesh.edges.index % 2).equal(0)]` : select the even `index`

Nodes having a **Selection** socket use the **Domain** selection initialized with this syntax.

In the following example, two vertices selected by the user are move upwards:

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    index1 = gn.Integer.Input(0, "Index 1")
    index2 = gn.Integer.Input(1, "Index 2")
    
    cube = gn.Mesh.Cube()
    
    cube.verts[index1, index2].position += (0, 0, .2)
    
    tree.og = cube
```

