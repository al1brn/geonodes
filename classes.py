from geonodes import baseclasses as bcls
from geonodes import nodes

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
# Data class Geometry

class Geometry(bcls.Geometry):
    """ Socket data class Geometry

    Properties
    ----------
        bound_box            : Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
        components           : Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]

    Node properties
    ---------------
        box                  : Geometry
        box_max              : Geometry
        box_min              : Geometry
        curve_component      : Mesh
        instances_component  : Mesh
        mesh_component       : Mesh
        points_component     : Mesh
        volume_component     : Mesh

    Attributes
    ----------
        ID                   : Integer
        capture_ID           : Integer
        capture_index        : Integer
        capture_is_viewport  : Boolean
        capture_normal       : Vector
        capture_position     : Vector
        capture_tangent      : Vector
        corner_normal        : Vector
        corner_tangent       : Vector
        curve_normal         : Vector
        curve_tangent        : Vector
        edge_normal          : Vector
        edge_tangent         : Vector
        face_normal          : Vector
        face_tangent         : Vector
        index                : Integer
        instance_normal      : Vector
        instance_tangent     : Vector
        is_viewport          : Boolean
        point_normal         : Vector
        point_tangent        : Vector
        position             : Vector

    Methods
    -------
        attribute_domain_size : Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
        attribute_remove     : Geometry
        attribute_statistic  : Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
        capture_attribute    : Sockets [geometry (Geometry), attribute (Float)]
        components           : Sockets [selection (Geometry), inverted (Geometry)]
        convex_hull          : Geometry
        join                 : Geometry
        proximity            : Sockets [position (Vector), distance (Float)]
        raycast              : Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
        switch               : Geometry
        to_instance          : Instances
        transfer_boolean     : Boolean
        transfer_color       : Color
        transfer_float       : Float
        transfer_integer     : Integer
        transfer_vector      : Vector

    Stacked methods
    ---------------
        delete_geometry      : Geometry
        merge_by_distance    : Geometry
        realize_instances    : Geometry
        replace_material     : Geometry
        scale_elements       : Geometry
        set_ID               : Geometry
        set_material         : Geometry
        set_material_index   : Geometry
        set_position         : Geometry
        set_shade_smooth     : Geometry
        transform            : Geometry

    """


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def bound_box(self):
        """ Property bound_box using node NodeBoundingBox

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
        """

        if not hasattr(self.top, 'bound_box_'):
            node = nodes.NodeBoundingBox(geometry=self)
            self.top.bound_box_ = Sockets(bounding_box=Geometry(node.bounding_box), min=Vector(node.min), max=Vector(node.max))
        return self.top.bound_box_

    @property
    def components(self):
        """ Property components using node NodeSeparateComponents

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
        """

        if not hasattr(self.top, 'components_'):
            node = nodes.NodeSeparateComponents(geometry=self)
            self.top.components_ = Sockets(mesh=Mesh(node.mesh), point_cloud=Geometry(node.point_cloud), curve=Curve(node.curve), volume=Volume(node.volume), instances=Instances(node.instances))
        return self.top.components_


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    @property
    def box(self):
        """ Node property box using node NodeBoundingBox on output socket bounding_box

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Geometry
        """

        return self.bound_box.bounding_box

    @property
    def box_min(self):
        """ Node property box_min using node NodeBoundingBox on output socket min

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Geometry
        """

        return self.bound_box.min

    @property
    def box_max(self):
        """ Node property box_max using node NodeBoundingBox on output socket max

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Geometry
        """

        return self.bound_box.max

    @property
    def mesh_component(self):
        """ Node property mesh_component using node NodeSeparateComponents on output socket mesh

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Mesh
        """

        return self.components.mesh

    @property
    def points_component(self):
        """ Node property points_component using node NodeSeparateComponents on output socket point_cloud

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Mesh
        """

        return self.components.point_cloud

    @property
    def curve_component(self):
        """ Node property curve_component using node NodeSeparateComponents on output socket curve

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Mesh
        """

        return self.components.curve

    @property
    def volume_component(self):
        """ Node property volume_component using node NodeSeparateComponents on output socket volume

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Mesh
        """

        return self.components.volume

    @property
    def instances_component(self):
        """ Node property instances_component using node NodeSeparateComponents on output socket instances

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Mesh
        """

        return self.components.instances


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    def capture_normal(self, domain='POINT'):
        """ Attribute capture_normal using node NodeNormal

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputNormal', name='capture_normal', owner_socket=self, data_type='FLOAT_VECTOR', domain=domain).normal)

    @property
    def point_normal(self):
        """ Attribute point_normal using node NodeNormal

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputNormal', name='point_normal', owner_socket=self, data_type='FLOAT_VECTOR', domain='POINT').normal)

    @property
    def edge_normal(self):
        """ Attribute edge_normal using node NodeNormal

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputNormal', name='edge_normal', owner_socket=self, data_type='FLOAT_VECTOR', domain='EDGE').normal)

    @property
    def face_normal(self):
        """ Attribute face_normal using node NodeNormal

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputNormal', name='face_normal', owner_socket=self, data_type='FLOAT_VECTOR', domain='FACE').normal)

    @property
    def corner_normal(self):
        """ Attribute corner_normal using node NodeNormal

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputNormal', name='corner_normal', owner_socket=self, data_type='FLOAT_VECTOR', domain='CORNER').normal)

    @property
    def curve_normal(self):
        """ Attribute curve_normal using node NodeNormal

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputNormal', name='curve_normal', owner_socket=self, data_type='FLOAT_VECTOR', domain='CURVE').normal)

    @property
    def instance_normal(self):
        """ Attribute instance_normal using node NodeNormal

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputNormal', name='instance_normal', owner_socket=self, data_type='FLOAT_VECTOR', domain='INSTANCE').normal)

    def capture_tangent(self, domain='POINT'):
        """ Attribute capture_tangent using node NodeCurveTangent

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputTangent', name='capture_tangent', owner_socket=self, data_type='FLOAT_VECTOR', domain=domain).tangent)

    @property
    def point_tangent(self):
        """ Attribute point_tangent using node NodeCurveTangent

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputTangent', name='point_tangent', owner_socket=self, data_type='FLOAT_VECTOR', domain='POINT').tangent)

    @property
    def edge_tangent(self):
        """ Attribute edge_tangent using node NodeCurveTangent

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputTangent', name='edge_tangent', owner_socket=self, data_type='FLOAT_VECTOR', domain='EDGE').tangent)

    @property
    def face_tangent(self):
        """ Attribute face_tangent using node NodeCurveTangent

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputTangent', name='face_tangent', owner_socket=self, data_type='FLOAT_VECTOR', domain='FACE').tangent)

    @property
    def corner_tangent(self):
        """ Attribute corner_tangent using node NodeCurveTangent

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputTangent', name='corner_tangent', owner_socket=self, data_type='FLOAT_VECTOR', domain='CORNER').tangent)

    @property
    def curve_tangent(self):
        """ Attribute curve_tangent using node NodeCurveTangent

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputTangent', name='curve_tangent', owner_socket=self, data_type='FLOAT_VECTOR', domain='CURVE').tangent)

    @property
    def instance_tangent(self):
        """ Attribute instance_tangent using node NodeCurveTangent

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputTangent', name='instance_tangent', owner_socket=self, data_type='FLOAT_VECTOR', domain='INSTANCE').tangent)

    def capture_ID(self, domain='POINT'):
        """ Attribute capture_ID using node NodeID

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return Integer(nodes.Attribute(bl_idname='GeometryNodeInputID', name='capture_ID', owner_socket=self, data_type='INT', domain=domain).ID)

    @property
    def ID(self):
        """ Attribute ID using node NodeID

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return Integer(nodes.Attribute(bl_idname='GeometryNodeInputID', name='ID', owner_socket=self, data_type='INT', domain='POINT').ID)

    def capture_index(self, domain='POINT'):
        """ Attribute capture_index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return Integer(nodes.Attribute(bl_idname='GeometryNodeInputIndex', name='capture_index', owner_socket=self, data_type='INT', domain=domain).index)

    @property
    def index(self):
        """ Attribute index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return Integer(nodes.Attribute(bl_idname='GeometryNodeInputIndex', name='index', owner_socket=self, data_type='INT', domain='POINT').index)

    def capture_position(self, domain='POINT'):
        """ Attribute capture_position using node NodePosition

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputPosition', name='capture_position', owner_socket=self, data_type='FLOAT_VECTOR', domain=domain).position)

    @property
    def position(self):
        """ Attribute position using node NodePosition

        Arguments
        ---------

        Returns
        -------
            Vector
        """

        return Vector(nodes.Attribute(bl_idname='GeometryNodeInputPosition', name='position', owner_socket=self, data_type='FLOAT_VECTOR', domain='POINT').position)

    def capture_is_viewport(self, domain='POINT'):
        """ Attribute capture_is_viewport using node NodeIsViewport

        Arguments
        ---------

        Returns
        -------
            Boolean
        """

        return Boolean(nodes.Attribute(bl_idname='GeometryNodeIsViewport', name='capture_is_viewport', owner_socket=self, data_type='BOOLEAN', domain=domain).is_viewport)

    @property
    def is_viewport(self):
        """ Attribute is_viewport using node NodeIsViewport

        Arguments
        ---------

        Returns
        -------
            Boolean
        """

        return Boolean(nodes.Attribute(bl_idname='GeometryNodeIsViewport', name='is_viewport', owner_socket=self, data_type='BOOLEAN', domain='POINT').is_viewport)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'GEOMETRY'

        Returns
        -------
            Geometry
        """

        return Geometry(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='GEOMETRY').output)

    def transfer_boolean(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_boolean using node NodeTransferAttribute

        Arguments
        ---------
            source          : Geometry: self socket
            attribute       : Vector
            source_position : Vector
            index           : Integer

            domain          : str
            mapping         : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return Boolean(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute)

    def transfer_integer(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_integer using node NodeTransferAttribute

        Arguments
        ---------
            source          : Geometry: self socket
            attribute       : Vector
            source_position : Vector
            index           : Integer

            domain          : str
            mapping         : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'INT'

        Returns
        -------
            Integer
        """

        return Integer(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping).attribute)

    def transfer_float(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_float using node NodeTransferAttribute

        Arguments
        ---------
            source          : Geometry: self socket
            attribute       : Vector
            source_position : Vector
            index           : Integer

            domain          : str
            mapping         : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT'

        Returns
        -------
            Float
        """

        return Float(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping).attribute)

    def transfer_vector(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_vector using node NodeTransferAttribute

        Arguments
        ---------
            source          : Geometry: self socket
            attribute       : Vector
            source_position : Vector
            index           : Integer

            domain          : str
            mapping         : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return Vector(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping).attribute)

    def transfer_color(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_color using node NodeTransferAttribute

        Arguments
        ---------
            source          : Geometry: self socket
            attribute       : Vector
            source_position : Vector
            index           : Integer

            domain          : str
            mapping         : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT_COLOR'

        Returns
        -------
            Color
        """

        return Color(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute)

    def attribute_domain_size(self, component='MESH'):
        """ Method attribute_domain_size using node NodeDomainSize

        Arguments
        ---------
            geometry        : Geometry: self socket

            component       : str

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
        """

        node = nodes.NodeDomainSize(geometry=self, component=component)
        return Sockets(point_count=Integer(node.point_count), edge_count=Integer(node.edge_count), face_count=Integer(node.face_count), face_corner_count=Integer(node.face_corner_count))

    def attribute_remove(self, *attribute):
        """ Method attribute_remove using node NodeAttributeRemove

        Arguments
        ---------
            geometry        : Geometry: self socket
            attribute       : String (multi input)

        Returns
        -------
            Geometry
        """

        return Geometry(nodes.NodeAttributeRemove(*attribute, geometry=self).geometry)

    def attribute_statistic(self, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):
        """ Method attribute_statistic using node NodeAttributeStatistic

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            attribute       : Float

            data_type       : str
            domain          : str

        Returns
        -------
            Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
        """

        node = nodes.NodeAttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type, domain=domain)
        return Sockets(mean=Float(node.mean), median=Float(node.median), sum=Float(node.sum), min=Float(node.min), max=Float(node.max), range=Float(node.range), standard_deviation=Float(node.standard_deviation), variance=Float(node.variance))

    def components(self, selection=None, domain='POINT'):
        """ Method components using node NodeSeparateGeometry

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean

            domain          : str

        Returns
        -------
            Sockets [selection (Geometry), inverted (Geometry)]
        """

        node = nodes.NodeSeparateGeometry(geometry=self, selection=selection, domain=domain)
        return Sockets(selection=Geometry(node.selection), inverted=Geometry(node.inverted))

    def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT'):
        """ Method capture_attribute using node NodeCaptureAttribute

        Arguments
        ---------
            geometry        : Geometry: self socket
            value           : Vector

            data_type       : str
            domain          : str

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Float)]
        """

        node = nodes.NodeCaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain)
        return Sockets(geometry=Geometry(node.geometry), attribute=Float(node.attribute))

    def convex_hull(self):
        """ Method convex_hull using node NodeConvexHull

        Arguments
        ---------
            geometry        : Geometry: self socket

        Returns
        -------
            Geometry
        """

        return Geometry(nodes.NodeConvexHull(geometry=self).convex_hull)

    def to_instance(self, *geometry):
        """ Method to_instance using node NodeGeometrytoInstance

        Arguments
        ---------
            geometry        : Geometry (multi input): self socket

        Returns
        -------
            Instances
        """

        return Instances(nodes.NodeGeometrytoInstance(self, *geometry).instances)

    def join(self, *geometry):
        """ Method join using node NodeJoinGeometry

        Arguments
        ---------
            geometry        : Geometry (multi input): self socket

        Returns
        -------
            Geometry
        """

        return Geometry(nodes.NodeJoinGeometry(self, *geometry).geometry)

    def proximity(self, source_position=None, target_element='FACES'):
        """ Method proximity using node NodeGeometryProximity

        Arguments
        ---------
            target          : Geometry: self socket
            source_position : Vector

            target_element  : str

        Returns
        -------
            Sockets [position (Vector), distance (Float)]
        """

        node = nodes.NodeGeometryProximity(target=self, source_position=source_position, target_element=target_element)
        return Sockets(position=Vector(node.position), distance=Float(node.distance))

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED'):
        """ Method raycast using node NodeRaycast

        Arguments
        ---------
            target_geometry : Geometry: self socket
            attribute       : Vector
            source_position : Vector
            ray_direction   : Vector
            ray_length      : Float

            data_type       : str
            mapping         : str

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
        """

        node = nodes.NodeRaycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type, mapping=mapping)
        return Sockets(is_hit=Boolean(node.is_hit), hit_position=Vector(node.hit_position), hit_normal=Vector(node.hit_normal), hit_distance=Float(node.hit_distance), attribute=Float(node.attribute))


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL'):
        """ Stacked method delete_geometry using node NodeDeleteGeometry

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean

            domain          : str
            mode            : str

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeDeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))

    def merge_by_distance(self, selection=None, distance=None):
        """ Stacked method merge_by_distance using node NodeMergebyDistance

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            distance        : Float

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeMergebyDistance(geometry=self, selection=selection, distance=distance))

    def realize_instances(self, legacy_behavior=False):
        """ Stacked method realize_instances using node NodeRealizeInstances

        Arguments
        ---------
            geometry        : Geometry: self socket

            legacy_behavior : bool

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeRealizeInstances(geometry=self, legacy_behavior=legacy_behavior))

    def replace_material(self, old=None, new=None):
        """ Stacked method replace_material using node NodeReplaceMaterial

        Arguments
        ---------
            geometry        : Geometry: self socket
            old             : Material
            new             : Material

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeReplaceMaterial(geometry=self, old=old, new=new))

    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """ Stacked method scale_elements using node NodeScaleElements

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            scale           : Float
            center          : Vector
            axis            : Vector

            domain          : str
            scale_mode      : str

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode))

    def set_ID(self, selection=None, ID=None):
        """ Stacked method set_ID using node NodeSetID

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            ID              : Integer

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeSetID(geometry=self, selection=selection, ID=ID))

    def set_material(self, selection=None, material=None):
        """ Stacked method set_material using node NodeSetMaterial

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            material        : Material

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeSetMaterial(geometry=self, selection=selection, material=material))

    def set_material_index(self, selection=None, material_index=None):
        """ Stacked method set_material_index using node NodeSetMaterialIndex

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            material_index  : Integer

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeSetMaterialIndex(geometry=self, selection=selection, material_index=material_index))

    def set_position(self, selection=None, position=None, offset=None):
        """ Stacked method set_position using node NodeSetPosition

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            position        : Vector
            offset          : Vector

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeSetPosition(geometry=self, selection=selection, position=position, offset=offset))

    def set_shade_smooth(self, selection=None, shade_smooth=None):
        """ Stacked method set_shade_smooth using node NodeSetShadeSmooth

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            shade_smooth    : Boolean

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeSetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))

    def transform(self, translation=None, rotation=None, scale=None):
        """ Stacked method transform using node NodeTransform

        Arguments
        ---------
            geometry        : Geometry: self socket
            translation     : Vector
            rotation        : Vector
            scale           : Vector

        Returns
        -------
            Geometry
        """

        return self.stack(nodes.NodeTransform(geometry=self, translation=translation, rotation=rotation, scale=scale))

