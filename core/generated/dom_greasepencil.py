# Generated 2026-01-21 11:40:29

from __future__ import annotations
from .. sockettype import SocketType
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class GreasePencil:
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
        - Integer
        """
        node = self._cache('Domain Size', {'Geometry': self}, component='GREASEPENCIL')
        return node._out

    def to_curves(self, layers_as_instances: Boolean = None):
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
        node = Node('Grease Pencil to Curves', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Layers as Instances': layers_as_instances})
        return node._out

    @classmethod
    def named_layer_selection(cls, name: String = None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Layer Selection', {'Name': name})
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
        node = Node('Merge Layers', {'Grease Pencil': self, 'Selection': self.get_selection()}, mode='MERGE_BY_NAME')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_layers_by_id(self, group_id: Integer = None):
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
        node = Node('Merge Layers', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Group ID': group_id}, mode='MERGE_BY_ID')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_layers(self, mode: Literal['MERGE_BY_NAME', 'MERGE_BY_ID'] = 'MERGE_BY_NAME'):
        """ > Node <&Node Merge Layers>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (str): parameter 'mode' in ('By Name', 'By Group ID')

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Merge Layers', 'mode', mode, 'merge_layers', ('MERGE_BY_NAME', 'MERGE_BY_ID'))
        node = Node('Merge Layers', {'Grease Pencil': self, 'Selection': self.get_selection()}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_color_stroke(self, color: Color = None, opacity: Float = None):
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
        node = Node('Set Grease Pencil Color', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Color': color, 'Opacity': opacity}, mode='STROKE')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_color_fill(self, color: Color = None, opacity: Float = None):
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
        node = Node('Set Grease Pencil Color', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Color': color, 'Opacity': opacity}, mode='FILL')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_color(self,
                    color: Color = None,
                    opacity: Float = None,
                    mode: Literal['STROKE', 'FILL'] = 'STROKE'):
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
        - mode (str): parameter 'mode' in ('Stroke', 'Fill')

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Color', 'mode', mode, 'set_color', ('STROKE', 'FILL'))
        node = Node('Set Grease Pencil Color', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Color': color, 'Opacity': opacity}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_depth(self, depth_order: Literal['2D', '3D'] = '2D'):
        """ > Node <&Node Set Grease Pencil Depth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self

        Arguments
        ---------
        - depth_order (str): parameter 'depth_order' in ('2D Layers', '3D Location')

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Depth', 'depth_order', depth_order, 'set_depth', ('2D', '3D'))
        node = Node('Set Grease Pencil Depth', {'Grease Pencil': self}, depth_order=depth_order)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_softness(self, softness: Float = None):
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
        node = Node('Set Grease Pencil Softness', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Softness': softness})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def stroke_color(self):
        """ Write only property for node <Node Set Grease Pencil Color>
        """
        raise NodeError('Property GreasePencil.stroke_color is write only.')

    @stroke_color.setter
    def stroke_color(self, color: Color = None):
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
        node = Node('Set Grease Pencil Color', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Color': color, 'Opacity': None}, mode='STROKE')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def fill_color(self):
        """ Write only property for node <Node Set Grease Pencil Color>
        """
        raise NodeError('Property GreasePencil.fill_color is write only.')

    @fill_color.setter
    def fill_color(self, color: Color = None):
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
        node = Node('Set Grease Pencil Color', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Color': color, 'Opacity': None}, mode='FILL')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def depth(self):
        """ Write only property for node <Node Set Grease Pencil Depth>
        """
        raise NodeError('Property GreasePencil.depth is write only.')

    @depth.setter
    def depth(self, depth_order: Literal['2D', '3D'] = '2D'):
        """ > Node <&Node Set Grease Pencil Depth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self

        Arguments
        ---------
        - depth_order (str): parameter 'depth_order' in ('2D Layers', '3D Location')

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Depth', 'depth_order', depth_order, 'depth', ('2D', '3D'))
        node = Node('Set Grease Pencil Depth', {'Grease Pencil': self}, depth_order=depth_order)
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def softness(self):
        """ Write only property for node <Node Set Grease Pencil Softness>
        """
        raise NodeError('Property GreasePencil.softness is write only.')

    @softness.setter
    def softness(self, softness: Float = None):
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
        node = Node('Set Grease Pencil Softness', {'Grease Pencil': self, 'Selection': self.get_selection(), 'Softness': softness})
        self._jump(node._out)
        return self._domain_to_geometry

