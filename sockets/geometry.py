#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-18
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Geometry

class Geometry(dsock.Geometry):
    """ Data class Geometry
    """

    def copy(self):

        return Geometry(self)


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
        """ Geometry node [*Is Viewport*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.IsViewport`
            
            
            .. blid:: GeometryNodeIsViewport
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.IsViewport(label=node_label, node_color=node_color)
                
        """

        return nodes.IsViewport(label=node_label, node_color=node_color).is_viewport


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def bound_box(self):
        """ Geometry node [*Bounding Box*].
        
        
        
            Returns:
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BoundingBox`
            
            
            .. blid:: GeometryNodeBoundBox
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
                
        """

        if self.bound_box_ is None:
            self.bound_box_ = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
        return self.bound_box_

    @property
    def box(self):
        """ Geometry node [*Bounding Box*].
        
        
        
            Returns:
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BoundingBox`
            
            
            .. blid:: GeometryNodeBoundBox
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box")
                
        """

        return self.bound_box.bounding_box

    @property
    def box_min(self):
        """ Geometry node [*Bounding Box*].
        
        
        
            Returns:
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BoundingBox`
            
            
            .. blid:: GeometryNodeBoundBox
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_min")
                
        """

        return self.bound_box.min

    @property
    def box_max(self):
        """ Geometry node [*Bounding Box*].
        
        
        
            Returns:
                Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BoundingBox`
            
            
            .. blid:: GeometryNodeBoundBox
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_max")
                
        """

        return self.bound_box.max

    @property
    def components(self):
        """ Geometry node [*Separate Components*].
        
        
        
            Returns:
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateComponents`
            
            
            .. blid:: GeometryNodeSeparateComponents
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
                
        """

        if self.components_ is None:
            self.components_ = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
        return self.components_

    @property
    def mesh_component(self):
        """ Geometry node [*Separate Components*].
        
        
        
            Returns:
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateComponents`
            
            
            .. blid:: GeometryNodeSeparateComponents
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.mesh_component")
                
        """

        return self.components.mesh

    @property
    def points_component(self):
        """ Geometry node [*Separate Components*].
        
        
        
            Returns:
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateComponents`
            
            
            .. blid:: GeometryNodeSeparateComponents
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.points_component")
                
        """

        return self.components.point_cloud

    @property
    def curve_component(self):
        """ Geometry node [*Separate Components*].
        
        
        
            Returns:
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateComponents`
            
            
            .. blid:: GeometryNodeSeparateComponents
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.curve_component")
                
        """

        return self.components.curve

    @property
    def volume_component(self):
        """ Geometry node [*Separate Components*].
        
        
        
            Returns:
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateComponents`
            
            
            .. blid:: GeometryNodeSeparateComponents
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.volume_component")
                
        """

        return self.components.volume

    @property
    def instances_component(self):
        """ Geometry node [*Separate Components*].
        
        
        
            Returns:
                Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateComponents`
            
            
            .. blid:: GeometryNodeSeparateComponents
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.instances_component")
                
        """

        return self.components.instances


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Geometry
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'GEOMETRY'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='GEOMETRY', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='GEOMETRY', label=node_label, node_color=node_color).output

    def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Capture Attribute*].
        
        
            Args:
                value: Float
                data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), attribute (data_type dependant)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
            
            
            .. blid:: GeometryNodeCaptureAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
                
        """

        node = nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
        self.stack(node)
        return node.attribute

    def transfer_boolean(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ Geometry node [*Transfer Attribute*].
        
        
            Args:
                attribute: Boolean
                source_position: Vector
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                mapping (str): 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.TransferAttribute`
            
                - data_type = 'BOOLEAN'
                  
            .. blid:: GeometryNodeAttributeTransfer
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_integer(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ Geometry node [*Transfer Attribute*].
        
        
            Args:
                attribute: Integer
                source_position: Vector
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                mapping (str): 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.TransferAttribute`
            
                - data_type = 'INT'
                  
            .. blid:: GeometryNodeAttributeTransfer
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_float(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ Geometry node [*Transfer Attribute*].
        
        
            Args:
                attribute: Float
                source_position: Vector
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                mapping (str): 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.TransferAttribute`
            
                - data_type = 'FLOAT'
                  
            .. blid:: GeometryNodeAttributeTransfer
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_vector(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ Geometry node [*Transfer Attribute*].
        
        
            Args:
                attribute: Vector
                source_position: Vector
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                mapping (str): 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Vector
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.TransferAttribute`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: GeometryNodeAttributeTransfer
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def transfer_color(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ Geometry node [*Transfer Attribute*].
        
        
            Args:
                attribute: Color
                source_position: Vector
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                mapping (str): 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.TransferAttribute`
            
                - data_type = 'FLOAT_COLOR'
                  
            .. blid:: GeometryNodeAttributeTransfer
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def duplicate_elements(self, selection=None, amount=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Duplicate Elements*].
        
        
            Args:
                selection: Boolean
                amount: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), duplicate_index (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DuplicateElements`
            
            
            .. blid:: GeometryNodeDuplicateElements
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain=domain, label=node_label, node_color=node_color)

    def duplicate_points(self, selection=None, amount=None, node_label = None, node_color = None):
        """ Geometry node [*Duplicate Elements*].
        
        
            Args:
                selection: Boolean
                amount: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), duplicate_index (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DuplicateElements`
            
                - domain = 'POINT'
                  
            .. blid:: GeometryNodeDuplicateElements
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='POINT', label=node_label, node_color=node_color)
                
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='POINT', label=node_label, node_color=node_color)

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL', node_label = None, node_color = None):
        """ Geometry node [*Delete Geometry*].
        
        
            Args:
                selection: Boolean
                domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
                mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DeleteGeometry`
            
            
            .. blid:: GeometryNodeDeleteGeometry
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode, label=node_label, node_color=node_color))

    def merge_by_distance(self, selection=None, distance=None, mode='ALL', node_label = None, node_color = None):
        """ Geometry node [*Merge by Distance*].
        
        
            Args:
                selection: Boolean
                distance: Float
                mode (str): 'ALL' in [ALL, CONNECTED]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MergeByDistance`
            
            
            .. blid:: GeometryNodeMergeByDistance
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode, label=node_label, node_color=node_color))

    def replace_material(self, old=None, new=None, node_label = None, node_color = None):
        """ Geometry node [*Replace Material*].
        
        
            Args:
                old: Material
                new: Material
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ReplaceMaterial`
            
            
            .. blid:: GeometryNodeReplaceMaterial
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ReplaceMaterial(geometry=self, old=old, new=new, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.ReplaceMaterial(geometry=self, old=old, new=new, label=node_label, node_color=node_color))

    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', node_label = None, node_color = None):
        """ Geometry node [*Scale Elements*].
        
        
            Args:
                selection: Boolean
                scale: Float
                center: Vector
                axis: Vector
                domain (str): 'FACE' in [FACE, EDGE]
                scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ScaleElements`
            
            
            .. blid:: GeometryNodeScaleElements
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode, label=node_label, node_color=node_color))

    def set_ID(self, selection=None, ID=None, node_label = None, node_color = None):
        """ Geometry node [*Set ID*].
        
        
            Args:
                selection: Boolean
                ID: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetID`
            
            
            .. blid:: GeometryNodeSetID
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetID(geometry=self, selection=selection, ID=ID, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetID(geometry=self, selection=selection, ID=ID, label=node_label, node_color=node_color))

    def set_material(self, selection=None, material=None, node_label = None, node_color = None):
        """ Geometry node [*Set Material*].
        
        
            Args:
                selection: Boolean
                material: Material
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetMaterial`
            
            
            .. blid:: GeometryNodeSetMaterial
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetMaterial(geometry=self, selection=selection, material=material, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetMaterial(geometry=self, selection=selection, material=material, label=node_label, node_color=node_color))

    def set_material_index(self, selection=None, material_index=None, node_label = None, node_color = None):
        """ Geometry node [*Set Material Index*].
        
        
            Args:
                selection: Boolean
                material_index: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetMaterialIndex`
            
            
            .. blid:: GeometryNodeSetMaterialIndex
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index, label=node_label, node_color=node_color))

    def set_position(self, selection=None, position=None, offset=None, node_label = None, node_color = None):
        """ Geometry node [*Set Position*].
        
        
            Args:
                selection: Boolean
                position: Vector
                offset: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetPosition`
            
            
            .. blid:: GeometryNodeSetPosition
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset, label=node_label, node_color=node_color))

    def set_shade_smooth(self, selection=None, shade_smooth=None, node_label = None, node_color = None):
        """ Geometry node [*Set Shade Smooth*].
        
        
            Args:
                selection: Boolean
                shade_smooth: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetShadeSmooth`
            
            
            .. blid:: GeometryNodeSetShadeSmooth
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth, label=node_label, node_color=node_color))

    def transform(self, translation=None, rotation=None, scale=None, node_label = None, node_color = None):
        """ Geometry node [*Transform*].
        
        
            Args:
                translation: Vector
                rotation: Vector
                scale: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Transform`
            
            
            .. blid:: GeometryNodeTransform
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale, label=node_label, node_color=node_color))

    def store_named_attribute(self, name=None, value=None, data_type='FLOAT', domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Store Named Attribute*].
        
        
            Args:
                name: String
                value: Float
                data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BYTE_COLOR, BOOLEAN]
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
            
            
            .. blid:: GeometryNodeStoreNamedAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color))

    def store_named_float(self, name=None, value=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Store Named Attribute*].
        
        
            Args:
                name: String
                value: Float
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
            
                - data_type = 'FLOAT'
                  
            .. blid:: GeometryNodeStoreNamedAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color))

    def store_named_integer(self, name=None, value=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Store Named Attribute*].
        
        
            Args:
                name: String
                value: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
            
                - data_type = 'INT'
                  
            .. blid:: GeometryNodeStoreNamedAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color))

    def store_named_vector(self, name=None, value=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Store Named Attribute*].
        
        
            Args:
                name: String
                value: Vector
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
            
                - data_type = 'FLOAT_VECTOR'
                  
            .. blid:: GeometryNodeStoreNamedAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color))

    def store_named_color(self, name=None, value=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Store Named Attribute*].
        
        
            Args:
                name: String
                value: Color
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
            
                - data_type = 'FLOAT_COLOR'
                  
            .. blid:: GeometryNodeStoreNamedAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color))

    def store_named_byte_color(self, name=None, value=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Store Named Attribute*].
        
        
            Args:
                name: String
                value: Color
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
            
                - data_type = 'BYTE_COLOR'
                  
            .. blid:: GeometryNodeStoreNamedAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BYTE_COLOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BYTE_COLOR', domain=domain, label=node_label, node_color=node_color))

    def store_named_boolean(self, name=None, value=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Store Named Attribute*].
        
        
            Args:
                name: String
                value: Boolean
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
            
                - data_type = 'BOOLEAN'
                  
            .. blid:: GeometryNodeStoreNamedAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color))

    def remove_named_attribute(self, name=None, node_label = None, node_color = None):
        """ Geometry node [*Remove Named Attribute*].
        
        
            Args:
                name: String
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RemoveNamedAttribute`
            
            
            .. blid:: GeometryNodeRemoveAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RemoveNamedAttribute(geometry=self, name=name, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.RemoveNamedAttribute(geometry=self, name=name, label=node_label, node_color=node_color))

    def separate_geometry(self, selection=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Separate Geometry*].
        
        
            Args:
                selection: Boolean
                domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [selection (Geometry), inverted (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateGeometry`
            
            
            .. blid:: GeometryNodeSeparateGeometry
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain, label=node_label, node_color=node_color)

    def convex_hull(self, node_label = None, node_color = None):
        """ Geometry node [*Convex Hull*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ConvexHull`
            
            
            .. blid:: GeometryNodeConvexHull
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ConvexHull(geometry=self, label=node_label, node_color=node_color)
                
        """

        return nodes.ConvexHull(geometry=self, label=node_label, node_color=node_color).convex_hull

    def to_instance(self, *geometry, node_label = None, node_color = None):
        """ Geometry node [*Geometry to Instance*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Instances
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.GeometryToInstance`
            
            
            .. blid:: GeometryNodeGeometryToInstance
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.GeometryToInstance(self, *geometry, label=node_label, node_color=node_color)
                
        """

        return nodes.GeometryToInstance(self, *geometry, label=node_label, node_color=node_color).instances

    def join(self, *geometry, node_label = None, node_color = None):
        """ Geometry node [*Join Geometry*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.JoinGeometry`
            
            
            .. blid:: GeometryNodeJoinGeometry
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.JoinGeometry(self, *geometry, label=node_label, node_color=node_color)
                
        """

        return nodes.JoinGeometry(self, *geometry, label=node_label, node_color=node_color).geometry

    def proximity(self, source_position=None, target_element='FACES', node_label = None, node_color = None):
        """ Geometry node [*Geometry Proximity*].
        
        
            Args:
                source_position: Vector
                target_element (str): 'FACES' in [POINTS, EDGES, FACES]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [position (Vector), distance (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.GeometryProximity`
            
            
            .. blid:: GeometryNodeProximity
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element, label=node_label, node_color=node_color)
                
        """

        return nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element, label=node_label, node_color=node_color)


