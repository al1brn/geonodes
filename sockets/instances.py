import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Instances

class Instances(gn.Geometry):
    """ 

    Data socket Instances
    ---------------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Attributes
        ----------
            - instance_index : Integer = capture_index(domain='INSTANCE')
    

        Methods
        -------
            - rotate : instances (Instances)
            - scale : instances (Instances)
            - to_points : points (Points)
            - translate : instances (Instances)
    """


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def instance_index(self):
        """ > Node: Index
          
        <sub>go to: top index
        blender ref GeometryNodeInputIndex
        node ref Index </sub>
        
        ```python
        v = instances.instance_index(self)
        ```
    

        Arguments
        ---------
    

            Parameters
            ----------
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

        return self.capture_index(domain='INSTANCE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """ > Node: RotateInstances
          
        <sub>go to: top index
        blender ref GeometryNodeRotateInstances
        node ref Rotate Instances </sub>
        
        ```python
        v = instances.rotate(selection, rotation, pivot_point, local_space)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - instances : Instances (self)
                    - selection : Boolean
                    - rotation : Vector
                    - pivot_point : Vector
                    - local_space : Boolean
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space)
            ```
    

        Returns
        -------
            Instances
            
        """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        """ > Node: ScaleInstances
          
        <sub>go to: top index
        blender ref GeometryNodeScaleInstances
        node ref Scale Instances </sub>
        
        ```python
        v = instances.scale(selection, scale, center, local_space)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - instances : Instances (self)
                    - selection : Boolean
                    - scale : Vector
                    - center : Vector
                    - local_space : Boolean
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space)
            ```
    

        Returns
        -------
            Instances
            
        """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(self, selection=None, translation=None, local_space=None):
        """ > Node: TranslateInstances
          
        <sub>go to: top index
        blender ref GeometryNodeTranslateInstances
        node ref Translate Instances </sub>
        
        ```python
        v = instances.translate(selection, translation, local_space)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - instances : Instances (self)
                    - selection : Boolean
                    - translation : Vector
                    - local_space : Boolean
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space)
            ```
    

        Returns
        -------
            Instances
            
        """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))

    def to_points(self, selection=None, position=None, radius=None):
        """ > Node: InstancesToPoints
          
        <sub>go to: top index
        blender ref GeometryNodeInstancesToPoints
        node ref Instances to Points </sub>
        
        ```python
        v = instances.to_points(selection, position, radius)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - instances : Instances (self)
                    - selection : Boolean
                    - position : Vector
                    - radius : Float
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius)
            ```
    

        Returns
        -------
            Points
            
        """

        return nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius).points


