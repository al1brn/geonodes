from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Image(Socket):

    @property
    def info(self, frame=None):
        """ > Property Get <&Node Image Info>

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

    @property
    def width(self, frame=None):
        """ > Property Get <&Node Image Info>

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

    @property
    def height(self, frame=None):
        """ > Property Get <&Node Image Info>

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

    @property
    def has_alpha(self, frame=None):
        """ > Property Get <&Node Image Info>

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

    @property
    def frame_count(self, frame=None):
        """ > Property Get <&Node Image Info>

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

    @property
    def fps(self, frame=None):
        """ > Property Get <&Node Image Info>

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

