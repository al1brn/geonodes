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

module : scripterror
--------------------
- NodeError exception

NodeError has specific behaviors and features

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


import inspect
from pathlib import Path
import bpy

# No stack is displayed
NO_STACK = False

# If True, the errors coming from core files are omitted
IGNORE_CORE = True

# No stack is returned if keyword argument is not None
NO_STACK_ON_KEYWORD = True

# Return file full path
FULL_PATH = False

# ====================================================================================================
# Check if a file_name belongs to core module
# ====================================================================================================

def is_in_core(file_name):
    path = Path(file_name).resolve()
    package = Path(__file__).resolve().parents[2]
    return any(path.is_relative_to(package / name)
               for name in ('core', 'core_new', 'kernel'))

# ====================================================================================================
# Geonodes specific Exception
# ====================================================================================================

class NodeError(Exception):

    def __init__(self, *messages, keyword=None, **kwargs):

        self.message = "\n\nGeometry nodes error\n"

        if messages:
            self.message += '-'*100 + "\n"

            for msg in messages:
                if isinstance(msg, dict):
                    n = max([len(k) for k in msg.keys()])
                    for k, v in msg.items():
                        self.message += f"- {k:{n}s} : {v}\n"
                else:
                    self.message += f"{msg}\n"

        if kwargs:
            self.message += "\n"

            n = max([len(k) for k in kwargs.keys()])
            for k, v in kwargs.items():
                self.message += f"- {k:{n}s} : {v}\n"

        self.message += '-'*100 + "\n"

        self.message += "\n"

        # ----- stack

        stack_lines = self.stack_lines(IGNORE_CORE)

        if keyword is None:

            if NO_STACK:
                stack_lines = []

        else:
            item = self.find_keyword(keyword)

            if item is None:
                if NO_STACK or NO_STACK_ON_KEYWORD:
                    stack_lines = []

            else:
                file_name = item['file_name']
                lineno = item['lineno']
                stack_lines = [f"File '{file_name}', line {lineno}", item['code']]

        self.message += "\n".join(stack_lines)

    def __str__(self):
        return self.message

    # ----------------------------------------------------------------------------------------------------
    # Loop on the stack

    @staticmethod
    def get_stack(ignore_core: bool = True, limit=None):

        # List of dict:
        # - file_name
        # - lineno
        # - code

        stack = []
        insp_stack = inspect.stack()

        for frame_info in insp_stack:

            # ----- Generated source code

            if frame_info.filename == '<string>':
                continue

            path = Path(frame_info.filename)

            if path.resolve() == Path(__file__).resolve():
                continue

            if ignore_core and is_in_core(path):
                continue

            # ----- Python embedded in a blend file
            # "file.blend/text_name" or "/text_name"" if the file is not saved

            if len(frame_info.filename.split('/')) == 2:
                blend_text = True
                text_key   = frame_info.filename[1:]
            else:
                blend_file = path.parents[0]
                blend_text = blend_file.exists() and not blend_file.is_dir()
                if blend_text:
                    #text_key = path.stem
                    text_key = str(path).split('/')[-1]

            # ----- Read from blend text or from the file

            code_line0 = frame_info.lineno - 1
            code_line1 = frame_info.lineno
            code_lines = []
            if blend_text:
                lines = bpy.data.texts[text_key].lines
                code_lines = []
                for i in range(code_line0, code_line1):
                    try:
                        code_lines.append(f"{i + 1}> {lines[i].body}")
                    except:
                        pass
            else:
                try:
                    with open(frame_info.filename, 'r') as f:
                        lines = f.readlines()
                        code_lines = [f"{i+1}> {lines[i]}" for i in range(code_line0, code_line1)]
                        if True:
                            # lines are terminated by \n
                            code_lines = [("".join(code_lines))[:-1]]
                except:
                    code_lines = [f"Impossible to open '{frame_info.filename}'"]

            # ----- Track

            if FULL_PATH:
                file_name = str(path)
            else:
                file_name = str(path.name)

            stack.append({
                'file_name': file_name,
                'lineno'    : frame_info.lineno,
                'code'      : "\n".join(code_lines)

            })
            if limit is not None and len(stack) >= limit:
                break

        return stack

    # ----------------------------------------------------------------------------------------------------
    # Loop on the stack

    @staticmethod
    def stack_lines(ignore_core: bool = True):

        user_stack = NodeError.get_stack(ignore_core, limit=1)
        if not user_stack:
            return []

        item = user_stack[0]
        return [f"File '{item['file_name']}', line {item['lineno']}", item['code']]

    # ----------------------------------------------------------------------------------------------------
    # Search a keyword in the stack

    @staticmethod
    def find_keyword(keyword):

        if keyword is None:
            return None

        if isinstance(keyword, (tuple, list)):
            kws = keyword
        else:
            kws = [str(keyword)]

        for kw in kws:
            for item in NodeError.get_stack(IGNORE_CORE):
                if item['code'].find("raise") >= 0:
                    continue
                if item['code'].find(kw) >= 0:
                    return item

        return None
    
class NodeAttributeError(AttributeError):
    def __str__(self):
        ne = NodeError(super().__str__())
        return str(ne)
