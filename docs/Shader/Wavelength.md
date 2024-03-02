# Node Wavelength

- Node name : 'Wavelength'
- bl_idname : [ShaderNodeWavelength](https://docs.blender.org/api/current/bpy.types.ShaderNodeWavelength.html)


``` python
Wavelength(wavelength=None, node_label=None, node_color=None)
```
##### Arguments

- wavelength : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, wavelength=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeWavelength', node_label=node_label, node_color=node_color)

    self.wavelength      = wavelength
```