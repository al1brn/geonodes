# Generated 2026-04-05 13:12:12

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


class Geometry(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def bounding_box(self, use_radius: Boolean = None):
        """ > Node <&Node Bounding Box>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Parameters
        ----------
        use_radius : Boolean, optional
            socket 'Use Radius' (id: Use Radius)
        

        Returns
        -------
        Mesh
            peer sockets: min_ (Vector), max_ (Vector)

        """
        node = Node('Bounding Box', {'Geometry': self, 'Use Radius': use_radius})
        return node._out

    def convex_hull(self):
        """ > Node <&Node Convex Hull>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        Mesh
        """
        node = Node('Convex Hull', {'Geometry': self})
        return node._out

    def to_instance(self, *geometry: Geometry):
        """ > Node <&Node Geometry to Instance>

        Parameters
        ----------
        geometry : Geometry, optional
            socket 'Geometry' (id: Geometry)
        

        Returns
        -------
        Instances
        """
        node = Node('Geometry to Instance', {'Geometry': [self] + list(geometry)})
        return node._out

    @classmethod
    def index_of_nearest(cls, position: Vector = None, group_id: Integer = None):
        """ > Node <&Node Index of Nearest>

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        

        Returns
        -------
        Integer
            peer sockets: has_neighbor_ (Boolean)

        """
        node = Node('Index of Nearest', {'Position': position, 'Group ID': group_id})
        return node._out

    @utils.classproperty
    def index(cls):
        """ > Node <&Node Index>

        Returns
        -------
        Integer
        """
        node = Node('Index', )
        return node._out

    def instance_on_points(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None):
        """ > Node <&Node Instance on Points>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Points    | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        instance : Instances, optional
            socket 'Instance' (id: Instance)
        
        pick_instance : Boolean, optional
            socket 'Pick Instance' (id: Pick Instance)
        
        instance_index : Integer, optional
            socket 'Instance Index' (id: Instance Index)
        
        rotation : Rotation, optional
            socket 'Rotation' (id: Rotation)
        
        scale : Vector, optional
            socket 'Scale' (id: Scale)
        

        Returns
        -------
        Instances
        """
        node = Node('Instance on Points', {'Points': self, 'Selection': self.get_selection(), 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    def join(self, *geometry: Geometry):
        """ > Node <&Node Join Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Parameters
        ----------
        geometry : Geometry, optional
            socket 'Geometry' (id: Geometry)
        

        Returns
        -------
        Geometry
        """
        node = Node('Join Geometry', {'Geometry': [self] + list(geometry)})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Join(cls, *geometry: Geometry):
        """ > Node <&Node Join Geometry>

        Parameters
        ----------
        geometry : Geometry, optional
            socket 'Geometry' (id: Geometry)
        

        Returns
        -------
        Geometry
        """
        node = Node('Join Geometry', {'Geometry': list(geometry)})
        return cls(node._out)

    def merge_by_distance(self, mode: Literal['All', 'Connected'] = None, distance: Float = None):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        mode : menu='All', optional
            ('All', 'Connected')
        
        distance : Float, optional
            socket 'Distance' (id: Distance)
        

        Returns
        -------
        Geometry
        """
        node = Node('Merge by Distance', {'Geometry': self, 'Selection': self.get_selection(), 'Mode': mode, 'Distance': distance})
        self._jump(node._out)
        return self._domain_to_geometry

    def merge(self, mode: Literal['All', 'Connected'] = None, distance: Float = None):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        mode : menu='All', optional
            ('All', 'Connected')
        
        distance : Float, optional
            socket 'Distance' (id: Distance)
        

        Returns
        -------
        Geometry
        """
        node = Node('Merge by Distance', {'Geometry': self, 'Selection': self.get_selection(), 'Mode': mode, 'Distance': distance})
        self._jump(node._out)
        return self._domain_to_geometry

    def proximity(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    target_element: Literal['POINTS', 'EDGES', 'FACES'] = 'FACES'):
        """ > Node <&Node Geometry Proximity>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Parameters
        ----------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sample_position : Vector, optional
            socket 'Sample Position' (id: Source Position)
        
        sample_group_id : Integer, optional
            socket 'Sample Group ID' (id: Sample Group ID)
        
        target_element : Literal['Points', 'Edges', 'Faces']
            parameter `target_element`
        

        Returns
        -------
        Vector
            peer sockets: distance_ (Float), is_valid_ (Boolean)

        """
        utils.check_enum_arg('Geometry Proximity', 'target_element', target_element, 'proximity', ('POINTS', 'EDGES', 'FACES'))
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=target_element)
        return node._out

    def proximity_points(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None):
        """ > Node <&Node Geometry Proximity>

        **Fixed values**

        | Kind      | Name             | Value      |
        | --------- | ---------------- | ---------- |
        | Socket    | Geometry         | `self`     |
        | Parameter | `target_element` | `'POINTS'` |

        Parameters
        ----------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sample_position : Vector, optional
            socket 'Sample Position' (id: Source Position)
        
        sample_group_id : Integer, optional
            socket 'Sample Group ID' (id: Sample Group ID)
        

        Returns
        -------
        Vector
            peer sockets: distance_ (Float), is_valid_ (Boolean)

        """
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='POINTS')
        return node._out

    def proximity_edges(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None):
        """ > Node <&Node Geometry Proximity>

        **Fixed values**

        | Kind      | Name             | Value     |
        | --------- | ---------------- | --------- |
        | Socket    | Geometry         | `self`    |
        | Parameter | `target_element` | `'EDGES'` |

        Parameters
        ----------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sample_position : Vector, optional
            socket 'Sample Position' (id: Source Position)
        
        sample_group_id : Integer, optional
            socket 'Sample Group ID' (id: Sample Group ID)
        

        Returns
        -------
        Vector
            peer sockets: distance_ (Float), is_valid_ (Boolean)

        """
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='EDGES')
        return node._out

    def proximity_faces(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None):
        """ > Node <&Node Geometry Proximity>

        **Fixed values**

        | Kind      | Name             | Value     |
        | --------- | ---------------- | --------- |
        | Socket    | Geometry         | `self`    |
        | Parameter | `target_element` | `'FACES'` |

        Parameters
        ----------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sample_position : Vector, optional
            socket 'Sample Position' (id: Source Position)
        
        sample_group_id : Integer, optional
            socket 'Sample Group ID' (id: Sample Group ID)
        

        Returns
        -------
        Vector
            peer sockets: distance_ (Float), is_valid_ (Boolean)

        """
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='FACES')
        return node._out

    def raycast(self,
                    attribute: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    interpolation: Literal['Interpolated', 'Nearest'] = None,
                    source_position: Vector = None,
                    ray_direction: Vector = None,
                    ray_length: Float = None):
        """ > Node <&Node Raycast>

        **Fixed values**

        | Kind      | Name            | Value                 |
        | --------- | --------------- | --------------------- |
        | Socket    | Target Geometry | `self`                |
        | Parameter | `data_type`     | from `attribute` type |

        Parameters
        ----------
        attribute : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Attribute' (id: Attribute)
        
        interpolation : menu='Interpolated', optional
            ('Interpolated', 'Nearest')
        
        source_position : Vector, optional
            socket 'Source Position' (id: Source Position)
        
        ray_direction : Vector, optional
            socket 'Ray Direction' (id: Ray Direction)
        
        ray_length : Float, optional
            socket 'Ray Length' (id: Ray Length)
        

        Returns
        -------
        Boolean
            peer sockets: hit_position_ (Vector), hit_normal_ (Vector), hit_distance_ (Float), attribute_ (Float)

        """
        data_type = SocketType.get_data_type_for_node(attribute, 'GeometryNodeRaycast')
        node = Node('Raycast', {'Target Geometry': self, 'Attribute': attribute, 'Interpolation': interpolation, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type)
        return node._out

    def realize(self,
                    realize_all: Boolean = None,
                    depth: Integer = None,
                    realize_to_point_domain = False):
        """ > Node <&Node Realize Instances>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        realize_all : Boolean, optional
            socket 'Realize All' (id: Realize All)
        
        depth : Integer, optional
            socket 'Depth' (id: Depth)
        
        realize_to_point_domain : bool
            parameter `realize_to_point_domain`
        

        Returns
        -------
        Geometry
        """
        node = Node('Realize Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Realize All': realize_all, 'Depth': depth}, realize_to_point_domain=realize_to_point_domain)
        return node._out

    def remove_named_attribute(self, pattern_mode: Literal['Exact', 'Wildcard'] = None, name: String = None):
        """ > Node <&Node Remove Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Parameters
        ----------
        pattern_mode : menu='Exact', optional
            ('Exact', 'Wildcard')
        
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Geometry
        """
        node = Node('Remove Named Attribute', {'Geometry': self, 'Pattern Mode': pattern_mode, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    def replace_material(self, old: Material = None, new: Material = None):
        """ > Node <&Node Replace Material>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Parameters
        ----------
        old : Material, optional
            socket 'Old' (id: Old)
        
        new : Material, optional
            socket 'New' (id: New)
        

        Returns
        -------
        Geometry
        """
        node = Node('Replace Material', {'Geometry': self, 'Old': old, 'New': new})
        self._jump(node._out)
        return self._domain_to_geometry

    def separate_components(self):
        """ > Node <&Node Separate Components>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        node [mesh (Mesh), curve (Curve), grease_pencil (GreasePencil), point_cloud (Cloud), volume (Volume), instances (Instances)]
        """
        node = self._cache('Separate Components', {'Geometry': self})
        return node

    @property
    def mesh(self):
        """ > Node <&Node Separate Components>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        mesh
        """
        node = self._cache('Separate Components', {'Geometry': self})
        return node.mesh

    @property
    def curve(self):
        """ > Node <&Node Separate Components>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        curve
        """
        node = self._cache('Separate Components', {'Geometry': self})
        return node.curve

    @property
    def grease_pencil(self):
        """ > Node <&Node Separate Components>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        grease_pencil
        """
        node = self._cache('Separate Components', {'Geometry': self})
        return node.grease_pencil

    @property
    def point_cloud(self):
        """ > Node <&Node Separate Components>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        point_cloud
        """
        node = self._cache('Separate Components', {'Geometry': self})
        return node.point_cloud

    @property
    def volume(self):
        """ > Node <&Node Separate Components>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        volume
        """
        node = self._cache('Separate Components', {'Geometry': self})
        return node.volume

    @property
    def instances(self):
        """ > Node <&Node Separate Components>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Returns
        -------
        instances
        """
        node = self._cache('Separate Components', {'Geometry': self})
        return node.instances

    def set_name(self, name: String = None):
        """ > Node <&Node Set Geometry Name>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Geometry Name', {'Geometry': self, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_id(self, id: Integer = None):
        """ > Node <&Node Set ID>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        id : Integer, optional
            socket 'ID' (id: ID)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set ID', {'Geometry': self, 'Selection': self.get_selection(), 'ID': id})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_material(self, material: Material = None):
        """ > Node <&Node Set Material>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        material : Material, optional
            socket 'Material' (id: Material)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Material', {'Geometry': self, 'Selection': self.get_selection(), 'Material': material})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_material_index(self, material_index: Integer = None):
        """ > Node <&Node Set Material Index>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        material_index : Integer, optional
            socket 'Material Index' (id: Material Index)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Material Index', {'Geometry': self, 'Selection': self.get_selection(), 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_position(self, position: Vector = None, offset: Vector = None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': offset})
        self._jump(node._out)
        return self._domain_to_geometry

    def transform(self,
                    mode: Literal['Components', 'Matrix'] = None,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None,
                    transform: Matrix = None):
        """ > Node <&Node Transform Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Parameters
        ----------
        mode : menu='Components', optional
            ('Components', 'Matrix')
        
        translation : Vector, optional
            socket 'Translation' (id: Translation)
        
        rotation : Rotation, optional
            socket 'Rotation' (id: Rotation)
        
        scale : Vector, optional
            socket 'Scale' (id: Scale)
        
        transform : Matrix, optional
            socket 'Transform' (id: Transform)
        

        Returns
        -------
        Geometry
        """
        node = Node('Transform Geometry', {'Geometry': self, 'Mode': mode, 'Translation': translation, 'Rotation': rotation, 'Scale': scale, 'Transform': transform})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Parameter | `domain` | `'AUTO'` |

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        ui_shortcut : int
            parameter `ui_shortcut`
        
        sockets : dict, default={}
            Socket created with python name attributes

        """
        node = Node('Viewer', named_sockets, domain='AUTO', ui_shortcut=ui_shortcut, **sockets)
        return

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Value       | `self`       |
        | Parameter | `data_type` | `'GEOMETRY'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Geometry
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='GEOMETRY')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def position(self):
        """ Property get node <Node Set Position>
        """
        return Node('Position', {})._out

    @position.setter
    def position(self, position: Vector = None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |
        | Socket | Offset    | ignored           |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': None})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def offset(self):
        """ Write only property for node <Node Set Position>
        """
        raise NodeError('Property Geometry.offset is write only.')

    @offset.setter
    def offset(self, offset: Vector = None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |
        | Socket | Position  | ignored           |

        Parameters
        ----------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': None, 'Offset': offset})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def id(self):
        """ Property get node <Node Set ID>
        """
        return Node('ID', {})._out

    @id.setter
    def id(self, id: Integer = None):
        """ > Node <&Node Set ID>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        id : Integer, optional
            socket 'ID' (id: ID)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set ID', {'Geometry': self, 'Selection': self.get_selection(), 'ID': id})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def material(self):
        """ Write only property for node <Node Set Material>
        """
        raise NodeError('Property Geometry.material is write only.')

    @material.setter
    def material(self, material: Material = None):
        """ > Node <&Node Set Material>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        material : Material, optional
            socket 'Material' (id: Material)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Material', {'Geometry': self, 'Selection': self.get_selection(), 'Material': material})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def name(self):
        """ Write only property for node <Node Set Geometry Name>
        """
        raise NodeError('Property Geometry.name is write only.')

    @name.setter
    def name(self, name: String = None):
        """ > Node <&Node Set Geometry Name>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Geometry | `self` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Geometry Name', {'Geometry': self, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def material_index(self):
        """ Property get node <Node Set Material Index>
        """
        return Node('Material Index', {})._out

    @material_index.setter
    def material_index(self, material_index: Integer = None):
        """ > Node <&Node Set Material Index>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        material_index : Integer, optional
            socket 'Material Index' (id: Material Index)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Material Index', {'Geometry': self, 'Selection': self.get_selection(), 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def _create_input_socket(cls,
        name: str = 'Geometry',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > Geometry Input

        New <#Geometry> input with subtype 'NONE'.

        Parameters
        ----------
        name : str, default=`Geometry`
            Input socket name

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier


        Returns
        -------
        Geometry
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketGeometry', name=name, tip=tip,
            panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier)

