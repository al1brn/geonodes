#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 07:20:36 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : documentation
----------------------
- dynamic nodes documentation
- static document builder

update : 2024/02/17
"""

from pprint import pprint
from pathlib import Path

# ====================================================================================================
# A link

class Link:
    def __init__(self, name, link=None):
        self.name      = name
        self.link      = link
        
    def text(self, target='TEXT'):
        if target == 'TEXT':
            return self.name
        
        elif target == 'MD':
            return f"[{self.name}]({self.link})"
        
# ====================================================================================================
# Left translated
#
# Translate to left an inline comment to be compatible with MarkDown
#

def left_translate(text):
    if text is None:
        return None
    
    lines = text.split('\n')
    n = 0
    for line in lines:
        if line.strip() != "":
            n = len(line) - len(line.lstrip())
            break
    return "\n".join([line[n:] for line in lines])
    
# ====================================================================================================
# Split a big line in several lines

def split_text(text, width, bullet=None, margin=0):

    if text is None:
        return None
    
    # ----- Split in lines
    
    lines = text.split("\n")
    if bullet is None:
        prefix0   = ""
        prefix    = ""
        rem_width = width
    else:
        prefix0   = bullet + " "
        prefix    = " "*len(prefix0)
        rem_width = width - len(prefix0)
        
    prefix0 = " "*margin + prefix0
    prefix  = " "*margin + prefix
        
    # ----- Loop on the lines
    
    text = ""
    for line in lines:
        while len(line):
            if len(line) > width:
                force = True
                for i in reversed(range(width)):
                    if line[i] == " ":
                        text += prefix0 + line[:i] + "\n"
                        line = line[i+1:]
                        force = False
                        break
                    
                if force:
                    text += prefix0 + line[:width]  + "\n"
                    line = line[width:]
            else:
                text += prefix0 + line[:width]  + "\n"
                line = ""
            
            prefix0 = prefix
            
    return text

# ====================================================================================================
# Bullets list

class Bullets:
    def __init__(self, doc, bullet="-", item_len=None, new_line=True):
        
        self.doc        = doc

        self._bullet    = bullet
        self.bullet     = bullet
        self.indent     = 3 if bullet == "1" else 2
        
        if isinstance(item_len, (list, tuple)):
            self.item_len = max([len(item) for item in item_len])
        else:
            self.item_len = item_len
        self.item_count = 0
        
        self.new_line   = new_line
        
    def add(self, text, description=None, new_line=False):
        
        self.item_count += 1
        
        # ---------------------------------------------------------------------------
        # MarkDown

        if self.doc.is_md:
            
            if self._bullet == "1":
                self.bullet = f"{1}."
            else:
                self.bullet = self._bullet
            
            s = text
            if description is not None:
                s = text + " : " + description
                
            self.doc.para(s, new_line=False)
                
        # ---------------------------------------------------------------------------
        # Text
                
        else:
            if self._bullet == "1":
                self.bullet = f"{self.item_count}."
            else:
                self.bullet = self._bullet
            
            s = text
            if description is not None:
                if self.item_len is not None:
                    s = f"{s:{self.item_len}s}"
                s += " : " + description
                    
            self.doc.para(s, new_line=False)
            
        if new_line:
            self.doc.new_line()
            
    def follow(self, text, new_line=False):
        with self.doc.bullets(bullet=None) as b:
            self.doc.para(text, new_line=new_line)
            
            
    def __enter__(self):
        
        self.doc.push_bullets(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
       
        self.doc.pop_bullets()

        if self.new_line:
            self.doc.new_line()
            
    # ----------------------------------------------------------------------------------------------------
    # Alphabetical list
    
    def alphabetical(self, items, max_list=10):
        
        if isinstance(items, (list, tuple)):
            items = {item: item for item in items}
        
        # ----- A short list
            
        if len(items) <= max_list:
            for key in sorted(items):
                self.add(items[key])
            return
        
        # ----- A long list
        
        initials = sorted(set([key[0].upper() for key in items]))
        for initial in initials:
            self.add(initial, " ".join([items[key] for key in items if key[0].upper() == initial]))
            
# ====================================================================================================
# Documentation builder

class Doc:
    def __init__(self, target='TEXT', width=100, margin=4, link_root=None):
        
        if target not in ['TEXT', 'MD']:
            raise AttributeError (f"Unknown doc target '{target}'")

        self.target    = target
        self.width     = width
        self.margin    = margin
        self.link_root = link_root
        
        self.clear()
        
    # ====================================================================================================
    # Clear
    
    def clear(self):
        self._text    = ""
        self._bullets = []
    
    # ====================================================================================================
    # Constructors
        
    @classmethod
    def Text(cls, width=100, margin=4):
        return cls(target='TEXT', width=width, margin=margin)
        
    @classmethod
    def MarkDown(cls, link_root="/docs", file_path=None):
        return cls(target='MD', link_root=link_root)
    
    @classmethod
    def Html(cls, link_root="/docs"):
        return cls(target='HTML', link_root=link_root)
    
    # ====================================================================================================
    # Doc type
    
    @property
    def is_text(self):
        return self.target == 'TEXT'
    
    @property
    def is_md(self):
        return self.target == 'MD'
    
    @property
    def is_html(self):
        return self.target == 'HTML'

    # ====================================================================================================
    # Links
        
    def url(self, name, url):
        
        if self.is_text or url is None:
            return name
        
        elif self.is_md:
            return f"[{name}]({url})"
    
    def title_link(self, name, title=None):
        if title is None:
            title = name
        return self.url(name, f"#{title.replace(' ', '-')}")
    
    def page_link(self, name, path=None, title=None):
        if path is None:
            path = name
        url = f"{self.link_root}/{path}.md"
        if title is not None:
            url += f"#{title.replace(' ', '-')}"
        return self.url(name, url)
    
    # ----------------------------------------------------------------------------------------------------
    # Bullets
        
    def bullets(self, bullet="-", item_len=None, new_line=True):
        return Bullets(self, bullet=bullet, item_len=item_len, new_line=new_line)
    
    def push_bullets(self, bullets):
        self._bullets.append(bullets)
        
    def pop_bullets(self):
        if not len(self._bullets):
            raise RuntimeError("Doc.pop_bullets error: pop called on empty list. problem in balance with push_bullets and pop_bullets.")
        self._bullets.pop()
        
    @property
    def bullet(self):
        if len(self._bullets):
            return self._bullets[-1].bullet
        else:
            return None
        
    @property
    def indent(self):
        return sum([bullets.indent for bullets in self._bullets[:-1]])
    
    # ====================================================================================================
    # Writing document
        
    # ----------------------------------------------------------------------------------------------------
    # New line
    
    def new_line(self):
        self._text += "\n"
    
    # ----------------------------------------------------------------------------------------------------
    # Header
    
    def header(self, text, level):
        
        if self.is_md:
            self._text += "#" * (level + 1) + " " + text + "\n\n"
            
        else:
            n = len(text)
            if level <= 2:
                self._text += text + "\n"
                if level == 0:
                    self._text += "="*self.width
                elif level == 1:
                    self._text += "="*n
                elif level == 2:
                    self._text += "-"*n
                self._text += "\n\n"
            else:
                self._text += "---"*(level-2) + " " + text + "\n\n"
        
    # ----------------------------------------------------------------------------------------------------
    # A paragraph
    
    def para(self, text, new_line=True):
        
        if text is None:
            return
        
        bullet = self.bullet
        indent = self.indent
        
        # ----- Markdown
        
        if self.is_md:
            if bullet is None:
                indent  = " "*indent
                indent0 = indent
            else:
                indent0 = " "*self.indent + bullet + " "
                indent = "\n" + " "*self.indent
                
            lines = text.split("\n")
            self._text += indent0 + indent.join(lines) + "\n"
            
        # ----- Text

        else:
            self._text += split_text(text, self.width - self.margin - indent, bullet=bullet, margin=self.margin + indent)
                
        if new_line:
            self._text += "\n"
    
    # ---------------------------------------------------------------------------
    # Separator
        
    def sepa(self, fill=None):
        if self.is_md:
            self._text += "\n-----\n\n"
        else:
            self._text += "\n" + '-'*self.width + "\n\n"

    # ---------------------------------------------------------------------------
    # Description

    def descr(self, text="", new_line=True):
        with self.bullets(bullet=">", new_line=new_line):
            self.para(text, new_line=False)
            
    # ---------------------------------------------------------------------------
    # Source code
    
    def source(self, text):
        
        source = text.strip().replace("\t", "    ")

        if self.is_md:
            
            self._text += "``` python\n" + source + "\n```\n"
        
        else:
            lines = text.split("\n")
            for i, line in enumerate(lines):
                self._text += f"{i+1:2d}. " + line + "\n"
            self._text += "\n\n"
           
    # ====================================================================================================
    # Links
    
    def done(self, file_name=None):
        if file_name is None:
            print(self._text)
            
        else:
            print("Doc: writing", file_name)
            with open(file_name, "w") as f:
                f.write(self._text)
                
        self.clear()

    # ====================================================================================================
    # Demo
    
    @staticmethod
    def demo(md=False):
        if md:
            doc = Doc.MarkDown()
        else:
            doc = Doc.Text(width=60, margin=4)

        doc.header(f"Doc demo, target {doc.target}", 0)
        doc.descr("This is a demo of class 'Doc' which allows to build document with a set a basic instructions.")
        
        doc.header("How to use", 1)
        doc.para("One initialized, the Doc offers a set of writing instructions:")
        with doc.bullets(item_len = len('new_line')) as b:
            b.add(doc.title_link('header', 'headers'), "Create a header at a certain level (starting from 0)")
            b.add(doc.title_link('para'), "Create a simple paragraph")
            b.add(doc.title_link('descr'), "Write text as description")
            b.add('new_line', "Write a new line")
            b.add('sepa', "Write an horizontal separator")
            b.add(doc.title_link('bullets', 'bullet points'), "List of bullet points")
            b.add('source', "Write source code")
            
        doc.header("Headers", 1)
        doc.para("Headers are created with `doc.header` method. The level start from 0 for the main top title", new_line=False)
        doc.para("This section uses the level 1 style. See below for upper levels:")
        doc.header("Level 2", 2)
        doc.header("Level 3", 3)
        doc.header("Level 4", 4)
        doc.source("doc.header(title, level=0)")
        
        
        doc.header("Para", 1)
        doc.para("Text is written with `doc.para` method.", new_line=False)
        doc.para("The paragraph uses the current 'bullets' context. see bullets")

        doc.source("doc.para(text, new_line=True)")    
        doc.header("Arguments:", 2)
        with doc.bullets(item_len=len('new_line (bool=True)')) as b:
            b.add('text (str)', "Text to write")
            b.add('new_line (bool=True)', "Add an additional new line at the end")
            
        doc.header("Descr", 1)
        doc.para("The 'doc.descr', method use the '>' bullet for the paragraphs.")
        
        doc.header("Bullet points", 1)
        doc.para("Bullet points allow to write list with bullet points or numbers:")
        with doc.bullets(item_len=10) as b:
            b.add("First item", "Item description")
            b.add("Second item", "Items of a list can simple text or a couple (item, description)")
            b.add("Not described item")
            b.add("With a sub list", "Lists can be nested")
            with doc.bullets(bullet="1", new_line=False) as b1:
                b1.add("Order item", "Example of an order list")
                b1.add("Other ordered items", "Which follows the same principe")
                b1.add("Not described item")
            b.add("Item", "Back to the main list", new_line=True)
            b.follow("Text can be added to a bullet point as a complementary paragraph to the current bullet.", new_line=False)
            
        doc.para("End of demo")
        doc.done()
                





