# Node TranslateInstances

- Node name : 'Translate Instances'
- bl_idname : GeometryNodeTranslateInstances


``` python
TranslateInstances(instances=None, selection=None, translation=None, local_space=None, node_label=None, node_color=None)
```
##### Arguments

- instances : None
- selection : None
- translation : None
- local_space : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [translate_instances](/docs/GeoNodes/Geometry.md#translate_instances)

## Init

``` python
def __init__(self, instances=None, selection=None, translation=None, local_space=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeTranslateInstances', node_label=node_label, node_color=node_color)

    self.instances       = instances
    self.selection       = selection
    self.translation     = translation
    self.local_space     = local_space
```
