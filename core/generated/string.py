# Generated 2025-12-04 08:23:30

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves, MenuNode, IndexSwitchNode
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


class String(Socket):
    """"
    $DOC SET hidden
    """
    def equal(self, b: String = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'STRING'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'EQUAL'

        Arguments
        ---------
        - b (String) : socket 'B' (id: B_STR)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_STR': self, 'B_STR': b}, data_type='STRING', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: String = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'STRING'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'NOT_EQUAL'

        Arguments
        ---------
        - b (String) : socket 'B' (id: B_STR)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_STR': self, 'B_STR': b}, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def find_in_string(self, search: String = None):
        """ > Node <&Node Find in String>

        Information
        -----------
        - Socket 'String' : self

        Arguments
        ---------
        - search (String) : socket 'Search' (id: Search)

        Returns
        -------
        - Integer [count_ (Integer)]
        """
        node = Node('Find in String', {'String': self, 'Search': search})
        return node._out

    def find(self, search: String = None):
        """ > Node <&Node Find in String>

        Information
        -----------
        - Socket 'String' : self

        Arguments
        ---------
        - search (String) : socket 'Search' (id: Search)

        Returns
        -------
        - Integer [count_ (Integer)]
        """
        node = Node('Find in String', {'String': self, 'Search': search})
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'STRING'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='STRING')
        return node._out

    @classmethod
    def special_characters(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        - node [line_break (String), tab (String)]
        """
        node = Node('Special Characters', )
        return node

    @classmethod
    @property
    def line_break(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        - String [tab_ (String)]
        """
        node = Node('Special Characters', )
        return node._out

    @classmethod
    @property
    def tab(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        - tab
        """
        node = Node('Special Characters', )
        return node.tab

    def replace(self, find: String = None, replace: String = None):
        """ > Node <&Node Replace String>

        Information
        -----------
        - Socket 'String' : self

        Arguments
        ---------
        - find (String) : socket 'Find' (id: Find)
        - replace (String) : socket 'Replace' (id: Replace)

        Returns
        -------
        - String
        """
        node = Node('Replace String', {'String': self, 'Find': find, 'Replace': replace})
        return node._out

    def slice(self, position: Integer = None, length: Integer = None):
        """ > Node <&Node Slice String>

        Information
        -----------
        - Socket 'String' : self

        Arguments
        ---------
        - position (Integer) : socket 'Position' (id: Position)
        - length (Integer) : socket 'Length' (id: Length)

        Returns
        -------
        - String
        """
        node = Node('Slice String', {'String': self, 'Position': position, 'Length': length})
        return node._out

    def length(self):
        """ > Node <&Node String Length>

        Information
        -----------
        - Socket 'String' : self

        Returns
        -------
        - Integer
        """
        node = Node('String Length', {'String': self})
        return node._out

    def format(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Format String>

        Information
        -----------
        - Socket 'Format' : self

        Returns
        -------
        - String
        """
        node = Node('Format String', {'Format': self, **named_sockets}, **sockets)
        return node._out

    @classmethod
    def Format(cls, named_sockets: dict = {}, format: String = None, **sockets):
        """ > Node <&Node Format String>

        Arguments
        ---------
        - format (String) : socket 'Format' (id: Format)

        Returns
        -------
        - String
        """
        node = Node('Format String', {'Format': format, **named_sockets}, **sockets)
        return cls(node._out)

    @classmethod
    def ImportText(cls, path: String = None):
        """ > Node <&Node Import Text>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - String
        """
        node = Node('Import Text', {'Path': path})
        return cls(node._out)

    def match_string(self,
                    operation: Literal['Starts With', 'Ends With', 'Contains'] = None,
                    key: String = None):
        """ > Node <&Node Match String>

        Information
        -----------
        - Socket 'String' : self

        Arguments
        ---------
        - operation (menu='Starts With') : ('Starts With', 'Ends With', 'Contains')
        - key (String) : socket 'Key' (id: Key)

        Returns
        -------
        - Boolean
        """
        node = Node('Match String', {'String': self, 'Operation': operation, 'Key': key})
        return node._out

    def join(self, *strings: String):
        """ > Node <&Node Join Strings>

        Information
        -----------
        - Socket 'Delimiter' : self

        Arguments
        ---------
        - strings (String) : socket 'Strings' (id: Strings)

        Returns
        -------
        - String
        """
        node = Node('Join Strings', {'Delimiter': self, 'Strings': list(strings)})
        return node._out

    @classmethod
    def Join(cls, *strings: String, delimiter: String = None):
        """ > Node <&Node Join Strings>

        Arguments
        ---------
        - delimiter (String) : socket 'Delimiter' (id: Delimiter)
        - strings (String) : socket 'Strings' (id: Strings)

        Returns
        -------
        - String
        """
        node = Node('Join Strings', {'Delimiter': delimiter, 'Strings': list(strings)})
        return cls(node._out)

    def to_curves(self,
                    size: Float = None,
                    character_spacing: Float = None,
                    word_spacing: Float = None,
                    line_spacing: Float = None,
                    text_box_width: Float = None,
                    align_x: Literal['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH'] = 'LEFT',
                    align_y: Literal['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM'] = 'TOP_BASELINE',
                    font = None,
                    overflow: Literal['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE'] = 'OVERFLOW',
                    pivot_mode: Literal['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT'] = 'BOTTOM_LEFT'):
        """ > Node <&Node String to Curves>

        Information
        -----------
        - Socket 'String' : self

        Arguments
        ---------
        - size (Float) : socket 'Size' (id: Size)
        - character_spacing (Float) : socket 'Character Spacing' (id: Character Spacing)
        - word_spacing (Float) : socket 'Word Spacing' (id: Word Spacing)
        - line_spacing (Float) : socket 'Line Spacing' (id: Line Spacing)
        - text_box_width (Float) : socket 'Text Box Width' (id: Text Box Width)
        - align_x (str): parameter 'align_x' in ['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH']
        - align_y (str): parameter 'align_y' in ['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM']
        - font (Blender VectorFont | str): VectorFont, or name of a valid font in bpy.types.fonts (see `utils.get_font`)
        - overflow (str): parameter 'overflow' in ['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE']
        - pivot_mode (str): parameter 'pivot_mode' in ['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT']

        Returns
        -------
        - Instances [line_ (Integer), pivot_point_ (Vector)]
        """
        utils.check_enum_arg('String to Curves', 'align_x', align_x, 'to_curves', ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH'))
        utils.check_enum_arg('String to Curves', 'align_y', align_y, 'to_curves', ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM'))
        utils.check_enum_arg('String to Curves', 'overflow', overflow, 'to_curves', ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE'))
        utils.check_enum_arg('String to Curves', 'pivot_mode', pivot_mode, 'to_curves', ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT'))
        node = Node('String to Curves', {'String': self, 'Size': size, 'Character Spacing': character_spacing, 'Word Spacing': word_spacing, 'Line Spacing': line_spacing, 'Text Box Width': text_box_width}, align_x=align_x, align_y=align_y, font=utils.get_font(font), overflow=overflow, pivot_mode=pivot_mode)
        return node._out

    def to_value(self, data_type: Literal['FLOAT', 'INT'] = 'FLOAT'):
        """ > Node <&Node String to Value>

        Information
        -----------
        - Socket 'String' : self

        Arguments
        ---------
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT']

        Returns
        -------
        - Float [length_ (Integer)]
        """
        node = Node('String to Value', {'String': self}, data_type=data_type)
        return node._out

    def to_float(self):
        """ > Node <&Node String to Value>

        Information
        -----------
        - Socket 'String' : self
        - Parameter 'data_type' : 'FLOAT'

        Returns
        -------
        - Float [length_ (Integer)]
        """
        node = Node('String to Value', {'String': self}, data_type='FLOAT')
        return node._out

    def to_integer(self):
        """ > Node <&Node String to Value>

        Information
        -----------
        - Socket 'String' : self
        - Parameter 'data_type' : 'INT'

        Returns
        -------
        - Integer [length_ (Integer)]
        """
        node = Node('String to Value', {'String': self}, data_type='INT')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'STRING'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - String
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='STRING')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = "",
        name: str = 'String',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: str = '',
        subtype: str = 'NONE',
         ):
        """ > String Input

        New <#String> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = "") : Default value
        - name  (str = 'String') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (str = '') : Property default_value
        - subtype (str = 'NONE') : Socket sub type in ('NONE', 'FILE_PATH')

        Returns
        -------
        - String
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketString', value=value, name=name, tip=tip,
            panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default=default, subtype=subtype)

    @classmethod
    def FilePath(cls,
        value: object = "",
        name: str = 'FilePath',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: str = '',
         ):
        """ > FilePath Input

        New <#String> input with subtype 'FILE_PATH'.

        Aguments
        --------
        - value  (object = "") : Default value
        - name  (str = 'FilePath') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (str = '') : Property default_value

        Returns
        -------
        - String
        """
        return cls(value=value, name=name, tip=tip, panel=panel, optional_label=optional_label,
            hide_value=hide_value, hide_in_modifier=hide_in_modifier, default=default, subtype='FILE_PATH')

