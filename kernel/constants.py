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

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : kernel/constants
-------------------------
- constants common to generation and api

updates
-------
- creation : 2026/11/14
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"

DATA_TYPE_HOMONYMS = {
    'INT8'          : 'INT',
    'INTEGER'       : 'INT',
    'FLOAT2'        : 'VECTOR',
    'FLOAT_VECTOR'  : 'VECTOR',
    'VECTOR_FLOAT'  : 'VECTOR',
    'TRANSFORM'     : 'MATRIX',
    'FLOAT4X4'      : 'MATRIX',
    'BYTE_COLOR'    : 'RGBA',
    'FLOAT_COLOR'   : 'RGBA',
    'COLOR'         : 'RGBA',
    'FLOAT'         : 'VALUE',
    'QUATERNION'    : 'ROTATION',
    'FLOAT4'        : 'VECTOR',
}

CLASS_NAMES = {
 'BOOLEAN'      : 'Boolean',
 'BUNDLE'       : 'Bundle',
 'CLOSURE'      : 'Closure',
 'COLLECTION'   : 'Collection',
 'CUSTOM'       : 'Input',
 'FONT'         : 'Font',
 'GEOMETRY'     : 'Geometry',
 'IMAGE'        : 'Image',
 'INT'          : 'Integer',
 #'INT_VECTOR'   : 'IntVector',
 'MATERIAL'     : 'Material',
 'MATRIX'       : 'Matrix',
 'MENU'         : 'Menu',
 'OBJECT'       : 'Object',
 'RGBA'         : 'Color',
 'ROTATION'     : 'Rotation',
 'SHADER'       : 'Shader',
 'SOUND'        : 'Sound',
 'STRING'       : 'String',
 'VALUE'        : 'Float',
 'VECTOR'       : 'Vector'
}


