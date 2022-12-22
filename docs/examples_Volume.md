## Examples

### Initialization

A **Volume** can be initialized:
- by typecasting another geometry
- or by using the constructor `Cube`

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # ---- Parameters
    
    size    = gn.Float.Input(1, "Volume size", min_value=.1, max_value=10)
    density = gn.Float.Input(1, "Density",     min_value=0., max_value=30)
    
    # ---- Let's initialize the volume
    
    volume = gn.Volume.Cube(min=-size/2, max=size/2, density=density)
    
    tree.og = volume
```
