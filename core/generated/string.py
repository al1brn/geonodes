from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class String(Socket):

    def equal(self, b=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_STR': self, 'B_STR': b}, data_type='STRING', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_STR': self, 'B_STR': b}, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def hash_value(self, seed=None):
        """ > Method <&Node Hash Value>

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
        node = Node('Hash Value', sockets={'Value': self, 'Seed': seed}, data_type='STRING')
        return node._out

    @classmethod
    @property
    def special_characters(cls):
        """ > Property Get <&Node Special Characters>

        Returns
        -------
        - node [line_break (String), tab (String)]
        """
        node = Node('Special Characters', sockets={})
        return node

    @classmethod
    @property
    def line_break(cls):
        """ > Property Get <&Node Special Characters>

        Returns
        -------
        - String [tab_ (String)]
        """
        node = Node('Special Characters', sockets={})
        return node._out

    @classmethod
    @property
    def tab(cls):
        """ > Property Get <&Node Special Characters>

        Returns
        -------
        - tab
        """
        node = Node('Special Characters', sockets={})
        return node.tab

    def replace(self, find=None, replace=None):
        """ > Method <&Node Replace String>

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
        node = Node('Replace String', sockets={'String': self, 'Find': find, 'Replace': replace})
        return node._out

    def slice(self, position=None, length=None):
        """ > Method <&Node Slice String>

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
        node = Node('Slice String', sockets={'String': self, 'Position': position, 'Length': length})
        return node._out

    @property
    def length(self):
        """ > Property Get <&Node String Length>

        Information
        -----------
        - Socket 'String' : self

        Returns
        -------
        - Integer
        """
        node = Node('String Length', sockets={'String': self})
        return node._out

    def join(self, *strings):
        """ > Method <&Node Join Strings>

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
        node = Node('Join Strings', sockets={'Delimiter': self, 'Strings': list(strings)})
        return node._out

    @classmethod
    def Join(cls, *strings, delimiter=None):
        """ > Constructor <&Node Join Strings>

        Arguments
        ---------
        - delimiter (String) : socket 'Delimiter' (id: Delimiter)
        - strings (String) : socket 'Strings' (id: Strings)

        Returns
        -------
        - String
        """
        node = Node('Join Strings', sockets={'Delimiter': delimiter, 'Strings': list(strings)})
        return cls(node._out)

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """ > Method <&Node String to Curves>

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
        - align_x (str): parameter 'align_x' in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
        - align_y (str): parameter 'align_y' in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
        - overflow (str): parameter 'overflow' in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
        - pivot_mode (str): parameter 'pivot_mode' in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')

        Returns
        -------
        - Instances [line_ (Integer), pivot_point_ (Vector)]
        """
        node = Node('String to Curves', sockets={'String': self, 'Size': size, 'Character Spacing': character_spacing, 'Word Spacing': word_spacing, 'Line Spacing': line_spacing, 'Text Box Width': text_box_width}, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
        return node._out

