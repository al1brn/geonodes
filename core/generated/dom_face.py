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


class Face:
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None):
        """ > Node <&Node Accumulate Field>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'FACE'`          |

        Parameters
        ---------
        value : Float | Integer | Vector | Matrix, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        

        Returns
        -------
        Float
            peer sockets: trailing_ (Float), total_ (Float)

        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeAccumulateField')
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='FACE')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        **Fixed values**

        | Kind      | Name        | Value                 |
        | --------- | ----------- | --------------------- |
        | Socket    | Geometry    | `self`                |
        | Socket    | Selection   | `self[selection]`     |
        | Parameter | `data_type` | from `attribute` type |
        | Parameter | `domain`    | `'FACE'`              |

        Parameters
        ---------
        attribute : Float | Vector, optional
            socket 'Attribute' (id: Attribute)
        

        Returns
        -------
        Float
            peer sockets: median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)

        """
        data_type = SocketType.get_data_type_for_node(attribute, 'GeometryNodeAttributeStatistic')
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='FACE')
        return node._out

    @classmethod
    def field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Average>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ---------
        value : Float | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain (str): parameter 'domain' in ('Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer')

        Returns
        -------
        Float
            peer sockets: median_ (Float)

        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldAverage')
        node = Node('Field Average', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Min & Max>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ---------
        value : Float | Integer | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain (str): parameter 'domain' in ('Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer')

        Returns
        -------
        Float
            peer sockets: max_ (Float)

        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldMinAndMax')
        node = Node('Field Min & Max', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Variance>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ---------
        value : Float | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain (str): parameter 'domain' in ('Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer')

        Returns
        -------
        Float
            peer sockets: variance_ (Float)

        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldVariance')
        node = Node('Field Variance', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def corners(cls,
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
    def corner_index(cls,
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
        corner_index
        """
        node = Node('Corners of Face', {'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.corner_index

    @classmethod
    def corners_total(cls,
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
        total
        """
        node = Node('Corners of Face', {'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    def delete_geometry_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |
        | Parameter | `mode`    | `'ALL'`           |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |
        | Parameter | `mode`    | `'EDGE_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |
        | Parameter | `mode`    | `'ONLY_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        mode (str): parameter 'mode' in ('All', 'Only Edges & Faces', 'Only Faces')

        Returns
        -------
        Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete_geometry', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |
        | Parameter | `mode`    | `'ALL'`           |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |
        | Parameter | `mode`    | `'EDGE_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |
        | Parameter | `mode`    | `'ONLY_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        mode (str): parameter 'mode' in ('All', 'Only Edges & Faces', 'Only Faces')

        Returns
        -------
        Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def distribute_points(self,
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
        utils.check_enum_arg('Distribute Points on Faces', 'distribute_method', distribute_method, 'distribute_points', ('RANDOM', 'POISSON'))
        node = Node('Distribute Points on Faces', {'Mesh': self, 'Selection': self.get_selection(), 'Density': density, 'Seed': seed}, distribute_method=distribute_method)
        return node._out

    def distribute_points_random(self, density: Float = None, seed: Integer = None):
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

    def distribute_points_poisson(self,
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

    def duplicate(self, amount: Integer = None):
        """ > Node <&Node Duplicate Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        amount : Integer, optional
            socket 'Amount' (id: Amount)
        

        Returns
        -------
        Geometry
            peer sockets: duplicate_index_ (Integer)

        """
        node = Node('Duplicate Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Amount': amount}, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def extrude(self,
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

    @classmethod
    def evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None):
        """ > Node <&Node Evaluate at Index>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'FACE'`          |

        Parameters
        ---------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        index : Integer, optional
            socket 'Index' (id: Index)
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldAtIndex')
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='FACE')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'FACE'`          |

        Parameters
        ---------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldOnDomain')
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='FACE')
        return node._out

    @utils.classproperty
    def area(cls):
        """ > Node <&Node Face Area>

        Returns
        -------
        Float
        """
        node = Node('Face Area', )
        return node._out

    @classmethod
    def is_planar(cls, threshold: Float = None):
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
    def neighbors(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        Integer
            peer sockets: face_count_ (Integer)

        """
        node = Node('Face Neighbors', )
        return node._out

    @utils.classproperty
    def neighbors_vertex_count(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        vertex_count
        """
        node = Node('Face Neighbors', )
        return node.vertex_count

    @utils.classproperty
    def neighbors_face_count(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        face_count
        """
        node = Node('Face Neighbors', )
        return node.face_count

    def to_points(self, position: Vector = None, radius: Float = None):
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

    def sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False):
        """ > Node <&Node Sample Index>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'FACE'`          |

        Parameters
        ---------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        index : Integer, optional
            socket 'Index' (id: Index)
        
        clamp (bool): parameter 'clamp'

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleIndex')
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='FACE')
        return node._out

    def sample_nearest(self, sample_position: Vector = None):
        """ > Node <&Node Sample Nearest>

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Socket    | Geometry | `self`   |
        | Parameter | `domain` | `'FACE'` |

        Parameters
        ---------
        sample_position : Vector, optional
            socket 'Sample Position' (id: Sample Position)
        

        Returns
        -------
        Integer
        """
        node = Node('Sample Nearest', {'Geometry': self, 'Sample Position': sample_position}, domain='FACE')
        return node._out

    def scale(self,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None):
        """ > Node <&Node Scale Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        center : Vector, optional
            socket 'Center' (id: Center)
        
        scale_mode : menu='Uniform', optional
            ('Uniform', 'Single Axis')
        
        axis : Vector, optional
            socket 'Axis' (id: Axis)
        

        Returns
        -------
        Geometry
        """
        node = Node('Scale Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Scale': scale, 'Center': center, 'Scale Mode': scale_mode, 'Axis': axis}, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def separate(self):
        """ > Node <&Node Separate Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Returns
        -------
        node [selection (Geometry), inverted (Geometry)]
        """
        node = Node('Separate Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE')
        self._jump(node._out)
        return node

    def set_shade_smooth(self, shade_smooth: Boolean = None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        shade_smooth : Boolean, optional
            socket 'Shade Smooth' (id: Shade Smooth)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def sort(self, group_id: Integer = None, sort_weight: Float = None):
        """ > Node <&Node Sort Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sort_weight : Float, optional
            socket 'Sort Weight' (id: Sort Weight)
        

        Returns
        -------
        Geometry
        """
        node = Node('Sort Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id: Integer = None):
        """ > Node <&Node Split to Instances>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        

        Returns
        -------
        Instances
            peer sockets: group_id_ (Integer)

        """
        node = Node('Split to Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id}, domain='FACE')
        return node._out

    def store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Socket    | Selection   | `self[selection]` |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'FACE'`          |

        Parameters
        ---------
        name : String, optional
            socket 'Name' (id: Name)
        
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Geometry
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeStoreNamedAttribute')
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Socket    | Selection   | `self[selection]` |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'FACE'`          |

        Parameters
        ---------
        name : String, optional
            socket 'Name' (id: Name)
        
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Geometry
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeStoreNamedAttribute')
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def active_element(cls):
        """ > Node <&Node Active Element>

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Parameter | `domain` | `'FACE'` |

        Returns
        -------
        Integer
            peer sockets: exists_ (Boolean)

        """
        node = Node('Active Element', domain='FACE')
        return node._out

    def set_selection(self):
        """ > Node <&Node Set Selection>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name             | Value                 |
        | --------- | ---------------- | --------------------- |
        | Socket    | Geometry         | `self`                |
        | Socket    | Selection        | `self[selection]`     |
        | Parameter | `domain`         | `'FACE'`              |
        | Parameter | `selection_type` | from `selection` type |

        Returns
        -------
        Geometry
        """
        selection_type = SocketType.get_data_type_for_node(selection, 'GeometryNodeToolSetSelection')
        node = Node('Set Selection', {'Geometry': self, 'Selection': self.get_selection()}, domain='FACE', selection_type=selection_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Parameter | `domain` | `'FACE'` |

        Parameters
        ---------
        ui_shortcut (int): parameter 'ui_shortcut'

        """
        node = Node('Viewer', named_sockets, domain='FACE', ui_shortcut=ui_shortcut, **sockets)
        return

    @property
    def material(self):
        """ Write only property for node <Node Set Material>
        """
        raise NodeError('Property Face.material is write only.')

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
        ---------
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
        ---------
        material_index : Integer, optional
            socket 'Material Index' (id: Material Index)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Material Index', {'Geometry': self, 'Selection': self.get_selection(), 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def shade_smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Face Smooth', {})._out

    @shade_smooth.setter
    def shade_smooth(self, shade_smooth: Boolean = None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        shade_smooth : Boolean, optional
            socket 'Shade Smooth' (id: Shade Smooth)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Face Smooth', {})._out

    @smooth.setter
    def smooth(self, shade_smooth: Boolean = None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'FACE'`          |

        Parameters
        ---------
        shade_smooth : Boolean, optional
            socket 'Shade Smooth' (id: Shade Smooth)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def normal(self):
        """ Write only property for node <Node Set Mesh Normal>
        """
        raise NodeError('Property Face.normal is write only.')

    @normal.setter
    def normal(self, custom_normal: Vector = None):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Socket    | Mesh     | `self`   |
        | Parameter | `domain` | `'FACE'` |
        | Parameter | `mode`   | `'FREE'` |

        Parameters
        ---------
        custom_normal : Vector, optional
            socket 'Custom Normal' (id: Custom Normal)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Mesh Normal', {'Mesh': self, 'Custom Normal': custom_normal}, domain='FACE', mode='FREE')
        self._jump(node._out)
        return self._domain_to_geometry

