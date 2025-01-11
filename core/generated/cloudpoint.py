from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class CloudPoint(Socket):
    """"
    $DOC SET hidden
    """

    @property
    def radius(self):
        """ Property get node <Node Set Point Radius>
        """
        return Node('Radius', sockets={})._out

    @radius.setter
    def radius(self, radius=None):
        """ > Jump Method <&Node Set Point Radius>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Set Point Radius', sockets={'Points': self, 'Selection': self._sel, 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

