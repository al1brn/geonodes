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
            return None

    return bpy.data.fonts.load(path)
