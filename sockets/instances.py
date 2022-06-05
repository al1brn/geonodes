import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Instances

class Instances(Geometry):
    """ Class Instances
    

    | Inherits from: Geometry 
    

    Attributes
    ==========
    - instance_index : Integer = capture_index(domain='INSTANCE') 
    

    Methods
    =======
    - to_points : points (Points) 
    

    Stacked methods
    ===============
    - rotate    : Instances 
    - scale     : Instances 
    - translate : Instances 
    """


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def instance_index(self):
        """ instance_index
        

        | Node: Index 
        

            v = instances.instance_index(self) 
        

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

        return self.capture_index(domain='INSTANCE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_points(self, selection=None, position=None, radius=None):
        """ to_points
        

        | Node: InstancesToPoints 
        

            v = instances.to_points(selection, position, radius) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - instances : Instances (self) 
            - selection : Boolean 
            - position  : Vector 
            - radius    : Float 
        

        Node creation
        =============
        

            node = nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius)
        

        Returns
        =======
                Points 
        """

        return nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius).points


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """ rotate
        

        | Node: RotateInstances 
        

            instances.rotate(selection, rotation, pivot_point, local_space) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - instances   : Instances (self) 
            - selection   : Boolean 
            - rotation    : Vector 
            - pivot_point : Vector 
            - local_space : Boolean 
        

        Node creation
        =============
        

            node = nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point,
            local_space=local_space) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        """ scale
        

        | Node: ScaleInstances 
        

            instances.scale(selection, scale, center, local_space) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - instances   : Instances (self) 
            - selection   : Boolean 
            - scale       : Vector 
            - center      : Vector 
            - local_space : Boolean 
        

        Node creation
        =============
        

            node = nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space)
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(self, selection=None, translation=None, local_space=None):
        """ translate
        

        | Node: TranslateInstances 
        

            instances.translate(selection, translation, local_space) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - instances   : Instances (self) 
            - selection   : Boolean 
            - translation : Vector 
            - local_space : Boolean 
        

        Node creation
        =============
        

            node = nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space)
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))


