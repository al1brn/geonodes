#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-18
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
    """ Data class Mesh
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
        """ Geometry node [*Mesh Circle*].
        
        
            Args:
                vertices: Integer
                radius: Float
                fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MeshCircle`
            
            
            .. blid:: GeometryNodeMeshCircle
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type, label=node_label, node_color=node_color).mesh)

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', node_label = None, node_color = None):
        """ Geometry node [*Cone*].
        
        
            Args:
                vertices: Integer
                side_segments: Integer
                fill_segments: Integer
                radius_top: Float
                radius_bottom: Float
                depth: Float
                fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Cone`
            
            
            .. blid:: GeometryNodeMeshCone
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
                
        """

        return nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None, node_label = None, node_color = None):
        """ Geometry node [*Cube*].
        
        
            Args:
                size: Vector
                vertices_x: Integer
                vertices_y: Integer
                vertices_z: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Cube`
            
            
            .. blid:: GeometryNodeMeshCube
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z, label=node_label, node_color=node_color).mesh)

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', node_label = None, node_color = None):
        """ Geometry node [*Cylinder*].
        
        
            Args:
                vertices: Integer
                side_segments: Integer
                fill_segments: Integer
                radius: Float
                depth: Float
                fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Cylinder`
            
            
            .. blid:: GeometryNodeMeshCylinder
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
                
        """

        return nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None, node_label = None, node_color = None):
        """ Geometry node [*Grid*].
        
        
            Args:
                size_x: Float
                size_y: Float
                vertices_x: Integer
                vertices_y: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Grid`
            
            
            .. blid:: GeometryNodeMeshGrid
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y, label=node_label, node_color=node_color).mesh)

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None, node_label = None, node_color = None):
        """ Geometry node [*Ico Sphere*].
        
        
            Args:
                radius: Float
                subdivisions: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.IcoSphere`
            
            
            .. blid:: GeometryNodeMeshIcoSphere
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.IcoSphere(radius=radius, subdivisions=subdivisions, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.IcoSphere(radius=radius, subdivisions=subdivisions, label=node_label, node_color=node_color).mesh)

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', node_label = None, node_color = None):
        """ Geometry node [*Mesh Line*].
        
        
            Args:
                count: Integer
                start_location: Vector
                offset: Vector
                count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
                mode (str): 'OFFSET' in [OFFSET, END_POINTS]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MeshLine`
            
            
            .. blid:: GeometryNodeMeshLine
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode, label=node_label, node_color=node_color).mesh)

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None, node_label = None, node_color = None):
        """ Geometry node [*UV Sphere*].
        
        
            Args:
                segments: Integer
                rings: Integer
                radius: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.UvSphere`
            
            
            .. blid:: GeometryNodeMeshUVSphere
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.UvSphere(segments=segments, rings=rings, radius=radius, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.UvSphere(segments=segments, rings=rings, radius=radius, label=node_label, node_color=node_color).mesh)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def domain_size(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'MESH'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.domain_size")
                
        """

        if self.domain_size_ is None:
            self.domain_size_ = nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.domain_size")
        return self.domain_size_

    @property
    def point_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'MESH'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.point_count")
                
        """

        return self.domain_size.point_count

    @property
    def edge_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'MESH'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.edge_count")
                
        """

        return self.domain_size.edge_count

    @property
    def face_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'MESH'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.face_count")
                
        """

        return self.domain_size.face_count

    @property
    def corner_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'MESH'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.corner_count")
                
        """

        return self.domain_size.face_corner_count


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(self, *mesh_2, self_intersection=None, hole_tolerant=None, node_label = None, node_color = None):
        """ Geometry node [*Mesh Boolean*].
        
        
            Args:
                self_intersection: Boolean
                hole_tolerant: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MeshBoolean`
            
                - operation = 'INTERSECT'
                  
            .. blid:: GeometryNodeMeshBoolean
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT', label=node_label, node_color=node_color)
                
        """

        return nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT', label=node_label, node_color=node_color).mesh

    def union(self, *mesh_2, self_intersection=None, hole_tolerant=None, node_label = None, node_color = None):
        """ Geometry node [*Mesh Boolean*].
        
        
            Args:
                self_intersection: Boolean
                hole_tolerant: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MeshBoolean`
            
                - operation = 'UNION'
                  
            .. blid:: GeometryNodeMeshBoolean
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION', label=node_label, node_color=node_color)
                
        """

        return nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION', label=node_label, node_color=node_color).mesh

    def difference(self, *mesh_2, self_intersection=None, hole_tolerant=None, node_label = None, node_color = None):
        """ Geometry node [*Mesh Boolean*].
        
        
            Args:
                mesh_2: <m>Geometry
                self_intersection: Boolean
                hole_tolerant: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MeshBoolean`
            
                - operation = 'DIFFERENCE'
                  
            .. blid:: GeometryNodeMeshBoolean
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE', label=node_label, node_color=node_color)
                
        """

        return nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE', label=node_label, node_color=node_color).mesh

    def split_edges(self, selection=None, node_label = None, node_color = None):
        """ Geometry node [*Split Edges*].
        
        
            Args:
                selection: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SplitEdges`
            
            
            .. blid:: GeometryNodeSplitEdges
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SplitEdges(mesh=self, selection=selection, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SplitEdges(mesh=self, selection=selection, label=node_label, node_color=node_color))

    def subdivide(self, level=None, node_label = None, node_color = None):
        """ Geometry node [*Subdivide Mesh*].
        
        
            Args:
                level: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SubdivideMesh`
            
            
            .. blid:: GeometryNodeSubdivideMesh
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SubdivideMesh(mesh=self, level=level, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SubdivideMesh(mesh=self, level=level, label=node_label, node_color=node_color))

    def subdivision_surface(self, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label = None, node_color = None):
        """ Geometry node [*Subdivision Surface*].
        
        
            Args:
                level: Integer
                crease: Float
                boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
                uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SubdivisionSurface`
            
            
            .. blid:: GeometryNodeSubdivisionSurface
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth, label=node_label, node_color=node_color))

    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label = None, node_color = None):
        """ Geometry node [*Triangulate*].
        
        
            Args:
                selection: Boolean
                minimum_vertices: Integer
                ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
                quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Triangulate`
            
            
            .. blid:: GeometryNodeTriangulate
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method, label=node_label, node_color=node_color))

    def dual(self, keep_boundaries=None, node_label = None, node_color = None):
        """ Geometry node [*Dual Mesh*].
        
        
            Args:
                keep_boundaries: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DualMesh`
            
            
            .. blid:: GeometryNodeDualMesh
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries, label=node_label, node_color=node_color))

    def flip_faces(self, selection=None, node_label = None, node_color = None):
        """ Geometry node [*Flip Faces*].
        
        
            Args:
                selection: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.FlipFaces`
            
            
            .. blid:: GeometryNodeFlipFaces
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.FlipFaces(mesh=self, selection=selection, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.FlipFaces(mesh=self, selection=selection, label=node_label, node_color=node_color))

    def duplicate_edges(self, selection=None, amount=None, node_label = None, node_color = None):
        """ Geometry node [*Duplicate Elements*].
        
        
            Args:
                selection: Boolean
                amount: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), duplicate_index (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DuplicateElements`
            
                - domain = 'EDGE'
                  
            .. blid:: GeometryNodeDuplicateElements
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='EDGE', label=node_label, node_color=node_color)
                
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='EDGE', label=node_label, node_color=node_color)

    def duplicate_faces(self, selection=None, amount=None, node_label = None, node_color = None):
        """ Geometry node [*Duplicate Elements*].
        
        
            Args:
                selection: Boolean
                amount: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), duplicate_index (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DuplicateElements`
            
                - domain = 'FACE'
                  
            .. blid:: GeometryNodeDuplicateElements
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='FACE', label=node_label, node_color=node_color)
                
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='FACE', label=node_label, node_color=node_color)

    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', node_label = None, node_color = None):
        """ Geometry node [*Extrude Mesh*].
        
        
            Args:
                selection: Boolean
                offset: Vector
                offset_scale: Float
                individual: Boolean
                mode (str): 'FACES' in [VERTICES, EDGES, FACES]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [mesh (Mesh), top (Boolean), side (Boolean)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ExtrudeMesh`
            
            
            .. blid:: GeometryNodeExtrudeMesh
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode, label=node_label, node_color=node_color)
                
        """

        return nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode, label=node_label, node_color=node_color)

    def to_curve(self, selection=None, node_label = None, node_color = None):
        """ Geometry node [*Mesh to Curve*].
        
        
            Args:
                selection: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MeshToCurve`
            
            
            .. blid:: GeometryNodeMeshToCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MeshToCurve(mesh=self, selection=selection, label=node_label, node_color=node_color)
                
        """

        return nodes.MeshToCurve(mesh=self, selection=selection, label=node_label, node_color=node_color).curve

    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES', node_label = None, node_color = None):
        """ Geometry node [*Mesh to Points*].
        
        
            Args:
                selection: Boolean
                position: Vector
                radius: Float
                mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Points
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MeshToPoints`
            
            
            .. blid:: GeometryNodeMeshToPoints
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode, label=node_label, node_color=node_color)
                
        """

        return nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode, label=node_label, node_color=node_color).points

    def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', node_label = None, node_color = None):
        """ Geometry node [*Distribute Points on Faces*].
        
        
            Args:
                selection: Boolean
                distance_min: Float
                density_max: Float
                density: Float
                density_factor: Float
                seed: Integer
                distribute_method (str): 'RANDOM' in [RANDOM, POISSON]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [points (Points), normal (Vector), rotation (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DistributePointsOnFaces`
            
            
            .. blid:: GeometryNodeDistributePointsOnFaces
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method, label=node_label, node_color=node_color)
                
        """

        return nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method, label=node_label, node_color=node_color)


