#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket, Node
from geonodes.nodes import nodes
from geonodes.nodes.nodes import create_node
import geonodes.core.field as field


import logging
logger = logging.getLogger('geonodes')


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
#     - Instance : instans (or insts)
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
    
    def __init__(self, data_socket, domain, selection=None):

        self.data_socket = data_socket
        self.domain      = domain
        self.selection   = selection
        self.init_cache()
        
    def init_cache(self):
        self.ID_       = None
        self.index_    = None
        self.position_ = None
        
        self.named_fields = {}
        
    def select(self, selection):
        if self.selection is None:
            sel = selection
        elif selection is None:
            sel = self.selection
        else:
            sel = self.selection.b_and(selection)
        return type(self)(self.data_socket, selection=sel)
    
    def __call__(self, selection):
        return self.select(selection)
    
    def __repr__(self):
        sel = "" if self.selection is None else f" (selection: {self.selection})"
        #return f"[Domain {self.data_socket}.{self.domain}{sel}]"
        return f"[Domain {self.domain} of {self.data_socket}{sel}]"
    
    def stack(self, node):
        return self.data_socket.stack(node)

    # ----------------------------------------------------------------------------------------------------
    # Access by index
    
    def __getitem__(self, index):
        
        import geonodes as gn
        
        if isinstance(index, int) or Socket.is_socket(index):
            return self.select(self.index.equal(index))
        
        elif isinstance(index, slice):
            if index.start is None:
                return self.select(self.index.less_equal(index.stop))
            
            elif index.stop is None:
                return self.select(self.index.greater_equal(index.start))
            
            else:
                center = (index.start + index.stop - 1)/2
                amp    = (index.stop - index.start - 1)/2
                return self.select(gn.Float(self.index).equal(center, epsilon=amp+0.1))
            
        elif hasattr(index, '__len__'):
            sel = None
            for i in index[:10]:
                if sel is None:
                    sel = self.index.equal(i)
                else:
                    sel = sel.b_or(self.index.equal(i))
            return self.select(sel)
        
        else:
            raise Exceptionf(f"Invalid geometry index: {index}. Only ints, slices and arrays are valid.")
            
    
    # ----------------------------------------------------------------------------------------------------
    # Force a domain change
    #
    # For instance, it can be used to manage the faces of instances of meshes
    
    @property
    def as_verts(self):
        return Vertex(self.data_socket)
        
    @property
    def as_edges(self):
        return Edge(self.data_socket)
        
    @property
    def as_faces(self):
        return Face(self.data_socket)
        
    @property
    def as_corners(self):
        return Corner(self.data_socket)
        
    @property
    def as_control_points(self):
        return ControlPoint(self.data_socket)

    @property
    def as_splines(self):
        return Spline(self.data_socket)
        
    @property
    def as_cloud_points(self):
        return CloudPoint(self.data_socket)
        
    @property
    def as_insts(self):
        return Instance(self.data_socket)
    
    # ----------------------------------------------------------------------------------------------------
    # Statistics
    
    def statistic(self, attribute, data_type=None):
        """ <method GeometryNodeAttributeStatistic>
        """
        dt = Socket.domain_data_type(attribute) if data_type is None else Socket.domain_data_type(data_type)
        if dt in ['BOOLEAN', 'INT', 'COLOR']:
            dt = 'FLOAT'
        
        return nodes.AttributeStatistic(self.data_socket, selection=self.selection, attribute=attribute, data_type=dt, domain=self.domain)
    
    @property
    def count(self):
        import geonodes as gn
        with self.data_socket.node.tree.layout(f"{self}.count", color='UTIL'):
            count = gn.Integer(self.statistic(self.index).max + 1)
            count.node.label = "count"
            return count
    
    # ----------------------------------------------------------------------------------------------------
    # Transfer attribute

    def transfer_attribute(self, attribute, source_position=None, index=None, data_type=None, mapping=None):
        """ <method GeometryNodeAttributeTransfer>
        
        mapping in ('NEAREST', 'INDEX'):
        - NEAREST if index is None
        - INDEX otherwise
        
        call transfer_attribute_interpolated for NEAREST_FACE_INTERPOLATED
        """
        dt = Socket.domain_data_type(attribute) if data_type is None else Socket.domain_data_type(data_type)
        
        # NEAREST_FACE_INTERPOLATED in a dedicated method
        
        if mapping is None:
            if index is None:
                mapping = 'NEAREST'
            else:
                mapping = 'INDEX'
        
        return nodes.TransferAttribute(self.data_socket, attribute=attribute, source_position=source_position, index=index, data_type=dt, domain=self.domain, mapping=mapping).attribute

    def transfer_index(self, attribute):
        """ <method GeometryNodeAttributeTransfer>
        
        call transfer_attribute
        """
        return self.transfer_attribute(attribute, index=self.index, mapping='INDEX')

    def transfer_nearest(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        call transfer_attribute
        """
        return self.transfer_attribute(attribute, source_position=source_position, mapping='NEAREST')

    def transfer_nearest_face(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        call transfer_attribute
        """
        return self.transfer_attribute(attribute, source_position=source_position, mapping='NEAREST_FACE_INTERPOLATED')

    # ----------------------------------------------------------------------------------------------------
    # > Named field
    #
    # Exposed methods are get_named_attribute and set_named_attribute to be closed to the name of the nodes
    # These methods use the named_field method (not named named_attribute to avoid misusing).
    # 
    # named_field creates an instance of NamedField and store it in a dedciated dictionnary
    #
    # Raise an error if different data types are used for the same name
        
    def named_field(self, name, data_type):

        nfield = self.named_fields.get(name)

        if nfield is None:
            nfield = field.NamedField(self, name, data_type=data_type)
            self.named_fields[name] = nfield
            return nfield
        
        if data_type is not None:
            if nfield.data_type is None:
                nfield.data_type = data_type

            elif nfield.data_type != data_type:
                raise RuntimeError(f"The named attribute '{name}' is defined with two different data types: '{nfield.data_type}' (first) and '{data_type}' (second).")
                
        return nfield
    
    # ----------------------------------------------------------------------------------------------------
    # Def a node as attribute node
    
    def attribute(self, node):
        """ Define an input node as attribute
        
        Called when creating an input node in a property getter.
        Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
        
        This will allow the :func:`Tree.check_attributes` to see if it is necessary
        to create a *Capture Attribute* for this field.
        """

        node.as_attribute(owning_socket=self.data_socket, domain=self.domain)
        node.field_of = self
        return node
    

    # ----------------------------------------------------------------------------------------------------
    # > Get a named attribute socket
    #
    # Make use named_field method
    
    def get_named_attribute(self, name, data_type='FLOAT'):
        """ Get a named attribute
        
        Called by methods set_named_xxx:
            
        - :func:`get_named_boolean`
        - :func:`get_named_integer`
        - :func:`get_named_float`
        - :func:`get_named_vector`
        - :func:`get_named_color`
        """
        
        if data_type is None:
            raise RuntimeError(f"Data type for named attribute '{name}' not defined")
            
        return self.attribute(nodes.NamedAttribute(name=name, data_type=data_type)).get_datasocket(0)
    
    
        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD
    
        
        return self.named_field(name, data_type).node_socket
        
    # ----------------------------------------------------------------------------------------------------
    # > Set a named attribute socket
    #
    # Make use named_field method
    #
    # If data_type is None, the data_type is infered from the type of the value
    
    def set_named_attribute(self, name, value, data_type=None):
        """ Set a named attribute
        
        Called by classes set_named_xxx:
            
        - :func:`set_named_boolean`
        - :func:`set_named_integer`
        - :func:`set_named_float`
        - :func:`set_named_vector`
        - :func:`set_named_color`
        - :func:`set_named_byte_color`
        """
        
        if data_type is None:
            data_type = Socket.domain_data_type(value)
        
        return self.stack(nodes.StoreNamedAttribute(self.data_socket, name=name, value=value, data_type=data_type, domain=self.domain))
        

        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD

        self.named_field(name, data_type).set_value(value)

    def get_named_boolean(self, name):
        """ Get named attribute of type BOOLEAN"""
        return self.get_named_attribute(name, data_type='BOOLEAN')

    def get_named_integer(self, name):
        """ Get named attribute of type INT"""
        return self.get_named_attribute(name, data_type='INT')
        
    def get_named_float(self, name):
        """ Get named attribute of type FLOAT"""
        return self.get_named_attribute(name, data_type='FLOAT')

    def get_named_vector(self, name):
        """ Get named attribute of type FLOAT_VECTOR"""
        return self.get_named_attribute(name, data_type='FLOAT_VECTOR')
        
    def get_named_color(self, name):
        """ Get named attribute of type FLOAT_COLOR"""
        return self.get_named_attribute(name, data_type='FLOAT_COLOR')
        
    # NOT SUPPORTED YET
    #def get_named_byte_color(self, name):
    #    return self.get_named_attribute(name, data_type='BYTE_COLOR')
    
    
    def set_named_boolean(self, name, value):
        """ Set named attribute of type BOOLEAN"""
        self.set_named_attribute(name, value, data_type='BOOLEAN')

    def set_named_integer(self, name, value):
        """ Set named attribute of type INT"""
        self.set_named_attribute(name, value, data_type='INT')
        
    def set_named_float(self, name, value):
        """ Set named attribute of type FLOAT"""
        self.set_named_attribute(name, value, data_type='FLOAT')

    def set_named_vector(self, name, value):
        """ Set named attribute of type FLOAT_VECTOR"""
        self.set_named_attribute(name, value, data_type='FLOAT_VECTOR')
        
    def set_named_color(self, name, value):
        """ Set named attribute of type FLOAT_COLOR"""
        self.set_named_attribute(name, value, data_type='FLOAT_COLOR')
        
    def set_named_byte_color(self, name, value):
        """ Set named attribute of type BYTE_COLOR"""
        self.set_named_attribute(name, value, data_type='BYTE_COLOR')
        
    # ====================================================================================================
    # Fields all domain have
        
    @property
    def ID(self):
        """ ID attribute
        
        - setter: :class:`nodes.ID`
        - getter: read only
        - selectable: yes
        """
        
        return self.attribute(nodes.ID()).get_datasocket(0)
        
        
        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD
        
        
        if self.ID_ is None:
            self.ID_ = field.ID(self)
        return self.ID_.node_socket
    
    @ID.setter
    def ID(self, value):
        return self.stack(nodes.SetID(self.data_socket, selection=self.selection, ID=value))
        
        
        
        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD
        
        if self.ID_ is None:
            self.ID_ = field.ID(self)
        self.ID_.set_value(value)
    
    @property
    def index(self):
        """ .. blid:: GeometryNodeInputIndex"""
        
        return self.attribute(nodes.Index()).get_datasocket(0)
        
        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD
        
        if self.index_ is None:
            self.index_ = field.Index(self)
        return self.index_.node_socket
    
    @property
    def position(self):
        """ .. blid:: GeometryNodeInputPosition"""
        
        vector = self.attribute(nodes.Position()).get_datasocket(0)
        
        # ----- Hack to implement += in set_offset

        #vector.offset_setter = lambda value: self.set_position(position=vector, offset=value)
        vector.offset_setter = lambda value: self.stack(nodes.SetPosition(self.data_socket, selection=self.selection, offset=value))
        vector.point_domain  = self
        
        return vector
        
        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD
        
        if self.position_ is None:
            self.position_ = field.Position(self)
        vector = self.position_.node_socket
        
        # By setting the point_domain, += will be implemented in set_position(offset = value)
        # rather that a vector math node incrementing the position
        vector.point_domain = self
        return vector
        
    
    @position.setter
    def position(self, value):
        """ .. blid:: GeometryNodeSetPosition"""
        
        # points.position += vector: __iadd__ return None
        
        if value is None:
            return
        
        # No setter
        
        if self.domain in ['EDGE', 'FACE', 'CORNER']:
            raise Exception(f"The position of edges, faces and corners is read only")
            
        # Let's go
        
        return self.stack(nodes.SetPosition(self.data_socket, selection=self.selection, position=value))
        
        
        
        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD
        
        
        if value is None:  # points.position += vector: __iadd__ return None
            return
        
        if self.domain in ['EDGE', 'FACE', 'CORNER']:
            raise Exception(f"The position of edges, faces and corners is read only")
        if self.position_ is None:
            self.position_ = field.Position(self)
        self.position_.set_value(value)
        
    @property
    def offset(self):
        return Node.Vector(0)
    
    @offset.setter
    def offset(self, value):
        """ .. blid:: GeometryNodeSetPosition"""
        
        # No setter
        
        if self.domain in ['EDGE', 'FACE', 'CORNER']:
            raise Exception(f"The position of edges, faces and corners is read only")
            
        # Let's go
        
        return self.stack(nodes.SetPosition(self.data_socket, selection=self.selection, offset=value))
    
        # -OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD-OLD
        
        """ > Property Point offset setter
        <blid GeometryNodeSetPosition>
        
        Arguments
        ---------
            - value: Vector
        """
        if self.domain in ['EDGE', 'FACE']:
            raise Exception(f"The position of edges and faces is read only")
            
        if self.position_ is None:
            self.position_ = field.Position(self)
            
        self.position_.set_offset(value)
    
    # ====================================================================================================
    # Methods for all domains
    
    def duplicate(self, amount=None):
        """ > Duplicate domain
        
        <blid GeometryNodeDuplicateElements>
        
        Arguments
        ---------
            - amount : Integer
            
        Returns
        -------
            - duplicate index
        """
        node = nodes.DuplicateElements(self.data_socket, self.selection, amount=amount, domain=self.domain)
        self.stack(node)
        return node.duplicate_index
    
    
        
# =============================================================================================================================
# Point interface
#
# Properties and methods shared by all POINT domains:
# - Vertex
# - ControlPoiint
# - CloudPoint

class PointInterface:
    
    def init_point_cache(self):
        pass
    
    def instantiate(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Put instances on points
        
        <blid GeometryNodeInstanceOnPoints>
        
        Arguments
        ---------
            - instance : Geometry
            - pick_instance : Boolean
            - instance_index : Integer
            - rotation : Vector
            - scale : Vector

        Example
        -------        
        
        ```python
        mesh.verts(...).instantiate(...)
        curve.points(...).instantiate(...)
        cloud.points(...).instantiate(...)
        ```
        """
        return nodes.InstanceOnPoints(
                points=self.data_socket, selection=self.selection, 
                instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale
                ).instances
        
# =============================================================================================================================
# Mesh domains
#
# Mesh domains are:
# - Vertex
# - Edge
# - Face
# - Corner
#
# Vertex, Edge and Face share the interface PEFInterface


# -----------------------------------------------------------------------------------------------------------------------------
# Properties and methodes shared by all Mesh domains: Point, Edeg,  Face and Corner

class MeshInterface:
    
    def init_mesh_cache(self):
        self.normal_   = None
    
    @property
    def normal(self):
        if self.normal_ is None:
            self.normal_ = field.Normal(self)
        return self.normal_.node_socket
    
    # ====================================================================================================
    # Methods
    
    def to_points(self, position=None, radius=None):
        """ > Convert to points cloud
        
        <blid GeometryNodeMeshToPoints>
        
        Arguments
        ---------
            - position : Vector
            - radius : Float
            
        Returns
        -------
            - Points
            
        Example
        -------        
        
        ```python
        mesh.verts.to_points(...)
        mesh.edges.to_points(...)
        mesh.faces.to_points(...)
        mesh.corners.to_points(...)
        ```
        
        """
        mode = {'POINT': 'VERTICES', 'EDGE': 'EDGES', 'FACE': 'FACES', 'CORNER': 'CORNERS'}[self.domain]
        return nodes.MeshToPoints(
            mesh=self.data_socket, selection=self.selection, position=position, radius=radius, mode=mode).points

# -----------------------------------------------------------------------------------------------------------------------------
# Properties and methodes shared by Mesh Point, Edge and Face (but not Corner)

class PEFInterface:
    
    def init_PEF_cache(self):
        pass
    
    def delete(self, mode='ALL'):
        """ <method GeometryNodeDeleteGeometry>
        
        mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')        
        
        Example
        -------        
        
        ```python
        mesh.verts(...).delete(mode='ALL')
        mesh.edges(...).delete(mode='EDGE_FACE')
        mesh.faces(...).delete(mode='ONLY_FACE')
        ```
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))
    
    def delete_all(self):
        """ <method GeometryNodeDeleteGeometry>
        
        call delete with mode : 'ALL'
        
        Example
        -------        
        
        ```python
        mesh.verts(...).delete_all()
        mesh.edges(...).delete_all()
        mesh.faces(...).delete_all()
        ```
        """
        return self.delete(mode='ALL')
        
    def delete_faces(self):
        """ <method GeometryNodeDeleteGeometry>
        
        call delete with mode : 'ONLY_FACE'
        
        Example
        -------        
        
        ```python
        mesh.verts(...).delete_faces()
        mesh.edges(...).delete_faces()
        mesh.faces(...).delete_faces()
        ```
        """
        return self.delete(mode='ONLY_FACE')
        
    def delete_edges_faces(self):
        """ <method GeometryNodeDeleteGeometry>
        
        call delete with mode : 'EDGE_FACE'
        
        Example
        -------        
        
        ```python
        mesh.verts(...).delete_edges_faces()
        mesh.edges(...).delete_edges_faces()
        mesh.faces(...).delete_edges_faces()
        ```
        """
        return self.delete(mode='EDGE_FACE')
    
    def proximity(self, source_position=None):
        """ <method GeometryNodeProximity>
        
        Example
        -------        
        
        ```python
        mesh.verts(...).proximity()
        mesh.edges(...).proximity()
        mesh.faces(...).proximity()
        ```
        
        Arguments
        ---------
            - source_position : Vector
            
        Returns
        -------
            - Node with sockets
                - position : Vector
                - distance : Float
        """
        target_element = self.domain + 'S'
        return nodes.GeometryProximity(target=self.data_socket, source_position=source_position, target_element=target_element)
        
    
    def extrude(self, offset=None, offset_scale=None, individual=None):
        """ > Extrusion
        
        <blid GeometryNodeExtrudeMesh>
        
        Arguments
        ---------
            - offset : Vector
            - offset_scale : Float
            - individual : Boolean
            
        Returns
        -------
            - tuple with top and side selections
                            
        Example
        -------        
        
        ```python
         top, side = mesh.verts(...).extrude(...)
         top, side = mesh.edges(...).extrude(...)
         top, side = mesh.faces(...).extrude(...)
         
         # Example of insetting and extruding the faces of a mesh
         
         top, _ = mesh.faces.extrude(offset_scale=0)
         top.scale(0.5)
         top1, _ = top.extrude(top.normal, .3)
         
        ```
        
        """
        mode = {'POINT': 'VERTICES', 'EDGE': 'EDGES', 'FACE': 'FACES'}[self.domain]
        node = nodes.ExtrudeMesh(
            mesh=self.data_socket, selection=self.selection,
            offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)
        self.stack(node)
        return self.select(node.top), self.select(node.side)
    
    def scale(self, scale=None, center=None, axis=None, scale_mode='UNIFORM'):
        """ > Scale a face or an edge
        
        <blid GeometryNodeScaleElements>
        
        scale_uniform and scale_single_axis can be called without the argument scale_mode
        
        Arguments
        ---------
            - scale : Float
            - center : Vector
            - axis : Vector
            - scale_mode : str (default = 'UNIFORM') in ('UNIFORM', 'SINGLE_AXIS')
            
                            
        Example
        -------        
        
        ```python
         mesh.edges(...).scale(...)
         mesh.faces(...).scale(...)
        ```
        
        """
        
        if self.domain == 'POINT':
            raise Exception(f"Vertices are not scalable: scale method can't be called")
        return self.stack(nodes.ScaleElements(
            geometry=self.data_socket, selection=self.selection,
            scale=scale, center=center, axis=axis, domain=self.domain, scale_mode=scale_mode))
        
    def scale_uniform(self, scale=None, center=None):
        """ > Scale a face or an edge in uniform mode
        
        <blid GeometryNodeScaleElements>
        
        call scale with mode='UNIFORM'
        
        
        Arguments
        ---------
            - scale : Float
            - center : Vector
                            
        Example
        -------        
        
        ```python
         mesh.edges(...).scale_uniform(...)
         mesh.faces(...).scale_uniform(...)
        ```
        
        """
        return self.scale(scale=scale, center=center, mode='UNIFORM')
        
    def scale_single_axis(self, scale=None, center=None, axis=None):
        """ > Scale a face or an edge in single axis mode
        
        <blid GeometryNodeScaleElements>
        
        call scale with mode='SINGLE_AXIS'
        
        
        Arguments
        ---------
            - scale : Float
            - center : Vector
            
        Example
        -------        
        
        ```python
         mesh.edges(...).scale_single_axis(...)
         mesh.faces(...).scale_single_axis(...)
        ```
        
        """
        return self.scale(scale=scale, center=center, axis=axis, mode='SINGLE_AXIS')
        
        
    
        
# -----------------------------------------------------------------------------------------------------------------------------
# vertex: the point domain of meshes

class Vertex(Domain, PointInterface, MeshInterface, PEFInterface):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='POINT', selection=selection)
        
    def init_cache(self):
        super().init_cache()
        self.init_point_cache()
        self.init_mesh_cache()
        self.init_PEF_cache()
        
        self.neighbors_ = None
        
    @property
    def neighbors_vertices(self):
        """ > Neighbors vertices
        <blid GeometryNodeInputMeshVertexNeighbors>
        """
        if self.neighbors_ is None:
            self.neighbors_ = field.Neighbors(self)
        return self.neighbors_.input_node.get_datasocket(0)
        
    @property
    def neighbors_faces(self):
        """ > Neighbors faces
        <blid GeometryNodeInputMeshVertexNeighbors>
        """
        if self.neighbors_ is None:
            self.neighbors_ = field.Neighbors(self)
        return self.neighbors_.input_node.get_datasocket(1)
    
    # ====================================================================================================
    # Methods
    
    def merge(self, distance=0.001, mode='ALL'):
        """ > Merge vertices by distance
        
        <blid GeometryNodeMergeByDistance>

        Arguments
        ---------
            - mode : str (default = 'ALL') in ('ALL', 'CONNECTED')        
            - distance : Float
                The merge distance
        Example
        -------        
        
        '''python
        mesh.verts().merge()
        ````
        """
        return self.stack(nodes.MergeByDistance(self.data_socket, selection=self.selection, distance=distance, mode=mode))

    def merge_connected(self, distance=0.001):
        """ > Merge connected vertices by distance
        
        <blid GeometryNodeMergeByDistance>

        Arguments
        ---------
            - distance : Float
                The merge distance

        Example
        -------        
        
        '''python
        mesh.verts().merge_connected()
        ````
        """
        return self.merge(distance=distance, mode='CONNECTED')
        
        
    
        
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Face domain

class Face(Domain, MeshInterface, PEFInterface):

    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='FACE', selection=selection)
        
    def init_cache(self):
        super().init_cache()
        
        self.init_mesh_cache()
        self.init_PEF_cache()

        self.neighbors_      = None
        self.area_           = None
        self.shade_smooth_   = None
        self.island_         = None
        self.material_index_ = None
        
    # ----------------------------------------------------------------------------------------------------
    # Transfer attribute

    def transfer_attribute_interpolated(self, attribute, source_position=None, data_type=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute(attribute, source_position=source_position, data_type=data_type, mapping='NEAREST_FACE_INTERPOLATED')
    
    def transfer_boolean_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='BOOLEAN')
        
    def transfer_integer_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='INT')
        
    def transfer_float_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='FLOAT')
        
    def transfer_vector_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='FLOAT_VECTOR')
        
    def transfer_color_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='FLOAT_COLOR')

    # ----------------------------------------------------------------------------------------------------
    # Fields
        
    @property
    def neighbors_vertices(self):
        if self.neighbors_ is None:
            self.neighbors_ = field.Neighbors(self)
        return self.neighbors_.input_node.get_datasocket(0)
        
    @property
    def neighbors_faces(self):
        if self.neighbors_ is None:
            self.neighbors_ = field.Neighbors(self)
        return self.neighbors_.input_node.get_datasocket(1)
        
    @property
    def area(self):
        """ <field GeometryNodeInputMeshFaceArea>
        
        Property
        
        Returns
        -------
            Float
        """
        if self.area_ is None:
            self.area_ = field.Area(self)
        return self.area_.node_socket
    
    def is_planar(self, threshold=None):
        """ <field GeometryNodeInputMeshFaceIsPlanar>
        
        Method
        
        Arguments
        ---------
            - threshold : Float
        
        Returns
        -------
            Boolean
        """
        
        return field.IsPlanar(threshold=threshold).node_socket

    @property
    def shade_smooth(self):
        if self.shade_smooth_ is None:
            self.shade_smooth_ = field.ShadeSmooth(self)
        return self.shade_smooth_.input_node.node_socket
    
    @shade_smooth.setter
    def shade_smooth(self, value):
        if self.shade_smooth_ is None:
            self.shade_smooth_ = field.ShadeSmooth(self)
        self.shade_smooth_.set_value(value)
        
    @property
    def island_index(self):
        if self.island_ is None:
            self.island_ = field.Island(self)
        self.shade_smooth_.get_datasocket(0)
        
    @property
    def island_count(self):
        if self.island_ is None:
            self.island_ = field.Island(self)
        self.shade_smooth_.get_datasocket(1)
        
    @property
    def material_index(self):
        """ <field GeometryNodeInputMaterialIndex>
        
        Property getter
        
        Returns
        -------
            Integer
        """
        if self.material_index_ is None:
            self.material_index_ = field.MaterialIndex(self)
        return self.material_index_.node_socket
    
    @material_index.setter
    def material_index(self, value):
        """ <field GeometryNodeSetMaterialIndex>
        
        Property setter
        """
        if self.material_index_ is None:
            self.material_index_ = field.MaterialIndex(self)
        self.material_index_.set_value(value)
        
    def set_material(self, material):
        """ > Set a material on the faces
        
        <blid GeometryNodeSetMaterial>
        
        Arguments
        ---------
            - material : material of material name
        
        Example
        -------
        ```python
        mesh.faces.set_material(...)
        ```
        """
        return self.stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material))
    
    @property
    def material(self):
        raise Exception(f"Face.material is a write only property")
        
    @material.setter
    def material(self, value):
        self.set_material(value)
    
    def material_selection(self, material=None):
        """ <field GeometryNodeMaterialSelection>
        
        Method
        
        Arguments
        ---------
            - material : Material or str (material name)
        
        Returns
        -------
            Boolean
        """
        return field.MaterialSelection(self, material=material).node_socket
    
    # ====================================================================================================
    # Methods
    
    def flip(self):
        """ > Flip faces
        
        <blid GeometryNodeFlipFaces>
        
        Example
        -------        
        
        ```python
        mesh.faces.flip()
        ```
        
        """
        return self.stack(nodes.FlipFaces(mesh=self.data_socket, selection=self.selection))
    
    def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ > Triangulate faces
        
        <blid GeometryNodeTriangulate>
        
        Arguments
        ---------
            - minimum_vertices : Integer
            - ngon_method : str (default = 'BEAUTY') in ('BEAUTY', 'CLIP')
            - quad_method : str (default = 'SHORTEST_DIAGONAL') in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')

        Example
        -------        
        
        ```python
        mesh.faces(...).triangulate(...)
        ```
        """
        return self.stack(nodes.Triangulate(
            mesh=self.data_socket, selection=self.selection,
            minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))
    
    def distribute_points(self, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """ > Distribute points on faces
        
        <blid GeometryNodeDistributePointsOnFaces>

        Arguments
        ---------
            - distance_min : Float
            - density_max : Float
            - density : Float
            - density_factor : Float
            - seed : Integer
            - distribute_method : str (default = 'RANDOM') in ('RANDOM', 'POISSON')

        Returns
        -------
        Node with 3 sockets:
            - points : Points
            - normal : Vector
            - rotation : Vector
            
        Example
        -------
        
        ```python
        node = mesh.faces.distribute_points(...)
        cloud = node.points
        normal = node.normal
        rotation = node.rotation
        
        ```
            
        """
        
        return nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection,
                distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor,
                seed=seed, distribute_method=distribute_method)
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Edge domain
        
class Edge(Domain, MeshInterface, PEFInterface):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='EDGE', selection=selection)
        
    def init_cache(self):
        super().init_cache()

        self.init_mesh_cache()
        self.init_PEF_cache()
        
        self.neighbors_ = None
        self.angle_     = None
        self.vertices_  = None
        
    @property
    def neighbors_faces(self):
        """ <field GeometryNodeInputMeshEdgeNeighbors>
        
        Property
        
        Returns
        -------
            Integer
        """
        
        if self.neighbors_ is None:
            self.neighbors_ = field.Neighbors(self)
        return self.neighbors_.input_node.node_socket

    @property
    def unsigned_angle(self):
        """ <field GeometryNodeInputMeshEdgeAngle>
        
        Property

        To get the signed angle, used the property [angle](#angle).
        
        Returns
        -------
            Float
        """
        if self.angle_ is None:
            self.angle_ = field.Angle(self)
        return self.angle_.get_datasocket(0)

    @property
    def angle(self):
        """ <field GeometryNodeInputMeshEdgeAngle>
        
        Property
        
        To get the unsigned angle, used the property [unsigned_angle](#unsigned_angle).
        
        Returns
        -------
            Float
        """
        if self.angle_ is None:
            self.angle_ = field.Angle(self)
        return self.angle_.get_datasocket(1)
    
    @property
    def vertices_index_1(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property

        Sockets can be access individually via:
            
        - [vertices_index_1](#vertices_index_1)
        - [vertices_index_2](#vertices_index_2)
        - [vertices_position_1](#vertices_position_1)
        - [vertices_position_2](#vertices_position_2)
        
        Returns
        -------
            Integer
        """
        if self.vertices_ is None:
            self.vertices_ = field.EdgeVertices(self)
        self.vertices.get_datasocket(0)
    
    @property
    def vertices_index_2(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Sockets can be access individually via:
            
        - [vertices_index_1](#vertices_index_1)
        - [vertices_index_2](#vertices_index_2)
        - [vertices_position_1](#vertices_position_1)
        - [vertices_position_2](#vertices_position_2)
        
        
        Returns
        -------
            Integer
        """
        if self.vertices_ is None:
            self.vertices_ = field.EdgeVertices(self)
        self.vertices.get_datasocket(1)
    
    @property
    def vertices_position_1(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Sockets can be access individually via:
            
        - [vertices_index_1](#vertices_index_1)
        - [vertices_index_2](#vertices_index_2)
        - [vertices_position_1](#vertices_position_1)
        - [vertices_position_2](#vertices_position_2)
        
        
        Returns
        -------
            Integer
        """
        if self.vertices_ is None:
            self.vertices_ = field.EdgeVertices(self)
        self.vertices.get_datasocket(2)
    
    @property
    def vertices_position_2(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Sockets can be access individually via:
            
        - [vertices_index_1](#vertices_index_1)
        - [vertices_index_2](#vertices_index_2)
        - [vertices_position_1](#vertices_position_1)
        - [vertices_position_2](#vertices_position_2)
        
        
        Returns
        -------
            Integer
        """
        if self.vertices_ is None:
            self.vertices_ = field.EdgeVertices(self)
        self.vertices.get_datasocket(2)
        return self.vertices.position_2
    
    # ====================================================================================================
    # Methods
    
    def to_curve(self):
        """ > Convert edges to curve
        
        <blid GeometryNodeMeshToCurve>
        
            
        Example
        -------        
        
        ```python
        mesh.edges.to_curve(...)
        ```
        
        """
        return nodes.MeshToCurve(
            mesh=self.data_socket, selection=self.selection).curve
    
    def split(self):
        """ > Split edges
        
        <blid GeometryNodeSplitEdges>
        
        Example
        -------        
        
        ```python
        mesh.edges.split()
        ```
        
        """
        return self.stack(nodes.SplitEdges(mesh=self.data_socket, selection=self.selectoin))
    
    
    
    
# ---------------------------------------------------------------------------
# Face corner domain

class Corner(Domain, MeshInterface):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='CORNER', selection=selection)
        
    def init_cache(self):
        super().init_cache()

        self.init_mesh_cache()
        
# =============================================================================================================================
# Curve domains

# ----------------------------------------------------------------------------------------------------
# Control point : the point domain of splines

class ControlPoint(Domain, PointInterface):

    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='POINT', selection=selection)
        
    def init_cache(self):
        super().init_cache()

        self.init_point_cache()
        self.handles_ = None
        
    # ----------------------------------------------------------------------------------------------------
    # Handles
        
    # ----- Handles type

    def set_handle_type(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        stype = handle_type.upper()
        valid_types = ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        if not stype in valid_types:
            raise Exception(f"'{handle_type}' is not a valid handle type. Valid types are {valid_types}")
        
        return self.stack(nodes.SetHandleType(curve=self.data_socket, selection=self.selection, handle_type=stype, mode=mode))
    
    @property
    def handle_type(self):
        raise Exception(f"'handle_type' is a write only property")
        
    @handle_type.setter
    def handle_type(self, value):
        """ > Set the handles type
        
        <blid GeometryNodeCurveSetHandles>

        Set the type of the left and right handles
        
        ```python
        curve.splines.type = 'BEZIER'
        curve.points.handle_type = 'FREE'
        ```
        """
        return self.set_handle_type(handle_type=value, mode={'LEFT', 'RIGHT'})
        
    @property
    def left_type(self):
        raise Exception(f"'left_type' is a write only property")
        
    @left_type.setter
    def left_type(self, value):
        """ > Set the left handles type
        
        <blid GeometryNodeCurveSetHandles>

        Set the type of the left handles
        
        ```python
        curve.splines.type = 'BEZIER'
        curve.points.left_type = 'FREE'
        ```
        """
        return self.set_handle_type(handle_type=value, mode={'LEFT'})
        
    @property
    def right_type(self):
        raise Exception(f"'handles_type' is a write only property")
        
    @right_type.setter
    def right_type(self, value):
        """ > Set the right handles type
        
        <blid GeometryNodeCurveSetHandles>

        Set the type of the right handles
        
        ```python
        curve.splines.type = 'BEZIER'
        curve.points.right_type = 'FREE'
        ```
        """
        return self.set_handle_type(handle_type=value, mode={'RIGHT'})

    # ----- Handles position / offset
    
    def handles(self, relative=None, mode={'LEFT', 'RIGHT'}):
        return field.HandlePositions(self, relative=relative, mode=mode)
            
    def lefts(self, relative=None):
        return self.handles(relative=relative, mode={'LEFT'})
            
    def rights(self, relative=None):
        return self.handles(relative=relative, mode={'RIGHT'})
            
    @property
    def left(self):
        vector = self.handles().left
        
        # ----- Hack to implemenet += in offset
        
        vector.point_domain = self
        vector.is_handle    = True
        return vector
    
    @left.setter
    def left(self, value):
        if value is None:
            return
        return self.stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=value, mode='LEFT'))

    @property
    def right(self):
        vector = self.handles().right
        
        # ----- Hack to implemenet += in offset
        
        vector.point_domain = self
        vector.is_handle    = True
        return vector

    @right.setter
    def right(self, value):
        if value is None:
            return
        return self.stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=value, mode='RIGHT'))

    @property
    def relative_left(self):
        return self.handles(relative=True).left
    
    @property
    def relative_right(self):
        return self.handles(relative=True).right

    # ----- Handle selection
    
    def handles_selection(self, handle_type='AUTO', left=True, right=True):
        mode = set()
        if left:  mode.add('LEFT')
        if right: mode.add('RIGHT')
        
        valids = ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        stype = handle_type.upper()
        if stype not in valids:
            raise Exception(f"Points.handles: the handle type '{handle_type}' is not valid. It should be in {valids}.")
        
        return field.HandleTypeSelection(self, handle_type=handle_type, mode=mode).node_socket
    
    @property
    def handle_auto(self):
        return self.handles_selection(handle_type='AUTO')
    
    @property
    def handle_free(self):
        return self.handles_selection(handle_type='FREE')
    
    @property
    def handle_vector(self):
        return self.handles_selection(handle_type='VECTOR')
    
    @property
    def handle_align(self):
        return self.handles_selection(handle_type='ALIGN')
    
    @property
    def left_handle_auto(self):
        return self.handles_selection(handle_type='AUTO', right=False)
    
    @property
    def right_handle_auto(self):
        return self.handles_selection(handle_type='AUTO', left=False)
    
    @property
    def left_handle_free(self):
        return self.handles_selection(handle_type='FREE', right=False)
    
    @property
    def right_handle_free(self):
        return self.handles_selection(handle_type='FREE', left=False)
    
    @property
    def left_handle_vector(self):
        return self.handles_selection(handle_type='VECTOR', right=False)
    
    @property
    def right_handle_vector(self):
        return self.handles_selection(handle_type='VECTOR', left=False)
    
    @property
    def left_handle_align(self):
        return self.handles_selection(handle_type='ALIGN', right=False)
    
    @property
    def right_handle_align(self):
        return self.handles_selection(handle_type='ALIGN', left=False)
    
    
    
    
    
    
    
    
    
    
    
            











    
    @property
    def left_offset(self):
        return Node.Vector(0)
    
    @left_offset.setter
    def left_offset(self, value):
        """ > Property Handle offset setter
        
        <blid GeometryNodeSetCurveHandlePositions>
        
        Arguments
        ---------
            - value: Vector
        """
        return self.stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, offset=value, mode='LEFT'))
    
    @property
    def right_offset(self):
        return Node.Vector(0)
    
    @right_offset.setter
    def right_offset(self, value):
        """ > Property Handle offset setter
        
        <blid GeometryNodeSetCurveHandlePositions>
        
        Arguments
        ---------
            - value: Vector
        """
        return self.stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, offset=value, mode='RIGHT'))
    

    
# ----------------------------------------------------------------------------------------------------
# Spline

class Spline(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='CURVE', selection=selection)
        
    def init_cache(self):
        super().init_cache()
        
        self.radius_     = None
        self.tilt_       = None
        self.cylic_      = None
        self.tangent_    = None
        self.length_     = None
        self.parameter_  = None
        self.resolution_ = None
        
    @property
    def radius(self):
        if self.radius_ is None:
            self.radius_ = field.Radius(self)
        return self.radius_.node_socket
    
    @radius.setter
    def radius(self, value):
        if self.radius_ is None:
            self.radius_ = field.Radius(self)
        self.radius_.set_value(value)
        
        
    @property
    def tilt(self):
        """ <field GeometryNodeInputCurveTilt>
        
        Property
        
        Returns
        -------
            Float
        """
        if self.tilt_ is None:
            self.tilt_ = field.Tilt(self)
        return self.tilt_.node_socket
    
    @tilt.setter
    def tilt(self, value):
        """ <field GeometryNodeSetCurveTilt>
        """
        if self.tilt_ is None:
            self.tilt_ = field.Tilt(self)
        self.tilt_.set_value(value)
    
    @property
    def cyclic(self):
        """ <field GeometryNodeInputSplineCyclic>
        
        Property
        
        Returns
            Boolean
        """
        if self.cylic_ is None:
            self.cylic_ = field.Tilt(self)
        return self.cylic_.input_node.node_socket
    
    @cyclic.setter
    def cyclic(self, value):
        """ <field GeometryNodeSetSplineCyclic>
        """
        if self.cylic_ is None:
            self.cylic_ = field.Tilt(self)
        self.cylic_.set_value(value)
        
    @property
    def tangent(self):
        """ <field GeometryNodeInputTangent>
        
        Property
        
        Returns
        -------
            Vector
        """
        if self.tangent_ is None:
            self.tangent_ = field.CurveTangent(self)
        return self.tangent_.node_socket
    
    @property
    def length(self):
        """ <field GeometryNodeSplineLength>
        
        Property
        
        - **length: Float**
        - _point_count: Integer_
        
        Returns
        -------
            Float
        """                
        if self.length_ is None:
            self.length_ = field.SplineLength(self)
        return self.length_.get_datasocket(0)
    
    @property
    def point_count(self):
        """ <field GeometryNodeSplineLength>
        
        Property
        
        - _length : Float_
        - **point_count : Integer**
                                       
        Returns
        -------
            Integer
        """                
        if self.length_ is None:
            self.length_ = field.SplineLength(self)
        return self.length_.get_datasocket(1)
    
    @property
    def parameter_factor(self):
        """ <field GeometryNodeSplineParameter>
        
        Property
        
        - **factor : Float**
        - _length  : Float_
        - _index : Integer_
                                       
        Returns
        -------
            Float
        """                
        if self.parameter_ is None:
            self.parameter_ = field.SplineParameter(self)
        return self.parameter_.get_datasocket(0)
        
    @property
    def parameter_length(self):
        """ <field GeometryNodeSplineParameter>
        
        Property
        
        - _factor : Float_
        - **length  : Float**
        - _index : Integer_
                                       
        Returns
        -------
            Float
        """                
        if self.parameter_ is None:
            self.parameter_ = field.SplineParameter(self)
        return self.parameter_.get_datasocket(1)
        
    @property
    def parameter_index(self):
        """ <field GeometryNodeSplineParameter>
        
        Property
        
        - _factor : Float_
        - _length  : Float**
        - **index : Integer_
                                       
        Returns
        -------
            Integer
        """                
        if self.parameter_ is None:
            self.parameter_ = field.SplineParameter(self)
        return self.parameter_.get_datasocket(2)
    
    @property
    def resolution(self):
        """ <field GeometryNodeInputSplineResolution>
        
        Property
        
        Returns
            Integer
        """
        if self.resolution_ is None:
            self.resolution_ = field.SplineResolution(self)
        return self.resolution_.node_socket
    
    @resolution.setter
    def resolution(self, value):
        """ <field GeometryNodeSetSplineResolution>
        """
        if self.resolution_ is None:
            self.resolution_ = field.SplineResolution(self)
        return self.resolution_.set_value(value)
    
    
    def endpoint_selection(self, start_size=None, end_size=None):
        """ <field GeometryNodeCurveEndpointSelection>
        
        Method
        
        Arguments
        ---------
            - start_size : Integer
            - end_size : Integer
        
        Returns
        -------
            Float
        """
        return field.EndpointSelection(self, start_size=start_size, end_size=end_size).input_node.node_socket
    
    @property
    def type(self):
        raise Exception(f"'splines.type' property is write only")
    
    @type.setter
    def type(self, value):
        """ > Set the spline type
        
        <blid GeometryNodeCurveSplineType>
        
        """
        valids = ('BEZIER', 'NURBS', 'POLY')
        stype = value.upper()
        if not stype in valids:
            raise Exception(f"{value}' is not a valide splien type. Valide spline types are {valids}")
            
        return self.stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=stype))
        
    def handle_positions(self, relative=None):
        """ <field GeometryNodeInputCurveHandlePositions>
        
        Method
        
        Arguments
        ---------
            - relative : Boolean
        
        Returns
        -------
            Node with two sockets : left and right
        """
        return field.HandlePositions(relative=relative).input_node
    
    def set_handle_positions(self, position=None, offset=None, mode={'LEFT', 'RIGHT'}):
        """ <field GeometryNodeSetCurveHandlePositions>
        
        Methodes set_left_handle_positions and set_right_handle_positions are available
        """
        return field.HandlePositions(relative=relative).set_position(position=position, offset=offset, mode=mode)
        
    def set_left_handle_positions(self, position=None, offset=None):
        """ <field GeometryNodeSetCurveHandlePositions>
        
        Methodes set_left_handle_positions and set_right_handle_positions are available
        """
        self.set_handle_position(position=position, offset=offset, mode='LEFT')
        
    def set_right_handle_positions(self, position=None, offset=None):
        """ <field GeometryNodeSetCurveHandlePositions>
        
        Methodes set_left_handle_positions and set_right_handle_positions are available
        """
        self.set_handle_position(position=position, offset=offset, mode='RIGHT')
        
    def handle_type_selection(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Method
        
        The values of the two parameters are declined in 2 methods:
        - [left_handle_selection](#left_handle_selection)
        - [right_handle_selection](#right_handle_selection)
                                       
        and 8 properties:
        - [left_handle_free](#left_handle_free)
        - [left_handle_vector](#left_handle_vector)
        - [left_handle_vector](#left_handle_vector)
        - [left_handle_align](#left_handle_align)
        - [right_handle_free](#right_handle_free)
        - [right_handle_auto](#right_handle_auto)
        - [right_handle_vector](#right_handle_vector)
        - [right_handle_align](#right_handle_align)
        
        Arguments
        ---------
            - handle_type : str in 'AUTO', 'FREE', 'VECTOR', 'ALIGN'
            - mode : str in ['RIGHT', 'LEFT'] or set {'RIGHT', 'LEFT'}
        
        Returns
        -------
            Boolean
        """
        return field.HandleTypeSelection(handle_type=handle_type, mode=mode).node_socket
    
    def left_handle_selection(self, handle_type='AUTO'):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Method
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.handle_type_selection(handle_type=handle_type, mode='LEFT')

    def right_handle_selection(self, handle_type='AUTO'):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Method
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.handle_type_selection(handle_type=handle_type, mode='RIGHT')
    
    @property
    def left_handle_free(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='FREE')
    
    @property
    def left_handle_auto(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='AUTO')
    
    @property
    def left_handle_vector(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='VECTOR')
    
    @property
    def left_handle_align(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='ALIGN')
    
    @property
    def right_handle_free(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='FREE')
    
    @property
    def right_handle_auto(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='AUTO')
    
    @property
    def right_handle_vector(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='VECTOR')
    
    @property
    def right_handle_align(self):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Property
        
        See [handle_type_selection](#handle_type_selection)
                                    
        Returns
            Boolean
        """
        return self.left_handle_selection(handle_type='ALIGN')
    
    # ====================================================================================================
    # Methods
    
    def delete(self):
        """ <method GeometryNodeDeleteGeometry>
        
        Example
        -------        
        
        ```python
        curve.splines(...).delete()
        ```
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
# =============================================================================================================================
# Cloud point : the point domain of cloud of points

class CloudPoint(Domain, PointInterface):

    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='POINT', selection=selection)
        
    def init_cache(self):
        super().init_cache()

        self.init_point_cache()
        
        self.radius_ = None
        
    @property
    def radius(self):
        if self.radius_ is None:
            self.radius_ = field.Radius(self)
        return self.radius_.node_socket
    
    @radius.setter
    def radius(self, value):
        if self.radius_ is None:
            self.radius_ = field.Radius(self)
        self.radius_.set_value(value)
        
    # ====================================================================================================
    # Methods

    def delete(self):
        """ <method GeometryNodeDeleteGeometry>
        
        Example
        -------        
        
        ```python
        cloud.points(...).delete()
        ```
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
    def merge(self, distance=0.001):
        """ > Merge points by distance
        
        <blid GeometryNodeMergeByDistance>
        
        Example
        -------        
        
        '''python
        cloud.points().merge()
        ````

        Arguments
        ---------
            - distance : Float
                The merge distance
        """
        return self.stack(nodes.MergeByDistance(self.data_socket, selection=self.selection, distance=distance))
    
    def to_vertices(self):
        """ > Convert points to vertices
        
        <blid GeometryNodePointsToVertices>
        
        Returns
        -------
        Points
        
        Example
        -------
        
        ```python
        verts = cloud.points.to_vertices()
        ```
        """
        return nodes.PointsToVertices(points=self.data_socket, selection=self.selection)
        
    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Convert points to vertices
        
        <blid GeometryNodePointsToVertices>
        
        Parameters
        ----------
            - density : Float
            - voxel_size : Float
            - voxel_amount : Float
            - radius : Float
            - resolution_mode : str (default = 'VOXEL_AMOUNT') in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        
        
        Returns
        -------
        Volume
        
        Example
        -------
        
        ```python
        volume = cloud.points.to_volume()
        ```
        """
        return nodes.PointsToVolume(points=self.data_socket, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode='VOXEL_AMOUNT')
        
        
        
# =============================================================================================================================
# Instance domain

class Instance(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='INSTANCE', selection=selection)
        
    # ====================================================================================================
    # Methods
    
    def delete(self):
        """ > Delete instances
        
        <blid GeometryNodeDeleteGeometry>
        
        Example
        -------        
        
        ```python
        instances.insts(...).delete()
        ```
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection))
    
    def rotate(self, rotation=None, pivot_point=None, local_space=None):
        """ > Rotate instances
        
        <blid GeometryNodeRotateInstances>
        
        Arguments
        ---------
            - rotation : Vector
            - pivot_point : Vector
            - local_space : Boolean
        
        Example
        -------        
        
        ```python
        instances.insts(...).rotate(...)
        ```
        """
        return self.stack(nodes.RotateInstances(
            instances=self.data_socket, selection=self.selection,
            rotation=rotation, pivot_point=pivot_point, local_space=local_space))
    
    def scale(self, scale=None, center=None, local_space=None):
        """ > Scale instances
        
        <blid GeometryNodeScaleInstances>
        
        Arguments
        ---------
            - scale : Vector
            - center : Vector
            - local_space : Boolean
        
        Example
        -------        
        
        ```python
        instances.insts(...).scale(...)
        ```
        """
        return self.stack(nodes.ScaleInstances(
            instances=self.data_socket, selection=self.selection,
            scale=scale, center=center, local_space=local_space))
    
    def translate(self, translation=None, local_space=None):
        """ > Translate instances
        
        <blid GeometryNodeTranslateInstances>
        
        Arguments
        ---------
            - translation : Vector
            - local_space : Boolean
        
        Example
        -------        
        
        ```python
        instances.insts(...).translate(...)
        ```
        """
        return self.stack(nodes.TranslateInstances(
            instances=self.data_socket, selection=self.selection,
            translation=translation, local_space=local_space))
    
    
