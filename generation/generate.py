""" Generate geonodes API from current Blender version

# Overview

To create a new version, manual update is necessary to:
- take info account a new type of socket
- update low level descriptions
- define specific ways of implementing new nodes

# New type of socket

If a new type of socket is introduced in the current Blender version,
`generate` will stop with the list of unknown sockets.

The new sockets must be declared in `config.SOCKET_BLID_TO_TYPE` which
provides the socket `type` for each socket `bl_idname`.

The default class name is the "title" version of socket `type` (BOOLEAN -> Boolean)



If a new type of socket is introduced in the new Blender version,


"""

from importlib import reload

from .context import TREE_TYPES, TREE_MODULES, node_dims

from . import gen_config, target_core


def write_files(trees):
    """Render every selected environment before writing any generated module."""
    core_path = target_core()
    modules = {}
    for tree in trees.values():
        modules.update(tree.render_modules(core_path))
    count = 0
    for path, source in modules.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(source, encoding='utf-8')
        count += 1
    print(f'Generated: {count} files')


def generate(*, tree_type=None, write=True):
    """Build configuration, then collect one independent TreeClass per environment.

    Return a tree_type -> TreeClass mapping, including sources and cross refs.
    write=False collects sources without writing generated files.
    """
    selected = TREE_TYPES if tree_type is None else (tree_type,)
    for selected_type in selected:
        if selected_type not in TREE_TYPES:
            raise ValueError(f'Unsupported tree type: {selected_type!r}')
    if write:
        target_core()
    reload(node_dims)
    gen_config.build()
    from .tree_class import TreeClass
    trees = {selected_type: TreeClass(selected_type).generate() for selected_type in selected}
    if write:
        write_files(trees)
    environments = ', '.join(TREE_MODULES[selected_type] for selected_type in selected)
    action = 'Generation completed' if write else 'Source collection completed (no files written)'
    print(f'\n{action}: {environments}.')
    return trees
