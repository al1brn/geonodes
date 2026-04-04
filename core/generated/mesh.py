# Generated 2026-04-04 12:37:35

from __future__ import annotations
from .. sockettype import SocketType
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Mesh(Socket):

    __slots__ = ()

    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Geometry    | `self`   |
        | Parameter | `component` | `'MESH'` |

        Returns
        -------
        Integer
            peer sockets: edge_count_ (Integer), face_count_ (Integer), face_corner_count_ (Integer)

        """
        node = self._cache('Domain Size', {'Geometry': self}, component='MESH')
        return node._out

    @classmethod
    def corners_of_edge(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Parameters
        ---------
        edge_index : Integer, optional
            socket 'Edge Index' (id: Edge Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_face(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Face>

        Parameters
        ---------
        face_index : Integer, optional
            socket 'Face Index' (id: Face Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Corners of Face', {'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_vertex(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Vertex>

        Parameters
        ---------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    def distribute_points_on_faces(self,
                    density: Float = None,
                    seed: Integer = None,
                    distribute_method: Literal['RANDOM', 'POISSON'] = 'RANDOM'):
        """ > Node <&Node Distribute Points on Faces>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ---------
        density : Float, optional
            socket 'Density' (id: Density)
        
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        
        distribute_method (str): parameter 'distribute_method' in ('Random', 'Poisson Disk')

        Returns
        -------
        Cloud
            peer sockets: normal_ (Vector), rotation_ (Rotation)

        """
        utils.check_enum_arg('Distribute Points on Faces', 'distribute_method', distribute_method, 'distribute_points_on_faces', ('RANDOM', 'POISSON'))
        node = Node('Distribute Points on Faces', {'Mesh': self, 'Selection': self.get_selection(), 'Density': density, 'Seed': seed}, distribute_method=distribute_method)
        return node._out

    def distribute_points_on_faces_random(self, density: Float = None, seed: Integer = None):
        """ > Node <&Node Distribute Points on Faces>

        **Fixed values**

        | Kind      | Name                | Value             |
        | --------- | ------------------- | ----------------- |
        | Socket    | Mesh                | `self`            |
        | Socket    | Selection           | `self[selection]` |
        | Parameter | `distribute_method` | `'RANDOM'`        |

        Parameters
        ---------
        density : Float, optional
            socket 'Density' (id: Density)
        
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Cloud
            peer sockets: normal_ (Vector), rotation_ (Rotation)

        """
        node = Node('Distribute Points on Faces', {'Mesh': self, 'Selection': self.get_selection(), 'Density': density, 'Seed': seed}, distribute_method='RANDOM')
        return node._out

    def distribute_points_on_faces_poisson(self,
                    distance_min: Float = None,
                    density_max: Float = None,
                    density_factor: Float = None,
                    seed: Integer = None):
        """ > Node <&Node Distribute Points on Faces>

        **Fixed values**

        | Kind      | Name                | Value             |
        | --------- | ------------------- | ----------------- |
        | Socket    | Mesh                | `self`            |
        | Socket    | Selection           | `self[selection]` |
        | Parameter | `distribute_method` | `'POISSON'`       |

        Parameters
        ---------
        distance_min : Float, optional
            socket 'Distance Min' (id: Distance Min)
        
        density_max : Float, optional
            socket 'Density Max' (id: Density Max)
        
        density_factor : Float, optional
            socket 'Density Factor' (id: Density Factor)
        
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Cloud
            peer sockets: normal_ (Vector), rotation_ (Rotation)

        """
        node = Node('Distribute Points on Faces', {'Mesh': self, 'Selection': self.get_selection(), 'Distance Min': distance_min, 'Density Max': density_max, 'Density Factor': density_factor, 'Seed': seed}, distribute_method='POISSON')
        return node._out

    def dual(self, keep_boundaries: Boolean = None):
        """ > Node <&Node Dual Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        keep_boundaries : Boolean, optional
            socket 'Keep Boundaries' (id: Keep Boundaries)
        

        Returns
        -------
        Mesh
        """
        node = Node('Dual Mesh', {'Mesh': self, 'Keep Boundaries': keep_boundaries})
        self._jump(node._out)
        return self._domain_to_geometry

    def edge_paths_to_curves(self, start_vertices: Boolean = None, next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Curves>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        start_vertices : Boolean, optional
            socket 'Start Vertices' (id: Start Vertices)
        
        next_vertex_index : Integer, optional
            socket 'Next Vertex Index' (id: Next Vertex Index)
        

        Returns
        -------
        Curve
        """
        node = Node('Edge Paths to Curves', {'Mesh': self, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edge_paths_to_selection(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Selection>

        Parameters
        ---------
        start_vertices : Boolean, optional
            socket 'Start Vertices' (id: Start Vertices)
        
        next_vertex_index : Integer, optional
            socket 'Next Vertex Index' (id: Next Vertex Index)
        

        Returns
        -------
        Boolean
        """
        node = Node('Edge Paths to Selection', {'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edges_of_corner(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Parameters
        ---------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        Integer
            peer sockets: previous_edge_index_ (Integer)

        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def edges_of_vertex(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Edges of Vertex>

        Parameters
        ---------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def edges_to_face_groups(cls, boundary_edges: Boolean = None):
        """ > Node <&Node Edges to Face Groups>

        Parameters
        ---------
        boundary_edges : Boolean, optional
            socket 'Boundary Edges' (id: Boundary Edges)
        

        Returns
        -------
        Integer
        """
        node = Node('Edges to Face Groups', {'Boundary Edges': boundary_edges})
        return node._out

    def extrude_vertices(self, offset: Vector = None, offset_scale: Float = None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'VERTICES'`      |

        Parameters
        ---------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        offset_scale : Float, optional
            socket 'Offset Scale' (id: Offset Scale)
        

        Returns
        -------
        Mesh
            peer sockets: top_ (Boolean), side_ (Boolean)

        """
        node = Node('Extrude Mesh', {'Mesh': self, 'Selection': self.get_selection(), 'Offset': offset, 'Offset Scale': offset_scale}, mode='VERTICES')
        self._jump(node._out)
        return self._domain_to_geometry

    def extrude_edges(self, offset: Vector = None, offset_scale: Float = None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'EDGES'`         |

        Parameters
        ---------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        offset_scale : Float, optional
            socket 'Offset Scale' (id: Offset Scale)
        

        Returns
        -------
        Mesh
            peer sockets: top_ (Boolean), side_ (Boolean)

        """
        node = Node('Extrude Mesh', {'Mesh': self, 'Selection': self.get_selection(), 'Offset': offset, 'Offset Scale': offset_scale}, mode='EDGES')
        self._jump(node._out)
        return self._domain_to_geometry

    def extrude_faces(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'FACES'`         |

        Parameters
        ---------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        offset_scale : Float, optional
            socket 'Offset Scale' (id: Offset Scale)
        
        individual : Boolean, optional
            socket 'Individual' (id: Individual)
        

        Returns
        -------
        Mesh
            peer sockets: top_ (Boolean), side_ (Boolean)

        """
        node = Node('Extrude Mesh', {'Mesh': self, 'Selection': self.get_selection(), 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode='FACES')
        self._jump(node._out)
        return self._domain_to_geometry

    def extrude(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES'] = 'FACES'):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ---------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        offset_scale : Float, optional
            socket 'Offset Scale' (id: Offset Scale)
        
        individual : Boolean, optional
            socket 'Individual' (id: Individual)
        
        mode (str): parameter 'mode' in ('Vertices', 'Edges', 'Faces')

        Returns
        -------
        Mesh
            peer sockets: top_ (Boolean), side_ (Boolean)

        """
        utils.check_enum_arg('Extrude Mesh', 'mode', mode, 'extrude', ('VERTICES', 'EDGES', 'FACES'))
        node = Node('Extrude Mesh', {'Mesh': self, 'Selection': self.get_selection(), 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def face_of_corner(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Parameters
        ---------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        Integer
            peer sockets: index_in_face_ (Integer)

        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node._out

    def flip_faces(self):
        """ > Node <&Node Flip Faces>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Returns
        -------
        Mesh
        """
        node = Node('Flip Faces', {'Mesh': self, 'Selection': self.get_selection()})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def ImportPLY(cls, path: String = None):
        """ > Node <&Node Import PLY>

        Parameters
        ---------
        path : String, optional
            socket 'Path' (id: Path)
        

        Returns
        -------
        Mesh
        """
        node = Node('Import PLY', {'Path': path})
        return cls(node._out)

    @classmethod
    def ImportSTL(cls, path: String = None):
        """ > Node <&Node Import STL>

        Parameters
        ---------
        path : String, optional
            socket 'Path' (id: Path)
        

        Returns
        -------
        Mesh
        """
        node = Node('Import STL', {'Path': path})
        return cls(node._out)

    @utils.classproperty
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        Float
            peer sockets: signed_angle_ (Float)

        """
        node = Node('Edge Angle', )
        return node._out

    @utils.classproperty
    def unsigned_edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        unsigned_angle
        """
        node = Node('Edge Angle', )
        return node.unsigned_angle

    @utils.classproperty
    def signed_edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        signed_angle
        """
        node = Node('Edge Angle', )
        return node.signed_angle

    @utils.classproperty
    def edge_neighbors(cls):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        Integer
        """
        node = Node('Edge Neighbors', )
        return node._out

    @utils.classproperty
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        Integer
            peer sockets: vertex_index_2_ (Integer), position_1_ (Vector), position_2_ (Vector)

        """
        node = Node('Edge Vertices', )
        return node._out

    @utils.classproperty
    def face_area(cls):
        """ > Node <&Node Face Area>

        Returns
        -------
        Float
        """
        node = Node('Face Area', )
        return node._out

    @classmethod
    def is_face_planar(cls, threshold: Float = None):
        """ > Node <&Node Is Face Planar>

        Parameters
        ---------
        threshold : Float, optional
            socket 'Threshold' (id: Threshold)
        

        Returns
        -------
        Boolean
        """
        node = Node('Is Face Planar', {'Threshold': threshold})
        return node._out

    @utils.classproperty
    def face_neighbors(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        Integer
            peer sockets: face_count_ (Integer)

        """
        node = Node('Face Neighbors', )
        return node._out

    @utils.classproperty
    def mesh_island(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        Integer
            peer sockets: island_count_ (Integer)

        """
        node = Node('Mesh Island', )
        return node._out

    @utils.classproperty
    def island_index(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        island_index
        """
        node = Node('Mesh Island', )
        return node.island_index

    @utils.classproperty
    def island_count(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        island_count
        """
        node = Node('Mesh Island', )
        return node.island_count

    @utils.classproperty
    def vertex_neighbors(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        Integer
            peer sockets: face_count_ (Integer)

        """
        node = Node('Vertex Neighbors', )
        return node._out

    @classmethod
    def shortest_edge_paths(cls, end_vertex: Boolean = None, edge_cost: Float = None):
        """ > Node <&Node Shortest Edge Paths>

        Parameters
        ---------
        end_vertex : Boolean, optional
            socket 'End Vertex' (id: End Vertex)
        
        edge_cost : Float, optional
            socket 'Edge Cost' (id: Edge Cost)
        

        Returns
        -------
        Integer
            peer sockets: total_cost_ (Float)

        """
        node = Node('Shortest Edge Paths', {'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node._out

    @classmethod
    def material_selection(cls, material: Material = None):
        """ > Node <&Node Material Selection>

        Parameters
        ---------
        material : Material, optional
            socket 'Material' (id: Material)
        

        Returns
        -------
        Boolean
        """
        node = Node('Material Selection', {'Material': material})
        return node._out

    def boolean(self,
                    *mesh_2: Mesh,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Mesh 1 | `self` |

        Parameters
        ---------
        mesh_2 : Mesh, optional
            socket 'Mesh 2' (id: Mesh 2)
        
        operation (str): parameter 'operation' in ('Intersect', 'Union', 'Difference')
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'operation', operation, 'boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'boolean', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 1': self, 'Mesh 2': list(mesh_2)}, operation=operation, solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Boolean(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Parameters
        ---------
        mesh_1 : Mesh, optional
            socket 'Mesh 1' (id: Mesh 1)
        
        mesh_2 : Mesh, optional
            socket 'Mesh 2' (id: Mesh 2)
        
        operation (str): parameter 'operation' in ('Intersect', 'Union', 'Difference')
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'operation', operation, 'Boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Boolean', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 1': mesh_1, 'Mesh 2': list(mesh_2)}, operation=operation, solver=solver)
        return cls(node._out)

    def intersect(self, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Parameter | `operation` | `'INTERSECT'` |

        Parameters
        ---------
        mesh : Mesh, optional
            socket 'Mesh' (id: Mesh 2)
        
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'intersect', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 2': [self] + list(mesh)}, operation='INTERSECT', solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    def union(self, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Parameter | `operation` | `'UNION'` |

        Parameters
        ---------
        mesh : Mesh, optional
            socket 'Mesh' (id: Mesh 2)
        
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'union', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 2': [self] + list(mesh)}, operation='UNION', solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    def difference(self, *mesh_2: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Socket    | Mesh 1      | `self`         |
        | Parameter | `operation` | `'DIFFERENCE'` |

        Parameters
        ---------
        mesh_2 : Mesh, optional
            socket 'Mesh 2' (id: Mesh 2)
        
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'difference', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 1': self, 'Mesh 2': list(mesh_2)}, operation='DIFFERENCE', solver=solver)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Intersect(cls, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Parameter | `operation` | `'INTERSECT'` |

        Parameters
        ---------
        mesh : Mesh, optional
            socket 'Mesh' (id: Mesh 2)
        
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Intersect', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 2': list(mesh)}, operation='INTERSECT', solver=solver)
        return cls(node._out)

    @classmethod
    def Union(cls, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Parameter | `operation` | `'UNION'` |

        Parameters
        ---------
        mesh : Mesh, optional
            socket 'Mesh' (id: Mesh 2)
        
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Union', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 2': list(mesh)}, operation='UNION', solver=solver)
        return cls(node._out)

    @classmethod
    def Difference(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Parameter | `operation` | `'DIFFERENCE'` |

        Parameters
        ---------
        mesh_1 : Mesh, optional
            socket 'Mesh 1' (id: Mesh 1)
        
        mesh_2 : Mesh, optional
            socket 'Mesh 2' (id: Mesh 2)
        
        solver (str): parameter 'solver' in ('Exact', 'Float', 'Manifold')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'Difference', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 1': mesh_1, 'Mesh 2': list(mesh_2)}, operation='DIFFERENCE', solver=solver)
        return cls(node._out)

    @classmethod
    def Circle(cls,
                    vertices: Integer = None,
                    radius: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NONE'):
        """ > Node <&Node Mesh Circle>

        Parameters
        ---------
        vertices : Integer, optional
            socket 'Vertices' (id: Vertices)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        fill_type (str): parameter 'fill_type' in ('None', 'N-Gon', 'Triangles')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Circle', 'fill_type', fill_type, 'Circle', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Mesh Circle', {'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)
        return cls(node._out)

    @classmethod
    def Cone(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius_top: Float = None,
                    radius_bottom: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON'):
        """ > Node <&Node Cone>

        Parameters
        ---------
        vertices : Integer, optional
            socket 'Vertices' (id: Vertices)
        
        side_segments : Integer, optional
            socket 'Side Segments' (id: Side Segments)
        
        fill_segments : Integer, optional
            socket 'Fill Segments' (id: Fill Segments)
        
        radius_top : Float, optional
            socket 'Radius Top' (id: Radius Top)
        
        radius_bottom : Float, optional
            socket 'Radius Bottom' (id: Radius Bottom)
        
        depth : Float, optional
            socket 'Depth' (id: Depth)
        
        fill_type (str): parameter 'fill_type' in ('None', 'N-Gon', 'Triangles')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Cone', 'fill_type', fill_type, 'Cone', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Cone', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)
        return cls(node._out)

    @classmethod
    def Cube(cls,
                    size: Vector = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None,
                    vertices_z: Integer = None):
        """ > Node <&Node Cube>

        Parameters
        ---------
        size : Vector, optional
            socket 'Size' (id: Size)
        
        vertices_x : Integer, optional
            socket 'Vertices X' (id: Vertices X)
        
        vertices_y : Integer, optional
            socket 'Vertices Y' (id: Vertices Y)
        
        vertices_z : Integer, optional
            socket 'Vertices Z' (id: Vertices Z)
        

        Returns
        -------
        Mesh
        """
        node = Node('Cube', {'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})
        return cls(node._out)

    @classmethod
    def Cylinder(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON'):
        """ > Node <&Node Cylinder>

        Parameters
        ---------
        vertices : Integer, optional
            socket 'Vertices' (id: Vertices)
        
        side_segments : Integer, optional
            socket 'Side Segments' (id: Side Segments)
        
        fill_segments : Integer, optional
            socket 'Fill Segments' (id: Fill Segments)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        depth : Float, optional
            socket 'Depth' (id: Depth)
        
        fill_type (str): parameter 'fill_type' in ('None', 'N-Gon', 'Triangles')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Cylinder', 'fill_type', fill_type, 'Cylinder', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Cylinder', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius': radius, 'Depth': depth}, fill_type=fill_type)
        return cls(node._out)

    @classmethod
    def face_group_boundaries(cls, face_group_id: Integer = None):
        """ > Node <&Node Face Group Boundaries>

        Parameters
        ---------
        face_group_id : Integer, optional
            socket 'Face Group ID' (id: Face Set)
        

        Returns
        -------
        Boolean
        """
        node = Node('Face Group Boundaries', {'Face Set': face_group_id})
        return node._out

    @classmethod
    def Grid(cls,
                    size_x: Float = None,
                    size_y: Float = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None):
        """ > Node <&Node Grid>

        Parameters
        ---------
        size_x : Float, optional
            socket 'Size X' (id: Size X)
        
        size_y : Float, optional
            socket 'Size Y' (id: Size Y)
        
        vertices_x : Integer, optional
            socket 'Vertices X' (id: Vertices X)
        
        vertices_y : Integer, optional
            socket 'Vertices Y' (id: Vertices Y)
        

        Returns
        -------
        Mesh
        """
        node = Node('Grid', {'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})
        return cls(node._out)

    @classmethod
    def IcoSphere(cls, radius: Float = None, subdivisions: Integer = None):
        """ > Node <&Node Ico Sphere>

        Parameters
        ---------
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        subdivisions : Integer, optional
            socket 'Subdivisions' (id: Subdivisions)
        

        Returns
        -------
        Mesh
        """
        node = Node('Ico Sphere', {'Radius': radius, 'Subdivisions': subdivisions})
        return cls(node._out)

    @classmethod
    def LineOffset(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL'):
        """ > Node <&Node Mesh Line>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'OFFSET'` |

        Parameters
        ---------
        count : Integer, optional
            socket 'Count' (id: Count)
        
        start_location : Vector, optional
            socket 'Start Location' (id: Start Location)
        
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        count_mode (str): parameter 'count_mode' in ('Count', 'Resolution')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Line', 'count_mode', count_mode, 'LineOffset', ('TOTAL', 'RESOLUTION'))
        node = Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': offset}, count_mode=count_mode, mode='OFFSET')
        return cls(node._out)

    @classmethod
    def LineEndPoints(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    end_location: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL'):
        """ > Node <&Node Mesh Line>

        **Fixed values**

        | Kind      | Name   | Value          |
        | --------- | ------ | -------------- |
        | Parameter | `mode` | `'END_POINTS'` |

        Parameters
        ---------
        count : Integer, optional
            socket 'Count' (id: Count)
        
        start_location : Vector, optional
            socket 'Start Location' (id: Start Location)
        
        end_location : Vector, optional
            socket 'End Location' (id: Offset)
        
        count_mode (str): parameter 'count_mode' in ('Count', 'Resolution')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Line', 'count_mode', count_mode, 'LineEndPoints', ('TOTAL', 'RESOLUTION'))
        node = Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': end_location}, count_mode=count_mode, mode='END_POINTS')
        return cls(node._out)

    @classmethod
    def Line(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL',
                    mode: Literal['OFFSET', 'END_POINTS'] = 'OFFSET'):
        """ > Node <&Node Mesh Line>

        Parameters
        ---------
        count : Integer, optional
            socket 'Count' (id: Count)
        
        start_location : Vector, optional
            socket 'Start Location' (id: Start Location)
        
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        count_mode (str): parameter 'count_mode' in ('Count', 'Resolution')
        mode (str): parameter 'mode' in ('Offset', 'End Points')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Mesh Line', 'count_mode', count_mode, 'Line', ('TOTAL', 'RESOLUTION'))
        utils.check_enum_arg('Mesh Line', 'mode', mode, 'Line', ('OFFSET', 'END_POINTS'))
        node = Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': offset}, count_mode=count_mode, mode=mode)
        return cls(node._out)

    def to_curve_edges(self):
        """ > Node <&Node Mesh to Curve>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'EDGES'`         |

        Returns
        -------
        Curve
        """
        node = Node('Mesh to Curve', {'Mesh': self, 'Selection': self.get_selection()}, mode='EDGES')
        return node._out

    def to_curve_faces(self):
        """ > Node <&Node Mesh to Curve>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'FACES'`         |

        Returns
        -------
        Curve
        """
        node = Node('Mesh to Curve', {'Mesh': self, 'Selection': self.get_selection()}, mode='FACES')
        return node._out

    def to_curve(self, mode: Literal['EDGES', 'FACES'] = 'EDGES'):
        """ > Node <&Node Mesh to Curve>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ---------
        mode (str): parameter 'mode' in ('Edges', 'Faces')

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Mesh to Curve', 'mode', mode, 'to_curve', ('EDGES', 'FACES'))
        node = Node('Mesh to Curve', {'Mesh': self, 'Selection': self.get_selection()}, mode=mode)
        return node._out

    def to_points(self,
                    position: Vector = None,
                    radius: Float = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS'] = 'VERTICES'):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ---------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        mode (str): parameter 'mode' in ('Vertices', 'Edges', 'Faces', 'Corners')

        Returns
        -------
        Cloud
        """
        utils.check_enum_arg('Mesh to Points', 'mode', mode, 'to_points', ('VERTICES', 'EDGES', 'FACES', 'CORNERS'))
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode=mode)
        return node._out

    def vertices_to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'VERTICES'`      |

        Parameters
        ---------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='VERTICES')
        return node._out

    def edges_to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'EDGES'`         |

        Parameters
        ---------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='EDGES')
        return node._out

    def faces_to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'FACES'`         |

        Parameters
        ---------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='FACES')
        return node._out

    def corners_to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'CORNERS'`       |

        Parameters
        ---------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='CORNERS')
        return node._out

    def to_volume(self,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    interior_band_width: Float = None):
        """ > Node <&Node Mesh to Volume>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        density : Float, optional
            socket 'Density' (id: Density)
        
        resolution_mode : menu='Amount', optional
            ('Amount', 'Size')
        
        voxel_size : Float, optional
            socket 'Voxel Size' (id: Voxel Size)
        
        voxel_amount : Float, optional
            socket 'Voxel Amount' (id: Voxel Amount)
        
        interior_band_width : Float, optional
            socket 'Interior Band Width' (id: Interior Band Width)
        

        Returns
        -------
        Volume
        """
        node = Node('Mesh to Volume', {'Mesh': self, 'Density': density, 'Resolution Mode': resolution_mode, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Interior Band Width': interior_band_width})
        return node._out

    @classmethod
    def UVSphere(cls, segments: Integer = None, rings: Integer = None, radius: Float = None):
        """ > Node <&Node UV Sphere>

        Parameters
        ---------
        segments : Integer, optional
            socket 'Segments' (id: Segments)
        
        rings : Integer, optional
            socket 'Rings' (id: Rings)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Mesh
        """
        node = Node('UV Sphere', {'Segments': segments, 'Rings': rings, 'Radius': radius})
        return cls(node._out)

    @classmethod
    def offset_corner_in_face(cls, corner_index: Integer = None, offset: Integer = None):
        """ > Node <&Node Offset Corner in Face>

        Parameters
        ---------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        
        offset : Integer, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Integer
        """
        node = Node('Offset Corner in Face', {'Corner Index': corner_index, 'Offset': offset})
        return node._out

    def sample_nearest_surface(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None):
        """ > Node <&Node Sample Nearest Surface>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Mesh        | `self`            |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ---------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sample_position : Vector, optional
            socket 'Sample Position' (id: Sample Position)
        
        sample_group_id : Integer, optional
            socket 'Sample Group ID' (id: Sample Group ID)
        

        Returns
        -------
        Float
            peer sockets: is_valid_ (Boolean)

        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleNearestSurface')
        node = Node('Sample Nearest Surface', {'Mesh': self, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=data_type)
        return node._out

    def sample_uv_surface(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    uv_map: Vector = None,
                    sample_uv: Vector = None):
        """ > Node <&Node Sample UV Surface>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Mesh        | `self`            |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ---------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        uv_map : Vector, optional
            socket 'UV Map' (id: Source UV Map)
        
        sample_uv : Vector, optional
            socket 'Sample UV' (id: Sample UV)
        

        Returns
        -------
        Float
            peer sockets: is_valid_ (Boolean)

        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleUVSurface')
        node = Node('Sample UV Surface', {'Mesh': self, 'Value': value, 'Source UV Map': uv_map, 'Sample UV': sample_uv}, data_type=data_type)
        return node._out

    def set_normal_sharpness(self,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT'):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name   | Value         |
        | --------- | ------ | ------------- |
        | Socket    | Mesh   | `self`        |
        | Parameter | `mode` | `'SHARPNESS'` |

        Parameters
        ---------
        remove_custom : Boolean, optional
            socket 'Remove Custom' (id: Remove Custom)
        
        edge_sharpness : Boolean, optional
            socket 'Edge Sharpness' (id: Edge Sharpness)
        
        face_sharpness : Boolean, optional
            socket 'Face Sharpness' (id: Face Sharpness)
        
        domain (str): parameter 'domain' in ('Point', 'Face', 'Face Corner')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Set Mesh Normal', 'domain', domain, 'set_normal_sharpness', ('POINT', 'FACE', 'CORNER'))
        node = Node('Set Mesh Normal', {'Mesh': self, 'Remove Custom': remove_custom, 'Edge Sharpness': edge_sharpness, 'Face Sharpness': face_sharpness}, domain=domain, mode='SHARPNESS')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal_free(self,
                    custom_normal: Vector = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT'):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name   | Value    |
        | --------- | ------ | -------- |
        | Socket    | Mesh   | `self`   |
        | Parameter | `mode` | `'FREE'` |

        Parameters
        ---------
        custom_normal : Vector, optional
            socket 'Custom Normal' (id: Custom Normal)
        
        domain (str): parameter 'domain' in ('Point', 'Face', 'Face Corner')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Set Mesh Normal', 'domain', domain, 'set_normal_free', ('POINT', 'FACE', 'CORNER'))
        node = Node('Set Mesh Normal', {'Mesh': self, 'Custom Normal': custom_normal}, domain=domain, mode='FREE')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal_tangent_space(self,
                    custom_normal: Vector = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT'):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name   | Value             |
        | --------- | ------ | ----------------- |
        | Socket    | Mesh   | `self`            |
        | Parameter | `mode` | `'TANGENT_SPACE'` |

        Parameters
        ---------
        custom_normal : Vector, optional
            socket 'Custom Normal' (id: Custom Normal)
        
        domain (str): parameter 'domain' in ('Point', 'Face', 'Face Corner')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Set Mesh Normal', 'domain', domain, 'set_normal_tangent_space', ('POINT', 'FACE', 'CORNER'))
        node = Node('Set Mesh Normal', {'Mesh': self, 'Custom Normal': custom_normal}, domain=domain, mode='TANGENT_SPACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal(self,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT',
                    mode: Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE'] = 'SHARPNESS'):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        remove_custom : Boolean, optional
            socket 'Remove Custom' (id: Remove Custom)
        
        edge_sharpness : Boolean, optional
            socket 'Edge Sharpness' (id: Edge Sharpness)
        
        face_sharpness : Boolean, optional
            socket 'Face Sharpness' (id: Face Sharpness)
        
        domain (str): parameter 'domain' in ('Point', 'Face', 'Face Corner')
        mode (str): parameter 'mode' in ('Sharpness', 'Free', 'Tangent Space')

        Returns
        -------
        Mesh
        """
        utils.check_enum_arg('Set Mesh Normal', 'domain', domain, 'set_normal', ('POINT', 'FACE', 'CORNER'))
        utils.check_enum_arg('Set Mesh Normal', 'mode', mode, 'set_normal', ('SHARPNESS', 'FREE', 'TANGENT_SPACE'))
        node = Node('Set Mesh Normal', {'Mesh': self, 'Remove Custom': remove_custom, 'Edge Sharpness': edge_sharpness, 'Face Sharpness': face_sharpness}, domain=domain, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def split_edges(self):
        """ > Node <&Node Split Edges>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Returns
        -------
        Mesh
        """
        node = Node('Split Edges', {'Mesh': self, 'Selection': self.get_selection()})
        self._jump(node._out)
        return self._domain_to_geometry

    def subdivide(self, level: Integer = None):
        """ > Node <&Node Subdivide Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        level : Integer, optional
            socket 'Level' (id: Level)
        

        Returns
        -------
        Mesh
        """
        node = Node('Subdivide Mesh', {'Mesh': self, 'Level': level})
        self._jump(node._out)
        return self._domain_to_geometry

    def subdivision_surface(self,
                    level: Integer = None,
                    edge_crease: Float = None,
                    vertex_crease: Float = None,
                    limit_surface: Boolean = None,
                    uv_smooth: Literal['None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All'] = None,
                    boundary_smooth: Literal['Keep Corners', 'All'] = None):
        """ > Node <&Node Subdivision Surface>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        level : Integer, optional
            socket 'Level' (id: Level)
        
        edge_crease : Float, optional
            socket 'Edge Crease' (id: Edge Crease)
        
        vertex_crease : Float, optional
            socket 'Vertex Crease' (id: Vertex Crease)
        
        limit_surface : Boolean, optional
            socket 'Limit Surface' (id: Limit Surface)
        
        uv_smooth : menu='Keep Boundaries', optional
            ('None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All')
        
        boundary_smooth : menu='All', optional
            ('Keep Corners', 'All')
        

        Returns
        -------
        Mesh
        """
        node = Node('Subdivision Surface', {'Mesh': self, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease, 'Limit Surface': limit_surface, 'UV Smooth': uv_smooth, 'Boundary Smooth': boundary_smooth})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_face_set(self, face_set: Integer = None):
        """ > Node <&Node Set Face Set>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ---------
        face_set : Integer, optional
            socket 'Face Set' (id: Face Set)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Face Set', {'Mesh': self, 'Selection': self.get_selection(), 'Face Set': face_set})
        self._jump(node._out)
        return self._domain_to_geometry

    def triangulate(self,
                    quad_method: Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal'] = None,
                    n_gon_method: Literal['Beauty', 'Clip'] = None):
        """ > Node <&Node Triangulate>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ---------
        quad_method : menu='Shortest Diagonal', optional
            ('Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal')
        
        n_gon_method : menu='Beauty', optional
            ('Beauty', 'Clip')
        

        Returns
        -------
        Mesh
        """
        node = Node('Triangulate', {'Mesh': self, 'Selection': self.get_selection(), 'Quad Method': quad_method, 'N-gon Method': n_gon_method})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def vertex_of_corner(cls, corner_index: Integer = None):
        """ > Node <&Node Vertex of Corner>

        Parameters
        ---------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        Integer
        """
        node = Node('Vertex of Corner', {'Corner Index': corner_index})
        return node._out

    def to_density_grid(self,
                    density: Float = None,
                    voxel_size: Float = None,
                    gradient_width: Float = None):
        """ > Node <&Node Mesh to Density Grid>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        density : Float, optional
            socket 'Density' (id: Density)
        
        voxel_size : Float, optional
            socket 'Voxel Size' (id: Voxel Size)
        
        gradient_width : Float, optional
            socket 'Gradient Width' (id: Gradient Width)
        

        Returns
        -------
        Float
        """
        node = Node('Mesh to Density Grid', {'Mesh': self, 'Density': density, 'Voxel Size': voxel_size, 'Gradient Width': gradient_width})
        return node._out

    def to_sdf_grid(self, voxel_size: Float = None, band_width: Integer = None):
        """ > Node <&Node Mesh to SDF Grid>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ---------
        voxel_size : Float, optional
            socket 'Voxel Size' (id: Voxel Size)
        
        band_width : Integer, optional
            socket 'Band Width' (id: Band Width)
        

        Returns
        -------
        Float
        """
        node = Node('Mesh to SDF Grid', {'Mesh': self, 'Voxel Size': voxel_size, 'Band Width': band_width})
        return node._out

    @property
    def normal(self):
        """ Write only property for node <Node Set Mesh Normal>
        """
        raise NodeError('Property Mesh.normal is write only.')

    @normal.setter
    def normal(self, custom_normal: Vector = None):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name     | Value             |
        | --------- | -------- | ----------------- |
        | Socket    | Mesh     | `self`            |
        | Parameter | `domain` | `'POINT'`         |
        | Parameter | `mode`   | `'TANGENT_SPACE'` |

        Parameters
        ---------
        custom_normal : Vector, optional
            socket 'Custom Normal' (id: Custom Normal)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Mesh Normal', {'Mesh': self, 'Custom Normal': custom_normal}, domain='POINT', mode='TANGENT_SPACE')
        self._jump(node._out)
        return self._domain_to_geometry

