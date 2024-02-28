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
# Doc specification

class DocSpec:
    def __init__(self, target='TEXT', width=100, margin=4, path=None):
        self.target = target
        self.width  = width
        self.margin = margin
        self.path   = path
        if self.is_md:
            self.margin = 0
        
    @property
    def is_md(self):
        return self.target == 'MD'

# ====================================================================================================
# Split a big line in several lines

def split_line(line, width, indent=0, bullet=None):

    if line is None or line == "":
        return [""]
    
    # ----- Several lines
    
    sev_lines = line.split("\n")
    if len(sev_lines) > 1:
        lines = split_line(sev_lines[0], width, indent=indent, bullet=bullet)
        if bullet is not None:
            indent += 1
        for l in sev_lines[1:]:
            lines.extend(split_line(l, width, indent=indent, bullet=None))
        return lines
    
    # ----- Ok : only one line
    
    if bullet is not None:
        indent += 1
    
    prefix = "  "*indent
    width -= 2*indent
    
    cur_prefix = prefix
    if bullet is not None:
        cur_prefix = "  "*(indent - 1) + bullet + " "
    
    lines = []
    while len(line) > width:
        force = True
        for i in reversed(range(width)):
            if line[i] == " ":
                lines.append(cur_prefix + line[:i])
                line = line[i+1:]
                force = False
                break
        if force:
            lines.append(cur_prefix + line[:width])
            line = line[width:]
        cur_prefix = prefix
            
    if line != "":
        lines.append(cur_prefix + line)
        
    return lines

# ====================================================================================================
# Sort a dictionnary from a field

def sort_dict(dct, field, none_key=None):
    
    s_dct = {}
    for key, item in dct.items():
        value = item.get(field)
        if value is None:
            if none_key is None:
                raise Exception("Impossible to sort the dictionaty on field '{field}': entry '{key}' has no such field.")
            value = none_key
            
        if value in s_dct:
            s_dct[value][key] = item
        else:
            s_dct[value] = {key: item}
            
    return s_dct

# ====================================================================================================
# Doc items

# ----------------------------------------------------------------------------------------------------
# Base text

class DocText:
    
    text_type = 'TEXT'
    
    def __init__(self, text="", level=0, use_margin=True):
        self.text       = text
        self.level      = level
        self.use_margin = use_margin
        
    def __str__(self):
        return f"<DocText {self.level}, {self.text[:20]}>"
    
    def lines(self, doc_spec):
        
        if self.text is None:
            return [""]
        
        elif doc_spec.target == 'MD':
            return ['  '*self.level + self.text]
        
        else:
            return split_line(self.text, doc_spec.width, indent=self.level)
        
# ----------------------------------------------------------------------------------------------------
# Paragraph

class Paragraph(DocText):
    def __init__(self, text="", level=0, bullet=None, item=None):
        super().__init__(text, level=level)
        
        self.bullet   = bullet
        self.item     = item
        self.item_len = 1
        
    def __str__(self):
        return f"<Paragraph {self.level}, {self.bullet}, {self.item}, {self.text[:20]}>"
        
    def lines(self, doc_spec):
        if doc_spec.target == 'MD':
            s = ' '*self.level
            if self.bullet is not None:
                s += self.bullet + ' '
            if self.item is None:
                if self.text is None:
                    return ["\n"]
                else:
                    return [s + self.text]
            else:
                if self.text is None:
                    return [s + self.item]
                else:
                    return [s + self.item + ' : ' + self.text]
        
        width = doc_spec.width
        
        if self.item is None:
            return split_line(self.text, width, indent=self.level, bullet=self.bullet)
        else:
            item_len = max(1, self.item_len)
            return split_line(f"{self.item:{item_len}s} : {self.text}", width, indent=self.level, bullet=self.bullet)
        
class NewLine(Paragraph):
    def __init__(self):
        super().__init__()

# ----------------------------------------------------------------------------------------------------
# Section

class Header(DocText):
    
    text_type = 'HEADER'
    
    def __init__(self, title, level=0, prefix=None, indent=0, use_margin=False):
        super().__init__(title, level)
        self.prefix = "" if prefix is None else prefix.strip() + " "
        self.indent = indent
        self.use_margin = use_margin or level > 3
        
    def lines(self, doc_spec):
        if self.level < 0:
            return []
        
        # ---------------------------------------------------------------------------
        # Markdown
        
        if doc_spec.is_md:
            return ['#'*(self.level +1 ) + ' ' + self.text + "\n"]
        
        # ---------------------------------------------------------------------------
        # Text
        
        width = doc_spec.width
        
        n = len(self.text)
        s_top = None
        s_bot = None
        
        prefix = ""
        
        if self.level == 0:
            s_top = "\n"
            s_bot = "="*width
            
        elif self.level == 1:
            s_bot = "="*n
            
        elif self.level == 2:
            s_top = "-"*n
            s_bot = "-"*n
            
        elif self.level == 3:
            s_bot = "-"*n
            
        else:
            prefix = "---" * (self.level-3) + " "
            
        prefix = "  "*self.indent + prefix
            
        lines = []
        if s_top is not None: lines.append(prefix + s_top)
        lines.append(prefix + self.prefix + self.text)
        if s_bot is not None: lines.append(prefix + s_bot)
        lines.append("")
        
        return lines
        
    def __str__(self):
        return f"<Section [{self.level}] {self.text}>"
    
# ----------------------------------------------------------------------------------------------------
# Source code

class Source(DocText):
    text_type = 'PYTHON'
    
    def lines(self, doc_spec):
        width = 250 if doc_spec.target == 'MD' else 120
        return split_line("``` python", width, indent=self.level) + super().lines(DocSpec(width=width)) + split_line("```", width, indent=self.level)
        
# ====================================================================================================
# List

class List:
    def __init__(self, doc, title=None, bullet=None, new_line=True):
        self.doc      = doc
        self.paras    = []
        self.title    = title
        self.bullet   = bullet
        self.new_line = True
        
    def add(self, label, description=None):
        para = Paragraph(description, level=self.level, bullet=self.bullet, item=label)
        self.doc.add(para)
        self.paras.append(para)
        
        if label is not None:
            self.item_len = max(self.item_len, len(label))
        
    def __enter__(self):

        if self.title is not None:
            #self.doc.add(Header(self.title, 2, indent=self.doc.list_level, use_margin=True))
            if self.doc.is_md:
                self.doc.add(Paragraph(self.title, level=self.doc.list_level))
            else:
                self.doc.add(Paragraph(self.title, level=self.doc.list_level), Paragraph('-'*len(self.title), level=self.doc.list_level))

            self.doc.list_level += 1
        
        self.level    = self.doc.list_level
        self.bullet   = ['o', '-', '.', ':'][self.level % 4] if self.bullet is None else self.bullet
        self.item_len = 1
        self.doc.list_level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.doc.list_level -= 1 if self.title is None else 2
        for para in self.paras:
            para.item_len = self.item_len
        if self.new_line:
            self.doc.add(new_line=True)

# ====================================================================================================
# Documentation builder

class Doc:
    def __init__(self, doc_spec=None):
        
        self.doc_spec = DocSpec() if doc_spec is None else doc_spec

        self.list_level = 0
        self.paragraphs = []
        
    # ---------------------------------------------------------------------------
    # Clear the content
        
    def clear(self):
        self.list_level = 0
        self.paragraphs = []

    # ---------------------------------------------------------------------------
    # Is markdown tag
        
    @property
    def is_md(self):
        return self.doc_spec.is_md
    
    # ---------------------------------------------------------------------------
    # Add paragraphs
        
    def add(self, *paras, new_line=False):
        for para in paras:
            self.paragraphs.append(para)
        if new_line:
            self.paragraphs.append(Paragraph())
            
    # ---------------------------------------------------------------------------
    # New line
            
    def new_line(self):
        self.add(new_line=True)

    # ---------------------------------------------------------------------------
    # Separator
        
    def separator(self, fill=None):
        if self.is_md:
            self.add(Paragraph("\n-----\n"), new_line=True)
        else:
            self.add(new_line=True)
            if fill is None:
                self.add(Paragraph(fill), new_line=True)

    # ---------------------------------------------------------------------------
    # Paragraph
            
    def paragraph(self, text="", level=0, bullet=None, item=None, new_line=True):
        self.add(Paragraph(text=text, level=level, bullet=bullet, item=item), new_line=new_line)

    # ---------------------------------------------------------------------------
    # Description

    def description(self, text="", level=0, new_line=True):
        self.add(Paragraph(text=text, level=level, bullet=">"), new_line=new_line)

    # ---------------------------------------------------------------------------
    # Header

    def header(self, title, level=0, prefix=None, indent=0, use_margin=False, new_line=False):
        self.add(Header(title, level=level, prefix=prefix, indent=indent, use_margin=use_margin), new_line=new_line)
            
    # ---------------------------------------------------------------------------
    # Bullets
        
    def bullets(self, title=None, bullet="-", new_line=True):
        return List(self, title=title, bullet=bullet, new_line=new_line)
    
    # ====================================================================================================
    # Build the resulting text
    
    # ---------------------------------------------------------------------------
    # List of lines
    
    @property
    def lines(self):
        lines = []
        for para in self.paragraphs:
            ls = para.lines(self.doc_spec)
            if para.use_margin:
                ls = [" "*self.doc_spec.margin + l for l in ls]
            lines.extend(ls)
        return lines

    # ---------------------------------------------------------------------------
    # Global text
    
    @property
    def text(self):
        return "\n".join(self.lines)      
    
    # ====================================================================================================
    # Demo
    
    @staticmethod
    def demo():
        
        def test(doc, title):
            doc.header(title, 0)
            doc.description("This a demo document containing a main header and sub sections. One can also find list of bullets points.")
            doc.header("Section 1", 1)
            doc.description("This is the first section of the document.")
            with doc.bullets("Here is what you'll find:") as bs:
                bs.add("Section 1", "This section")
                bs.add("Another section", "Just for fun")
                bs.add("The last section", "The description of this section is very long. "*5)
            
            doc.header("Another section", 1)
            doc.description("This section has several sub sections.")

            doc.header("Sub section 1", 2)
            doc.header("Sub sub section 1", 3)
            doc.header("Last sub section 1", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 2", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 3", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            
            doc.header("Sub sub section 2", 3)
            doc.header("Last sub section 1", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 2", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 3", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            
            doc.header("Sub section 2", 2)
            doc.header("Sub sub section 1", 3)
            doc.header("Last sub section 1", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 2", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 3", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            
            doc.header("Sub sub section 2", 3)
            doc.header("Last sub section 1", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 2", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            doc.header("Last sub section 3", 4)
            doc.paragraph("Some standard text in ths final subsection. "*5)
            
            doc.header("The last section", 1)
            doc.paragraph("This closes this demo.")
            
        
        doc = Doc()
        test(doc, "Text version")
        
        print(doc.text)
        
        doc = Doc(DocSpec(target='MD'))
        test(doc, "MarkDown version")
        
        print(doc.text)
        
Doc.demo()
    
    

"""

# Node BooleanMath

> Geometry node name: [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)<br>
  Blender type: [Boolean Math](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
  
<sub>go to [index](/docs/index.md)</sub>
"""

class Doc_OLD:
    def __init__(self, tree_type, doc_spec=None):
        
        self.tree_type  = tree_type
        self.tree_class = TREE_CLASSES[tree_type]
        
        self.dct  = doc_dict(tree_type)
        self.cref = cross_ref_dict(tree_type)
        
        self.doc_spec = DocSpec() if doc_spec is None else doc_spec

        self.list_level = 0
        self.paragraphs = []
        
    def clear(self):
        self.list_level = 0
        self.paragraphs = []
        
    @property
    def is_md(self):
        return self.doc_spec.is_md
        
    def add(self, *paras, new_line=False):
        for para in paras:
            self.paragraphs.append(para)
        if new_line:
            self.paragraphs.append(Paragraph())
        
    def sepa(self, fill=None):
        self.add(new_line=True)
        if fill is None:
            self.add(Paragraph(fill), new_line=True)
        
    def bullets(self, title=None, bullet=None, new_line=True):
        return List(self, title=title, bullet=bullet, new_line=new_line)
    
    @property
    def lines(self):
        lines = []
        for para in self.paragraphs:
            ls = para.lines(self.doc_spec)
            if para.use_margin:
                ls = [" "*self.doc_spec.margin + l for l in ls]
            lines.extend(ls)
        return lines
    
    @property
    def text(self):
        return "\n".join(self.lines)
    
    # ====================================================================================================
    # Links
    
    def class_link(self, name, class_name=None):
        if name is None:
            return "None"
        
        elif self.doc_spec.target == 'MD':
            if class_name is None:
                return f"[{name}](/docs/{self.tree_class}_classes/{name}.md)"
            else:
                return f"[{name}](/docs/{self.tree_class}_classes/{class_name}.md#{name})"
                
        else:
            return name
        
    def page_link(self, name):
        if name is None:
            return ""
        elif self.doc_spec.target == 'MD':
            return f"[{name}](#{name.lower().replace(' ', '-')})"
        
    def list_links(self, names, page=False, class_name=None):
        if self.doc_spec.target == 'MD':
            if page:
                return [self.page_link(name) for name in names]
            else:
                return [self.class_link(name, class_name=class_name) for name in names]
        else:
            return names
        
    @staticmethod
    def initials(names):
        initials = set([name.upper()[0] for name in names])
        return {initial: [name for name in names if name.upper()[0] == initial] for initial in initials}
    
    # ====================================================================================================
    # Cross references
    
    def cross_reference(self, class_name):
        
        cref = self.cref[class_name]
        with self.bullets(new_line=True) as bullets:
        
            if 'GLOBAL' in cref:
                bullets.add("functions", " ".join(self.list_links(cref['GLOBAL'], class_name='GLOBAL'))  + "\n")
                
            for target, names in cref.items():
                if target == 'GLOBAL':
                    continue
                
                bullets.add(target, " ".join(self.list_links(names, class_name=target))  + "\n")
    
    # ====================================================================================================
    # Member documentation
    
    def member_doc(self, member, level=1):
        
        title = member['name']
        if member.get('static', False):
            title += ' (static)'
        self.add(Header(title, level=level))
        
        if member['descr'] is not None:
            self.add(Paragraph('> ' + member['descr']), new_line=True)

        is_property = member['type'] == 'Properties'
            
        if member.get('code') is not None:
            self.add(Source(member['code'].strip().split("\n")[0]))
        
        if is_property:
            with self.bullets("Nodes", new_line=True) as bullets:
                bullets.add('get', self.class_link(member['getter_node']))
                bullets.add('set', self.class_link(member['setter_node']))
                
            getter = member.get('getter')
            if getter is None:
                s = f"# Write only property"
            else:
                s = "@property\n" + getter.strip()
            
            setter = member.get('setter')
            if setter is not None:
                s += f"\n\n@{title}.setter\n" + setter.strip()
                
            self.add(Source(s))
                
        else:
            with self.bullets("Node", new_line=True) as bullets:
                bullets.add('class_name', self.class_link(member['node_class']))
                bullets.add('bl_idname', member['bl_idname'])
                
        meth_args = member.get('meth_args')
        if meth_args is not None and (len(meth_args) > 1 or (len(meth_args) == 1 and meth_args[0] != "self")):
            with self.bullets("Arguments", new_line=True) as bullets:
                for item in meth_args:
                    if item == "self":
                        continue
                    if isinstance(item, tuple):
                        bullets.add(item[0], item[1])
                    else:
                        bullets.add(item, "")
                        
        node_args = member.get('node_args')
        if node_args is not None:
            with self.bullets("Node initialization", new_line=True) as bullets:
                for item in node_args:
                    if isinstance(item, tuple):
                        bullets.add(item[0], item[1])
                    else:
                        bullets.add(item, "")


    # ====================================================================================================
    # Class documentation
    
    def node_class_doc(self, class_name):
        
        dct = self.dct[class_name]
        
        self.add(Header(f"class {class_name} ({dct['category']})", 0))

        if self.is_md:
            self.add(Paragraph("<sub>go to [index](/docs/index.md)</sub>"), new_line=True)
    
        if dct['descr'] is not None:
            self.add(Paragraph(dct['descr']), new_line=True)
            
        # ----- Node reference
    
        self.add(Header("Node reference", 1))
        
        with self.bullets("Node") as bullets:
            bullets.add("Class name", class_name)
            bullets.add("bl_idname", dct['bl_idname'])
            
        params = dct.get('params')
        if params is not None:
            with self.bullets("Node parameters") as bullets:
                for param, value in params.items():
                    bullets.add(param, value)
            
        sockets = dct.get('input_sockets')
        if sockets is not None:
            with self.bullets("Input sockets") as bullets:
                for param, value in sockets.items():
                    bullets.add(param, value[0] if len(value)==1 else str(value))
            
        sockets = dct.get('output_sockets')
        if sockets is not None:
            with self.bullets("Output sockets") as bullets:
                for param, value in sockets.items():
                    bullets.add(param, value[0] if len(value)==1 else str(value))
                        
        # ----- Init code
                        
        if dct['code'] is not None:
            self.add(Header("Header", 2, use_margin=True))
            self.add(Source(dct['code'].split("\n")[0]), new_line=True)
            
        # ----- Cross reference
        
        self.add(Header("Implementations", 1))
        self.cross_reference(class_name)
        self.add(new_line=True)

                
    # ====================================================================================================
    # Socket documentation
    
    def socket_class_doc(self, class_name, member_name=None, small=True):
        
        dct = self.dct[class_name]
        
        # ----- Member detail
        
        if member_name is not None:
            dct = dct['members'].get(member_name)
            if dct is None:
                self.add(Paragraph(f"Class {class_name} has no member named {member_name}."), new_line=True)
            else:
                self.member_doc(dct, level=1)
            return

        # ----- Class documentation
        
        self.add(Header(f"class {class_name} ({dct['category']})", 0))
        
        if self.is_md:
            self.add(Paragraph("<sub>go to [index](/docs/index.md)</sub>"), new_line=True)
    
        if dct['descr'] is not None:
            self.add(Paragraph("> " + dct['descr']), new_line=True)
            
        # ----- Socket reference
        
        if not small:
            self.add(Header("Socket reference", 1))
        
        with self.bullets("Socket") as bullets:
            bullets.add("Type", dct['socket type'])
            bullets.add("bl_idname", dct['bl_idname'])
        
        # ----- Members

        s_dct = sort_dict(dct['members'], "type", none_key=None)
        if len(s_dct):
            
            # ----- Member list
            
            for stype in s_dct:
                with self.bullets(stype) as bullets:
                    for member_name in sorted(s_dct[stype].keys()):
                        bullets.add(self.page_link(member_name), s_dct[stype][member_name]['descr'])
                        
            # ----- Member detail
                        
            if self.is_md:
                for stype in s_dct:
                    self.add(Header(stype, 1))
                    
                    for member_name in sorted(s_dct[stype].keys()):
                        member = s_dct[stype][member_name]
                        
                        self.member_doc(member, level=2)
                
                
    # ====================================================================================================
    # Class documentation
    
    def class_doc(self, class_name, member_name=None):
        
        dct = self.dct[class_name]
        if dct['category'] == 'Node':
            self.node_class_doc(class_name)
        elif dct['category'] == 'Socket':
            self.socket_class_doc(class_name, member_name=member_name)
        else:
            self.add(Header(f"class {class_name} ({dct['category']})", 0))
        
            if dct['descr'] is not None:
                self.add(Paragraph(dct['descr']), new_line=True)
                
# =============================================================================================================================
# Build the documentation

FULL_BUILD = """

from geonodes import GeoNodes, Shader
from geonodes.nodes.documentation import build_doc

with GeoNodes("Build"):
    pass

with Shader("Build"):
    pass

build_doc(...)

"""

def build_doc(folder):
    
    INDEX = {tree_type : {} for tree_type in TREE_CLASSES.keys()}
    
    index_doc = Doc('GeometryNodeTree', doc_spec=DocSpec(target='MD'))
    index_doc.add(Header("Index", 0))
    for key in sorted(TREE_CLASSES.values()):
        index_doc.add(Paragraph(f"[{key}](#{key.lower()})\n"))
    index_doc.add(new_line=True)
    
    for tree_type in TREE_CLASSES.keys():
        
        # ----- Documentation of classes
        
        tree_class = TREE_CLASSES[tree_type]
        
        root = Path(folder)
        
        classes_folder = root / f"{tree_class}_classes"
        
        classes = {}
        globs   = []
        
        doc = Doc(tree_type, DocSpec(target='MD', path=root))
        for class_name in doc.dct.keys():
            if class_name == 'GLOBAL':
                keys = sorted(doc.dct['GLOBAL'].keys())
                
                doc.add(Header("Global functions", 0))

                initials = index_doc.initials(keys)
                for initial in sorted(initials.keys()):
                    sub = initials[initial]
                    links = " ".join(doc.list_links(sorted(sub), page=True))
                    doc.add(Paragraph(f"***{initial}*** : " + links), new_line=True)
                    
                for name in keys:
                    member = doc.dct['GLOBAL'][name]
                    doc.member_doc(member)
                    globs.append(name)
            
            else:
                doc.class_doc(class_name)
                cat = doc.dct[class_name]['category']
                if cat not in classes:
                    classes[cat] = []
                    
                classes[cat].append(class_name)
                
            with open(classes_folder / f"{class_name}.md", 'w') as f:
                f.write(doc.text)
            doc.clear()
            
        # ----- Index
        
        index_doc.add(Header(tree_class, 0))
        for cat, class_names in classes.items():
            index_doc.add(Header(cat, 1))
            if len(class_names) > 20:
                initials = index_doc.initials(class_names)
                for initial in sorted(initials.keys()):
                    sub = initials[initial]
                    links = " ".join(doc.list_links(sorted(sub)))
                    index_doc.add(Paragraph(f"***{initial}*** : " + links), new_line=True)
            else:
                links = " ".join(index_doc.list_links(sorted(class_names)))
                index_doc.add(Paragraph(links))

    with open(root / "index.md", 'w') as f:
        f.write(index_doc.text)
        
    doc.clear()
    
    
        
        
    
    
                
            
# =============================================================================================================================
# Documentation

def print_doc(obj, member_name=None):
    
    tree_type = obj.__dict__.get('_tree_type', None)
    if tree_type is None:
        print(f"{obj} is not documented.")
        return
    
    # ----- Initialize the documentation
    
    doc = Doc(tree_type, doc_spec=DocSpec())
    class_name = obj.__dict__.get('_class_name')
    
    # ----- No class_name : this is a class
    
    if class_name is None:
        class_name = obj.__name__
        if not class_name in doc.dct:
            print("Sorry: {obj} is not documented.")
            return

        doc.class_doc(class_name, member_name=member_name)

    # ----- Global function

    elif class_name == 'GLOBAL':
        member = doc.dct['GLOBAL'].get(obj.__name__)
        if member is None:
            print(f"Sorry: function {obj.__name__} is not documented.")
            return

        doc.member_doc(member)
        
    # ----- Class method
        
    else:
        member = doc.dct[class_name]['members'].get(obj.__name__)
        if member is None:
            print(f"Sorry: method {obj.__name__} of class {class_name} is not documented.")
            return
            
        doc.member_doc(member)
        
    print('-'*100)
    print()
    print(doc.text)
    print()
        
 








