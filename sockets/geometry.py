#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-14
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Geometry

class Geometry(dsock.Geometry):
    """ 

    Data socket Geometry
    --------------------
        > Inherits from dsock.Geometry
          
        <sub>go to index</sub>
        
        
    

        Static methods
        --------------
            - is_viewport : is_viewport (Boolean)
    

        Properties
        ----------
            - bound_box : Sockets      [bounding_box (Geometry), min (Vector), max (Vector)]
            - box : bounding_box (Geometry) = bound_box.bounding_box
            - box_max : max (Vector) = bound_box.max
            - box_min : min (Vector) = bound_box.min
            - components : Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
            - curve_component : curve (Curve) = components.curve
            - instances_component : instances (Instances) = components.instances
            - mesh_component : mesh (Mesh) = components.mesh
            - points_component : point_cloud (Geometry) = components.point_cloud
            - volume_component : volume (Volume) = components.volume
    

        Attribute capture
        -----------------
            - capture_ID : ID (Integer)
            - capture_index : index (Integer)
            - capture_normal : normal (Vector)
            - capture_position : position (Vector)
            - capture_radius : radius (Float)
    

        Attributes
        ----------
            - ID : Integer = capture_ID(domain='POINT')
            - index : Integer = capture_index(domain='POINT')
            - normal : Vector = capture_normal(domain='FACE')
            - position : Vector = capture_position(domain='POINT')
            - radius : Float = capture_radius(domain='POINT')
    

        Methods
        -------
            - attribute_domain_size : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
            - capture_attribute : attribute (data_type dependant)
            - components : Sockets      [selection (Geometry), inverted (Geometry)]
            - convex_hull : convex_hull (Geometry)
            - delete_geometry : geometry (Geometry)
            - join : geometry (Geometry)
            - merge_by_distance : geometry (Geometry)
            - proximity : Sockets      [position (Vector), distance (Float)]
            - realize_instances : geometry (Geometry)
            - remove_attribute : geometry (Geometry)
            - replace_material : geometry (Geometry)
            - scale_elements : geometry (Geometry)
            - set_ID : geometry (Geometry)
            - set_material : geometry (Geometry)
            - set_material_index : geometry (Geometry)
            - set_position : geometry (Geometry)
            - set_shade_smooth : geometry (Geometry)
            - switch : output (Geometry)
            - to_instance : instances (Instances)
            - transfer_boolean : attribute (Boolean)
            - transfer_color : attribute (Color)
            - transfer_float : attribute (Float)
            - transfer_integer : attribute (Integer)
            - transfer_vector : attribute (Vector)
            - transform : geometry (Geometry)
    """


    def reset_properties(self):

        super().reset_properties()

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
    def is_viewport(node_label = None, node_color = None):
        """ > Node: IsViewport
          
        <sub>go to: top index
        blender ref GeometryNodeIsViewport
        node ref Is Viewport </sub>
                                  
        ```python
        v = Geometry.is_viewport(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.IsViewport(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.IsViewport(label=node_label, node_color=node_color).is_viewport


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def bound_box(self):
        """ > Node: BoundingBox
          
        <sub>go to: top index
        blender ref GeometryNodeBoundBox
        node ref Bounding Box </sub>
                                  
        ```python
        v = geometry.bound_box
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.bound_box"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
            ```
    

        Returns
        -------
            Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
            
        """

        if self.bound_box_ is None:
            self.bound_box_ = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
        return self.bound_box_

    @property
    def box(self):
        """ > Node: BoundingBox
          
        <sub>go to: top index
        blender ref GeometryNodeBoundBox
        node ref Bounding Box </sub>
                                  
        ```python
        v = geometry.box
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.box"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box")
            ```
    

        Returns
        -------
            Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
            
        """

        return self.bound_box.bounding_box

    @property
    def box_min(self):
        """ > Node: BoundingBox
          
        <sub>go to: top index
        blender ref GeometryNodeBoundBox
        node ref Bounding Box </sub>
                                  
        ```python
        v = geometry.box_min
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.box_min"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_min")
            ```
    

        Returns
        -------
            Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
            
        """

        return self.bound_box.min

    @property
    def box_max(self):
        """ > Node: BoundingBox
          
        <sub>go to: top index
        blender ref GeometryNodeBoundBox
        node ref Bounding Box </sub>
                                  
        ```python
        v = geometry.box_max
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.box_max"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_max")
            ```
    

        Returns
        -------
            Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
            
        """

        return self.bound_box.max

    @property
    def components(self):
        """ > Node: SeparateComponents
          
        <sub>go to: top index
        blender ref GeometryNodeSeparateComponents
        node ref Separate Components </sub>
                                  
        ```python
        v = geometry.components
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.components"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
            
        """

        if self.components_ is None:
            self.components_ = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
        return self.components_

    @property
    def mesh_component(self):
        """ > Node: SeparateComponents
          
        <sub>go to: top index
        blender ref GeometryNodeSeparateComponents
        node ref Separate Components </sub>
                                  
        ```python
        v = geometry.mesh_component
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.mesh_component"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.mesh_component")
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
            
        """

        return self.components.mesh

    @property
    def points_component(self):
        """ > Node: SeparateComponents
          
        <sub>go to: top index
        blender ref GeometryNodeSeparateComponents
        node ref Separate Components </sub>
                                  
        ```python
        v = geometry.points_component
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.points_component"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.points_component")
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
            
        """

        return self.components.point_cloud

    @property
    def curve_component(self):
        """ > Node: SeparateComponents
          
        <sub>go to: top index
        blender ref GeometryNodeSeparateComponents
        node ref Separate Components </sub>
                                  
        ```python
        v = geometry.curve_component
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.curve_component"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.curve_component")
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
            
        """

        return self.components.curve

    @property
    def volume_component(self):
        """ > Node: SeparateComponents
          
        <sub>go to: top index
        blender ref GeometryNodeSeparateComponents
        node ref Separate Components </sub>
                                  
        ```python
        v = geometry.volume_component
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.volume_component"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.volume_component")
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
            
        """

        return self.components.volume

    @property
    def instances_component(self):
        """ > Node: SeparateComponents
          
        <sub>go to: top index
        blender ref GeometryNodeSeparateComponents
        node ref Separate Components </sub>
                                  
        ```python
        v = geometry.instances_component
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - label:f"{self.node_chain_label}.instances_component"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.instances_component")
            ```
    

        Returns
        -------
            Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
            
        """

        return self.components.instances


    # ----------------------------------------------------------------------------------------------------
    # Attribute capture

    def capture_ID(self, domain='POINT', node_label = None, node_color = None):
        """ > Node: ID
          
        <sub>go to: top index
        blender ref GeometryNodeInputID
        node ref ID </sub>
                                  
        ```python
        v = geometry.capture_ID(self, domain='POINT', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'POINT'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ID(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        attr_name = 'capture_ID_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.ID(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.ID

    def capture_index(self, domain='POINT', node_label = None, node_color = None):
        """ > Node: Index
          
        <sub>go to: top index
        blender ref GeometryNodeInputIndex
        node ref Index </sub>
                                  
        ```python
        v = geometry.capture_index(self, domain='POINT', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'POINT'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Index(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        attr_name = 'capture_index_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.Index(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.index

    def capture_normal(self, domain='FACE', node_label = None, node_color = None):
        """ > Node: Normal
          
        <sub>go to: top index
        blender ref GeometryNodeInputNormal
        node ref Normal </sub>
                                  
        ```python
        v = geometry.capture_normal(self, domain='FACE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'FACE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Normal(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        attr_name = 'capture_normal_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.Normal(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.normal

    def capture_position(self, domain='POINT', node_label = None, node_color = None):
        """ > Node: Position
          
        <sub>go to: top index
        blender ref GeometryNodeInputPosition
        node ref Position </sub>
                                  
        ```python
        v = geometry.capture_position(self, domain='POINT', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'POINT'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Position(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        attr_name = 'capture_position_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.Position(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.position

    def capture_radius(self, domain='POINT', node_label = None, node_color = None):
        """ > Node: Radius
          
        <sub>go to: top index
        blender ref GeometryNodeInputRadius
        node ref Radius </sub>
                                  
        ```python
        v = geometry.capture_radius(self, domain='POINT', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'POINT'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Radius(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        attr_name = 'capture_radius_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.Radius(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.radius


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def ID(self):
        """ > Node: ID
          
        <sub>go to: top index
        blender ref GeometryNodeInputID
        node ref ID </sub>
                                  
        ```python
        v = geometry.ID(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ID()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_ID(domain='POINT')

    @property
    def index(self):
        """ > Node: Index
          
        <sub>go to: top index
        blender ref GeometryNodeInputIndex
        node ref Index </sub>
                                  
        ```python
        v = geometry.index(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Index()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_index(domain='POINT')

    @property
    def normal(self):
        """ > Node: Normal
          
        <sub>go to: top index
        blender ref GeometryNodeInputNormal
        node ref Normal </sub>
                                  
        ```python
        v = geometry.normal(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Normal()
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.capture_normal(domain='FACE')

    @property
    def position(self):
        """ > Node: Position
          
        <sub>go to: top index
        blender ref GeometryNodeInputPosition
        node ref Position </sub>
                                  
        ```python
        v = geometry.position(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Position()
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.capture_position(domain='POINT')

    @property
    def radius(self):
        """ > Node: Radius
          
        <sub>go to: top index
        blender ref GeometryNodeInputRadius
        node ref Radius </sub>
                                  
        ```python
        v = geometry.radius(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Radius()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_radius(domain='POINT')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = geometry.switch(switch1, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Geometry (self)
            - switch1 : Boolean
            - true : Geometry## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'GEOMETRY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch1=switch1, true=true, input_type='GEOMETRY', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='GEOMETRY', label=node_label, node_color=node_color).output

    def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT', node_label = None, node_color = None):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
                                  
        ```python
        v = geometry.capture_attribute(value, data_type, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - value : Float## Parameters
            - data_type : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (data_type dependant)]
            
        """

        node = nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
        self.stack(node)
        return node.attribute

    def transfer_boolean(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = geometry.transfer_boolean(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - source : Geometry (self)
            - attribute : Boolean
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_integer(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = geometry.transfer_integer(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - source : Geometry (self)
            - attribute : Integer
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_float(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = geometry.transfer_float(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - source : Geometry (self)
            - attribute : Float
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_vector(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = geometry.transfer_vector(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - source : Geometry (self)
            - attribute : Vector
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_VECTOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_color(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = geometry.transfer_color(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - source : Geometry (self)
            - attribute : Color
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT_COLOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Color
            
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL', node_label = None, node_color = None):
        """ > Node: DeleteGeometry
          
        <sub>go to: top index
        blender ref GeometryNodeDeleteGeometry
        node ref Delete Geometry </sub>
                                  
        ```python
        v = geometry.delete_geometry(selection, domain, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
            - mode : 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode, label=node_label, node_color=node_color))

    def merge_by_distance(self, selection=None, distance=None, mode='ALL', node_label = None, node_color = None):
        """ > Node: MergeByDistance
          
        <sub>go to: top index
        blender ref GeometryNodeMergeByDistance
        node ref Merge by Distance </sub>
                                  
        ```python
        v = geometry.merge_by_distance(selection, distance, mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - distance : Float## Parameters
            - mode : 'ALL' in [ALL, CONNECTED]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode, label=node_label, node_color=node_color))

    def realize_instances(self, legacy_behavior=False, node_label = None, node_color = None):
        """ > Node: RealizeInstances
          
        <sub>go to: top index
        blender ref GeometryNodeRealizeInstances
        node ref Realize Instances </sub>
                                  
        ```python
        v = geometry.realize_instances(legacy_behavior, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Parameters
            - legacy_behavior : False
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior, label=node_label, node_color=node_color))

    def replace_material(self, old=None, new=None, node_label = None, node_color = None):
        """ > Node: ReplaceMaterial
          
        <sub>go to: top index
        blender ref GeometryNodeReplaceMaterial
        node ref Replace Material </sub>
                                  
        ```python
        v = geometry.replace_material(old, new, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - old : Material
            - new : Material## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ReplaceMaterial(geometry=self, old=old, new=new, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.ReplaceMaterial(geometry=self, old=old, new=new, label=node_label, node_color=node_color))

    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', node_label = None, node_color = None):
        """ > Node: ScaleElements
          
        <sub>go to: top index
        blender ref GeometryNodeScaleElements
        node ref Scale Elements </sub>
                                  
        ```python
        v = geometry.scale_elements(selection, scale, center, axis, domain, scale_mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - scale : Float
            - center : Vector
            - axis : Vector## Parameters
            - domain : 'FACE' in [FACE, EDGE]
            - scale_mode : 'UNIFORM' in [UNIFORM, SINGLE_AXIS]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode, label=node_label, node_color=node_color))

    def set_ID(self, selection=None, ID=None, node_label = None, node_color = None):
        """ > Node: SetID
          
        <sub>go to: top index
        blender ref GeometryNodeSetID
        node ref Set ID </sub>
                                  
        ```python
        v = geometry.set_ID(selection, ID, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - ID : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetID(geometry=self, selection=selection, ID=ID, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetID(geometry=self, selection=selection, ID=ID, label=node_label, node_color=node_color))

    def set_material(self, selection=None, material=None, node_label = None, node_color = None):
        """ > Node: SetMaterial
          
        <sub>go to: top index
        blender ref GeometryNodeSetMaterial
        node ref Set Material </sub>
                                  
        ```python
        v = geometry.set_material(selection, material, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - material : Material## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetMaterial(geometry=self, selection=selection, material=material, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetMaterial(geometry=self, selection=selection, material=material, label=node_label, node_color=node_color))

    def set_material_index(self, selection=None, material_index=None, node_label = None, node_color = None):
        """ > Node: SetMaterialIndex
          
        <sub>go to: top index
        blender ref GeometryNodeSetMaterialIndex
        node ref Set Material Index </sub>
                                  
        ```python
        v = geometry.set_material_index(selection, material_index, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - material_index : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index, label=node_label, node_color=node_color))

    def set_position(self, selection=None, position=None, offset=None, node_label = None, node_color = None):
        """ > Node: SetPosition
          
        <sub>go to: top index
        blender ref GeometryNodeSetPosition
        node ref Set Position </sub>
                                  
        ```python
        v = geometry.set_position(selection, position, offset, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - position : Vector
            - offset : Vector## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset, label=node_label, node_color=node_color))

    def set_shade_smooth(self, selection=None, shade_smooth=None, node_label = None, node_color = None):
        """ > Node: SetShadeSmooth
          
        <sub>go to: top index
        blender ref GeometryNodeSetShadeSmooth
        node ref Set Shade Smooth </sub>
                                  
        ```python
        v = geometry.set_shade_smooth(selection, shade_smooth, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - shade_smooth : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth, label=node_label, node_color=node_color))

    def transform(self, translation=None, rotation=None, scale=None, node_label = None, node_color = None):
        """ > Node: Transform
          
        <sub>go to: top index
        blender ref GeometryNodeTransform
        node ref Transform </sub>
                                  
        ```python
        v = geometry.transform(translation, rotation, scale, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - translation : Vector
            - rotation : Vector
            - scale : Vector## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale, label=node_label, node_color=node_color))

    def attribute_domain_size(self, component='MESH', node_label = None, node_color = None):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = geometry.attribute_domain_size(component, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Parameters
            - component : 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component=component, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
            
        """

        return nodes.DomainSize(geometry=self, component=component, label=node_label, node_color=node_color)

    def remove_attribute(self, name=None, node_label = None, node_color = None):
        """ > Node: RemoveNamedAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeRemoveAttribute
        node ref Remove Named Attribute </sub>
                                  
        ```python
        v = geometry.remove_attribute(name, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - name : String## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RemoveNamedAttribute(geometry=self, name=name, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return nodes.RemoveNamedAttribute(geometry=self, name=name, label=node_label, node_color=node_color).geometry

    def components(self, selection=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: SeparateGeometry
          
        <sub>go to: top index
        blender ref GeometryNodeSeparateGeometry
        node ref Separate Geometry </sub>
                                  
        ```python
        v = geometry.components(selection, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [selection (Geometry), inverted (Geometry)]
            
        """

        return nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain, label=node_label, node_color=node_color)

    def convex_hull(self, node_label = None, node_color = None):
        """ > Node: ConvexHull
          
        <sub>go to: top index
        blender ref GeometryNodeConvexHull
        node ref Convex Hull </sub>
                                  
        ```python
        v = geometry.convex_hull(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ConvexHull(geometry=self, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return nodes.ConvexHull(geometry=self, label=node_label, node_color=node_color).convex_hull

    def to_instance(self, *geometry, node_label = None, node_color = None):
        """ > Node: GeometryToInstance
          
        <sub>go to: top index
        blender ref GeometryNodeGeometryToInstance
        node ref Geometry to Instance </sub>
                                  
        ```python
        v = geometry.to_instance(geometry_1, geometry_2, geometry_3, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : *Geometry (self)## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.GeometryToInstance(self, *geometry, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Instances
            
        """

        return nodes.GeometryToInstance(self, *geometry, label=node_label, node_color=node_color).instances

    def join(self, *geometry, node_label = None, node_color = None):
        """ > Node: JoinGeometry
          
        <sub>go to: top index
        blender ref GeometryNodeJoinGeometry
        node ref Join Geometry </sub>
                                  
        ```python
        v = geometry.join(geometry_1, geometry_2, geometry_3, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : *Geometry (self)## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.JoinGeometry(self, *geometry, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return nodes.JoinGeometry(self, *geometry, label=node_label, node_color=node_color).geometry

    def proximity(self, source_position=None, target_element='FACES', node_label = None, node_color = None):
        """ > Node: GeometryProximity
          
        <sub>go to: top index
        blender ref GeometryNodeProximity
        node ref Geometry Proximity </sub>
                                  
        ```python
        v = geometry.proximity(source_position, target_element, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - target : Geometry (self)
            - source_position : Vector## Parameters
            - target_element : 'FACES' in [POINTS, EDGES, FACES]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [position (Vector), distance (Float)]
            
        """

        return nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element, label=node_label, node_color=node_color)


