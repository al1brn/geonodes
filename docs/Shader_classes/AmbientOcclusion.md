# class AmbientOcclusion (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : AmbientOcclusion
 - bl_idname : ShaderNodeAmbientOcclusion

Node parameters
 - inside : False
 - only_local : False
 - samples : 16

Input sockets
 - color : Col
 - distance : Float
 - normal : Vect

Output sockets
 - color : Col
 - ao : Float

### Header

``` python
def AmbientOcclusion(self, color=None, distance=None, normal=None, inside=False, only_local=False, samples=16, node_label=None, node_color=None):
```

## Implementations

o Col : [ambient_occlusion](#ambient_occlusion) 

