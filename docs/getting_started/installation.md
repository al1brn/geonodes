# Installation

**geonodes** is a python package. To install it, copy the package folder **geonodes** in `scripts/modules`.

The Blender `scripts` folder is defined in Blender preferences, see: [Blender File Paths settings](https://docs.blender.org/manual/en/latest/editors/preferences/file_paths.html).

> Note that **geonodes** is a python module, not an Blender addon

After the install, the Blender scripts hierarchy should look like:
```
.../scripts/
       modules/
           geonodes/
               __init__.py
               core
               demos
               ...
```

To make the module available in your script, use `import` in your script:

```python
from geonodes import *
```

## Check the builder API

Run this in Blender's Text Editor:

```python
from geonodes import *

@modifier("Installation Check")
def installation_check():
    Mesh.Cube().out()

installation_check.build()
```

Select **Installation Check** as the node group of a Geometry Nodes modifier.
Decorated functions wait for `.build()`; running the declaration alone creates
no tree. Continue with [Hello World](hello_world.md),
[Modifiers, groups and tools](modifiers_groups.md), and [Packages](packages.md).

The current guides describe the decorator API, including newer `core_new`
features. Blender 5.2.0 selects the legacy `core`; other supported builds select
`core_new`. Use the generated node API matching your Blender version.
