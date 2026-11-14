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

module : utils
--------------
- a set a utility functions

This module regroups all the global functions

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2026/11/14
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"

from .constants import DATA_TYPE_HOMONYMS, CLASS_NAMES


# ====================================================================================================
# Litteral to python name
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Replace accents and replace non kw chars by '_'
# ----------------------------------------------------------------------------------------------------

def only_kw_chars(s):

    accents = {'à': 'a', 'â': 'a', 'À': 'A', 'Â': 'A',
               'é': 'e', 'è': 'e', 'ê':'e', 'ë': 'e', 'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
               'î': 'i', 'Î': 'I',
               'ô': 'o', 'Ô': 'O',
               'û': 'u', 'ü': 'u', 'ù': 'u', 'Ù': 'U', 'Û': 'U', 'Ü': 'U'}

    valids = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"

    cleaned = ""
    last = ""
    for c in s:
        # Remove accents
        ch = accents.get(c, c)

        # Append if valid
        if ch in valids:
            cleaned += ch
            last = ch

        # Otherwise add a _ char, avoiding doing it twice
        elif last != '_':
            cleaned += '_'
            last = '_'

    # Remove '__' sequences

    for i in range(10):
        p = cleaned.find('__')
        if p < 0:
            break
        cleaned = cleaned.replace('__', '_')

    return cleaned

# ----------------------------------------------------------------------------------------------------
# Camel version of a string
# ----------------------------------------------------------------------------------------------------

def CamelCase(s):

    if s == "":
        return None

    title = ""
    for w in s.split(' '):
        if w in ['RGB', 'HSL', 'HSV', 'BSDF']:
            title += w
        else:
            title += w.title()


    cc = only_kw_chars(title)

    cc = cc.replace('_', '')
    if cc[0] in "0123456789":
        cc = "_" + cc

    return cc

# ----------------------------------------------------------------------------------------------------
# Snake case version of a string
# ----------------------------------------------------------------------------------------------------

def snake_case(s: str, test_keyword=True) -> str:

    import keyword

    if s == "":
        return ""

    sc = only_kw_chars(s.lower())

    if sc[0] in "0123456789":
        sc = '_' + sc

    if test_keyword and (sc in keyword.kwlist):
        sc += '_'

    return sc

# ====================================================================================================
# Get socket type from a type
# ====================================================================================================

def get_socket_type(socket_type: str) -> str:

    name = DATA_TYPE_HOMONYMS.get(socket_type, socket_type)
    if name not in CLASS_NAMES:
        raise AttributeError(f"Unknown socket type: {socket_type}")

    return name

# ====================================================================================================
# Get class name from a type
# ====================================================================================================

def get_class_name(socket_type: str) -> str:

    return CLASS_NAMES[get_socket_type(socket_type)]


