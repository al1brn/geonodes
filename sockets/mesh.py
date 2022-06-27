#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-26
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

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
    

        Properties
        ----------
            - corner_count : face_corner_count (Integer) = domain_size.face_corner_count
            - domain_size : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
            - edge_count : edge_count (Integer) = domain_size.edge_count
            - face_count : face_count (Integer) = domain_size.face_count
            - point_count : point_count (Integer) = domain_size.point_count
    

        Methods
        -------
            - difference : mesh (Mesh)
            - distribute_points_on_faces : Sockets      [points (Points), normal (Vector), rotation (Vector)]
            - dual : dual_mesh (Geometry)
            - duplicate_edges : Sockets      [geometry (Geometry), duplicate_index (Integer)]
            - duplicate_faces : Sockets      [geometry (Geometry), duplicate_index (Integer)]
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


    def copy(self):

        return Mesh(self)

    def init_domains(self):
        self.verts   = domains.Vertex(self)
        self.edges   = domains.Edge(self)
        self.faces   = domains.Face(self)
        self.corners = domains.Corner(self)

    @property
    def point(self):
        return self.verts

    @property
    def edge(self):
        return self.edges
    @property
    def face(self):
        return self.faces
    @property
    def corner(self):
        return self.corners



    def reset_properties(self):

        super().reset_properties()

        self.domain_size_ = None

        self.point_count_ = None

        self.edge_count_ = None

        self.face_count_ = None

        self.corner_count_ = None

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
    # Properties

    @property
    def domain_size(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = mesh.domain_size
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'MESH'
            - label:f"{self.node_chain_label}.domain_size"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.domain_size")
            ```
    

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
            
        """

        if self.domain_size_ is None:
            self.domain_size_ = nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.domain_size")
        return self.domain_size_

    @property
    def point_count(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = mesh.point_count
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'MESH'
            - label:f"{self.node_chain_label}.point_count"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.point_count")
            ```
    

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
            
        """

        return self.domain_size.point_count

    @property
    def edge_count(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = mesh.edge_count
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'MESH'
            - label:f"{self.node_chain_label}.edge_count"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.edge_count")
            ```
    

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
            
        """

        return self.domain_size.edge_count

    @property
    def face_count(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = mesh.face_count
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'MESH'
            - label:f"{self.node_chain_label}.face_count"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.face_count")
            ```
    

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
            
        """

        return self.domain_size.face_count

    @property
    def corner_count(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = mesh.corner_count
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'MESH'
            - label:f"{self.node_chain_label}.corner_count"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.corner_count")
            ```
    

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
            
        """

        return self.domain_size.face_corner_count


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


