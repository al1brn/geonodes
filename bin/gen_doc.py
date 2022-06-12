#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:40:15 2022

@author: alain.bernard@loreal.com
"""

br = ("\n", "<br>")
    

def Link(text, link):
    return (text, f"[{text}]({link})")

def Bold(text):
    return (text, f"**{text}**")

def Italic(text):
    return (text, f"_{text}_")

def BoldItalic(text):
    return (text, f"***{text}***")

def Code(text):
    return (text, f"`{text}`")
            

# ====================================================================================================
# Text: manages formated text (bold, links...)
# yield unformetted version for inline comments

class Text:
    
    def __init__(self, *tokens):
        self.tokens = []
        self.add(*tokens)
        
    def __repr__(self):
        s = ">>>>> Text\n"
        for t in self.tokens:
            s += "    " + str(t) + "\n"
        return s + "<<<<<"
        
    def add(self, *tokens):
        for token in tokens:
            
            if type(token) is str:
                self.tokens.append((token, token))
            
            elif isinstance(token, (tuple, list)):
                if len(token) != 2:
                    raise RuntimeError(f"Invalid token {token}. Only str and couples are valid tokens")
                if type(token[0]) is not str:
                    raise RuntimeError(f"Invalid token index 0 '{token[0]}', type {type(token[0]).__name__}. Only str are valid types")
                if type(token[1]) is not str:
                    raise RuntimeError(f"Invalid token index 1 '{token[1]}', type {type(token[1]).__name__}. Only str are valid types")
                if token[0] == "" or token[1] == "":
                    raise RuntimeError(f"Token strings can't be empty:  '{token}'.")
                    
                    
                self.tokens.append(token)
            else:
                raise RuntimeError(f"Invalid token {token}. Only str and couples are valid tokens")
    
    def paragraphs(self, md=True):
        s   = ""
        sep = ""
        index = 1 if md else 0
        for token in self.tokens:
            
            #print("PARAGRAPHS.token", token)
            
            if token == br:
                if md:
                    s += '<br>'
                else:
                    yield s
                    s = ""
                sep = ""
                    
            else:
                try:
                    c = token[0][0]
                except Exception as e:
                    print(f"PARAGRAPHS, token= '{token}', token[0]: '{token[0]}', type: {type(token[0]).__name__}")
                    raise e
                
                if c not in ['.', ',']:
                    s += sep
                    
                s += token[index]
                sep = " "
                
        if s != "":
            yield s
        
        
    def gen_md(self):
        for line in self.paragraphs(True):
            yield line
        #yield "\n"
        
    def gen_text(self, width=100, first_indent=0):
        
        w = width - first_indent
        
        for text in self.paragraphs(False):
            
            lines = text.split("\n")
            
            for line in lines:
                words = line.split(' ')
                s = ""
                for word in words:
                    s += word
                    if len(s) > w:
                        yield s
                        s = ""
                        w = width
                    else:
                        s += " "
        
                if s != "":
                    yield s
                    
                w = width
            
            
# ====================================================================================================
# Documentation
#
# A doc is a list of documentations :-)

class Doc(list):
    
    def __init__(self, *tokens, depth=0):
        super().__init__()
        self.depth = depth
        self.text  = Text(*tokens)
    
    def gen_md(self):
        indent = "  " * self.depth
        for line in self.text.gen_md():
            yield indent + line
            
        for doc in self:
            for line in doc.gen_md():
                yield line
                
    def gen_text(self, width=100, first_indent=0):
        indent = "    " * self.depth
        first  = first_indent
        for line in self.text.gen_text(width, first_indent=first_indent):
            yield indent + line
            first = 0
        
        for doc in self:
            for line in doc.gen_text(width, first_indent=first):
                yield line
                
    def get_lists(self, create=True, **kwargs):
        
        lsts = []
        for item in self:
            if isinstance(item, List):
                lsts.append(item)
        
        if len(lsts) == 0 and create:
            lst = List(**kwargs)
            self.append(lst)
            return [lst]
        else:
            return lsts
                

class Section(Doc):
    
    def __init__(self, title, level=0):
        super().__init__()
        self.title = title
        self.level = level
        self.tag   = Section.title_tag(title)
        self.subsections = {}
        
    def get_subsection(self, title):
        tag = Section.title_tag(title)
        section = self.subsections.get(tag)
        if section is None:
            if title is None:
                title = tag
            section = Section(title, level=self.level + 1)
            self.subsections[tag] = section
        return section
    
    def add_subsection(self, section):
        delta = self.level - section.level + 1
        section.change_level(delta)
        self.subsections[Section.title_tag(section.title)] = section
        
    
    def change_level(self, delta):
        self.level += delta
        for section in self.subsections.values():
            section.change_level(delta)
    
    @staticmethod
    def title_tag(title):
        words = title.lower().split(' ')
        s = ""
        sep = ""
        for word in words:
            s += sep + word
            sep = "-"
        return s
    
    def gen_md(self):
        
        # ----- The secton title
        
        #if self.tag is None:
        #    stag = ""
        #else:
        #    stag = " {#" + self.tag + "}"
            
        yield f"\n{'#'*(self.level+1)} {self.title}\n"
        #yield f"\n{'#'*(self.level+1)} {self.title}{stag}\n"
        
        # ----- Proper content (description...)
        
        for line in super().gen_md():
            yield line
            
        # ----- Sub sections
        
        for section in self.subsections.values():
            for line in section.gen_md():
                yield line
            
        
    def gen_text(self, width=100, first_indent=0):
        
        if self.level > 0:
            indent = "    " * (self.level - 1)
        else:
            indent = ""
        
        # ----- The secton title
        
        
        if self.level > 0:
            yield "\n"
        yield indent + self.title
        
        if self.level == 0:
            yield "\n"
        else:
            c = '=' if self.level == 1 else '-'
            yield indent + c*len(self.title)
        
        # ----- Proper content (description...)
        
        for line in super().gen_text(width):
            yield indent + line

        # ----- Sub sections
        
        for section in self.subsections.values():
            for line in section.gen_text(width=width):
                yield line
                
    def gen_toc(self):

        link = Text.Link(self.title, self.tag)
        yield "  " * self.level + link[1]
        
        for section in self.subsections.values():
            for line in section.gen_toc():
                yield line
            
            
class Description(Doc):
    
    def gen_md(self):
        indent = "  " * self.depth + "> "
        for line in super().gen_md():
            yield indent + line
        yield "\n"
        
    def gen_text(self, width=100, first_indent=0):
        indent = "    " * self.depth + "| "
        for line in super().gen_text(width):
            yield indent + line


class Python(Doc):

    def gen_md(self):
        yield "\n```python"
        for line in super().gen_md():
            yield line
        yield "```\n"
        
    def gen_text(self, width=100, first_indent=0):
        indent = "    " 
        yield "\n"
        for line in super().gen_text(width):
            yield indent + line
        
class List(Doc):
    def __init__(self, *items, depth=0, ordered=False, align_char = None):
        super().__init__(depth=depth)
        self.ordered = ordered
        self.items = []
        self.add_item(*items)
        self.align_char = align_char
            
    def add_item(self, *items):
        for item in items:
            self.items.append(item)
            
    def gen_md(self):
        
        yield "\n"
        
        indent = "  " * self.depth
        for index, item in enumerate(self.items):
            prefix = indent + f"{index}. " if self.ordered  else "- "
            for line in item.gen_md():
                yield prefix + line
                prefix = indent + "  "
                
        yield "\n"
        
    def gen_text(self, width=100, first_indent=0):
        
        c = self.align_char
        c_loc = 0
        if c is not None:
            for index, item in enumerate(self.items):
                for line in item.gen_text():
                    c_loc = max(c_loc, line.find(c))
                    break
        
        indent = "    " * self.depth
        for index, item in enumerate(self.items):
            prefix = indent + f"{index}. " if self.ordered  else "- "
            first = True
            for line in item.gen_text(width):
                if first and c is not None:
                    p = line.find(c)
                    yield prefix + f"{line[:p]:{c_loc}s}{line[p:]}"
                    first = False
                else:
                    yield prefix + line
                prefix = indent + "  "
            
            
    
     
        
        
        
