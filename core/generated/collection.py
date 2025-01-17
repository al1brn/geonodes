from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Collection(Socket):
    """"
    $DOC SET hidden
    """
    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """ > Node <&Node Collection Info>

        Information
        -----------
        - Socket 'Collection' : self

        Arguments
        ---------
        - separate_children (Boolean) : socket 'Separate Children' (id: Separate Children)
        - reset_children (Boolean) : socket 'Reset Children' (id: Reset Children)
        - transform_space (str): parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']

        Returns
        -------
        - Instances
        """
        utils.check_enum_arg('Collection Info', 'transform_space', transform_space, 'info', ('ORIGINAL', 'RELATIVE'))
        node = self._cache('Collection Info', sockets={'Collection': self, 'Separate Children': separate_children, 'Reset Children': reset_children}, transform_space=transform_space)
        return node._out

