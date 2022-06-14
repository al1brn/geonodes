#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-14
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Mesh

class Mesh(gn.Geometry):
    """ 

    Data socket Mesh
    ----------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - Circle : mesh (Mesh)
            - Cone : Sockets      [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
            - Cube : mesh (Mesh)
            - Cylinder : Sockets      [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
            - Grid : mesh (Mesh)
            - IcoSphere : mesh (Mesh)
            - Line : mesh (Mesh)
            - UVSphere : mesh (Mesh)
    

        Attribute capture
        -----------------
            - capture_edge_angle : Sockets      [unsigned_angle (Float), signed_angle (Float)]
            - capture_edge_neighbors : face_count (Integer)
            - capture_edge_vertices : Sockets      [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
            - capture_face_area : area (Float)
            - capture_face_neighbors : Sockets      [vertex_count (Integer), face_count (Integer)]
            - capture_island : Sockets      [island_index (Integer), island_count (Integer)]
            - capture_material_index : material_index (Integer)
            - capture_material_selection : selection (Boolean)
            - capture_shade_smooth : smooth (Boolean)
            - capture_vertex_neighbors : Sockets      [vertex_count (Integer), face_count (Integer)]
    

        Attributes
        ----------
            - corner_ID : Float = capture_ID(domain='CORNER').unsigned_angle
            - corner_index : Float = capture_index(domain='CORNER').unsigned_angle
            - corner_position : Float = capture_position(domain='CORNER').unsigned_angle
            - edge_angle : Float = capture_edge_angle(domain='EDGE').unsigned_angle
            - edge_neighbors : Integer = capture_edge_neighbors(domain='EDGE')
            - edge_unsigned_angle : Float = capture_edge_angle(domain='EDGE').signed_angle
            - edge_vertices_index1 : Integer = capture_edge_vertices(domain='EDGE').vertex_index_1
            - edge_vertices_index2 : Integer = capture_edge_vertices(domain='EDGE').vertex_index_2
            - edge_vertices_position1 : Vector = capture_edge_vertices(domain='EDGE').position_1
            - edge_vertices_position2 : Vector = capture_edge_vertices(domain='EDGE').position_2
            - egde_ID : Float = capture_ID(domain='EDGE').unsigned_angle
            - egde_index : Float = capture_index(domain='EDGE').unsigned_angle
            - egde_position : Float = capture_position(domain='EDGE').unsigned_angle
            - face_ID : Float = capture_ID(domain='FACE').unsigned_angle
            - face_area : Float = capture_face_area(domain='FACE')
            - face_index : Float = capture_index(domain='FACE').unsigned_angle
            - face_is_planar : Boolean = capture_face_is_planar(domain='FACE')
            - face_neighbors_face_count : Integer = capture_face_neighbors(domain='FACE').face_count
            - face_neighbors_vertex_count : Integer = capture_face_neighbors(domain='FACE').vertex_count
            - face_position : Float = capture_position(domain='FACE').unsigned_angle
            - island : Integer = capture_island(domain='POINT').island_index
            - material_index : Integer = capture_material_index(domain='FACE')
            - material_selection : Boolean = capture_material_selection(domain='FACE')
            - shade_smooth : Boolean = capture_shade_smooth(domain='FACE')
            - vertex_neighbors_face_count : Integer = capture_vertex_neighbors(domain='POINT').face_count
            - vertex_neighbors_vertex_count : Integer = capture_vertex_neighbors(domain='POINT').vertex_count
    

        Methods
        -------
            - difference : mesh (Mesh)
            - distribute_points_on_faces : Sockets      [points (Points), normal (Vector), rotation (Vector)]
            - dual : dual_mesh (Geometry)
            - duplicate_edges : Sockets      [geometry (Geometry), duplicate_index (Integer)]
            - duplicate_faces : Sockets      [geometry (Geometry), duplicate_index (Integer)]
            - duplicate_points : Sockets      [geometry (Geometry), duplicate_index (Integer)]
            - extrude : Sockets      [mesh (Mesh), top (Boolean), side (Boolean)]
            - flip_faces : mesh (Mesh)
            - intersect : mesh (Mesh)
            - split_edges : mesh (Mesh)
            - subdivide : mesh (Mesh)
            - subdivision_surface : mesh (Mesh)
            - to_curve : curve (Curve)
            - to_points : points (Points)
            - triangulate : mesh (Mesh)
            - union : mesh (Mesh)
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE', node_label = None, node_color = None):
        """ > Node: MeshCircle
          
        <sub>go to: top index
        blender ref GeometryNodeMeshCircle
        node ref Mesh Circle </sub>
                                  
        ```python
        v = Mesh.Circle(vertices, radius, fill_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vertices : Integer
            - radius : Float## Parameters
            - fill_type : 'NONE' in [NONE, NGON, TRIANGLE_FAN]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return cls(nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type, label=node_label, node_color=node_color).mesh)

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', node_label = None, node_color = None):
        """ > Node: Cone
          
        <sub>go to: top index
        blender ref GeometryNodeMeshCone
        node ref Cone </sub>
                                  
        ```python
        v = Mesh.Cone(vertices, side_segments, fill_segments, radius_top, radius_bottom, depth, fill_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vertices : Integer
            - side_segments : Integer
            - fill_segments : Integer
            - radius_top : Float
            - radius_bottom : Float
            - depth : Float## Parameters
            - fill_type : 'NGON' in [NONE, NGON, TRIANGLE_FAN]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
            
        """

        return nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None, node_label = None, node_color = None):
        """ > Node: Cube
          
        <sub>go to: top index
        blender ref GeometryNodeMeshCube
        node ref Cube </sub>
                                  
        ```python
        v = Mesh.Cube(size, vertices_x, vertices_y, vertices_z, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - size : Vector
            - vertices_x : Integer
            - vertices_y : Integer
            - vertices_z : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return cls(nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z, label=node_label, node_color=node_color).mesh)

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', node_label = None, node_color = None):
        """ > Node: Cylinder
          
        <sub>go to: top index
        blender ref GeometryNodeMeshCylinder
        node ref Cylinder </sub>
                                  
        ```python
        v = Mesh.Cylinder(vertices, side_segments, fill_segments, radius, depth, fill_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vertices : Integer
            - side_segments : Integer
            - fill_segments : Integer
            - radius : Float
            - depth : Float## Parameters
            - fill_type : 'NGON' in [NONE, NGON, TRIANGLE_FAN]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
            
        """

        return nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None, node_label = None, node_color = None):
        """ > Node: Grid
          
        <sub>go to: top index
        blender ref GeometryNodeMeshGrid
        node ref Grid </sub>
                                  
        ```python
        v = Mesh.Grid(size_x, size_y, vertices_x, vertices_y, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - size_x : Float
            - size_y : Float
            - vertices_x : Integer
            - vertices_y : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return cls(nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y, label=node_label, node_color=node_color).mesh)

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None, node_label = None, node_color = None):
        """ > Node: IcoSphere
          
        <sub>go to: top index
        blender ref GeometryNodeMeshIcoSphere
        node ref Ico Sphere </sub>
                                  
        ```python
        v = Mesh.IcoSphere(radius, subdivisions, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - radius : Float
            - subdivisions : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.IcoSphere(radius=radius, subdivisions=subdivisions, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return cls(nodes.IcoSphere(radius=radius, subdivisions=subdivisions, label=node_label, node_color=node_color).mesh)

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', node_label = None, node_color = None):
        """ > Node: MeshLine
          
        <sub>go to: top index
        blender ref GeometryNodeMeshLine
        node ref Mesh Line </sub>
                                  
        ```python
        v = Mesh.Line(count, start_location, offset, count_mode, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - count : Integer
            - start_location : Vector
            - offset : Vector## Parameters
            - count_mode : 'TOTAL' in [TOTAL, RESOLUTION]
            - mode : 'OFFSET' in [OFFSET, END_POINTS]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return cls(nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode, label=node_label, node_color=node_color).mesh)

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None, node_label = None, node_color = None):
        """ > Node: UvSphere
          
        <sub>go to: top index
        blender ref GeometryNodeMeshUVSphere
        node ref UV Sphere </sub>
                                  
        ```python
        v = Mesh.UVSphere(segments, rings, radius, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - segments : Integer
            - rings : Integer
            - radius : Float## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.UvSphere(segments=segments, rings=rings, radius=radius, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return cls(nodes.UvSphere(segments=segments, rings=rings, radius=radius, label=node_label, node_color=node_color).mesh)


    # ----------------------------------------------------------------------------------------------------
    # Attribute capture

    def capture_edge_angle(self, domain='EDGE', node_label = None, node_color = None):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.capture_edge_angle(self, domain='EDGE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'EDGE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [unsigned_angle (Float), signed_angle (Float)]
            
        """

        attr_name = 'capture_edge_angle_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.EdgeAngle(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_edge_neighbors(self, domain='EDGE', node_label = None, node_color = None):
        """ > Node: EdgeNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeNeighbors
        node ref Edge Neighbors </sub>
                                  
        ```python
        v = mesh.capture_edge_neighbors(self, domain='EDGE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'EDGE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeNeighbors(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        attr_name = 'capture_edge_neighbors_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.EdgeNeighbors(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.face_count

    def capture_edge_vertices(self, domain='EDGE', node_label = None, node_color = None):
        """ > Node: EdgeVertices
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeVertices
        node ref Edge Vertices </sub>
                                  
        ```python
        v = mesh.capture_edge_vertices(self, domain='EDGE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'EDGE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeVertices(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
            
        """

        attr_name = 'capture_edge_vertices_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.EdgeVertices(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_face_area(self, domain='FACE', node_label = None, node_color = None):
        """ > Node: FaceArea
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshFaceArea
        node ref Face Area </sub>
                                  
        ```python
        v = mesh.capture_face_area(self, domain='FACE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'FACE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FaceArea(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        attr_name = 'capture_face_area_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.FaceArea(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.area

    def capture_face_neighbors(self, domain='FACE', node_label = None, node_color = None):
        """ > Node: FaceNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshFaceNeighbors
        node ref Face Neighbors </sub>
                                  
        ```python
        v = mesh.capture_face_neighbors(self, domain='FACE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'FACE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FaceNeighbors(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
            
        """

        attr_name = 'capture_face_neighbors_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.FaceNeighbors(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_island(self, domain='POINT', node_label = None, node_color = None):
        """ > Node: MeshIsland
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshIsland
        node ref Mesh Island </sub>
                                  
        ```python
        v = mesh.capture_island(self, domain='POINT', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'POINT'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshIsland(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [island_index (Integer), island_count (Integer)]
            
        """

        attr_name = 'capture_island_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.MeshIsland(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_shade_smooth(self, domain='FACE', node_label = None, node_color = None):
        """ > Node: IsShadeSmooth
          
        <sub>go to: top index
        blender ref GeometryNodeInputShadeSmooth
        node ref Is Shade Smooth </sub>
                                  
        ```python
        v = mesh.capture_shade_smooth(self, domain='FACE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'FACE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.IsShadeSmooth(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        attr_name = 'capture_shade_smooth_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.IsShadeSmooth(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.smooth

    def capture_vertex_neighbors(self, domain='POINT', node_label = None, node_color = None):
        """ > Node: VertexNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshVertexNeighbors
        node ref Vertex Neighbors </sub>
                                  
        ```python
        v = mesh.capture_vertex_neighbors(self, domain='POINT', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'POINT'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VertexNeighbors(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
            
        """

        attr_name = 'capture_vertex_neighbors_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.VertexNeighbors(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_material_index(self, domain='FACE', node_label = None, node_color = None):
        """ > Node: MaterialIndex
          
        <sub>go to: top index
        blender ref GeometryNodeInputMaterialIndex
        node ref Material Index </sub>
                                  
        ```python
        v = mesh.capture_material_index(self, domain='FACE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'FACE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MaterialIndex(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        attr_name = 'capture_material_index_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.MaterialIndex(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.material_index

    def capture_material_selection(self, material=None, domain='FACE', node_label = None, node_color = None):
        """ > Node: MaterialSelection
          
        <sub>go to: top index
        blender ref GeometryNodeMaterialSelection
        node ref Material Selection </sub>
                                  
        ```python
        v = mesh.capture_material_selection(self, material, domain='FACE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - material : Material## Parameters
            - self
            - domain:'FACE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MaterialSelection(material=material, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        attr_name = 'capture_material_selection_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.MaterialSelection(material=material, label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.selection


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def face_ID(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.face_ID(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_ID(domain='FACE').unsigned_angle

    @property
    def egde_ID(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.egde_ID(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_ID(domain='EDGE').unsigned_angle

    @property
    def corner_ID(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.corner_ID(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_ID(domain='CORNER').unsigned_angle

    @property
    def face_index(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.face_index(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_index(domain='FACE').unsigned_angle

    @property
    def egde_index(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.egde_index(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_index(domain='EDGE').unsigned_angle

    @property
    def corner_index(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.corner_index(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_index(domain='CORNER').unsigned_angle

    @property
    def face_position(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.face_position(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_position(domain='FACE').unsigned_angle

    @property
    def egde_position(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.egde_position(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_position(domain='EDGE').unsigned_angle

    @property
    def corner_position(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.corner_position(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_position(domain='CORNER').unsigned_angle

    @property
    def edge_angle(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.edge_angle(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_edge_angle(domain='EDGE').unsigned_angle

    @property
    def edge_unsigned_angle(self):
        """ > Node: EdgeAngle
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeAngle
        node ref Edge Angle </sub>
                                  
        ```python
        v = mesh.edge_unsigned_angle(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeAngle()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_edge_angle(domain='EDGE').signed_angle

    @property
    def edge_neighbors(self):
        """ > Node: EdgeNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeNeighbors
        node ref Edge Neighbors </sub>
                                  
        ```python
        v = mesh.edge_neighbors(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeNeighbors()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_edge_neighbors(domain='EDGE')

    @property
    def edge_vertices_index1(self):
        """ > Node: EdgeVertices
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeVertices
        node ref Edge Vertices </sub>
                                  
        ```python
        v = mesh.edge_vertices_index1(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeVertices()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_edge_vertices(domain='EDGE').vertex_index_1

    @property
    def edge_vertices_index2(self):
        """ > Node: EdgeVertices
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeVertices
        node ref Edge Vertices </sub>
                                  
        ```python
        v = mesh.edge_vertices_index2(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeVertices()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_edge_vertices(domain='EDGE').vertex_index_2

    @property
    def edge_vertices_position1(self):
        """ > Node: EdgeVertices
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeVertices
        node ref Edge Vertices </sub>
                                  
        ```python
        v = mesh.edge_vertices_position1(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeVertices()
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.capture_edge_vertices(domain='EDGE').position_1

    @property
    def edge_vertices_position2(self):
        """ > Node: EdgeVertices
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshEdgeVertices
        node ref Edge Vertices </sub>
                                  
        ```python
        v = mesh.edge_vertices_position2(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EdgeVertices()
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.capture_edge_vertices(domain='EDGE').position_2

    @property
    def face_area(self):
        """ > Node: FaceArea
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshFaceArea
        node ref Face Area </sub>
                                  
        ```python
        v = mesh.face_area(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FaceArea()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_face_area(domain='FACE')

    @property
    def face_neighbors_vertex_count(self):
        """ > Node: FaceNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshFaceNeighbors
        node ref Face Neighbors </sub>
                                  
        ```python
        v = mesh.face_neighbors_vertex_count(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FaceNeighbors()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_face_neighbors(domain='FACE').vertex_count

    @property
    def face_neighbors_face_count(self):
        """ > Node: FaceNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshFaceNeighbors
        node ref Face Neighbors </sub>
                                  
        ```python
        v = mesh.face_neighbors_face_count(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FaceNeighbors()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_face_neighbors(domain='FACE').face_count

    @property
    def island(self):
        """ > Node: MeshIsland
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshIsland
        node ref Mesh Island </sub>
                                  
        ```python
        v = mesh.island(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshIsland()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_island(domain='POINT').island_index

    @property
    def shade_smooth(self):
        """ > Node: IsShadeSmooth
          
        <sub>go to: top index
        blender ref GeometryNodeInputShadeSmooth
        node ref Is Shade Smooth </sub>
                                  
        ```python
        v = mesh.shade_smooth(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.IsShadeSmooth()
            ```
    

        Returns
        -------
            Boolean
            
        """

        return self.capture_shade_smooth(domain='FACE')

    @property
    def vertex_neighbors_vertex_count(self):
        """ > Node: VertexNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshVertexNeighbors
        node ref Vertex Neighbors </sub>
                                  
        ```python
        v = mesh.vertex_neighbors_vertex_count(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VertexNeighbors()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_vertex_neighbors(domain='POINT').vertex_count

    @property
    def vertex_neighbors_face_count(self):
        """ > Node: VertexNeighbors
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshVertexNeighbors
        node ref Vertex Neighbors </sub>
                                  
        ```python
        v = mesh.vertex_neighbors_face_count(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VertexNeighbors()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_vertex_neighbors(domain='POINT').face_count

    @property
    def material_index(self):
        """ > Node: MaterialIndex
          
        <sub>go to: top index
        blender ref GeometryNodeInputMaterialIndex
        node ref Material Index </sub>
                                  
        ```python
        v = mesh.material_index(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MaterialIndex()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_material_index(domain='FACE')

    @property
    def material_selection(self, material=None):
        """ > Node: MaterialSelection
          
        <sub>go to: top index
        blender ref GeometryNodeMaterialSelection
        node ref Material Selection </sub>
                                  
        ```python
        v = mesh.material_selection(self, material)
        ```
    

        Arguments
        ---------
            ## Sockets
            - material : Material## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MaterialSelection(material=material)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return self.capture_material_selection(domain='FACE')

    @property
    def face_is_planar(self, threshold=None):
        """ > Node: FaceIsPlanar
          
        <sub>go to: top index
        blender ref GeometryNodeInputMeshFaceIsPlanar
        node ref Face is Planar </sub>
                                  
        ```python
        v = mesh.face_is_planar(self, threshold)
        ```
    

        Arguments
        ---------
            ## Sockets
            - threshold : Float## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FaceIsPlanar(threshold=threshold)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return self.capture_face_is_planar(domain='FACE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(self, *mesh_2, self_intersection=None, hole_tolerant=None, node_label = None, node_color = None):
        """ > Node: MeshBoolean
          
        <sub>go to: top index
        blender ref GeometryNodeMeshBoolean
        node ref Mesh Boolean </sub>
                                  
        ```python
        v = mesh.intersect(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh_2 : *Geometry (self)
            - self_intersection : Boolean
            - hole_tolerant : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'INTERSECT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT', label=node_label, node_color=node_color).mesh

    def union(self, *mesh_2, self_intersection=None, hole_tolerant=None, node_label = None, node_color = None):
        """ > Node: MeshBoolean
          
        <sub>go to: top index
        blender ref GeometryNodeMeshBoolean
        node ref Mesh Boolean </sub>
                                  
        ```python
        v = mesh.union(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh_2 : *Geometry (self)
            - self_intersection : Boolean
            - hole_tolerant : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'UNION'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION', label=node_label, node_color=node_color).mesh

    def difference(self, *mesh_2, self_intersection=None, hole_tolerant=None, node_label = None, node_color = None):
        """ > Node: MeshBoolean
          
        <sub>go to: top index
        blender ref GeometryNodeMeshBoolean
        node ref Mesh Boolean </sub>
                                  
        ```python
        v = mesh.difference(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh_1 : Geometry (self)
            - mesh_2 : *Geometry
            - self_intersection : Boolean
            - hole_tolerant : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'DIFFERENCE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE', label=node_label, node_color=node_color).mesh

    def split_edges(self, selection=None, node_label = None, node_color = None):
        """ > Node: SplitEdges
          
        <sub>go to: top index
        blender ref GeometryNodeSplitEdges
        node ref Split Edges </sub>
                                  
        ```python
        v = mesh.split_edges(selection, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - selection : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplitEdges(mesh=self, selection=selection, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return self.stack(nodes.SplitEdges(mesh=self, selection=selection, label=node_label, node_color=node_color))

    def subdivide(self, level=None, node_label = None, node_color = None):
        """ > Node: SubdivideMesh
          
        <sub>go to: top index
        blender ref GeometryNodeSubdivideMesh
        node ref Subdivide Mesh </sub>
                                  
        ```python
        v = mesh.subdivide(level, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - level : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SubdivideMesh(mesh=self, level=level, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return self.stack(nodes.SubdivideMesh(mesh=self, level=level, label=node_label, node_color=node_color))

    def subdivision_surface(self, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label = None, node_color = None):
        """ > Node: SubdivisionSurface
          
        <sub>go to: top index
        blender ref GeometryNodeSubdivisionSurface
        node ref Subdivision Surface </sub>
                                  
        ```python
        v = mesh.subdivision_surface(level, crease, boundary_smooth, uv_smooth, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - level : Integer
            - crease : Float## Parameters
            - boundary_smooth : 'ALL' in [PRESERVE_CORNERS, ALL]
            - uv_smooth : 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return self.stack(nodes.SubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth, label=node_label, node_color=node_color))

    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label = None, node_color = None):
        """ > Node: Triangulate
          
        <sub>go to: top index
        blender ref GeometryNodeTriangulate
        node ref Triangulate </sub>
                                  
        ```python
        v = mesh.triangulate(selection, minimum_vertices, ngon_method, quad_method, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - selection : Boolean
            - minimum_vertices : Integer## Parameters
            - ngon_method : 'BEAUTY' in [BEAUTY, CLIP]
            - quad_method : 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return self.stack(nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method, label=node_label, node_color=node_color))

    def dual(self, keep_boundaries=None, node_label = None, node_color = None):
        """ > Node: DualMesh
          
        <sub>go to: top index
        blender ref GeometryNodeDualMesh
        node ref Dual Mesh </sub>
                                  
        ```python
        v = mesh.dual(keep_boundaries, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - keep_boundaries : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries, label=node_label, node_color=node_color))

    def flip_faces(self, selection=None, node_label = None, node_color = None):
        """ > Node: FlipFaces
          
        <sub>go to: top index
        blender ref GeometryNodeFlipFaces
        node ref Flip Faces </sub>
                                  
        ```python
        v = mesh.flip_faces(selection, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - selection : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FlipFaces(mesh=self, selection=selection, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return self.stack(nodes.FlipFaces(mesh=self, selection=selection, label=node_label, node_color=node_color))

    def duplicate_points(self, selection=None, amount=None, node_label = None, node_color = None):
        """ > Node: DuplicateElements
          
        <sub>go to: top index
        blender ref GeometryNodeDuplicateElements
        node ref Duplicate Elements </sub>
                                  
        ```python
        v = mesh.duplicate_points(selection, amount, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - amount : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - domain : 'POINT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='POINT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), duplicate_index (Integer)]
            
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='POINT', label=node_label, node_color=node_color)

    def duplicate_edges(self, selection=None, amount=None, node_label = None, node_color = None):
        """ > Node: DuplicateElements
          
        <sub>go to: top index
        blender ref GeometryNodeDuplicateElements
        node ref Duplicate Elements </sub>
                                  
        ```python
        v = mesh.duplicate_edges(selection, amount, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - amount : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - domain : 'EDGE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='EDGE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), duplicate_index (Integer)]
            
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='EDGE', label=node_label, node_color=node_color)

    def duplicate_faces(self, selection=None, amount=None, node_label = None, node_color = None):
        """ > Node: DuplicateElements
          
        <sub>go to: top index
        blender ref GeometryNodeDuplicateElements
        node ref Duplicate Elements </sub>
                                  
        ```python
        v = mesh.duplicate_faces(selection, amount, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - amount : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - domain : 'FACE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='FACE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), duplicate_index (Integer)]
            
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='FACE', label=node_label, node_color=node_color)

    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', node_label = None, node_color = None):
        """ > Node: ExtrudeMesh
          
        <sub>go to: top index
        blender ref GeometryNodeExtrudeMesh
        node ref Extrude Mesh </sub>
                                  
        ```python
        v = mesh.extrude(selection, offset, offset_scale, individual, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - selection : Boolean
            - offset : Vector
            - offset_scale : Float
            - individual : Boolean## Parameters
            - mode : 'FACES' in [VERTICES, EDGES, FACES]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), top (Boolean), side (Boolean)]
            
        """

        return nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode, label=node_label, node_color=node_color)

    def to_curve(self, selection=None, node_label = None, node_color = None):
        """ > Node: MeshToCurve
          
        <sub>go to: top index
        blender ref GeometryNodeMeshToCurve
        node ref Mesh to Curve </sub>
                                  
        ```python
        v = mesh.to_curve(selection, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - selection : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshToCurve(mesh=self, selection=selection, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Curve
            
        """

        return nodes.MeshToCurve(mesh=self, selection=selection, label=node_label, node_color=node_color).curve

    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES', node_label = None, node_color = None):
        """ > Node: MeshToPoints
          
        <sub>go to: top index
        blender ref GeometryNodeMeshToPoints
        node ref Mesh to Points </sub>
                                  
        ```python
        v = mesh.to_points(selection, position, radius, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - selection : Boolean
            - position : Vector
            - radius : Float## Parameters
            - mode : 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Points
            
        """

        return nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode, label=node_label, node_color=node_color).points

    def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', node_label = None, node_color = None):
        """ > Node: DistributePointsOnFaces
          
        <sub>go to: top index
        blender ref GeometryNodeDistributePointsOnFaces
        node ref Distribute Points on Faces </sub>
                                  
        ```python
        v = mesh.distribute_points_on_faces(selection, distance_min, density_max, density, density_factor, seed, distribute_method, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - mesh : Mesh (self)
            - selection : Boolean
            - distance_min : Float
            - density_max : Float
            - density : Float
            - density_factor : Float
            - seed : Integer## Parameters
            - distribute_method : 'RANDOM' in [RANDOM, POISSON]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [points (Points), normal (Vector), rotation (Vector)]
            
        """

        return nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method, label=node_label, node_color=node_color)


