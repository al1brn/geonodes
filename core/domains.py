#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket
from geonodes.nodes import nodes
from geonodes.nodes.nodes import create_node
import geonodes.core.field as field


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

class Domain:
    
    def __init__(self, data_socket, domain, selection=None):

        self.data_socket = data_socket
        self.domain      = domain
        self.selection   = selection
        self.init_cache()
        
    def init_cache(self):
        self.ID_       = None
        self.index_    = None
        self.normal_   = None
        self.position_ = None
        self.radius_   = None
        
        self.named_fields = {}
        
    def select(self, selection):
        return type(self)(self.data_socket, selection=selection)
        
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
        
    # ----------------------------------------------------------------------------------------------------
        
    @property
    def ID(self):
        if self.ID_ is None:
            self.ID_ = field.ID(self)
        return self.ID_.node_socket
    
    @property
    def index(self):
        if self.index_ is None:
            self.index_ = field.Index(self)
        return self.index_.node_socket
        
    @property
    def normal(self):
        if self.normal_ is None:
            self.normal_ = field.Normal(self)
        return self.normal_.node_socket
    
    @property
    def position(self):
        if self.position_ is None:
            self.position_ = field.Position(self)
        return self.position_.node_socket
    
    @position.setter
    def position(self, value):
        if self.position_ is None:
            self.position_ = Location(self)
        self.position_.set_value(value)
        
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
        
        
# =============================================================================================================================
# Domain Point
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh, Curve, Points

class PointDomain(Domain):
    
    def __init__(self, data_socket):
        super().__init__(data_socket, domain='POINT')
        
    def init_cache(self):
        super().init_cache()
        
        self.neighbors_ = None
        
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
    
    # ====================================================================================================
    # Functions
    
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

    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='FACE', selection=selection)
        
    def init_cache(self):
        super().init_cache()

        self.neighbors_      = None
        self.area_           = None
        self.shade_smooth_   = None
        self.island_         = None
        self.material_index_ = None
        
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
    
    
# ---------------------------------------------------------------------------
# > Field domain FACE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh
        
        
class EdgeDomain(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='EDGE', selection=selection)
        
    def init_cache(self):
        super().init_cache()
        
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
# > Field domain CORNER
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh
        

class CornerDomain(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='CORNER', selection=selection)

        
# ---------------------------------------------------------------------------
# > Field domain CURVE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Spline and Curve

class CurveDomain(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='CURVE', selection=selection)
        
    def init_cache(self):
        super().init_cache()
        
        self.tilt_       = None
        self.cylic_      = None
        self.tangent_    = None
        self.length_     = None
        self.parameter_  = None
        self.resolution_ = None
        
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
    

# ---------------------------------------------------------------------------
# > Field domain INSTANCE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Instances

class InstanceDomain(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='INSTANCE', selection=selection)

        




    
        
