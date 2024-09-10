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
    """ Move lines of a text leftwards.
    
    Comment read in source code can have a non nul left margin whcih is interprated in markdown.
    This method:
    - suppresses the margin of the first line
    - move leftwards the lines after in order that the leftmost line has no margin and 
      that the relative indentation remains the same
      
    The following text:
    |     Example of text
    |               This text is aligned
    |               with a margin:
    |               - because it is written as a multiline comment string
    |                 with indentation
    |               Text continues here
    
    Is realigned:
    | Example of text
    | This texte is aligned
    | with a margin:
    | - because it is written as a multiline comment string
    |   with indentation
    | Text continues here
    
    Arguments
    ---------
    - comment (str) : the comment
    
    Return
    ------
    - str : the realigned comment
    """
    
    if comment is None:
        return None
    
    # Removes leading and ending triple quotes
    
    if comment[:3] == '"""':
        comment = comment[3:-3]
    
    # ----------------------------------------------------------------------------------------------------
    # Split in lines and split the lines in couples (indent, stripped line)
    # Computes the minimum indentation excluding the first one
    
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

    # ----------------------------------------------------------------------------------------------------
    # Left shift the lines from the minimum indentation
    # in order that the left most line sticks to the margin
                
    if min_indent is None:
        return None
    else:
        return "\n".join([lines[0].strip()] + [" "*(indent - min_indent) + line for indent, line in indents])

# =============================================================================================================================
# A cursor on a text

class Source:
    def __init__(self, text):
        """ Implements a simple text reader.
        
        The Source class manages a cursor on a multilines string.
        It offers basic function to read around the cursor (backward and forwards).
        It also implements features to move to (or after) a target and
        to replace a text segment by replacement string.
        
        Properties
        ----------
        - cursor (int) : current position
        
        Arguments
        ---------
        - text (str) : the managed text
        """
        self.text   = text + '\n'
        self.cursor = 0
        
    @property
    def eof(self):
        """ End of text is reached
        
        Returns
        -------
        - boolean : True if end of text is reached
        """
        return self.cursor == len(self.text)
    
    @property
    def eol(self):
        """ End of line is reached
        
        Returns
        -------
        - boolean : True if current char is eol (or if eof is True)
        """
        if self.eof:
            return True
        else:
            return self.text[self.cursor] == '\n'
        
    @property
    def c(self):
        """ Current character
        
        Note that an error is raised if <!eof> is True.
        
        ``` python
        return self.text[self.cursor]
        ```
        
        Returns
        -------
        - str : the character at cursor
        """
        return self.text[self.cursor]
    
    def value(self, start=1, count=None):
        """ Read the string around the cursor
        
        One or two argumentscan be passed:
        - If only one argument is passed (**count** is None), it is used as the number of chars
          to read after the cursoor
        - If two arguments are passed, they are interpreted as the starting position to read
          from and the number of characters to read
          
         > [!NOTE]
         > The start position is relative to the cursor
         
         ``` python
         # Read 3 characters from the cursor
         a = source.value(3)
         
         # Read the character preceeding the cursor
         b = source.value(-1, 1)
         
         # Note that the two following lines return the same result
         c = source.value()
         c = source.c
         ```
         
         Arguments
         ---------
         - start (int) : number of characters to read from the cursor if count is None,
           position to start to read otherwise
         - count (int) : number of characters to read, 1 is read if None
         
         Returns
         -------
         - str : the read characters
         """
        
        if count is None:
            count = start
            start = 0
            
        s = self.cursor + start
            
        return self.text[s:][:count]
    
    def move(self, count=1):
        """ Move the cursor of the given offset
        
        Arguments
        ---------
        - count (int = 1) : cursor offset
        
        Returns
        -------
        - int : new cursor position
        """
        self.cursor = min(len(self.text), self.cursor + count)
        if self.eof:
            return None
        else:
            return self.cursor
        
    def move_to(self, target):
        """ Move the cursor until it reaches the given argument
        
        Note that an error is raised if the target is not found.
        
        Arguments
        ---------
        - target (str) : the string to reach
        
        Returns
        -------
        - int : the new cursor position
        """
        i = self.text[self.cursor + 1:].index(target)
        self.cursor = self.cursor + 1 + i
        return self.cursor
        
    def move_after(self, target):
        """ Move the cursor after the given argument
        
        Note that an error is raised if the target is not found.
        
        The function is equivalent to:
        
        ``` python
        source.move_to(target)
        return source.move(len(target))
        ```
        
        Arguments
        ---------
        - target (str) : the string to reach
        
        Returns
        -------
        - int : the new cursor position
        """
        self.move_to(target)
        return self.move(len(target))
        
    def replace(self, start, end, repl):
        """ Replace the text between two positions by a replacement string.
        
        After the operation, the cursor is placed after the replacement string.
        
        This method return the **replaced** string.
        
        > [!NOTE]
        > The **start** and **end** position are absolute positions, note relative
        > to the cursor
        
        Typical use is given here below:
    
        ```python
        line = "Line of text with a token <My Token>."
        
        source = Source(line)
        start = source.move_to('<')
        end = source.move_after('>')
        token = source.replace(start, end, "HERE WAS A TOKEN")
        
        print(source.text)
        # Line of text with a token HERE WAS A TOKEN.
        
        print(token)
        # <My Token>
        ```
        
        Arguments
        ---------
        - start (int) : start index of replaced part
        - end (int) : end index of replace part
        - repl (str) : the replacement string
        
        Returns
        -------
        - str : the replaced string
        """
        n = len(self.text)
        suppressed = self.text[start:end]
        self.text = self.text[:start] + repl + self.text[end:]
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
    """ Parse a python file source
    
    Extracton returns
    - classes:
      - inherictance
      - methods (see functions)
      - properties made of decorated methods
      - comment
    - functions:
      - decorators
      - arguments
      - comment
      
    The parsing is done with regular expressions.
    
    This process works only if strings and comments are removed.
    This is why the first step is to _clean_ the source file using <!clean_python>.
     
    Arguments
    ---------
    - text (str) : source code to parse
     
    Returns
    -------
    - dict : classes and functions
    """
    
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
            'methods'     : {},
            'properties'  : {},
            }
        
        starts.append((m.span()[0], class_name))
        
    starts = sorted(starts, key=lambda x: x[0])
    

    # ----------------------------------------------------------------------------------------------------
    # Look for functions definitions:
    #
    #     @decorator
    #     def NAME(...):
    #         <COMMENT index>
    
    func_expr = r"^(((\s*)@([\w\.]*)\s*\n)*)(\s*)def +(\w*)\s*(\((.*)\)\s*):\s*([\n\s])*(<COMMENT ([0-9]+)>)?"
    
    functions = {}
    for m in re.finditer(func_expr, clean, flags=re.MULTILINE):
        
        is_setter = False
        is_getter = False
        decorators= []
        for decorator in m.group(1).split('\n'):
            deco = decorator.strip()
            if deco == "":
                continue
            if deco.endswith('.setter'):
                deco = '@setter'
                is_setter = True
            if deco == '@property':
                is_getter = True
            decorators.append(deco)
            
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
                
            class_ = classes[last_class_name]
                
            if is_setter or is_getter:
                prop_ = class_['properties'].get(name)
                if prop_ is None:
                    prop_ = {'name': name, 'getter': None, 'setter': None}
                    class_['properties'][name] = prop_
                if is_setter:
                    prop_['setter'] = function_
                else:
                    prop_['getter'] = function_

            else:
                class_['methods'][name] = function_
                
            
                
                
                
            
            
    #pprint(classes)
    #pprint(functions)
    
    
    



fpath = "/Users/alain/Documents/blender/scripts/modules/geonodes/geonodes/textures.py"
fpath = "/Users/alain/Documents/blender/scripts/modules/geonodes/geonodes/geometryclass.py"

text = Path(fpath).read_text()


parse(text)


line = "Line of text with a token <My Token>."

source = Source(line)
start = source.move_to('<')
end = source.move_after('>')
token = source.replace(start, end, "HERE WAS A TOKEN")

print(source.text)
print(token)


  
    
    
    