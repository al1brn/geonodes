#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:44:18 2024

@author: alain
"""

import re
from pathlib import Path
from pprint import pprint

# =============================================================================================================================
# Align comment

def realign_comment(comment):
    
    if comment is None:
        return None
    
    comment = comment[3:-3]
    
    lines = comment.split('\n')
    indents = []
    min_indent = None
    for line in lines[1:]:
        m = re.search(r"(\s*)(.*)", line)

        indent = 0 if m.group(1) is None else len(m.group(1))
        stripped = m.group(2)
        
        indents.append((indent, stripped))
        
        if stripped.strip() != "":
            if min_indent is None:
                min_indent = indent
            else:
                min_indent = min(indent, min_indent)
                
    if min_indent is None:
        return None
    else:
        return "\n".join([lines[0].strip()] + [" "*(indent - min_indent) + line for indent, line in indents])

# =============================================================================================================================
# A cursor on a text

class Source:
    def __init__(self, text):
        self.text   = text + '\n'
        self.cursor = 0
        
    @property
    def eof(self):
        return self.cursor == len(self.text)
    
    @property
    def eol(self):
        if self.eof:
            return True
        else:
            return self.text[self.cursor] == '\n'
        
    @property
    def c(self):
        return self.text[self.cursor]
    
    def value(self, start=1, count=None):
        
        if count is None:
            count = start
            start = 0
            
        s = self.cursor + start
            
        return self.text[s:][:count]
    
    def move(self, count=1):
        self.cursor = min(len(self.text), self.cursor + count)
        if self.eof:
            return None
        else:
            return self.cursor
        
    def move_to(self, target):
        i = self.text[self.cursor + 1:].find(target)
        self.cursor = self.cursor + 1 + i
        return self.cursor
        
    def move_after(self, target):
        self.move_to(target)
        self.move(len(target))
        return self.cursor
        
    def replace(self, start, stop, repl):
        n = len(self.text)
        suppressed = self.text[start:stop]
        self.text = self.text[:start] + repl + self.text[stop:]
        self.cursor = start + len(repl)
        return suppressed
    
# =============================================================================================================================
# Clean python source

def clean_python(text):
    """ Clean python source code
    
    - Replace the comments by an comment index
    - Replace the strings by an index
    - Remove the blank lines
    - Group multilines instructions between ( and ) 
    
    Comments and strings are store in lists.
    Comments are replaced by <COMMENT index> and strings by "index"
    
    Arguments
    ---------
    - text (str) : source code to clean
    
    Returns
    -------
    - str  : cleaned text
    - list : list of comments 
    - list : list of strings

    Parameters
    ----------
    text : TYPE
        DESCRIPTION.

    Returns
    -------
    text : TYPE
        DESCRIPTION.
    comments : TYPE
        DESCRIPTION.
    strings : TYPE
        DESCRIPTION.
    """
    
    source = Source(text)
    comments = []
    strings  = []
    
    # ----------------------------------------------------------------------------------------------------
    # Extract the comments en strings
    
    context = 'SOURCE'
    while not source.eof:
        
        c = source.c
        
        if c == '#':
            source.replace(source.cursor, source.move_after('\n'), "")
            
        elif c == '"' and source.value(3) == '"""':
            index = f"<COMMENT {len(comments)}>"
            comments.append(realign_comment(source.replace(source.cursor, source.move_after('"""'), index)))
            
        elif c in ["'", '"']:
            raw = False
            if source.cursor > 0:
                raw = source.value(-1, 1) == 'r'
                
            a = source.cursor
            while True:
                source.move()
                assert(not source.eof)
                if source.value() == c:
                    b = source.move()
                    break
                    
                elif source.value() == "\\":
                    if not raw:
                        source.move()

            index = f'"{len(strings)}"'
            strings.append(source.replace(a, b, index))
            
            
        else:
            source.move()
            
    # ----------------------------------------------------------------------------------------------------
    # Remove empty lines
    
    text = re.sub(r'^ *\n', "", source.text, flags=re.MULTILINE)
    
    # ----------------------------------------------------------------------------------------------------
    # Group \n within (...)
    
    group_expr = r"\(([^\)\(]*\n[^\)]*)*\)"
    text = re.sub(group_expr, lambda m: m.group(0).replace('\n', ' '), text, flags=re.MULTILINE)
            
    return text, comments, strings

# =============================================================================================================================
# Parse python source code

def parse(text):
    
    # ----------------------------------------------------------------------------------------------------
    # Clean to properly apply regex expressions
    
    clean, comments, strings = clean_python(text)
    
    # ----------------------------------------------------------------------------------------------------
    # Look for class definitions:
    #
    # class CLASS_NAME (...):
    #     <COMMENT index>
    
    class_expr = r"^class\s*([\w]*)\s*(\(([^\)]*)\))*\s*:\s*([\n\s])*(<COMMENT ([0-9]+)>)?"
    
    
    starts = []
    classes = {}
    for m in re.finditer(class_expr, clean, flags=re.MULTILINE):
        
        class_name = m.group(1)

        icomm = m.group(6)
        comment = None if icomm is None else comments[int(icomm)]

        
        classes[m.group(1)] = {
            'name'        : class_name,
            'inheritance' : m.group(3),
            'comment'     : comment,
            'functions'   : {},
            }
        
        starts.append((m.span()[0], class_name))
        
    starts = sorted(starts, key=lambda x: x[0])
    

    # ----------------------------------------------------------------------------------------------------
    # Look for functions definitions:
    #
    #     @decorator
    #     def NAME(...):
    #         <COMMENT index>
    
    func_expr = r"^(((\s*)@(\w*)\s*\n)*)(\s*)def +(\w*)\s*(\((.*)\)\s*):\s*([\n\s])*(<COMMENT ([0-9]+)>)?"
    
    functions = {}
    for m in re.finditer(func_expr, clean, flags=re.MULTILINE):
        
        if len(m.group(1)):
            decorators = [deco.strip() for deco in m.group(1).strip().split('\n')]
        else:
            decorators= []
            
        if m.group(5) is None:
            indent = 0
        else:
            indent = len(m.group(5))
            
        name = m.group(6)
        args = re.sub(r"  +", " ", m.group(8))

        icomm = m.group(11)
        comment = None if icomm is None else comments[int(icomm)]
        
        function_ = {
            'name'        : name,
            'decorators'  : decorators,
            'args'        : args,
            'comment'     : comment,
            }
        
        if indent == 0:
            functions[name] = function_
            
        else:
            func_start = m.span()[0]
            
            last_class_name = None
            for start, class_name in starts:
                if func_start < start:
                    break
                last_class_name = class_name
                
            classes[last_class_name]['functions'][name] = function_
            
        pprint(function_)
            
    #pprint(classes)
    #pprint(functions)
    
    
    



fpath = "/Users/alain/Documents/blender/scripts/modules/geonodes/geonodes/textures.py"
fpath = "/Users/alain/Documents/blender/scripts/modules/geonodes/geonodes/geometryclass.py"

text = Path(fpath).read_text()


parse(text)

  
    
    
    