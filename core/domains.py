#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket
from geonodes.nodes.nodes import create_node

import bpy

import logging
logger = logging.getLogger('geonodes')


# =============================================================================================================================
# Domain is used to implement points, edges, faces, corners, splines, instances properties 
#
# Mesh.faces.area : the area of the mesh faces

class Domain(Socket):
    """ Root class for domains: Points, Faces, Edges, Corners, Curves, Instances
    
    Fields are properties of domains.
    
    Initialization is made in method init_socket called by initializer Socket.__init__
    """ 
        
    def init_socket(self):
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
        """
        return self.create_field_node('GeometryNodeInputID').ID
        
    @property
    def index(self):
        """ <field GeometryNodeInputIndex>
        """
        return self.create_field_node('GeometryNodeInputIndex').index

    @property
    def normal(self):
        """ <field GeometryNodeInputNormal>
        """
        return self.create_field_node('GeometryNodeInputNormal').normal
    
    @property
    def position(self):
        """ <field GeometryNodeInputPosition>
        """
        return self.create_field_node('GeometryNodeInputPosition').position
    
    @property
    def radius(self):
        """ <field GeometryNodeInputRadius>
        """
        return self.create_field_node('GeometryNodeInputRadius').radius
    
    def named_attribute(self, name=None, data_type='FLOAT'):
        return self.create_field_node('GeometryNodeInputPosition', name=name).attribute
    
    def named_float(self, name):
        return self.named_attribute(name, data_type='FLOAT')
    
    def named_integer(self, name):
        return self.named_attribute(name, data_type='INT')
    
    def named_vector(self, name):
        return self.named_attribute(name, data_type='FLOAT_VECTOR')
    
    def named_color(self, name):
        return self.named_attribute(name, data_type='FLOAT_COLOR')
    
    def named_boolean(self, name):
        return self.named_attribute(name, data_type='BOOLEAN')
        
    # ---------------------------------------------------------------------------
    # Mesh menu
    
    @property
    def island(self):
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        return self.island.face_count
    

class PointDomain(Domain):
    """ > Field domain Point
    
    Inherits from [Domain](/docs/core/domain.MD)
    """
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'POINT'

    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        """
        return self.create_field_node('GeometryNodeInputMeshVertexNeighbors')
    
    @property
    def neighbors_vertices(self):
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        return self.neighbors.face_count
    
    @property
    def island(self):
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        return self.island.face_count


class FaceDomain(Domain):

    def init_socket(self):
        super().init_socket()
        self.domain = 'FACE'
        
    @property
    def area(self):
        return self.create_field_node('GeometryNodeInputMeshFaceArea').area
    
    @property
    def neighbors(self):
        return self.create_field_node('GeometryNodeInputMeshFaceNeighbors')
    
    @property
    def neighbors_vertices(self):
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        return self.neighbors.face_count
    
    @property
    def is_shade_smooth(self):
        return self.create_field_node('GeometryNodeInputShadeSmooth').smooth
    
    @property
    def island(self):
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        return self.island.face_count

    @property
    def material_index(self):
        return self.create_field_node('GeometryNodeInputMaterialIndex').material_index
    
    def material_selection(self, material=None):
        return self.create_field_node('GeometryNodeMaterialSelection', material=material).selection
    
    def face_is_planar(self, threshold=None):
        return self.create_field_node('GeometryNodeInputMeshFaceIsPlanar', threshold=threshold).planar
        
        
class EdgeDomain(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'EDGE'
        
    @property
    def angle(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeAngle').signed_angle
    
    @property
    def unsigned_angle(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeAngle').unsigned_angle
    
    @property
    def neighbors(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeNeighbors').face_count
    
    @property
    def vertices(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeVertices')
    
    @property
    def vertices_index_1(self):
        return self.vertices.vertex_index_1
    
    @property
    def vertices_index_2(self):
        return self.vertices.vertex_index_2
    
    @property
    def vertices_position_1(self):
        return self.vertices.position_1
    
    @property
    def vertices_position_2(self):
        return self.vertices.position_2
    
    @property
    def island(self):
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        return self.island.face_count
        

class CornerDomain(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'CORNER'

""" Instances inherits both from DataSocket and from Domain
class Instances(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'INSTANCES'
"""

class CurveDomain(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'CURVE'
        
    def handle_positions(self, relative=None):
        return self.create_field_node('GeometryNodeInputCurveHandlePositions', relative=relative)
    
    def handle_positions_left(self, relative=None):
        return self.handle_positions(relative=relative).left
    
    def handle_positions_right(self, relative=None):
        return self.handle_positions(relative=relative).right
    
    @property
    def tangent(self):
        return self.create_field_node('GeometryNodeInputTangent').tangent
    
    @property
    def tilt(self):
        return self.create_field_node('GeometryNodeInputCurveTilt').tilt
    
    def endpoint_selection(self, start_size=None, end_size=None):
        return self.create_field_node('GeometryNodeCurveEndpointSelection', start_size=start_size, end_size=end_size).selection
    
    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        return self.create_field_node('GeometryNodeCurveHandleTypeSelection', handle_type=handle_type, mode=mode).selection
    
    def left_handle_selection(self, handle_type='AUTO'):
        return self.handle_type_selection(handle_type=handle_type, mode='LEFT')

    def right_handle_selection(self, handle_type='AUTO'):
        return self.handle_type_selection(handle_type=handle_type, mode='RIGHT')
    
    @property
    def left_handle_free(self):
        return self.left_handle_selection(handle_type='FREE')
    
    @property
    def left_handle_auto(self):
        return self.left_handle_selection(handle_type='AUTO')
    
    @property
    def left_handle_vector(self):
        return self.left_handle_selection(handle_type='VECTOR')
    
    @property
    def left_handle_align(self):
        return self.left_handle_selection(handle_type='ALIGN')
    
    @property
    def right_handle_free(self):
        return self.left_handle_selection(handle_type='FREE')
    
    @property
    def right_handle_auto(self):
        return self.left_handle_selection(handle_type='AUTO')
    
    @property
    def right_handle_vector(self):
        return self.left_handle_selection(handle_type='VECTOR')
    
    @property
    def right_handle_align(self):
        return self.left_handle_selection(handle_type='ALIGN')
    
    @property
    def cyclic(self):
        return self.create_field_node('GeometryNodeInputSplineCyclic').cyclic
    
    @property
    def length_point_count(self):
        return self.create_field_node('GeometryNodeSplineLength')
    
    @property
    def length(self):
        return self.length_point_count.length
    
    @property
    def point_count(self):
        return self.length_point_count.point_count
    
    @property
    def parameter(self):
        return self.create_field_node('GeometryNodeSplineParameter')
    
    @property
    def factor(self):
        return self.parameter.factor
    
    @property
    def parameter_length(self):
        return self.parameter.length
    
    @property
    def parameter_index(self):
        return self.parameter.index
    
    @property
    def resolution(self):
        return self.create_field_node('GeometryNodeInputSplineResolution').resolution
        
