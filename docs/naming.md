# Naming conventions

> Blend has names for nodes, nodes sockets, nodes parameters and nodes parameters values.
> This section explains the conventions used to name python classes, methods and properties after these names

## Nodes

The nodes class names are **CamelCase** versions of their Blender name:
- 'Replace Material' --> **ReplaceMaterial**
- 'Check Texture' --> **CheckerTexture**

Note the Blender node 'ColorRamp' which is strangely name in one word. This CamelCase named is kept:
- 'ColorRamp' --> **ColorRamp**

## Output sockets

Output sockets are implemented as properties of node classes.
Their python name is the **snake_case** of their name.
Since, the most often, the socket names are single words, their python name is the lower case version of their name:
- Geometry --> geomtry
- Attribute --> attribute
- Value --> value

## Data sockets

Data socket classes are named as described 


