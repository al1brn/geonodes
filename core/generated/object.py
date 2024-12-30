from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Object(Socket):

    @classmethod
    @property
    def ActiveCamera(cls):
        """ > Constructor <&Node Active Camera>

        Returns
        -------
        - Object
        """
        node = Node('Active Camera', sockets={})
        return cls(node._out)

    @property
    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """ > Property Get <&Node Object Info>

        Information
        -----------
        - Socket 'Object' : self

        Arguments
        ---------
        - as_instance (Boolean) : socket 'As Instance' (id: As Instance)
        - transform_space (str): parameter 'transform_space' in ('ORIGINAL', 'RELATIVE')

        Returns
        -------
        - node [transform (Matrix), location (Vector), rotation (Rotation), scale (Vector), geometry (Geometry)]
        """
        node = Node('Object Info', sockets={'Object': self, 'As Instance': as_instance}, transform_space=transform_space)
        return node

    @classmethod
    @property
    def Self(cls):
        """ > Constructor <&Node Self Object>

        Returns
        -------
        - Object
        """
        node = Node('Self Object', sockets={})
        return cls(node._out)

