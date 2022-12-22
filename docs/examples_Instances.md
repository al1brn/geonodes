## Examples

### Initialization

A **Instances** can be initialized:
- by typecasting another geometry
- or by using the constructor `InstanceOnPoints`

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # ---- We'll instanciate the input geometry on points
    
    mesh = tree.ig
    mesh.transform(scale=.1)
    
    # ----- Let's create the points
    
    points = gn.Points.Points(count=100)
    points.points.position = gn.random_vector(min=-5, max=5)
    
    # ----- We can construct our instances
    
    instances = gn.Instances.InstanceOnPoints(points=points, instance=mesh)
    
    tree.og = instances
```

