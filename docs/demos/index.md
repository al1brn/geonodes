# Demo files

The repository contains demonstrations in `demos/` and `demos/`. Individual
modules may retain historical entry points and node names. Use the implementation
matching your Blender version when running them; the guide examples below use
the current decorator API.

For current projects, import decorated builders and construct one member or a
whole [Package](../getting_started/packages.md):

```python
# In your own module containing a Package subclass:
# Project.result.build()           # selected modifier
# Project.result.build(full=True)  # include dependencies
# Project.build(full=True)         # all package members and dependencies
```

Inside another builder, call an imported group as `create_plank(width=0.4)` to
insert a Group node. Outside a tree, use `.build()`. Function arguments connect
sockets, not build-time Python settings. Public `.build()` takes `full`, not
`rebuild`. Historical `demo(rebuild=False)` functions are module-specific
wrappers; they are not the builder API and may require migration.

See [Modifiers, groups and tools](../getting_started/modifiers_groups.md) and the
[migration guide](../getting_started/migration.md) before adapting older demos.

The avaiable demos are:

- [shaders](shaders.md) : simple materials
- [random](random.md) : random values generators
- [arrows](arrows.md) : single arrow and field of arrows
- [counters](counters.md) : clocks and counters
- [curly](curly.md) : playing with curve handles
- [explosion](explosion.md) : kinematics simulation with gravity and viscosity,
  how to fracture a mesh
- [topology](topology.md) : displaying domain indices
- [cam_culling](cam_culling.md) : remove geometry outside camera field of view
- [furniture](furniture.md) : block-based furniture construction, dimensions, and cut sheets









