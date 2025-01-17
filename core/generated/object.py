from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Object(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def ActiveCamera(cls):
        """ > Node <&Node Active Camera>

        Returns
        -------
        - Object
        """
        node = Node('Active Camera', sockets={})
        return cls(node._out)

    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """ > Node <&Node Object Info>

        Information
        -----------
        - Socket 'Object' : self

        Arguments
        ---------
        - as_instance (Boolean) : socket 'As Instance' (id: As Instance)
        - transform_space (str): parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']

        Returns
        -------
        - node [transform (Matrix), location (Vector), rotation (Rotation), scale (Vector), geometry (Geometry)]
        """
        utils.check_enum_arg('Object Info', 'transform_space', transform_space, 'info', ('ORIGINAL', 'RELATIVE'))
        node = Node('Object Info', sockets={'Object': self, 'As Instance': as_instance}, transform_space=transform_space)
        return node

    @classmethod
    def Self(cls):
        """ > Node <&Node Self Object>

        Returns
        -------
        - Object
        """
        node = Node('Self Object', sockets={})
        return cls(node._out)

