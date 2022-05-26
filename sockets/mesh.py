import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Mesh

class Mesh(gn.Geometry):
    """ Data socket Mesh

    Constructors
    ------------
        Circle               : mesh (Geometry)
        Cone                 : Sockets [mesh (Geometry), top (Boolean), bottom (Boolean), side (Boolean)]
        Cube                 : mesh (Geometry)
        Cylinder             : Sockets [mesh (Geometry), top (Boolean), side (Boolean), bottom (Boolean)]
        Grid                 : mesh (Geometry)
        IcoSphere            : mesh (Geometry)
        Line                 : mesh (Geometry)
        UVSphere             : mesh (Geometry)
    Methods
    -------
        difference           : mesh (Geometry)
        distribute_points_on_faces : Sockets [points (Geometry), normal (Vector), rotation (Vector)]
        extrude              : Sockets [mesh (Geometry), top (Boolean), side (Boolean)]
        intersect            : mesh (Geometry)
        to_curve             : curve (Geometry)
        to_points            : points (Geometry)
        union                : mesh (Geometry)
    Stacked methods
    ---------------
        dual                 : Mesh
        flip_faces           : Mesh
        split_edges          : Mesh
        subdivide            : Mesh
        subdivision_surface  : Mesh
        triangulate          : Mesh
    """

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
        """Call node NodeMeshCircle (GeometryNodeMeshCircle)

        Sockets arguments
        -----------------
            vertices       : Integer
            radius         : Float

        Parameters arguments
        --------------------
            fill_type      : 'NONE' in [NONE, NGON, TRIANGLE_FAN]
        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeMeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).mesh)

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """Call node NodeCone (GeometryNodeMeshCone)

        Sockets arguments
        -----------------
            vertices       : Integer
            side_segments  : Integer
            fill_segments  : Integer
            radius_top     : Float
            radius_bottom  : Float
            depth          : Float

        Parameters arguments
        --------------------
            fill_type      : 'NGON' in [NONE, NGON, TRIANGLE_FAN]
        Returns
        -------
            Sockets [mesh (Geometry), top (Boolean), bottom (Boolean), side (Boolean)]
        """

        return nodes.NodeCone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """Call node NodeCube (GeometryNodeMeshCube)

        Sockets arguments
        -----------------
            size           : Vector
            vertices_x     : Integer
            vertices_y     : Integer
            vertices_z     : Integer
        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeCube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).mesh)

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """Call node NodeCylinder (GeometryNodeMeshCylinder)

        Sockets arguments
        -----------------
            vertices       : Integer
            side_segments  : Integer
            fill_segments  : Integer
            radius         : Float
            depth          : Float

        Parameters arguments
        --------------------
            fill_type      : 'NGON' in [NONE, NGON, TRIANGLE_FAN]
        Returns
        -------
            Sockets [mesh (Geometry), top (Boolean), side (Boolean), bottom (Boolean)]
        """

        return nodes.NodeCylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """Call node NodeGrid (GeometryNodeMeshGrid)

        Sockets arguments
        -----------------
            size_x         : Float
            size_y         : Float
            vertices_x     : Integer
            vertices_y     : Integer
        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeGrid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).mesh)

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        """Call node NodeIcoSphere (GeometryNodeMeshIcoSphere)

        Sockets arguments
        -----------------
            radius         : Float
            subdivisions   : Integer
        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeIcoSphere(radius=radius, subdivisions=subdivisions).mesh)

    @classmethod
    def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """Call node NodeMeshLine (GeometryNodeMeshLine)

        Sockets arguments
        -----------------
            count          : Integer
            resolution     : Float
            start_location : Vector
            offset         : Vector

        Parameters arguments
        --------------------
            count_mode     : 'TOTAL' in [TOTAL, RESOLUTION]
            mode           : 'OFFSET' in [OFFSET, END_POINTS]
        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeMeshLine(count=count, resolution=resolution, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).mesh)

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        """Call node NodeUvSphere (GeometryNodeMeshUVSphere)

        Sockets arguments
        -----------------
            segments       : Integer
            rings          : Integer
            radius         : Float
        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeUvSphere(segments=segments, rings=rings, radius=radius).mesh)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None):
        """Call node NodeMeshBoolean (GeometryNodeMeshBoolean)

        Sockets arguments
        -----------------
            mesh_2         : *Geometry
            mesh_1         : Geometry
            self_intersection: Boolean
            hole_tolerant  : Boolean

        Fixed parameters
        ----------------
            operation      : 'INTERSECT'

        Returns
        -------
            Geometry
        """

        return nodes.NodeMeshBoolean(*mesh_2, mesh_1=mesh_1, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT').mesh

    def union(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None):
        """Call node NodeMeshBoolean (GeometryNodeMeshBoolean)

        Sockets arguments
        -----------------
            mesh_2         : *Geometry
            mesh_1         : Geometry
            self_intersection: Boolean
            hole_tolerant  : Boolean

        Fixed parameters
        ----------------
            operation      : 'UNION'

        Returns
        -------
            Geometry
        """

        return nodes.NodeMeshBoolean(*mesh_2, mesh_1=mesh_1, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION').mesh

    def difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """Call node NodeMeshBoolean (GeometryNodeMeshBoolean)

        Sockets arguments
        -----------------
            mesh_1         : Geometry (self)
            mesh_2         : *Geometry
            self_intersection: Boolean
            hole_tolerant  : Boolean

        Fixed parameters
        ----------------
            operation      : 'DIFFERENCE'

        Returns
        -------
            Geometry
        """

        return nodes.NodeMeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE').mesh

    def extrude(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """Call node NodeExtrudeMesh (GeometryNodeExtrudeMesh)

        Sockets arguments
        -----------------
            mesh           : Geometry
            selection      : Boolean
            offset         : Vector
            offset_scale   : Float
            individual     : Boolean

        Parameters arguments
        --------------------
            mode           : 'FACES' in [VERTICES, EDGES, FACES]
        Returns
        -------
            Sockets [mesh (Geometry), top (Boolean), side (Boolean)]
        """

        return nodes.NodeExtrudeMesh(mesh=mesh, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)

    def to_curve(mesh=None, selection=None):
        """Call node NodeMeshToCurve (GeometryNodeMeshToCurve)

        Sockets arguments
        -----------------
            mesh           : Geometry
            selection      : Boolean
        Returns
        -------
            Geometry
        """

        return nodes.NodeMeshToCurve(mesh=mesh, selection=selection).curve

    def to_points(mesh=None, selection=None, position=None, radius=None, mode='VERTICES'):
        """Call node NodeMeshToPoints (GeometryNodeMeshToPoints)

        Sockets arguments
        -----------------
            mesh           : Geometry
            selection      : Boolean
            position       : Vector
            radius         : Float

        Parameters arguments
        --------------------
            mode           : 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]
        Returns
        -------
            Geometry
        """

        return nodes.NodeMeshToPoints(mesh=mesh, selection=selection, position=position, radius=radius, mode=mode).points

    def distribute_points_on_faces(mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """Call node NodeDistributePointsOnFaces (GeometryNodeDistributePointsOnFaces)

        Sockets arguments
        -----------------
            mesh           : Geometry
            selection      : Boolean
            distance_min   : Float
            density_max    : Float
            density        : Float
            density_factor : Float
            seed           : Integer

        Parameters arguments
        --------------------
            distribute_method: 'RANDOM' in [RANDOM, POISSON]
        Returns
        -------
            Sockets [points (Geometry), normal (Vector), rotation (Vector)]
        """

        return nodes.NodeDistributePointsOnFaces(mesh=mesh, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def split_edges(mesh=None, selection=None):
        """Call node NodeSplitEdges (GeometryNodeSplitEdges)

        Sockets arguments
        -----------------
            mesh           : Geometry
            selection      : Boolean
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSplitEdges(mesh=mesh, selection=selection))

    def subdivide(mesh=None, level=None):
        """Call node NodeSubdivideMesh (GeometryNodeSubdivideMesh)

        Sockets arguments
        -----------------
            mesh           : Geometry
            level          : Integer
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSubdivideMesh(mesh=mesh, level=level))

    def subdivision_surface(mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """Call node NodeSubdivisionSurface (GeometryNodeSubdivisionSurface)

        Sockets arguments
        -----------------
            mesh           : Geometry
            level          : Integer
            crease         : Float

        Parameters arguments
        --------------------
            boundary_smooth: 'ALL' in [PRESERVE_CORNERS, ALL]
            uv_smooth      : 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSubdivisionSurface(mesh=mesh, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))

    def triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """Call node NodeTriangulate (GeometryNodeTriangulate)

        Sockets arguments
        -----------------
            mesh           : Geometry
            selection      : Boolean
            minimum_vertices: Integer

        Parameters arguments
        --------------------
            ngon_method    : 'BEAUTY' in [BEAUTY, CLIP]
            quad_method    : 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeTriangulate(mesh=mesh, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))

    def dual(mesh=None, keep_boundaries=None):
        """Call node NodeDualMesh (GeometryNodeDualMesh)

        Sockets arguments
        -----------------
            mesh           : Geometry
            keep_boundaries: Boolean
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeDualMesh(mesh=mesh, keep_boundaries=keep_boundaries))

    def flip_faces(mesh=None, selection=None):
        """Call node NodeFlipFaces (GeometryNodeFlipFaces)

        Sockets arguments
        -----------------
            mesh           : Geometry
            selection      : Boolean
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeFlipFaces(mesh=mesh, selection=selection))


