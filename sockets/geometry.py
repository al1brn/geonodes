import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Geometry

class Geometry(dsock.Geometry):
    """ Data socket Geometry

    Properties
    ----------
        bound_box                 : Sockets      [bounding_box (Geometry), min (Vector), max (Vector)]
        components                : Sockets      [mesh (Geometry), point_cloud (Geometry), curve (Geometry), volume (Geometry), instances (Geometry)]

    Attribute captures
    ------------------
        capture_ID                : ID           (Integer)
        capture_index             : index        (Integer)
        capture_is_viewport       : is_viewport  (Boolean)
        capture_normal            : normal       (Vector)
        capture_position          : position     (Vector)
        capture_tangent           : tangent      (Vector)

    Attributes
    ----------
        corner_normal             : Vector    = capture_normal(domain='CORNER')
        corner_tangent            : Vector    = capture_tangent(domain='CORNER')
        curve_normal              : Vector    = capture_normal(domain='CURVE')
        curve_tangent             : Vector    = capture_tangent(domain='CURVE')
        edge_normal               : Vector    = capture_normal(domain='EDGE')
        edge_tangent              : Vector    = capture_tangent(domain='EDGE')
        face_normal               : Vector    = capture_normal(domain='FACE')
        face_tangent              : Vector    = capture_tangent(domain='FACE')
        instance_normal           : Vector    = capture_normal(domain='INSTANCE')
        instance_tangent          : Vector    = capture_tangent(domain='INSTANCE')
        point_ID                  : Integer   = capture_ID(domain='POINT')
        point_index               : Integer   = capture_index(domain='POINT')
        point_is_viewport         : Boolean   = capture_is_viewport(domain='POINT')
        point_normal              : Vector    = capture_normal(domain='POINT')
        point_tangent             : Vector    = capture_tangent(domain='POINT')
        position                  : Vector    = capture_position(domain='POINT')

    Methods
    -------
        attribute_domain_size     : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
        attribute_remove          : geometry     (Geometry)
        attribute_statistic       : Sockets      [mean (data_type dependant), median (data_type dependant), sum (data_type dependant), min (data_type dependant), max (data_type dependant), range (data_type dependant), standard_deviation (data_type dependant), variance (data_type dependant)]
        capture_attribute         : Sockets      [geometry (Geometry), attribute (data_type dependant)]
        components                : Sockets      [selection (Geometry), inverted (Geometry)]
        convex_hull               : convex_hull  (Geometry)
        join                      : geometry     (Geometry)
        proximity                 : Sockets      [position (Vector), distance (Float)]
        raycast                   : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (data_type dependant)]
        switch                    : output       (Geometry)
        to_instance               : instances    (Geometry)
        transfer_boolean          : attribute    (Boolean)
        transfer_color            : attribute    (Color)
        transfer_float            : attribute    (Float)
        transfer_integer          : attribute    (Integer)
        transfer_vector           : attribute    (Vector)

    Stacked methods
    ---------------
        delete_geometry           : Geometry
        merge_by_distance         : Geometry
        realize_instances         : Geometry
        replace_material          : Geometry
        scale_elements            : Geometry
        set_ID                    : Geometry
        set_material              : Geometry
        set_material_index        : Geometry
        set_position              : Geometry
        set_shade_smooth          : Geometry
        transform                 : Geometry
    """

    def reset_properties(self):
        self.bound_box_ = None
        self.components_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def bound_box(self):
        """Call node NodeBoundingBox (GeometryNodeBoundBox)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Returns
        -------
            Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
        """

        if self.bound_box_ is None:
            self.bound_box_ = nodes.NodeBoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
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
        """Call node NodeSeparateComponents (GeometryNodeSeparateComponents)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Returns
        -------
            Sockets [mesh (Geometry), point_cloud (Geometry), curve (Geometry), volume (Geometry), instances (Geometry)]
        """

        if self.components_ is None:
            self.components_ = nodes.NodeSeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
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
    # Attribute captures

    def capture_normal(self, domain='POINT'):
        """Call node NodeNormal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        attr_name = 'capture_normal_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeNormal()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).normal

    def capture_tangent(self, domain='POINT'):
        """Call node NodeCurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        attr_name = 'capture_tangent_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeCurveTangent()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).tangent

    def capture_ID(self, domain='POINT'):
        """Call node NodeID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_ID_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeID()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).ID

    def capture_index(self, domain='POINT'):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_index_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeIndex()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).index

    def capture_position(self, domain='POINT'):
        """Call node NodePosition (GeometryNodeInputPosition)

        Returns
        -------
            Vector
        """

        attr_name = 'capture_position_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodePosition()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).position

    def capture_is_viewport(self, domain='POINT'):
        """Call node NodeIsViewport (GeometryNodeIsViewport)

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_is_viewport_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeIsViewport()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).is_viewport


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def point_normal(self):
        """Call node NodeNormal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        return self.capture_normal(domain='POINT')

    @property
    def edge_normal(self):
        """Call node NodeNormal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        return self.capture_normal(domain='EDGE')

    @property
    def face_normal(self):
        """Call node NodeNormal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        return self.capture_normal(domain='FACE')

    @property
    def corner_normal(self):
        """Call node NodeNormal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        return self.capture_normal(domain='CORNER')

    @property
    def curve_normal(self):
        """Call node NodeNormal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        return self.capture_normal(domain='CURVE')

    @property
    def instance_normal(self):
        """Call node NodeNormal (GeometryNodeInputNormal)

        Returns
        -------
            Vector
        """

        return self.capture_normal(domain='INSTANCE')

    @property
    def point_tangent(self):
        """Call node NodeCurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        return self.capture_tangent(domain='POINT')

    @property
    def edge_tangent(self):
        """Call node NodeCurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        return self.capture_tangent(domain='EDGE')

    @property
    def face_tangent(self):
        """Call node NodeCurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        return self.capture_tangent(domain='FACE')

    @property
    def corner_tangent(self):
        """Call node NodeCurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        return self.capture_tangent(domain='CORNER')

    @property
    def curve_tangent(self):
        """Call node NodeCurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        return self.capture_tangent(domain='CURVE')

    @property
    def instance_tangent(self):
        """Call node NodeCurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        return self.capture_tangent(domain='INSTANCE')

    @property
    def point_ID(self):
        """Call node NodeID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        return self.capture_ID(domain='POINT')

    @property
    def point_index(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='POINT')

    @property
    def position(self):
        """Call node NodePosition (GeometryNodeInputPosition)

        Returns
        -------
            Vector
        """

        return self.capture_position(domain='POINT')

    @property
    def point_is_viewport(self):
        """Call node NodeIsViewport (GeometryNodeIsViewport)

        Returns
        -------
            Boolean
        """

        return self.capture_is_viewport(domain='POINT')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

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

        return nodes.NodeSwitch(false=self, switch1=switch1, true=true, input_type='GEOMETRY').output

    def transfer_boolean(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node NodeTransferAttribute (GeometryNodeAttributeTransfer)

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

        return nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute

    def transfer_integer(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node NodeTransferAttribute (GeometryNodeAttributeTransfer)

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

        return nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping).attribute

    def transfer_float(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node NodeTransferAttribute (GeometryNodeAttributeTransfer)

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

        return nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping).attribute

    def transfer_vector(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node NodeTransferAttribute (GeometryNodeAttributeTransfer)

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

        return nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping).attribute

    def transfer_color(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node NodeTransferAttribute (GeometryNodeAttributeTransfer)

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

        return nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute

    def attribute_domain_size(self, component='MESH'):
        """Call node NodeDomainSize (GeometryNodeAttributeDomainSize)

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

        return nodes.NodeDomainSize(geometry=self, component=component)

    def attribute_remove(self, *attribute):
        """Call node NodeAttributeRemove (GeometryNodeAttributeRemove)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            attribute      : *String

        Returns
        -------
            Geometry
        """

        return nodes.NodeAttributeRemove(*attribute, geometry=self).geometry

    def attribute_statistic(self, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):
        """Call node NodeAttributeStatistic (GeometryNodeAttributeStatistic)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            attribute      : Float

        Parameters arguments
        --------------------
            data_type      : 'FLOAT' in [FLOAT, FLOAT_VECTOR]
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Returns
        -------
            Sockets [mean (data_type dependant), median (data_type dependant), sum (data_type dependant), min (data_type dependant), max (data_type dependant), range (data_type dependant), standard_deviation (data_type dependant), variance (data_type dependant)]
        """

        return nodes.NodeAttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type, domain=domain)

    def components(self, selection=None, domain='POINT'):
        """Call node NodeSeparateGeometry (GeometryNodeSeparateGeometry)

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

        return nodes.NodeSeparateGeometry(geometry=self, selection=selection, domain=domain)

    def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT'):
        """Call node NodeCaptureAttribute (GeometryNodeCaptureAttribute)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            value          : Float

        Parameters arguments
        --------------------
            data_type      : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Returns
        -------
            Sockets [geometry (Geometry), attribute (data_type dependant)]
        """

        return nodes.NodeCaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain)

    def convex_hull(self):
        """Call node NodeConvexHull (GeometryNodeConvexHull)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)

        Returns
        -------
            Geometry
        """

        return nodes.NodeConvexHull(geometry=self).convex_hull

    def to_instance(self, *geometry):
        """Call node NodeGeometryToInstance (GeometryNodeGeometryToInstance)

        Sockets arguments
        -----------------
            geometry       : *Geometry (self)

        Returns
        -------
            Geometry
        """

        return nodes.NodeGeometryToInstance(self, *geometry).instances

    def join(self, *geometry):
        """Call node NodeJoinGeometry (GeometryNodeJoinGeometry)

        Sockets arguments
        -----------------
            geometry       : *Geometry (self)

        Returns
        -------
            Geometry
        """

        return nodes.NodeJoinGeometry(self, *geometry).geometry

    def proximity(self, source_position=None, target_element='FACES'):
        """Call node NodeGeometryProximity (GeometryNodeProximity)

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

        return nodes.NodeGeometryProximity(target=self, source_position=source_position, target_element=target_element)

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED'):
        """Call node NodeRaycast (GeometryNodeRaycast)

        Sockets arguments
        -----------------
            target_geometry: Geometry (self)
            attribute      : Float
            source_position: Vector
            ray_direction  : Vector
            ray_length     : Float

        Parameters arguments
        --------------------
            data_type      : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
            mapping        : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (data_type dependant)]
        """

        return nodes.NodeRaycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type, mapping=mapping)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL'):
        """Call node NodeDeleteGeometry (GeometryNodeDeleteGeometry)

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

        return self.stack(nodes.NodeDeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))

    def merge_by_distance(self, selection=None, distance=None):
        """Call node NodeMergeByDistance (GeometryNodeMergeByDistance)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            distance       : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeMergeByDistance(geometry=self, selection=selection, distance=distance))

    def realize_instances(self, legacy_behavior=False):
        """Call node NodeRealizeInstances (GeometryNodeRealizeInstances)

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

        return self.stack(nodes.NodeRealizeInstances(geometry=self, legacy_behavior=legacy_behavior))

    def replace_material(self, old=None, new=None):
        """Call node NodeReplaceMaterial (GeometryNodeReplaceMaterial)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            old            : Material
            new            : Material

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeReplaceMaterial(geometry=self, old=old, new=new))

    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """Call node NodeScaleElements (GeometryNodeScaleElements)

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

        return self.stack(nodes.NodeScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode))

    def set_ID(self, selection=None, ID=None):
        """Call node NodeSetID (GeometryNodeSetID)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            ID             : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetID(geometry=self, selection=selection, ID=ID))

    def set_material(self, selection=None, material=None):
        """Call node NodeSetMaterial (GeometryNodeSetMaterial)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            material       : Material

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetMaterial(geometry=self, selection=selection, material=material))

    def set_material_index(self, selection=None, material_index=None):
        """Call node NodeSetMaterialIndex (GeometryNodeSetMaterialIndex)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            material_index : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetMaterialIndex(geometry=self, selection=selection, material_index=material_index))

    def set_position(self, selection=None, position=None, offset=None):
        """Call node NodeSetPosition (GeometryNodeSetPosition)

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

        return self.stack(nodes.NodeSetPosition(geometry=self, selection=selection, position=position, offset=offset))

    def set_shade_smooth(self, selection=None, shade_smooth=None):
        """Call node NodeSetShadeSmooth (GeometryNodeSetShadeSmooth)

        Sockets arguments
        -----------------
            geometry       : Geometry (self)
            selection      : Boolean
            shade_smooth   : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))

    def transform(self, translation=None, rotation=None, scale=None):
        """Call node NodeTransform (GeometryNodeTransform)

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

        return self.stack(nodes.NodeTransform(geometry=self, translation=translation, rotation=rotation, scale=scale))


