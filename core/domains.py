"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : dom_point
----------------------
- Implement domain Point

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
- update : 2024/12/30
"""

import bpy

from .scripterror import NodeError
from . import constants
from . import utils
from .treeclass import Node
from .geometry_class import GeoBase, Geometry
from .domain_class import Domain
from . import generated

# ====================================================================================================
# Point Domain

class Point(Domain, generated.Point):

    DOMAIN_NAME = 'POINT'

    @property
    def count(self):
        """ > Socket 'Point Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.point_count

class Vertex(Point):
    pass

class SplinePoint(Point):
    pass

class CloudPoint(Point):
    pass

# ====================================================================================================
# Face Domain

class Face(Domain, generated.Face):
    """ > Face domain of a <!Mesh>
    """

    DOMAIN_NAME = 'FACE'

    @property
    def count(self):
        """ > Socket 'Face Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.face_count

# ====================================================================================================
# Edge Domain

class Edge(Domain, generated.Edge):
    """ > Edge domain of a <!Mesh>
    """

    DOMAIN_NAME = 'EDGE'

    @property
    def count(self):
        """ > Socket 'Edge Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.edge_count

    # ----- To face groups

    @property
    def to_face_groups(self):
        """ > Node <&Node Edges to Face Groups>

        Returns
        -------
        - Integer
        """
        return Node('Edges to Face Groups', {'Boundary Edges': self._sel})._out

# ====================================================================================================
# Corner Domain

class Corner(Domain, generated.Corner):
    """ > Corner domain of a <!Mesh>
    """

    DOMAIN_NAME = 'CORNER'

    @property
    def count(self):
        """ > Socket 'Corner Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.face_corner_count

# ====================================================================================================
# Spline Domain

class Spline(Domain, generated.Spline):
    """ > Curve, or Spline, domain of a <!Curve>

    Methods of **Spline** class are nodes which accept a SPLINE or CURVE domain.

    In addition, the node <*Node Points of Curve> is implemented as method <#points>.
    """

    DOMAIN_NAME = 'CURVE'

    @property
    def count(self):
        """ > Socket 'Spline Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.spline_count

# ====================================================================================================
# Layer Domain

class Layer(Domain, generated.Layer):
    """ > Layer domain of <!GreasePencil>

    """

    DOMAIN_NAME = 'LAYER'

    @property
    def count(self):
        """ > Socket 'Instance Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.layer_count

# ====================================================================================================
# Instance Domain

class Instance(Domain, generated.Instance):
    """ > Instance domain of <!Instances>

    > [!NOTE]
    > The geometry has only one domain sharing the same name:
    > - <!Instances> : name of geometry class
    > - **Instance** : name of domain class
    > - <!Instances#insts> : name of the domain property of class <!Instances>
    """

    DOMAIN_NAME = 'INSTANCE'

    @property
    def count(self):
        """ > Socket 'Instance Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.instance_count

    # ====================================================================================================
    # Properties

    # ----- Scale

    @property
    def scale(self):
        """ > Scale property

        - getter : <&Node Instance Scale>
        - setter : <&Node Scale Instances>

        Scale can be set either by a <!Vector> argument or by a dict with keys
        in ('Scale', 'Center', 'Local Space')

        ``` python
        instances = Instances()
        instances.insts.scale = (1, 2, 3)
        instances.insts.scale = {'Scale': (1, 2, 3), 'Center': (10, 11, 12), 'Local Space': True}
        ```

        Returns
        -------
        - Vector
        """
        return Node('Instance Scale')._out

    @scale.setter
    def scale(self, value):
        keys = ['Scale', 'Center', 'Local Space']
        sockets = {'Instances': self._geo, 'Selection': self._sel}
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in keys is None:
                    raise NodeError(f"Node 'Scale Instances' error: invalid key '{k}' to set instance scale.", valid_keys=keys)
                sockets[k] = v
        else:
            sockets['Scale'] = value

        return self._jump(Node('Scale Instances', sockets)._out)

    # ----- Rotation

    @property
    def rotation(self):
        """ > Rotation property

       - getter : <&Node Instance Rotation>
       - setter : <&Node Rotate Instances>

        Rotation can be set either by a <!Rotation> argument or by a dict with keys
        in ('Rotation', 'Pivot Point', 'Local Space')

        ``` python
        instances = Instances()
        instances.insts.rotation = (1, 2, 3)
        instances.insts.rotation = {'Rotation': (1, 2, 3), 'Pivot Point': (10, 11, 12), 'Local Space': True}
        ```

        Returns
        -------
        - Rotation
        """
        return Node('Instance Rotation')._out

    @rotation.setter
    def rotation(self, value):
        keys = ['Rotation', 'Pivot Point', 'Local Space']
        sockets = {'Instances': self._geo, 'Selection': self._sel}
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in keys:
                    raise NodeError(f"Node 'Rotate Instances' error: invalid key '{k}' to set instance rotation.", valid_keys=keys)
                sockets[k] = v
        else:
            sockets['Rotation'] = value

        return self._jump(Node('Rotate Instances', sockets)._out)
