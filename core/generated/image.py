from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Image(Socket):
    """"
    $DOC SET hidden
    """
    def info(self, frame=None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - node [width (Integer), height (Integer), has_alpha (Boolean), frame_count (Integer), fps (Float)]
        """
        node = self._cache('Image Info', sockets={'Image': self, 'Frame': frame})
        return node

    def width(self, frame=None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - width
        """
        node = self._cache('Image Info', sockets={'Image': self, 'Frame': frame})
        return node.width

    def height(self, frame=None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - height
        """
        node = self._cache('Image Info', sockets={'Image': self, 'Frame': frame})
        return node.height

    def has_alpha(self, frame=None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - has_alpha
        """
        node = self._cache('Image Info', sockets={'Image': self, 'Frame': frame})
        return node.has_alpha

    def frame_count(self, frame=None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - frame_count
        """
        node = self._cache('Image Info', sockets={'Image': self, 'Frame': frame})
        return node.frame_count

    def fps(self, frame=None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - fps
        """
        node = self._cache('Image Info', sockets={'Image': self, 'Frame': frame})
        return node.fps

