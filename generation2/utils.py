"""Utilities shared by the generation tools."""

import bpy
from time import perf_counter


NODE_NAMES = {}


def get_node_names(tree_type="GeometryNodeTree"):
    """Return cached bl_idname -> UI name entries for this tree type.

    Discover each catalogue once per module lifetime. Only strings are cached,
    never Blender references. Treat the returned dictionary as read-only.
    Clear the cache after registering/unregistering node types or changing UI
    language with clear_node_cache().
    """
    if tree_type in NODE_NAMES:
        return NODE_NAMES[tree_type]
    tree = bpy.data.node_groups.new(name="Loop on Nodes", type=tree_type)
    try:
        nodes = {}
        for type_name in dir(bpy.types):
            try:
                node = tree.nodes.new(type=type_name)
            except (RuntimeError, TypeError):
                continue
            nodes[node.bl_idname] = node.name
            tree.nodes.clear()
    finally:
        bpy.data.node_groups.remove(tree)
    NODE_NAMES[tree_type] = dict(sorted(nodes.items(), key=lambda item: (item[1].casefold(), item[0])))
    return NODE_NAMES[tree_type]


def clear_node_cache(tree_type=None):
    """Invalidate one catalogue, or all catalogues when tree_type is None."""
    if tree_type is None:
        NODE_NAMES.clear()
    else:
        NODE_NAMES.pop(tree_type, None)


def loop_on_nodes(func, tree_type="GeometryNodeTree"):
    """Apply func(node) in UI-name order using the cached node catalogue.

    Create and clear nodes individually to avoid updating a tree containing
    every supported node. Always remove the temporary tree, even on errors.
    """
    started = perf_counter()
    hook_time = 0.0
    tree = None
    try:
        nodes = get_node_names(tree_type)
        tree = bpy.data.node_groups.new(name="Loop on Nodes", type=tree_type)
        for identifier in nodes:
            node = tree.nodes.new(type=identifier)
            try:
                hook_started = perf_counter()
                try:
                    func(node)
                finally:
                    hook_time += perf_counter() - hook_started
            finally:
                tree.nodes.clear()
    finally:
        try:
            if tree is not None:
                bpy.data.node_groups.remove(tree)
        finally:
            total_time = perf_counter() - started
            print(f"loop_on_nodes ({tree_type}): total={total_time:.3f}s, "
                  f"hooks={hook_time:.3f}s, outside hooks={total_time - hook_time:.3f}s")


def to_mk_table(headers, lines, prefix=''):
    """
    Build a padded Markdown table with optional left indentation.

    Parameters
    ----------
    headers : list of str
    lines : list of list
    indent : int
        Number of spaces to indent the table (use 4 inside docstrings).

    Returns
    -------
    str
    """

    # Normalize
    headers = [str(h) for h in headers]

    old = lines
    lines = []
    for line in old:
        skind = str(line[0]).title()
        sname = f"`{str(line[1])}`" if skind == 'Parameter' else str(line[1])
        lines.append([skind, sname, str(line[2])])

    cols = len(headers)

    # Compute widths
    widths = [len(headers[i]) for i in range(cols)]
    for row in lines:
        for i in range(cols):
            if i < len(row):
                widths[i] = max(widths[i], len(row[i]))

    # Header
    header_line = prefix + "| " + " | ".join(
        headers[i].ljust(widths[i]) for i in range(cols)
    ) + " |"

    # Separator
    sep_line = prefix + "| " + " | ".join(
        "-" * widths[i] for i in range(cols)
    ) + " |"

    # Rows
    row_lines = []
    for row in lines:
        padded = [
            (row[i] if i < len(row) else "").ljust(widths[i])
            for i in range(cols)
        ]
        row_lines.append(prefix + "| " + " | ".join(padded) + " |")

    return "\n".join([header_line, sep_line] + row_lines)
