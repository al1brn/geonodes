#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:08:29 2022

@author: alain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket
from geonodes.nodes import nodes
from geonodes.nodes.nodes import create_node

import bpy

import logging
logger = logging.getLogger('geonodes')

# =============================================================================================================================
# A field is the basic geometry data

class Field:
    """ > Field
    
    Field is the root class for domain attributes : ID, index, position, radius...
    
    The fields are implemented by the domains:
        
    ```python
        
    class Domain:        
        @property
        def prop(self):
            return Field(self)
        
        @prop.setter
        def prop(self, value):
            Field(self).set_value(value)
    ```
    
    In a typical scheme Field(self) 
        
    
    
    """
    
    def __init__(self, geo_domain):
        self.geo_domain  = geo_domain
        self.input_node_ = None
        self.cache_node  = True
        
    def __repr__(self):
        return f"<Field {self.geo_domain}.{type(self).__name__}>"
    
    def stack(self, node):
        return self.geo_domain.stack(node)
        
    @property
    def geometry(self):
        return self.geo_domain.data_socket
    
    @property
    def domain(self):
        return self.geo_domain.domain
    
    @property
    def selection(self):
        return self.geo_domain.selection
    
    @property
    def input_node(self):
        node = self.input_node_
        if node is None:
            node = self.create_input_node()
            node.as_attribute(owning_socket=self.geo_domain.data_socket, domain=self.domain)
            node.field_of = self
            if self.cache_node:
                self.input_node_ = node
        return node
    
    @property
    def node_socket(self):
        return self.input_node.get_datasocket(0)
    
    def create_input_node(self):
        raise RuntimeError("Input node not implemented !")        
        
    def set_value(self, value):
        raise RuntimeError(f"The field '{type(self).__name}' is read only.")
        
    # ---------------------------------------------------------------------------
    # Transfers
    
    @property
    def transfer_index(self):
        return self.geo_domain.transfer_attribute(attribute=self.node_socket, index=self.geo_domain.index, mapping='INDEX')
    
    def transfer_nearest(self, source_position=None):
        return self.geo_domain.transfer_attribute(attribute=self.node_socket, source_position=source_position, mapping='NEAREST')
    
    def transfer_nearest_face(self, source_position=None):
        return self.geo_domain.transfer_attribute(attribute=self.node_socket, source_position=source_position, mapping='NEAREST_FACE_INTERPOLATED')

# ----------------------------------------------------------------------------------------------------
# Named field

class NamedField(Field):
    """ > Named attribute

    - get        : NamedAttribute (type defined in data_type)
    - set        : StoreNamedAttribute
    - selectable : False
    """
    
    def __init__(self, geo_domain, name, data_type=None):
        super().__init__(geo_domain)
        self.name = name
        self.data_type = data_type
        
    def create_input_node(self):
        if self.data_type is None:
            raise RuntimeError(f"Data type for named attribute '{name}' not defined. You must give it in __init__ if the attribute is already stored")
        return nodes.NamedAttribute(name=self.name, data_type=self.data_type)
        
    def set_value(self, value):
        if self.data_type is None:
            self.data_type = Socket.domain_data_type(value)
        return self.stack(nodes.StoreNamedAttribute(self.geometry, name=self.name, value=value, data_type=self.data_type, domain=self.domain))
        
# ----------------------------------------------------------------------------------------------------
# ID

class ID(Field):
    """ > Field index

    - get        : ID (Integer)
    - set        : SetID
    - selectable : True
    """
    def create_input_node(self):
        return nodes.ID()
    
    def set_value(self, value):
        return self.stack(nodes.SetID(self.geometry, selection=self.selection, position=value))
    
        
# ----------------------------------------------------------------------------------------------------
# Index

class Index(Field):
    """ > Field index

    - get        : Index (Integer)
    - set        : Read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.Index()
        
# ----------------------------------------------------------------------------------------------------
# Normal

class Normal(Field):
    """ > Field index

    - get        : Normal (Vector)
    - set        : read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.Normal()
        
# ----------------------------------------------------------------------------------------------------
# Position field

class Position(Field):
    """ > Field position
    
    - get        : Position (Vector)
    - set        : SetPosition
    - selectable : True
    """
    def create_input_node(self):
        return nodes.Position()
    
    @property
    def node_socket(self):
        vector = self.input_node.get_datasocket(0)
        
        # ----- Hack to implement += in set_offset

        vector.offset_setter = lambda value: self.set_position(position=vector, offset=value)
        return vector
    
    def set_position(self, position=None, offset=None):
        return self.stack(nodes.SetPosition(self.geometry, selection=self.selection, position=position, offset=offset))

    def set_value(self, value):
        return self.stack(nodes.SetPosition(self.geometry, selection=self.selection, position=value))
    
    def set_offset(self, value):
        return self.stack(nodes.SetPosition(self.geometry, selection=self.selection, offset=value))
    
    def __iadd__(self, value):
        return self.set_offset(value)
        
    
        
# ----------------------------------------------------------------------------------------------------
# Radius

class Radius(Field):
    """ > Field index

    - get        : Radius (Float)
    - set        : SetPointRadius or SetCurveRadius
    - selectable : True
    """
    def create_input_node(self):
        return nodes.Radius()
        
    def set_value(self, value):
        if self.domain == 'CURVE':
            return self.stack(nodes.SetCurveRadius(self.geometry, selection=self.selection, radius=value))
        elif self.domain == 'POINT':
            return self.stack(nodes.SetPointRadius(self.geometry, selection=self.selection, radius=value))
        else:
            raise Exception(f"Radius attribute only available on domains POINTS and CURVE")
        
# ----------------------------------------------------------------------------------------------------
# Neighbors

class Neighbors(Field):
    """ > Field neighbors

    - get        : VertexNeighbors, EdgeNeighbors or FaceNeighbors
    - set        : Read only
    - selectable : False
    """
    def create_input_node(self):
        if self.domain == 'POINT':
            return nodes.VertexNeighbors()
        elif self.domain == 'EDGE':
            return nodes.EdgeNeighbors()
        elif self.domain == 'FACE':
            return nodes.FaceNeighbors()
        else:
            raise RuntimeError(f"There is no neighbors for domain '{self.domain}'")
            
# ----------------------------------------------------------------------------------------------------
# Area

class Area(Field):
    """ > Field face area

    - get        : FaceArea (Float)
    - set        : read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.FaceArea()
        
# ----------------------------------------------------------------------------------------------------
# Is planar

class IsPlanar(Field):
    """ > Field face is planar

    - get        : FaceIsPlanar (Boolean)
    - set        : read only
    - selectable : False
    """
    
    def __init__(self, geo_domain, threshold=None):
        super().__init__(geo_domain)
        self.threshold = threshold
        self.cache_node = False
    
    def create_input_node(self):
        return nodes.FaceArea(threshold=self.threshold)
            
# ----------------------------------------------------------------------------------------------------
# Is shade smooth

class ShadeSmooth(Field):
    """ > Field face shade smooth

    - get        : IsShadeSmooth (Boolean)
    - set        : SetShadeSmooth
    - selectable : True
    """
    
    def create_input_node(self):
        return nodes.IsShadeSmooth()
        
    def set_value(self, value):
        return self.stack(nodes.SetShadeSmooth(self.geometry, selection=self.selection, shade_smooth=value))
    
    
# ----------------------------------------------------------------------------------------------------
# Islands

class Island(Field):
    """ > Field islane

    - get        : MeshIsland (Integer)
    - set        : Read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.MeshIsland()
    
# ----------------------------------------------------------------------------------------------------
# Material index

class MaterialIndex(Field):
    """ > Field islane

    - get        : MaterialIndex (Integer)
    - set        : SetMaterialIndex
    - selectable : True
    """
    def create_input_node(self):
        return nodes.MaterialIndex()
    
    def set_value(self, value):
        return self.stack(nodes.SetMaterialIndex(self.geometry, selection=self.selection, material_index=value))

# ----------------------------------------------------------------------------------------------------
# Material selection

class MaterialSelection(Field):
    """ > Field Material selection

    - get        : MaterialSelection (Boolean)
    - set        : read only
    - selectable : False
    """
    
    def __init__(self, geo_domain, material=None):
        super().__init__(geo_domain)
        if isinstance(material, str):
            mat = bpy.data.materials.get(material)
            if mat is None:
                raise RuntimeError(f"The material named '{material}' doesn't exist")
            self.material = mat
        else:
            self.material = material
        self.cache_node = False
    
    def create_input_node(self):
        return nodes.MaterialSelection(material=self.material)
    
# ----------------------------------------------------------------------------------------------------
# Angle

class Angle(Field):
    """ > Field Material selection

    - get        : EdgeAngle (Unisgned Float and Float)
    - set        : read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.EdgeAngle()

# ----------------------------------------------------------------------------------------------------
# Edge vertices

class EdgeVertices(Field):
    """ > Field Edge vertices

    - get        : EdgeVertices (Integer, Integer, Vector, Vector)
    - set        : read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.EdgeVertices()
    
    
# ----------------------------------------------------------------------------------------------------
# Curve Tangent

class CurveTangent(Field):
    """ > Field Curve tangent

    - get        : CurveTangent (Vector)
    - set        : read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.CurveTangent()
    
# ----------------------------------------------------------------------------------------------------
# Spline length

class SplineLength(Field):
    """ > Field Spline length

    - get        : SplineLength (Float, Integer)
    - set        : read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.SplineLength()
    
# ----------------------------------------------------------------------------------------------------
# Spline parameter

class SplineParameter(Field):
    """ > Field Spline parameter

    - get        : SplineParameter (Float, Integer)
    - set        : read only
    - selectable : False
    """
    def create_input_node(self):
        return nodes.SplineParameter()
    
# ----------------------------------------------------------------------------------------------------
# Spline tilt

class Tilt(Field):
    """ > Field Spline tilt

    - get        : CurveTilt (Float)
    - set        : SetCurveTilt
    - selectable : True
    """
    def create_input_node(self):
        return nodes.CurveTilt()
    
    def set_value(self, value):
        return self.stack(nodes.SetCurveTilt(self.geometry, selection=self.selection, tilt=value))
        
        
# ----------------------------------------------------------------------------------------------------
# Spline Cyclic

class Cyclic(Field):
    """ > Field Spline Cyclic

    - get        : IsSplineCyclic (Boolean)
    - set        : SetSplineCyclic
    - selectable : True
    """
    def create_input_node(self):
        return nodes.IsSplineCyclic()
    
    def set_value(self, value):
        return self.stack(nodes.SetSplineCyclic(self.geometry, selection=self.selection, cyclic=value))
    
# ----------------------------------------------------------------------------------------------------
# End point selection

class EndpointSelection(Field):
    """ > Field Endpoint selection

    - get        : EndpointSelection (Boolean)
    - set        : Read only
    - selectable : False
    """
    
    def __init__(self, geo_domain, start_size=None, end_size=None):
        super().__init__(geo_domain)
        self.start_size = start_size
        self.end_size = end_size
        self.cache_node = False
    
    def create_input_node(self):
        return nodes.EndpointSelection(start_size=start_size, end_size=end_size)

# ----------------------------------------------------------------------------------------------------
# Spline Resolution

class SplineResolution(Field):
    """ > Field Spline Resolution

    - get        : SplineResolution (Integer)
    - set        : SetSplineResolution
    - selectable : True
    """
    def create_input_node(self):
        return nodes.SplineResolution()
    
    def set_value(self, value):
        return self.stack(nodes.SetSplineResolution(self.geometry, selection=self.selection, resolution=value))
    
# ----------------------------------------------------------------------------------------------------
# Handle Position

class HandlePositions(Field):
    """ > Field Handle Position

    - get        : CurveHandlePositions (Integer)
    - set        : SetHandlePositions
    - selectable : True
    
    CAUTION: The getter takes the **relative** parameter but not the setter
    """
    
    def __init__(self, geo_domain, relative=None, mode={'LEFT', 'RIGHT'}):
        super().__init__(geo_domain)
        self.relative   = relative
        self.mode       = mode
        self.cache_node = False
    
    def create_input_node(self):
        return nodes.CurveHandlePositions(relative=self.relative)
    
    @property
    def node_socket(self):
        if 'LEFT' in self.mode:
            return self.input_node.left
        else:
            return self.input_node.right
            
    
    @property
    def left(self):
        vector = self.input_node.left
        
        # ----- Hack to implement += in set_offset

        vector.offset_setter = lambda value: self.stack(nodes.SetHandlePositions(self.geometry, selection=self.selection, position=vector, offset=value, mode='LEFT'))
        return vector
    
    @property
    def right(self):
        vector = self.input_node.right
        
        # ----- Hack to implement += in set_offset
        
        vector.offset_setter = lambda value: self.stack(nodes.SetHandlePositions(self.geometry, selection=self.selection, position=vector, offset=value, mode='RIGHT'))
        return vector
    
    def set_position(self, position=None, offset=None):
        return self.stack(nodes.SetHandlePositions(self.geometry, selection=self.selection, position=position, offset=offset, mode=self.mode))
    

# ----------------------------------------------------------------------------------------------------
# Handle type selection

class HandleTypeSelection(Field):
    """ > Field Handle type selection

    - get        : HandleTypeSelection (Integer)
    - set        : Read only
    - selectable : False
    
    Arguments
    ---------
    
    - handle_type : str (default = 'AUTO') in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
    - mode : set (default = {'RIGHT', 'LEFT'})
    """
    
    def __init__(self, geo_domain, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        super().__init__(geo_domain)
        self.handle_type = handle_type
        self.mode        = mode
        self.cache_node  = False
    
    def create_input_node(self):
        
        print("Field", self.mode)
        return nodes.HandleTypeSelection(handle_type=self.handle_type, mode=self.mode)
    
    
    
    
    
    
    
    
        

        
