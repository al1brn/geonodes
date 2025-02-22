from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Mesh(Socket):
    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'component' : 'MESH'

        Returns
        -------
        - node [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
        """
        node = self._cache('Domain Size', sockets={'Geometry': self}, component='MESH')
        return node

    @classmethod
    def corners_of_edge(cls, edge_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (id: Edge Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Corners of Edge', sockets={'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_face(cls, face_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Face>

        Arguments
        ---------
        - face_index (Integer) : socket 'Face Index' (id: Face Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Corners of Face', sockets={'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_vertex(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Corners of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    def distribute_points_on_faces(self, density=None, seed=None, distribute_method='RANDOM', use_legacy_normal=False):
        """ > Node <&Node Distribute Points on Faces>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - distribute_method (str): parameter 'distribute_method' in ['RANDOM', 'POISSON']
        - use_legacy_normal (bool): parameter 'use_legacy_normal'

        Returns
        -------
        - Cloud [normal_ (Vector), rotation_ (Rotation)]
        """
        utils.check_enum_arg('Distribute Points on Faces', 'distribute_method', distribute_method, 'distribute_points_on_faces', ('RANDOM', 'POISSON'))
        node = Node('Distribute Points on Faces', sockets={'Mesh': self, 'Selection': self._sel, 'Density': density, 'Seed': seed}, distribute_method=distribute_method, use_legacy_normal=use_legacy_normal)
        return node._out

    def distribute_points_on_faces_random(self, density=None, seed=None, use_legacy_normal=False):
        """ > Node <&Node Distribute Points on Faces>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'distribute_method' : 'RANDOM'

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - use_legacy_normal (bool): parameter 'use_legacy_normal'

        Returns
        -------
        - Cloud [normal_ (Vector), rotation_ (Rotation)]
        """
        node = Node('Distribute Points on Faces', sockets={'Mesh': self, 'Selection': self._sel, 'Density': density, 'Seed': seed}, distribute_method='RANDOM', use_legacy_normal=use_legacy_normal)
        return node._out

    def distribute_points_on_faces_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None, use_legacy_normal=False):
        """ > Node <&Node Distribute Points on Faces>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'distribute_method' : 'POISSON'

        Arguments
        ---------
        - distance_min (Float) : socket 'Distance Min' (id: Distance Min)
        - density_max (Float) : socket 'Density Max' (id: Density Max)
        - density_factor (Float) : socket 'Density Factor' (id: Density Factor)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - use_legacy_normal (bool): parameter 'use_legacy_normal'

        Returns
        -------
        - Cloud [normal_ (Vector), rotation_ (Rotation)]
        """
        node = Node('Distribute Points on Faces', sockets={'Mesh': self, 'Selection': self._sel, 'Distance Min': distance_min, 'Density Max': density_max, 'Density Factor': density_factor, 'Seed': seed}, distribute_method='POISSON', use_legacy_normal=use_legacy_normal)
        return node._out

    def dual(self, keep_boundaries=None):
        """ > Node <&Node Dual Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - keep_boundaries (Boolean) : socket 'Keep Boundaries' (id: Keep Boundaries)

        Returns
        -------
        - Mesh
        """
        node = Node('Dual Mesh', sockets={'Mesh': self, 'Keep Boundaries': keep_boundaries})
        self._jump(node._out)
        return self._domain_to_geometry

    def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Curves>

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Curve
        """
        node = Node('Edge Paths to Curves', sockets={'Mesh': self, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edge_paths_to_selection(cls, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Selection>

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Boolean
        """
        node = Node('Edge Paths to Selection', sockets={'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edges_of_corner(cls, corner_index=None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [previous_edge_index_ (Integer)]
        """
        node = Node('Edges of Corner', sockets={'Corner Index': corner_index})
        return node._out

    @classmethod
    def edges_of_vertex(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Node <&Node Edges of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Edges of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def edges_to_face_groups(cls, boundary_edges=None):
        """ > Node <&Node Edges to Face Groups>

        Arguments
        ---------
        - boundary_edges (Boolean) : socket 'Boundary Edges' (id: Boundary Edges)

        Returns
        -------
        - Integer
        """
        node = Node('Edges to Face Groups', sockets={'Boundary Edges': boundary_edges})
        return node._out

    def extrude_vertices(self, offset=None, offset_scale=None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'VERTICES'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)
        - offset_scale (Float) : socket 'Offset Scale' (id: Offset Scale)

        Returns
        -------
        - Mesh [top_ (Boolean), side_ (Boolean)]
        """
        node = Node('Extrude Mesh', sockets={'Mesh': self, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale}, mode='VERTICES')
        self._jump(node._out)
        return self._domain_to_geometry

    def extrude_edges(self, offset=None, offset_scale=None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'EDGES'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)
        - offset_scale (Float) : socket 'Offset Scale' (id: Offset Scale)

        Returns
        -------
        - Mesh [top_ (Boolean), side_ (Boolean)]
        """
        node = Node('Extrude Mesh', sockets={'Mesh': self, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale}, mode='EDGES')
        self._jump(node._out)
        return self._domain_to_geometry

    def extrude_faces(self, offset=None, offset_scale=None, individual=None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'FACES'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)
        - offset_scale (Float) : socket 'Offset Scale' (id: Offset Scale)
        - individual (Boolean) : socket 'Individual' (id: Individual)

        Returns
        -------
        - Mesh [top_ (Boolean), side_ (Boolean)]
        """
        node = Node('Extrude Mesh', sockets={'Mesh': self, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode='FACES')
        self._jump(node._out)
        return self._domain_to_geometry

    def extrude(self, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)
        - offset_scale (Float) : socket 'Offset Scale' (id: Offset Scale)
        - individual (Boolean) : socket 'Individual' (id: Individual)
        - mode (str): parameter 'mode' in ['VERTICES', 'EDGES', 'FACES']

        Returns
        -------
        - Mesh [top_ (Boolean), side_ (Boolean)]
        """
        utils.check_enum_arg('Extrude Mesh', 'mode', mode, 'extrude', ('VERTICES', 'EDGES', 'FACES'))
        node = Node('Extrude Mesh', sockets={'Mesh': self, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def face_of_corner(cls, corner_index=None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [index_in_face_ (Integer)]
        """
        node = Node('Face of Corner', sockets={'Corner Index': corner_index})
        return node._out

    def flip_faces(self):
        """ > Node <&Node Flip Faces>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Mesh
        """
        node = Node('Flip Faces', sockets={'Mesh': self, 'Selection': self._sel})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def ImportPLY(cls, path=None):
        """ > Node <&Node Import PLY>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import PLY', sockets={'Path': path})
        return cls(node._out)

    @classmethod
    def ImportSTL(cls, path=None):
        """ > Node <&Node Import STL>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import STL', sockets={'Path': path})
        return cls(node._out)

    @classmethod
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - node [unsigned_angle (Float), signed_angle (Float)]
        """
        node = Node('Edge Angle', sockets={})
        return node

    @classmethod
    @property
    def unsigned_edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - unsigned_angle
        """
        node = Node('Edge Angle', sockets={})
        return node.unsigned_angle

    @classmethod
    @property
    def signed_edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - signed_angle
        """
        node = Node('Edge Angle', sockets={})
        return node.signed_angle

    @classmethod
    @property
    def edge_neighbors(cls):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        - Integer
        """
        node = Node('Edge Neighbors', sockets={})
        return node._out

    @classmethod
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - node [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """
        node = Node('Edge Vertices', sockets={})
        return node

    @classmethod
    @property
    def face_area(cls):
        """ > Node <&Node Face Area>

        Returns
        -------
        - Float
        """
        node = Node('Face Area', sockets={})
        return node._out

    @classmethod
    def is_face_planar(cls, threshold=None):
        """ > Node <&Node Is Face Planar>

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Boolean
        """
        node = Node('Is Face Planar', sockets={'Threshold': threshold})
        return node._out

    @classmethod
    def face_neighbors(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        - node [vertex_count (Integer), face_count (Integer)]
        """
        node = Node('Face Neighbors', sockets={})
        return node

    @classmethod
    def mesh_island(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        - node [island_index (Integer), island_count (Integer)]
        """
        node = Node('Mesh Island', sockets={})
        return node

    @classmethod
    @property
    def island_index(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        - island_index
        """
        node = Node('Mesh Island', sockets={})
        return node.island_index

    @classmethod
    @property
    def island_count(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        - island_count
        """
        node = Node('Mesh Island', sockets={})
        return node.island_count

    @classmethod
    def vertex_neighbors(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        - node [vertex_count (Integer), face_count (Integer)]
        """
        node = Node('Vertex Neighbors', sockets={})
        return node

    @classmethod
    @property
    def normal(cls):
        """ > Node <&Node Normal>

        Returns
        -------
        - Vector
        """
        node = Node('Normal', sockets={})
        return node._out

    @classmethod
    def shortest_edge_paths(cls, end_vertex=None, edge_cost=None):
        """ > Node <&Node Shortest Edge Paths>

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (id: End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (id: Edge Cost)

        Returns
        -------
        - Integer [total_cost_ (Float)]
        """
        node = Node('Shortest Edge Paths', sockets={'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node._out

    @classmethod
    def material_selection(cls, material=None):
        """ > Node <&Node Material Selection>

        Arguments
        ---------
        - material (Material) : socket 'Material' (id: Material)

        Returns
        -------
        - Boolean
        """
        node = Node('Material Selection', sockets={'Material': material})
        return node._out

    def boolean(self, *mesh_2, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh 1' : self

        Arguments
        ---------
        - mesh_2 (Geometry) : socket 'Mesh 2' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - operation (str): parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'operation', operation, 'boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'boolean', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 1': self, 'Mesh 2': list(mesh_2), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation=operation, solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Boolean(cls, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Arguments
        ---------
        - mesh_1 (Geometry) : socket 'Mesh 1' (id: Mesh 1)
        - mesh_2 (Geometry) : socket 'Mesh 2' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - operation (str): parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'operation', operation, 'Boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Boolean', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 1': mesh_1, 'Mesh 2': list(mesh_2), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation=operation, solver=solver)
        return cls(node._out)

    def intersect(self, *mesh, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Parameter 'operation' : 'INTERSECT'

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'intersect', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 2': [self] + list(mesh), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation='INTERSECT', solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    def union(self, *mesh, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Parameter 'operation' : 'UNION'

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'union', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 2': [self] + list(mesh), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation='UNION', solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    def difference(self, *mesh_2, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh 1' : self
        - Parameter 'operation' : 'DIFFERENCE'

        Arguments
        ---------
        - mesh_2 (Geometry) : socket 'Mesh 2' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'difference', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 1': self, 'Mesh 2': list(mesh_2), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation='DIFFERENCE', solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Intersect(cls, *mesh, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Information
        -----------
        - Parameter 'operation' : 'INTERSECT'

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Intersect', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 2': list(mesh), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation='INTERSECT', solver=solver)
        return cls(node._out)

    @classmethod
    def Union(cls, *mesh, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Information
        -----------
        - Parameter 'operation' : 'UNION'

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Union', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 2': list(mesh), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation='UNION', solver=solver)
        return cls(node._out)

    @classmethod
    def Difference(cls, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Information
        -----------
        - Parameter 'operation' : 'DIFFERENCE'

        Arguments
        ---------
        - mesh_1 (Geometry) : socket 'Mesh 1' (id: Mesh 1)
        - mesh_2 (Geometry) : socket 'Mesh 2' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Difference', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 1': mesh_1, 'Mesh 2': list(mesh_2), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation='DIFFERENCE', solver=solver)
        return cls(node._out)

    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
        """ > Node <&Node Mesh Circle>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (id: Vertices)
        - radius (Float) : socket 'Radius' (id: Radius)
        - fill_type (str): parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Circle', 'fill_type', fill_type, 'Circle', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Mesh Circle', sockets={'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)
        return cls(node._out)

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """ > Node <&Node Cone>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (id: Vertices)
        - side_segments (Integer) : socket 'Side Segments' (id: Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (id: Fill Segments)
        - radius_top (Float) : socket 'Radius Top' (id: Radius Top)
        - radius_bottom (Float) : socket 'Radius Bottom' (id: Radius Bottom)
        - depth (Float) : socket 'Depth' (id: Depth)
        - fill_type (str): parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Cone', 'fill_type', fill_type, 'Cone', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Cone', sockets={'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)
        return cls(node._out)

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """ > Node <&Node Cube>

        Arguments
        ---------
        - size (Vector) : socket 'Size' (id: Size)
        - vertices_x (Integer) : socket 'Vertices X' (id: Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (id: Vertices Y)
        - vertices_z (Integer) : socket 'Vertices Z' (id: Vertices Z)

        Returns
        -------
        - Mesh
        """
        node = Node('Cube', sockets={'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})
        return cls(node._out)

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """ > Node <&Node Cylinder>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (id: Vertices)
        - side_segments (Integer) : socket 'Side Segments' (id: Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (id: Fill Segments)
        - radius (Float) : socket 'Radius' (id: Radius)
        - depth (Float) : socket 'Depth' (id: Depth)
        - fill_type (str): parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Cylinder', 'fill_type', fill_type, 'Cylinder', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Cylinder', sockets={'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius': radius, 'Depth': depth}, fill_type=fill_type)
        return cls(node._out)

    @classmethod
    def face_group_boundaries(cls, face_group_id=None):
        """ > Node <&Node Face Group Boundaries>

        Arguments
        ---------
        - face_group_id (Integer) : socket 'Face Group ID' (id: Face Set)

        Returns
        -------
        - Boolean
        """
        node = Node('Face Group Boundaries', sockets={'Face Set': face_group_id})
        return node._out

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """ > Node <&Node Grid>

        Arguments
        ---------
        - size_x (Float) : socket 'Size X' (id: Size X)
        - size_y (Float) : socket 'Size Y' (id: Size Y)
        - vertices_x (Integer) : socket 'Vertices X' (id: Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (id: Vertices Y)

        Returns
        -------
        - Mesh
        """
        node = Node('Grid', sockets={'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})
        return cls(node._out)

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        """ > Node <&Node Ico Sphere>

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - subdivisions (Integer) : socket 'Subdivisions' (id: Subdivisions)

        Returns
        -------
        - Mesh
        """
        node = Node('Ico Sphere', sockets={'Radius': radius, 'Subdivisions': subdivisions})
        return cls(node._out)

    @classmethod
    def LineOffset(cls, count=None, start_location=None, offset=None, count_mode='TOTAL'):
        """ > Node <&Node Mesh Line>

        Information
        -----------
        - Parameter 'mode' : 'OFFSET'

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - start_location (Vector) : socket 'Start Location' (id: Start Location)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - count_mode (str): parameter 'count_mode' in ['TOTAL', 'RESOLUTION']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Line', 'count_mode', count_mode, 'LineOffset', ('TOTAL', 'RESOLUTION'))
        node = Node('Mesh Line', sockets={'Count': count, 'Start Location': start_location, 'Offset': offset}, count_mode=count_mode, mode='OFFSET')
        return cls(node._out)

    @classmethod
    def LineEndPoints(cls, count=None, start_location=None, end_location=None, count_mode='TOTAL'):
        """ > Node <&Node Mesh Line>

        Information
        -----------
        - Parameter 'mode' : 'END_POINTS'

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - start_location (Vector) : socket 'Start Location' (id: Start Location)
        - end_location (Vector) : socket 'End Location' (id: Offset)
        - count_mode (str): parameter 'count_mode' in ['TOTAL', 'RESOLUTION']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Line', 'count_mode', count_mode, 'LineEndPoints', ('TOTAL', 'RESOLUTION'))
        node = Node('Mesh Line', sockets={'Count': count, 'Start Location': start_location, 'Offset': end_location}, count_mode=count_mode, mode='END_POINTS')
        return cls(node._out)

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """ > Node <&Node Mesh Line>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - start_location (Vector) : socket 'Start Location' (id: Start Location)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - count_mode (str): parameter 'count_mode' in ['TOTAL', 'RESOLUTION']
        - mode (str): parameter 'mode' in ['OFFSET', 'END_POINTS']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Line', 'count_mode', count_mode, 'Line', ('TOTAL', 'RESOLUTION'))
        utils.check_enum_arg('Mesh Line', 'mode', mode, 'Line', ('OFFSET', 'END_POINTS'))
        node = Node('Mesh Line', sockets={'Count': count, 'Start Location': start_location, 'Offset': offset}, count_mode=count_mode, mode=mode)
        return cls(node._out)

    def to_curve(self):
        """ > Node <&Node Mesh to Curve>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Curve
        """
        node = Node('Mesh to Curve', sockets={'Mesh': self, 'Selection': self._sel})
        return node._out

    def to_density_grid(self, density=None, voxel_size=None, gradient_width=None):
        """ > Node <&Node Mesh to Density Grid>

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - gradient_width (Float) : socket 'Gradient Width' (id: Gradient Width)

        Returns
        -------
        - Float
        """
        node = Node('Mesh to Density Grid', sockets={'Mesh': self, 'Density': density, 'Voxel Size': voxel_size, 'Gradient Width': gradient_width})
        return node._out

    def to_points(self, position=None, radius=None, mode='VERTICES'):
        """ > Node <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)
        - mode (str): parameter 'mode' in ['VERTICES', 'EDGES', 'FACES', 'CORNERS']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Mesh to Points', 'mode', mode, 'to_points', ('VERTICES', 'EDGES', 'FACES', 'CORNERS'))
        node = Node('Mesh to Points', sockets={'Mesh': self, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode=mode)
        return node._out

    def vertices_to_points(self, position=None, radius=None):
        """ > Node <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'VERTICES'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Mesh to Points', sockets={'Mesh': self, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode='VERTICES')
        return node._out

    def edges_to_points(self, position=None, radius=None):
        """ > Node <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'EDGES'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Mesh to Points', sockets={'Mesh': self, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode='EDGES')
        return node._out

    def faces_to_points(self, position=None, radius=None):
        """ > Node <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'FACES'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Mesh to Points', sockets={'Mesh': self, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode='FACES')
        return node._out

    def corners_to_points(self, position=None, radius=None):
        """ > Node <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'CORNERS'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Mesh to Points', sockets={'Mesh': self, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode='CORNERS')
        return node._out

    def to_sdf_grid(self, voxel_size=None, band_width=None):
        """ > Node <&Node Mesh to SDF Grid>

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - band_width (Integer) : socket 'Band Width' (id: Band Width)

        Returns
        -------
        - Float
        """
        node = Node('Mesh to SDF Grid', sockets={'Mesh': self, 'Voxel Size': voxel_size, 'Band Width': band_width})
        return node._out

    def to_volume(self, density=None, voxel_amount=None, interior_band_width=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node <&Node Mesh to Volume>

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - interior_band_width (Float) : socket 'Interior Band Width' (id: Interior Band Width)
        - resolution_mode (str): parameter 'resolution_mode' in ['VOXEL_AMOUNT', 'VOXEL_SIZE']

        Returns
        -------
        - Volume
        """
        utils.check_enum_arg('Mesh to Volume', 'resolution_mode', resolution_mode, 'to_volume', ('VOXEL_AMOUNT', 'VOXEL_SIZE'))
        node = Node('Mesh to Volume', sockets={'Mesh': self, 'Density': density, 'Voxel Amount': voxel_amount, 'Interior Band Width': interior_band_width}, resolution_mode=resolution_mode)
        return node._out

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        """ > Node <&Node UV Sphere>

        Arguments
        ---------
        - segments (Integer) : socket 'Segments' (id: Segments)
        - rings (Integer) : socket 'Rings' (id: Rings)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Mesh
        """
        node = Node('UV Sphere', sockets={'Segments': segments, 'Rings': rings, 'Radius': radius})
        return cls(node._out)

    @classmethod
    def offset_corner_in_face(cls, corner_index=None, offset=None):
        """ > Node <&Node Offset Corner in Face>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Integer
        """
        node = Node('Offset Corner in Face', sockets={'Corner Index': corner_index, 'Offset': offset})
        return node._out

    def sample_nearest_surface(self, value=None, group_id=None, sample_position=None, sample_group_id=None):
        """ > Node <&Node Sample Nearest Surface>

        Information
        -----------
        - Socket 'Mesh' : self
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)

        Returns
        -------
        - Float [is_valid_ (Boolean)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Mesh.sample_nearest_surface', 'value')
        node = Node('Sample Nearest Surface', sockets={'Mesh': self, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=data_type)
        return node._out

    def sample_uv_surface(self, value=None, uv_map=None, sample_uv=None):
        """ > Node <&Node Sample UV Surface>

        Information
        -----------
        - Socket 'Mesh' : self
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - uv_map (Vector) : socket 'UV Map' (id: Source UV Map)
        - sample_uv (Vector) : socket 'Sample UV' (id: Sample UV)

        Returns
        -------
        - Float [is_valid_ (Boolean)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Mesh.sample_uv_surface', 'value')
        node = Node('Sample UV Surface', sockets={'Mesh': self, 'Value': value, 'Source UV Map': uv_map, 'Sample UV': sample_uv}, data_type=data_type)
        return node._out

    def split_edges(self):
        """ > Node <&Node Split Edges>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Mesh
        """
        node = Node('Split Edges', sockets={'Mesh': self, 'Selection': self._sel})
        self._jump(node._out)
        return self._domain_to_geometry

    def subdivide(self, level=None):
        """ > Node <&Node Subdivide Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - level (Integer) : socket 'Level' (id: Level)

        Returns
        -------
        - Mesh
        """
        node = Node('Subdivide Mesh', sockets={'Mesh': self, 'Level': level})
        self._jump(node._out)
        return self._domain_to_geometry

    def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """ > Node <&Node Subdivision Surface>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - level (Integer) : socket 'Level' (id: Level)
        - edge_crease (Float) : socket 'Edge Crease' (id: Edge Crease)
        - vertex_crease (Float) : socket 'Vertex Crease' (id: Vertex Crease)
        - boundary_smooth (str): parameter 'boundary_smooth' in ['PRESERVE_CORNERS', 'ALL']
        - uv_smooth (str): parameter 'uv_smooth' in ['NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Subdivision Surface', 'boundary_smooth', boundary_smooth, 'subdivision_surface', ('PRESERVE_CORNERS', 'ALL'))
        utils.check_enum_arg('Subdivision Surface', 'uv_smooth', uv_smooth, 'subdivision_surface', ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL'))
        node = Node('Subdivision Surface', sockets={'Mesh': self, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease}, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_face_set(self, face_set=None):
        """ > Node <&Node Set Face Set>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - face_set (Integer) : socket 'Face Set' (id: Face Set)

        Returns
        -------
        - Mesh
        """
        node = Node('Set Face Set', sockets={'Mesh': self, 'Selection': self._sel, 'Face Set': face_set})
        self._jump(node._out)
        return self._domain_to_geometry

    def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ > Node <&Node Triangulate>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - minimum_vertices (Integer) : socket 'Minimum Vertices' (id: Minimum Vertices)
        - ngon_method (str): parameter 'ngon_method' in ['BEAUTY', 'CLIP']
        - quad_method (str): parameter 'quad_method' in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Triangulate', 'ngon_method', ngon_method, 'triangulate', ('BEAUTY', 'CLIP'))
        utils.check_enum_arg('Triangulate', 'quad_method', quad_method, 'triangulate', ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL'))
        node = Node('Triangulate', sockets={'Mesh': self, 'Selection': self._sel, 'Minimum Vertices': minimum_vertices}, ngon_method=ngon_method, quad_method=quad_method)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def vertex_of_corner(cls, corner_index=None):
        """ > Node <&Node Vertex of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer
        """
        node = Node('Vertex of Corner', sockets={'Corner Index': corner_index})
        return node._out

