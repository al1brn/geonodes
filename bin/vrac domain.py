#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:47:34 2022

@author: alain
"""

    # ---------------------------------------------------------------------------
    # Input menu
        
    @property
    def ID_OLD(self):
        """ <field GeometryNodeInputID>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputID').ID
        
    @property
    def index_OLD(self):
        """ <field GeometryNodeInputIndex>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputIndex').index

    @property
    def normal_OLD(self):
        """ <field GeometryNodeInputNormal>
        
        Property
        
        Returns
        -------
            Vector
        """
        return self.create_field_node('GeometryNodeInputNormal').normal
    
    @property
    def position_OLD(self):
        """ <field GeometryNodeInputPosition>
        
        Property
        
        Returns
        -------
            Vector
        """
        return self.create_field_node('GeometryNodeInputPosition').position
    
    @property
    def radius_OLD(self):
        """ <field GeometryNodeInputRadius>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputRadius').radius
    
    def named_attribute_OLD(self, name=None, data_type='FLOAT'):
        """ <field GeometryNodeInputNamedAttribute>
        
        This method is called by the following methods:
            
        - [named_float](#named_float)
        - [named_integer](#named_integer)
        - [named_vector](#named_vector)
        - [named_color](#named_color)
        - [named_boolean](#named_boolean)
        
        Returns
        -------
            Linked to data_type
        """
        return self.create_field_node('GeometryNodeInputNamedAttribute', name=name).attribute
    
    
    def named_float(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT'
                               
        Returns
        -------
            Float
        """
        return self.named_attribute(name, data_type='FLOAT')
    
    def named_integer(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'INT'
        """
        return self.named_attribute(name, data_type='INT')
    
    def named_vector(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT_VECTOR'
                               
        Returns
        -------
            Vector
        """
        return self.named_attribute(name, data_type='FLOAT_VECTOR')
    
    def named_color(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT_COLOR'
                               
        Returns
        -------
            Color
        """
        return self.named_attribute(name, data_type='FLOAT_COLOR')
    
    def named_boolean(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'BOOLEAN'
                               
        Returns
        -------
            Boolean
        """
        return self.named_attribute(name, data_type='BOOLEAN')
        
    def create_field_node(self, bl_idname, **kwargs):
        """ > Create a **geonodes** from a bl_idname
        
        If kwargs is an empty dict, the node is put in cache in the _fields_ dict,
        otherwise it is returned directly.
        
        Attributes
        ----------
            - bl_idname : str
                A valid node bl_idname
            - kwargs : dict
                Arguments to pass to initialize the node
                
        Returns
        -------
            Node, the created node
        """
        
        cache = len(kwargs) == 0
        
        node = self.fields.get(bl_idname) if cache else None

        if node is None:
            node = create_node(bl_idname, **kwargs)
            node.as_attribute(self.bsocket, domain=self.domain)
            if cache:
                self.fields[bl_idname] = node
        return node
    

    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property

        Individual sockets can be accessed via properties:
            
        - [neighbors_vertices](#neighbors_vertices)
        - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
            - vertex_count
            - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshVertexNeighbors')
    
    @property
    def neighbors_vertices(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property
        
        Return the socket **vertex_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property
        
        Return the socket **face_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.face_count    
    
    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property

        Individual sockets can be accessed via properties:
            
        - [neighbors_vertices](#neighbors_vertices)
        - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
                - vertex_count
                - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshFaceNeighbors')
    
    @property
    def neighbors_vertices(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property
        
        Return the socket **vertex_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property
        
        Return the socket **face_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.face_count
    
    @property
    def is_shade_smooth(self):
        """ <field GeometryNodeInputShadeSmooth>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputShadeSmooth').smooth
    
    
    @property
    def island(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property

        Individual sockets can be accessed via properties:
            
        - [neighbors_vertices](#neighbors_vertices)
        - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
                - vertex_count
                - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property
        
        Return the socket **vertex_count** of property [island](#island)
        
        Returns
        -------
            Integer
        """
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property
        
        Return the socket **face_count** of property [island](#island)
        
        Returns
        -------
            Integer
        """
        return self.island.face_count    
    
    
    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ <field GeometryNodeCurveHandleTypeSelection>
        
        Method
        
        The values of the two parameters are declined in 2 methods:
        - [left_handle_selection](#left_handle_selection)
        - [right_handle_selection](#right_handle_selection)
                                       
        and 8 properties:
        - [left_handle_free](#left_handle_free)
        - [left_handle_vector](#left_handle_vector)
        - [left_handle_vector](#left_handle_vector)
        - [left_handle_align](#left_handle_align)
        - [right_handle_free](#right_handle_free)
        - [right_handle_auto](#right_handle_auto)
        - [right_handle_vector](#right_handle_vector)
        - [right_handle_align](#right_handle_align)
        
        Arguments
        ---------
            - handle_type : str in 'AUTO', 'FREE', 'VECTOR', 'ALIGN'
            - mode : str in ['RIGHT', 'LEFT'] or set {'RIGHT', 'LEFT'}
        
        Returns
        -------
            Boolean
        """
        return self.create_field_node('GeometryNodeCurveHandleTypeSelection', handle_type=handle_type, mode=mode).node_
      
    
    
    