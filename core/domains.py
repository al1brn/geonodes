#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket
from geonodes.nodes import nodes
from geonodes.nodes.nodes import create_node

import bpy

import logging
logger = logging.getLogger('geonodes')


# =============================================================================================================================
# Root class for domains: PointDomain, FaceDomain, EdgeDomain, CornerDomain, CurveDomain and Instance
#    
# Fields are properties of domains.
#   
# Initialization is made in method init_socket called by initializer Socket.__init__
#
# Domains classes
# ---------------
#
# Domain classes are implemented as properties of geometries:
#     - Mesh owns `point`, `edge`, `face` and `corner` properties (`vertex` and `face_corner`
#       can be used rather than `point` and `corner`)
#     - Curve owns `point` and `spline` (`control_point` can be used rather than `point`)
#     - Points owns `point`
#     - Instances has no domain properties, fields are direct properties of this class
#
# To get the index of a point, use the syntax:
#
# ```python
# position = mesh.point.position
# ```
#
# Thanks to this syntax, you always know which field you want.
#
# ```python
# # mesh, curve and instances are initialized respectively as Mesh, Curve ans Instances
#
# mesh.point.position  # position of the vertices
# mesg.vertex.position # same
# mesh.face.position   # position of the faces
# mesh.face.area       # faces area
# curve.point.position # location of the curve control_points
# instances.index      # Indices of the individual instances
# instances.position   # Location of the instances
# ```
#

class Domain(Socket):
    
    def __init__(self, data_socket, domain):
        super().__init__(data_socket, data_socket.node)
        self.domain = domain
        self.fields = {}
        
    def create_field_node(self, bl_idname, **kwargs):
        """ > Create a **geonodes** from a bl_idname
        
        If kwargs is an empty dict, the node is put in cache in the _fields_ dict,
        otherwise it is returned directly.
        
        Attributes
        ----------
            - bl_idname : str
                A valid node bl_idname
            - kwargs : dict
                Arguments to pass to initialize the node
                
        Returns
        -------
            Node, the created node
        """
        
        cache = len(kwargs) == 0
        
        node = self.fields.get(bl_idname) if cache else None

        if node is None:
            node = create_node(bl_idname, **kwargs)
            node.as_attribute(self.bsocket, domain=self.domain)
            if cache:
                self.fields[bl_idname] = node
        return node
    
    # ---------------------------------------------------------------------------
    # Input menu
        
    @property
    def ID(self):
        """ <field GeometryNodeInputID>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputID').ID
        
    @property
    def index(self):
        """ <field GeometryNodeInputIndex>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputIndex').index

    @property
    def normal(self):
        """ <field GeometryNodeInputNormal>
        
        Property
        
        Returns
        -------
            Vector
        """
        return self.create_field_node('GeometryNodeInputNormal').normal
    
    @property
    def position(self):
        """ <field GeometryNodeInputPosition>
        
        Property
        
        Returns
        -------
            Vector
        """
        return self.create_field_node('GeometryNodeInputPosition').position
    
    @property
    def radius(self):
        """ <field GeometryNodeInputRadius>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputRadius').radius
    
    def named_attribute(self, name=None, data_type='FLOAT'):
        """ <field GeometryNodeInputNamedAttribute>
        
        This method is called by the following methods:
            
        - [named_float](#named_float)
        - [named_integer](#named_integer)
        - [named_vector](#named_vector)
        - [named_color](#named_color)
        - [named_boolean](#named_boolean)
        
        Returns
        -------
            Linked to data_type
        """
        return self.create_field_node('GeometryNodeInputNamedAttribute', name=name).attribute
    
    def named_float(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT'
                               
        Returns
        -------
            Float
        """
        return self.named_attribute(name, data_type='FLOAT')
    
    def named_integer(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'INT'
        """
        return self.named_attribute(name, data_type='INT')
    
    def named_vector(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT_VECTOR'
                               
        Returns
        -------
            Vector
        """
        return self.named_attribute(name, data_type='FLOAT_VECTOR')
    
    def named_color(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT_COLOR'
                               
        Returns
        -------
            Color
        """
        return self.named_attribute(name, data_type='FLOAT_COLOR')
    
    def named_boolean(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'BOOLEAN'
                               
        Returns
        -------
            Boolean
        """
        return self.named_attribute(name, data_type='BOOLEAN')
        

# ---------------------------------------------------------------------------
# > Field domain POINT
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh, Curve, Points

class PointDomain(Domain):
    
    def __init__(self, data_socket):
        super().__init__(data_socket, domain='POINT')

    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property

        Individual sockets can be accessed via properties:
            
        - [neighbors_vertices](#neighbors_vertices)
        - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
            - vertex_count
            - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshVertexNeighbors')
    
    @property
    def neighbors_vertices(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property
        
        Return the socket **vertex_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property
        
        Return the socket **face_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.face_count
    
    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, node_label = None, node_color = None):
        """ <method GeometryNodeExtrudeMesh>
        
        call [Mesh.extrude](/docs/sockets/Mesh.md#extrude) with mode = 'VERTICES'
                            
        ```python
        node = mesh.verts.extrude()
        ```
        
        """
        
        return self.data_socket.extrude(selection=selection, offset=offset, offset_scale=offset_scale, individual=individual,
                        mode='VERTICES', node_label=node_label, node_color=node_color)
                            
    
    
# ---------------------------------------------------------------------------
# > Field domain FACE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh

class FaceDomain(Domain):

    def __init__(self, data_socket):
        super().__init__(data_socket, domain='FACE')
        
    @property
    def area(self):
        """ <field GeometryNodeInputMeshFaceArea>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputMeshFaceArea').area
    
    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property

        Individual sockets can be accessed via properties:
            
        - [neighbors_vertices](#neighbors_vertices)
        - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
                - vertex_count
                - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshFaceNeighbors')
    
    @property
    def neighbors_vertices(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property
        
        Return the socket **vertex_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property
        
        Return the socket **face_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.face_count
    
    @property
    def is_shade_smooth(self):
        """ <field GeometryNodeInputShadeSmooth>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputShadeSmooth').smooth
    
    @property
    def island(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property

        Individual sockets can be accessed via properties:
            
        - [neighbors_vertices](#neighbors_vertices)
        - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
                - vertex_count
                - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property
        
        Return the socket **vertex_count** of property [island](#island)
        
        Returns
        -------
            Integer
        """
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property
        
        Return the socket **face_count** of property [island](#island)
        
        Returns
        -------
            Integer
        """
        return self.island.face_count

    @property
    def material_index(self):
        """ <field GeometryNodeInputMaterialIndex>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputMaterialIndex').material_index
    
    def material_selection(self, material=None):
        """ <field GeometryNodeMaterialSelection>
        
        Method
        
        Arguments
        ---------
            - material : Material
        
        Returns
        -------
            Boolean
        """
        return self.create_field_node('GeometryNodeMaterialSelection', material=material).selection
    
    def face_is_planar(self, threshold=None):
        """ <field GeometryNodeInputMeshFaceIsPlanar>
        
        Method
        
        Arguments
        ---------
            - threshold : Float
        
        Returns
        -------
            Boolean
        """
        return self.create_field_node('GeometryNodeInputMeshFaceIsPlanar', threshold=threshold).planar
    
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
    
    
# ---------------------------------------------------------------------------
# > Field domain FACE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh
        
        
class EdgeDomain(Domain):
    
    def __init__(self, data_socket):
        super().__init__(data_socket, domain='EDGE')

    @property
    def angle(self):
        """ <field GeometryNodeInputMeshEdgeAngle>
        
        Property
        
        To get the unsigned angle, used the property [unsigned_angle](#unsigned_angle).
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputMeshEdgeAngle').signed_angle
    
    @property
    def unsigned_angle(self):
        """ <field GeometryNodeInputMeshEdgeAngle>
        
        Property

        To get the signed angle, used the property [angle](#angle).
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputMeshEdgeAngle').unsigned_angle
    
    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshEdgeNeighbors>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputMeshEdgeNeighbors').face_count
    
    @property
    def vertices(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Sockets can be access individually via:
            
        - [vertices_index_1](#vertices_index_1)
        - [vertices_index_2](#vertices_index_2)
        - [vertices_position_1](#vertices_position_1)
        - [vertices_position_2](#vertices_position_2)
                                 
        
        Returns
        -------
            Node with 4 output sockets:
                - vertex_index_1
                - vertex_index_2
                - position_1
                - position_2
        """
        return self.create_field_node('GeometryNodeInputMeshEdgeVertices')
    
    @property
    def vertices_index_1(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.vertices.vertex_index_1
    
    @property
    def vertices_index_2(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.vertices.vertex_index_2
    
    @property
    def vertices_position_1(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.vertices.position_1
    
    @property
    def vertices_position_2(self):
        """ <field GeometryNodeInputMeshEdgeVertices>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.vertices.position_2
    
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
# > Field domain CORNER
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh
        

class CornerDomain(Domain):
    
    def __init__(self, data_socket):
        super().__init__(data_socket, domain='CORNER')

        
# ---------------------------------------------------------------------------
# > Field domain CURVE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Spline and Curve

class CurveDomain(Domain):
    
    def __init__(self, data_socket):
        super().__init__(data_socket, domain='CURVE')

        
    def handle_positions(self, relative=None):
        """ <field GeometryNodeInputCurveHandlePositions>
        
        Method
        
        Sockets can be access individually via:
            
        - [handle_positions_left](#handle_positions_left)
        - [handle_positions_right](#handle_positions_right)
                                       
        Arguments
        ---------
            - relative : Boolean
        
        Returns
        -------
            Node with 2 output sockets:
                - left
                - right
        """                
        return self.create_field_node('GeometryNodeInputCurveHandlePositions', relative=relative)
    
    def handle_positions_left(self, relative=None):
        """ <field GeometryNodeInputCurveHandlePositions>
        
        Method
        
        Returns the socket **left** of the methode [handle_positions(#handle_positions)]
                                       
        Arguments
        ---------
            - relative : Boolean
        
        Returns
        -------
            Vector
        """                
        return self.handle_positions(relative=relative).left
    
    def handle_positions_right(self, relative=None):
        """ <field GeometryNodeInputCurveHandlePositions>
        
        Method
        
        Returns the socket **right** of the methode [handle_positions(#handle_positions)]
                                       
        Arguments
        ---------
            - relative : Boolean
        
        Returns
        -------
            Vector
        """                
        return self.handle_positions(relative=relative).right
    
    @property
    def tangent(self):
        """ <field GeometryNodeInputTangent>
        
        Property
        
        Returns
        -------
            Vector
        """
        return self.create_field_node('GeometryNodeInputTangent').tangent
    
    @property
    def tilt(self):
        """ <field GeometryNodeInputCurveTilt>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputCurveTilt').tilt
    
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
        return self.create_field_node('GeometryNodeCurveEndpointSelection', start_size=start_size, end_size=end_size).selection
    
    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
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
        return self.create_field_node('GeometryNodeCurveHandleTypeSelection', handle_type=handle_type, mode=mode).selection
    
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
    
    @property
    def cyclic(self):
        """ <field GeometryNodeInputSplineCyclic>
        
        Property
        
        Returns
            Boolean
        """
        return self.create_field_node('GeometryNodeInputSplineCyclic').cyclic
    
    @property
    def length_point_count(self):
        """ <field GeometryNodeSplineLength>
        
        Property
        
        Sockets can be access individually via:
            
        - [length](#length)
        - [point_count](#point_count)
                                       
        Returns
        -------
            Node with 2 output sockets:
                - length
                - point_count
        """                
        return self.create_field_node('GeometryNodeSplineLength')
    
    @property
    def length(self):
        """ <field GeometryNodeSplineLength>
        
        Property
        
        Returns the socket **length** of method [length_point_count(#length_point_count)]
                                       
        Returns
        -------
            Float
        """                
        return self.length_point_count.length
    
    @property
    def point_count(self):
        """ <field GeometryNodeSplineLength>
        
        Property
        
        Returns the socket **point_count** of method [length_point_count(#length_point_count)]
                                       
        Returns
        -------
            Integer
        """                
        return self.length_point_count.point_count
    
    @property
    def parameter(self):
        """ <field GeometryNodeSplineParameter>
        
        Property
        
        Sockets can be access individually via:
            
        - [factor](#factor)
        - [parameter_length](#parameter_length)
        - [parameter_index](#parameter_index)
                                       
        Returns
        -------
            Node with 3 output sockets:
                - factor
                - length
                - index
        """                
        return self.create_field_node('GeometryNodeSplineParameter')
    
    @property
    def factor(self):
        """ <field GeometryNodeSplineParameter>
        
        Property
        
        Returns the socket **factor** of method [parameter(#parameter)]
                                       
        Returns
        -------
            Float
        """                
        return self.parameter.factor
    
    @property
    def parameter_length(self):
        """ <field GeometryNodeSplineParameter>
        
        Property
        
        Returns the socket **length** of method [parameter(#parameter)]
                                       
        Returns
        -------
            Float
        """                
        return self.parameter.length
    
    @property
    def parameter_index(self):
        """ <field GeometryNodeSplineParameter>
        
        Property
        
        Returns the socket **index** of method [parameter(#parameter)]
                                       
        Returns
        -------
            Integer
        """                
        return self.parameter.index
    
    @property
    def resolution(self):
        """ <field GeometryNodeInputSplineResolution>
        
        Property
        
        Returns
            Integer
        """
        return self.create_field_node('GeometryNodeInputSplineResolution').resolution
    
# ---------------------------------------------------------------------------
# > Field domain INSTANCE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Instances

class InstanceDomain(Domain):
    
    def __init__(self, data_socket):
        super().__init__(data_socket, domain='INSTANCE')

        




    
        
