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

# ----- Documentation

DOCUMENTATION_DICT = {}

# ----- CROSS REFERENCES
# How nodes are implemented

CROSS_REF_DICT = {}

# ====================================================================================================
# Dynamic access

def doc_dict(tree_type, class_name=None):
    """ Get a doc dictionary dedicated to a given tree type.
    
    Create the dictionary if it doesn't exist
    
    A tree type dictionary contains:
        - 'GLOBAL' : a dictionary for global functions such as sin or tan
        - On dictionary per entry
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        - class_name (str = None) : class name entry
        
    Returns
    -------
        - dict
    """
    
    dct = DOCUMENTATION_DICT.get(tree_type)
    if dct is None:
        dct = {'GLOBAL': {}}
        DOCUMENTATION_DICT[tree_type] = dct
        
    if class_name is None:
        return dct
    
    d = dct.get(class_name)
    if d is None:
        d = {'name'      : class_name,
             'category'  : None,
             'bl_idname' : None,
             'descr'     : None,
             'code'      : None,
             'members'   : {},
            }
        dct[class_name] = d
        
    return d

def global_doc_dict(tree_type):
    """ Get the global dictionary for a tree type.
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        
    Returns
    -------
        - dict
    """
    
    return doc_dict(tree_type, class_name = 'GLOBAL')

def cross_ref_dict(tree_type=None, class_name=None):
    """ Get the cross ref dictionary for a tree type.
    
    The cross reference provides an entry per method or function implementing a node class.
    
    cross_ref[Math] = {'GLOBAL' : ['sin', 'cos', ...],
                       'Float'  : ['sin', 'cos', ...],
                       'Int';   : ['sin', 'cos', ...],
                       }
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        - class_name : Node class name
        
    Returns
    -------
        - dict
    """
    
    dct = CROSS_REF_DICT.get(tree_type)
    if dct is None:
        dct = {}
        CROSS_REF_DICT[tree_type] = dct
        
    if class_name is None:
        return dct
    
    d = dct.get(class_name)
    if d is None:
        d = {}
        dct[class_name] = d
    return d

def new_cross_ref(tree_type, class_name, target=None, name=None):
    """ Register a new cross reference for a node.
    
    Name is the name of the global function or of the target class method.
    If name is None, the cross_ref dict is created for further use.
    An empty dict means that the Node is not implemented.
    
    Target is the name of the socket class implementing the node.
    Use 'target=None' for global functions.
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        - class_name (str) : Node class name
        - target (str = None) : class name using the node
        - name (str = None) : method name using the node
    """    
        
    dct = cross_ref_dict(tree_type, class_name)

    if name is None: # Just to create the entry for cross reference
        return

    if target is None:
        target = 'GLOBAL'
    
    if target not in dct:
        dct[target] = [name]
    else:
        dct[target].append(name)

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
# Doc specification

class DocSpec:
    def __init__(self, target='TEXT', width=100, margin=4):
        self.target = target
        self.width  = width
        self.margin = margin
        
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
    
    def lines(self, width):
        if self.text is None:
            return [""]
        else:
            return split_line(self.text, width, indent=self.level)
        
# ----------------------------------------------------------------------------------------------------
# Paragraph

class Paragraph(DocText):
    def __init__(self, text="", level=0, bullet=None, item=None):
        super().__init__(text, level=level)
        
        self.bullet   = bullet
        self.item     = item     # item   : text
        self.item_len = 1
        
    def __str__(self):
        return f"<Paragraph {self.level}, {self.bullet}, {self.item}, {self.text[:20]}>"
        
    def lines(self, width):
        if self.item is None:
            return split_line(self.text, width, indent=self.level, bullet=self.bullet)
        else:
            item_len = max(1, self.item_len)
            return split_line(f"{self.item:{item_len}s} : {self.text}", width, indent=self.level, bullet=self.bullet)

# ----------------------------------------------------------------------------------------------------
# Section

class Header(DocText):
    
    text_type = 'HEADER'
    
    def __init__(self, title, level=0, prefix=None, indent=0, use_margin=False):
        super().__init__(title, level)
        self.prefix = "" if prefix is None else prefix.strip() + " "
        self.indent = indent
        self.use_margin = use_margin or level > 3
        
    def lines(self, width):
        if self.level < 0:
            return []
        
        n = len(self.text)
        s_top = None
        s_bot = None
        if self.level == 0:
            s_bot = "="*n
        elif self.level == 1:
            s_top = "-"*n
            s_bot = "-"*n
        elif self.level == 2:
            s_bot = "-"*n
            
        prefix = "  "*self.indent
            
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
    
    def lines(self, width):
        return split_line("``` python", width, indent=self.level) + super().lines(250) + split_line("```", width, indent=self.level)
        
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
        
        self.item_len = max(self.item_len, len(label))
        
    def __enter__(self):

        if self.title is not None:
            #self.doc.add(Header(self.title, 2, indent=self.doc.list_level, use_margin=True))
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
    def __init__(self, tree_type, doc_spec=None):
        
        self.dct  = doc_dict(tree_type)
        self.cref = cross_ref_dict(tree_type)
        
        self.doc_spec = DocSpec() if doc_spec is None else doc_spec

        self.list_level = 0
        self.paragraphs = []
        
    def clear(self):
        self.list_level = 0
        self.paragraphs = []
        
        
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
            ls = para.lines(self.doc_spec.width)
            if para.use_margin:
                ls = [" "*self.doc_spec.margin + l for l in ls]
            lines.extend(ls)
        return lines
    
    @property
    def text(self):
        return "\n".join(self.lines)
    
    # ====================================================================================================
    # Cross references
    
    def cross_reference(self, class_name):
        
        cref = self.cref[class_name]
        
        with self.bullets(new_line=True) as bullets:
        
            if 'GLOBAL' in cref:
                bullets.add("functions", " ".join(cref['GLOBAL']))
                
            for target, names in cref.items():
                if target == 'GLOBAL':
                    continue
    
                bullets.add(target, " ".join(names) + " ")
    
    # ====================================================================================================
    # Member documentation
    
    def member_doc(self, member, level=1):
        title = member['name']
        if member.get('static', False):
            title += ' (static)'
        self.add(Header(title, level=level))
        
        if member['descr'] is not None:
            self.add(Paragraph(member['descr']), new_line=True)
            
        with self.bullets("Node", new_line=True) as bullets:
            bullets.add('class_name', member['class_name'])
            bullets.add('bl_idname', member['bl_idname'])
            
        if member['type'] == 'Method':
            meth_args = member['meth_args']
            if meth_args is not None and (len(meth_args) > 1 or (len(meth_args) == 1 and meth_args[0] != "self")):
                with self.bullets("Arguments", new_line=True) as bullets:
                    for item in meth_args:
                        if item == "self":
                            continue
                        if isinstance(item, tuple):
                            bullets.add(item[0], item[1])
                        else:
                            bullets.add(item, "")
                            
            node_args = member['node_args']
            if node_args is not None:
                with self.bullets("Node initialization", new_line=True) as bullets:
                    for item in node_args:
                        if isinstance(item, tuple):
                            bullets.add(item[0], item[1])
                        else:
                            bullets.add(item, "")

            if member['code'] is not None:
                self.add(Source(member['code'].strip().split("\n")[0]))
                
            if False and member['code'] is not None:
                self.add(Source(member['code'].strip()))

    # ====================================================================================================
    # Class documentation
    
    def node_class_doc(self, class_name):
        
        dct = self.dct[class_name]
        
        self.add(Header(f"class {class_name} ({dct['category']})", 0))
    
        if dct['descr'] is not None:
            self.add(Paragraph(dct['descr']), new_line=True)
            
        # ----- Node reference
    
        self.add(Header("Node reference", 1))
        
        with self.bullets("Node") as bullets:
            bullets.add("Class name", dct['name'])
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
    
    def socket_class_doc(self, class_name, small=True):
        
        dct = self.dct[class_name]
        
        self.add(Header(f"class {class_name} ({dct['category']})", 0))
    
        if dct['descr'] is not None:
            self.add(Paragraph(dct['descr']), new_line=True)
            
        # ----- Socket reference
        
        if not small:
            self.add(Header("Socket reference", 1))
        
        with self.bullets("Socket") as bullets:
            bullets.add("Type", dct['socket type'])
            bullets.add("bl_idname", dct['bl_idname'])
        
        # ----- Members

        s_dct = sort_dict(dct['members'], "type", none_key=None)
        if len(s_dct):
            for stype in ['Method']:
                
                if small:
                    with self.bullets(stype) as bullets:
                        for member_name in sorted(s_dct[stype].keys()):
                            bullets.add(member_name, s_dct[stype][member_name]['descr'])
                
                else:
                    self.add(Header(stype, 1))
                    
                    for member_name in sorted(s_dct[stype].keys()):
                        member = s_dct[stype][member_name]
                        self.member_doc(member, level=2)
                
                
    # ====================================================================================================
    # Class documentation
    
    def class_doc(self, class_name):
        
        dct = self.dct[class_name]
        if dct['category'] == 'Node':
            self.node_class_doc(class_name)
        elif dct['category'] == 'Socket':
            self.socket_class_doc(class_name)
        else:
            self.add(Header(f"class {class_name} ({dct['category']})", 0))
        
            if dct['descr'] is not None:
                self.add(Paragraph(dct['descr']), new_line=True)
            
# =============================================================================================================================
# Documentation

def print_doc(obj):
    
    # ----- Tree type
    
    tree_type = obj.__dict__.get('_tree_type', None)
    if tree_type is None:
        print(f"{obj} is not documented.")
        return
    
    # ----- Initialize the documentation
    
    doc = Doc(tree_type)
    class_name = obj.__dict__.get('_class_name')
    
    # ----- No class_name : this is a class
    
    if class_name is None:
        class_name = obj.__name__
        if not class_name in doc.dct:
            print("Sorry: {obj} is not documented.")
            return

        doc.class_doc(class_name)

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
        
 







