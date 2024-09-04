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
# Text reader

class Reader:
    """ Implements a cursor onto a text
    """

    def __init__(self, text):
        self.text   = text
        self.cursor = 0

    @classmethod
    def FromFile(cls, fname):
        with open(fname) as f:
            return cls(f.read())

    def __str__(self):
        return self.text

    def __len__(self):
        return len(self.text)

    def __getitem__(self, index):
        return self.text[index]

    def reset(self):
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
        """ Move the cursort backwards
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
# Simple python parser

class Parser(Reader):

    # ---------------------------------------------------------------------------
    # Parse the content by lines
    # The source itself is scanned to pass the strings
    # The multi string are returned as a whole

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

            elif context == 'COMMENT':

                lines = raw_line.split("\n")
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

    def source_code_only(self, indented=True):

        lines = []
        for packet in self.to_packets():
            if packet[0] == 'SOURCE':
                if indented:
                    lines.extend([" "*packet[1] + line for line in packet[2]])
                else:
                    lines.extend(packet[2])

        if False:
            print('='*100)
            print(self.text)
            print('-'*100)
            print("\n".join(lines))
            print()

        return "\n".join(lines)



    # ---------------------------------------------------------------------------
    # Return classes and functions from a python file

    def documentation(self):

        # ---------------------------------------------------------------------------
        # Works on types indented packets

        packets = self.to_packets()

        # ---------------------------------------------------------------------------
        # Let's loop on these packets

        class Doc:
            def __init__(self, match):
                self.is_class = match.group(1) == 'class'
                self.name     = match.group(2)
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
                # Takes before comment or not
                if True:
                    return self.aft_comment
                else:
                    return self.bef_comment if self.aft_comment == "" else self.aft_comment

            @comment.setter
            def comment(self, value):
                self.aft_comment = value

            def __repr__(self):
                indent = "" if (self.is_class or self.class_doc is None) else "    "
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

                match = re.search(r"(def|class)\s+(\w+)([^:]*)", line)
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

                aft = packets[packet_index+1]
                if packets[packet_index+1][0] == 'COMMENT':
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

# ====================================================================================================
# Class documentation

SECTIONS = ['Properties', 'Class and static methods', 'Methods']

class ClassDoc:

    def __init__(self, class_name, is_class=True):
        self.name       = class_name
        self.is_class   = is_class

        self.init       = None
        self.comment    = ""

        self.inheritance = {section: set() for section in SECTIONS}
        self.sections    = {section: {} for section in SECTIONS}

    @property
    def props(self):
        return self.sections[SECTIONS[0]]

    @property
    def cs_methods(self):
        return self.sections[SECTIONS[1]]

    @property
    def methods(self):
        return self.sections[SECTIONS[2]]


    # ----------------------------------------------------------------------------------------------------
    # Rep

    def __repr__(self):
        s = f"class {self.name} (functions: {self.functions})\n"
        s += f"   - init       : {self.init is not None}\n"
        s += f"   - comment    : {self.comment[:15]}...\n"
        s += f"   - props      : {len(self.props)}\n"
        s += f"   - cs_methods : {len(self.cs_methods)}\n"
        s += f"   - methods    : {len(self.methods)}\n"
        return s

    # ----------------------------------------------------------------------------------------------------
    # Add the result of a python file parsing

    def add(self, cdoc):

        # ----- Check

        if self.is_class != cdoc.is_class:
            raise Exception(f"is_class incompatibility: ClassDoc={self.is_class}, cdoc: {cdoc.is_class}")

        if self.is_class:

        # ----- Class Comment

            if cdoc.comment != "":
                if self.comment != "":
                    self.comment += "\n\n"
                self.comment += cdoc.comment

            # ----- Methods

            for name, fdoc in cdoc.funcs.items():
                if name == '__init__':
                    self.init = {
                        'args':    fdoc.args,
                        'comment': fdoc.comment,
                        }
                    continue

                if not ok_comment(fdoc.comment):
                    continue

                is_prop   = False
                is_setter = False
                is_clmeth = False
                for d in fdoc.decorators:
                    if d in ['@classmethod', '@staticmethod']:
                        is_clmeth = True
                    if d == '@property':
                        is_prop = True
                    if d[-6:] == 'setter':
                        is_setter = True

                if is_prop or is_setter:
                    if is_prop:
                        self.props[name] = {'comment': fdoc.comment}

                    elif fdoc.comment != "":
                        fname = name[:-7]
                        if self.props[fname]['comment'] == "":
                            self.props[fname]['comment'] = {'comment': fdoc.comment}
                        else:
                            self.props[fname]['comment'] += "\n\nSetter\n\n" + fdoc.comment

                elif is_clmeth:
                    self.cs_methods[name] = {
                        'deco'   : fdoc.decorators,
                        'args'   : fdoc.args,
                        'comment': fdoc.comment,
                        }

                else:
                    self.methods[name] = {
                        'args'   : fdoc.args,
                        'comment': fdoc.comment,
                        }

        else:
            self.methods[cdoc.name] = {
                'args'    : cdoc.args,
                'comment' : cdoc.comment,
                }

    # ----------------------------------------------------------------------------------------------------
    # Get inheritance

    def get_inheritance(self):

        inheritance = {section: set(methods) for section, methods in self.inheritance.items()}

        for section in SECTIONS:
            methods = self.sections[section]
            if methods:
                inheritance[section].update({f"[{name}]({self.name}.md#{name})" for name in methods})

        return inheritance

    # ----------------------------------------------------------------------------------------------------
    # Add inheritance

    def add_inheritance(self, inheritance):
        for section in SECTIONS:
            self.inheritance[section].update(inheritance[section])

    # ----------------------------------------------------------------------------------------------------
    # Add inherited things

    def inherits_from(self, super_doc):

        if self.init is None and super_doc.init is not None:
            self.init = super_doc.init

        if self.comment == "":
            self.comment = super_doc.comment

        for section in SECTIONS:
            super_methods = super_doc.sections.get(section)
            methods       = self.sections.get(section)

            for name, super_meth in super_methods.items():
                if name not in methods:
                    methods[name] = super_meth

            # ----- Inheritance

            self.inheritance[section].update(super_doc.inheritance[section])

    # ----------------------------------------------------------------------------------------------------
    # Gen the markdown text

    def gen_markdown(self):

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Desindent utility

        def desindent(text, n):
            lines = text.split("\n")
            ok_args    = False
            ok_returns = False

            for i in range(len(lines)):

                line = lines[i]

                # ----- Desindent

                left = line[:n*4]
                if left.strip() == "":
                    lines[i] = line[n*4:]

                # ----- Args formatting

                line = lines[i]

                if line == "":
                    ok_args    = False
                    ok_returns = False

                else:
                    if ok_args or ok_returns:
                        if line[0] == " ":
                            line = line.strip()
                            if line == "":
                                ok_args    = False
                                ok_returns = False
                            else:
                                if line[0] != '-':
                                    line = "- " + line
                            if ok_args or ok_returns:
                                lines[i] = line

                    else:
                        if line.strip().lower()[:3] == 'arg':
                            lines[i] = "#### Args:"
                            ok_args    = True
                            ok_returns = False

                        elif line.strip().lower()[:6] == 'return' and len(line.strip()) < 10:
                            lines[i] = "#### Returns:"
                            ok_args    = False
                            ok_returns = True

            return "\n".join(lines)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if self.is_class:
            yield f"# Class {self.name}\n\n"
            top_anchor = f"#class-{self.name}"
        else:
            yield f"# Global functions\n\n"
            top_anchor = "#global-functions"

        yield "> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)\n\n"

        # ----------------------------------------------------------------------------------------------------
        # Global comment

        n_indent = 2 if self.is_class else 1

        # ----- Comment

        if ok_comment(self.comment):
            yield desindent(self.comment, n_indent - 1) + "\n\n"

        # Completed by init

        if self.init is not None:
            yield "### Constructor\n\n"

            yield f"```python\n{self.name}{self.init['args']}\n```\n\n"

            if ok_comment(self.init['comment']):
                yield desindent(self.init['comment'], n_indent) + "\n\n"

        # ----- TOC

        yield "## Content\n\n"

        for section in SECTIONS:
            methods = self.sections[section]
            inhs    = self.inheritance[section]

            if methods or inhs:

                if self.is_class:
                    yield f"**{section}**\n\n"

                if methods:
                    lines = [f"[{mname}](#{mname})" for mname in sorted(methods)]
                    yield " | ".join(lines)
                    del lines
                    yield "\n\n"

                if inhs:
                    yield "***Inherited***\n\n"
                    yield " | ".join(sorted(inhs))
                    yield "\n\n"

        # ----------------------------------------------------------------------------------------------------
        # Sections

        for section in SECTIONS:

            methods = self.sections[section]

            if methods:
                if self.is_class:
                    yield f"## {section}\n\n"

                for mname in sorted(methods):
                    meth = methods[mname]
                    yield f"### {mname}\n\n"

                    deco = meth.get('deco')
                    if deco:
                        sdeco = "\n".join(deco) + "\n"
                    else:
                        sdeco = ""

                    if meth.get('args'):
                        yield f"```python\n{sdeco}def {mname}{meth['args']}\n```\n\n"

                    if ok_comment(meth.get('comment')):
                        yield desindent(meth['comment'], n_indent) + "\n\n"

                    # ----- Bottom menu

                    yield f"<sub>Go to [top]({top_anchor}) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>\n\n"


# ====================================================================================================
# A module

class Module:
    """ Module class comment
    """

    def __init__(self, file_name, documented_classes=None):
        """ My own comment

        Arguments
        ---------
        - filename (str) : path of the module file
        - documented_classes (dict) : classes already documented

        """
        self.name      = file_name.split("/")[-1].split(".")[0]
        self.file_name = file_name

        self.parsed     = Parser.FromFile(file_name).documentation()
        self.class_docs = {}
        self.functions  = ClassDoc('functions', is_class=False)

        for class_name, cdoc in self.parsed.items():
            if cdoc.is_class:
                class_doc = ClassDoc(class_name)
                class_doc.add(cdoc)
                self.class_docs[class_name] = class_doc

            else:
                self.functions.add(cdoc)

        self.documented_classes = []
        if documented_classes is not None:
            if documented_classes == 'ALL':
                self.documented_classes = list(self.class_docs.keys())
            else:
                self.documented_classes = documented_classes

    def __repr__(self):
        return f"module {self.name}\n{pformat(self.class_docs)}\n"

    # ---------------------------------------------------------------------------
    # Inherits: add properties and methods from other classes

    def inherits(self, classes, super_classes=None, super_module=None):

        module = self if super_module is None else super_module

        if not isinstance(classes, list):
            classes = [classes]

        if super_classes is None:
            super_classes = classes
        elif not isinstance(super_classes, list):

            super_classes = [super_classes] * len(classes)

        for class_spec, super_spec in zip(classes, super_classes):
            self.class_docs[class_spec].inherits_from(module.class_docs[super_spec])

    # ---------------------------------------------------------------------------
    # Add references to inherited properties and methods

    def add_inheritance(self, classes, super_classes=None, super_module=None):

        module = self if super_module is None else super_module

        if not isinstance(classes, list):
            classes = [classes]

        if super_classes is None:
            super_classes = classes

        elif not isinstance(super_classes, list):
            super_classes = [super_classes] * len(classes)

        for class_spec, super_spec in zip(classes, super_classes):
            self.class_docs[class_spec].add_inheritance(module.class_docs[super_spec].get_inheritance())


    def markdown(self, class_name):
        return [line for line in self.class_docs[class_name].gen_markdown()]


def debug():
    text = """

#def test(test, other):
#    return test

class Foo1:
    # Foo comment 1
    # Foo comment 2

    def __init__(self, name=""):
        yeee !

    @classmethod
    def bar():
        # bar comment 1
        # bar comment 2

        bar code

    def baz():
        # baz comment 1
        # baz comment 2

        bar code

    @property
    def prop(self):
        ret toto

    @prop.setter
    def prop(self, value):
        toto


class Foo2:
    # Foo comment 1
    # Foo comment 2

    def bar():
        # bar comment 1
        # bar comment 2

        bar code

    def baz():
        # baz comment 1
        # baz comment 2

        bar code
"""


    doc = Parser(text).documentation()


    for class_name, cdoc in doc.items():
        class_doc = ClassDoc(class_name)
        class_doc.add(cdoc)
        for line in class_doc.gen_markdown():
            print(line)



    #for class_name, cdoc in doc.items():
    #    for name, fdoc in cdoc.funcs.items():
    #        print(class_name, name, fdoc.decorat)
    #        print()

#debug()

# /Users/alain/Documents/blender/scripts/modules/geonodes/script

if False:

    fpath = "/Users/alain/Documents/blender/scripts/modules/geonodes/"

    file_name = fpath + "core/datasockets.py"



    print("="*100)

    doc = Parser.FromFile(file_name).documentation()
    for class_name, cdoc in doc.items():
        class_doc = ClassDoc(class_name)
        class_doc.add(cdoc)

        for line in class_doc.gen_markdown():
            print(line)

        #break

    #print(doc)

if False:
    for member in inspect.getmembers(Module):

        print(">>>>>", member[0])

        obj = member[1]
        try:
            #code = inspect.getsourcelines(obj)
            #code = inspect.getsource(obj)
            #code = inspect.getcomments(obj)
            code = inspect.getdoc(obj)
            pprint(code)
            print
        except TypeError as e:
            pass

    print(inspect.getcomments(Module))



    import sys
    mod = sys.modules[__name__]
    print(mod)


    def test():
        #pprint(globals())
        for a in dir(mod):
            print(str(a), inspect.isclass(getattr(mod, a)))
# test()
