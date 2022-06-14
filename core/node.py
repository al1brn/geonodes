#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:15:16 2022

@author: alain
"""

import bpy
import mathutils
import itertools
from contextlib import contextmanager

from pprint import pprint
import logging
logger = logging.getLogger('geonodes')

from geonodes import colors
from .arrange import arrange

# =============================================================================================================================
# > Root for data classes
#
# DataSocket refers to an output socket of a Geometry Node.
#
# ```python 
# DataSocket.bsocket # The output socket of a Geometry Node
# ```
#
# Methods of DataSocket instances are implemented with nodes. The output socket refered by
# the DataSocket instance is linked to an input socket of the method node.
#
# For instance:
# 
# ```python
# geo = Mesh.UVSphere()  # geo refers to the output socket of the node "Mesh UVSphere"
# geo.set_shade_smooth() # the previous output socket is linked to the input socket of
#                        # the node "Set Shade Smooth"
# ````
#
# Properties
# ----------
#
# - node: The node owning the output socket. The Blender Geometry Node itself is a property of node
#
#   ```python
#   node = a_data_socket.node # The Node class wrapping the Geometry Node
#   blender_node = node.bnode # The Blender geometry node
#   ```
#
# - bsocket: The Blender output socket 
# 


class DataSocket:
    
    # DataSocket class, sub class and domain data type from socket bl_idname    
        
    SOCKET_IDS = {
        'NodeSocketBool'        : ('Boolean',    '',             'BOOLEAN'), 

        'NodeSocketInt'         : ('Integer',    '',             'INT'), 
        'NodeSocketIntUnsigned' : ('Integer',    'Unsigned',     'INT'), 

        'NodeSocketFloat'       : ('Float',      '',             'FLOAT'), 
        'NodeSocketFloatFactor' : ('Float',      'Factor',       'FLOAT'),
        'NodeSocketFloatAngle'  : ('Float',      'Angle',        'FLOAT'), 
        'NodeSocketFloatDistance': ('Float',     'Distance',     'FLOAT'), 

        'NodeSocketVector'      : ('Vector',     '',             'FLOAT_VECTOR'), 
        'NodeSocketVectorEuler' : ('Vector',     'Rotation',     'FLOAT_VECTOR'),
        'NodeSocketVectorXYZ'   : ('Vector',     'xyz',          'FLOAT_VECTOR'), 
        'NodeSocketVectorTranslation' : ('Vector', 'Translation','FLOAT_VECTOR'), 

        'NodeSocketColor'       : ('Color',      '',             'FLOAT_COLOR'), 
        'NodeSocketString'      : ('String',     '',             'FLOAT_COLOR'), 

        'NodeSocketGeometry'    : ('Geometry',   '',              None), 

        'NodeSocketCollection'  : ('Collection', '',              None), 
        'NodeSocketImage'       : ('Image',      '',              None), 
        'NodeSocketMaterial'    : ('Material',   '',              None), 
        'NodeSocketObject'      : ('Object',     '',              None), 
        'NodeSocketTexture'     : ('Texture',    '',              None), 
    }
    
    # ----------------------------------------------------------------------------------------------------
    # > DataSocket initialization
    #
    # Arguments
    # ---------
    # - socket: a node socket or a DataSocket
    #   Passing a DataSocket instance as argument allows type casting
    #
    #   ```python
    #   value = Float(10.) # Float data class pointing on the output socket of node "Value"
    #   v = Vector(value)  # Cast the previous socket to Vector
    #   ```
    #
    # - node: the node owning the socket. If node is None, the initializer searchs for it in the list
    #  of existing nodes.
    #
    # - label: optional node label. Used to name the created Geometry Nodes.
    #

    def __init__(self, socket, node=None, label=None):
        
        # ----- Ensure the properties are create
        
        self.reset_properties()
        
        # ----- A class Object doesn't have a constructor Node

        if socket is None:
            self.bsocket = None
            self.node    = None
            
        else:
            if DataSocket.is_data_socket(socket):
                self.bsocket = socket.get_blender_socket()
    
            elif isinstance(socket, bpy.types.NodeSocket):
                self.bsocket = socket
            else:
                raise RuntimeError(f"A DataSocket instance needs a socket to be initialized, not {socket}.")
                
            if node is None:
                self.node = Tree.TREE.get_bnode_wrapper(self.bsocket.node)
            else:
                self.node = node
            
            if label is not None:
                self.node.label = label
        
    def __str__(self):
        snode = str(self.node)
        if self.is_output:
            return f"{snode}.{self.name}"
        else:
            return f"{self.name}.{snode}"
        
    def __repr__(self):
        return str(self)
    
    @staticmethod
    def is_data_socket(value):
        """ > An alternative to isinstance(value, DataSocket)
        """
        return hasattr(value, 'get_blender_socket')

    @staticmethod
    def gives_bsocket(value):
        """ Test if the argument provides a valid output socket. It can be:
        - A Blender Geometry Node Socket
        - An instance of DataSocket
        
        Arguments
        ---------
        - value: the argument to test
        
        Returns
        -------
        bool
        """
        return DataSocket.is_data_socket(value) or isinstance(value, bpy.types.NodeSocket)
    
    @property
    def bl_idname(self):
        """ > Shortcut for `self.bsocket.bl_idname`
        """
        return self.bsocket.bl_socket_idname if isinstance(self.bsocket, bpy.types.NodeSocketInterfaceGeometry) else self.bsocket.bl_idname
    
    @property
    def name(self):
        """ > Shortcut for `self.bsocket.name`
        """
        return self.bsocket.name
        
    @property
    def is_output(self):
        """ > Shortcut for `self.bsocket.is_output`
        """
        return self.bsocket.is_output
    
    @property
    def is_multi_input(self):
        """ > Shortcut for `self.bsocket.is_multi_output`
        """
        return self.bsocket.is_multi_output
    
    @property
    def links(self):
        """ > Shortcut for `self.bsocket.links`
        """
        return self.bsocket.links

    @property
    def bnode(self):
        """ > Shortcut for `self.bsocket.node`
        """
        return self.bsocket.node
    
    @property
    def node_chain_label(self):
        """ > Shortcut for `self.node.chain_label`
        
        _chain_label_ property is the name to be used when automatically naming nodes.
        """
        if self.node is None:
            return ""
        else:
            return self.node.chain_label
    
    @property
    def socket_index(self):
        """ > Return the index of the socket within the list of node sockets.
        
        Depending on the _is_output_ property, the socket belongs either to _node.inputs_ or
        _node.outputs_.
        """
        if self.is_output:
            bsockets = self.bnode.outputs
        else:
            bsockets = self.bnode.inputs
            
        for index, bsocket in enumerate(bsockets):
            if self.bsocket == bsocket:
                return index
            
        raise RuntimeError(f"Impossible to find the index of socket {self} of node {self.node}")
        
    def connected_sockets(self):
        """ > Returns the list of DataSocket instances linked to this socket.
        """ 
        sockets = []
        for link in self.links:
            if self.is_output:
                bsocket = link.to_socket
            else:
                bsocket = link.from_socket
            sockets.append(self.node.tree.get_bsocket_wrapper(bsocket))
        return sockets
    
    # ----------------------------------------------------------------------------------------------------
    # Class name from socket bl_idname
    
    @staticmethod
    def domain_data_type(socket):
        """ > Returns the domain to which the socket belongs
        
        The correspondance table is the following:

          - NodeSocketBool : 'BOOLEAN' 
          - NodeSocketInt : 'INT'
          - NodeSocketIntUnsigned : 'INT
          - NodeSocketFloat :'FLOAT'
          - NodeSocketFloatFactor : 'FLOAT'
          - NodeSocketFloatAngle : 'FLOAT' 
          - NodeSocketFloatDistance :'FLOAT' 
          - NodeSocketVector : 'FLOAT_VECTOR'
          - NodeSocketVectorEuler : 'FLOAT_VECTOR'
          - NodeSocketVectorXYZ : 'FLOAT_VECTOR'
          - NodeSocketVectorTranslation : 'FLOAT_VECTOR'
          - NodeSocketColor : 'FLOAT_COLOR' 
          - NodeSocketString : 'FLOAT_COLOR'
        """
        return DataSocket.SOCKET_IDS[socket.bl_idname][2]
    
    # ----------------------------------------------------------------------------------------------------
    # Class name from socket bl_idname
    
    @staticmethod
    def get_class_name(socket, with_sub_class = False):
        """ > Get the DataSocket class name corresponding to the socket type and name.

        The correspondance table is the following:
        
          - NodeSocketBool : 'Boolean'
          - NodeSocketInt : 'Integer' 
          - NodeSocketIntUnsigned : Integer'
          - NodeSocketFloat : 'Float' 
          - NodeSocketFloatFactor : 'Float'
          - NodeSocketFloatAngle : 'Float'
          - NodeSocketFloatDistance : 'Float' 
          - NodeSocketVector : 'Vector'
          - NodeSocketVectorEuler : 'Vector'
          - NodeSocketVectorXYZ : 'Vector' 
          - NodeSocketVectorTranslation : 'Vector'
          - NodeSocketColor : 'Color'
          - NodeSocketString' : 'String'
          - NodeSocketCollection : 'Collection'
          - NodeSocketImage : 'Image'
          - NodeSocketMaterial : 'Material'
          - NodeSocketObject : 'Object'
          - NodeSocketTexture : 'Texture'
          - NodeSocketGeometry : 'Geometry'
            If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve'],
            the name is chosen as the class name.
        """
        bl_idname = socket.bl_idname
        class_name = DataSocket.SOCKET_IDS[bl_idname][0]
        name = socket.name
        
        if class_name == 'Geometry' and name in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve']:
            class_name = name
            
        if with_sub_class:
            return class_name, DataSocket.SOCKET_IDS[bl_idname][1]
        else:
            return class_name
        
    @staticmethod
    def get_bl_idname(class_name):
        """ > Get the node socket bl_idname name from the DataSocket class
        
        Used to create a new group input socket. Called in `DataClass.Input` method to determine
        which socket type must be created.
        
        Note that here the class_name argument accepts additional values which correspond to _sub classes_:
        
          - Unsigned: Integer sub class (NodeSocketIntUnsigned)
          - Factor : Float sub class (NodeSocketFloatFactor)
          - Angle : Float sub class  (NodeSocketFloatAngle)
          - Distance : Float sub class (NodeSocketFloatDistance)
          - Rotation : Vector sub class (NodeSocketVectorEuler)
          - Xyz : Vector sub class (NodeSocketVectorXYZ)
          - Translation : Vector sub class (NodeSocketVectorTranslation)
          
        These additional values allow to enter angle, distance, factor... as group input values.
        
        Arguments
        ---------
          - class_name: str in
            - Boolean
            - Integer, Unsigned
            - Float, Factor, Angle, Distance
            - Vector, Rotation, Xyz, Translation
            - Color
            - String
            - Geometry, Mesh, Points, Instances, Volume, Spline, Curve
            - Image
            - Material
            - Texture
            - Collection
            - Object
            
        Returns
        -------
          str: the name of the socket type
        """
        
        if DataSocket.is_data_socket(class_name):
            class_name = type(class_name).__name__
        
        if class_name in ['Boolean']:
            return 'NodeSocketBool'
        
        
        elif class_name in ['Integer']:
            return 'NodeSocketInt'
        
        elif class_name in ['Unsigned']:
            return 'NodeSocketIntUnsigned'
        
        
        elif class_name in ['Float']:
            return 'NodeSocketFloat'
        
        elif class_name in ['Factor']:
            return 'NodeSocketFloatFactor'
        
        elif class_name in ['Angle']:
            return 'NodeSocketFloatAngle'
        
        elif class_name in ['Distance']:
            return 'NodeSocketFloatDistance'

        
        elif class_name in ['Vector']:
            return 'NodeSocketVector'
        
        elif class_name in ['Rotation']:
            return 'NodeSocketVectorEuler'
        
        elif class_name in ['Xyz']:
            return 'NodeSocketVectorXYZ'
        
        elif class_name in ['Translation']:
            return 'NodeSocketVectorTranslation'

        
        elif class_name in ['Color']:
            return 'NodeSocketColor'
        
        elif class_name in ['String']:
            return 'NodeSocketString'
        
        elif class_name in ['Geometry', 'Mesh', 'Points', 'Instances', 'Volume', 'Curve', 'Spline']:
            return 'NodeSocketGeometry'
        
        elif class_name in ['Image']:
            return 'NodeSocketImage'
        
        elif class_name in ['Material']:
            return 'NodeSocketMaterial'
        
        elif class_name in ['Texture']:
            return 'NodeSocketTexture'
        
        elif class_name in ['Collection']:
            return 'NodeSocketCollection'
        
        elif class_name in ['Object']:
            return 'NodeSocketObject'

    
    # ----------------------------------------------------------------------------------------------------
    # The Blender socket is used to link nodes
    # Rather than accessing it directly, one must use the method get_blender_socket
    # This method can be used to implement specific code before connection
    
    def get_blender_socket(self):
        return self.bsocket
    
    # ----------------------------------------------------------------------------------------------------
    # The DataSocket can have properties
    # Reset the properties to None
    # It is called at initialization time to create the properties
    #
    # class Vector(...):
    #     def __init__(self, ...):
    #         ...
    #         self.reset_properties()
    #         ...
    #
    #     def reset_properties(self):
    #         super().reset_properties()
    #         self.separate_ = None      # Created by property self.seperate() with node SeparateXyz
    
    def reset_properties(self):
        pass
    
    # ----------------------------------------------------------------------------------------------------
    # > Utility changing the output sockets refered by the DataSocket instance
    #
    # Methods are implemented in two modes:
    # - Creation
    # - Transformation
    #
    # In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.
    # In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
    # After the method return, the calling DataSocket instance refers to a new Blender output socket.
    #
    # ```python
    # # 1. Creation mode
    # # 
    # # to_mesh method creates a new mesh from a curve.
    # # The curve instance refers to the same output node socket
    # # We need to get the result of the method in a new variable
    #
    # new_mesh = curve.to_mesh(profile_curve=circle)
    #
    # # 2. Transformation mode
    # #
    # # set_shade_smooth method transformes the mesh.
    # # After the call, the mesh instance refers to the output socket of the
    # # newly created node "Set Shade Smooth". There is no need to get the result
    # # of the method.
    #
    # mesh.set_shade_smooth()
    #
    # # Note that a transformation method returns self and so, the following line
    # # is equivallent:
    #
    # mesh = mesh.set_shade_smooth()
    # ```
    #
    # The stack method changes the socket the instance refers to and reinitialize the
    # properties
    #
    
    def stack(self, node):
        
        self.node    = node
        self.bsocket = node.bnode.outputs[0]
        self.reset_properties()

        #if self.node.label is None:
        #    self.node.label = label
            
        return self

    # ----------------------------------------------------------------------------------------------------
    # Plug (for input sockets only)
    
    @staticmethod
    def plug_bsocket(bsocket, *values):
        """ > Plug the values to the input Blender socket.
        
        This static method is called by the DataClass method `plug(*values)`.
        
        This method is the one which links an output socket of a node to the input
        socket of another one.
        
        Several values or DataSocket instances can be passed in the case the socket is
        multi input.
        
        If the socket is multi input, the plug method is called once per provided value.
        If a value is None, nothing happens.
        
        A not None value can be:
        - either a valid value for the socket (eg: 123 for Integer socket)
        - or an output socket of another Node
            
        When it is a socket, it can be a Blender socker or a DataSocket
        
        Arguments
        ---------
        - bsocket: Geometry Node input socket
        - *values: list of values
          Each value can be an acceptable default value for the socket
          or an output socket 
        """
        
        if bsocket.is_output:
            raise RuntimeError(f"Method 'plug' can only be used with input sockets, not {bsocket}.")
        
        # ---------------------------------------------------------------------------
        # Nothing to plug

        if len(values) == 0:
            return

        # ---------------------------------------------------------------------------
        # If several output sockets to plugn let's loop on the list
        
        if len(values) > 1:
            if not bsocket.is_multi_input:
                raise RuntimeError(f"Input socket {bsocket} is not multi input: impossible to plug multiple sockets: {values}.")
            for v in values:
                DataSocket.plug_bsocket(bsocket, v)
            return
        
        # ---------------------------------------------------------------------------
        # Ok now: only one thing to plug.
        # It can be a value or a socket (or directly a blender output socket)
        
        # ----- Let's suppress the existing links
        
        #if not is_multi_input:
        #    links = [link for link in self.bnode.links]
        #    for link in links:
        #        self.node.tree.links.remove(links) 
        
        value = values[0]
        if value is None:
            return
        
        out_socket = None
        if isinstance(value, bpy.types.NodeSocket):
            out_socket = value
        elif DataSocket.is_data_socket(value):
            # Node is None: particular cases
            if value.node is None:
                if hasattr(value, 'bobject'):        # An object socket not connected to input
                    value = value.bobject
                elif hasattr(value, 'bcollection'):  # Same for colleciton
                    value = value.bcollection
                else:
                    raise RuntimeError("Impossible to plug a socket with a None Node: {value}.")
            else:
                out_socket = value.get_blender_socket()
            
        # ----- It is a value
        # Let's put it in the default_value of the input socket
            
        if out_socket is None:
            
            if bsocket.is_multi_input:
                raise RuntimeError(f"The socket {bsocket} is multi input. Impossible to plug the value {value}.")
                
            # ----- Vector / Color hack: a single value is broadcasted in a triplet
            
            if hasattr(bsocket, 'default_value') and isinstance(bsocket.default_value, (bpy.types.bpy_prop_array, mathutils.Vector)):
                
                if not hasattr(value, '__len__'):
                    value = (value, value, value)
                    
                # ----- Hack : transform a triplet (a, b, c) with a component
                # which is a socket to a Vector
                
                to_vector = False
                for v in value:
                    if isinstance(v, DataSocket):
                        to_vector = True
                        break
                    
                if to_vector:
                    from geonodes import Vector
                    DataSocket.plug_bsocket(bsocket, Vector((value)).bsocket)
                    return
                
            # ----- Socket material hack : replace the name of the material by the material
            
            if isinstance(bsocket, bpy.types.NodeSocketMaterial):
                if type(value) is str:
                    try:
                        value = bpy.data.materials[value]
                    except:
                        raise RuntimeError(f"Material '{value}' not found.")
            
            ok = True
            try:
                bsocket.default_value = value
            except Exception as e:
                msg = str(e)
                ok = False
                
            if not ok:
                raise RuntimeError(f"Impossible to set the default value {value} to socket {bsocket}.\n Error: {msg}")
                
        else:
            Tree.TREE.btree.links.new(bsocket, out_socket, verify_limits=True)
            
            #print(out_socket, bsocket, Tree.TREE.group_output.inputs[0].bsocket)
            
            outs = Tree.TREE.group_output.inputs
            if outs and bsocket == outs[0].bsocket:
                Tree.TREE.arrange()
                
            
    # ----------------------------------------------------------------------------------------------------
    # Plug (for input sockets only)
            
    def plug(self, *values):
        """ > Plug values in the socket (input sockets only)
        
        see [plug_bsocket](#plug_bsocket)
        """
        DataSocket.plug_bsocket(self.bsocket, *values)
        self.node.tree.arrange(False)
        
    # ----------------------------------------------------------------------------------------------------
    # To group output (for output sockets only)
    
    def to_output(self):
        """ > Plug the data socket to the group output
        
        The socket is added to the outputs of the geometry nodes tree.
        
        **Note**: to define a data socket as the result geometry of the node, use `tree.output_geometry = my_geomety`.
        """
        if not self.is_output:
            raise RuntimeError(f"The socket '{str(self)}' is not an output socket. It can't be sent to group output.")
        self.node.tree.group_output.to_output(self, self.name)
        
    # ----------------------------------------------------------------------------------------------------
    # To viewer (for output sockets only)
        
    def to_viewer(self):
        if not self.is_output:
            """ > Link the data socket to the viewer
            
            If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.
            If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
            accordingly.
            """
            raise RuntimeError(f"The socket '{str(self)}' is not an output socket. It can't be connected to the viewer.")
        self.node.tree.to_viewer(self)
    

# =============================================================================================================================
# Nodes tree    

class Tree:
    """ > Wrap a Blender NodeTree
    
    A tree class encapsulates a Blender NodeTree:
        
    ```python
    blender_tree = tree.btree # The Blender NodeTree
    ```
    
    Nodes are created by data sockets methods. In case of an error, the user cas see the state of
    the tree when the script stops.
    
    Creation / closure
    ------------------
    
    Once the tree is completed, the `arrange` method tries to place the nodes in the most readable way.
    Hence, building a tree is made between the two instructions:
    - `tree = Tree(tree_name)` : creation / opening of the Blender NodeTree
    - `tree.close()` : arrange the nodes
    
    It is recommanded to use the `with` syntax:
        
    ```python
    with Tree("Geometry Nodes") as tree:
        # ... nodes creation
    ```
    
    The TREE static property
    ------------------------
    
    The TREE static attribute of class Tree maintains the current active Tree, i.e. the tree into which
    creating the new nodes. There is only one single _open_ tree at a time.
    The method `activate` set the tree as the current one.
    At creation time, a Tree instance becomes the current one.
    
    Layouts
    -------
    
    For clarity, it is possible to put the newly created nodes in a layout. At creation time, one can define
    both the layout label and color. The layout creation makes use of the `with` syntax:
        
    ```python
    with Tree("Geometry Node") as tree:
        
        # Nodes created here are placed directly on the tree background
        
        with tree.layout("Some tricky computation", color="green"):
            
            # Nodes created here are placed in the current layout
            
            with tree.layout("The most difficult part", color="red"):
                
                # Layouts can be imbricated
                
        # Back to standard creation
    ```
    
    Initialization
    --------------
    At initialization time, the existing nodes can be deleted or kept. Use clear=True
    to erase all the existing nodes.
      
    The nodes which are kep are the ones which can not be configured by script, for instance
    the "Float Curve" or "ColorRamp" nodes. These nodes are reused when instancied in the script.
    This allows not to loose nodes tuning.
        
    """
    
    KEEPS = ['GeometryNodeImageTexture', 'GeometryNodeInputMaterial', 'GeometryNodeStringToCurves', 'ShaderNodeFloatCurve',
             'ShaderNodeFloatCurve', 'ShaderNodeValToRGB', 'ShaderNodeVectorCurve', 'FunctionNodeInputColor']
    
    TREE = None
    
    def __init__(self, tree_name, clear=False):
        """ Initialize a new tree
        
        Arguments
        ---------
        - tree_name: str
          the name of the tree. The NodeTree is created if it doesn't exist.
        - clear: bool, default is False
          earase all the existing nodes
        """
        
        if bpy.data.node_groups.get(tree_name) is None:
            bpy.data.node_groups.new(tree_name, type='GeometryNodeTree')

        self.btree = bpy.data.node_groups[tree_name]
        self.btree.links.clear()

        self.old_bnodes = []
        if clear:
            self.btree.nodes.clear()
        else:
            rems = []
            for bnode in self.btree.nodes:
                if bnode.bl_idname in Tree.KEEPS:
                    self.old_bnodes.append(bnode)
                else:
                    rems.append(bnode)
                    
            for bnode in rems:
                self.btree.nodes.remove(bnode)
            del rems
            
        self.nodes  = []
        self.node_id = 0
        self.activate()
        self.auto_arrange = False
        self.capture_attributes = True
        
        # ----- Layouts stack
        
        self.layouts = []
        
        # ----- Input and outputs
        
        self.group_input  = GroupInput()
        self.group_output = GroupOutput()
        
        # ----- Viewer
        
        self.viewer = None
        self.scene_ = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.close()
        
        
    # ----------------------------------------------------------------------------------------------------
    # Get / create a Blender node
        
    def get_bnode(self, bl_idname, label=None):
        """ Get or create a new Blender node in the tree.
        
        At initialization time, some nodes (the ones which can be changed by UX) are kept
        in old_bnodes list. Before creating a new node, this list is scaned to find a node
        of the proper type and the proper label.
        
        Arguments
        ---------
        - bl_idname: str
          A valid node bl_idname
        - label: str, optional
          The label of the node.
        
        Returns
        -------
          A blender Node
        """
        
        found = None

        for bnode in self.old_bnodes:
            if bnode.bl_idname == bl_idname:
                if label is None:
                    found = bnode
                    break
                elif bnode.label == label:
                    found = bnode
                    break

        if found is None:
            bnode = self.btree.nodes.new(bl_idname)
        else:
            bnode = found
            self.old_bnodes.remove(bnode)
        
        if label is not None:
            bnode.label = label
            
        bnode.select = False
        bnode.parent = self.cur_frame
        
        return bnode
                        
        
    def activate(self):
        """ Set this tree as the current one.
        """
        
        Tree.TREE = self
        
    def register_node(self, node):
        """ Register the node passed in argument in the tree.
        
        When registered, a unique id is provided to the node.
        This allows the users to more clearly distinguish the nodes.
        
        Arguments
        ---------
            node: Node
        """
        
        self.node_id += 1
        node.node_id = self.node_id
        self.nodes.append(node)
        return node
    
    # ---------------------------------------------------------------------------
    # Get the node wrapper of a blender node
    
    def get_bnode_wrapper(self, bnode):
        """ Get the Node instance wrapping the Blender node passed in argument.
        
        Arguments
        ---------
        - bnode: Blender node
            
        Returns
        -------
          Node
            
        Raises
        ------
          Error if not found
        """
        
        for node in self.nodes:
            if node.bnode == bnode:
                return node
        raise RuntimeError(f"Impossible to find the wrapper node of Blender node {bnode}.")
            
    def get_bsocket_wrapper(self, bsocket):
        """ Get the DataSocket instance wrapping the Blender socket passed in argument.
        
        Arguments
        ---------
          bsocket: Blender socket
            
        Returns
        -------
          DataSocket
            
        Raises
        ------
          Error if not found
        """
        
        node = self.get_bnode_wrapper(bsocket.node)
        for socket in itertools.chain(node.inputs, node.outputs):
            if socket.bsocket == bsocket:
                return socket
        raise RuntimeError(f"Impossible to find the wrapper socket of Blender socket {bsocket}, of node {node}.")
        
    # ----------------------------------------------------------------------------------------------------
    # Input output interface
    
    @property
    def input_geometry(self):
        """ The group input geometry
        """
        return self.group_input.input_geometry
        
    @property
    def output_geometry(self):
        """ The group output geometry
        """
        return self.group_output.output_geometry
    
    @output_geometry.setter
    def output_geometry(self, value):
        self.group_output.plug(0, value)
        
    def new_input(self, class_name, value=None, name=None, min_value=None, max_value=None, description=""):
        """ Create a new input socket
        
        Don't use it directly, better call `DataSocket.Input(...)`
        """
        return self.group_input.new_socket(class_name=class_name, value=value, name=name, min_value=min_value, max_value=max_value, description=description)
    
    def to_output(self, socket):
        """ Create a new output socket linked to the data class
        
        Don't use it directly, better call `DataSocket.to_output(...)`
        """
        self.group_output.to_output(socket)
        
    # ----------------------------------------------------------------------------------------------------
    # Viewer
    
    def to_viewer(self, geometry=None, socket=None):
        """ Connect a data socket to the viewer
        
        Don't use it directly, better call `DataSocket.to_viewer()`
        
        The `Tree.to_viewer` method reuses the Viewer node if already exists.
        """
        
        if self.viewer is None:
            self.viewer = Viewer()
            
        self.viewer.plug_socket(geometry)
        self.viewer.plug_socket(socket)
        
    # ----------------------------------------------------------------------------------------------------
    # Scene
    
    @property
    def scene(self):
        """ Maintain a single instance of the node "Scene Time""
        """
        if self.scene_ is None:
            self.scene_ = SceneTime()
        return self.scene_
        
    @property
    def frame(self):
        """ The "Scene Time" output socket "frame"
        
        Used for animation:
            
        ```python
        with Tree("Geometry Nodes") as tree:
            height = tree.frame / 10 # a value which is a tenth of the current frame 
        ```
        """
        return self.scene.frame
    
    @property
    def seconds(self):
        """ The "Scene Time" output socket "seconds"
        
        Used for animation:
            
        ```python
        with Tree("Geometry Nodes") as tree:
            time = tree.seconds.sqrt() # a value which is the square root of the time
        ```
        """
        return self.scene.seconds

    # ----------------------------------------------------------------------------------------------------
    # Layouts
    
    @contextmanager
    def layout(self, label="Layout", color="orange"):
        """ Create a new layout where the newly created nodes will be placed
        
        To be used in a `with` block:
            
        ```python
        with tree.layout("My layout"): # Create a layout
            mesh = Mesh.UVSphere() # The node is parented in the layout
            
        mesh.set_shade_smooth() # "Set Shade Smooth" node is created in the tree backrgound
        ```

        """
        
        try:
            layout = Frame(label=label, color=color)
            self.layouts.append(layout)
            yield layout
        finally:
            self.layouts.pop()
            
    @property
    def cur_frame(self):
        """ Get the current layout for the newly created nodes
        """
        if self.layouts:
            return self.layouts[-1].bnode
        else:
            return None
    
    # ----------------------------------------------------------------------------------------------------
    # Check attributes
    
    def check_attributes(self):
        """ > Check the attributes
        
        Input attributes are initialized with a socket owner
        
        When finalizing the tree, we must check that the attribute actually feeds the expectedt geometry.
        If it is not the case, we must insert a "Capture Attribute" node.
        
        The insertion is made with the following algorithm
        
        1. Check if capture is needed
           for each fed node:
           - if the node has an input geometry:
             - if the input geometry is the expected one:
               - ok
             - else
               - insertion is needed
           - else:
             - continue exploration with the nodes fed by this node
        
        2. If insertion is needed
           - Create the capture node
           - Set the proper parameters
           - Input geometry with the owning socket
           - Output geometry to the sockets the owning socket was linked to
           - Output attribute to the sockets the attribute was connected to
        """
        
        
        from geonodes import Geometry
        
        attr_nodes = []
        for node in self.nodes:
            if node.is_attribute:
                attr_nodes.append(node)
                
        for attr_node in attr_nodes:
            
            # ---------------------------------------------------------------------------
            # ----- Check if the fed nodes with geometry input are ok
            
            security  = []
            def check_geo_nodes(node):
                for nd in node.fed_nodes:
                    
                    bsocket = nd.input_geometry_bsocket

                    print("CHECKING", attr_node, nd, '-->', bsocket)

                    if bsocket is None:
                        if nd in security:
                            continue
                        
                            #attr_node.node_color = "red"
                            #node.node_color = "red"
                            #nd.node_color = "red"
                            #raise RuntimeError(f"Error when checking the attribute node {attr_node}, apparently, the tree loops on node {nd} {nd.bnode}")
                        security.append(nd)
                        
                        if not check_geo_nodes(nd):
                            return False
                        
                    else:
                        
                        # ----- Normally one single input
                        
                        for link in bsocket.links:
                            if link.from_socket != attr_node.owning_bsocket:
                                return False
                
                return True
            
                        
            if check_geo_nodes(attr_node):
                continue
            
            # ---------------------------------------------------------------------------
            # ----- A capture node is required
            
            # ----- Store the links to reroute
            
            # Geometry
            
            geo_links  = attr_node.owning_bsocket.links
            
            # Attribute
            
            attr_links   = None
            output_index = 0
            for index, bsocket in enumerate(attr_node.bnode.outputs):
                links = bsocket.links
                if links:
                    if attr_links is not None:
                        self.arrange(True)
                        attr_node.node_color = "red"
                        raise RuntimeError(f"Error when inserting a capture node. The attribute node {attr_node} has several output sockets which are connected.")
                        
                    attr_links   = links
                    output_index = index
                
            if attr_links is None:
                raise RuntimeError("Algo error !")
                
            # ----- Capture node creation in the proper frame
            
            data_type = DataSocket.SOCKET_IDS[attr_node.bnode.outputs[output_index].bl_idname][2]
            
            capt_node = Geometry(attr_node.owning_bsocket).capture_attribute(value=attr_node.outputs[output_index], data_type=data_type, domain=attr_node.domain)
            capt_node.bnode.parent = attr_node.bnode.parent
            
            # ----- Links rerouting
            
            # Geometry
            
            for link in geo_links:
                to_socket = link.to_socket
                self.btree.links.remove(link)
                self.btree.links.new(capt_node.bnode.outputs[0], to_socket)
                
            # Attribute
            
            for index, bsocket in enumerate(capt_node.bnode.outputs):
                if index > 0 and bsocket.enabled:
                    out_bsocket = bsocket
                    break
            
            for link in attr_links:
                to_socket = link.to_socket
                self.btree.links.remove(link)
                self.btree.links.new(out_bsocket, to_socket)
                        
            # ---------------------------------------------------------------------------
            # ----- Done :-)
                        
            self.arrange(False)
     
    
    
    # ----------------------------------------------------------------------------------------------------
    # Arrange the nodes
    
    def arrange(self, force=True):
        """ Arrange the created nodes in the tree background for more lisibility
        """ 
        if self.auto_arrange or force:
            arrange(self.btree.name)    

    # ----------------------------------------------------------------------------------------------------
    # Close the tree
    #
    # Called by __exit__
    
    def close(self):
        """ Call to indicated that the tree is completed and that it can be finalized
        
        Two actions are performed:
        - Insertion of "Capture Attribute" nodes for attributes which require it,
          see [check_attributes](#check_attributes).
        - Nodes arrangement, see [arrange](#arrange)        
        """
        if self.capture_attributes:
            self.check_attributes()
        self.arrange(True)
        
    
# ---------------------------------------------------------------------------
# A Node    

class Node:
    """ The root class for Blender node wrappers.
    
    This class is basically intended to expose its constructor as a way to create
    the associated Geometry Node. In the following example, we create a Node
    supposingly have one single input socket named "geometry"
        
    ```python
    my_node = Node(geometry=value, parameter='PARAM')
    ```
    
    Nodes naming convention
    ----------------------
    
        The Node sub classes are named accoridng their Blender label with a **Camel case** conversion,
        for instance:
            
        - _Set Shade Smooth_ --> SetShadeSmoth
        - _Split Edges_ --> SplitEdges
        _ _Normal_ --> Normal
    
    Sockets naming convention
    -------------------------
    
        The node socket are named after the Blender sockets names with a **snake case** conversion,
        for instance:
            
        - _Geometry_ --> geometry
        - _Mesh 1_ --> mesh_1
        
        For some nodes, (Math node for instance), several sockets can share the same name. In that case, the
        sockets are numbered, starting from 0:
            
        - Value --> value0
        - Value --> value1
    
    Properties
    ----------
        - tree : Tree
          The tree the node bleongs to
        - name : str
          Standard Geometry node name
        - label : str
          User defined label. Can be None
        - bnode : bpy.types.Node
          The actual Blender Geometry node
        - inputs : list
          List of innput sockets
        - outputs : list
          List of output sockets
        - is_attribute : bool
          Indicates that the node is an field attribute
        - bl_idname : str
          The node type name
    """
        
    def __init__(self, bl_idname, name, label=None, node_color=None):
        """ The root class for Blender node wrappers.
        
        The creation tree is read in the static property Tree.TREE.
        
        The blender Node is created by calling the method `tree.get_bnode` method.
        
        Arguments
        ---------
        - bl_idname: str
          A valid node bl_idname
        - name: str
          The node name
        - label: str, optional
          The node label
        - node_color: color, optional
          The node color
        """
        
        self.tree = Tree.TREE
        self.tree.register_node(self)

        self.name    = name
        self.label_  = None
        self.bnode   = self.tree.get_bnode(bl_idname, label)
        self.bnode.name = str(self)
        self.label      = label
        self.node_color = node_color
        

        self.inputs  = [DataSocket(bsocket, node=self) for bsocket in self.bnode.inputs]
        self.outputs = [DataSocket(bsocket, node=self) for bsocket in self.bnode.outputs]
        
        self.is_attribute = False
        
    def __str__(self):
        return f"[{self.get_label()}]"
    
    def __repr__(self):
        s = f"<Node {str(self)}:\n"
        s += "inputs:\n"
        for ds in self.inputs:
            s += f"   {ds.name} {ds.connected_sockets()}"
            if hasattr(ds.bsocket, "default_value"):
                s += f" ({ds.bsocket.default_value})"
            s += "\n"
        s += "outputs:\n"
        for ds in self.outputs:
            s += f"   {ds.name} {ds.connected_sockets()}\n"
        return s + ">"
    
    # ---------------------------------------------------------------------------
    # bl idname
    
    @property
    def bl_idname(self):
        return self.bnode.bl_idname
    
    # ---------------------------------------------------------------------------
    # Node label
    
    def get_label(self):
        """ Build the node label
        
        If the label provided at initialization time is None, the node is labeled by concatening
        its unique id with its standard name.
        """
        return f"{self.node_id:2d} {self.name}" if self.label_ is None else self.label_
    
    @property
    def label(self):
        return self.label_
    
    @label.setter
    def label(self, value):
        self.label_ = value
        self.bnode.label = self.get_label()
        
    # ---------------------------------------------------------------------------
    # Chain label used when labeling chained nodes
    # eg: separate property of Vector is labeled: {chain_label}.separate
        
    @property
    def chain_label(self):
        if self.label is None:
            return str(self.node_id)
        else:
            return self.label
        
    # ---------------------------------------------------------------------------
    # The input geometry socket when exists
    
    @property
    def input_geometry_bsocket(self):
        for bsocket in self.bnode.inputs:
            if bsocket.bl_idname == 'NodeSocketGeometry':
                return bsocket
        return None

    # ---------------------------------------------------------------------------
    # All the fed nodes (nodes connected to one output socket)
    
    @property
    def fed_nodes(self):

        bnodes = []
        for bsocket in self.outputs:
            for link in bsocket.links:
                if link.to_node not in bnodes:
                    bnodes.append(link.to_node)

        nodes = []
        for bnode in bnodes:
            for node in self.tree.nodes:
                if node.bnode == bnode:
                    nodes.append(node)

        return nodes

    
    # ---------------------------------------------------------------------------
    # Node color
    
    @property
    def node_color(self):
        return self.bnode.color
    
    @node_color.setter
    def node_color(self, value):
        if value is None:
            self.bnode.use_custom_color = False
        else:
            self.bnode.use_custom_color = True
            self.bnode.color = colors.color(value)

    # ---------------------------------------------------------------------------
    # Switch input sockets
    
    def switch_input_sockets(self, index0, index1):
        """ Utility method switch the links fo two sockets/
        
        Used when implementing operators
        """
        
        bsock0 = self.bnode.inputs[index0]
        bsock1 = self.bnode.inputs[index1]
        
        links0 = [link for link in bsock0.links]
        links1 = [link for link in bsock1.links]
        
        def0     = bsock0.default_value if hasattr(bsock0, 'default_value') else None
        def1     = bsock1.default_value if hasattr(bsock1, 'default_value') else None
        
        inps0 = [link.from_socket for link in links0]
        inps1 = [link.from_socket for link in links1]
        
        for link in itertools.chain(links0, links1):
            self.tree.btree.links.remove(link)
            
        if hasattr(bsock0, 'default_value') and def1 is not None:
            bsock0.default_value = def1
            
        if hasattr(bsock1, 'default_value') and def0 is not None:
            bsock1.default_value = def0
            
        for inp in inps1:
            self.tree.btree.links.new(inp, bsock0)
        for inp in inps0:
            self.tree.btree.links.new(inp, bsock1)
        

    # ---------------------------------------------------------------------------
    # Sockets plugged to an input socket
    
    def plugged(self, index):
        return self.inputs[index].connected_sockets()
    
    # ---------------------------------------------------------------------------
    # Link an output socket with the input socket of another node
    
    def plug(self, index, *values):
        """ Plug the values to the input socket whose index is provided.
        
        Since an input socket can be multi input, the values argument is a list.
        
        If the socket is multi input, the plug method is called once per provide value.
        If a value is None, nothing happens.
        
        A not None value can be:
        - either a valid valud for the socket (eg: 123 for Integer socket)
        - or an output socket of another Node
            
        When it is a socket, it can be a Blender socker or a DataSocket
        
        Arguments
        ---------
        - index: int
          The index of the input sockets (a valid index for Node.inputs)
        - *values: list of values
          Each value can be an acceptable default value for the socket
          or an output socket 
        """
        
        # ----- Index can be a string
        valids = []
        if type(index) is str:
            for i, bsock in enumerate(self.bnode.inputs):
                
                if bsock.enabled:
                    valids.append((bsock.name, i))
                    if bsock.name.lower() == index.lower():
                        index = i
                        break

        if type(index) is str:
            raise RuntimeError(f"Invalid input socket name '{index}' for node {self}. Valid (names, index) are : {valids}.")
        
        DataSocket.plug_bsocket(self.bnode.inputs[index], *values)
        self.tree.arrange(False)
        
    # ====================================================================================================
    # The node is an attribute
    
    def as_attribute(self, owning_socket, domain='POINT', data_type='FLOAT'):
        """ Indicates that the node is an attribute
        
        An attribute is intended to provide information from a particular geometry.
        
        In Blender, one has to check if he has to use a Capture Node or not.
        
        With geonodes scripting, attributes are considered as properties of geometry.
        At creation time, the Node maintains a reference to the geometry it is an attribute of.
        When closing the tree, all the attributes are check to see if a "Capture Node" must be
        created instead of keeping the single attribute node.
        
        See `Tree.check_attributes` method.
        """
        
        self.is_attribute   = True
        self.owning_bsocket = owning_socket.bsocket
        self.domain         = domain
        
    # ----------------------------------------------------------------------------------------------------
    # List of the nodes which are connected through a GEOMETRY socket
    
    def connected_geometries(self):
        
        def conns(node):
            
            def app(nds, nd):
                if nd not in nds:
                    nds.append(nd)
                    
            geo_nodes = []
            oth_nodes = []
            for socket in node.outputs:
                for link in socket.links:
                    nd = link.to_node
                    if link.to_socket.bl_idname == 'NodeSocketGeometry':
                        app(geo_nodes, nd)
                    else:
                        app(oth_nodes, nd)
                        
            for nd in oth_nodes:
                for n in conns(nd):
                    app(geo_nodes, n)
                    
            return geo_nodes
        
        return conns(self)
        
    # ----------------------------------------------------------------------------------------------------
    # The attribute is "solved" when it feeds capture or transfer attribute
    
    def attribute_is_solved(self):

        solvers = ['GeometryNodeCaptureAttribute', 'GeometryNodeAttributeTransfer']
        geos = self.connected_geometries()
        for node in geos:
            if node.bl_idname not in solvers:
                return False
            
        return True

    # ====================================================================================================
    # Node socket classes will be created in generated modules
    
    @staticmethod
    def Boolean(socket):
        import geonodes as gn
        return gn.Boolean(socket)
    
    @staticmethod
    def Integer(socket):
        import geonodes as gn
        return gn.Integer(socket)
    
    @staticmethod
    def Float(socket):
        import geonodes as gn
        return gn.Float(socket)
    
    @staticmethod
    def Vector(socket):
        import geonodes as gn
        return gn.Vector(socket)
    
    @staticmethod
    def Color(socket):
        import geonodes as gn
        return gn.Color(socket)
    
    @staticmethod
    def String(socket):
        import geonodes as gn
        return gn.String(socket)
    
    @staticmethod
    def Geometry(socket):
        import geonodes as gn
        return gn.Geometry(socket)
    
    @staticmethod
    def Spline(socket):
        import geonodes as gn
        return gn.Spline(socket)
    
    @staticmethod
    def Curve(socket):
        import geonodes as gn
        return gn.Curve(socket)
    
    @staticmethod
    def Mesh(socket):
        import geonodes as gn
        return gn.Mesh(socket)
    
    @staticmethod
    def Points(socket):
        import geonodes as gn
        return gn.Points(socket)
    
    @staticmethod
    def Instances(socket):
        import geonodes as gn
        return gn.Instances(socket)
    
    @staticmethod
    def Volume(socket):
        import geonodes as gn
        return gn.Volume(socket)
    
    @staticmethod
    def Texture(socket):
        import geonodes as gn
        return gn.Texture(socket)
    
    @staticmethod
    def Material(socket):
        import geonodes as gn
        return gn.Material(socket)
    
    @staticmethod
    def Image(socket):
        import geonodes as gn
        return gn.Image(socket)
    
    @staticmethod
    def Collection(socket):
        import geonodes as gn
        return gn.Collection(socket)
    
    @staticmethod
    def Object(socket):
        import geonodes as gn
        return gn.Object(socket)       
    
    @staticmethod
    def DataClass(socket):
        class_name = DataSocket.get_class_name(socket)
        return getattr(Node, class_name)(socket)
        
    
# =============================================================================================================================
# Node groups input and output

class NodeGroup(Node):
    
    # --------------------------------------------------------------------------------
    # Build the input names to avoid duplicates
    
    def update_sock_names(self):
        
        if hasattr(self, 'sock_names'):
            for name in self.sock_names:
                delattr(self, name)
    
        self.sock_names = []
        for bsocket in self.bsockets:
            if bsocket.bl_idname != 'NodeSocketVirtual':
                self.sock_names.append(bsocket.name)
                
        def count_name(name):
            count = 0
            for bsocket in self.bsockets:
                if bsocket.name == name:
                    count += 1
            return count
                    
        def name_order(name, index):
            count = 0
            for i, bsocket in enumerate(self.bsockets):
                if bsocket.name == name:
                    if i == index:
                        return count
                    else:
                        count += 1
                        
        for index in range(len(self.sock_names)):
            name = self.sock_names[index]
            if count_name(name) > 1:
                self.sock_names[index] += str(name_order(name, index))
                
        for i, name in enumerate(self.sock_names):
            setattr(self, name, Node.DataClass(self.bsockets[i]))
            
    # --------------------------------------------------------------------------------
    # Socket index
    
    def socket_index(self, name):
        for i, sock_name in enumerate(self.sock_names):
            if name == sock_name:
                return i
        raise RuntimeError(f"Socket name '{name}' not found in node '{self.label}'. Check homonyms. Available sockets are {self.sock_names}.")
    
    
# ----------------------------------------------------------------------------------------------------
# Node NodeGroupInput for NodeGroupInput

class GroupInput(NodeGroup):
    
    """ > Node 'Group input'
    
    > Note that the **outputs** sockets of this node are the **input** sockets of the group.
    
    The first socket must be a geometry socket: this is the gemetry of the object on which the modifier
    applies. Make sure that this socket exists.
    
    """
    

    def __init__(self):
        
        super().__init__('NodeGroupInput', 'Group Input')
        
        self.bsockets = self.bnode.outputs
        self.update_sock_names()
        
    # --------------------------------------------------------------------------------
    # Default geometry input node

    @property
    def input_geometry(self):
        return Node.Geometry(self.bnode.outputs[0])
    
    # --------------------------------------------------------------------------------
    # Create a new output socket
    
    def new_socket(self, class_name, value=None, name=None, min_value=None, max_value=None, description=""):
        
        if name is None:
            name = class_name
            
        # ----- Look for an existing socket with the proper name
        
        socket    = None
        existing  = False
        for socket_index, bsocket in enumerate(self.bnode.outputs):
            
            # No virtual socket
            if bsocket.bl_idname == 'NodeSocketVirtual':
                continue
            
            cname, subclass = DataSocket.get_class_name(bsocket, True)
            if (cname == class_name or subclass == class_name) and bsocket.name == name:
                
                inp = self.tree.btree.inputs[socket_index]
                
                socket = Node.DataClass(bsocket)
                existing = True
                
                update = False
                
                if min_value is not None and inp.min_value != min_value:
                    inp.min_value = min_value
                    update = True
                if max_value is not None and inp.max_value != max_value:
                    inp.max_value = max_value
                    update = True
                if inp.description != description:
                    inp.description = description
                    update= True
                    
                if update:
                    self.update_sock_names()

                break
            
        # ----- Let's create it
            
        if socket is None:

            new_input = self.tree.btree.inputs.new(type=DataSocket.get_bl_idname(class_name), name=name)
            
            if min_value is not None:
                new_input.min_value = min_value
            if max_value is not None:
                new_input.max_value = max_value
            new_input.description = description
            
            self.update_sock_names()
        
        index  = self.socket_index(name)
        socket = getattr(self, self.sock_names[index])
            
        # ----- Let's set the value
        # Note: if the socket already exists, we don't override it value
        
        if value is not None:
            
            if DataSocket.is_data_socket(value):
                value.plug(socket)
                
            elif not existing:
                
                if class_name == 'Vector' and isinstance(value, (tuple, list)):
                    value = mathutils.Vector(value)
                
                elif class_name == 'Color' and isinstance(value, (tuple, list)):
                    if len(value) == 3:
                        r, g, b = value
                        value = (r, g, b, 1.)
                
                msg = None
                try:
                    self.tree.btree.inputs[index].default_value = value
                    socket.bsocket.default_value = value
                    
                except Exception as e:
                    msg = str(e)
                    
                if msg is not None:
                    raise RuntimeError(f"Impossible to set the default value '{value}' to the group input socket '{name}'.\n {msg}")
                    
                # ---------------------------------------------------------------------------
                # Set the default value to all modifiers using it
                #
                # The tree inputs store the default value of the sockets
                # The values themselves are stored in properties in the object modifiers
                # The modifier property is key by the tree input identifier
                
                for obj in bpy.data.objects:
                    for mod in obj.modifiers:
                        if isinstance(mod, bpy.types.NodesModifier):
                            if mod.node_group == self.tree.btree:
                                mod[new_input.identifier] = value
                                
                    
        # ----- Return the newly created socket
        
        return socket
    
    
            
# ----------------------------------------------------------------------------------------------------
# Node NodeGroupOutput for NodeGroupOutput

class GroupOutput(NodeGroup):
    """ > Node 'Group output'
    
    > Note that the **input** sockets of this node are the **output** sockets of the group.
    
    The first socket must be a geometry: this is the result of the modifier. Make sure that this
    output socket exists.
    
    """
    
    def __init__(self):
        
        super().__init__('NodeGroupOutput', 'Group Output')
        
        self.bsockets = self.bnode.inputs
        self.update_sock_names()
        
        
    # --------------------------------------------------------------------------------
    # Default geometry input node

    @property
    def output_geometry(self):
        return Node.Geometry(self.bnode.inputs[0])
    
    # --------------------------------------------------------------------------------
    # Create a new output socket
    
    def to_output(self, socket, name=None):
        
        class_name, sub_class = DataSocket.get_class_name(socket, True)
        if sub_class != '':
            class_name = sub_class
            
        if name is None:
            name = class_name
            
        # ----- Look for an existing socket with the proper name
        
        for index, bsocket in enumerate(self.bnode.inputs):
            
            #print("TO OUTPUT", index, bsocket.name, bsocket.bl_idname, 'look for', socket, class_name, sub_class, socket.bl_idname)
            if bsocket.bl_idname != socket.bl_idname:
                continue
            
            #if bsocket.bl_idname == 'NodeSocketVirtual':
            #    continue
                
            #cname, subclass = DataSocket.get_class_name(bsocket, True)
            #if (cname == class_name or subclass == class_name) and bsocket.name == name:
            if bsocket.name == name:
                self.plug(index, socket)
                self.tree.arrange(True)
                return

        # ----- Let's create it
        
        bsocket = self.tree.btree.outputs.new(type=DataSocket.get_bl_idname(class_name), name=name)
        self.update_sock_names()
        
        index  = self.socket_index(name)
        self.plug(index, socket)
        
        self.tree.arrange(True) 

        
# ----------------------------------------------------------------------------------------------------
# Node NodeViewer for GeometryNodeViewer

class Viewer(Node):
    """ > Node 'Viewer' (GeometryNodeViewer)

    Data type dependant sockets
    ---------------------------

        - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets     : ['value']

    Input sockets
    -------------
        - geometry        : Geometry
        - value           : data_type dependant

    Parameters
    ----------
        - data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']

    """

    def __init__(self, geometry=None, value=None, data_type='FLOAT', label=None):

        super().__init__('GeometryNodeViewer', name='Viewer', label=label)

        # Parameters

        self.bnode.data_type       = data_type

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, value)
        elif data_type == 'INT':
            self.plug(4, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(2, value)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, value)
        elif data_type == 'BOOLEAN':
            self.plug(5, value)

        self.plug(0, geometry)


        self.output_sockets  = {}     
        
    def plug_socket(self, socket):
        
        if socket is None:
            return
        
        class_name = DataSocket.get_class_name(socket, False)
        
        if class_name == 'Geometry':
            self.plug(0, socket)

        elif class_name == 'Boolean':
            self.bnode.data_type = 'BOOLEAN'
            self.plug(5, socket)
            
        elif class_name == 'Integer':
            self.bnode.data_type = 'INT'
            self.plug(4, socket)
            
        elif class_name == 'Float':
            self.bnode.data_type = 'FLOAT'
            self.plug(1, socket)
            
        elif class_name == 'Vector':
            self.bnode.data_type = 'FLOAT_VECTOR'
            self.plug(2, socket)
            
        elif class_name == 'Color':
            self.bnode.data_type = 'FLOAT_COLOR'
            self.plug(3, socket)
            
        else:
            raise RuntimeError(f"Impossible to connect the socket {socket} to the viewer. Class {class_name} is not viewable.")
            
        self.tree.arrange(False)
        
# ----------------------------------------------------------------------------------------------------
# Node NodeFrame for NodeFrame

class Frame(Node):

    """ > Node 'Frame' (NodeFrame)
    """

    def __init__(self, label="Layout", label_size=42, color=colors.orange, shrink=True):
        """ > Initialization
        
        Parameters
        ----------
            - label : str, default="Layout"
                  frame label
            - label_size : int, default=42
                  label font size
            - color: color
                  color specification
            - shrink: bool
                  Node parameter
        """

        super().__init__('NodeFrame', name='Frame', label=label)
        self.node_color = color

        # Parameters

        self.bnode.label_size      = label_size
        self.bnode.shrink          = shrink

        self.output_sockets  = {}
        
    @property
    def label_size(self):
        return self.bnode.label_size

    @label_size.setter
    def label_size(self, value):
        self.bnode.label_size = value

    @property
    def shrink(self):
        return self.bnode.shrink

    @shrink.setter
    def shrink(self, value):
        self.bnode.shrink = value
        
# ----------------------------------------------------------------------------------------------------
# Scene

class SceneTime(Node):

    """ > Node 'Scene Time' (GeometryNodeInputSceneTime)

    Output sockets
    --------------
        - seconds         : Float
        - frame           : Float
    """

    def __init__(self, label=None):
        """ Iniitialisation """

        super().__init__('GeometryNodeInputSceneTime', name='Scene Time', label=label)
        # Output sockets

        self.seconds         = self.Float(self.bnode.outputs[0])
        self.frame           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'seconds': self.seconds, 'frame': self.frame}
        
        
    
    
        