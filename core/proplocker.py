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

module : proplocker
------------------
- PropLocker class

Root class which raises an error when trying to write unknwon attributes

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

from .scripterror import NodeError

class PropLocker:

    def _lock(self):
        self._locked = True

    def _unlock(self):
        self._locked = False

    def __setattr__(self, name, value):
        if (name not in self.__dict__) and (name not in dir(self)) and ('_locked' in self.__dict__) and self._locked:
            raise NodeError(f"Class '{type(self).__name__}' has no attribute named '{name}'", keyword=name)
        super().__setattr__(name, value)
