# class Tree

**Tree** contains all the nodes and links. A **tree** must be initialized before nodes creation.
Once the nodes are created, they are arranged for a better readability. Hence, creating a **Tree** follows 3 steps:

- Initialization
- Nodes creation
- Closing

This is implemented using the pyton context manager:

```python
with Tree(...) as tree:
    ... nodes creation
```

## Modifier and Custom group

A **Tree** can be created to be directly used in a Geometry Nodes Modifier or to be a **Group** used in other trees.
When a **Tree** is created to be used in a modifier, there is a **Geometry** input socket and a geometry output socket.

## Initialization parameters

```python
class Tree:
    def __init__(self, tree_name, clear=False, group=False, fake_user=False, prefix=None):
```


The **Tree** initialization parameters are:
- `tree_name` (str): name of the **Tree**. This is the name which appears in the **Geometry nodes** modifier selector.
- `clear` (bool) : delete existing nodes
- `group` (bool) : No input and output geometry sockets if True.
- `fake_user` (bool) : fake user flag. Won't be delete if the **Tree** is not used.
- `prefix` (str or [Trees](Trees.md)) : prefix to add the the **Tree** name. For big projects, allows to group tree with a common prefix. See [Trees](Trees.md)

## Input and Output Geometries

For modifier **Trees**, input and output geometries can be access with properties `input_geometry` and `outpout_geometry`.
For convenience, short version are provided: `ig` and `og`.

Here below is the 'do nothing' tree:

```python
import geonodes as gn

with Tree("Do nothing") as tree:
    tree.og = tree.ig
```

## Layouts

One can create **Layouts** when generating nodes in order to enhance the readability of the final tree.
This is done through the **layout** method open and closed with a context manager.

```python
import geonodes as gn

with gn.Tree("Tree with a layout") as tree:
    
    mesh = gn.Mesh.Cube()
    
    # In the following context, nodes will be created in a layout
    
    with tree.layout("Computation of vertices"):

        # Vertices position
        v = mesh.verts.position
        
        # Which one are z < 0
        neg = v.z.less_than(0)
        
        # Operation on this selection
        mesh.verts[neg].position = v * 2
        
    # Back to the main tree
    
    mesh.faces.shade_smooth = True
    
    tree.og = mesh
```




 
