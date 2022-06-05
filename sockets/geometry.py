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
    - is_viewport : IsViewport is_viewport (Boolean) 
    

    Properties
    ==========
    - bound_box           : BoundingBox Sockets      [bounding_box (Geometry), min (Vector), max (Vector)] 
    - box                 : BoundingBox bounding_box (Geometry) = bound_box.bounding_box 
    - box_max             : BoundingBox max (Vector) = bound_box.max 
    - box_min             : BoundingBox min (Vector) = bound_box.min 
    - components          : SeparateComponents Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume
      (Volume), instances (Instances)] 
    - curve_component     : SeparateComponents curve (Curve) = components.curve 
    - instances_component : SeparateComponents instances (Instances) = components.instances 
    - mesh_component      : SeparateComponents mesh (Mesh) = components.mesh 
    - points_component    : SeparateComponents point_cloud (Geometry) = components.point_cloud 
    - volume_component    : SeparateComponents volume (Volume) = components.volume 
    

    Attribute capture
    =================
    - capture_ID       : ID ID (Integer) 
    - capture_index    : Index index (Integer) 
    - capture_normal   : Normal normal (Vector) 
    - capture_position : Position position (Vector) 
    - capture_radius   : Radius radius (Float) 
    

    Attributes
    ==========
    - ID       : ID Integer = capture_ID(domain='POINT') 
    - index    : Index Integer = capture_index(domain='POINT') 
    - normal   : Normal Vector = capture_normal(domain='FACE') 
    - position : Position Vector = capture_position(domain='POINT') 
    - radius   : Radius Float = capture_radius(domain='POINT') 
    

    Methods
    =======
    - attribute_domain_size : DomainSize Sockets      [point_count (Integer), edge_count (Integer), face_count
      (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)] 
    - attribute_remove      : AttributeRemove geometry (Geometry) 
    - components            : SeparateGeometry Sockets      [selection (Geometry), inverted (Geometry)] 
    - convex_hull           : ConvexHull convex_hull (Geometry) 
    - join                  : JoinGeometry geometry (Geometry) 
    - proximity             : GeometryProximity Sockets      [position (Vector), distance (Float)] 
    - switch                : Switch output (Geometry) 
    - to_instance           : GeometryToInstance instances (Instances) 
    - transfer_boolean      : TransferAttribute attribute (Boolean) 
    - transfer_color        : TransferAttribute attribute (Color) 
    - transfer_float        : TransferAttribute attribute (Float) 
    - transfer_integer      : TransferAttribute attribute (Integer) 
    - transfer_vector       : TransferAttribute attribute (Vector) 
    

    Stacked methods
    ===============
    - delete_geometry    : DeleteGeometry Geometry 
    - merge_by_distance  : MergeByDistance Geometry 
    - realize_instances  : RealizeInstances Geometry 
    - replace_material   : ReplaceMaterial Geometry 
    - scale_elements     : ScaleElements Geometry 
    - set_ID             : SetID Geometry 
    - set_material       : SetMaterial Geometry 
    - set_material_index : SetMaterialIndex Geometry 
    - set_position       : SetPosition Geometry 
    - set_shade_smooth   : SetShadeSmooth Geometry 
    - transform          : Transform Geometry 
    """


    def reset_properties(self):
        self.bound_box_ = None
        self.box_ = None
        self.box_min_ = None
        self.box_max_ = None
        self.components_ = None
        self.mesh_component_ = None
        self.points_component_ = None
        self.curve_component_ = None
        self.volume_component_ = None
        self.instances_component_ = None

    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def is_viewport():
        """ is_viewport
        

        | Node: IsViewport 
        

            v = Geometry.is_viewport() 
        

        Arguments
        =========
        

        Node creation
        =============
        

            node = nodes.IsViewport() 
        

        Returns
        =======
                Boolean 
        """

        return nodes.IsViewport().is_viewport


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def bound_box(self):
        """ bound_box
        

        | Node: BoundingBox 
        

            v = geometry.bound_box 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.bound_box" 
        

        Node creation
        =============
        

            node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box") 
        

        Returns
        =======
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)] 
        """

        if self.bound_box_ is None:
            self.bound_box_ = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
        return self.bound_box_

    @property
    def box(self):
        """ box
        

        | Node: BoundingBox 
        

            v = geometry.box 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.box" 
        

        Node creation
        =============
        

            node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box") 
        

        Returns
        =======
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)] 
        """

        return self.bound_box.bounding_box

    @property
    def box_min(self):
        """ box_min
        

        | Node: BoundingBox 
        

            v = geometry.box_min 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.box_min" 
        

        Node creation
        =============
        

            node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_min") 
        

        Returns
        =======
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)] 
        """

        return self.bound_box.min

    @property
    def box_max(self):
        """ box_max
        

        | Node: BoundingBox 
        

            v = geometry.box_max 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.box_max" 
        

        Node creation
        =============
        

            node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_max") 
        

        Returns
        =======
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)] 
        """

        return self.bound_box.max

    @property
    def components(self):
        """ components
        

        | Node: SeparateComponents 
        

            v = geometry.components 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.components" 
        

        Node creation
        =============
        

            node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components") 
        

        Returns
        =======
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)] 
        """

        if self.components_ is None:
            self.components_ = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
        return self.components_

    @property
    def mesh_component(self):
        """ mesh_component
        

        | Node: SeparateComponents 
        

            v = geometry.mesh_component 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.mesh_component" 
        

        Node creation
        =============
        

            node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.mesh_component") 
        

        Returns
        =======
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)] 
        """

        return self.components.mesh

    @property
    def points_component(self):
        """ points_component
        

        | Node: SeparateComponents 
        

            v = geometry.points_component 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.points_component" 
        

        Node creation
        =============
        

            node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.points_component") 
        

        Returns
        =======
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)] 
        """

        return self.components.point_cloud

    @property
    def curve_component(self):
        """ curve_component
        

        | Node: SeparateComponents 
        

            v = geometry.curve_component 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.curve_component" 
        

        Node creation
        =============
        

            node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.curve_component") 
        

        Returns
        =======
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)] 
        """

        return self.components.curve

    @property
    def volume_component(self):
        """ volume_component
        

        | Node: SeparateComponents 
        

            v = geometry.volume_component 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.volume_component" 
        

        Node creation
        =============
        

            node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.volume_component") 
        

        Returns
        =======
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)] 
        """

        return self.components.volume

    @property
    def instances_component(self):
        """ instances_component
        

        | Node: SeparateComponents 
        

            v = geometry.instances_component 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.instances_component" 
        

        Node creation
        =============
        

            node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.instances_component") 
        

        Returns
        =======
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)] 
        """

        return self.components.instances


    # ----------------------------------------------------------------------------------------------------
    # Attribute capture

    def capture_ID(self, domain='POINT'):
        """ capture_ID
        

        | Node: ID 
        

            v = geometry.capture_ID(self, domain='POINT') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'POINT' 
        

        Node creation
        =============
        

            node = nodes.ID() 
        

        Returns
        =======
                Integer 
        """

        attr_name = 'capture_ID_' + domain
        if not hasattr(self, attr_name):
            node = nodes.ID()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).ID

    def capture_index(self, domain='POINT'):
        """ capture_index
        

        | Node: Index 
        

            v = geometry.capture_index(self, domain='POINT') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'POINT' 
        

        Node creation
        =============
        

            node = nodes.Index() 
        

        Returns
        =======
                Integer 
        """

        attr_name = 'capture_index_' + domain
        if not hasattr(self, attr_name):
            node = nodes.Index()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).index

    def capture_normal(self, domain='FACE'):
        """ capture_normal
        

        | Node: Normal 
        

            v = geometry.capture_normal(self, domain='FACE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'FACE' 
        

        Node creation
        =============
        

            node = nodes.Normal() 
        

        Returns
        =======
                Vector 
        """

        attr_name = 'capture_normal_' + domain
        if not hasattr(self, attr_name):
            node = nodes.Normal()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).normal

    def capture_position(self, domain='POINT'):
        """ capture_position
        

        | Node: Position 
        

            v = geometry.capture_position(self, domain='POINT') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'POINT' 
        

        Node creation
        =============
        

            node = nodes.Position() 
        

        Returns
        =======
                Vector 
        """

        attr_name = 'capture_position_' + domain
        if not hasattr(self, attr_name):
            node = nodes.Position()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).position

    def capture_radius(self, domain='POINT'):
        """ capture_radius
        

        | Node: Radius 
        

            v = geometry.capture_radius(self, domain='POINT') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'POINT' 
        

        Node creation
        =============
        

            node = nodes.Radius() 
        

        Returns
        =======
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
        """ ID
        

        | Node: ID 
        

            v = geometry.ID(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.ID() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_ID(domain='POINT')

    @property
    def index(self):
        """ index
        

        | Node: Index 
        

            v = geometry.index(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.Index() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_index(domain='POINT')

    @property
    def normal(self):
        """ normal
        

        | Node: Normal 
        

            v = geometry.normal(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.Normal() 
        

        Returns
        =======
                Vector 
        """

        return self.capture_normal(domain='FACE')

    @property
    def position(self):
        """ position
        

        | Node: Position 
        

            v = geometry.position(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.Position() 
        

        Returns
        =======
                Vector 
        """

        return self.capture_position(domain='POINT')

    @property
    def radius(self):
        """ radius
        

        | Node: Radius 
        

            v = geometry.radius(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.Radius() 
        

        Returns
        =======
                Float 
        """

        return self.capture_radius(domain='POINT')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = geometry.switch(switch1, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Geometry (self) 
            - switch1 : Boolean 
            - true    : Geometry 
        

            Fixed parameters
            ----------------
            - input_type : 'GEOMETRY' 
        

        Node creation
        =============
        

            node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='GEOMETRY') 
        

        Returns
        =======
                Geometry 
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='GEOMETRY').output

    def transfer_boolean(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_boolean
        

        | Node: TransferAttribute 
        

            v = geometry.transfer_boolean(attribute, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - source          : Geometry (self) 
            - attribute       : Boolean 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'BOOLEAN' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index,
            data_type='BOOLEAN', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Boolean 
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute

    def transfer_integer(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_integer
        

        | Node: TransferAttribute 
        

            v = geometry.transfer_integer(attribute, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - source          : Geometry (self) 
            - attribute       : Integer 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index,
            data_type='INT', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Integer 
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping).attribute

    def transfer_float(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_float
        

        | Node: TransferAttribute 
        

            v = geometry.transfer_float(attribute, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - source          : Geometry (self) 
            - attribute       : Float 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index,
            data_type='FLOAT', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Float 
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping).attribute

    def transfer_vector(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_vector
        

        | Node: TransferAttribute 
        

            v = geometry.transfer_vector(attribute, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - source          : Geometry (self) 
            - attribute       : Vector 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index,
            data_type='FLOAT_VECTOR', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Vector 
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping).attribute

    def transfer_color(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_color
        

        | Node: TransferAttribute 
        

            v = geometry.transfer_color(attribute, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - source          : Geometry (self) 
            - attribute       : Color 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_COLOR' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index,
            data_type='FLOAT_COLOR', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Color 
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute

    def attribute_domain_size(self, component='MESH'):
        """ attribute_domain_size
        

        | Node: DomainSize 
        

            v = geometry.attribute_domain_size(component) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Parameters arguments
            --------------------
            - component : 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES] 
        

        Node creation
        =============
        

            node = nodes.DomainSize(geometry=self, component=component) 
        

        Returns
        =======
                Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer),
                spline_count (Integer), instance_count (Integer)] 
        """

        return nodes.DomainSize(geometry=self, component=component)

    def attribute_remove(self, *attribute):
        """ attribute_remove
        

        | Node: AttributeRemove 
        

            v = geometry.attribute_remove(attribute_1, attribute_2, attribute_3) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - attribute : *String 
        

        Node creation
        =============
        

            node = nodes.AttributeRemove(*attribute, geometry=self) 
        

        Returns
        =======
                Geometry 
        """

        return nodes.AttributeRemove(*attribute, geometry=self).geometry

    def components(self, selection=None, domain='POINT'):
        """ components
        

        | Node: SeparateGeometry 
        

            v = geometry.components(selection, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - selection : Boolean 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain) 
        

        Returns
        =======
                Sockets [selection (Geometry), inverted (Geometry)] 
        """

        return nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain)

    def convex_hull(self):
        """ convex_hull
        

        | Node: ConvexHull 
        

            v = geometry.convex_hull() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

        Node creation
        =============
        

            node = nodes.ConvexHull(geometry=self) 
        

        Returns
        =======
                Geometry 
        """

        return nodes.ConvexHull(geometry=self).convex_hull

    def to_instance(self, *geometry):
        """ to_instance
        

        | Node: GeometryToInstance 
        

            v = geometry.to_instance(geometry_1, geometry_2, geometry_3) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : *Geometry (self) 
        

        Node creation
        =============
        

            node = nodes.GeometryToInstance(self, *geometry) 
        

        Returns
        =======
                Instances 
        """

        return nodes.GeometryToInstance(self, *geometry).instances

    def join(self, *geometry):
        """ join
        

        | Node: JoinGeometry 
        

            v = geometry.join(geometry_1, geometry_2, geometry_3) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : *Geometry (self) 
        

        Node creation
        =============
        

            node = nodes.JoinGeometry(self, *geometry) 
        

        Returns
        =======
                Geometry 
        """

        return nodes.JoinGeometry(self, *geometry).geometry

    def proximity(self, source_position=None, target_element='FACES'):
        """ proximity
        

        | Node: GeometryProximity 
        

            v = geometry.proximity(source_position, target_element) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - target          : Geometry (self) 
            - source_position : Vector 
        

            Parameters arguments
            --------------------
            - target_element : 'FACES' in [POINTS, EDGES, FACES] 
        

        Node creation
        =============
        

            node = nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element)
        

        Returns
        =======
                Sockets [position (Vector), distance (Float)] 
        """

        return nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL'):
        """ delete_geometry
        

        | Node: DeleteGeometry 
        

            geometry.delete_geometry(selection, domain, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - selection : Boolean 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE] 
            - mode   : 'ALL' in [ALL, EDGE_FACE, ONLY_FACE] 
        

        Node creation
        =============
        

            node = nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))

    def merge_by_distance(self, selection=None, distance=None):
        """ merge_by_distance
        

        | Node: MergeByDistance 
        

            geometry.merge_by_distance(selection, distance) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - selection : Boolean 
            - distance  : Float 
        

        Node creation
        =============
        

            node = nodes.MergeByDistance(geometry=self, selection=selection, distance=distance) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.MergeByDistance(geometry=self, selection=selection, distance=distance))

    def realize_instances(self, legacy_behavior=False):
        """ realize_instances
        

        | Node: RealizeInstances 
        

            geometry.realize_instances(legacy_behavior) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
        

            Parameters arguments
            --------------------
            - legacy_behavior : False 
        

        Node creation
        =============
        

            node = nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior))

    def replace_material(self, old=None, new=None):
        """ replace_material
        

        | Node: ReplaceMaterial 
        

            geometry.replace_material(old, new) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry : Geometry (self) 
            - old      : Material 
            - new      : Material 
        

        Node creation
        =============
        

            node = nodes.ReplaceMaterial(geometry=self, old=old, new=new) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.ReplaceMaterial(geometry=self, old=old, new=new))

    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """ scale_elements
        

        | Node: ScaleElements 
        

            geometry.scale_elements(selection, scale, center, axis, domain, scale_mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - selection : Boolean 
            - scale     : Float 
            - center    : Vector 
            - axis      : Vector 
        

            Parameters arguments
            --------------------
            - domain     : 'FACE' in [FACE, EDGE] 
            - scale_mode : 'UNIFORM' in [UNIFORM, SINGLE_AXIS] 
        

        Node creation
        =============
        

            node = nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis,
            domain=domain, scale_mode=scale_mode) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode))

    def set_ID(self, selection=None, ID=None):
        """ set_ID
        

        | Node: SetID 
        

            geometry.set_ID(selection, ID) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - selection : Boolean 
            - ID        : Integer 
        

        Node creation
        =============
        

            node = nodes.SetID(geometry=self, selection=selection, ID=ID) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetID(geometry=self, selection=selection, ID=ID))

    def set_material(self, selection=None, material=None):
        """ set_material
        

        | Node: SetMaterial 
        

            geometry.set_material(selection, material) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - selection : Boolean 
            - material  : Material 
        

        Node creation
        =============
        

            node = nodes.SetMaterial(geometry=self, selection=selection, material=material) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetMaterial(geometry=self, selection=selection, material=material))

    def set_material_index(self, selection=None, material_index=None):
        """ set_material_index
        

        | Node: SetMaterialIndex 
        

            geometry.set_material_index(selection, material_index) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry       : Geometry (self) 
            - selection      : Boolean 
            - material_index : Integer 
        

        Node creation
        =============
        

            node = nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index))

    def set_position(self, selection=None, position=None, offset=None):
        """ set_position
        

        | Node: SetPosition 
        

            geometry.set_position(selection, position, offset) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry (self) 
            - selection : Boolean 
            - position  : Vector 
            - offset    : Vector 
        

        Node creation
        =============
        

            node = nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset))

    def set_shade_smooth(self, selection=None, shade_smooth=None):
        """ set_shade_smooth
        

        | Node: SetShadeSmooth 
        

            geometry.set_shade_smooth(selection, shade_smooth) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry     : Geometry (self) 
            - selection    : Boolean 
            - shade_smooth : Boolean 
        

        Node creation
        =============
        

            node = nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))

    def transform(self, translation=None, rotation=None, scale=None):
        """ transform
        

        | Node: Transform 
        

            geometry.transform(translation, rotation, scale) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry    : Geometry (self) 
            - translation : Vector 
            - rotation    : Vector 
            - scale       : Vector 
        

        Node creation
        =============
        

            node = nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale))


