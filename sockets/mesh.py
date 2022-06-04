import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Mesh

class Mesh(Geometry):
    """ Class Mesh
    

    | Inherits from: Geometry 
    

    Constructors
    ============
    - Circle    : mesh (Mesh) 
    - Cone      : Sockets      [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)] 
    - Cube      : mesh (Mesh) 
    - Cylinder  : Sockets      [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)] 
    - Grid      : mesh (Mesh) 
    - IcoSphere : mesh (Mesh) 
    - Line      : mesh (Mesh) 
    - UVSphere  : mesh (Mesh) 
    

    Attribute capture
    =================
    - capture_edge_angle         : Sockets      [unsigned_angle (Float), signed_angle (Float)] 
    - capture_edge_neighbors     : face_count (Integer) 
    - capture_edge_vertices      : Sockets      [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector),
      position_2 (Vector)] 
    - capture_face_area          : area (Float) 
    - capture_face_neighbors     : Sockets      [vertex_count (Integer), face_count (Integer)] 
    - capture_island             : Sockets      [island_index (Integer), island_count (Integer)] 
    - capture_material_index     : material_index (Integer) 
    - capture_material_selection : selection (Boolean) 
    - capture_shade_smooth       : smooth (Boolean) 
    - capture_vertex_neighbors   : Sockets      [vertex_count (Integer), face_count (Integer)] 
    

    Attributes
    ==========
    - corner_ID                     : Float = capture_ID(domain='CORNER').unsigned_angle 
    - corner_index                  : Float = capture_index(domain='CORNER').unsigned_angle 
    - corner_porision               : Float = capture_position(domain='CORNER').unsigned_angle 
    - edge_angle                    : Float = capture_edge_angle(domain='EDGE').unsigned_angle 
    - edge_neighbors                : Integer = capture_edge_neighbors(domain='EDGE') 
    - edge_unsigned_angle           : Float = capture_edge_angle(domain='EDGE').signed_angle 
    - edge_vertices_index1          : Integer = capture_edge_vertices(domain='EDGE').vertex_index_1 
    - edge_vertices_index2          : Integer = capture_edge_vertices(domain='EDGE').vertex_index_2 
    - edge_vertices_position1       : Vector = capture_edge_vertices(domain='EDGE').position_1 
    - edge_vertices_position2       : Vector = capture_edge_vertices(domain='EDGE').position_2 
    - egde_ID                       : Float = capture_ID(domain='EDGE').unsigned_angle 
    - egde_index                    : Float = capture_index(domain='EDGE').unsigned_angle 
    - egde_position                 : Float = capture_position(domain='EDGE').unsigned_angle 
    - face_ID                       : Float = capture_ID(domain='FACE').unsigned_angle 
    - face_area                     : Float = capture_face_area(domain='FACE') 
    - face_index                    : Float = capture_index(domain='FACE').unsigned_angle 
    - face_neighbors_face_count     : Integer = capture_face_neighbors(domain='FACE').face_count 
    - face_neighbors_vertex_count   : Integer = capture_face_neighbors(domain='FACE').vertex_count 
    - face_position                 : Float = capture_position(domain='FACE').unsigned_angle 
    - island                        : Integer = capture_island(domain='POINT').island_index 
    - material_index                : Integer = capture_material_index(domain='FACE') 
    - material_selection            : Boolean = capture_material_selection(domain='FACE') 
    - shade_smooth                  : Boolean = capture_shade_smooth(domain='FACE') 
    - vertex_neighbors_face_count   : Integer = capture_vertex_neighbors(domain='POINT').face_count 
    - vertex_neighbors_vertex_count : Integer = capture_vertex_neighbors(domain='POINT').vertex_count 
    

    Methods
    =======
    - difference                 : mesh (Mesh) 
    - distribute_points_on_faces : Sockets      [points (Points), normal (Vector), rotation (Vector)] 
    - extrude                    : Sockets      [mesh (Mesh), top (Boolean), side (Boolean)] 
    - intersect                  : mesh (Mesh) 
    - to_curve                   : curve (Curve) 
    - to_points                  : points (Points) 
    - union                      : mesh (Mesh) 
    

    Stacked methods
    ===============
    - dual                : Mesh 
    - flip_faces          : Mesh 
    - split_edges         : Mesh 
    - subdivide           : Mesh 
    - subdivision_surface : Mesh 
    - triangulate         : Mesh 
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
        """Call node MeshCircle (GeometryNodeMeshCircle)

        Sockets arguments
        -----------------
            vertices       : Integer
            radius         : Float

        Parameters arguments
        --------------------
            fill_type      : 'NONE' in [NONE, NGON, TRIANGLE_FAN]

        Returns
        -------
            Mesh
        """

        return cls(nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).mesh)

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """Call node Cone (GeometryNodeMeshCone)

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
            Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
        """

        return nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """Call node Cube (GeometryNodeMeshCube)

        Sockets arguments
        -----------------
            size           : Vector
            vertices_x     : Integer
            vertices_y     : Integer
            vertices_z     : Integer

        Returns
        -------
            Mesh
        """

        return cls(nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).mesh)

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """Call node Cylinder (GeometryNodeMeshCylinder)

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
            Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
        """

        return nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """Call node Grid (GeometryNodeMeshGrid)

        Sockets arguments
        -----------------
            size_x         : Float
            size_y         : Float
            vertices_x     : Integer
            vertices_y     : Integer

        Returns
        -------
            Mesh
        """

        return cls(nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).mesh)

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        """Call node IcoSphere (GeometryNodeMeshIcoSphere)

        Sockets arguments
        -----------------
            radius         : Float
            subdivisions   : Integer

        Returns
        -------
            Mesh
        """

        return cls(nodes.IcoSphere(radius=radius, subdivisions=subdivisions).mesh)

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """Call node MeshLine (GeometryNodeMeshLine)

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
            Mesh
        """

        return cls(nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).mesh)

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        """Call node UvSphere (GeometryNodeMeshUVSphere)

        Sockets arguments
        -----------------
            segments       : Integer
            rings          : Integer
            radius         : Float

        Returns
        -------
            Mesh
        """

        return cls(nodes.UvSphere(segments=segments, rings=rings, radius=radius).mesh)


    # ----------------------------------------------------------------------------------------------------
    # Attribute capture

    def capture_edge_angle(self, domain='EDGE'):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Sockets [unsigned_angle (Float), signed_angle (Float)]
        """

        attr_name = 'capture_edge_angle_' + domain
        if not hasattr(self, attr_name):
            node = nodes.EdgeAngle()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_edge_neighbors(self, domain='EDGE'):
        """Call node EdgeNeighbors (GeometryNodeInputMeshEdgeNeighbors)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_edge_neighbors_' + domain
        if not hasattr(self, attr_name):
            node = nodes.EdgeNeighbors()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).face_count

    def capture_edge_vertices(self, domain='EDGE'):
        """Call node EdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """

        attr_name = 'capture_edge_vertices_' + domain
        if not hasattr(self, attr_name):
            node = nodes.EdgeVertices()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_face_area(self, domain='FACE'):
        """Call node FaceArea (GeometryNodeInputMeshFaceArea)

        Returns
        -------
            Float
        """

        attr_name = 'capture_face_area_' + domain
        if not hasattr(self, attr_name):
            node = nodes.FaceArea()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).area

    def capture_face_neighbors(self, domain='FACE'):
        """Call node FaceNeighbors (GeometryNodeInputMeshFaceNeighbors)

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        attr_name = 'capture_face_neighbors_' + domain
        if not hasattr(self, attr_name):
            node = nodes.FaceNeighbors()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_island(self, domain='POINT'):
        """Call node MeshIsland (GeometryNodeInputMeshIsland)

        Returns
        -------
            Sockets [island_index (Integer), island_count (Integer)]
        """

        attr_name = 'capture_island_' + domain
        if not hasattr(self, attr_name):
            node = nodes.MeshIsland()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_shade_smooth(self, domain='FACE'):
        """Call node IsShadeSmooth (GeometryNodeInputShadeSmooth)

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_shade_smooth_' + domain
        if not hasattr(self, attr_name):
            node = nodes.IsShadeSmooth()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).smooth

    def capture_vertex_neighbors(self, domain='POINT'):
        """Call node VertexNeighbors (GeometryNodeInputMeshVertexNeighbors)

        Returns
        -------
            Sockets [vertex_count (Integer), face_count (Integer)]
        """

        attr_name = 'capture_vertex_neighbors_' + domain
        if not hasattr(self, attr_name):
            node = nodes.VertexNeighbors()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_material_index(self, domain='FACE'):
        """Call node MaterialIndex (GeometryNodeInputMaterialIndex)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_material_index_' + domain
        if not hasattr(self, attr_name):
            node = nodes.MaterialIndex()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).material_index

    def capture_material_selection(self, material=None, domain='FACE'):
        """Call node MaterialSelection (GeometryNodeMaterialSelection)

        Sockets arguments
        -----------------
            material       : Material

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_material_selection_' + domain
        if not hasattr(self, attr_name):
            node = nodes.MaterialSelection(material=material)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).selection


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def face_ID(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_ID(domain='FACE').unsigned_angle

    @property
    def egde_ID(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_ID(domain='EDGE').unsigned_angle

    @property
    def corner_ID(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_ID(domain='CORNER').unsigned_angle

    @property
    def face_index(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_index(domain='FACE').unsigned_angle

    @property
    def egde_index(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_index(domain='EDGE').unsigned_angle

    @property
    def corner_index(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_index(domain='CORNER').unsigned_angle

    @property
    def face_position(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_position(domain='FACE').unsigned_angle

    @property
    def egde_position(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_position(domain='EDGE').unsigned_angle

    @property
    def corner_porision(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_position(domain='CORNER').unsigned_angle

    @property
    def edge_angle(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_edge_angle(domain='EDGE').unsigned_angle

    @property
    def edge_unsigned_angle(self):
        """Call node EdgeAngle (GeometryNodeInputMeshEdgeAngle)

        Returns
        -------
            Float
        """

        return self.capture_edge_angle(domain='EDGE').signed_angle

    @property
    def edge_neighbors(self):
        """Call node EdgeNeighbors (GeometryNodeInputMeshEdgeNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_edge_neighbors(domain='EDGE')

    @property
    def edge_vertices_index1(self):
        """Call node EdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Integer
        """

        return self.capture_edge_vertices(domain='EDGE').vertex_index_1

    @property
    def edge_vertices_index2(self):
        """Call node EdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Integer
        """

        return self.capture_edge_vertices(domain='EDGE').vertex_index_2

    @property
    def edge_vertices_position1(self):
        """Call node EdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Vector
        """

        return self.capture_edge_vertices(domain='EDGE').position_1

    @property
    def edge_vertices_position2(self):
        """Call node EdgeVertices (GeometryNodeInputMeshEdgeVertices)

        Returns
        -------
            Vector
        """

        return self.capture_edge_vertices(domain='EDGE').position_2

    @property
    def face_area(self):
        """Call node FaceArea (GeometryNodeInputMeshFaceArea)

        Returns
        -------
            Float
        """

        return self.capture_face_area(domain='FACE')

    @property
    def face_neighbors_vertex_count(self):
        """Call node FaceNeighbors (GeometryNodeInputMeshFaceNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_face_neighbors(domain='FACE').vertex_count

    @property
    def face_neighbors_face_count(self):
        """Call node FaceNeighbors (GeometryNodeInputMeshFaceNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_face_neighbors(domain='FACE').face_count

    @property
    def island(self):
        """Call node MeshIsland (GeometryNodeInputMeshIsland)

        Returns
        -------
            Integer
        """

        return self.capture_island(domain='POINT').island_index

    @property
    def shade_smooth(self):
        """Call node IsShadeSmooth (GeometryNodeInputShadeSmooth)

        Returns
        -------
            Boolean
        """

        return self.capture_shade_smooth(domain='FACE')

    @property
    def vertex_neighbors_vertex_count(self):
        """Call node VertexNeighbors (GeometryNodeInputMeshVertexNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_vertex_neighbors(domain='POINT').vertex_count

    @property
    def vertex_neighbors_face_count(self):
        """Call node VertexNeighbors (GeometryNodeInputMeshVertexNeighbors)

        Returns
        -------
            Integer
        """

        return self.capture_vertex_neighbors(domain='POINT').face_count

    @property
    def material_index(self):
        """Call node MaterialIndex (GeometryNodeInputMaterialIndex)

        Returns
        -------
            Integer
        """

        return self.capture_material_index(domain='FACE')

    @property
    def material_selection(self, material=None):
        """Call node MaterialSelection (GeometryNodeMaterialSelection)

        Sockets arguments
        -----------------
            material       : Material

        Returns
        -------
            Boolean
        """

        return self.capture_material_selection(domain='FACE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(*mesh_2, self_intersection=None, hole_tolerant=None):
        """Call node MeshBoolean (GeometryNodeMeshBoolean)

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
            Mesh
        """

        return nodes.MeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT').mesh

    def union(*mesh_2, self_intersection=None, hole_tolerant=None):
        """Call node MeshBoolean (GeometryNodeMeshBoolean)

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
            Mesh
        """

        return nodes.MeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION').mesh

    def difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """Call node MeshBoolean (GeometryNodeMeshBoolean)

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
            Mesh
        """

        return nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE').mesh

    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """Call node ExtrudeMesh (GeometryNodeExtrudeMesh)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
            selection      : Boolean
            offset         : Vector
            offset_scale   : Float
            individual     : Boolean

        Parameters arguments
        --------------------
            mode           : 'FACES' in [VERTICES, EDGES, FACES]

        Returns
        -------
            Sockets [mesh (Mesh), top (Boolean), side (Boolean)]
        """

        return nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)

    def to_curve(self, selection=None):
        """Call node MeshToCurve (GeometryNodeMeshToCurve)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
            selection      : Boolean

        Returns
        -------
            Curve
        """

        return nodes.MeshToCurve(mesh=self, selection=selection).curve

    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):
        """Call node MeshToPoints (GeometryNodeMeshToPoints)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
            selection      : Boolean
            position       : Vector
            radius         : Float

        Parameters arguments
        --------------------
            mode           : 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

        Returns
        -------
            Points
        """

        return nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode).points

    def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """Call node DistributePointsOnFaces (GeometryNodeDistributePointsOnFaces)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
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
            Sockets [points (Points), normal (Vector), rotation (Vector)]
        """

        return nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def split_edges(self, selection=None):
        """Call node SplitEdges (GeometryNodeSplitEdges)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
            selection      : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.SplitEdges(mesh=self, selection=selection))

    def subdivide(self, level=None):
        """Call node SubdivideMesh (GeometryNodeSubdivideMesh)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
            level          : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.SubdivideMesh(mesh=self, level=level))

    def subdivision_surface(self, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """Call node SubdivisionSurface (GeometryNodeSubdivisionSurface)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
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

        return self.stack(nodes.SubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))

    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """Call node Triangulate (GeometryNodeTriangulate)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
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

        return self.stack(nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))

    def dual(self, keep_boundaries=None):
        """Call node DualMesh (GeometryNodeDualMesh)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
            keep_boundaries: Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries))

    def flip_faces(self, selection=None):
        """Call node FlipFaces (GeometryNodeFlipFaces)

        Sockets arguments
        -----------------
            mesh           : Mesh (self)
            selection      : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.FlipFaces(mesh=self, selection=selection))


