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


from pprint import pprint
import inspect
from pathlib import Path
import bpy

FULL_PATH = False
NO_STACK_ON_KEYWORD = True
NO_STACK = True

class NodeError(Exception):

    def __init__(self, *messages, keyword=None, **kwargs):
        self.message = "Geometry nodes error\n"

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

        stack_lines = self.stack_lines()

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
    def get_stack():

        # List of dict:
        # - file_name
        # - lineno
        # - code

        stack = []

        for i_frame, frame_info in enumerate(inspect.stack()):

            # ----- Generated source code

            if frame_info.filename == '<string>':
                continue

            path = Path(frame_info.filename)

            # ----- Python embedded in a blend file
            # "file.blend/text_name" or "/text_name"" if the file is not saved

            if len(frame_info.filename.split('/')) == 2:
                blend_text = True
                text_key   = frame_info.filename[1:]
            else:
                blend_file = path.parents[0]
                blend_text = blend_file.exists() and not blend_file.is_dir()
                if blend_text:
                    text_key = path.stem

            # ----- Read from blend text or from the file

            code_line0 = frame_info.lineno - 1
            code_line1 = frame_info.positions.end_lineno
            code_lines = []
            if blend_text:
                lines = bpy.data.texts[text_key].lines
                code_lines = []
                for i in range(code_line0, code_line1):
                    try:
                        code_lines.append(f"{i}> {lines[i].body}")
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

        return stack

    # ----------------------------------------------------------------------------------------------------
    # Loop on the stack

    @staticmethod
    def stack_lines():

        stack = ["Traceback (most recent call last):\n"]

        for item in NodeError.get_stack()[2:]:
            file_name = item['file_name']
            lineno = item['lineno']
            stack.append(f"File '{file_name}', line {lineno}")
            stack.append(item['code'])
            stack.append("")

        return stack

    # ----------------------------------------------------------------------------------------------------
    # Search a keyword in the stack

    @staticmethod
    def find_keyword(keyword):

        if keyword is None:
            return None

        if isinstance(keyword, str):
            kws = [keyword]
        else:
            kws = keyword

        for kw in kws:
            for item in NodeError.get_stack()[2:]:
                if item['code'].find("raise") >= 0:
                    continue
                if item['code'].find(kw) >= 0:
                    return item

        return None
