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

module : sock_font
------------------
- Font socket

This class inherits from Socket and from generated.Font
which is automatically generated.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"

from . import generated

class Font(generated.Font):
    """ Font Socket.

    A font object can be refered to by using its name in bpy.data.fonts.
    """

    SOCKET_TYPE = 'FONT'

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, String, Font

        with GeoNodes("Font Test"):

            curves = String("Default Font").to_curves()
            curves += String("Input Font").to_curves(font=Font(None, "Font")).transform(translation=(0, 1.5, 0))
            curves += String("Arial Font (default if not found)").to_curves(font="Arial").transform(translation=(0, 3, 0))
            
            curves.out()






