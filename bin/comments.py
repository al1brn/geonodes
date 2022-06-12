#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:00:41 2022

@author: alain.bernard@loreal.com
"""

# ----------------------------------------------------------------------------------------------------
# Simple parser

class Parser:
    def __init__(self, text):
        self.text   = text
        self.cursor = 0
        
    def __str__(self):
        return self.text
    
    def __len__(self):
        return len(self.text)
    
    def __getitem__(self, index):
        return self.text[index]
        
    @property
    def eol(self):
        if self.eof:
            return True
        else:
            return self.text[self.cursor] == "\n"
        
    @property
    def eof(self):
        return self.cursor >= len(self.text)
    
    def back(self):
        self.cursor -= 1
        
    @property
    def read(self):
        if self.eof:
            return None
        self.cursor += 1
        return self.text[self.cursor-1]
    
    def equal(self, s):
        if self.eof:
            return False
        return self.text[self.cursor:self.cursor + len(s)] == s
    
    # ---------------------------------------------------------------------------
    # Parse the content by lines
    # The source itself is scanned to pass the strings
    # The multi string are returned as a whole
    
    def python_split(self):
        
        self.cursor = 0
        context = 'SOURCE'
        txt = ""
        while not parser.eof:
            
            
            c = parser.read
            
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
                    quote = c
                    
                elif c == '"':
                    if parser.equal('""'):
                        parser.cursor += 2
                        context = 'COMMENT'
                        if txt != "":
                            yield 'SOURCE', txt
                            txt = ""
                        c = None
                        
                    else:
                        context = 'STRING'
                        quote = c
                        
                elif c == "\n":
                    if txt != "":
                        yield 'SOURCE', txt
                        txt = ""
                    c = None
                    
            # ---------------------------------------------------------------------------
            # Comment multi lines: looking for """
                        
            elif context == 'COMMENT':
        
                if c == '"' and parser.equal('""'):
                    parser.cursor += 2
                    context = 'SOURCE'
                    if txt != "":
                        yield 'COMMENT', txt
                        txt = ""
                    c = None
                
            # ---------------------------------------------------------------------------
            # String context:
            # - Passing the \?
            # - Looking for quote
                        
            elif context == 'STRING':
                
                if c == '\\':
                    c += parser.read
                    
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


# ----------------------------------------------------------------------------------------------------
# Source code for a class

class SourceItem:
    
    def __init__(self, line_index, block):
        
        header = block[line_index]
        if header[:5] == 'class':
            self.name = 'class'
            
        elif header[:3] == 'def':
            self.name = 'def'
            
        else:
            raise RuntimeError(f"Unknown item header: {header}")
            
        self.header = header[len(self.name):].strip()
        
        # ---------------------------------------------------------------------------
        # If def, get the optional decorator
        
        line_bef = line_index
        if self.name == 'def':
            line = block[line_index-1]
            if line[0] == '@':
                self.decorator = line
                line_bef = line_index-1
            else:
                self.decorator = ""
        
        # ---------------------------------------------------------------------------
        # Before comments
        
        self.bef_comments = []
        for i in reversed(range(line_bef)):
            line = block[i]
            if line[0] == '#':
                self.bef_comments.insert(0, line)
            else:
                break
            
        # ---------------------------------------------------------------------------
        # After comments
        
        b = block[line_index+1]
        if isinstance(b, Block) and b.is_comment:
            self.aft_comment = b
            line_aft = line_index + 1
        else:
            self.aft_comment = ""
            line_aft = line_index

        # ---------------------------------------------------------------------------
        # If class, explore the methods
        
        if self.name == 'def':
            return
        
        self.methods = []
        
        sub = block[line_aft+1]
        if not isinstance(sub, Block):
            raise RuntimeError(f"No sub block after the class {header}. Found is:\n{sub}")
            
        for idx, line in enumerate(sub):
            if line[:4] == 'def ':
                self.methods.append(SourceItem(idx, sub))
        
        
    def __repr__(self):
        indent = "    " if self.name == "def" else ""
        s = indent + self.name + " --> " + self.header + "\n\n"
        for line in self.bef_comments:
            s += indent + "... " + line + "\n"
        s += "\n"
        s += indent + str(self.aft_comment) + "\n\n"
        
        if self.name == 'class':
            for meth in self.methods:
                s += repr(meth)
        return s
    
    @property
    def item_name(self):
        words = self.header.split('(')
        if len(words) == 1:
            name = self.header[:-1]
        else:
            name = words[0]
        return name
    
    @property
    def item_name_(self):
        s = ""
        for c in self.item_name:
            if c == '_':
                s += "\\_"
            else:
                s += c
        return s
    
    def mark_down(self, index_link=None, class_link=None):
        
        if self.name == 'class':
            header_pref = "#"
            yield f"\n# class {self.item_name_}\n"
            header_pref = "#"
            if index_link is not None:
                yield f"\n<sub>go to {index_link}</sub>\n"
            class_link = f"[{self.item_name_}](#class-{self.item_name_.lower()})"

        else:
            header_pref = "###"
            yield f"\n### {self.item_name_}\n"
            
            #if self.decorator == "@property":
            #    yield "<sub>Property</sub>"
            #elif self.decorator == "@staticmethod":
            #    yield "<sub>Static method</sub>"
            #elif self.decorator == "@classmethod":
            #    yield "<sub>Class method</sub>"
                
            link = ""
            if index_link is not None:
                link = index_link
            if class_link is not None:
                link += " " + class_link
            if link != "":
                yield f"\n<sub>go to {link}</sub>\n"
                
            yield "\n```python"
            if self.decorator != "":
                yield f"{self.decorator}"
            yield f"def {self.header}\n```\n"
                
            
            
        lines = []
        if self.aft_comment != "":
            lines = self.aft_comment[0].split("\n")
        elif self.bef_comments:
            for line in self.bef_comments:
                lines.append(line[2:])
                
        if lines:
            spaces_min = 100
            for i in range(1, len(lines)):
                indent, _ = Block.indent_line(lines[i])
                if indent is not None:
                    spaces_min = min(spaces_min, indent)
                
            _, lines[0] = Block.indent_line(lines[0])
            
            for i in range(1, len(lines)):
                indent, line = Block.indent_line(lines[i])
                if indent is None:
                    lines[i] = ""
                else:
                    lines[i] = " " * (indent - spaces_min) + line
                    
            # -------- Yield the lines
            
            def is_horz(line):
                _, l = Block.indent_line(line)
                if l == "":
                    return False
                
                if l[0] not in ['-', '*', '='] or len(l)<4:
                    return False
                
                return l == l[0] * len(l)
            
            def is_list(line):
                _, l = Block.indent_line(line)
                if l == "":
                    return False

                return l[0] == '-'
                
            
            cache = ""
            first = True
            for line in lines:
                if is_horz(line):
                    if cache != "" and cache[0] != '#':
                        yield header_pref + '# ' + cache
                        cache = ""
                
                elif is_list(line):
                    if cache != "":
                        yield cache
                        yield "\n"
                        cache = ""
                    yield line
                    first = False
                            
                else:
                    if first and line.strip()[0] != ">":
                        line = "> " + line
                    yield cache
                    cache = line
                    first = False
                
        if self.name == 'class':
            
            methods = {}
            for meth in self.methods:
                name = meth.item_name
                if name[:2] == '__' and name != '__init__':
                    continue
                methods[meth.item_name_] = meth
                
            if methods:
                
                keys = list(methods.keys())
                keys.sort()
                
                yield "\n## List of methods\n"
                
                for name in keys:
                    yield f"- [{name}](#{name.lower()})"

                yield "\n## Methods\n"
                    
                yield "\n"
                for name in keys:
                    meth = methods[name]
                    for l in meth.mark_down(index_link, class_link):
                        yield l
                yield "\n"


# ----------------------------------------------------------------------------------------------------
# A block is either a single line or a block of lines

class Block(list):
    
    # ----------------------------------------------------------------------------------------------------
    # Simple initialization within an owner and with the first line
    
    def __init__(self, owner=None, line=None, is_comment=False):
        super().__init__()
        self.owner = owner
        if line is not None:
            self.append(line)
        self.is_comment = is_comment

    # ----------------------------------------------------------------------------------------------------
    # Create a child from a first line
        
    def new_block(self, line=None, is_comment=False):
        block = Block(self, line=line, is_comment=is_comment)
        self.append(block)
        return block

    # ----------------------------------------------------------------------------------------------------
    # Block depth
        
    @property
    def depth(self):
        if self.owner is None:
            return 0
        else:
            return 1 + self.owner.depth

    # ----------------------------------------------------------------------------------------------------
    # Representation
        
    def __repr__(self):
        s = ""
        for b in self:
            if type(b) is str:
                s += "    " * self.depth + b + "\n"
            else:
                if b.is_comment:
                    s += "# ----- COMMENT\n"

                s += repr(b)

                if b.is_comment:
                    s += "# <<<\n"
                
        return s

    # ----------------------------------------------------------------------------------------------------
    # Utility: returns the indentation (spaces count) and the stripped line 
        
    @staticmethod
    def indent_line(line):
        count = 0
        for c in line:
            if c == " ":
                count += 1
            elif c == "\t":
                raise RuntimeError("HELP")

            elif c == "\n":
                return None, ""

            else:
                if line[-1] == "\n":
                    line = line[:-1]
                if count == 0:
                    return 0, line
                else:
                    return count, line.strip()

        return None, ""
    
    # ----------------------------------------------------------------------------------------------------
    # Read from a source file

    @classmethod
    def FromParser(cls, parser):
        
        stack   = [Block()]
        indents = [0]
        for context, raw_line in parser.python_split():
            
            if context == 'COMMENT':
                stack[-1].new_block(raw_line, is_comment=True)
                continue
            
            indent, line = Block.indent_line(raw_line)
            if indent is None:
                continue
            
            # Same indentation
            
            if indent == indents[-1]:
                stack[-1].append(line)
                
            # Deeper indentation
            
            elif indent > indents[-1]:
                
                stack.append(stack[-1].new_block(line))
                indents.append(indent)
                
            # Shallower indentation
            
            else:
                depth = None
                for i, idt in enumerate(indents):
                    if idt == indent:
                        depth = i
                        break
                    
                if depth is None:
                    raise RuntimeError(f"Unindent error at line:\n{raw_line}\nIndent is {indent}, but is not in {indents}.")
                    
                stack   = stack[:depth+1]
                indents = indents[:depth+1] 
                
                stack[-1].append(line)

        return stack[0]    
    
    # ----------------------------------------------------------------------------------------------------
    # Return the classes
    
    def read_classes(self):
        classes = []
        
        for line_index, line in enumerate(self):
            if line[:6] == 'class ':
                
                # ---------------------------------------------------------------------------
                # Create a class item
                
                cl = SourceItem(line_index, self)
                classes.append(cl)
                
        return classes
    
    
        

fname0 = "/Users/alain.bernard@loreal.com/Documents/private/test comment.py"
fname1 = "/Users/alain.bernard@loreal.com/Documents/private/blender/scripts/modules/geonodes/core/datasockets.py"
fname2 = "/Users/alain.bernard@loreal.com/Documents/private/blender/scripts/modules/geonodes/core/node.py"

fname  = fname2

print('='*50)    

with open(fname) as f:
    parser = Parser(f.read())


block = Block.FromParser(parser)

#print(block)

classes = block.read_classes()

fname = "/Users/alain.bernard@loreal.com/Documents/private/test.md"
with open(fname, 'w') as f:
    for cl in classes:
        for line in cl.mark_down():
            f.write(line + "\n")
            
            
    
    




    
    
