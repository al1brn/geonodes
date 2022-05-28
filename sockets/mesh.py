import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Mesh

class Mesh(gn.Geometry):
    """ Data socket Mesh

    Constructors
    ------------
        Circle                    : mesh         (Geometry)
        Cone                      : Sockets      [mesh (Geometry), top (Boolean), bottom (Boolean), side (Boolean)]
        Cube                      : mesh         (Geometry)
        Cylinder                  : Sockets      [mesh (Geometry), top (Boolean), side (Boolean), bottom (Boolean)]
        Grid                      : mesh         (Geometry)
        IcoSphere                 : mesh         (Geometry)
        Line                      : mesh         (Geometry)
        UVSphere                  : mesh         (Geometry)

    Attribute captures
    ------------------
        capture_edge_angle        : Sockets      [unsigned_angle (Float), signed_angle (Float)]
        capture_edge_neighbors    : face_count   (Integer)
        capture_edge_vertices     : Sockets      [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        capture_face_area         : area         (Float)
        capture_face_neighbors    : Sockets      [vertex_count (Integer), face_count (Integer)]
        capture_island            : Sockets      [island_index (Integer), island_count (Integer)]
        capture_material_index    : material_index (Integer)
        capture_shade_smooth      : smooth       (Boolean)
        capture_vertex_neighbors  : Sockets      [vertex_count (Integer), face_count (Integer)]

    Attributes
    ----------
        corner_ID                 : Integer   = capture_ID(domain='CORNER')
        corner_index              : Integer   = capture_index(domain='CORNER')
        corner_position           : Integer   = capture_position(domain='CORNER')
        edge_ID                   : Integer   = capture_ID(domain='EDGE')
        edge_angle                : Float     = capture_edge_angle(domain='EDGE').signed_angle
        edge_index                : Integer   = capture_index(domain='EDGE')
        edge_neighbors            : Integer   = capture_edge_neighbors(domain='EDGE')
        edge_position             : Integer   = capture_position(domain='EDGE')
        edge_unsigned_angle       : Float     = capture_edge_angle(domain='EDGE').unsigned_angle
        edge_vertices_index1      : Integer   = capture_edge_vertices(domain='EDGE').vertex_index_1
        edge_vertices_index2      : Integer   = capture_edge_vertices(domain='EDGE').vertex_index_2
        edge_vertices_position1   : Vector    = capture_edge_vertices(domain='EDGE').position_1
        edge_vertices_position2   : Vector    = capture_edge_vertices(domain='EDGE').position_2
        face_ID                   : Integer   = capture_ID(domain='FACE')
        face_area                 : Float     = capture_face_area(domain='FACE')
        face_index                : Integer   = capture_index(domain='FACE')
        face_neighbors_face_count : Integer   = capture_face_neighbors(domain='FACE').face_count
        face_neighbors_vertex_count : Integer   = capture_face_neighbors(domain='FACE').vertex_count
        face_position             : Integer   = capture_position(domain='FACE')
        island_count              : Integer   = capture_island(domain='FACE').island_count
        island_index              : Integer   = capture_island(domain='FACE').island_index
        material_index            : Integer   = capture_material_index(domain='FACE')
        shade_smooth              : Boolean   = capture_shade_smooth(domain='FACE')
        vertex_neighbors_face_count : Integer   = capture_vertex_neighbors(domain='POINT').face_count
        vertex_neighbors_vertex_count : Integer   = capture_vertex_neighbors(domain='POINT').vertex_count

    Methods
    -------
        difference                : mesh         (Geometry)
        distribute_points_on_faces : Sockets      [points (Geometry), normal (Vector), rotation (Vector)]
        extrude                   : Sockets      [mesh (Geometry), top (Boolean), side (Boolean)]
        intersect                 : mesh         (Geometry)
        to_curve                  : curve        (Geometry)
        to_points                 : points       (Geometry)
        union                     : mesh         (Geometry)

    Stacked methods
    ---------------
        dual                      : Mesh
        flip_faces                : Mesh
        split_edges               : Mesh
        subdivide                 : Mesh
        subdivision_surface       : Mesh
        triangulate               : Mesh
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
    def Line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """Call node NodeMeshLine (GeometryNodeMeshLine)

        Sockets arguments
        -----------------
            count          : Integer
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

        return cls(nodes.NodeMeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).mesh)

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
    # Attribute captures

    def capture_edge_neighbors(self, domain='EDGE'):
        """Call node NodeEdgeNeighbors (GeometryNodeInputMeshEdgeNeighbors)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_edge_neighbors_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeEdgeNeighbors()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).face_count

    def capture_face_area(self, domain='FACE'):
        """Call node NodeFaceArea (GeometryNodeInputMeshFaceArea)

        Returns
        -------
            Float
        """

        attr_name = 'capture_face_area_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeFaceArea()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).area

    def capture_edge_angle(self, domain='EDGE'):
        """Call node NodeEdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Sockets [unsigned_angle (Float), signed_angle (Float)]
        """

        attr_name = 'capture_edge_angle_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeEdgeAngle()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_edge_vertices(self, domain='EDGE'):
        """Call node NodeEdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        attr_name = 'capture_edge_vertices_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeEdgeVertices()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_face_neighbors(self, domain='FACE'):
        """Call node NodeFaceNeighbors (GeometryNodeInputMeshFaceNeighbors)

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        attr_name = 'capture_face_neighbors_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeFaceNeighbors()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_island(self, domain='FACE'):
        """Call node NodeMeshIsland (GeometryNodeInputMeshIsland)

        Returns
        -------
            Sockets [island_index (Integer), island_count (Integer)]
        """

        attr_name = 'capture_island_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeMeshIsland()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_vertex_neighbors(self, domain='POINT'):
        """Call node NodeVertexNeighbors (GeometryNodeInputMeshVertexNeighbors)

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        attr_name = 'capture_vertex_neighbors_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeVertexNeighbors()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_material_index(self, domain='FACE'):
        """Call node NodeMaterialIndex (GeometryNodeInputMaterialIndex)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_material_index_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeMaterialIndex()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).material_index

    def capture_shade_smooth(self, domain='FACE'):
        """Call node NodeIsShadeSmooth (GeometryNodeInputShadeSmooth)

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_shade_smooth_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeIsShadeSmooth()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).smooth


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def corner_ID(self):
        """Call node NodeID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        return self.capture_ID(domain='CORNER')

    @property
    def edge_ID(self):
        """Call node NodeID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        return self.capture_ID(domain='EDGE')

    @property
    def face_ID(self):
        """Call node NodeID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        return self.capture_ID(domain='FACE')

    @property
    def corner_index(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='CORNER')

    @property
    def edge_index(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='EDGE')

    @property
    def face_index(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='FACE')

    @property
    def corner_position(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_position(domain='CORNER')

    @property
    def edge_position(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_position(domain='EDGE')

    @property
    def face_position(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_position(domain='FACE')

    @property
    def edge_neighbors(self):
        """Call node NodeEdgeNeighbors (GeometryNodeInputMeshEdgeNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_edge_neighbors(domain='EDGE')

    @property
    def face_area(self):
        """Call node NodeFaceArea (GeometryNodeInputMeshFaceArea)

        Returns
        -------
            Float
        """

        return self.capture_face_area(domain='FACE')

    @property
    def edge_unsigned_angle(self):
        """Call node NodeEdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_edge_angle(domain='EDGE').output_sockets[0]

    @property
    def edge_angle(self):
        """Call node NodeEdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_edge_angle(domain='EDGE').output_sockets[1]

    @property
    def edge_vertices_index1(self):
        """Call node NodeEdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Integer
        """

        return self.capture_edge_vertices(domain='EDGE').output_sockets[0]

    @property
    def edge_vertices_index2(self):
        """Call node NodeEdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Integer
        """

        return self.capture_edge_vertices(domain='EDGE').output_sockets[1]

    @property
    def edge_vertices_position1(self):
        """Call node NodeEdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Vector
        """

        return self.capture_edge_vertices(domain='EDGE').output_sockets[2]

    @property
    def edge_vertices_position2(self):
        """Call node NodeEdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Vector
        """

        return self.capture_edge_vertices(domain='EDGE').output_sockets[3]

    @property
    def face_neighbors_vertex_count(self):
        """Call node NodeFaceNeighbors (GeometryNodeInputMeshFaceNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_face_neighbors(domain='FACE').output_sockets[0]

    @property
    def face_neighbors_face_count(self):
        """Call node NodeFaceNeighbors (GeometryNodeInputMeshFaceNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_face_neighbors(domain='FACE').output_sockets[1]

    @property
    def island_index(self):
        """Call node NodeMeshIsland (GeometryNodeInputMeshIsland)

        Returns
        -------
            Integer
        """

        return self.capture_island(domain='FACE').output_sockets[0]

    @property
    def island_count(self):
        """Call node NodeMeshIsland (GeometryNodeInputMeshIsland)

        Returns
        -------
            Integer
        """

        return self.capture_island(domain='FACE').output_sockets[1]

    @property
    def vertex_neighbors_vertex_count(self):
        """Call node NodeVertexNeighbors (GeometryNodeInputMeshVertexNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_vertex_neighbors(domain='POINT').output_sockets[0]

    @property
    def vertex_neighbors_face_count(self):
        """Call node NodeVertexNeighbors (GeometryNodeInputMeshVertexNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_vertex_neighbors(domain='POINT').output_sockets[1]

    @property
    def material_index(self):
        """Call node NodeMaterialIndex (GeometryNodeInputMaterialIndex)

        Returns
        -------
            Integer
        """

        return self.capture_material_index(domain='FACE')

    @property
    def shade_smooth(self):
        """Call node NodeIsShadeSmooth (GeometryNodeInputShadeSmooth)

        Returns
        -------
            Boolean
        """

        return self.capture_shade_smooth(domain='FACE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(*mesh_2, self_intersection=None, hole_tolerant=None):
        """Call node NodeMeshBoolean (GeometryNodeMeshBoolean)

        Sockets arguments
        -----------------
            mesh_2         : *Geometry
            self_intersection: Boolean
            hole_tolerant  : Boolean

        Fixed parameters
        ----------------
            operation      : 'INTERSECT'

        Returns
        -------
            Geometry
        """

        return nodes.NodeMeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT').mesh

    def union(*mesh_2, self_intersection=None, hole_tolerant=None):
        """Call node NodeMeshBoolean (GeometryNodeMeshBoolean)

        Sockets arguments
        -----------------
            mesh_2         : *Geometry
            self_intersection: Boolean
            hole_tolerant  : Boolean

        Fixed parameters
        ----------------
            operation      : 'UNION'

        Returns
        -------
            Geometry
        """

        return nodes.NodeMeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION').mesh

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


