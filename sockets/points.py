import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Points

class Points(gn.Geometry):
    """ 

    Data socket Points
    ------------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - instance_on_points : instances (Instances)
            - set_radius : points (Points)
            - to_vertices : mesh (Mesh)
            - to_volume : volume (Volume)
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_radius(self, selection=None, radius=None):
        """ > Node: SetPointRadius
          
        <sub>go to: top index
        blender ref GeometryNodeSetPointRadius
        node ref Set Point Radius </sub>
                                  
                ```python
                v = points.set_radius(selection, radius)
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - points : Points (self)
                    - selection : Boolean
                    - radius : Float
                      
                        Node creation
                        -------------
                                
                                ```python
                                from geondes import nodes
                                nodes.SetPointRadius(points=self, selection=selection, radius=radius)
                                ```
    

        Returns
        -------
            Points
            
        """

        return self.stack(nodes.SetPointRadius(points=self, selection=selection, radius=radius))

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Node: InstanceOnPoints
          
        <sub>go to: top index
        blender ref GeometryNodeInstanceOnPoints
        node ref Instance on Points </sub>
                                  
                ```python
                v = points.instance_on_points(selection, instance, pick_instance, instance_index, rotation, scale)
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - points : Points (self)
                    - selection : Boolean
                    - instance : Geometry
                    - pick_instance : Boolean
                    - instance_index : Integer
                    - rotation : Vector
                    - scale : Vector
                      
                        Node creation
                        -------------
                                
                                ```python
                                from geondes import nodes
                                nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale)
                                ```
    

        Returns
        -------
            Instances
            
        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances

    def to_vertices(self, selection=None):
        """ > Node: PointsToVertices
          
        <sub>go to: top index
        blender ref GeometryNodePointsToVertices
        node ref Points to Vertices </sub>
                                  
                ```python
                v = points.to_vertices(selection)
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - points : Points (self)
                    - selection : Boolean
                      
                        Node creation
                        -------------
                                
                                ```python
                                from geondes import nodes
                                nodes.PointsToVertices(points=self, selection=selection)
                                ```
    

        Returns
        -------
            Mesh
            
        """

        return nodes.PointsToVertices(points=self, selection=selection).mesh

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node: PointsToVolume
          
        <sub>go to: top index
        blender ref GeometryNodePointsToVolume
        node ref Points to Volume </sub>
                                  
                ```python
                v = points.to_volume(density, voxel_size, voxel_amount, radius, resolution_mode)
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - points : Points (self)
                    - density : Float
                    - voxel_size : Float
                    - voxel_amount : Float
                    - radius : Float## Parameters
                    - resolution_mode : 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
                      
                        Node creation
                        -------------
                                
                                ```python
                                from geondes import nodes
                                nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode)
                                ```
    

        Returns
        -------
            Volume
            
        """

        return nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume


