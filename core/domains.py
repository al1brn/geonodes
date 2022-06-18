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


import bpy

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
        return type(self)(self.data_socket, selection=selection)
    
    def __repr__(self):
        return f"<Domain {self.domain} of {self.data_socket}>"
    
    def stack(self, node):
        return self.data_socket.stack(node)
    
    # ----------------------------------------------------------------------------------------------------
    # Statistics
    
    def statistic(self, attribute, data_type=None):
        """ <method GeometryNodeAttributeStatistic>
        """
        dt = Socket.domain_data_type(attribute) if data_type is None else Socket.domain_data_type(data_type)
        
        return nodes.AttributeStatistic(self.data_socket, selection=self.selection, attribute=attribute, data_type=dt, domain=self.domain)

        
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
        
        return nodes.TransferAttribute(self.data_socket, attribute=attribute, source_position=source_position, index=index, data_type=dt, domain=self.domain, mapping=mapping).node_socket
    
    def transfer_boolean(self, attribute, source_position=None, index=None, mapping=None):
        """ <method GeometryNodeAttributeTransfer>
        
        mapping in ('NEAREST', 'INDEX'):
        - INDEX if source_position is None
        - NEAREST otherwise
        
        call transfer_attribute_interpolated for NEAREST_FACE_INTERPOLATED
        """
        return self.transfer_attribute(attribute, source_position=source_position, index=index, data_type='BOOLEAN', mapping=mapping)
        
    def transfer_integer(self, attribute, source_position=None, index=None, mapping=None):
        """ <method GeometryNodeAttributeTransfer>
        
        mapping in ('NEAREST', 'INDEX'):
        - INDEX if source_position is None
        - NEAREST otherwise
        
        call transfer_attribute_interpolated for NEAREST_FACE_INTERPOLATED
        """
        return self.transfer_attribute(attribute, source_position=source_position, index=index, data_type='INT', mapping=mapping)
        
    def transfer_float(self, attribute, source_position=None, index=None, mapping=None):
        """ <method GeometryNodeAttributeTransfer>
        
        mapping in ('NEAREST', 'INDEX'):
        - INDEX if source_position is None
        - NEAREST otherwise
        
        call transfer_attribute_interpolated for NEAREST_FACE_INTERPOLATED
        """
        return self.transfer_attribute(attribute, source_position=source_position, index=index, data_type='FLOAT', mapping=mapping)
        
    def transfer_vector(self, attribute, source_position=None, index=None, mapping=None):
        """ <method GeometryNodeAttributeTransfer>
        
        mapping in ('NEAREST', 'INDEX'):
        - INDEX if source_position is None
        - NEAREST otherwise
        
        call transfer_attribute_interpolated for NEAREST_FACE_INTERPOLATED
        """
        return self.transfer_attribute(attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', mapping=mapping)
        
    def transfer_color(self, attribute, source_position=None, index=None, mapping=None):
        """ <method GeometryNodeAttributeTransfer>
        
        mapping in ('NEAREST', 'INDEX'):
        - INDEX if source_position is None
        - NEAREST otherwise
        
        call transfer_attribute_interpolated for NEAREST_FACE_INTERPOLATED
        """
        return self.transfer_attribute(attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', mapping=mapping)

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
    # > Get a named attribute socket
    #
    # Make use named_field method
    
    def get_named_attribute(self, name, data_type=None):
        return self.named_field(name, data_type).node_socket
        
    # ----------------------------------------------------------------------------------------------------
    # > Set a named attribute socket
    #
    # Make use named_field method
    #
    # If data_type is None, the data_type is infered from the type of the value
    
    def set_named_attribute(self, name, value, data_type=None):
        self.named_field(name, data_type).set_value(value)

    def get_named_boolean(self, name):
        return self.get_named_attribute(name, data_type='BOOLEAN')

    def get_named_integer(self, name):
        return self.get_named_attribute(name, data_type='INT')
        
    def get_named_float(self, name):
        return self.get_named_attribute(name, data_type='FLOAT')

    def get_named_vector(self, name):
        return self.get_named_attribute(name, data_type='FLOAT_VECTOR')
        
    def get_named_color(self, name):
        return self.get_named_attribute(name, data_type='FLOAT_COLOR')
        
    # NOT SUPPORTED YET
    #def get_named_byte_color(self, name):
    #    return self.get_named_attribute(name, data_type='BYTE_COLOR')
    
    
    def set_named_boolean(self, name, value):
        self.set_named_attribute(name, value, data_type='BOOLEAN')

    def set_named_integer(self, name, value):
        self.set_named_attribute(name, value, data_type='INT')
        
    def set_named_float(self, name, value):
        self.set_named_attribute(name, value, data_type='FLOAT')

    def set_named_vector(self, name, value):
        self.set_named_attribute(name, value, data_type='FLOAT_VECTOR')
        
    def set_named_color(self, name, value):
        self.set_named_attribute(name, value, data_type='FLOAT_COLOR')
        
    def set_named_byte_color(self, name, value):
        self.set_named_attribute(name, value, data_type='BYTE_COLOR')
        
    # ====================================================================================================
    # Fields all domain have
        
    @property
    def ID(self):
        if self.ID_ is None:
            self.ID_ = field.ID(self)
        return self.ID_.node_socket
    
    @ID.setter
    def ID(self, value):
        if self.ID_ is None:
            self.ID_ = field.ID(self)
        self.ID_.set_value(value)
    
    @property
    def index(self):
        if self.index_ is None:
            self.index_ = field.Index(self)
        return self.index_.node_socket
    
    @property
    def position(self):
        """ > Property Point position
        <blid GeometryNodeInputPosition>
        """
        if self.position_ is None:
            self.position_ = field.Position(self)
        return self.position_.node_socket
    
    @position.setter
    def position(self, value):
        """ > Property Point position setter
        <blid GeometryNodeSetPosition>
        
        Arguments
        ---------
            - value: Vector
        """
        if self.domain in ['EDGE', 'FACE']:
            raise Exception(f"The position of edges and faces is read only")
        if self.position_ is None:
            self.position_ = field.Position(self)
        self.position_.set_value(value)
        
    @property
    def offset(self):
        return Node.Vector(0)
    
    @offset.setter
    def offset(self, value):
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
        
        ```python
        mesh.vertss.select(...).instantiate(...)
        curve.points.select(...).instantiate(...)
        cloud.points.select(...).instantiate(...)
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

# -----------------------------------------------------------------------------------------------------------------------------
# Properties and methodes shared by Mesh Point, Edge and Face (but not Corner)

class PEFInterface:
    
    def init_PEF_cache(self):
        pass
    
    def delete(self, mode='ALL'):
        """ <method GeometryNodeDeleteGeometry>
        
        mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')        
        
        ```python
        mesh.verts.select(...).delete(mode='ALL')
        mesh.edges.select(...).delete(mode='EDGE_FACE')
        mesh.faces.select(...).delete(mode='ONLY_FACE')
        ```
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))
    
    def delete_all(self):
        """ <method GeometryNodeDeleteGeometry>
        
        call delete with mode : 'ALL'
        
        ```python
        mesh.verts.select(...).delete_all()
        mesh.edges.select(...).delete_all()
        mesh.faces.select(...).delete_all()
        ```
        """
        return self.delete(mode='ALL')
        
    def delete_faces(self):
        """ <method GeometryNodeDeleteGeometry>
        
        call delete with mode : 'ONLY_FACE'
        
        ```python
        mesh.verts.select(...).delete_faces()
        mesh.edges.select(...).delete_faces()
        mesh.faces.select(...).delete_faces()
        ```
        """
        return self.delete(mode='ONLY_FACE')
        
    def delete_edges_faces(self):
        """ <method GeometryNodeDeleteGeometry>
        
        call delete with mode : 'EDGE_FACE'
        
        ```python
        mesh.verts.select(...).delete_edges_faces()
        mesh.edges.select(...).delete_edges_faces()
        mesh.faces.select(...).delete_edges_faces()
        ```
        """
        return self.delete(mode='EDGE_FACE')
    
    def proximity(self, source_position=None):
        """ <method GeometryNodeProximity>
        
        ```python
        mesh.verts.select(...).proximity()
        mesh.edges.select(...).proximity()
        mesh.faces.select(...).proximity()
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
        
    
    def extrude(self, offset=None, offset_scale=None, individual=None, node_label = None, node_color = None):
        """ <method GeometryNodeExtrudeMesh>
        
        call [Mesh.extrude](/docs/sockets/Mesh.md#extrude) with mode = 'VERTICES'
                            
        ```python
        node = mesh.verts.extrude()
        ```
        
        """    
        return self.data_socket.extrude(selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual,
                        mode='VERTICES', node_label=node_label, node_color=node_color)
    
        
# -----------------------------------------------------------------------------------------------------------------------------
# vertex: the point domain of meshes

class Vertex(Domain, PointInterface, MeshInterface, PEFInterface):
    
    def __init__(self, data_socket):
        super().__init__(data_socket, domain='POINT')
        
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
        
        '''python
        mesh.verts.select().merge()
        ````

        Arguments
        ---------
            - mode : str (default = 'ALL') in ('ALL', 'CONNECTED')        
            - distance : Float
                The merge distance
        """
        return self.stack(nodes.MergeByDistance(self.data_socket, selection=self.selection, distance=distance, mode=mode))

    def merge_connected(self, distance=0.001):
        """ > Merge connected vertices by distance
        
        <blid GeometryNodeMergeByDistance>
        
        '''python
        mesh.verts.select().merge_connected()
        ````

        Arguments
        ---------
            - distance : Float
                The merge distance
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
        
    def set_material_index(self, value):
        field.MaterialIndex(self).set_value(value)
    
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
    
    
    def distribute_points(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None, node_color=None):
        """ <method GeometryNodeDistributePointsOnFaces>
    
        Call
        ----
        
        ```python
        node = mesh.face.distribute_points(selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None, node_color=None)
        ```

        Arguments
        ---------

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
                - distance_min : Float
                - density_max : Float
                - density : Float
                - density_factor : Float
                - seed : Integer
    

            Parameters
            ----------
                - distribute_method : str (default = 'RANDOM') in ('RANDOM', 'POISSON')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Returns
        -------
        Node with 3 sockets:
            - points : Points
            - normal : Vector
            - rotation : Vector
        """
        
        return nodes.DistributePointsOnFaces(mesh=self, selection=selection,
                distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor,
                seed=seed, distribute_method=distribute_method, label=label, node_color=node_color)
    
    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, node_label = None, node_color = None):
        """ <method GeometryNodeExtrudeMesh>
        
        call [Mesh.extrude](/docs/sockets/Mesh.md#extrude) with mode = 'FACES'
                            
        ```python
        node = mesh.faces.extrude()
        ```
        
        """
        
        return self.data_socket.extrude(selection=selection, offset=offset, offset_scale=offset_scale, individual=individual,
                        mode='FACES', node_label=node_label, node_color=node_color)
    
    
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
    
    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, node_label = None, node_color = None):
        """ <method GeometryNodeExtrudeMesh>
        
        call [Mesh.extrude](/docs/sockets/Mesh.md#extrude) with mode = 'EDGES'
                            
        ```python
        node = mesh.edges.extrude()
        ```
        
        """
        
        return self.data_socket.extrude(selection=selection, offset=offset, offset_scale=offset_scale, individual=individual,
                        mode='EDGES', node_label=node_label, node_color=node_color)
    
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
# Control point : the point domain of faces

class ControlPoint(Domain, PointInterface):

    def __init__(self, data_socket):
        super().__init__(data_socket, domain='POINT')
        
    def init_cache(self):
        super().init_cache()

        self.init_point_cache()
    
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
            self.resolution_ = field.SplineParameter(self)
        return self.resolution_.node_socket
    
    @resolution.setter
    def resolution(self, value):
        """ <field GeometryNodeSetSplineResolution>
        """
        if self.resolution_ is None:
            self.resolution_ = field.SplineParameter(self)
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
        
        mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')        
        
        ```python
        curve.splines.select(...).delete()
        ```
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
# =============================================================================================================================
# Cloud point : the point domain of cloud of points

class CloudPoint(Domain, PointInterface):

    def __init__(self, data_socket):
        super().__init__(data_socket, domain='POINT')
        
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
        
        mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')        
        
        ```python
        cloud.points.select(...).delete()
        ```
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
    def merge(self, distance=0.001):
        """ > Merge points by distance
        
        <blid GeometryNodeMergeByDistance>
        
        '''python
        cloud.points.select().merge()
        ````

        Arguments
        ---------
            - distance : Float
                The merge distance
        """
        return self.stack(nodes.MergeByDistance(self.data_socket, selection=self.selection, distance=distance))
    
        
        
        
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
        
        ```python
        instances.insts.select(...).delete()
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
        
        ```python
        instances.insts.select(...).rotate(...)
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
        
        ```python
        instances.insts.select(...).scale(...)
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
        
        ```python
        instances.insts.select(...).translate(...)
        ```
        """
        return self.stack(nodes.TranslateInstances(
            instances=self.data_socket, selection=self.selection,
            translation=translation, local_space=local_space))
    
    
    
        

        




    
        
