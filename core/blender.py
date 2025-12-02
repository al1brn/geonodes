"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC hidden

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : blender
------------------
- Access to blender features

updates
-------
- creation : 2025/02/22
"""

from typing import Literal
from pathlib import Path

import bpy
from bpy.types import VectorFont

# ====================================================================================================
# Load a system font

def get_font(name: str|VectorFont, path: str|None = None) -> VectorFont | None:
    """ Get a font by its name

    Arguments
    ---------
    - name : font name
    - path : path the font file

    Returns
    -------
    - font
    """
    if name is None:
        return None

    if isinstance(name, VectorFont):
        return name

    font = bpy.data.fonts.get(name)
    if font is None:
        if path is None:
            path = bpy.context.preferences.filepaths.font_directory
        font = bpy.data.fonts.load(str(Path(path) / (name + '.ttf')))
        font.name = name

    return font

# ====================================================================================================
# Editor context
# ====================================================================================================

def find_node_editor(tree=None):

    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type != 'NODE_EDITOR':
                continue

            if (tree is not None) and (area.ui_type != tree.bl_idname):
                continue

            space = area.spaces.active

            region = next((r for r in area.regions if r.type == 'WINDOW'), None)
            if region is None:
                continue

            if tree is not None:
                space.node_tree = tree

            print("Blender Find Editor", window, screen, area, region, space, space.node_tree)

            return {
                "window"    : window,
                "screen"    : screen,
                "area"      : area,
                "region"    : region,
                "space_data": space,
            }

    return None

def node_editor_context(tree=None):
    return bpy.context.temp_override(**find_node_editor(tree))

# ====================================================================================================
# Get the list of modifiers using geometry nodes tree

def get_geonodes_modifiers(tree):

    if tree.bl_idname != 'GeometryNodeTree':
        return []
    
    modifiers = []
    for obj in bpy.data.objects:
        for mod in obj.modifiers:
            if not isinstance(mod, bpy.types.NodesModifier) or (mod.node_group != tree):
                continue

            modifiers.append(mod)

    return modifiers

# ====================================================================================================
# Resource paths
# ====================================================================================================

def get_resource_path(name: Literal['DATAFILES', 'SCRIPTS', 'EXTENSIONS', 'PYTHON']='DATAFILES') -> Path:
    path = Path(bpy.utils.system_resource(name))
    assert path.is_dir(), f"Path {name}: '{path}' is not a dir"
    return path

def get_nodes_path(name: str):
    path = get_resource_path('DATAFILES') / "assets/nodes"
    assert path.is_dir(), f"Path '{path}' is not a dir."

    fname = path / name
    assert fname.exists(), f"File {fname} doesn't exist in {path}."

    return fname

def load_builtin_node_group(file_name: str, group_name: str = None):

    get_list = group_name is None

    if not get_list and group_name in bpy.data.node_groups:
        return bpy.data.node_groups[group_name]
    
    file_path = get_nodes_path(file_name)

    with bpy.data.libraries.load(str(file_path)) as (data_from, data_to):

        if get_list:
            return list(data_from.node_groups)

        if group_name not in data_from.node_groups:
            return None

        data_to.node_groups = [group_name]

    return bpy.data.node_groups[group_name]

def load_node_group(spec: dict):

    if spec is None or not len(spec):
        return None

    name = spec['name']
    group = spec.get('group')

    if group is None and spec['source'] == 'node_groups':
        group = bpy.data.node_groups.get(name)

    if group is None and spec['source'] == 'built_in':
        group = load_builtin_node_group(spec['file_name'], spec['name'])

    return group

