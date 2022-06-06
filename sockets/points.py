import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Points

class Points(gn.Geometry):
    """ Class Points
    

    | Inherits from: gn.Geometry 
    Index 
    

    Methods
    =======
    - **instance_on_points** : InstanceOnPoints instances (Instances) 
    - **set_radius**         : SetPointRadius points (Points) 
    - **to_vertices**        : PointsToVertices mesh (Mesh) 
    - **to_volume**          : PointsToVolume volume (Volume) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_radius(self, selection=None, radius=None):
        """ set_radius
        

        | Node: SetPointRadius 
        Top Index 
        

            v = points.set_radius(selection, radius) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - points    : Points (self) 
            - selection : Boolean 
            - radius    : Float 
        

        Node creation
        =============
        

            node = nodes.SetPointRadius(points=self, selection=selection, radius=radius) 
        

        Returns
        =======
                Points 
        """

        return self.stack(nodes.SetPointRadius(points=self, selection=selection, radius=radius))

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ instance_on_points
        

        | Node: InstanceOnPoints 
        Top Index 
        

            v = points.instance_on_points(selection, instance, pick_instance, instance_index, rotation, scale) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - points         : Points (self) 
            - selection      : Boolean 
            - instance       : Geometry 
            - pick_instance  : Boolean 
            - instance_index : Integer 
            - rotation       : Vector 
            - scale          : Vector 
        

        Node creation
        =============
        

            node = nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance,
            instance_index=instance_index, rotation=rotation, scale=scale) 
        

        Returns
        =======
                Instances 
        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances

    def to_vertices(self, selection=None):
        """ to_vertices
        

        | Node: PointsToVertices 
        Top Index 
        

            v = points.to_vertices(selection) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - points    : Points (self) 
            - selection : Boolean 
        

        Node creation
        =============
        

            node = nodes.PointsToVertices(points=self, selection=selection) 
        

        Returns
        =======
                Mesh 
        """

        return nodes.PointsToVertices(points=self, selection=selection).mesh

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ to_volume
        

        | Node: PointsToVolume 
        Top Index 
        

            v = points.to_volume(density, voxel_size, voxel_amount, radius, resolution_mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - points       : Points (self) 
            - density      : Float 
            - voxel_size   : Float 
            - voxel_amount : Float 
            - radius       : Float 
        

            Parameters arguments
            --------------------
            - resolution_mode : 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE] 
        

        Node creation
        =============
        

            node = nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount,
            radius=radius, resolution_mode=resolution_mode) 
        

        Returns
        =======
                Volume 
        """

        return nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume


