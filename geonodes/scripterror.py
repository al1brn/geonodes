#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC hidden

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : scripterror
--------------------
- Node error error raising

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import inspect
from pathlib import Path
import bpy

EXCLUDE_GEONODES = False
FULL_PATH = False

class NodeError(Exception):

    def __init__(self, *messages, **kwargs):
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

        self.message += "\n" + "\n".join(self.stack_lines())

    def __str__(self):
        return self.message

    # ----------------------------------------------------------------------------------------------------
    # Loop on the stack

    @staticmethod
    def stack_lines():

        stack = ["Traceback (most recent call last):\n"]

        for i_frame, frame_info in enumerate(inspect.stack()[2:]):

            # ----- Generated source code

            if frame_info.filename == '<string>':
                continue

            path = Path(frame_info.filename)

            # ----- Exclude track from module

            if not EXCLUDE_GEONODES:
                if path.stem in ['utils', 'custom', 'sockets', 'treestack', 'tree']:
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
                    text_key = path.stem

            # ----- Read from blend text or from the file

            code_line0 = frame_info.lineno - 1
            code_line1 = frame_info.positions.end_lineno
            code_lines = []
            if blend_text:
                lines = bpy.data.texts[text_key].lines
                #code_lines = [f"{i}> {lines[i].body}" for i in range(code_line0, code_line1)]
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
                stack.append(f"File '{path}', line {frame_info.lineno}")
            else:
                stack.append(f"File '{path.name}', line {frame_info.lineno}")
            stack.extend(code_lines)
            stack.append("")

        return stack
