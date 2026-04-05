# Generated 2026-04-05 13:37:20

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
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class String(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def equal(self, b: String = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | A           | `self`      |
        | Parameter | `data_type` | `'STRING'`  |
        | Parameter | `mode`      | `'ELEMENT'` |
        | Parameter | `operation` | `'EQUAL'`   |

        Parameters
        ----------
        b : String, optional
            socket 'B' (id: B_STR)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_STR': self, 'B_STR': b}, data_type='STRING', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: String = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Socket    | A           | `self`        |
        | Parameter | `data_type` | `'STRING'`    |
        | Parameter | `mode`      | `'ELEMENT'`   |
        | Parameter | `operation` | `'NOT_EQUAL'` |

        Parameters
        ----------
        b : String, optional
            socket 'B' (id: B_STR)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_STR': self, 'B_STR': b}, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def find_in_string(self, search: String = None):
        """ > Node <&Node Find in String>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Parameters
        ----------
        search : String, optional
            socket 'Search' (id: Search)
        

        Returns
        -------
        Integer
            peer sockets: count_ (Integer)

        """
        node = Node('Find in String', {'String': self, 'Search': search})
        return node._out

    def find(self, search: String = None):
        """ > Node <&Node Find in String>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Parameters
        ----------
        search : String, optional
            socket 'Search' (id: Search)
        

        Returns
        -------
        Integer
            peer sockets: count_ (Integer)

        """
        node = Node('Find in String', {'String': self, 'Search': search})
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'STRING'` |

        Parameters
        ----------
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='STRING')
        return node._out

    @utils.classproperty
    def special_characters(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        String
            peer sockets: tab_ (String)

        """
        node = Node('Special Characters', )
        return node._out

    @utils.classproperty
    def line_break(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        String
            peer sockets: tab_ (String)

        """
        node = Node('Special Characters', )
        return node._out

    @utils.classproperty
    def tab(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        tab
        """
        node = Node('Special Characters', )
        return node.tab

    def replace(self, find: String = None, replace: String = None):
        """ > Node <&Node Replace String>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Parameters
        ----------
        find : String, optional
            socket 'Find' (id: Find)
        
        replace : String, optional
            socket 'Replace' (id: Replace)
        

        Returns
        -------
        String
        """
        node = Node('Replace String', {'String': self, 'Find': find, 'Replace': replace})
        return node._out

    def slice(self, position: Integer = None, length: Integer = None):
        """ > Node <&Node Slice String>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Parameters
        ----------
        position : Integer, optional
            socket 'Position' (id: Position)
        
        length : Integer, optional
            socket 'Length' (id: Length)
        

        Returns
        -------
        String
        """
        node = Node('Slice String', {'String': self, 'Position': position, 'Length': length})
        return node._out

    def length(self):
        """ > Node <&Node String Length>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Returns
        -------
        Integer
        """
        node = Node('String Length', {'String': self})
        return node._out

    def format(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Format String>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Format | `self` |

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        String
        """
        node = Node('Format String', {'Format': self, **named_sockets}, **sockets)
        return node._out

    @classmethod
    def Format(cls, named_sockets: dict = {}, format: String = None, **sockets):
        """ > Node <&Node Format String>

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        format : String, optional
            socket 'Format' (id: Format)
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        String
        """
        node = Node('Format String', {'Format': format, **named_sockets}, **sockets)
        return cls(node._out)

    @classmethod
    def ImportText(cls, path: String = None):
        """ > Node <&Node Import Text>

        Parameters
        ----------
        path : String, optional
            socket 'Path' (id: Path)
        

        Returns
        -------
        String
        """
        node = Node('Import Text', {'Path': path})
        return cls(node._out)

    def match_string(self,
                    operation: Literal['Starts With', 'Ends With', 'Contains'] = None,
                    key: String = None):
        """ > Node <&Node Match String>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Parameters
        ----------
        operation : menu='Starts With', optional
            ('Starts With', 'Ends With', 'Contains')
        
        key : String, optional
            socket 'Key' (id: Key)
        

        Returns
        -------
        Boolean
        """
        node = Node('Match String', {'String': self, 'Operation': operation, 'Key': key})
        return node._out

    def join(self, *strings: String):
        """ > Node <&Node Join Strings>

        **Fixed values**

        | Kind   | Name      | Value  |
        | ------ | --------- | ------ |
        | Socket | Delimiter | `self` |

        Parameters
        ----------
        strings : String, optional
            socket 'Strings' (id: Strings)
        

        Returns
        -------
        String
        """
        node = Node('Join Strings', {'Delimiter': self, 'Strings': list(strings)})
        return node._out

    @classmethod
    def Join(cls, *strings: String, delimiter: String = None):
        """ > Node <&Node Join Strings>

        Parameters
        ----------
        delimiter : String, optional
            socket 'Delimiter' (id: Delimiter)
        
        strings : String, optional
            socket 'Strings' (id: Strings)
        

        Returns
        -------
        String
        """
        node = Node('Join Strings', {'Delimiter': delimiter, 'Strings': list(strings)})
        return cls(node._out)

    def to_curves(self,
                    size: Float = None,
                    font: Font = None,
                    align_x: Literal['Left', 'Center', 'Right', 'Justify', 'Flush'] = None,
                    align_y: Literal['Top', 'Top Baseline', 'Middle', 'Bottom Baseline', 'Bottom'] = None,
                    pivot_point: Literal['Midpoint', 'Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right'] = None,
                    character_spacing: Float = None,
                    word_spacing: Float = None,
                    line_spacing: Float = None,
                    overflow: Literal['Overflow', 'Scale To Fit', 'Truncate'] = None,
                    text_box_width: Float = None,
                    text_box_height: Float = None):
        """ > Node <&Node String to Curves>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Parameters
        ----------
        size : Float, optional
            socket 'Size' (id: Size)
        
        font : Font, optional
            socket 'Font' (id: Font)
        
        align_x : menu='Left', optional
            ('Left', 'Center', 'Right', 'Justify', 'Flush')
        
        align_y : menu='Top Baseline', optional
            ('Top', 'Top Baseline', 'Middle', 'Bottom Baseline', 'Bottom')
        
        pivot_point : menu='Midpoint', optional
            ('Midpoint', 'Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right')
        
        character_spacing : Float, optional
            socket 'Character Spacing' (id: Character Spacing)
        
        word_spacing : Float, optional
            socket 'Word Spacing' (id: Word Spacing)
        
        line_spacing : Float, optional
            socket 'Line Spacing' (id: Line Spacing)
        
        overflow : menu='Overflow', optional
            ('Overflow', 'Scale To Fit', 'Truncate')
        
        text_box_width : Float, optional
            socket 'Text Box Width' (id: Text Box Width)
        
        text_box_height : Float, optional
            socket 'Text Box Height' (id: Text Box Height)
        

        Returns
        -------
        Instances
            peer sockets: remainder_ (String), line_ (Integer), word_ (Integer), pivot_point_ (Vector)

        """
        node = Node('String to Curves', {'String': self, 'Size': size, 'Font': font, 'Align X': align_x, 'Align Y': align_y, 'Pivot Point': pivot_point, 'Character Spacing': character_spacing, 'Word Spacing': word_spacing, 'Line Spacing': line_spacing, 'Overflow': overflow, 'Text Box Width': text_box_width, 'Text Box Height': text_box_height})
        return node._out

    def to_value(self, data_type: Literal['FLOAT', 'INT'] = 'FLOAT'):
        """ > Node <&Node String to Value>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | String | `self` |

        Parameters
        ----------
        data_type : Literal['Float', 'Integer']
            parameter `data_type`
        

        Returns
        -------
        Float
            peer sockets: length_ (Integer)

        """
        node = Node('String to Value', {'String': self}, data_type=data_type)
        return node._out

    def to_float(self):
        """ > Node <&Node String to Value>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | String      | `self`    |
        | Parameter | `data_type` | `'FLOAT'` |

        Returns
        -------
        Float
            peer sockets: length_ (Integer)

        """
        node = Node('String to Value', {'String': self}, data_type='FLOAT')
        return node._out

    def to_integer(self):
        """ > Node <&Node String to Value>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | String      | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Returns
        -------
        Integer
            peer sockets: length_ (Integer)

        """
        node = Node('String to Value', {'String': self}, data_type='INT')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'STRING'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        String
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
        subtype: str = 'NONE',
         ):
        """ > String Input

        New <#String> input with subtype 'NONE'.

        Parameters
        ----------
        value : object, default=`""`
            Default value

        name : str, default=`String`
            Input socket name

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier

        subtype : str, default=`NONE`
            Socket sub type in ('NONE', 'FILE_PATH')


        Returns
        -------
        String
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketString', default_value = defval,
            name=name, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, subtype=subtype)

    @classmethod
    def FilePath(cls,
        value: object = "",
        name: str = 'FilePath',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > FilePath Input

        New <#String> input with subtype 'FILE_PATH'.

        Parameters
        ----------
        value : object, default=`""`
            Default value

        name : str, default=`FilePath`
            Input socket name

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier


        Returns
        -------
        String
        """
        return cls(value=value, name=name, tip=tip, panel=panel, optional_label=optional_label,
            hide_value=hide_value, hide_in_modifier=hide_in_modifier, subtype='FILE_PATH')

