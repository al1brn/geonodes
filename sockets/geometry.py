import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Geometry

class Geometry(dsock.Geometry):
    """ Class Geometry
    

    | Inherits from: dsock.Geometry 
    

    Static methods
    ==============
    - is_viewport : is_viewport (Boolean) 
    

    Properties
    ==========
    - bound_box  : Sockets      [bounding_box (Geometry), min (Vector), max (Vector)] 
    - components : Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances
      (Instances)] 
    

    Attribute capture
    =================
    - capture_ID       : ID (Integer) 
    - capture_index    : index (Integer) 
    - capture_normal   : normal (Vector) 
    - capture_position : position (Vector) 
    - capture_radius   : radius (Float) 
    

    Attributes
    ==========
    - ID       : Integer = capture_ID(domain='POINT') 
    - index    : Integer = capture_index(domain='POINT') 
    - normal   : Vector = capture_normal(domain='FACE') 
    - position : Vector = capture_position(domain='POINT') 
    - radius   : Float = capture_radius(domain='POINT') 
    

    Methods
    =======
    - attribute_domain_size : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer),
      face_corner_count (Integer), spline_count (Integer), instance_count (Integer)] 
    - attribute_remove      : geometry (Geometry) 
    - components            : Sockets      [selection (Geometry), inverted (Geometry)] 
    - convex_hull           : convex_hull (Geometry) 
    - join                  : geometry (Geometry) 
    - proximity             : Sockets      [position (Vector), distance (Float)] 
    - switch                : output (Geometry) 
    - to_instance           : instances (Instances) 
    - transfer_boolean      : attribute (Boolean) 
    - transfer_color        : attribute (Color) 
    - transfer_float        : attribute (Float) 
    - transfer_integer      : attribute (Integer) 
    - transfer_vector       : attribute (Vector) 
    

    Stacked methods
    ===============
    - delete_geometry    : Geometry 
    - merge_by_distance  : Geometry 
    - realize_instances  : Geometry 
    - replace_material   : Geometry 
    - scale_elements     : Geometry 
    - set_ID             : Geometry 
    - set_material       : Geometry 
    - set_material_index : Geometry 
    - set_position       : Geometry 
    - set_shade_smooth   : Geometry 
    - transform          : Geometry 
    """


    def reset_properties(self):
        self.bound_box_ = None
        self.components_ = None

    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def is_viewport():
        """Call node IsViewport (GeometryNodeIsViewport)

        Returns
        -------
            Boolean
        """

        return nodes.IsViewport().is_viewport


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def bound_box(self):
        """Call node BoundingBox (GeometryNodeBoundBox)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Returns
        -------
            Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
        """

        if self.bound_box_ is None:
            self.bound_box_ = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
        return self.bound_box_


    @property
    def box(self):
        return self.bound_box.bounding_box

    @property
    def box_min(self):
        return self.bound_box.min

    @property
    def box_max(self):
        return self.bound_box.max

    @property
    def components(self):
        """Call node SeparateComponents (GeometryNodeSeparateComponents)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
        """

        if self.components_ is None:
            self.components_ = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
        return self.components_


    @property
    def mesh_component(self):
        return self.components.mesh

    @property
    def points_component(self):
        return self.components.point_cloud

    @property
    def curve_component(self):
        return self.components.curve

    @property
    def volume_component(self):
        return self.components.volume

    @property
    def instances_component(self):
        return self.components.instances


    # ----------------------------------------------------------------------------------------------------
    # Attribute capture

    def capture_ID(self, domain='POINT'):
        """Call node ID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_ID_' + domain
        if not hasattr(self, attr_name):
            node = nodes.ID()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).ID

    def capture_index(self, domain='POINT'):
        """Call node Index (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_index_' + domain
        if not hasattr(self, attr_name):
            node = nodes.Index()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).index

    def capture_normal(self, domain='FACE'):
        """Call node Normal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        attr_name = 'capture_normal_' + domain
        if not hasattr(self, attr_name):
            node = nodes.Normal()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).normal

    def capture_position(self, domain='POINT'):
        """Call node Position (GeometryNodeInputPosition)

        Returns
        -------
            Vector
        """

        attr_name = 'capture_position_' + domain
        if not hasattr(self, attr_name):
            node = nodes.Position()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).position

    def capture_radius(self, domain='POINT'):
        """Call node Radius (GeometryNodeInputRadius)

        Returns
        -------
            Float
        """

        attr_name = 'capture_radius_' + domain
        if not hasattr(self, attr_name):
            node = nodes.Radius()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).radius


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def ID(self):
        """Call node ID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        return self.capture_ID(domain='POINT')

    @property
    def index(self):
        """Call node Index (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='POINT')

    @property
    def normal(self):
        """Call node Normal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        return self.capture_normal(domain='FACE')

    @property
    def position(self):
        """Call node Position (GeometryNodeInputPosition)

        Returns
        -------
            Vector
        """

        return self.capture_position(domain='POINT')

    @property
    def radius(self):
        """Call node Radius (GeometryNodeInputRadius)

        Returns
        -------
            Float
        """

        return self.capture_radius(domain='POINT')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """Call node Switch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Geometry (self)
            switch1        : Boolean
            true           : Geometry

        Fixed parameters
        ----------------
            input_type     : 'GEOMETRY'

        Returns
        -------
            Geometry
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='GEOMETRY').output

    def transfer_boolean(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            source         : Geometry (self)
            attribute      : Boolean
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute

    def transfer_integer(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            source         : Geometry (self)
            attribute      : Integer
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'INT'

        Returns
        -------
            Integer
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping).attribute

    def transfer_float(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            source         : Geometry (self)
            attribute      : Float
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping).attribute

    def transfer_vector(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            source         : Geometry (self)
            attribute      : Vector
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping).attribute

    def transfer_color(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            source         : Geometry (self)
            attribute      : Color
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_COLOR'

        Returns
        -------
            Color
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute

    def attribute_domain_size(self, component='MESH'):
        """Call node DomainSize (GeometryNodeAttributeDomainSize)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Parameters arguments
        --------------------
            component      : 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
        """

        return nodes.DomainSize(geometry=self, component=component)

    def attribute_remove(self, *attribute):
        """Call node AttributeRemove (GeometryNodeAttributeRemove)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            attribute      : *String

        Returns
        -------
            Geometry
        """

        return nodes.AttributeRemove(*attribute, geometry=self).geometry

    def components(self, selection=None, domain='POINT'):
        """Call node SeparateGeometry (GeometryNodeSeparateGeometry)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

        Returns
        -------
            Sockets [selection (Geometry), inverted (Geometry)]
        """

        return nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain)

    def convex_hull(self):
        """Call node ConvexHull (GeometryNodeConvexHull)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Returns
        -------
            Geometry
        """

        return nodes.ConvexHull(geometry=self).convex_hull

    def to_instance(self, *geometry):
        """Call node GeometryToInstance (GeometryNodeGeometryToInstance)

        Sockets arguments
        -----------------
            geometry       : *Geometry (self)

        Returns
        -------
            Instances
        """

        return nodes.GeometryToInstance(self, *geometry).instances

    def join(self, *geometry):
        """Call node JoinGeometry (GeometryNodeJoinGeometry)

        Sockets arguments
        -----------------
            geometry       : *Geometry (self)

        Returns
        -------
            Geometry
        """

        return nodes.JoinGeometry(self, *geometry).geometry

    def proximity(self, source_position=None, target_element='FACES'):
        """Call node GeometryProximity (GeometryNodeProximity)

        Sockets arguments
        -----------------
            target         : Geometry (self)
            source_position: Vector

        Parameters arguments
        --------------------
            target_element : 'FACES' in [POINTS, EDGES, FACES]

        Returns
        -------
            Sockets [position (Vector), distance (Float)]
        """

        return nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL'):
        """Call node DeleteGeometry (GeometryNodeDeleteGeometry)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
            mode           : 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        Returns
        -------
            self

        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))

    def merge_by_distance(self, selection=None, distance=None):
        """Call node MergeByDistance (GeometryNodeMergeByDistance)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            distance       : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.MergeByDistance(geometry=self, selection=selection, distance=distance))

    def realize_instances(self, legacy_behavior=False):
        """Call node RealizeInstances (GeometryNodeRealizeInstances)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Parameters arguments
        --------------------
            legacy_behavior: False

        Returns
        -------
            self

        """

        return self.stack(nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior))

    def replace_material(self, old=None, new=None):
        """Call node ReplaceMaterial (GeometryNodeReplaceMaterial)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            old            : Material
            new            : Material

        Returns
        -------
            self

        """

        return self.stack(nodes.ReplaceMaterial(geometry=self, old=old, new=new))

    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """Call node ScaleElements (GeometryNodeScaleElements)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            scale          : Float
            center         : Vector
            axis           : Vector

        Parameters arguments
        --------------------
            domain         : 'FACE' in [FACE, EDGE]
            scale_mode     : 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

        Returns
        -------
            self

        """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode))

    def set_ID(self, selection=None, ID=None):
        """Call node SetID (GeometryNodeSetID)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            ID             : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.SetID(geometry=self, selection=selection, ID=ID))

    def set_material(self, selection=None, material=None):
        """Call node SetMaterial (GeometryNodeSetMaterial)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            material       : Material

        Returns
        -------
            self

        """

        return self.stack(nodes.SetMaterial(geometry=self, selection=selection, material=material))

    def set_material_index(self, selection=None, material_index=None):
        """Call node SetMaterialIndex (GeometryNodeSetMaterialIndex)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            material_index : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index))

    def set_position(self, selection=None, position=None, offset=None):
        """Call node SetPosition (GeometryNodeSetPosition)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            position       : Vector
            offset         : Vector

        Returns
        -------
            self

        """

        return self.stack(nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset))

    def set_shade_smooth(self, selection=None, shade_smooth=None):
        """Call node SetShadeSmooth (GeometryNodeSetShadeSmooth)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            shade_smooth   : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))

    def transform(self, translation=None, rotation=None, scale=None):
        """Call node Transform (GeometryNodeTransform)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            translation    : Vector
            rotation       : Vector
            scale          : Vector

        Returns
        -------
            self

        """

        return self.stack(nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale))


