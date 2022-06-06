import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Instances

class Instances(gn.Geometry):
    """ Class Instances
    

    | Inherits from: gn.Geometry 
    Index 
    

    Attributes
    ==========
    - **instance_index** : Index Integer = capture_index(domain='INSTANCE') 
    

    Methods
    =======
    - **rotate**    : RotateInstances instances (Instances) 
    - **scale**     : ScaleInstances instances (Instances) 
    - **to_points** : InstancesToPoints points (Points) 
    - **translate** : TranslateInstances instances (Instances) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def instance_index(self):
        """ instance_index
        

        | Node: Index 
        Top Index 
        

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

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """ rotate
        

        | Node: RotateInstances 
        Top Index 
        

            v = instances.rotate(selection, rotation, pivot_point, local_space) 
        

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
                Instances 
        """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        """ scale
        

        | Node: ScaleInstances 
        Top Index 
        

            v = instances.scale(selection, scale, center, local_space) 
        

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
                Instances 
        """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(self, selection=None, translation=None, local_space=None):
        """ translate
        

        | Node: TranslateInstances 
        Top Index 
        

            v = instances.translate(selection, translation, local_space) 
        

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
                Instances 
        """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))

    def to_points(self, selection=None, position=None, radius=None):
        """ to_points
        

        | Node: InstancesToPoints 
        Top Index 
        

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


