#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 07:14:33 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : dynmaic
----------------
- Create dynamic classs

update : 2024/02/17
"""

from pprint import pprint
from pathlib import Path


from geonodes.nodes import constants
from geonodes.nodes import utils

from geonodes.nodes.documentation import Doc


# ----------------------------------------------------------------------------------------------------
# print_doc class method implemented in the dynamic classes

@classmethod
def print_doc(cls, member=None):
    
    dyn = getattr(cls, '_dynamic', None)
    if dyn is None:
        print(f"Sorry, the class '{cls.__name__}' is not documented (no '_dynamic' attribute).")
        
    elif dyn.dyn_type == Dynamic.TREE:
        dyn.tree_print_doc(member, target_doc=None)
        
    elif dyn.dyn_type == Dynamic.NODE:
        dyn.node_print_doc(target_doc=None)
        
    elif dyn.dyn_type == Dynamic.SOCKET:
        dyn.socket_print_doc(member, target_doc=None)
        
    else:
        print(f"Sorry, the class '{cls.__name__}' has an unsupported type: '{dyn.dyn_type}'.")
        

    
# =============================================================================================================================
# Dynamic class

class Dynamic:
    """ Dynamic creation and documentation of Tree, Node and Socket classes.
    
    Arguments
    ---------
        - dyn_type (str) : in 'TREE', 'NODE', 'SOCKET'
        - dyn_class (class) : class to dynamically document
        - descr (str) : root documentation
    """
    
    
    
    SOCKET = 'SOCKET'
    NODE   = 'NODE'
    TREE   = 'TREE'
    
    def __init__(self, dyn_type, dyn_class, descr):
        
        self.dyn_type   = dyn_type
        
        self.dyn_class  = dyn_class
        self.descr      = descr
        
        self.methods    = {}
        self.properties = {}
        
        # ----- Store the dynamic record and the print_doc class method
        
        setattr(dyn_class, '_dynamic', self)
        setattr(dyn_class, 'print_doc',   print_doc)
        
    def __str__(self):
        return f"<Dynamic {self.class_name}: methods ({len(self.methods)}), properties ({len(self.properties)})>"
    
    @property
    def class_name(self):
        return self.dyn_class.__name__

    @classmethod
    def Tree(cls, tree_class, descr=None):
        """ Dynamic documentation and enrichment of a Tree class.
        
        Arguments
        ---------
            - tree_class : a sub class of Tree with TREE_NODE attribute
            - descr (str) : base documentation
        """
        
        # Dynamic info
        dyn = cls(Dynamic.TREE, tree_class, descr)
        
        return dyn
    
    @classmethod
    def NewNode(cls, node_info, base_class, descr=None):
        """ Dynamic creation and documentation of a Node class.
        
        > The Dynamic class stores are reference to an instance of NodeInfo but the NodeInfo.bnode is not valid at run time.
        
        Arguments
        ---------
            - node_info (NodeInfo) : Information on the node to create
            - base_class : the base class to use
            - descr (str) : base documentation
        """
        
        # Create the class
        dyn_class = type(node_info.class_name, (base_class,), {})
        
        # Dynamic info
        dyn = cls(Dynamic.NODE, dyn_class, descr)
        
        # Complementary info
        dyn.node_info = node_info
        
        return dyn
    
        
    @classmethod
    def NewSocket(cls, class_name, base_class, socket_type, descr=None):
        """ Dynamic creation and documentation of a Socket class.
        
        Arguments
        ---------
            - class_name (str) : name of the class
            - base_class : the base class to use
            - socket_type (str) : socket type
            - descr (str) : base documentation
        """
        
        
        # Create the class
        dyn_class = type(class_name, (base_class,), {})
        
        # Dynamic info
        dyn = cls(Dynamic.SOCKET, dyn_class, descr)
        
        # Complementary info
        dyn.socket_type = socket_type
        
        return dyn
        
    
    # ====================================================================================================
    # Add a new member
    
    def add_member(self, member_type, name, code, node_class_name, args=None, descr=None, **kwargs):
        """ Dynamically add a member to the dynamic class.
        
        The member is the implemntation of a Node as a method or property of a socket class.
        
        Arguments
        ---------
            - member_type (str) : type in 'METHOD', 'GETTER', 'SETTER'
            - name (str) : name
            - code (str) : source code to compile
            - node_class_name (str) : Node class name used in this implemenation
            - args (Arguments = None) : arguments (for documentation)
            - descr (str = None) : base documentation
            - kwargs : addition information for documentation
        """
        
        if False and self.class_name == 'SeparateXYZ':
            print('-'*100)
            print(f"DYNAMIC add_member {self.class_name}, name: {name}, type: {member_type}")
            print()
            print(code)
            print()
            
        #----- Code is already compiled
        if isinstance(code, tuple):
            ccode = code[1]
            code  = code[0]
            
        # Compile code
        else:
            ccode = utils.compile_f(code, name)
        
        func = {
            'cat'             : 'METHOD',
            'f'               : ccode,
            'node_class_name' : node_class_name,
            'code'            : code.strip(),
            'args'            : args,
            'descr'           : descr,
            'kwargs'          : kwargs
            }
        
        if member_type == 'METHOD':
            if name in self.methods or name in self.properties:
                print(f"CAUTION: method named '{name}' already exists in class {self.class_name}")
                
            self.methods[name] = func
            
            # ----- Set to the class
            
            setattr(self.dyn_class, name, ccode)
            
            
        elif member_type in ['GETTER', 'SETTER']:
            
            if name in self.methods:
                print(f"CAUTION: property named '{name}' is already the name of a method in class {self.class_name}")
                
            prop = self.properties.get(name)
            if prop is None:
                prop = {'cat': 'PROPERTY', 'fget': None, 'fset': None, 'getter': None, 'setter': None, 'descr': "Property"}
                self.properties[name] = prop
                
            if member_type == 'GETTER':
                if prop['getter'] is not None:
                    print(f"CAUTION: getter of property named '{name}' is already defined")
                prop['getter'] = func
                prop['fget']   = func['f']
                if prop['setter'] is None:
                    prop['descr'] = "Read only property"
                else:
                    prop['descr'] = "Property"
            else:
                if prop['setter'] is not None:
                    print(f"CAUTION: setter of property named '{name}' is already defined")
                prop['setter'] = func
                prop['fset']   = func['f']
                if prop['getter'] is None:
                    prop['descr'] = "Write only property"
                else:
                    prop['descr'] = "Property"
                
            
                
            setattr(self.dyn_class, name, property(prop['fget'], prop['fset']))
                
                
        else:
            raise AttributeError(f"Dynamic.add_member error: unknown member_type: '{member_type}' for member '{name}' in class '{self.class_name}'")
            
    # ====================================================================================================
    # Inline documentation
    
    # ----------------------------------------------------------------------------------------------------
    # Print list of args
    
    @staticmethod
    def print_args(doc, args):
        
        arg_docs = args.docs
        
        if len(arg_docs) == 0:
            return
        
        doc.header("Arguments", 4)
        with doc.bullets(item_len=[arg_doc[0] for arg_doc in arg_docs]) as bs:
            for arg_doc in arg_docs:
                descr = None
                if arg_doc[1] != 'ARG_NO_VALUE':
                    descr = str(arg_doc[1])
                    if arg_doc[2] is not None:
                        descr += f" in {arg_doc[2]}"
                bs.add(arg_doc[0], descr)

    # ----------------------------------------------------------------------------------------------------
    # Print func dict
                    
    @staticmethod
    def print_func(doc, func):
        
        doc.descr(func['descr'])
        
        # ---------------------------------------------------------------------------
        # Method
        
        if func['cat'] == 'METHOD':
            
            with doc.bullets(item_len=["node"] + [k for k in func['kwargs']]) as bs:
                bs.add("node", doc.page_link(func['node_class_name']))
                for k, v in func['kwargs'].items():
                    k_ = 'self' if k == 'self_socket' else k
                    bs.add(k_, v)
                    
            Dynamic.print_args(doc, func['args'])

            doc.header("Source code", 3)
            doc.source(func['code'])
        
        # ---------------------------------------------------------------------------
        # Property
        
        elif func['cat'] == 'PROPERTY':
        
            if func['getter'] is not None:
                doc.header("Get", 2)
                Dynamic.print_func(doc, func['getter'])

            if func['setter'] is not None:
                doc.header("Set", 2)
                Dynamic.print_func(doc, func['setter'])
                
        else:
            raise Exception(f"Unknown func category: {func['cat']}")
        
    
    # ----------------------------------------------------------------------------------------------------
    # Tree documentation
    
    def tree_print_doc(self, function=None, target_doc=None):

        if target_doc is None:
            doc = Doc()
        else:
            doc = target_doc
            
        tree_type = self.dyn_class.TREE_TYPE

        doc.header(f"Tree {self.class_name} ({tree_type})", 0)

        # ----------------------------------------------------------------------------------------------------
        # The whole Tree

        if function is None:
        
            doc.descr(self.descr)
            
            # ----- Socket classes
            
            doc.header("Socket classes", 2)

            links = {class_name: doc.page_link(class_name, "socket_"+class_name) for class_name in constants.SOCKETS[tree_type]}
            with doc.bullets() as bullets:
                bullets.alphabetical(links, len(links))

            # ----- Node classes
            
            doc.header("Node classes", 2)

            links = {dyn.node_info.class_name: doc.page_link(dyn.node_info.class_name, dyn.node_info.class_name) for bl_idname, dyn in constants.NODES[tree_type].items()}
            with doc.bullets() as bullets:
                bullets.alphabetical(links)

            # ----- Global function
            
            doc.header("Functions", 2)
            
            links = {name: doc.title_link(name) for name in self.methods.keys()}
            with doc.bullets() as bullets:
                bullets.alphabetical(links)

            # ----- All the functions if MarkDown
            
            if doc.is_md:
                doc.header("Functions", 1)

                for name in sorted(self.methods.keys()):
                    func = self.methods[name]
                    doc.header(f"{name}", 2)
                    self.print_func(doc, func)
            
        # ----------------------------------------------------------------------------------------------------
        # A specific function
        
        else:

            func = self.methods.get(function)
            if func is None:
                doc.descr(f"Sorry, no function named '{function}' found in tree '{type(self).__name__}'.")
            else:
                doc.header(f"{function} (function)", 1)
                self.print_func(doc, func)
            
        # ----------------------------------------------------------------------------------------------------
        # Print the doc
        
        if target_doc is None:
            doc.done()
        
    # ----------------------------------------------------------------------------------------------------
    # Node documentation
    
    def node_print_doc(self, target_doc=None):
        
        if target_doc is None:
            doc = Doc()
        else:
            doc = target_doc
            
        tree_type  = self.node_info.tree_type
        class_name = self.node_info.class_name
        bl_idname  = self.node_info.bl_idname
        
        doc.header(f"Node {class_name}", 0)

        with doc.bullets() as bullets:
            bullets.add("Node name", f"'{self.node_info.name}'")
            bullets.add("bl_idname", doc.url(bl_idname, constants.bldoc_node_bl_idname + f".{bl_idname}.html"))

        doc.descr(self.descr)

        func = self.methods.get('__init__')

        if func is not None:
            header = func['code'].split("\n")[0].replace("def __init__(self, ", class_name + "(").strip()[:-1]
            doc.source(header)
            self.print_args(doc, func['args'])
            
        doc.header("Implementation", 1)

        cross_ref = constants.CROSS_REF[tree_type].get(class_name)
        if cross_ref is None:
            doc.para("No implementation in sockets")

        else:
            with doc.bullets() as bullets:
                globs = None
                for socket in sorted(cross_ref.keys()):
                    if socket == 'GLOBAL':
                        globs = [doc.page_link(name, constants.TREE_CLASS_NAMES[tree_type]+"Tree", title=name) for name in sorted(cross_ref[socket])]
                    else:
                        links = [doc.page_link(name, f"socket_{socket}", title=name) for name in sorted(cross_ref[socket])]
                        bullets.add(doc.page_link(socket, f"socket_{socket}"), " ".join(links))
                        
                if globs is not None:
                    bullets.add("Functions", " ".join(globs))
                    
        if func is not None:
            doc.header("Init", 1)
            doc.source(func['code'])
        
        # ----------------------------------------------------------------------------------------------------
        # Print the doc
        
        if target_doc is None:
            doc.done()
        
        
    # ----------------------------------------------------------------------------------------------------
    # Class documentation
    
    def socket_print_doc(self, member=None, target_doc=None):
        
        if target_doc is None:
            doc = Doc()
        else:
            doc = target_doc
            
        # DEBUG            
        #doc = Doc.MarkDown()
            
        s = "" if member is None else f".{member}"
        doc.header(f"Socket {self.class_name}{s}", 0)
        
        # ----------------------------------------------------------------------------------------------------
        # The Socket class
            
        if member is None:
            
            if self.descr is not None:
                doc.description(self.descr)
                
            ok_header = True
            with doc.bullets() as bullets:
                for name in sorted(self.properties):
                    if ok_header:
                        doc.header("Properties", 2)
                        ok_header = False
                    bullets.add(doc.title_link(name))

            ok_header = True            
            with doc.bullets() as bullets:
                for name in sorted(self.methods):
                    if ok_header:
                        doc.header("Methods", 2)
                        ok_header = False
                    bullets.add(doc.title_link(name))
                    
            if doc.is_md:
                
                ok_header = True
                for name in sorted(self.properties.keys()):
                    if ok_header:
                        doc.header("Properties", 1)
                        ok_header = False
                        
                    func = self.properties[name]
                    doc.header(f"{name}", 2)
                    self.print_func(doc, func)
                
                ok_header = True
                for name in sorted(self.methods.keys()):
                    if ok_header:
                        doc.header("Methods", 1)
                        ok_header = False
                        
                    func = self.methods[name]
                    doc.header(f"{name}", 2)
                    self.print_func(doc, func)
                
        
        # ----------------------------------------------------------------------------------------------------
        # A specific member
            
        else:
            
            is_meth = True
            func    = self.methods.get(member)
            if func is None:
                is_meth = False
                func    = self.properties.get(member)
                
            if func is None:
                doc.paragraph(f"Sorry, Socket class '{type(self).__name__}' has no member named {member}\n\n")
                
            else:
                if is_meth:
                    
                    doc.header(f"{member} (Method)", 1)
                    self.print_func(doc, func)
                    
                else:
                    cat = 'Property'
                    if func['getter'] is None:
                        cat = 'Write only Property'
                    elif func['setter'] is None:
                        cat = 'Read only Property'
                        
                    doc.header(f"{member} ({cat})", 1)
                    
                    self.print_func(func)
                        
        # ----------------------------------------------------------------------------------------------------
        # Print the doc
        
        if target_doc is None:
            doc.done()
            
# =============================================================================================================================
# Print MD doc

def print_md_doc(folder):
    
    root = Path(folder)
    
    for tree_type, dyn_tree in constants.TREES.items():
        
        print('-'*100)
        print(f"Tree documentation: ", tree_type)
        print()
        
        tree_class = dyn_tree.dyn_class

        link_root = f"/docs/{tree_class.__name__}"
        file_root = root / tree_class.__name__

        doc = Doc.MarkDown(link_root=link_root)

        # ----- Tree class
        
        dyn_tree.tree_print_doc(None, target_doc=doc)
        doc.done(file_name=file_root / f"{tree_class.__name__}Tree.md")
        
        # ----- Socket classes
        
        for class_name, dyn in constants.SOCKETS[tree_type].items():
            dyn.socket_print_doc(None, target_doc=doc)
            doc.done(file_name=file_root / f"socket_{class_name}.md")
        
        # ----- Node classes
        
        for bl_idname, dyn in constants.NODES[tree_type].items():

            bl_idname  = dyn.node_info.bl_idname
            class_name = dyn.dyn_class.__name__
            if bl_idname in constants.NO_DOC_NODES:
                continue
            
            if False: # DEBUG
                print(f"Node class {class_name} ({bl_idname})")
            
            dyn.node_print_doc(target_doc=doc)
            doc.done(file_name=file_root / f"{class_name}.md")
        
    print("\nDocumentation built")
        
        
        
        
    
    
    
        
