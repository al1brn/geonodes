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

from geonodes.nodes import constants
from geonodes.nodes import utils

# ----------------------------------------------------------------------------------------------------
# print_doc class method implemented in the dynamic classes

@classmethod
def print_doc(cls, member=None):
    
    dyn = getattr(cls, '_dynamic', None)
    if dyn is None:
        print(f"Sorry, the class '{cls.__name__}' is not documented (no '_dynamic' attribute).")
        
    elif dyn.dyn_type == Dynamic.TREE:
        dyn.tree_print_doc(member)
        
    elif dyn.dyn_type == Dynamic.NODE:
        dyn.node_print_doc(member)
        
    elif dyn.dyn_type == Dynamic.SOCKET:
        dyn.socket_print_doc(member)
        
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
        
        if True and self.class_name == 'SeparateXYZ':
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
                prop = {'fget': None, 'fset': None, 'getter': None, 'setter': None}
                self.properties[name] = prop
                
            if member_type == 'GETTER':
                if prop['getter'] is not None:
                    print(f"CAUTION: getter of property named '{name}' is already defined")
                prop['getter'] = func
                prop['fget']   = func['f']
            else:
                if prop['setter'] is not None:
                    print(f"CAUTION: setter of property named '{name}' is already defined")
                prop['setter'] = func
                prop['fset']   = func['f']
                
            setattr(self.dyn_class, name, property(prop['fget'], prop['fset']))
                
                
        else:
            raise AttributeError(f"Dynamic.add_member error: unknown member_type: '{member_type}' for member '{name}' in class '{self.class_name}'")
                
    # ====================================================================================================
    # Build the class
        
    def build_class_OLD(self):
        """ Set methods and properties to the class.
        
        Done afterward in order to collect fget and fset for properties
        """
        
        if True and self.class_name == 'SeparateXYZ':
            print("DYNAMIC build_class", self.class_name, list(self.methods.keys()), list(self.properties.keys()))
        
        for name, method in self.methods.items():
            setattr(self.dyn_class, name, method['f'])
            
        for name, prop in self.properties.items():
            setattr(self.dyn_class, name, property(prop['fget'], prop['fset']))
            
    # ====================================================================================================
    # Inline documentation
    
    # ----------------------------------------------------------------------------------------------------
    # Print list of args
    
    @staticmethod
    def print_args(args):
        docs = args.docs
        if len(docs) == 0:
            return
        print("Arguments")
        print('---------')
        for doc in docs:
            print(f" - {doc[0]:15s}", end = "")
            if doc[1] != 'ARG_NO_VALUE':
                print(f": {doc[1]}", end="")
                if doc[2] is not None:
                    print(f" in {doc[2]}", end="")
            print()
        print()

    # ----------------------------------------------------------------------------------------------------
    # Print func dict
                    
    @staticmethod
    def print_func(func):
        if func['descr'] is not None:
            print(func['descr'])
            print()
            
        print(f"- {'node':15s} : {func['node_class_name']}")
        for k, v in func['kwargs'].items():
            k_ = 'self' if k == 'self_socket' else k
            print(f"- {k_:15s} : {v}")
        print()
        
        Dynamic.print_args(func['args'])

        print()
        print("Source code")
        print("-----------")
        print(func['code'].replace('\t', '    '))
    
    # ----------------------------------------------------------------------------------------------------
    # Tree documentation
    
    def tree_print_doc(self, function=None):
        
        tree_type = self.dyn_class.TREE_TYPE
        
        print('-'*80)
        print(f"Tree {self.class_name} ({tree_type})")
        print()
        
        # ----------------------------------------------------------------------------------------------------
        # A specific function
        
        if function is not None:
            func = self.methods.get(function)
            if func is None:
                print(f"Sorry, no function named '{function}' found in tree '{cls.__name__}'.")
            
            else:
                self.print_func(func)
            
            return

        # ----------------------------------------------------------------------------------------------------
        # The whole Tree

        if self.descr is not None:
            print(self.descr)
            print()
            
        print("Socket Classes")
        print("------------")
        print()
        for class_name in sorted(constants.SOCKETS[tree_type].keys()):
            print(" -", class_name)
        print()
        
        print("Node Classes")
        print("------------")
        print()
        for class_name in sorted(constants.NODES[tree_type].keys()):
            print(class_name, end=" ")
        print()
        print()

        print("Functions")
        print("---------")
        print()
        for name in sorted(self.methods.keys()):
            print(name, end=" ")
        print()
        print()
        
    # ----------------------------------------------------------------------------------------------------
    # Node documentation
    
    def node_print_doc(self, member=None):
        
        tree_type  = self.node_info.tree_type
        class_name = self.node_info.class_name
        
        print('-'*80)
        print(f"Node {class_name}")
        print()
        print(f"- Node name : '{self.node_info.name}'")
        print(f"- bl_idname : {self.node_info.bl_idname}")
        print()
        
        if self.descr is not None:
            print(self.descr)
            print()
            
        print("")
        
        func = self.methods.get('__init__')
        if func is not None:
            header = func['code'].split("\n")[0].replace("def __init__(self, ", class_name + "(").strip()[:-1]
            print(header)
            print()
            
            self.print_args(func['args'])
            
        print("Implementation")
        print("==============")
        print()

        cross_ref = constants.CROSS_REF[tree_type].get(class_name)
        if cross_ref is None:
            print("No implementation in sockets")
            print()
        else:
            for socket in sorted(cross_ref.keys()):
                print(" -", socket, end = " : ")
                print(" ".join(sorted(cross_ref[socket])))
            print()

        print("Init")
        print("====")
        print()
        print(func['code'])
        print()
        

            
            
        print()
        
    # ----------------------------------------------------------------------------------------------------
    # Class documentation
    
    def socket_print_doc(self, member=None):

        print('-'*80)
        s = "" if member is None else f".{member}"
        print(f"Socket {self.class_name}{s}")
        print()
        
        # ----------------------------------------------------------------------------------------------------
        # A specific member
            
        if member is not None:
            
            is_meth = True
            func    = self.methods.get(member)
            if func is None:
                is_meth = False
                func    = self.properties.get(member)
                
            if func is None:
                print(f"Sorry, Socket class '{type(self).__name__}' has no member named {member}\n\n")
                return
            
            if is_meth:
                print(f"{member} (Method):")
                print()
                self.print_func(func)
                
            else:
                cat = 'Property'
                if func['getter'] is None:
                    cat = 'Write only Property'
                elif func['setter'] is None:
                    cat = 'Read only Property'
                    
                print(f"{member} ({cat}):")
                print()
                if func['getter'] is not None:
                    print("GET")
                    print('==========')
                    print()
                    self.print_func(func['getter'])
                print()
    
                if func['setter'] is not None:
                    print("SET")
                    print('==========')
                    print()
                    self.print_func(func['setter'])
                print()
                
            print()
            print()
            return
        
        # ----------------------------------------------------------------------------------------------------
        # The Socket class
            
        if self.descr is not None:
            print(self.desct)
            print()
            
        print(f"Properties ({len(self.properties)}):")
        print( "-----------------")
        for name in sorted(self.properties.keys()):
            print(name, end=" ")
        print()
        print()
        
        print(f"Methods ({len(self.methods)}):" )
        print( "-----------------")
        for name in sorted(self.methods.keys()):
            print(name, end=" ")
        print()
        print()
            

                
        
        
        
        
    
    
    
        
