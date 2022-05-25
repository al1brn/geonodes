import geonodes as gn
from geonodes.core import socket as bcls
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

# ----------------------------------------------------------------------------------------------------
# Argument is a vector

def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)

# ----------------------------------------------------------------------------------------------------
# Sockets outputs

class Sockets(bcls.Sockets):
    pass


# ==============================================================================================================
# Data class Mesh

class Mesh(gn.Geometry):
    """ Socket data class Mesh

    Constructors
    ------------
        Circle               : Mesh
        Cone                 : Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
        Cube                 : Mesh
        Cylinder             : Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
        Grid                 : Mesh
        IcoSphere            : Mesh
        Line                 : Mesh
        UVSphere             : Mesh

    Attributes
    ----------
        capture_edge_angle_signed_angle : Sockets [unsigned_angle (Float), signed_angle (Float)]
        capture_edge_angle_unsigned_angle : Sockets [unsigned_angle (Float), signed_angle (Float)]
        capture_edge_neighbors : Integer
        capture_edge_vertices_position_1 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        capture_edge_vertices_position_2 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        capture_edge_vertices_vertex_index_1 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        capture_edge_vertices_vertex_index_2 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        capture_face_area    : Float
        capture_face_neighbors_face_count : Sockets [vertex_count (Integer), face_count (Integer)]
        capture_face_neighbors_vertex_count : Sockets [vertex_count (Integer), face_count (Integer)]
        capture_island_count : Sockets [island_index (Integer), island_count (Integer)]
        capture_island_index : Sockets [island_index (Integer), island_count (Integer)]
        capture_material_index : Integer
        capture_shade_smooth : Boolean
        capture_vertex_neighbors_face_count : Sockets [vertex_count (Integer), face_count (Integer)]
        capture_vertex_neighbors_vertex_count : Sockets [vertex_count (Integer), face_count (Integer)]
        corner_ID            : Integer
        corner_index         : Integer
        edge_ID              : Integer
        edge_angle_signed_angle : Sockets [unsigned_angle (Float), signed_angle (Float)]
        edge_angle_unsigned_angle : Sockets [unsigned_angle (Float), signed_angle (Float)]
        edge_index           : Integer
        edge_neighbors       : Integer
        edge_vertices_position_1 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        edge_vertices_position_2 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        edge_vertices_vertex_index_1 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        edge_vertices_vertex_index_2 : Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        face_ID              : Integer
        face_area            : Float
        face_index           : Integer
        face_neighbors_face_count : Sockets [vertex_count (Integer), face_count (Integer)]
        face_neighbors_vertex_count : Sockets [vertex_count (Integer), face_count (Integer)]
        island_count         : Sockets [island_index (Integer), island_count (Integer)]
        island_index         : Sockets [island_index (Integer), island_count (Integer)]
        material_index       : Integer
        shade_smooth         : Boolean
        vertex_neighbors_face_count : Sockets [vertex_count (Integer), face_count (Integer)]
        vertex_neighbors_vertex_count : Sockets [vertex_count (Integer), face_count (Integer)]

    Methods
    -------
        difference           : Mesh
        distribute_points_on_faces : Sockets [points (Points), normal (Vector), rotation (Vector)]
        extrude              : Sockets [mesh (Mesh), top (Boolean), side (Boolean)]
        intersect            : Mesh
        to_curve             : Curve
        to_points            : Points
        union                : Mesh

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
        """ Constructor Circle using node NodeMeshCircle

        Arguments
        ---------
            vertices        : Integer
            radius          : Float

            fill_type       : str

        Returns
        -------
            Mesh
        """

        return nodes.NodeMeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).output

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """ Constructor Cone using node NodeCone

        Arguments
        ---------
            vertices        : Integer
            side_segments   : Integer
            fill_segments   : Integer
            radius_top      : Float
            radius_bottom   : Float
            depth           : Float

            fill_type       : str

        Returns
        -------
            Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
        """

        return nodes.NodeCone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type).output

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """ Constructor Cube using node NodeCube

        Arguments
        ---------
            size            : Vector
            vertices_x      : Integer
            vertices_y      : Integer
            vertices_z      : Integer

        Returns
        -------
            Mesh
        """

        return nodes.NodeCube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).output

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """ Constructor Cylinder using node NodeCylinder

        Arguments
        ---------
            vertices        : Integer
            side_segments   : Integer
            fill_segments   : Integer
            radius          : Float
            depth           : Float

            fill_type       : str

        Returns
        -------
            Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
        """

        return nodes.NodeCylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type).output

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """ Constructor Grid using node NodeGrid

        Arguments
        ---------
            size_x          : Float
            size_y          : Float
            vertices_x      : Integer
            vertices_y      : Integer

        Returns
        -------
            Mesh
        """

        return nodes.NodeGrid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).output

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        """ Constructor IcoSphere using node NodeIcoSphere

        Arguments
        ---------
            radius          : Float
            subdivisions    : Integer

        Returns
        -------
            Mesh
        """

        return nodes.NodeIcoSphere(radius=radius, subdivisions=subdivisions).output

    @classmethod
    def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """ Constructor Line using node NodeMeshLine

        Arguments
        ---------
            count           : Integer
            resolution      : Float
            start_location  : Vector
            offset          : Vector

            count_mode      : str
            mode            : str

        Returns
        -------
            Mesh
        """

        return nodes.NodeMeshLine(count=count, resolution=resolution, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).output

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        """ Constructor UVSphere using node NodeUVSphere

        Arguments
        ---------
            segments        : Integer
            rings           : Integer
            radius          : Float

        Returns
        -------
            Mesh
        """

        return nodes.NodeUVSphere(segments=segments, rings=rings, radius=radius).output


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def corner_ID(self):
        """ Attribute corner_ID using node NodeID

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def edge_ID(self):
        """ Attribute edge_ID using node NodeID

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def face_ID(self):
        """ Attribute face_ID using node NodeID

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def corner_index(self):
        """ Attribute corner_index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def edge_index(self):
        """ Attribute edge_index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def face_index(self):
        """ Attribute face_index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    def capture_edge_neighbors(self, domain='EDGE'):
        """ Attribute capture_edge_neighbors using node NodeEdgeNeighbors

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def edge_neighbors(self):
        """ Attribute edge_neighbors using node NodeEdgeNeighbors

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    def capture_face_area(self, domain='FACE'):
        """ Attribute capture_face_area using node NodeFaceArea

        Arguments
        ---------

        Returns
        -------
            Float
        """

        return nodes.Attribute().output

    @property
    def face_area(self):
        """ Attribute face_area using node NodeFaceArea

        Arguments
        ---------

        Returns
        -------
            Float
        """

        return nodes.Attribute().output

    def capture_edge_angle_unsigned_angle(self, domain='EDGE'):
        """ Attribute capture_edge_angle_unsigned_angle using node NodeEdgeAngle

        Arguments
        ---------

        Returns
        -------
            Sockets [unsigned_angle (Float), signed_angle (Float)]
        """

        return nodes.Attribute().output

    def edge_angle_unsigned_angle(self):
        """ Attribute edge_angle_unsigned_angle using node NodeEdgeAngle

        Arguments
        ---------

        Returns
        -------
            Sockets [unsigned_angle (Float), signed_angle (Float)]
        """

        return nodes.Attribute().output

    def capture_edge_angle_signed_angle(self, domain='EDGE'):
        """ Attribute capture_edge_angle_signed_angle using node NodeEdgeAngle

        Arguments
        ---------

        Returns
        -------
            Sockets [unsigned_angle (Float), signed_angle (Float)]
        """

        return nodes.Attribute().output

    def edge_angle_signed_angle(self):
        """ Attribute edge_angle_signed_angle using node NodeEdgeAngle

        Arguments
        ---------

        Returns
        -------
            Sockets [unsigned_angle (Float), signed_angle (Float)]
        """

        return nodes.Attribute().output

    def capture_edge_vertices_vertex_index_1(self, domain='EDGE'):
        """ Attribute capture_edge_vertices_vertex_index_1 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def edge_vertices_vertex_index_1(self):
        """ Attribute edge_vertices_vertex_index_1 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def capture_edge_vertices_vertex_index_2(self, domain='EDGE'):
        """ Attribute capture_edge_vertices_vertex_index_2 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def edge_vertices_vertex_index_2(self):
        """ Attribute edge_vertices_vertex_index_2 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def capture_edge_vertices_position_1(self, domain='EDGE'):
        """ Attribute capture_edge_vertices_position_1 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def edge_vertices_position_1(self):
        """ Attribute edge_vertices_position_1 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def capture_edge_vertices_position_2(self, domain='EDGE'):
        """ Attribute capture_edge_vertices_position_2 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def edge_vertices_position_2(self):
        """ Attribute edge_vertices_position_2 using node NodeEdgeVertices

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        return nodes.Attribute().output

    def capture_face_neighbors_vertex_count(self, domain='FACE'):
        """ Attribute capture_face_neighbors_vertex_count using node NodeFaceNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def face_neighbors_vertex_count(self):
        """ Attribute face_neighbors_vertex_count using node NodeFaceNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_face_neighbors_face_count(self, domain='FACE'):
        """ Attribute capture_face_neighbors_face_count using node NodeFaceNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def face_neighbors_face_count(self):
        """ Attribute face_neighbors_face_count using node NodeFaceNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_island_index(self, domain='FACE'):
        """ Attribute capture_island_index using node NodeMeshIsland

        Arguments
        ---------

        Returns
        -------
            Sockets [island_index (Integer), island_count (Integer)]
        """

        return nodes.Attribute().output

    def island_index(self):
        """ Attribute island_index using node NodeMeshIsland

        Arguments
        ---------

        Returns
        -------
            Sockets [island_index (Integer), island_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_island_count(self, domain='FACE'):
        """ Attribute capture_island_count using node NodeMeshIsland

        Arguments
        ---------

        Returns
        -------
            Sockets [island_index (Integer), island_count (Integer)]
        """

        return nodes.Attribute().output

    def island_count(self):
        """ Attribute island_count using node NodeMeshIsland

        Arguments
        ---------

        Returns
        -------
            Sockets [island_index (Integer), island_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_vertex_neighbors_vertex_count(self, domain='POINT'):
        """ Attribute capture_vertex_neighbors_vertex_count using node NodeVertexNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def vertex_neighbors_vertex_count(self):
        """ Attribute vertex_neighbors_vertex_count using node NodeVertexNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_vertex_neighbors_face_count(self, domain='POINT'):
        """ Attribute capture_vertex_neighbors_face_count using node NodeVertexNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def vertex_neighbors_face_count(self):
        """ Attribute vertex_neighbors_face_count using node NodeVertexNeighbors

        Arguments
        ---------

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_material_index(self, domain='FACE'):
        """ Attribute capture_material_index using node NodeMaterialIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def material_index(self):
        """ Attribute material_index using node NodeMaterialIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    def capture_shade_smooth(self, domain='FACE'):
        """ Attribute capture_shade_smooth using node NodeIsShadeSmooth

        Arguments
        ---------

        Returns
        -------
            Boolean
        """

        return nodes.Attribute().output

    @property
    def shade_smooth(self):
        """ Attribute shade_smooth using node NodeIsShadeSmooth

        Arguments
        ---------

        Returns
        -------
            Boolean
        """

        return nodes.Attribute().output


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """ Method intersect using node NodeMeshBoolean

        Arguments
        ---------
            mesh_2          : Geometry (multi input): self socket
            self_intersection : Boolean
            hole_tolerant   : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'INTERSECT'

        Returns
        -------
            Mesh
        """

        return nodes.NodeMeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT').output

    def union(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """ Method union using node NodeMeshBoolean

        Arguments
        ---------
            mesh_2          : Geometry (multi input): self socket
            self_intersection : Boolean
            hole_tolerant   : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'UNION'

        Returns
        -------
            Mesh
        """

        return nodes.NodeMeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION').output

    def difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """ Method difference using node NodeMeshBoolean

        Arguments
        ---------
            mesh_1          : Geometry: self socket
            mesh_2          : Geometry (multi input)
            self_intersection : Boolean
            hole_tolerant   : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'DIFFERENCE'

        Returns
        -------
            Mesh
        """

        return nodes.NodeMeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE').output

    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """ Method extrude using node NodeExtrudeMesh

        Arguments
        ---------
            mesh            : Mesh: self socket
            selection       : Boolean
            offset          : Vector
            offset_scale    : Float
            individual      : Boolean

            mode            : str

        Returns
        -------
            Sockets [mesh (Mesh), top (Boolean), side (Boolean)]
        """

        return nodes.NodeExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode).output

    def to_curve(self, selection=None):
        """ Method to_curve using node NodeMeshtoCurve

        Arguments
        ---------
            mesh            : Mesh: self socket
            selection       : Boolean

        Returns
        -------
            Curve
        """

        return nodes.NodeMeshtoCurve(mesh=self, selection=selection).output

    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):
        """ Method to_points using node NodeMeshtoPoints

        Arguments
        ---------
            mesh            : Mesh: self socket
            selection       : Boolean
            position        : Vector
            radius          : Float

            mode            : str

        Returns
        -------
            Points
        """

        return nodes.NodeMeshtoPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode).output

    def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """ Method distribute_points_on_faces using node NodeDistributePointsonFaces

        Arguments
        ---------
            mesh            : Mesh: self socket
            selection       : Boolean
            distance_min    : Float
            density_max     : Float
            density         : Float
            density_factor  : Float
            seed            : Integer

            distribute_method : str

        Returns
        -------
            Sockets [points (Points), normal (Vector), rotation (Vector)]
        """

        return nodes.NodeDistributePointsonFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method).output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def split_edges(self, selection=None):
        """ Stacked method split_edges using node NodeSplitEdges

        Arguments
        ---------
            mesh            : Mesh: self socket
            selection       : Boolean

        Returns
        -------
            Mesh
        """

        return self.stack(nodes.NodeSplitEdges(mesh=self, selection=selection))

    def subdivide(self, level=None):
        """ Stacked method subdivide using node NodeSubdivideMesh

        Arguments
        ---------
            mesh            : Mesh: self socket
            level           : Integer

        Returns
        -------
            Mesh
        """

        return self.stack(nodes.NodeSubdivideMesh(mesh=self, level=level))

    def subdivision_surface(self, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """ Stacked method subdivision_surface using node NodeSubdivisionSurface

        Arguments
        ---------
            mesh            : Mesh: self socket
            level           : Integer
            crease          : Float

            boundary_smooth : str
            uv_smooth       : str

        Returns
        -------
            Mesh
        """

        return self.stack(nodes.NodeSubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))

    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ Stacked method triangulate using node NodeTriangulate

        Arguments
        ---------
            mesh            : Mesh: self socket
            selection       : Boolean
            minimum_vertices : Integer

            ngon_method     : str
            quad_method     : str

        Returns
        -------
            Mesh
        """

        return self.stack(nodes.NodeTriangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))

    def dual(self, keep_boundaries=None):
        """ Stacked method dual using node NodeDualMesh

        Arguments
        ---------
            mesh            : Mesh: self socket
            keep_boundaries : Boolean

        Returns
        -------
            Mesh
        """

        return self.stack(nodes.NodeDualMesh(mesh=self, keep_boundaries=keep_boundaries))

    def flip_faces(self, selection=None):
        """ Stacked method flip_faces using node NodeFlipFaces

        Arguments
        ---------
            mesh            : Mesh: self socket
            selection       : Boolean

        Returns
        -------
            Mesh
        """

        return self.stack(nodes.NodeFlipFaces(mesh=self, selection=selection))



