#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket, Node
from geonodes.nodes import nodes
from geonodes.nodes.nodes import create_node


import logging
logger = logging.getLogger('geonodes')


# =============================================================================================================================
# Root class for domains
#    
# Fields are properties of domains.
#   
# Components and domains
# ----------------------
#
# - Mesh component
#     - Point   : point (or points, verts)
#     - Edge    : edge  (or edges)
#     - Face    : face  (or faces)
#     - Corner  : face_corner (or corner or corners)
# - Curve component
#     - Point   : point (or points)
#     - Spline  : spline (or splines)
# - Points
#     - Point   : point (or points)
# - Instances components
#     - Instance : instans (or insts)
#
# POINT domain is share between Mesh, Curve and Points but has not the same methods
#
# The inheritance diagram is the following:
#
# - Interfaces
#   - PointInterface      : common to points : Vertex, ControlPoint and CloudPoint
#   - MeshInterface       : common to all mesh domains: Vertex, Edge, Face, Corner
#   - PEFInterface        : common to Mesh domains except Corner: Vertex, Edge and Face
#
# - Classes
#   - Domain
#     - Vertex          : POINT
#     - Edge            : EDGE
#     - Face            : FACE
#     - Corner          : CORNER
#     - ControlPoint    : POINT
#     - Spline          : CURVE
#     - CloudPoint      : POINT
#     - Instance        : INSTANCE


class Domain:
    """ Root class for domains
    
    Args:
        data_socket (DataSocket): The geometry the domain belongs to
        domain (str): Domain in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
        selection (Boolean): selection input socket
    
        
    Components and domains:
        - Mesh component
            - verts   : Vertex
            - edges   : Edge
            - faces   : Face
            - corners : Corner
            
        - Curve component
            - points  : ControlPoint
            - splines : Spline
            
        - Points
            - points   : CloudPoint
            
        - Instances components
           - insts : Instance
           
    """
    
    def __init__(self, data_socket, domain, selection=None):

        self.data_socket = data_socket
        self.domain      = domain
        self.selection   = selection
        
    def select(self, selection):
        """ Select the domain
        
        Args:
            selection (Boolean): The selection condition
        
        If a selection is existing, the resulting selection is a logical and betwenn the two
        """
        
        if self.selection is None:
            sel = selection
            
        elif selection is None:
            sel = self.selection
            
        else:
            sel = self.selection.b_and(selection)
            
        return type(self)(self.data_socket, selection=sel)
    
    def __call__(self, selection):
        return self.select(selection)
    
    def __repr__(self):
        sel = "" if self.selection is None else f" (selection: {self.selection})"
        #return f"[Domain {self.data_socket}.{self.domain}{sel}]"
        return f"[Domain {self.domain} of {self.data_socket}{sel}]"
    
    def stack(self, node):
        """ Make the owning socket jump to the output socket of the node passed in argumment.
        
        Args:
            node (Node): The node to jump to
        """
        return self.data_socket.stack(node)

    # ----------------------------------------------------------------------------------------------------
    # Access by index
    
    def __getitem__(self, index):
        
        import geonodes as gn
        
        if isinstance(index, int) or Socket.is_socket(index):
            return self.select(self.index.equal(index))
        
        elif isinstance(index, slice):
            if index.start is None:
                return self.select(self.index.less_equal(index.stop))
            
            elif index.stop is None:
                return self.select(self.index.greater_equal(index.start))
            
            else:
                center = (index.start + index.stop - 1)/2
                amp    = (index.stop - index.start - 1)/2
                return self.select(gn.Float(self.index).equal(center, epsilon=amp+0.1))
            
        elif hasattr(index, '__len__'):
            sel = None
            for i in index[:10]:
                if sel is None:
                    sel = self.index.equal(i)
                else:
                    sel = sel.b_or(self.index.equal(i))
            return self.select(sel)
        
        else:
            raise Exceptionf(f"Invalid geometry index: {index}. Only ints, slices and arrays are valid.")
            
    
    # ----------------------------------------------------------------------------------------------------
    # Force a domain change
    #
    # For instance, it can be used to manage the faces of instances of meshes
    
    @property
    def as_verts(self):
        """ Type cast to Vertex."""
        return Vertex(self.data_socket)
        
    @property
    def as_edges(self):
        """ Type cast to Edge."""
        return Edge(self.data_socket)
        
    @property
    def as_faces(self):
        """ Type cast to Face."""
        return Face(self.data_socket)
        
    @property
    def as_corners(self):
        """ Type cast to Corner."""
        return Corner(self.data_socket)
        
    @property
    def as_control_points(self):
        """ Type cast to ControlPoint."""
        return ControlPoint(self.data_socket)

    @property
    def as_splines(self):
        """ Type cast to Spline."""
        return Spline(self.data_socket)
        
    @property
    def as_cloud_points(self):
        """ Type cast to CloudPoint."""
        return CloudPoint(self.data_socket)
        
    @property
    def as_insts(self):
        """ Type cast to Instance."""
        return Instance(self.data_socket)
    
    # ----------------------------------------------------------------------------------------------------
    # Statistics
    
    def statistic(self, attribute, data_type=None):
        """ Attribute statistic
        
        call :class:`~geonodes.nodes.nodes.AttributeStatistic`
        """
        
        dt = Socket.domain_data_type(attribute) if data_type is None else Socket.domain_data_type(data_type)
        
        if dt in ['BOOLEAN', 'INT', 'COLOR']:
            dt = 'FLOAT'

        return nodes.AttributeStatistic(self.data_socket, selection=self.selection, attribute=attribute, data_type=dt, domain=self.domain)
    
    @property
    def count(self):
        """ Count the number of items by return static.max + 1
        
        Returns:
            Integer
        
        getter: :class:`AttributeStatistic`
        setter: read only
        """
        
        import geonodes as gn
        with self.data_socket.node.tree.layout(f"{self}.count", color='UTIL'):
            count = gn.Integer(self.statistic(self.index).max + 1)
            count.node_label = "count"
            return count
    
    # ----------------------------------------------------------------------------------------------------
    # Def a node as attribute node
    
    def attribute(self, node):
        """ Define an input node as attribute
        
        Args:
            node (Node): The node created by the domain
            
        Returns:
            The node argument
        
        Called when creating an input node in a property getter. Performs two actions:
            
            - Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
              This will allow the :func:`Tree.check_attributes` to see if it is necessary to create
              a *Capture Attribute* for this field.
            - Set the nde property :attr:`field_of` to self in order to implement the transfer attribute
              mechanism.
        """

        node.as_attribute(owning_socket=self.data_socket, domain=self.domain)
        node.field_of = self
        return node
    

    # ----------------------------------------------------------------------------------------------------
    # > Get a named attribute socket
    #
    # Make use named_field method
    
    def get_named_attribute(self, name, data_type='FLOAT'):
        """ Get a named attribute
        
        Called by methods set_named_xxx:
            
        - :func:`get_named_boolean`
        - :func:`get_named_integer`
        - :func:`get_named_float`
        - :func:`get_named_vector`
        - :func:`get_named_color`
        """
        
        if data_type is None:
            raise RuntimeError(f"Data type for named attribute '{name}' not defined")
            
        return self.attribute(nodes.NamedAttribute(name=name, data_type=data_type)).get_datasocket(0)
        
    # ----------------------------------------------------------------------------------------------------
    # > Set a named attribute socket
    #
    # Make use named_field method
    #
    # If data_type is None, the data_type is infered from the type of the value
    
    def set_named_attribute(self, name, value, data_type=None):
        """ Set a named attribute
        
        Called by classes set_named_xxx:
            
        - :func:`set_named_boolean`
        - :func:`set_named_integer`
        - :func:`set_named_float`
        - :func:`set_named_vector`
        - :func:`set_named_color`
        - :func:`set_named_byte_color`
        """
        
        if data_type is None:
            data_type = Socket.domain_data_type(value)
        
        return self.stack(nodes.StoreNamedAttribute(self.data_socket, name=name, value=value, data_type=data_type, domain=self.domain))

    def get_named_boolean(self, name):
        """ Get named attribute of type BOOLEAN"""
        return self.get_named_attribute(name, data_type='BOOLEAN')

    def get_named_integer(self, name):
        """ Get named attribute of type INT"""
        return self.get_named_attribute(name, data_type='INT')
        
    def get_named_float(self, name):
        """ Get named attribute of type FLOAT"""
        return self.get_named_attribute(name, data_type='FLOAT')

    def get_named_vector(self, name):
        """ Get named attribute of type FLOAT_VECTOR"""
        return self.get_named_attribute(name, data_type='FLOAT_VECTOR')
        
    def get_named_color(self, name):
        """ Get named attribute of type FLOAT_COLOR"""
        return self.get_named_attribute(name, data_type='FLOAT_COLOR')
        
    # NOT SUPPORTED YET
    #def get_named_byte_color(self, name):
    #    return self.get_named_attribute(name, data_type='BYTE_COLOR')
    
    
    def set_named_boolean(self, name, value):
        """ Set named attribute of type BOOLEAN"""
        self.set_named_attribute(name, value, data_type='BOOLEAN')

    def set_named_integer(self, name, value):
        """ Set named attribute of type INT"""
        self.set_named_attribute(name, value, data_type='INT')
        
    def set_named_float(self, name, value):
        """ Set named attribute of type FLOAT"""
        self.set_named_attribute(name, value, data_type='FLOAT')

    def set_named_vector(self, name, value):
        """ Set named attribute of type FLOAT_VECTOR"""
        self.set_named_attribute(name, value, data_type='FLOAT_VECTOR')
        
    def set_named_color(self, name, value):
        """ Set named attribute of type FLOAT_COLOR"""
        self.set_named_attribute(name, value, data_type='FLOAT_COLOR')
        
    def set_named_byte_color(self, name, value):
        """ Set named attribute of type BYTE_COLOR"""
        self.set_named_attribute(name, value, data_type='BYTE_COLOR')
        
    # ====================================================================================================
    # Transfer attribute

    def transfer_attribute(self, attribute, source_position=None, index=None, data_type=None, mapping='NEAREST_FACE_INTERPOLATED'):
        """ Transfer attribute
        
        Args:
            attribute (Any): The attribute to transfer
            source_position (Vector): Source position socket
            index (Integer): Index socket
            data_type (str): A valid data type
            mapping (str): str in ('NEAREST', 'INDEX', 'NEAREST_FACE_INTERPOLATED').
            
        Returns:
            As defined by data_type
            
        If data_type is None, it is computed from the attribute type.
        
        This method is called by a DataSocket with a property :attr:`field_of` pointing on the domain:
            
        .. code-block:: python
        
            # Domain Vertex
        
            verts = mesh.verts
            
            # Attribute position: position.field_of = verts
        
            position = verts.position
            
            # Transfer to a var

            location = position.index_transfer()
            
            # Which is equivalent to:
                
            location = verts.index_transfer(verts.position)
        
        """
        
        dt = Socket.domain_data_type(attribute) if data_type is None else Socket.domain_data_type(data_type)
        
        return nodes.TransferAttribute(self.data_socket, attribute=attribute, source_position=source_position, index=index,
                        data_type=dt, domain=self.domain, mapping=mapping).attribute

    def index_transfer(self, attribute, index=None):
        """ Transfer attribute with INDEX mapping
        
        Args:
            attribute (Any): The attribute to transfer
            index (Integer): Index
            
        Returns:
            Same as attribute
        """
        return self.transfer_attribute(attribute, index=index, mapping='INDEX')

    def nearest_transfer(self, attribute, source_position=None):
        """ Transfer attribute with NEAREST mapping
        
        Args:
            attribute (Any): The attribute to transfer
            source_position (Vector): Source position socket
            
        Returns:
            Same as attribute
        """
        return self.transfer_attribute(attribute, source_position=source_position, mapping='NEAREST')

    def nearest_face_transfer(self, attribute, source_position=None):
        """ Transfer attribute with NEAREST_FACE_INTERPOLATED mapping
        
        Args:
            attribute (Any): The attribute to transfer
            source_position (Vector): Source position socket
            
        Returns:
            Same as attribute
        """
        return self.transfer_attribute(attribute, source_position=source_position, mapping='NEAREST_FACE_INTERPOLATED')        
        
    # ====================================================================================================
    # Fields all domain have
        
    @property
    def ID(self):
        """ ID attribute
        
        Returns:
            Integer
        
        - getter: :class:`~geonodes.nodes.nodes.ID`
        - setter: :class:`~geonodes.nodes.nodes.SetID`
        """
        
        return self.attribute(nodes.ID()).get_datasocket(0)
    
    @ID.setter
    def ID(self, value):
        return self.stack(nodes.SetID(self.data_socket, selection=self.selection, ID=value))
    
    @property
    def index(self):
        """ Index attribute
        
        Returns:
            Integer
        
        - setter: :class:`~geonodes.nodes.nodes.Index`
        - setter: Read only
        """
        
        return self.attribute(nodes.Index()).get_datasocket(0)
        
    
    @property
    def position(self):
        """ Position attribute
        
        Returns:
            Vector
        
        - getter: :class:`~geonodes.nodes.nodes.Position`
        - setter: :class:`~geonodes.nodes.nodes.SetPosition`
        """
        
        vector = self.attribute(nodes.Position()).get_datasocket(0)
        
        # ----- Hack to implement += in set_offset

        vector.offset_setter = lambda value: self.stack(nodes.SetPosition(self.data_socket, selection=self.selection, offset=value))
        vector.point_domain  = self
        
        return vector
        
    
    @position.setter
    def position(self, value):
        
        # When implemented +=, __iadd__ returns None
        
        if value is None:
            return
        
        # No setter
        
        if self.domain in ['EDGE', 'FACE', 'CORNER']:
            raise Exception(f"The position of edges, faces and corners is read only")
            
        # Let's go
        
        return self.stack(nodes.SetPosition(self.data_socket, selection=self.selection, position=value))
        
    @property
    def offset(self):
        """ "Offset" attribute (offset socket of *SetPosition* node)
        
        Returns:
            Vector
        
        - getter: :class:`~geonodes.nodes.nodes.Position`
        - setter: :class:`~geonodes.nodes.nodes.SetPosition`
        """
        
        return Node.Vector(0)
    
    @offset.setter
    def offset(self, value):
        
        # No setter
        
        if self.domain in ['EDGE', 'FACE', 'CORNER']:
            raise Exception(f"The position of edges, faces and corners is read only")
            
        # Let's go
        
        return self.stack(nodes.SetPosition(self.data_socket, selection=self.selection, offset=value))
    
    # ====================================================================================================
    # Methods for all domains
    
    def duplicate(self, amount=None):
        """ Duplicate domain.
        
        Node :class:`~geonodes.nodes.nodes.DuplicateElements`
        
        Args:
            amount : Integer
            
        Returns:
            duplicate index
        """
        
        node = nodes.DuplicateElements(self.data_socket, self.selection, amount=amount, domain=self.domain)
        self.stack(node)
        return node.duplicate_index
    
    #def __mul__(self, other):
    #    self.duplicate(amount=other)
    #    return self
    
    #def __rmul__(self, other):
    #    return self * other
    
    def __imul__(self, other):
        self.duplicate(amount=other)
    
    # ====================================================================================================
    # Field at index
    
    def field_at_index(self, index=None, value=None, data_type=None):
        """ Field at index
        
        Args:
            index (Integer): index to use for getting the attributes
            value (Any): the value to collect from the domain
            data_type (str): the value data_type. Can be None
            
        Returns:
            The field values
            
        If data_type is None, it is computed from the attribute type.
        """


        dt = Socket.domain_data_type(value) if data_type is None else Socket.domain_data_type(data_type)
        
        if index is None:
            index = self.index
        
        return self.attribute(nodes.FieldAtIndex(index=index, value=value, data_type=dt, domain=self.domain)).value    
    
    
    
        
# =============================================================================================================================
# Point
#
# Properties and methods shared by all POINT domains:
# - Vertex
# - ControlPoiint
# - CloudPoint

class Point(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='POINT', selection=selection)
    
    
    def instantiate(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ Put instances on points
        
        Node :class:`~geonodes.nodes.nodes.InstanceOnPoints`
        
        Args:
            instance : Geometry
            pick_instance : Boolean
            instance_index : Integer
            rotation : Vector
            scale : Vector
            
        Returns:
            Instances

        Example:
            
            .. code-block:: python

            mesh.verts(...).instantiate(...)
            curve.points(...).instantiate(...)
            cloud.points(...).instantiate(...)
        """
        
        return nodes.InstanceOnPoints(
                points=self.data_socket, selection=self.selection, 
                instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale
                ).instances
        
# =============================================================================================================================
# Mesh domains
#
# Mesh domains are:
# - Vertex
# - Edge
# - Face
# - Corner
#
# Vertex, Edge and Face share the interface PEFInterface


# -----------------------------------------------------------------------------------------------------------------------------
# Properties and methodes shared by all Mesh domains: Point, Edge,  Face and Corner

class MeshInterface:
    
    @property
    def normal(self):
        """ Normal attribute
        
        Returns:
            Vector
        
        - getter: :class:`~geonodes.nodes.nodes.Normal`
        - setter: readonly
        """
        
        return self.attribute(nodes.Normal()).get_datasocket(0)
    
    @property
    def island(self):
        """ Island node attribute
        
        Returns:
            Node MeshIsland
            
        getter: :class:`~geonodes.nodes.nodes.MeshIsland`
        setter: read only
        """
        
        return self.attribute(nodes.MeshIsland())
        
    @property
    def island_index(self):
        """ island_index output socket of Island attribute
        
        Returns:
            Int
            
        getter: :class:`~geonodes.nodes.nodes.MeshIsland`
        setter: read only
        """

        return self.island.island_index
    
        
    @property
    def island_count(self):
        """ island_count output socket of Island attribute
        
        Returns:
            Int
            
        getter: :class:`~geonodes.nodes.nodes.MeshIsland`
        setter: read only
        """

        return self.island.island_count
    
    
    # ====================================================================================================
    # Methods
    
    def to_points(self, position=None, radius=None):
        """ Convert to points cloud.
        
        Node :class:`MeshToPoints` 
        
        Args:
            position : Vector
            radius : Float
            
        Returns:
            Points
            
        Example:
            
            .. code-block:: python
        
            mesh.verts.to_points(...)
            mesh.edges.to_points(...)
            mesh.faces.to_points(...)
            mesh.corners.to_points(...)
        """

        mode = {'POINT': 'VERTICES', 'EDGE': 'EDGES', 'FACE': 'FACES', 'CORNER': 'CORNERS'}[self.domain]
        return nodes.MeshToPoints(
            mesh=self.data_socket, selection=self.selection, position=position, radius=radius, mode=mode).points

# -----------------------------------------------------------------------------------------------------------------------------
# Properties and methodes shared by Mesh Point, Edge and Face (but not Corner)

class PEFInterface:
    
    def delete(self, mode='ALL'):
        """ Delete geometry
        
        Node :class:`DeleteGeometry`
        
        Args:
            mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')      
            
        Returns:
            self
        
        .. code-block:: python

            mesh.verts(...).delete(mode='ALL')
            mesh.edges(...).delete(mode='EDGE_FACE')
            mesh.faces(...).delete(mode='ONLY_FACE')
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))
    
    def delete_all(self):
        """ Delete all geometry.
        
        call :func:`delete` with mode : 'ALL'
            
        Returns:
            self
        
        .. code-block:: python

            mesh.verts(...).delete_all()
            mesh.edges(...).delete_all()
            mesh.faces(...).delete_all()
        """
        return self.delete(mode='ALL')
        
    def delete_faces(self):
        """ Delete faces
        
        call :func:`delete` with mode : 'ONLY_FACE'
            
        Returns:
            self
        
        .. code-block:: python

        mesh.verts(...).delete_faces()
        mesh.edges(...).delete_faces()
        mesh.faces(...).delete_faces()
        """
        return self.delete(mode='ONLY_FACE')
        
    def delete_edges_faces(self):
        """ Delete edges and faces.
        
        call :func:`delete` with mode : 'EDGE_FACE'
            
        Returns:
            self
        
        .. code-block:: python
        
            mesh.verts(...).delete_edges_faces()
            mesh.edges(...).delete_edges_faces()
            mesh.faces(...).delete_edges_faces()
        """
        return self.delete(mode='EDGE_FACE')
    
    def proximity(self, source_position=None):
        """ Proximity.
        
        Node :class:`~geonodes.nodes.nodes.GeometryProximity`
        
        Args:
            source_position: Vector
            
        Returns:
            Node with two sockets:
                
                - position : Vector
                - distance : Float
        
        .. code-block:: python
            
            mesh.verts(...).proximity()
            mesh.edges(...).proximity()
            mesh.faces(...).proximity()
        """
        target_element = self.domain + 'S'
        return nodes.GeometryProximity(target=self.data_socket, source_position=source_position, target_element=target_element)
        
    
    def extrude(self, offset=None, offset_scale=None, individual=None):
        """ Extrusion.
        
        Node :class:`~geonode.nodes.nodes.ExtrudeMesh`
        
        Args:
            offset : Vector
            offset_scale : Float
            individual : Boolean
            
        Returns:
            tuple with top and side selections
                            
        .. code-block:: python
            
             top, side = mesh.verts(...).extrude(...)
             top, side = mesh.edges(...).extrude(...)
             top, side = mesh.faces(...).extrude(...)
             
             # Example of insetting and extruding the faces of a mesh
             
             top, _ = mesh.faces.extrude(offset_scale=0)
             top.scale(0.5)
             top1, _ = top.extrude(top.normal, .3)
        """
        mode = {'POINT': 'VERTICES', 'EDGE': 'EDGES', 'FACE': 'FACES'}[self.domain]
        node = nodes.ExtrudeMesh(
            mesh=self.data_socket, selection=self.selection,
            offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)
        self.stack(node)
        
        if self.domain == 'POINT':
            return self.data_socket.verts(node.top), self.data_socket.faces(node.side)
        
        elif self.domain == 'EDGE':
            return self.data_socket.edges(node.top), self.data_socket.faces(node.side)
        else:
            
            return self.data_socket.faces(node.top), self.data_socket.faces(node.side)
        
        # OLD !
        return self.select(node.top), self.select(node.side)
    
    def scale(self, scale=None, center=None, axis=None, scale_mode='UNIFORM'):
        """ Scale a face or an edge.
        
        Node :class:`~geonodes.nodes.nodes.ScaleElements`
        
        scale_uniform and scale_single_axis can be called without the argument scale_mode
        
        Args:
            scale : Float
            center : Vector
            axis : Vector
            scale_mode : str (default = 'UNIFORM') in ('UNIFORM', 'SINGLE_AXIS')
            
        Returns:
            self
                            
        .. code-block:: python
            
             mesh.edges(...).scale(...)
             mesh.faces(...).scale(...)
        """
        
        if self.domain == 'POINT':
            raise Exception(f"Vertices are not scalable: scale method can't be called")
            
        return self.stack(nodes.ScaleElements(
            geometry=self.data_socket, selection=self.selection,
            scale=scale, center=center, axis=axis, domain=self.domain, scale_mode=scale_mode))
        
    def scale_uniform(self, scale=None, center=None):
        """ Scale a face or an edge in uniform mode.
        
        call :func:`scale` with mode='UNIFORM'
        
        Args:
            scale : Float
            center : Vector
            
        Returns:
            self
        
        .. code-block:: python
            
             mesh.edges(...).scale_uniform(...)
             mesh.faces(...).scale_uniform(...)
        """
        return self.scale(scale=scale, center=center, mode='UNIFORM')
        
    def scale_single_axis(self, scale=None, center=None, axis=None):
        """ Scale a face or an edge in single axis mode.
        
        call :func:`scale` with mode='SINGLE_AXIS'
        
        Args:
            scale : Float
            center : Vector
            
        Returns:
            self
            
        .. code-block:: python
            
             mesh.edges(...).scale_single_axis(...)
             mesh.faces(...).scale_single_axis(...)
        """
        return self.scale(scale=scale, center=center, axis=axis, mode='SINGLE_AXIS')
    
        
# -----------------------------------------------------------------------------------------------------------------------------
# vertex: the point domain of meshes

class Vertex(Point, MeshInterface, PEFInterface):
    
    @property
    def neighbors(self):
        """ Neighbors
        
        Returns:
            Node *VertexNeighbors*
        
        - getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
        - setter: read only
        """
        return self.attribute(nodes.VertexNeighbors())
        
    @property
    def neighbors_vertices(self):
        """ Neighbors vertices attribute
        
        Returns:
            Integer: The output socket *vertices* of the *VertexNeighbors* node.
        
        - getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
        - setter: read only
        """
        
        return self.neighbors.get_datasocket(0)

        
        if self.domain == 'POINT':
            return nodes.VertexNeighbors()
        elif self.domain == 'EDGE':
            return nodes.EdgeNeighbors()
        elif self.domain == 'FACE':
            return nodes.FaceNeighbors()
        
    @property
    def neighbors_faces(self):
        """ Neighbors faces attribute
        
        Returns:
            Integer: The output socket *faces* of the *VertexNeighbors* node.
        
        - getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
        - setter: read only
        """
        
        return self.neighbors.get_datasocket(1)
    
    # ====================================================================================================
    # Methods
    
    def merge(self, distance=0.001, mode='ALL'):
        """ Merge vertices by distance.
        
        Node :class:`~geonodes.nodes.nodes.MergeByDistance`

        Args:
            distance (Float): The merge distance
            mode (str): str (default = 'ALL') in ('ALL', 'CONNECTED')        
            
        Returns:
            self

        .. code-block:: python
            
            mesh.verts().merge()
        """
        return self.stack(nodes.MergeByDistance(self.data_socket, selection=self.selection, distance=distance, mode=mode))

    def merge_connected(self, distance=0.001):
        """ Merge connected vertices by distance.
        
        call :func:`merge` with mode = 'CONNECTED'

        Args:
            distance (Float): The merge distance
            
        Returns:
            self

        .. code-block:: python
            
            mesh.verts().merge_connected()
        """
        return self.merge(distance=distance, mode='CONNECTED')
        
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Face domain

class Face(Domain, MeshInterface, PEFInterface):

    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='FACE', selection=selection)
        
    # ----------------------------------------------------------------------------------------------------
    # Transfer attribute

    def transfer_attribute_interpolated(self, attribute, source_position=None, data_type=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute(attribute, source_position=source_position, data_type=data_type, mapping='NEAREST_FACE_INTERPOLATED')
    
    def transfer_boolean_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='BOOLEAN')
        
    def transfer_integer_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='INT')
        
    def transfer_float_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='FLOAT')
        
    def transfer_vector_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='FLOAT_VECTOR')
        
    def transfer_color_interpolated(self, attribute, source_position=None):
        """ <method GeometryNodeAttributeTransfer>
        
        for other mapping, use transfer_attribute
        """
        return self.transfer_attribute_interpolated(attribute, source_position=source_position, data_type='FLOAT_COLOR')

    # ----------------------------------------------------------------------------------------------------
    # Fields
    
    @property
    def neighbors(self):
        """ Neighbors node
        
        Returns:
            Node FaceNeighbors
        
        - getter: :class:`~geonodes.nodes.nodes.FaceNeighbors`
        - setter: read only
        """
        return self.attribute(nodes.FaceNeighbors())
    
    @property
    def neighbors_vertices(self):
        """ Neighbors vertices attribute
        
        Returns:
            Integer: the output socket *vertices* of the *FaceNeighbors* node.
        
        - getter: :class:`~geonodes.nodes.nodes.FaceNeighbors`
        - setter: read only
        """
        
        return self.neighbors.get_datasocket(0)

        
    @property
    def neighbors_faces(self):
        """ Neighbors faces attribute
        
        Returns:
            Integer: The output socket *faces* of the *FaceNeighbors* node.
        
        - getter: :class:`~geonodes.nodes.nodes.FaceNeighbors`
        - setter: read only
        """
        
        return self.neighbors.get_datasocket(1)
        
    @property
    def area(self):
        """ Area attribute
        
        Returns:
            Float

        - getter: :class:`~geonodes.nodes.nodes.FaceArea`
        - setter: read only
        
        """
        
        return self.attribute(nodes.FaceArea()).get_datasocket(0)
        
    
    def is_planar(self, threshold=None):
        """ Attribute is_planar
        
        Args:
            threshold: Float
            
        Returns:
            Boolean
            
        - getter: :class:`~geonodes.nodes.nodes.FaceIsPlanar`
        - setter: read only
        """
        
        return self.attribute(nodes.FaceIsPlanar(threshold=threshold)).get_datasocket(0)

    @property
    def shade_smooth(self):
        """ Area attribute
        
        Returns:
            Boolean

        - getter: :class:`~geonodes.nodes.nodes.IsShadeSmooth`
        - setter: :class:`~geonodes.nodes.nodes.SetShadeSmooth`
        """

        return self.attribute(nodes.IsShadeSmooth()).get_datasocket(0)
    
    @shade_smooth.setter
    def shade_smooth(self, value):
        
        self.stack(nodes.SetShadeSmooth(self.data_socket, selection=self.selection, shade_smooth=value))

        
    @property
    def material_index(self):
        """ Material index attribute
        
        Returns:
            Integer

        - getter: :class:`~geonodes.nodes.nodes.MaterialIndex`
        - setter: :class:`~geonodes.nodes.nodes.SetMaterialIndex`
        """
        
        return self.attribute(nodes.MaterialIndex()).get_datasocket(0)
        
    
    @material_index.setter
    def material_index(self, value):
        
        self.stack(nodes.SetMaterialIndex(self.data_socket, selection=self.selection, material_index=value))
        
        
    def set_material(self, material):
        """ Material attribute
        
        Args:
            material (str or bpy.types.Material): The material to set
        
        - setter: :class:`~geonodes.nodes.nodes.SetMaterial`
        """
        
        import bpy
        if isinstance(material, str):
            mat = bpy.data.materials.get(material)
            if mat is None:
                raise Exception(f"Face.material: material {material} not found.")
        else:
            mat = material
        
        return self.stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=mat))
    
    @property
    def material(self):
        """ Material attribute
        
        - getter: write only
        - setter: :class:`~geonodes.nodes.nodes.SetMaterial`
        """
        
        raise Exception(f"Face.material is a write only property")
        
    @material.setter
    def material(self, value):
        self.set_material(value)
    
    def material_selection(self, material=None):
        """ Material selection attribule
        
        Args:
            material (str or bpy.types.Material): The material to select
        
        Returns:
            Boolean

        - getter: :class:`~geonodes.nodes.nodes.MaterialSelection`
        """
        
        import bpy
        if isinstance(material, str):
            mat = bpy.data.materials.get(material)
            if mat is None:
                raise Exception(f"Face.material: material {material} not found.")
        else:
            mat = material
        
        return self.attribute(nodes.MaterialSelection(mat)).get_datasocket(0)
    
    # ====================================================================================================
    # Methods
    
    def flip(self):
        """ Flip faces.
        
        Node :class:`~geonodes.nodes.nodes.FlipFaces`
            
        Returns:
            self
        
        .. code-block:: python
            
            mesh.faces.flip()
        """
        return self.stack(nodes.FlipFaces(mesh=self.data_socket, selection=self.selection))
    
    def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ Triangulate faces.
        
        Node :class:`~geonodes.nodes.nodes.Triangulate`
        
        Args:
            minimum_vertices : Integer
            ngon_method (str): (default = 'BEAUTY') in ('BEAUTY', 'CLIP')
            quad_method (str): (default = 'SHORTEST_DIAGONAL') in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
            
        Returns:
            self

        .. code-block:: python
            
            mesh.faces(...).triangulate(...)
        """
        return self.stack(nodes.Triangulate(
            mesh=self.data_socket, selection=self.selection,
            minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))
    
    def distribute_points(self, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """ Distribute points on faces.
        
        Node :class:`~geonodes.nodes.nodes.DistributePointsOnFaces`

        Args:
            distance_min : Float
            density_max : Float
            density : Float
            density_factor : Float
            seed : Integer
            distribute_method (str): (default = 'RANDOM') in ('RANDOM', 'POISSON')

        Returns:
            Node with 3 sockets:
                
                - points : Points
                - normal : Vector
                - rotation : Vector
            
        .. code-block:: python
            
            node = mesh.faces.distribute_points(...)
            cloud = node.points
            normal = node.normal
            rotation = node.rotation
        """
        
        return nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection,
                distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor,
                seed=seed, distribute_method=distribute_method)
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Edge domain
        
class Edge(Domain, MeshInterface, PEFInterface):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='EDGE', selection=selection)
        
    @property
    def neighbors_faces(self):
        """ Neighbors (faces count)
        
        Returns:
            Integer
        
        - getter: :class:`~geonodes.nodes.nodes.EdgeNeighbors`
        - setter: read only
        """
        return self.attribute(nodes.EdgeNeighbors()).get_datasocket(0)
    
    @property
    def edge_angle(self):
        """ Edge angle node
        
        Returns:
            Node *EdgeAngle*
        
        - getter: :class:`~geonodes.nodes.nodes.EdgeAngle`
        - setter: read only
        """
        return self.attribute(nodes.EdgeAngle())

    @property
    def unsigned_angle(self):
        """ Unsigned angle
        
        Returns:
            Float: Unsigned output socket of *EdgeAngle*
        
        - getter: :class:`~geonodes.nodes.nodes.EdgeAngle`
        - setter: read only
        """
        
        return self.edge_angle.unisgned_angle

    @property
    def angle(self):
        """ Signed angle
        
        Returns:
            Float: Signed output socket of *EdgeAngle*
        
        - getter: :class:`~geonodes.nodes.nodes.EdgeAngle`
        - setter: read only
        """
        
        return self.edge_angle.signed_angle
    
    @property
    def vertices(self):
        """ EdgeVertices node
        
        Returns:
            Node *EdgeVertices*
            
        Output sockets:
            - vertex_index_1 : Integer
            - vertex_index_2 : Integer
            - position_1 : Vector
            - position_2 : Vector
        
        - getter: :class:`~geonodes.nodes.nodes.EdgeVertices`
        - setter: read only
        """
        
        return self.attribute(nodes.EdgeVertices())
    
    @property
    def vertex_index(self):
        """ The indices of the vertices composing the edge
        
        Returns:
            (Integer, Integer)
        
        - getter: :class:`~geonodes.nodes.nodes.EdgeVertices`
        - setter: read only
        """
        
        node = self.vertices
        return node.vertex_index_1, node.vertex_index_2
    
    @property
    def vertex_position(self):
        """ The position of the vertices composing the edge
        
        Returns:
            (Float, Float)
        
        - getter: :class:`~geonodes.nodes.nodes.EdgeVertices`
        - setter: read only
        """
        
        node = self.vertices
        return node.position_1, node.position_2

    
    # ====================================================================================================
    # Methods
    
    def to_curve(self):
        """ Convert edges to curve.
        
        Node :class:`~geonodes.nodes.nodes.MeshToCurve`
            
        Returns:
            Curve
            
        .. code-block:: python
            
            mesh.edges.to_curve(...)
        """
        return nodes.MeshToCurve(
            mesh=self.data_socket, selection=self.selection).curve
    
    def split(self):
        """ Split edges.
        
        Node :class:`SplitEdges`
            
        Returns:
            self
        
        .. code-block:: python
            
            mesh.edges.split()
        """
        return self.stack(nodes.SplitEdges(mesh=self.data_socket, selection=self.selectoin))
    
# ---------------------------------------------------------------------------
# Face corner domain

class Corner(Domain, MeshInterface):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='CORNER', selection=selection)
        
# =============================================================================================================================
# Curve domains

# ----------------------------------------------------------------------------------------------------
# Control point : the point domain of splines

class ControlPoint(Point):

    # ----------------------------------------------------------------------------------------------------
    # Radius and tilt
        
    @property
    def radius(self):
        """ Radius attribute
        
        Returns:
            Float
            
        getter: :class:`~geonodes.nodes.nodes.Radius`
        setter: :class: `~geonodes.nodes.nodes.SetCurveRadius`
        """
        return self.attribute(nodes.Radius()).get_datasocket(0)
    
    @radius.setter
    def radius(self, value):
        self.stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=value))
        
    @property
    def tilt(self):
        """ Tilt attribute
        
        Returns:
            Float
            
        getter: :class:`~geonodes.nodes.nodes.CurveTilt`
        setter: :class: `~geonodes.nodes.nodes.SetCurveTilt`
        """
        return self.attribute(nodes.CurveTilt()).get_datasocket(0)
    
    @tilt.setter
    def tilt(self, value):
        self.stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=value))
        
    @property
    def tangent(self):
        """ Tangent attribute
        
        Returns:
            Vector
            
        getter: :class:`~geonodes.nodes.nodes.CurveTangent`
        setter: read only
        """
        return self.attribute(nodes.CurveTangent()).get_datasocket(0)
        
    # ----------------------------------------------------------------------------------------------------
    # Handles
        
    # ----- Handles type

    def set_handle_type(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ Set handle type
        
        Args:
            handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
            mode (set of strs): {'LEFT', 'RIGHT'}
        """
        
        stype = handle_type.upper()
        valid_types = ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        if not stype in valid_types:
            raise Exception(f"'{handle_type}' is not a valid handle type. Valid types are {valid_types}")
        
        return self.stack(nodes.SetHandleType(curve=self.data_socket, selection=self.selection, handle_type=stype, mode=mode))
    
    @property
    def handle_type(self):
        """ Handle type attribute
        
        - getter: write only
        - setter: :class:`~geonodes.nodes.nodes.SetHandleType`
        """

        raise Exception(f"'handle_type' is a write only property")
        
    @handle_type.setter
    def handle_type(self, value):
        self.set_handle_type(handle_type=value, mode={'LEFT', 'RIGHT'})
        
    @property
    def left_type(self):
        """ Left handle type attribute
        
        - getter: write only
        - setter: :class:`~geonodes.nodes.nodes.SetHandleType`
        """

        raise Exception(f"'left_type' is a write only property")
        
    @left_type.setter
    def left_type(self, value):
        return self.set_handle_type(handle_type=value, mode={'LEFT'})
        
    @property
    def right_type(self):
        """ Left handle type attribute
        
        - getter: write only
        - setter: :class:`~geonodes.nodes.nodes.SetHandleType`
        """
        
        raise Exception(f"'right_type' is a write only property")
        
    @right_type.setter
    def right_type(self, value):
        return self.set_handle_type(handle_type=value, mode={'RIGHT'})

    # ----- Handles position / offset
    
    def handle_positions(self, relative=None):
        """ Handle positions node
        
        Args:
            relative (Boolean): relative
            
        Returns:
            node CurveHandlePositions
            
        Output sockets:
            - left : Vector
            - right : Vector
        """
        return self.attribute(nodes.CurveHandlePositions(relative=relative))
    
    def set_handle_positions(self, position=None, offset=None, mode='LEFT'):
        """ Set handle positions
        
        Args:
            position (Vector): Positions
            offset (Vector): Offset
            mode (str): 'LEFT' or 'RIGHT'

        - setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
        """
        
        self.stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode=mode))
        
        
    def left_handles(self, relative=None):
        """ Left handle positions
        
        Args:
            relative (Boolean): relative
            
        Returns:
            Vector: the left output socket of node *CurveHandlePositions*
        """
        
        vector = self.handle_positions(relative=relative).left
        
        # ----- Hack to implement += in set_offset

        vector.offset_setter = lambda value: self.stack(nodes.SetHandlePositions(self.data_socket, selection=self.selection, offset=value, mode='LEFT'))
        vector.point_domain  = self
        
        return vector
    
    def right_handles(self, relative=None):
        """ Right handle positions
        
        Args:
            relative (Boolean): relative
            
        Returns:
            Vector: the right output socket of node *CurveHandlePositions*
        """
        vector = self.handle_positions(relative=relative).left
        
        # ----- Hack to implement += in set_offset

        vector.offset_setter = lambda value: self.stack(nodes.SetHandlePositions(self.data_socket, selection=self.selection, offset=value, mode='RIGHT'))
        vector.point_domain  = self
        
        return vector
    
    @property
    def left_handle_positions(self):
        """ Right handle positions, write only
        
        - getter: read only
        - setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
        """
        
        raise Exception(f"left_handle_positions is write only. Use left_handles(relative: Boolean) to get the positions of left handles")
    
    @left_handle_positions.setter
    def left_handle_positions(self, value):
        return self.set_handle_positions(position=value, mode='LEFT')
    
        
    @property
    def right_handle_positions(self):
        """ Right handle positions, write only
        
        - getter: write only
        - setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
        """
        
        raise Exception(f"right_handle_positions is write only. Use right_handles(relative: Boolean) to get the positions of right handles")
    
    @right_handle_positions.setter
    def right_handle_positions(self, value):
        return self.set_handle_positions(position=value, mode='RIGHT')
    
    @property
    def left_handle_offsets(self):
        """ Left handle offsets, write only
        
        - getter: write only
        - setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
        """
        
        raise Exception(f"left_handle_offsets is write only. Use left_handles(relative: Boolean) to get the positions of left handles")
    
    @left_handle_offsets.setter
    def left_handle_offsets(self, value):
        return self.set_handle_positions(offset=value, mode='LEFT')
    
    @property
    def right_handle_offsets(self):
        """ Right handle offsets, write only
        
        - getter: write only
        - setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
        """
        
        raise Exception(f"right_handle_offsets is write only. Use right_handles(relative: Boolean) to get the positions of right handles")
    
    @right_handle_offsets.setter
    def right_handle_offsets(self, value):
        return self.set_handle_positions(offset=value, mode='RIGHT')
    

    # ----- Handle selection
    
    def handles_selection(self, handle_type='AUTO', left=True, right=True):
        """ Handle type selection
        
        Args:
            handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
            left (bool): select left handle
            right (bool): select right handle
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        
        mode = set()
        if left:  mode.add('LEFT')
        if right: mode.add('RIGHT')
        
        valids = ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        stype = handle_type.upper()
        if stype not in valids:
            raise Exception(f"Points.handles: the handle type '{handle_type}' is not valid. It should be in {valids}.")
            
        return self.attribute(nodes.HandleTypeSelection(handle_type=stype, mode=mode)).get_datasocket(0)
    
    @property
    def handle_auto(self):
        """ Auto Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='AUTO')
    
    @property
    def handle_free(self):
        """ Free Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='FREE')
    
    @property
    def handle_vector(self):
        """ Vector Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='VECTOR')
    
    @property
    def handle_align(self):
        """ Align Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='ALIGN')
    
    @property
    def left_handle_auto(self):
        """ Left Auto Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='AUTO', right=False)
    
    @property
    def right_handle_auto(self):
        """ Right Auto Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='AUTO', left=False)
    
    @property
    def left_handle_free(self):
        """ Left Free Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='FREE', right=False)
    
    @property
    def right_handle_free(self):
        """ Right Free Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='FREE', left=False)
    
    @property
    def left_handle_vector(self):
        """ Left Vector Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='VECTOR', right=False)
    
    @property
    def right_handle_vector(self):
        """ Right Vector Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='VECTOR', left=False)
    
    @property
    def left_handle_align(self):
        """ Left Align Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='ALIGN', right=False)
    
    @property
    def right_handle_align(self):
        """ Right Align Handle selection
            
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`
        """
        return self.handles_selection(handle_type='ALIGN', left=False)
    
    @property
    def parameter(self):
        """ Spline parameter attribute
        
        Returns:
            Node SplineParameter
            
        Output sockets:
            - factor : Float
            - length : Float
            - index : Integer
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """        
        return self.attribute(nodes.SplineParameter())
    
    
    @property
    def parameter_factor(self):
        """ Parameter factor attribute
        
        Returns:
            Float: factor socket of parameter
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """
        return self.parameter.factor
        
    @property
    def parameter_length(self):
        """ Parameter length attribute
        
        Returns:
            Float: length socket of parameter
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """
        return self.parameter.length
        
    @property
    def parameter_index(self):
        """ Parameter factor attribute
        
        Returns:
            Integer: index socket of parameter
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """
        return self.parameter.index    
    
    # ====================================================================================================
    # Methods
    
    def delete(self):
        """ Delete points
        
        Node :class:`~geonodes.nodes.nodes.DeleteGeometry`
            
        Returns:
            self
        
        .. code-block:: python
            
            curve.points(...).delete()
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
    
# ----------------------------------------------------------------------------------------------------
# Spline

class Spline(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='CURVE', selection=selection)
        
    @property
    def radius(self):
        """ Radius attribute
        
        Returns:
            Float
            
        getter: :class:`~geonodes.nodes.nodes.Radius`
        setter: :class: `~geonodes.nodes.nodes.SetCurveRadius`
        """
        return self.attribute(nodes.Radius()).get_datasocket(0)
    
    @radius.setter
    def radius(self, value):
        self.stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=value))
        
    @property
    def tilt(self):
        """ Tilt attribute
        
        Returns:
            Float
            
        getter: :class:`~geonodes.nodes.nodes.CurveTilt`
        setter: :class: `~geonodes.nodes.nodes.SetCurveTilt`
        """
        return self.attribute(nodes.CurveTilt()).get_datasocket(0)
    
    @tilt.setter
    def tilt(self, value):
        self.stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=value))
    
    @property
    def cyclic(self):
        """ Cylic attribute
        
        Returns:
            Boolean
            
        getter: :class:`~geonodes.nodes.nodes.IsSplineCyclic`
        setter: :class: `~geonodes.nodes.nodes.SetSplineCyclic`
        """
        return self.attribute(nodes.IsSplineCyclic()).get_datasocket(0)
    
    @cyclic.setter
    def cyclic(self, value):
        self.stack(nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=value))
        
    @property
    def tangent(self):
        """ Tangent attribute
        
        Returns:
            Vector
            
        getter: :class:`~geonodes.nodes.nodes.CurveTangent`
        setter: read only
        """
        return self.attribute(nodes.CurveTangent()).get_datasocket(0)
    
    @property
    def spline_length(self):
        """ spline_length attribute
        
        Returns:
            node SplineLength
            
        Output sockets:
            - length : Float
            - point_count : Integer
            
        getter: :class:`~geonodes.nodes.nodes.SplineLength`
        setter: read only
        """
        return self.attribute(nodes.SplineLength())
    
    @property
    def length(self):
        """ Length attribute
        
        Returns:
            Float: length socket of spline_length
            
        getter: :class:`~geonodes.nodes.nodes.SplineLength`
        setter: read only
        """
        return self.spline_length.length
    
    
    @property
    def point_count(self):
        """ Point count attribute
        
        Returns:
            Integer: point_count socket of spline_length
            
        getter: :class:`~geonodes.nodes.nodes.SplineLength`
        setter: read only
        """
        return self.spline_length.point_count
    
    @property
    def parameter(self):
        """ Spline parameter attribute
        
        Returns:
            Node SplineParameter
            
        Output sockets:
            - factor : Float
            - length : Float
            - index : Integer
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """        
        return self.attribute(nodes.SplineParameter())
    
    
    @property
    def parameter_factor(self):
        """ Parameter factor attribute
        
        Returns:
            Float: factor socket of parameter
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """
        return self.parameter.factor
        
    @property
    def parameter_length(self):
        """ Parameter length attribute
        
        Returns:
            Float: length socket of parameter
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """
        return self.parameter.length
        
    @property
    def parameter_index(self):
        """ Parameter factor attribute
        
        Returns:
            Integer: index socket of parameter
            
        getter: :class:`~geonodes.nodes.nodes.SplineParameter`
        setter: read only
        """
        return self.parameter.index
    
    @property
    def resolution(self):
        """ Resolution attribute
        
        Returns:
            Integer
            
        getter: :class:`~geonodes.nodes.nodes.SplineResolution`
        setter: :class: `~geonodes.nodes.nodes.SetSplineResolution`
        """
        return self.attribute(nodes.SplineResolution()).get_datasocket(0)
    
    @resolution.setter
    def resolution(self, value):
        self.stack(nodes.SetSplineResolution(self.data_socket, selection=self.selection, resolution=value))
    
    def endpoint_selection(self, start_size=None, end_size=None):
        """ End point selection
        
        Args:
            - start_size : Integer
            - end_size : Integer
        
        Returns
        -------
            Float
            
        getter: :class:`~geonodes.nodes.nodes.EndpointSelection`
        """
        return self.attribute(nodes.EndpointSelection(start_size=start_size, end_size=end_size)).get_datasocket(0)
    
    @property
    def type(self):
        """ Parameter factor attribute
        
        Returns:
            Float: factor socket of parameter
            
        type in ('BEZIER', 'NURBS', 'POLY')
            
        getter: write only
        setter: :class:`~geonodes.nodes.nodes.SetSplineType`
        """
        
        raise Exception(f"'splines.type' property is write only")
    
    @type.setter
    def type(self, value):
        valids = ('BEZIER', 'NURBS', 'POLY')
        stype = value.upper()
        if not stype in valids:
            raise Exception(f"{value}' is not a valide splien type. Valide spline types are {valids}")
            
        return self.stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=stype))
    
    # ====================================================================================================
    # Methods
    
    def delete(self):
        """ Delete splines
        
        Node :class:`~geonodes.nodes.nodes.DeleteGeometry`
            
        Returns:
            self
        
        .. code-block:: python
            
            curve.splines(...).delete()
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
# =============================================================================================================================
# Cloud point : the point domain of cloud of points

class CloudPoint(Point):

    @property
    def radius(self):
        """ Radius attribute
        
        Returns:
            Float
            
        getter: :class:`~geonodes.nodes.nodes.Radius`
        setter: :class: `~geonodes.nodes.nodes.SetPointRadius`
        """
        return self.attribute(nodes.Radius()).get_datasocket(0)
    
    @radius.setter
    def radius(self, value):
        self.stack(nodes.SetPointRadius(self.data_socket, selection=self.selection, radius=value))
        
    # ====================================================================================================
    # Methods

    def delete(self):
        """ Delete points.
        
        Node :class:`~geonodes.nodes.nodes.DeleteGeometry`        
            
        Returns:
            self
        
        .. code-block:: python
            
            cloud.points(...).delete()
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
    def merge(self, distance=0.001):
        """ Merge points by distance.
        
        Node :class:`~geonodes.nodes.nodes.MergeByDistance`

        Args:
            distance : Float

        Returns:
            self

        .. code-block:: python
            
            cloud.points().merge()

        """
        return self.stack(nodes.MergeByDistance(self.data_socket, selection=self.selection, distance=distance))
    
    def to_vertices(self):
        """ Convert points to vertices.
        
        Node :class:`~geonodes.nodes.nodes.PointsToVertices`
        
        Returns:
            Points
        
        .. code-block:: python
            
            verts = cloud.points.to_vertices()
        """
        return nodes.PointsToVertices(points=self.data_socket, selection=self.selection)
        
    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ Convert points to volume.
        
        Node :class:`~geonodes.nodes.nodes.PointsToVolume`
        
        Args:
            density : Float
            voxel_size : Float
            voxel_amount : Float
            radius : Float
            resolution_mode (str): (default = 'VOXEL_AMOUNT') in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        
        Returns:
            Volume
        
        .. code-block:: python
            
            volume = cloud.points.to_volume()
        """
        return nodes.PointsToVolume(points=self.data_socket, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode='VOXEL_AMOUNT')
        
        
        
# =============================================================================================================================
# Instance domain

class Instance(Domain):
    
    def __init__(self, data_socket, selection=None):
        super().__init__(data_socket, domain='INSTANCE', selection=selection)
        
    # ====================================================================================================
    # Methods
    
    def delete(self):
        """ Delete instances.
        
        Node :class:`~geonodes.nodes.nodes.DeleteGeometry`
            
        Returns:
            self
        
        .. code-block:: python
            
            instances.insts(...).delete()
        """
        return self.stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain))
    
    def rotate(self, rotation=None, pivot_point=None, local_space=None):
        """ Rotate instances.
        
        Node :class:`~geonodes.nodes.nodes.RotateInstances`
        
        Args:
            rotation : Vector
            pivot_point : Vector
            local_space : Boolean
            
        Returns:
            self
        
        .. code-block:: python
            
            instances.insts(...).rotate(...)
        """
        return self.stack(nodes.RotateInstances(
            instances=self.data_socket, selection=self.selection,
            rotation=rotation, pivot_point=pivot_point, local_space=local_space))
    
    def scale(self, scale=None, center=None, local_space=None):
        """ Scale instances.
        
        Node :class:`~geonodes.nodes.nodes.ScaleInstances`
        
        Args:
            scale : Vector
            center : Vector
            local_space : Boolean
            
        Returns:
            self
        
        .. code-block:: python
            
            instances.insts(...).scale(...)
        """
        return self.stack(nodes.ScaleInstances(
            instances=self.data_socket, selection=self.selection,
            scale=scale, center=center, local_space=local_space))
    
    def translate(self, translation=None, local_space=None):
        """ > Translate instances.
        
        Node :class:`~geonodes.nodes.nodes.TranslateInstances`
        
        Args:
            - translation : Vector
            - local_space : Boolean
            
        Returns:
            self
        
        .. code-block:: python
            
            instances.insts(...).translate(...)
        """
        return self.stack(nodes.TranslateInstances(
            instances=self.data_socket, selection=self.selection,
            translation=translation, local_space=local_space))
    
    
