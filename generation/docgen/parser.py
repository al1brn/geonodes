#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:44:18 2024

@author: alain


Module parser

This module implements a simple python parser which extract comments
form a source code file.

The parsing returns nested dicts where a dict contains information on the documented item

A base dict structure is:
    
- obj      : module, class, function, ...
- name     : python name
- comment  : the first multilines string after item declaration
- subs     : dict of dicts containing sub items

In addition to this structure, a dict can contain complementory values such as inheritance for
classes or arguments for functions
"""

import re
from pathlib import Path
from pprint import pprint

# =============================================================================================================================
# Align comment

def del_margin(comment):
    """ Move lines leftwards to suppress margin.
    
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
        return ("\n".join(lines)).strip()
    else:
        return "\n".join([lines[0].strip()] + [" "*(indent - min_indent) + line for indent, line in indents])

# =============================================================================================================================
# A cursor on a text

class Text:
    def __init__(self, text):
        """ Implements a simple text reader.
        
        The Text class manages a cursor on a multilines string.
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
    
    @property
    def from_cursor(self):
        """ Return the text from the cursor.
        
        Returns
        -------
        - str : text from the cursor
        """
        return self.text[self.cursor:]
    
    def __call__(self, start=1, count=None):
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
         a = text(3)
         
         # Read the character preceeding the cursor
         b = text(-1, 1)
         
         # Note that the two following lines return the same result
         c = text()
         c = text.c
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
    
    def move(self, offset=1):
        """ Move the cursor of the given offset
        
        Arguments
        ---------
        - offset (int = 1) : cursor offset
        
        Returns
        -------
        - int : new cursor position
        """
        self.cursor = min(len(self.text), self.cursor + offset)
        if self.eof:
            return None
        else:
            return self.cursor
        
    def find(self, target, regex=False, halt=True):
        """ Find a target into the text
        
        > [!IMPORTANT]
        > The search starts at the cursor
        
        The target can be a single string or a tuple of strings.
        The function return the target and the cursor is place just after
        the target
        
        An error is raised if the target is not found and **halt** is True.
        
        ``` python
        text = Text("Search for A B C")
        
        print(text.find("B"))
        # > B
        
        text.cursor = 0
        print(text.find(("A", "B", "C")))
        # > A
        
        print(Text("Find this number: 123!").find(r"\d+"))
        # > 123
        ```
        
        Arguments
        ---------
        - target (str or tuple of strs) : the string(s) to reach
        - regex (bool = False) : target is a regular expression or not
        - halt (bool = True) : raise an exception if not found
        
        Returns
        -------
        - int : the new cursor position
        """
        
        def to_regex(s):
            if regex:
                return s
            
            s_ = ""
            for c in s:
                if c in "\\^$.|?*()[]{}":
                    s_ += '\\'
                s_ += c

            return s_
        
        if isinstance(target, str):
            expr = to_regex(target)
        else:
            expr = "|".join([to_regex(s) for s in target])
            
        m = re.search(expr, self.text[self.cursor:])
        if m is None:
            if halt:
                raise Exception(f"Text.find error: target {target} not found from cursor {self.cursor} in> {self(20)}...")
            else:
                return None
        
        self.cursor += m.span()[1]
        
        return m.group(0)
        
    def move_to(self, target, regex=False, halt=True):
        """ Move the cursor until it reaches the given target.
        
        This function execute a <!find> on the target and places the
        cursor just before the target.
        
        ``` python
        found = self.find(target)
        return self.move(-len(found))
        ```
        
        ``` python
        text = Text("Just go HERE")
        
        text.move_to("HERE")
        print(text.from_cursor)
        # > HERE
        ```
        
        Arguments
        ---------
        - target (str or tuple of strs) : the string(s) to reach
        
        Returns
        -------
        - int : the new cursor position
        """
        
        found = self.find(target, regex=regex, halt=halt)
        if found is None:
            return None
        else:
            return self.move(-len(target))
        
    def move_after(self, target, regex=False, halt=True):
        """ Move the cursor until it reaches the given target.
        
        This function execute a <!find> on the target and places the
        cursor just before the target.
        
        ``` python
        self.find(target)
        return self.cursor
        ```
        
        ``` python
        text = Text("Go after TARGET: here")
        
        text.move_after("TARGET")
        print(text.from_cursor)
        # > : here
        ```
        
        Arguments
        ---------
        - target (str or tuple of strs) : the string(s) to reach
        
        Returns
        -------
        - int : the new cursor position
        """
        found = self.find(target, regex=regex, halt=halt)
        if found is None:
            return None
        else:
            return self.cursor
        
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
        
        text = Text(line)
        start = text.move_to('<')
        end = text.move_after('>')
        token = text.replace(start, end, "HERE WAS A TOKEN")
        
        print(text.text)
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
# Extract strings

def extract_strings(text):
    """ Replace string by an index.
    
    This pretreatment ensure that the content of strings could interfer with
    regular expression
    
    Arguments
    ---------
    - text (str) : text to extract strings from
    
    Returns
    -------
    - str, list : cleaned text and list of extracted strings
    """
    
    expr1 = r'("[^"\\]*(?:\\.[^"\\]*)*")'
    expr2 = r"('[^'\\]*(?:\\.[^'\\]*)*')"
    
    strings = []
    def repl(m):
        index = f"'{len(strings)}'"
        strings.append(m.group(0))
        return index
    
    text = re.sub(expr1, repl, text, flags=re.MULTILINE)
    text = re.sub(expr2, repl, text, flags=re.MULTILINE)
    
    return text, strings

def replace_strings(text, strings):
    """ Replace the extracted strings.
    
    Arguments
    ---------
    - text (str) : text with replaced strings
    - strings : list of strings
    
    Returns
    -------
    - Text with original strings
    """
    
    for index, s in enumerate(strings):
        text = text.replace(f"'{index}'", s)
        
    return text
    
    
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
    
    source = Text(text)
    comments = []
    strings  = []
    
    # ----------------------------------------------------------------------------------------------------
    # Extract the comments en strings
    
    context = 'SOURCE'
    while not source.eof:
        
        c = source.c
        
        if c == '#':
            source.replace(source.cursor, source.move_after('\n'), "")
            
        elif c == '"' and source(3) == '"""':
            index = f"<COMMENT {len(comments)}>"
            
            start = source.cursor
            source.move(3)
            comments.append(del_margin(source.replace(start, source.move_after('"""'), index)))
            
            
        elif c in ["'", '"']:
            raw = False
            if source.cursor > 0:
                raw = source(-1, 1) == 'r'
                
            a = source.cursor
            while True:
                source.move()
                assert(not source.eof)
                if source() == c:
                    b = source.move()
                    break
                    
                elif source() == "\\":
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
# Parse comment list line

def parse_list_line(line):
    """ Parse a list line in a comment
    
    syntax:
    - name (type = default) : description
    
    Default value could contain parenthesis as in `Vector = (1, 2, 3)`,
    the parsing is done by reading the line char per char to handle
    parenthesis nesting.
    
    ``` python
    line = "- text (str = None) : text to parse"
    pprint(parse_list_line(line))
    # > {'default': 'None',
    # > 'description': 'text to parse',
    # > 'name': 'text',
    # > 'obj' : 'str'}
    ```
    """
    
    if line is None:
        return None
    
    # ----------------------------------------------------------------------------------------------------
    # We need at least a name
    
    line, strings = extract_strings(line)
    
    text = Text(line.strip())
    name = text.find(r"\w+", regex=True, halt=False)
    if name is None:
        return None

    items = {
        'name'        : name,
        'type'        : None,
        'default'     : None,
        'description' : None,
        }
    
    # ----------------------------------------------------------------------------------------------------
    # Next possible sepa is ( or : 
    
    sepa = text.find(('(', ':'), halt=False)
    
    if sepa is None:
        items['description'] = replace_strings(text.from_cursor, strings)
        get_descr = False
        
    # ----------------------------------------------------------------------------------------------------
    # Open parenthesis : (type = default)
        
    elif sepa == '(':
        
        cursor   = text.cursor
        type_def = None
        
        level = 1        
        while True: # No fear
            sepa = text.find(('(', ')'), halt=False)

            if sepa is None:
                break
                
            elif sepa == '(':
                level += 1
                
            elif sepa == ')':
                level -= 1
                
            if level == 0:
                type_def = replace_strings(text.text[cursor:text.cursor-1], strings)
                break
            
        # ( and ) nesting is not consistent
        # We give the raw result in description
            
        if type_def is None:
            text.cursor = cursor - 1
            items['description'] = replace_string(text.from_cursor, strings)
            
        # We have the interior of ( ... ) in type def
        # syntax is: type = default
            
        else:
            m = re.search(r"([^=]+)(=(.*))", type_def.strip())
            if m is None:
                items['type']    = replace_strings(type_def.strip(), strings)
            else:
                items['type']    = replace_strings(m.group(1).strip(), strings)
                items['default'] = replace_strings(m.group(3).strip(), strings)
                
            # ----- we are still in a proper syntax
            
            sepa = text.find(':', halt=False)
        
    # ----------------------------------------------------------------------------------------------------
    # Open parenthesis : (type = default)
    
    if sepa == ':':
        items['description'] = replace_strings(text.from_cursor.strip(), strings)
        
    return items


# =============================================================================================================================
# Parse comment to extract information

def extract_lists(comment, titles):
    """ Extract lists from a comment.

    This parser extracts Properties, Arguments and Returns sections.
    The corresponding lines are removed to build the 'new_comment' text.

    The lists are generated from the structure

    Arguments
    ---------
    - comment (str) : the raw comment
    - titles (str or list of strs) : the titles of the lists to extract

    Returns
    -------
    - str, dict: comment without the lists, lists as dict
    """
    
    TITLES = {
        'property'   : 'properties',
        'properties' : 'properties',
        'argument'   : 'arguments',
        'arguments'  : 'arguments',
        'return'     : 'returns',
        'returns'    : 'returns',
        'raise'      : 'raises',
        'raises'     : 'raises',
        }

    if comment is None:
        return None, {}
    
    if isinstance(titles, str):
        titles = [titles]
    
    lists = {}
    
    # ----------------------------------------------------------------------------------------------------
    # Replacement function
    
    def repl(m):
        
        # ----- List title
        
        title = m.group(1).strip().lower()
        if not title in TITLES:
            return m.group(0)
        
        if not title in titles:
            return m.group(0)
        
        # ----- Merge the lines to have one single line per item
        
        lines = []
        for line in m.group(2).split('\n'):
            if line.strip() == '':
                continue
            if line[0] == ' ':
                lines[-1] += ' ' + line.strip()
            else:
                lines.append(line.strip())
                
        # ----- Parse the items
        
        lists[title] = [parse_list_line(line) for line in lines]
        
        # ----- Delete in the comment
        
        return ""
    
    # ----------------------------------------------------------------------------------------------------
    # Substitution in the comment
    
    list_expr = r"^(\w*) ?\n-+ ?\n(([^\w\n]+.*\n)*)"
    
    comment = re.sub(list_expr, repl, comment + '\n\n\n', flags=re.MULTILINE)
    
    return comment.strip(), lists


# =============================================================================================================================
# Structures describing documented objects

def new_struct(obj, name, comment=None, subs=None, **kwargs):
    struct = {'obj' : obj, 'name': name, 'comment': comment, **kwargs}
    if subs is not None:
        struct['subs'] = subs
    return struct

def new_module(name, comment=None, subs={}):
    return new_struct('module', name, comment, subs=subs)

def new_class(name, comment=None, subs={}, inherits=[]):
    return new_struct('class', name, comment, subs=subs, inherits=inherits)

def new_function(name, comment=None, decorators=[], args=None, arguments=[], raises={}, returns={}):
    return new_struct('function', name, comment, args=args, arguments=arguments, raises=raises, returns=returns)

def new_property(name, comment=None, type=None, default=None, setter=None, getter=None):
    return new_struct('property', name, comment, type=type, default=default, setter=setter, getter=getter)


# =============================================================================================================================
# Parse python source code

def parse(text):
    """ Parse a python file source
    
    The parser returns a dictionary giving the content of the module:
        
    - module
      - comment
      - subs : dict of classes and functions
    - class
      - name
      - comment
      - inherits (list)
      - subs : dict of properties and functions (methods)
    - function
      - name
      - comment
      - args (str)
      - decorators (list of strs)
      - raises: list of dicts for raises
      - arguments: list of dicts for arguments
      - returns: list of dicts for returns
    - property
      - name
      - comment
      - type
      - default
      - setter : function
      - getter : function
      
    The parsing is done with regular expressions.
    
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
    # Documentation result
    
    module_subs= {}
    
    module = new_module('Module', comments[0] if len(comments) else None, subs=module_subs)
    
    # ----------------------------------------------------------------------------------------------------
    # Look for class definitions:
    #
    # class CLASS_NAME (...):
    #     <COMMENT index>
    
    class_expr = r"^class\s*([\w]*)\s*(\(([^\)]*)\))*\s*:\s*([\n\s])*(<COMMENT ([0-9]+)>)?"
    
    starts = []
    for m in re.finditer(class_expr, clean, flags=re.MULTILINE):
        
        class_name = m.group(1)
        starts.append((m.span()[0], class_name))
        
        # ----- Comment 

        icomm = m.group(6)
        comment = None if icomm is None else comments[int(icomm)]
        
        # Extract properties from the comment
        
        comment, lists = extract_lists(comment, 'properties')
        
        # ----- Create the class
        
        class_ = new_class(class_name, comment, inherits=m.group(3))
        
        # Add the properties declared in the comment
        
        props = lists.get('properties', [])
        for info in props:
            prop_name = info['name']
            class_['subs'][prop_name] = new_property(prop_name, info['description'], type=info['type'], default=info['default'])
        
        # ----- Put the class in the subs of the module
        
        module_subs[class_name] = class_
        
        
    # ----- Build the list of classes order by their appearance in the source file
    # This list will permit to know to whom further methods must be attached
        
    starts = sorted(starts, key=lambda x: x[0])

    # ----------------------------------------------------------------------------------------------------
    # Look for functions definitions:
    #
    #     @decorator
    #     def NAME(...):
    #         <COMMENT index>
    
    func_expr = r"^(((\s*)@([\w\.]*)\s*\n)*)(\s*)def +(\w*)\s*(\((.*)\)\s*):\s*([\n\s])*(<COMMENT ([0-9]+)>)?"
    
    for m in re.finditer(func_expr, clean, flags=re.MULTILINE):
        
        # ----------------------------------------------------------------------------------------------------
        # Name and args
            
        name = m.group(6)
        args = re.sub(r"  +", " ", m.group(8))
        
        DEBUG = name == 'clean_python'
        
        # ----------------------------------------------------------------------------------------------------
        # Decorators
        
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
            
        # ----------------------------------------------------------------------------------------------------
        # Indentation
            
        if m.group(5) is None:
            indent = 0
        else:
            indent = len(m.group(5))

        # ----------------------------------------------------------------------------------------------------
        # Comment

        icomm = m.group(11)
        comment = None if icomm is None else comments[int(icomm)]
        
        if DEBUG:
            print('COMMENT', name)
            print('-'*50)
            print(comment)
            
        
        # Extract lists
        
        comment, lists = extract_lists(comment, ['raises', 'arguments', 'returns'])
        
        if DEBUG:
            print('EXTRACTED COMMENT', name)
            print('-'*50)
            print(comment)
        
        
        # ----------------------------------------------------------------------------------------------------
        # Create the function dict
        
        function_ = new_function(name, comment, decorators=decorators, args=args)
        
        # Add the lists
        
        for title, items in lists.items():
            function_[title] = items

        # ----------------------------------------------------------------------------------------------------
        # Place the function at module level or in a class
        
        # ----- Indentation is null : this is function at module level
        
        if indent == 0:

            module_subs[name] = function_
            
        # ----- This is a class method
            
        else:
            
            # ----- Let's find the last class declared before the function
            
            func_start = m.span()[0]
            
            last_class_name = None
            for start, class_name in starts:
                if func_start < start:
                    break
                last_class_name = class_name
                
            class_     = module_subs[last_class_name]
            class_subs = class_['subs']
            
            # ----- If the method is a getter or a getter we create a class property
                
            if is_setter or is_getter:
                prop_ = class_subs.get(name)
                if prop_ is None:
                    prop_ = new_property(name)
                    class_subs[name] = prop_
                    
                if is_setter:
                    prop_['setter'] = function_
                else:
                    prop_['getter'] = function_
                    
            # ----- Otherwise we create a method

            else:
                class_subs[name] = function_
                
    return module


# =============================================================================================================================
# Tests

# -----------------------------------------------------------------------------------------------------------------------------
# Dump the content of a dict

def dump_dict(d, indent=0):
    
    INCR = 4
    
    if len(d) == 0:
        return
    
    print(f"{' '*indent}{d['name']} ({d['obj' ]})")
    if d['comment'] is not None:
        print(f"{' '*indent}> {d['comment'][:20]}...")
    print()
    
    for sub, sub_ in d.get('subs', {}).items():
        dump_dict(sub_, indent + 1*INCR)
        
        
def test():
    text = Path(__file__).read_text()

    module = parse(text)
    
    #dump_dict(module)
    
    pprint(module['subs']['clean_python'])
    
test()

