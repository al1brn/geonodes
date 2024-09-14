#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:44:18 2024

@author: alain


File parser

This module implements a simple python parser which extract comments
form a source code file.

The parsing returns nested dicts where a dict contains information on the documented item

A base dict structure is:

- obj      : file, class, function, ...
- name     : python name
- comment  : the first multilines string after item declaration
- subs     : dict of dicts containing sub items

In addition to this structure, a dict can contain complementory values such as inheritance for
classes or arguments for functions
"""

import re
from pathlib import Path
from pprint import pprint

# For ref
regex_string1 = r'("[^"\\]*(?:\\.[^"\\]*)*")'
regex_string2 = r"('[^'\\]*(?:\\.[^'\\]*)*')"

regex_source  = r"`((``[^`]*``)|([^`\n]*))`"

regex_csource  = re.compile(regex_source,  flags=re.MULTILINE)


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

    Returns
    -------
    - str : the realigned comment
    """

    if comment is None:
        return None

    # Removes leading and ending triple quotes
    
    if not isinstance(comment, str):
        comment = str(comment)

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
        self.text   = text
        self.cursor = 0
        
    def __str__(self):
        return f"<Text[{self.cursor}]: {self.from_cursor[:15]}...>"

    @property
    def eof(self):
        """ End of text is reached

        Returns
        -------
        - bool : True if end of text is reached
        """
        return self.cursor >= len(self.text)

    @property
    def eol(self):
        """ End of line is reached

        Returns
        -------
        - bool : True if current char is eol (or if eof is True)
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
                self.cursor = len(self.text)
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
    
    # ====================================================================================================
    # Extract strings from a text
    
    @classmethod
    def extract_strings(cls, text):
        """ Extract strings from a text and returns the extracted text and the list of extracted strings.
        
        Arguments
        ---------
        - text (str) : the text to extract strings from
        
        Returns
        -------
        - str : text with strings replaced by 'index'
        - list of strs : list of extracted strings
        """

        strings = []
        stxt = cls(text)
        
        while not stxt.eof:
    
            quote = stxt.find(('"', "'"), halt=False)
            if quote is None:
                return stxt.text, strings
            
            a = stxt.cursor - 1
            b = None
            
            # ----------------------------------------------------------------------------------------------------
            # Multiline strings
            
            if stxt(3) == '"""':
                b = stxt.move_after('"""', halt=False)
                if b is None:
                    break

            # ----------------------------------------------------------------------------------------------------
            # Single line strings
            
            else:
                while not stxt.eof:
                    b = stxt.move_after(quote, halt=False)
                    if b is None:
                        break
                    
                    if stxt.cursor == a + 1  or stxt(-2, 1) != "\\":
                        break
                    
                if b is None:
                    return stxt.text, strings
                
            strings.append(stxt.replace(a, b, f"'{len(strings)}'"))
            
        return stxt.text, strings
    
    @staticmethod
    def replace_strings(text, strings):
        for index, string in enumerate(strings):
            text = text.replace(f"'{index}'", string)
        return text
    

# =============================================================================================================================
# Extract strings

def extract_strings(text):
    """ Replace string by an index.

    This pretreatment ensure that the content of strings won't interfer with
    regular expression

    Arguments
    ---------
    - text (str) : text to extract strings from

    Returns
    -------
    - str, list : cleaned text and list of extracted strings
    """
    return Text.extract_strings(text)

    # OLD OLD OLD
    
    def repl(m):
        index = f"'{len(strings)}'"
        strings.append(m.group(0))
        return index

    text = regex_cstrings.sub(repl, text)

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
    return Text.replace_strings(text, strings)



# =============================================================================================================================
# Extract strings

def extract_source(text):
    """ Replace source code block by an index.

    This pretreatment ensure that the content of sourcode won't interfer with
    regular expression

    Arguments
    ---------
    - text (str) : text to extract source code from

    Returns
    -------
    - str, list : cleaned text and list of extracted pieces of code
    """

    strings = []
    def repl(m):
        index = f"${len(strings)}<"
        strings.append(m.group(0))
        return index

    text = regex_csource.sub(repl, text)

    return text, strings


def replace_source(text, strings):
    """ Replace the extracted strings.

    Arguments
    ---------
    - text (str) : text with replaced pieces of code
    - strings : list of pieces of code

    Returns
    -------
    - Text with original strings
    """

    for index, s in enumerate(strings):
        text = text.replace(f"${index}<", s)

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

    source = Text(text + '\n\n')
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
        #'type'        : None,
        #'default'     : None,
        #'description' : None,
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
            items['description'] = replace_strings(text.from_cursor, strings)

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

def extract_lists(comment, *titles):
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
                if len(lines):
                    lines[-1] += ' ' + line.strip()
                else:
                    lines.append(line.strip())
                    
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
# Format list line

def format_list_line(d):
    s = "- "
    if d['name'] is None:
        return s + d['description']

    s += f"**{d['name']}**"
    
    if d['type'] is not None or d['default'] is not None:
        s += ' ('
        if d['type'] is None:
            s += f"{d['default']})"
        elif d['default'] is None:
            s += f"{d['type']})"
        else:
            s += f"_{d['type']}_ = {d['default']})"
            
    if d['description'] is not None:
        s += f" : {d['description']}"
        
    return s


# =============================================================================================================================
# Structures describing documented objects

def new_struct(obj, name, comment=None, subs=None, **kwargs):
    struct = {'obj' : obj, 'name': name, 'comment': comment, **kwargs}
    if subs is not None:
        struct['subs'] = subs
    return struct

def new_file(name, comment=None, subs=None):
    return new_struct('file', name, comment, subs={} if subs is None else subs)

def new_class(name, comment=None, subs=None, inherits=None):
    return new_struct('class', name, comment, subs={} if subs is None else subs, inherits=[] if inherits is None else inherits)

def new_function(name, comment=None, decorators=None, args=None, arguments=None, raises=None, returns=None):
    
    function = new_struct('function', name, comment)
    
    function['decorators'] = [] if decorators is None else decorators
    function['args']       = [] if args       is None else args
    function['arguments']  = [] if arguments  is None else arguments
    function['raises']     = [] if raises     is None else raises
    function['returns']    = [] if returns    is None else returns
    
    return function

def new_property(name, comment=None, type=None, default=None, setter=None, getter=None):
    prop = new_struct('property', name, comment, type=type, default=default)
    if getter is not None:
        prop['getter'] = getter
    if setter is not None:
        prop['setter'] = setter
    return prop


def struct_search(struct, **kwargs):
    
    ok = True
    for key, value in kwargs.items():
        if struct.get(key) != value:
            ok = False
            break
        
    if ok:
        return struct
    
    if struct.get('subs'):
        for sub in struct['subs'].values():
            stc = struct_search(sub, **kwargs)
            if stc is not None:
                return stc
            
    return None

def struct_iter(struct, f, *args, **kwargs):
    
    ok = True
    for key, value in kwargs.items():
        if struct.get(key) != value:
            ok = False
            break
        
    if ok:
        res = f(struct, *args)
        if res == True:
            return struct
        
    if struct.get('subs'):
        for sub in struct['subs'].values():
            stc = struct_iter(sub, f, *args, **kwargs)
            if stc is not None:
                return stc
            
    return None

def struct_list(struct, name_only=True, **kwargs):

    structs = []

    def add(stc):
        if name_only:
            structs.append(stc['name'])
        else:
            structs.append(stc)
            
    struct_iter(struct, add, **kwargs)
    
    return structs

# =============================================================================================================================
# Parse comment (for meta tage)

def parse_meta_comment(comment):
    """ Parse the comment itsel to extract meta tags
    
    Tags are `$` starting at the beginin of the line followed by a command line:
        
    - DOC START : extract comment from here
    - DOC END : don't extract after after
    - SET property value : property value pair
    """
    
    meta = r"^\$ *(?P<command>[\w]*) *(?P<param>.*)\n"
    
    props = {}
    
    index = 0
    while True:

        m = re.search(meta, comment[index:], flags=re.MULTILINE)

        if m is None:
            return comment, props
        
        command = m.group('command').upper()
        param   = m.group('param')
        if param is not None:
            param = param.strip()
        
        # ----------------------------------------------------------------------------------------------------
        # DOC command
        
        if command == 'DOC':
            if param is None or param == '' or param.upper() == 'START':
                comment = comment[index + m.span()[1]:]
                index = 0
                
            elif param.upper() == 'END':
                return comment[:index + m.span()[0]], props
            
            else:
                print(f"CAUTION: invalid meta command {m.group(1)}, DOC option must be in ('START','END') not '{param}'")
                index += m.span()[1]
                
        # ----------------------------------------------------------------------------------------------------
        # SET command
        
        elif command == 'SET':
            
            try:
                exec(param, None, props)
            except Exception as e:
                print(f"CAUTION: invalid meta command {m.group(1)}, impossible to exec instruction:\n> {param}'\n{str(e)}")
            
            comment = comment[:index + m.span()[0]] + comment[index + m.span()[1]:]
            index += m.span()[0]
                
    return comment, props

    

# =============================================================================================================================
# Parse python source code

def parse_file_source(text, file_name='File'):
    """ Parse a python file source

    The parser returns a dictionary giving the content of the file:

    - file
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

    file_subs= {}

    file = new_file(file_name, comments[0] if len(comments) else None, subs=file_subs)

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
        
        inherits = m.group(3)
        if inherits is not None:
            inherits = [s.strip() for s in m.group(3).split(',')]

        class_ = new_class(class_name, comment, inherits=inherits)

        # Add the properties declared in the comment

        props = lists.get('properties', [])
        for info in props:
            prop_name = info['name']
            class_['subs'][prop_name] = new_property(prop_name, info['description'], type=info['type'], default=info['default'])

        # ----- Put the class in the subs of the file

        file_subs[class_name] = class_


    # ----- Build the list of classes order by their appearance in the source file
    # This list will permit to know to whom further methods must be attached
    # 
    # Note that this list of positions in text doesn't include positions of functions
    # Hence, the following structure
    #
    # Class ClassName:
    #    def method
    #
    # def function_name:
    #     def sub_function
    #
    # Because of its indentation, sub_function will be interpreted as a method of ClassName
    # 
    # To solve that, this list will be updated with functions

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
        # Name

        name = m.group(6)

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
        # Argument string

        args = re.sub(r"  +", " ", m.group(8))
        args_list = args.split(',')
        if len(args_list) and args_list[0] in ('self', 'cls'):
            args = ','.join(args_list[1:]).strip()

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

        # Extract lists

        comment, lists = extract_lists(comment, ['raises', 'arguments', 'returns', 'properties'])

        # ----------------------------------------------------------------------------------------------------
        # Create the function dict

        function_ = new_function(name, comment, decorators=decorators, args=args)

        # Add the lists

        for title, items in lists.items():
            function_[title] = items

        # ----------------------------------------------------------------------------------------------------
        # Place the function at file level or in a class

        # ----- Indentation is null : this is function at file level

        if indent == 0:

            file_subs[name] = function_
            
            # update start positions to avoid a sub function to be interpreted as a previous class method
            
            starts = sorted(starts + [(m.span()[0], name)], key=lambda x: x[0])


        # ----- This is a class method

        else:

            # ----- Let's find the last class declared before the function

            func_start = m.span()[0]

            last_class_name = None
            for start, class_name in starts:
                if func_start < start:
                    break
                last_class_name = class_name
                
            if last_class_name is None:
                raise Exception(f"Sorry shouldn't append: wrong indentation for function '{name}'")

            class_ = file_subs[last_class_name]
            
            # it's a sub function: don't care
            if class_['obj'] != 'class':
                continue
            
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
                    if len(function_['returns']):
                        prop_['type'] = function_['returns'][0]['name']
                    if prop_['comment'] is None:
                        prop_['comment'] = function_['comment']
                        
            # ----- It is the __init__ method
            
            elif name == '__init__':
                if class_['comment'] is None:
                    class_['comment'] = function_['comment']
                    function_['comment'] = None
                    
                class_['args'] = function_.get('args')
                function_['args'] = None
                
                props = function_.get('properties', [])
                for info in props:
                    prop_name = info['name']
                    if class_['subs'].get(prop_name) is None:
                        class_['subs'][prop_name] = new_property(prop_name, info['description'], type=info['type'], default=info['default'])
                
                    
                class_['__init__'] = function_

            # ----- Otherwise we create a method

            else:
                class_subs[name] = function_
                
    # ----------------------------------------------------------------------------------------------------
    # Parse meta commands in comment
    
    def meta(struct):
        comment = struct['comment']
        if comment is None:
            return
        comment, props = parse_meta_comment(comment)
        
        struct['comment'] = comment
        for k, v in props:
            struct[k] = v
            
    struct_iter(file, meta)
    

    return file

# =============================================================================================================================
# Parse source files to build the reference documentation

def parse_files(folder, key="", verbose=False):
    """ Load files from a folder.

    All the files with `.py` extension are parsed.

    Arguments
    ---------
    - folder (str) : main folder
    - root (str=None) :

    Returns
    -------
    - dict
    """

    files = {}
    root_key = Path(key)

    for fpath in Path(folder).iterdir():
        if not fpath.match("*.py"):
            continue

        file_key = str(root_key / fpath.stem)
        if verbose:
            print(f"Loading {fpath.name} in file '{file_key}'")
            
        files[file_key] = parse_file_source(fpath.read_text(), fpath.stem)

    return files

# =============================================================================================================================
# Class : capture inheritance from another class

def capture_inheritance(class_, base_, remove=True):
    """ Capture properties et methods from another class
    
    Allow to document class items as it were not inherited.
    
    > [!Note]
    > if the name of the base class is in the inherits list, it is removed from it
    
    Arguments
    ---------
    - class_ (dict) : the class to enrich
    - base_ (dict) : the class to capture properties and methods from
    - remove (bool = True) : remove base name from inheritance list
    """
    
    for sub in base_['subs'].values():
        
        # Sub is overloaded or is __init__
        
        if sub['name'] in list(class_['subs'].keys()) + ['__init__']:
            continue

        # Let's capture it
        
        class_['subs'][sub['name']] = sub
        
    # Let's suppress the entrance in inherit
    
    if remove and class_.get('inherits') is not None:
        if base_['name'] in class_['inherits']:
            class_['inherits'].remove(base_['name'])
            
    return class_

def capture_inheritances(class_, files_, include=None, exclude=[], verbose=True):
    """ Capture inheritances
    
    Allow to document class items as it were not inherited.
    
    > [!Note]
    > if the name of the base class is in the inherits list, it is removed from it
    
    Arguments
    ---------
    - class_ (dict) : the class to enrich
    - files_ (dict) : the hierarchy containing base classes to capture from
    - include (list = None) : limit capture to the given list
    - exclude (list = []) : exclude classes in the given list
    """
    
    if class_.get('inherits') is None:
        return class_
    
    to_capture = class_['inherits'] if include is None else include
    captured = []
    
    for base_name in to_capture:
        
        if base_name in exclude:
            continue
        
        base_ = struct_search(files_, obj='class', name=base_name)
        if base_ is None:
            continue
        
        if verbose:
            print(f"Capture inheritance {class_['name']} <- {base_name}")
        
        capture_inheritance(class_, base_, remove=False)
        captured.append(base_name)
        
    for base_name in captured:
        if base_name in class_['inherits']:
            class_['inherits'].remove(base_name)
            
    return class_

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

    file = parse_file(text)

    #dump_dict(file)

    pprint(file['subs']['clean_python'])
    pprint(file['subs']['Text'])


def test_folder(folder=None, sub_folders=[]):
    if folder is None:
        folder = Path(__file__).parents[0]
        print(folder)
        
    d = parse_files(folder, sub_folders=sub_folders, verbose=True)
    pprint(d)
    
    




