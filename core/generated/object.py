from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Object(Socket):
    """"
    $DOC SET hidden
    """
    def camera_info(self):
        """ > Node <&Node Camera Info>

        Information
        -----------
        - Socket 'Camera' : self

        Returns
        -------
        - node [projection_matrix (Matrix), focal_length (Float), sensor (Vector), shift (Vector), clip_start (Float), clip_end (Float), focus_distance (Float), is_orthographic (Boolean), orthographic_scale (Float)]
        """
        node = Node('Camera Info', sockets={'Camera': self})
        return node

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

