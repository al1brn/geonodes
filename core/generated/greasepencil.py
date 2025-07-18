from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class GreasePencil(Socket):
    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'component' : 'GREASEPENCIL'

        Returns
        -------
        - node [layer_count (Integer)]
        """
        node = self._cache('Domain Size', sockets={'Geometry': self}, component='GREASEPENCIL')
        return node

    def to_curves(self, layers_as_instances=None):
        """ > Node <&Node Grease Pencil to Curves>

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - layers_as_instances (Boolean) : socket 'Layers as Instances' (id: Layers as Instances)

        Returns
        -------
        - Curve
        """
        node = Node('Grease Pencil to Curves', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Layers as Instances': layers_as_instances})
        return node._out

    @classmethod
    def named_layer_selection(cls, name=None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Layer Selection', sockets={'Name': name})
        return node._out

    def merge_layers_by_name(self):
        """ > Node <&Node Merge Layers>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'MERGE_BY_NAME'

        Returns
        -------
        - GreasePencil
        """
        node = Node('Merge Layers', sockets={'Grease Pencil': self, 'Selection': self._sel}, mode='MERGE_BY_NAME')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_layers_by_id(self, group_id=None):
        """ > Node <&Node Merge Layers>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'MERGE_BY_ID'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Merge Layers', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Group ID': group_id}, mode='MERGE_BY_ID')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_layers(self, mode='MERGE_BY_NAME'):
        """ > Node <&Node Merge Layers>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['MERGE_BY_NAME', 'MERGE_BY_ID']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Merge Layers', 'mode', mode, 'merge_layers', ('MERGE_BY_NAME', 'MERGE_BY_ID'))
        node = Node('Merge Layers', sockets={'Grease Pencil': self, 'Selection': self._sel}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_grease_pencil_color_stroke(self, color=None, opacity=None):
        """ > Node <&Node Set Grease Pencil Color>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'STROKE'

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - opacity (Float) : socket 'Opacity' (id: Opacity)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Set Grease Pencil Color', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Color': color, 'Opacity': opacity}, mode='STROKE')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_grease_pencil_color_fill(self, color=None, opacity=None):
        """ > Node <&Node Set Grease Pencil Color>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'FILL'

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - opacity (Float) : socket 'Opacity' (id: Opacity)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Set Grease Pencil Color', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Color': color, 'Opacity': opacity}, mode='FILL')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_grease_pencil_color(self, color=None, opacity=None, mode='STROKE'):
        """ > Node <&Node Set Grease Pencil Color>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - opacity (Float) : socket 'Opacity' (id: Opacity)
        - mode (str): parameter 'mode' in ['STROKE', 'FILL']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Color', 'mode', mode, 'set_grease_pencil_color', ('STROKE', 'FILL'))
        node = Node('Set Grease Pencil Color', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Color': color, 'Opacity': opacity}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_grease_pencil_depth(self, depth_order='2D'):
        """ > Node <&Node Set Grease Pencil Depth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self

        Arguments
        ---------
        - depth_order (str): parameter 'depth_order' in ['2D', '3D']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Depth', 'depth_order', depth_order, 'set_grease_pencil_depth', ('2D', '3D'))
        node = Node('Set Grease Pencil Depth', sockets={'Grease Pencil': self}, depth_order=depth_order)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_grease_pencil_softness(self, softness=None):
        """ > Node <&Node Set Grease Pencil Softness>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - softness (Float) : socket 'Softness' (id: Softness)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Set Grease Pencil Softness', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Softness': softness})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def stroke_color(self):
        """ Write only property for node <Node Set Grease Pencil Color>
        """
        raise NodeError('Property GreasePencil.stroke_color is write only.')

    @stroke_color.setter
    def stroke_color(self, color=None):
        """ > Node <&Node Set Grease Pencil Color>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Opacity' : ignored
        - Parameter 'mode' : 'STROKE'

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Set Grease Pencil Color', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Color': color, 'Opacity': None}, mode='STROKE')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def fill_color(self):
        """ Write only property for node <Node Set Grease Pencil Color>
        """
        raise NodeError('Property GreasePencil.fill_color is write only.')

    @fill_color.setter
    def fill_color(self, color=None):
        """ > Node <&Node Set Grease Pencil Color>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Opacity' : ignored
        - Parameter 'mode' : 'FILL'

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Set Grease Pencil Color', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Color': color, 'Opacity': None}, mode='FILL')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def depth(self):
        """ Write only property for node <Node Set Grease Pencil Depth>
        """
        raise NodeError('Property GreasePencil.depth is write only.')

    @depth.setter
    def depth(self, depth_order='2D'):
        """ > Node <&Node Set Grease Pencil Depth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self

        Arguments
        ---------
        - depth_order (str): parameter 'depth_order' in ['2D', '3D']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Depth', 'depth_order', depth_order, 'depth', ('2D', '3D'))
        node = Node('Set Grease Pencil Depth', sockets={'Grease Pencil': self}, depth_order=depth_order)
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def softness(self):
        """ Write only property for node <Node Set Grease Pencil Softness>
        """
        raise NodeError('Property GreasePencil.softness is write only.')

    @softness.setter
    def softness(self, softness=None):
        """ > Node <&Node Set Grease Pencil Softness>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - softness (Float) : socket 'Softness' (id: Softness)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Set Grease Pencil Softness', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Softness': softness})
        self._jump(node._out)
        return self._domain_to_geometry

