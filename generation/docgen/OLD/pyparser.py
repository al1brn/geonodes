#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:00:41 2022

@author: alain.bernard@loreal.com
"""

import re
from pprint import pprint, pformat
from pathlib import Path
import inspect

# ====================================================================================================
# Utilities

def ok_comment(s):
    if s is None or s.split() == "":
        return False
    else:
        return True

# ====================================================================================================
# Normalize md text

def md_normalize(text):
    """ Normalize markdown text

    Merge the lines not separated by a blank line

    Arguments
    ---------
    - text (srt) : the mark down text to normalize

    Returns
    -------
    - str : normalized mark down text
    """

    if text is None:
        return ""

    # ----------------------------------------------------------------------------------------------------
    # Returns info on the current line:
    # - indentation
    # - bullet (a line ------) is a bullet !
    # - stripped line

    def line_info(line):

        if line.strip() == "":
            return 0, "", ""

        expr = r"(\s*)([^\w] |[0-9]*\. |[^\w]*)?\s*(.*)?"

        m = re.search(expr, line)

        indent   = 0  if m.group(1) is None else len(m.group(1))
        bullet   = "" if m.group(2) is None else m.group(2)
        stripped = "" if m.group(3) is None else m.group(3).strip()

        return indent, bullet, stripped

    # ----------------------------------------------------------------------------------------------------
    # Build the line infos

    base_indent = None
    line_infos = []
    for index, text_line in enumerate(text.split('\n')):
        indent, bullet, line = line_info(text_line)
        line_infos.append((indent, bullet, line, bullet == "" and line == ""))

        if index == 0:
            continue
        if bullet != "" or line != "":
            if base_indent is None:
                base_indent = indent
            else:
                base_indent = min(base_indent, indent)

    if base_indent is None:
        base_indent = 0

    # ----------------------------------------------------------------------------------------------------
    # Merge with proper indentation

    # List of lines with a first empty line which will be suppressed at the end
    lines = [""]
    prev_indent = 0
    in_source = False
    source_indent = 0

    for index, (indent, bullet, line, empty) in enumerate(line_infos):

        if empty:
            lines.append("")
            prev_indent = 0
        else:
            append = True

            # Comment / Source switch

            if bullet[:3] == "```":
                in_source = not in_source
                source_indent = indent

            # Regular line

            elif bullet == "":
                # Merge if current indent is greater equal than to the previous indent
                merge = indent in range(prev_indent, prev_indent + 4)

                # Merge if previous line is not blank
                merge = merge and lines[-1] != ""

                # Merge if previous line is not source code
                if index > 0:
                    merge = merge and line_infos[index-1][1][:1] != '`'

                if merge:
                    lines[-1] = lines[-1] + " " + line
                    append = False

            if append:
                lines.append(" "*max(indent - (source_indent if in_source else base_indent), 0) + bullet + line)
                if not in_source:
                    prev_indent = indent

    return "\n".join(lines[1:])

# ====================================================================================================
# Extract source code into a dictionary
# The dictionary can then used to replace the source code

def extract_source(comment):

    d = {}

    def extract(m):
        key = f"<s0urc3 {len(d)}>"
        d[key] = m.group(0)
        return key

    expr = r"```[^`]*```|`[\w ]*`"
    expr = r"```[^`]*```|`[^\n]*`"

    return re.sub(expr, extract, comment), d

def replace_source(comment, d):
    for key, source in d.items():
        comment = comment.replace(key, source)

    return comment


# ====================================================================================================
# Text reader

class Reader:
    def __init__(self, text):
        """ Simple python source code parser.

        Arguments
        ---------
        - text (str) : text to parse
        """
        self.text   = text
        self.cursor = 0

    @classmethod
    def FromFile(cls, fname):
        """ Initialize a parser from a file.

        Arguments
        ---------
        - fname (str) : full path of the file top parse
        """
        with open(fname) as f:
            return cls(f.read())

    def __str__(self):
        return self.text

    def __len__(self):
        return len(self.text)

    def __getitem__(self, index):
        return self.text[index]

    def reset(self):
        """ Reset the cursor to the start of the text
        """
        self.cursor = 0

    @property
    def eol(self):
        """ End of line flag

        Returns
        -------
            - Boolean : True if end of line is reached, False otherwise
        """
        if self.eof:
            return True
        else:
            return self.text[self.cursor] == "\n"

    @property
    def eof(self):
        """ End of file flag

        Returns
        -------
            - Boolean : True if end of file is reached, False otherwise
        """
        return self.cursor >= len(self.text)

    def back(self):
        """ Move the cursor one step backwards
        """
        self.cursor -= 1

    @property
    def read(self):
        """ Read the next char

        After reading, the cursor is incremented

        Returns
        -------
            - str : Next character or None if end of file
        """

        if self.eof:
            return None
        self.cursor += 1
        return self.text[self.cursor-1]

    @property
    def current(self):
        """ Read the current char

        Getting the current char doesn't move the cursor.

        Returns
        -------
            - str : Next character or None if end of file
        """

        if self.eof:
            return None
        else:
            return self.text[self.cursor]

    @property
    def previous(self):
        """ Read the previous char

        Returns
        -------
            - str : Previous character or None if start of file
        """
        if self.cursor == 0:
            return None
        else:
            return self.text[self.cursor-1]

    def equal(self, s):
        """ Compare the string starting at the cursor with the argument

        Arguments
        ---------
        - s (str) : the string to compare with

        Returns
        -------
        - Boolean : True if the text at the cursor is equal to the argument
        """
        if self.eof:
            return False
        return self.text[self.cursor:self.cursor + len(s)] == s

# ====================================================================================================
# Tokenizer

class Tokenizer(Reader):

    FIGURE = [chr(i) for i in range(ord('0'), ord('0')+10)]
    FIG0 = ['.', ] + FIGURE

    VAR0 = ['_'] + [chr(i) for i in range(ord('A'), ord('A')+26)] + [chr(i) for i in range(ord('a'), ord('a')+26)]
    VAR1 = VAR0 + FIGURE

    def token(self):

        # ----------------------------------------------------------------------------------------------------
        # Read the next not space char

        while True:
            c = self.read
            if c is None:
                return None
            elif c not in [' ', '\n', '\t']:
                break

        # ----------------------------------------------------------------------------------------------------
        # python name

        if c in Tokenizer.VAR0:
            var_name = c
            while True:
                if self.current in Tokenizer.VAR1:
                    var_name += self.read
                else:
                    break

            return 'NAME', var_name

        # ----------------------------------------------------------------------------------------------------
        # Numeric

        elif c in Tokenizer.FIG0:
            number = c
            ok_point = c != '.'
            ok_e = True

            while True:
                if self.current in Tokenizer.FIGURE:
                    number += self.read
                elif self.current == '.' and ok_point:
                    number += self.read
                    ok_point = False
                elif self.current in ['e', 'E'] and ok_e:
                    number += self.read
                    ok_e = False
                    if self.current in ['-', '+']:
                        number += self.read
                else:
                    break

            if number == '.':
                return 'OTHER', '.'
            else:
                return 'NUMBER', number

        # ----------------------------------------------------------------------------------------------------
        # String

        elif c in ["'", '"']:
            cstr = c
            s = ""
            while True:
                c = self.read
                if c == cstr:
                    if self.previous != "\\":
                        break
                    else:
                        s = s[:-1] + c
                else:
                    s += c

            return 'STRING', s

        # ----------------------------------------------------------------------------------------------------
        # List or tuple

        elif c in ['(', '[']:

            cend = ']' if c == '[' else ')'
            a = []
            item = []
            while True:
                token = self.token()
                assert(token is not None)

                if token[1] == cend:
                    if len(item):
                        a.append(item)
                    return c, a

                elif token[1] == ',':
                    a.append(list(item))
                    item = []

                else:
                    item.append(token)

                assert(len(a) < 50)
                assert(len(item) < 50)

        # ----------------------------------------------------------------------------------------------------
        # Dict

        elif c == '{':

            d = {}
            read_key = True
            while read_key:

                # ----- End of list

                token = self.token()
                if token[1] == '}':
                    break

                # ----- {**other} syntax

                if token[1] == '*':
                    token = self.token()
                    assert(token[1] == '*')
                    token = self.token()
                    assert(token[0] in ['NAME', '{'])
                    if d.get('**') is None:
                        d['**'] = [token]
                    else:
                        d['**'].append(token)
                    continue

                # ----- Key name

                assert(token[0] in ['STRING', 'NAME', 'NUMBER'])

                key = token[1]
                d[key] = []

                # ----- Separator

                token = self.token()
                assert(token[1] == ':')

                # ----- Value

                while True:
                    token = self.token()
                    if token[1] == '}':
                        read_key = False
                        break

                    elif token[1] == ',':
                        break

                    else:
                        d[key].append(token)

            return ('{', d)

        # ----------------------------------------------------------------------------------------------------
        # Other

        else:
            return 'OTHER', c

    def tokens(self):
        self.reset()

        tokens = []
        while True:
            token = self.token()
            if token is None:
                break
            tokens.append(token)
        return tokens

# ====================================================================================================
# Item Documentation

class Doc:
    def __init__(self, match):
        """ Item documentation

        This class stores the documentation of a functions or a class.
        In addition to the doc, it contains complementary information:
        - function:
          - args : call arguments
          - decorators : list of decorators
        - class:
          - bases : list of classes it inherits from
          - funcs : dict of method docs

        The class is initialized with the not null result of the regular expression:

        ``` match = re.search(r"(def|class)\s+(\w+)([^:]*)", line) ```

        which returns:
        1. def | class
        2. name
        3. args | base class

        Arguments
        ---------
        - match (re.search result) : see above
        """

        self.is_class     = match.group(1) == 'class'
        self.name         = match.group(2)
        self.bef_comment  = ""
        self.aft_comment  = ""

        if self.is_class:
            content_pat = r"\s*\((.*)\)"
            m = re.search(content_pat, match.group(3))
            if m is None:
                self.bases = []
            else:
                self.bases = m.group(1).split(',')
            self.funcs = {}

        else:
            self.class_doc  = None
            self.args       = match.group(3)
            self.decorators = []

    @property
    def comment(self):
        if self.aft_comment is None or self.aft_comment == "":
            return None
        else:
            return self.aft_comment

    @comment.setter
    def comment(self, value):
        self.aft_comment = value

    def __str__(self):
        if self.is_class:
            return f"<Doc class {self.name} {len(self.funcs)}, comment: {self.comment is not None}>"
        else:
            return f"<Doc method {self.name} {self.decorators}, comment: {self.comment is not None}>"

    # ----------------------------------------------------------------------------------------------------
    # Repr

    def __repr__(self):
        indent = "" if (self.is_class or self.class_doc is None) else "    "
        if self.comment is None:
            scomm = ""
        else:
            scomm = f"\n{indent}    | ".join([""] + self.comment.split("\n"))
        if self.is_class:
            sfuncs = "\n".join([repr(func) for func in self.funcs.values()])
            return f"{'='*100}\nclass {self.name}\n{scomm}\n{sfuncs}"
        else:
            if self.decorators:
                decs = f"\n{indent}".join([""] + self.decorators) + "\n"
            else:
                decs = ""
            return f"{indent}{'-'*80}\n{decs}{indent}def {self.name}{self.args}\n{scomm}\n"

    # ----------------------------------------------------------------------------------------------------
    # __str__

    def structure(self):
        indent = "" if (self.is_class or self.class_doc is None) else "    "
        #scomm = f"\n{indent}    | ".join([""] + self.comment.split("\n"))
        if self.is_class:
            sfuncs = "\n   - ".join([func for func in self.funcs.keys()])
            return f"{'='*100}\nclass {self.name}\n{sfuncs}"
        else:
            if self.decorators:
                decs = f"\n{indent}".join([""] + self.decorators) + "\n"
            else:
                decs = ""
            return f"{indent}{'-'*80}\n{decs}{indent}def {self.name}{self.args}\n"

# ====================================================================================================
# Simple python parser
#
# Parse the content by lines
# The source itself is scanned to pass the strings
# The multi string are returned as a whole

class Parser(Reader):

    def python_split(self):
        """ Split the python source file in parts

        The methods returns a couple.
        - The first item is the context in ('SOURCE', 'COMMENT', 'STRING')
        - The second item is the source code

        yield
        -----
        - tuple (str, str) : context, source code
        """

        self.cursor = 0
        context = 'SOURCE'
        txt     = ""
        while not self.eof:

            prev = self.previous
            c = self.read

            # ---------------------------------------------------------------------------
            # Source context : we can switch
            # - Comment #
            # - String '
            # - String "
            # - Comment multi lines """ ... """

            if context == 'SOURCE':

                if c == '#':
                    context = '#'

                elif c == "'":
                    context = 'STRING'
                    quote   = c
                    raw_str = prev == 'r'

                elif c == '"':
                    if self.equal('""'):
                        self.cursor += 2
                        context = 'COMMENT'
                        if txt != "":
                            # Return start of the line if different from spaces only
                            # otherwise keeps the spaces
                            if txt != " " * len(txt):
                                yield 'SOURCE', txt
                                txt = ""
                        c = None

                    else:
                        context = 'STRING'
                        quote = c
                        raw_str = prev == 'r'

                elif c == "\n":
                    yield 'SOURCE', txt
                    txt = ""
                    c = None

            # ---------------------------------------------------------------------------
            # Comment multi lines: looking for """

            elif context == 'COMMENT':

                if c == '"' and self.equal('""'):
                    self.cursor += 2
                    context = 'SOURCE'
                    yield 'COMMENT', txt
                    txt = ""
                    c = None

            # ---------------------------------------------------------------------------
            # String context:
            # - Passing the \?
            # - Looking for quote

            elif context == 'STRING':

                if not raw_str and (c == '\\'):
                    c += self.read

                elif c == quote:
                    context = 'SOURCE'

            # ---------------------------------------------------------------------------
            # Comment #: looking for eol

            elif context == '#':

                if c == "\n":
                    context = "SOURCE"
                    if txt != "":
                        yield 'SOURCE', txt
                        txt = ""
                    c = None

            # ---------------------------------------------------------------------------
            # Idiot proof

            else:
                raise RuntimeError(f"Unknown context {context}")

            # ---------------------------------------------------------------------------
            # Let's consume the char

            if c is not None:
                txt += c

        if txt != "":
            yield 'SOURCE', txt

    # ---------------------------------------------------------------------------
    # Return the source code in blocks of lines of the same type
    # - Source code
    # - Comment lines (starting by #)
    # - Comment (multi lines string)

    def to_packets(self):
        """ Split the source code into packets

        A packet is a triplet:
        - context : str in ('SOURCE', 'COMMENT')
        - indentation : int
        - code : the content

        Returns
        -------
        - (str, int, str) : context, indentation, source code
        """

        self.cursor = 0

        packets = []
        for context, raw_line in self.python_split():

            if raw_line.strip() == "":
                if packets:
                    packets[-1][2].append("")
                else:
                    packets = [('SOURCE', 0, [""])]
                continue

            # ----- Starting comment

            if context == 'SOURCE':

            # ----- Indentation and line from first non space char

                match  = re.search("(\s*)([^\s].*)", raw_line)
                indent = 0 if match.group(1) is None else len(match.group(1))
                line   = match.group(2)

                if line[0] == '#':
                    context = "COMMENT"
                    line = line[2:].strip()
                    if len(line) > 5 and line[0] in ['-', '=', '*']:
                        if line == line[0]*len(line):
                            line = ""

                lines = [line]

            # ----- Ensure the first line of a block comment is indented
            # Merge lines without blank lines without them

            elif context == 'COMMENT':

                lines = raw_line.split("\n")
                indent = 0

                # OLD ALGO replaced by md_normalized
                if False:
                    indent = 0
                    if lines:
                        indent = None
                        for i, line in enumerate(lines):
                            if line.strip() == "":
                                continue

                            match  = re.search("(\s*)([^\s].*)", line)
                            idt = 0 if match.group(1) is None else len(match.group(1))
                            if indent is None:
                                indent = idt
                            else:
                                indent = min(indent, idt)
                        if indent is None:
                            indent = 0

            # ----- Append the lines of new packet

            new = True
            if packets:
                if context == packets[-1][0] and indent == packets[-1][1]:
                    packets[-1][2].extend(lines)
                    new = False

            if new:
                packets.append((context, indent, lines))

        return packets

    # ---------------------------------------------------------------------------
    # Source code without comments

    def uncommented(self, indented=True):

        lines = []
        for packet in self.to_packets():
            if packet[0] == 'SOURCE':
                if indented:
                    lines.extend([" "*packet[1] + line for line in packet[2]])
                else:
                    lines.extend(packet[2])

        return "\n".join(lines)

    # ---------------------------------------------------------------------------
    # Return classes and functions from a python file

    def documentation(self):
        """ Retrieve the document of a python files

        Returns
        -------
        - list of Docs : A Doc instance for each function and class of the file
        """

        # ---------------------------------------------------------------------------
        # Works on types indented packets

        packets = self.to_packets()

        # ---------------------------------------------------------------------------
        # Let's loop on these packets

        docs = {}

        func_indent = 0
        read_index  = 0
        cur_class   = None

        while read_index < len(packets):

            packet = packets[read_index]
            packet_index = read_index
            read_index += 1

            # ----- Only source packets

            if packet[0] != 'SOURCE':
                continue

            # ----- Indentation is greater than the current function
            # we are within it

            indent = packet[1]
            if indent > func_indent:
                continue

            # ----- Normally, class of def header

            lines = packet[2]
            for line_index, line in enumerate(lines):

                match = re.search(r"^\W?(def|class)\s+(\w+)([^:]*)", line)
                if match is None:
                    continue

                # ----- Something found

                doc = Doc(match)

                # ----- Let's ignore inner classes

                if doc.is_class and indent != 0:
                    break

                # ----- Do we have a comment before ?

                if packet_index > 0:
                    bef = packets[packet_index-1]
                    if bef[0] == 'COMMENT' and bef[1] == indent:
                        doc.bef_comment = "\n".join(bef[2])

                # ----- Do we have a comment after ?

                if len(packets) > packet_index + 1:
                    aft = packets[packet_index + 1]
                    if packets[packet_index + 1][0] == 'COMMENT':
                        if aft[0] == 'COMMENT':
                            doc.aft_comment = "\n".join(aft[2])

                # ----- A new class

                if doc.is_class:
                    docs[doc.name] = doc

                    cur_class   = doc
                    func_indent = 99

                else:
                    prop_setter = False
                    for i in reversed(range(line_index)):
                        if lines[i] != "" and lines[i][0] == '@':
                            if lines[i][-6:] == 'setter':
                                prop_setter = True
                            doc.decorators.append(lines[i])

                    # Global function
                    if indent == 0:
                        docs[doc.name] = doc
                        cur_class   = None
                        func_indent = 0

                    # Class method
                    else:
                        doc.class_doc = cur_class
                        doc_name = doc.name
                        if prop_setter:
                            doc_name += ".setter"
                        cur_class.funcs[doc_name] = doc
                        func_indent = indent

                break

        return docs
