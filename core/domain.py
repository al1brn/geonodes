#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:57:33 2022

@author: alain
"""

from geonodes.core.socket import Socket
from geonodes.core.node import Node
from geonodes.nodes import nodes
from geonodes.nodes.nodes import create_node


import logging
logger = logging.getLogger('geonodes')

# =============================================================================================================================
# Domain selector
#
# Domain uses selector property which can be used to get the selection or the index
# - selection: selector.selection
# - index:     selector.index

class Selector:
    
    def __init__(self, domain, value):
        self.domain     = domain
        self.value      = value
        self._selection = None
        
    def __repr__(self):
        return str(self.value)
        
    @property
    def is_index(self):
        return isinstance(self.value, int) or Socket.is_socket(self.value)
            
    @property
    def index(self):
        
        if self.value is None:
            raise Exception(f"{self} index error: the selection is not an Integer. Use {type(self).__name__}[Integer] to have a valid index.")
            #return self.domain.domain_index

        # ----- Index is an int or a socket (different from Boolean addressed above)
        
        elif self.is_index:
            return self.value
        
        else:
            raise Exception(f"Invalid domain index: {self.value}. Only Int is a valid type to get an index from domain[value].")
            
    @property
    def selection(self):
        
        import geonodes as gn
        
        if self.value is None:
            return True
        
        # ----- Index is a boolean
        
        elif isinstance(self.value, (bool, gn.Boolean)):
            return self.value

        # ----- Index is an int or a socket (different from Boolean addressed above)
        
        elif isinstance(self.value, int) or Socket.is_socket(self.value):
            return self.domain.domain_index.equal(self.value)

        # ----- Index is slice
        
        elif isinstance(self.value, slice):
            if self.value.start is None:
                return self.domain.domain_index.less_equal(self.value.stop)
            
            elif self.value.stop is None:
                return self.domain.domain_index.greater_equal(self.value.start)
            
            else:
                center = (self.value.start + self.value.stop - 1)/2
                amp    = (self.value.stop - self.value.start - 1)/2
                return gn.Float(self.domain.domain_index).equal(center, epsilon=amp+0.1)
            
        # ----- Index is an array of indices
        
        elif hasattr(self.value, '__len__'):
            sel = None
            for i in self.value[:10]:
                if sel is None:
                    sel = self.domain.domain_index.equal(i)
                else:
                    sel = sel.b_or(self.domain.domain_index.equal(i))
            return sel
        
        else:
            msg = f"Invalid domain index: {self.value}. Only bool, int, slice and array are valid."
            if hasattr(self.value, 'is_Node'):
                msg += f"\nThe value is a Node, you certainly want to use one output socket in {list(self.value.outsockets.keys())}."
                
            raise Exception(msg)
            
# =============================================================================================================================
# Weighted list
# 
# Implement nodes (index, weights, sorted_index) --> (index, total) as list
#
# - domain     : the calling domain
# - node       : the node
# - out_domain : domain class returned
# - sorted_index_socket : name of sorted_index socket
# - index_socket        : index of the output socket Index
# - total_socket        : index of the output socket Total

class WeightedList:
    
    def __init__(self, domain, node_class, weights=None, out_domain=None, sorted_index_socket="sort_index", index_socket=0, total_socket=1):

        self.domain       = domain
        
        self.node_class   = node_class
        self.weights      = weights
        
        self.out_domain   = out_domain

        self.sorted_index_socket = sorted_index_socket

        self.index_socket = index_socket
        self.total_socket = total_socket
        
        self.nodes   = [(self.build_node(), None)]
        self.weights = weights
        
    def build_node(self, sort_index=None):
        return self.domain.attribute(self.node_class(self.domain.index, weights=self.weights, sort_index=sort_index))
        
    def __len__(self):
        return self.nodes[0][0].get_datasocket(self.total_socket)
    
    def __getitem__(self, index):
        
        node = None
        for nd, idx in self.nodes:
            if idx == index:
                node = nd
                break
                
        if node is None:
            if self.nodes[0][1] is None:
                node = self.nodes[0][0]
                node.set_input_socket(self.sorted_index_socket, index)
                self.nodes[0] = (node, index)

            else:
                node = self.build_node(index)
                self.nodes.append((node, index))
                
        #self.node.set_input_socket(self.sorted_index_socket, index)

        domain_index = node.get_datasocket(self.index_socket)
        
        if self.out_domain is None:
            return domain_index
        else:
            return self.out_domain(self.domain.data_socket, selection=domain_index)


# =============================================================================================================================
# Root class for domains
#    
# Fields are properties of domains.
#   
# Components and domains
# ----------------------
#
# - Mesh component
#     - Point   : point (or points, verts)
#     - Edge    : edge  (or edges)
#     - Face    : face  (or faces)
#     - Corner  : face_corner (or corner or corners)
# - Curve component
#     - Point   : point (or points)
#     - Spline  : spline (or splines)
# - Points
#     - Point   : point (or points)
# - Instances components
#     - Instance : instances (or insts)
#
# POINT domain is share between Mesh, Curve and Points but has not the same methods
#
# The inheritance diagram is the following:
#
# - Interfaces
#   - PointInterface      : common to points : Vertex, ControlPoint and CloudPoint
#   - MeshInterface       : common to all mesh domains: Vertex, Edge, Face, Corner
#   - PEFInterface        : common to Mesh domains except Corner: Vertex, Edge and Face
#
# - Classes
#   - Domain
#     - Vertex          : POINT
#     - Edge            : EDGE
#     - Face            : FACE
#     - Corner          : CORNER
#     - ControlPoint    : POINT
#     - Spline          : CURVE
#     - CloudPoint      : POINT
#     - Instance        : INSTANCE


class Domain:
    """ Root class for domains
    
    Args:
        data_socket (DataSocket): The geometry the domain belongs to
        domain (str): Domain in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
        selection (Boolean): selection input socket
    
        
    Components and domains:
        - Mesh component
            - verts   : Vertex
            - edges   : Edge
            - faces   : Face
            - corners : Corner
            
        - Curve component
            - points  : ControlPoint
            - splines : Spline
            
        - Points
            - points   : CloudPoint
            
        - Instances components
           - insts : Instance
           
    """
    
    def __init__(self, data_socket, selection=None):
        self._data_socket = data_socket
        self.selector     = None if selection is None else Selector(self, selection)
        
    @classmethod
    @property
    def domain(cls):
        return {
            'Domain'        : None,
            'Vertex'        : 'POINT',
            'Edge'          : 'EDGE',
            'Face'          : 'FACE',
            'Corner'        : 'CORNER',
            'ControlPoint'  : 'POINT',
            'Spline'        : 'CURVE',
            'CloudPoint'    : 'POINT',
            'Instance'      : 'INSTANCE',
            }[cls.__name__]
        
    # ----------------------------------------------------------------------------------------------------
    # Data socket
    
    @property
    def data_socket(self):
        return self if self._data_socket is None else self._data_socket
        
    # ----------------------------------------------------------------------------------------------------
    # Return bool selection
        
    @property
    def selection(self):
        return None if self.selector is None else self.selector.selection
    
    @property
    def selection_index(self):
        return None if self.selector is None else self.selector.index
    
    # ----------------------------------------------------------------------------------------------------
    # Select domain either by a bool or by int(s)
    
    @staticmethod
    def value_data_type(socket, default=None):
        return self.data_socket.value_data_type(socket, default=default)

    # ----------------------------------------------------------------------------------------------------
    # Select domain either by a bool or by int(s)
        
    def select(self, selection):
        """ Select the domain
        
        Args:
            selection (Boolean or Integer): The selection condition
        
        If a selection is existing, the resulting selection is a logical and betwenn the two
        """
        
        if self.selector is None:
            sel = selection
            
        elif selection is None:
            sel = self.selector.value
            
        else:
            other = Selector(self, selection)
            sel = self.selector.selection.b_and(other.selection)
            
        return type(self)(self.data_socket, selection=sel)
    
    # ----------------------------------------------------------------------------------------------------
    # Representation
    
    def __repr__(self):
        sel = "" if self.selector is None else f" [{self.selector}]"
        return f"[Domain {self.domain} of {self.data_socket}{sel}]"
    
    # ----------------------------------------------------------------------------------------------------
    # Reset the cache
    
    def reset_cache(self):
        
        cache = set()
        for name in dir(self):
            if name[:3] == '_c_':
                cache.add(name)
                
        for name in cache:
            delattr(self, name)
    
    # ----------------------------------------------------------------------------------------------------
    # Stack
    
    def socket_stack(self, node):
        """ Make the owning socket jump to the output socket of the node passed in argumment.
        
        Args:
            node (Node): The node to jump to
        """
        self.reset_cache()
        return self.data_socket.stack(node)
    
    # ----------------------------------------------------------------------------------------------------
    # Def a node as attribute node
    
    def attribute_node(self, node):
        """ Define an input node as attribute
        
        Args:
            node (Node): The node created by the domain
            
        Returns:
            The node argument
        
        Called when creating an input node in a property getter. Performs two actions:
            
            - Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
              This will allow the :func:`Tree.check_attributes` to see if it is necessary to create
              a *Capture Attribute* for this field.
            - Set the nde property :attr:`field_of` to self in order to implement the transfer attribute
              mechanism.
        """

        node.as_attribute(owning_socket=self.data_socket, domain=self.domain)
        node.field_of = self
        return node    

    # ----------------------------------------------------------------------------------------------------
    # Access by index
    
    def __getitem__(self, index):
        
        if True:
            return self.select(index)
        
        else:
            import geonodes as gn
            
            # ----- Index is a boolean
            # We plug it directly
            
            if isinstance(index, (bool, gn.Boolean)):
                return self.select(index)
    
            # ----- Index is an int or a socket (different from Boolean addressed above)
            # We plug it directly
            
            elif isinstance(index, int) or Socket.is_socket(index):
                return self.select(self.index.equal(index))
    
            # ----- Index is slice
            
            elif isinstance(index, slice):
                if index.start is None:
                    return self.select(self.index.less_equal(index.stop))
                
                elif index.stop is None:
                    return self.select(self.index.greater_equal(index.start))
                
                else:
                    center = (index.start + index.stop - 1)/2
                    amp    = (index.stop - index.start - 1)/2
                    return self.select(gn.Float(self.index).equal(center, epsilon=amp+0.1))
                
            # ----- Index is an array of indices
            
            elif hasattr(index, '__len__'):
                sel = None
                for i in index[:10]:
                    if sel is None:
                        sel = self.index.equal(i)
                    else:
                        sel = sel.b_or(self.index.equal(i))
                return self.select(sel)
            
            else:
                raise Exception(f"Invalid domain index: {index}. Only bool, int, slice and array are valid.")
            
    # ----------------------------------------------------------------------------------------------------
    # To viewer
    
    def view(self, socket=None, label=None, node_color=None):
        """ To viewer.
        
        Args:
            socket (DataSocket): The value to view        
        """
        return self.data_socket.node.tree.view(geometry=self.data_socket, socket=socket, domain=self.domain, label=label, node_color=node_color)
    
    # ----------------------------------------------------------------------------------------------------
    # Force a domain change
    #
    # For instance, it can be used to manage the faces of instances of meshes
    
    @property
    def as_verts(self):
        """ Type cast to Vertex."""
        return Vertex(self.data_socket)
        
    @property
    def as_edges(self):
        """ Type cast to Edge."""
        return Edge(self.data_socket)
        
    @property
    def as_faces(self):
        """ Type cast to Face."""
        return Face(self.data_socket)
        
    @property
    def as_corners(self):
        """ Type cast to Corner."""
        return Corner(self.data_socket)
        
    @property
    def as_control_points(self):
        """ Type cast to ControlPoint."""
        return ControlPoint(self.data_socket)

    @property
    def as_splines(self):
        """ Type cast to Spline."""
        return Spline(self.data_socket)
        
    @property
    def as_cloud_points(self):
        """ Type cast to CloudPoint."""
        return CloudPoint(self.data_socket)
        
    @property
    def as_insts(self):
        """ Type cast to Instance."""
        return Instance(self.data_socket)
    

    
    


    