from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Collection(Socket):

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """ > Method <&Node Collection Info>

        Information
        -----------
        - Socket 'Collection' : self

        Arguments
        ---------
        - separate_children (Boolean) : socket 'Separate Children' (id: Separate Children)
        - reset_children (Boolean) : socket 'Reset Children' (id: Reset Children)
        - transform_space (str): parameter 'transform_space' in ('ORIGINAL', 'RELATIVE')

        Returns
        -------
        - Instances
        """
        node = self._cache('Collection Info', sockets={'Collection': self, 'Separate Children': separate_children, 'Reset Children': reset_children}, transform_space=transform_space)
        return node._out

