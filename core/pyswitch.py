"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : pyswitch
-----------------

Mimic if else elif python syntax

updates
-------
- creation : 2025/01/15
"""

# DEPRECATED DEPRECATED DEPRECATED DEPRECATED DEPRECATED DEPRECATED DEPRECATED DEPRECATED DEPRECATED 

from . import utils
from . scripterror import NodeError

# ====================================================================================================
# Root class
# ====================================================================================================

class IfElse:
    """ Root class for If, Else and Elif

    Manages context With.
    Create a Layout with property layout_name  
    """

    def __init__(self, *, data_type=None, is_default=False, title=""):
        self._if            = None
        self._current_index = 0
        self.title          = title
        if data_type is not None:
            self.socket_class = utils.get_socket_class(data_type)
        self.is_default = is_default

    def from_socket(self, socket, title=None):
        
        if socket is None or socket._if is None:
            raise NodeError("Else() requires a socket created with If()", keyword="Else")

        self._if = socket._if
        self.node = self._if.node
        self.title = self._if.title if title is None else title

    def __enter__(self):
        from geonodes import Layout

        if self.TYPE == If.TYPE:
            if self.current_index == 0:
                name = f"If (true)"
            else:
                name = f"If (false)"

        elif self.TYPE == IndexSwitch.TYPE:
            name = f"Switch index ({self.current_index})"

        else:
            name = f"Menu Switch ({self.name})"

        if self.title != "":
            name = self.title + f" [{name}]"

        self.layout = Layout(name)
        self.layout.push()

        return self.get_socket()

    def __exit__(self, type, exc_value, traceback):
        self.layout.pop()
        pass

    def __str__(self):
        return f"<'{self.switch_type}' initialized with 'if_({self.current})'>"

    # ====================================================================================================
    # Property
    # ====================================================================================================

    @property
    def current_index(self):
        if self._if is None:
            return self._current_index
        else:
            return self._if.current_index

    @current_index.setter
    def current_index(self, value):
        if self._if is None:
            self._current_index = value
        else:
            self._if.current_index = value

    def get_socket(self):
        if self._if is None:
            return self.socket
        else:
            return self._if.socket
        
    @property
    def linked_selector_socket(self):
        node = getattr(self, 'node', None)
        if node is None:
            return None
                
        if not node._bnode.inputs[0].is_linked:
            return None
        
        return node._bnode.inputs[0].links[0].from_socket
        
    @property
    def is_linked(self):
        return self.linked_selector_socket is not None


# ====================================================================================================
# Switch
# ====================================================================================================

class If(IfElse):

    TYPE = "If"

    def __init__(self, data_type, condition=False, title=""):
        """ Initialize Switch syntax mimicing

        Arguments
        ---------
        - data_type (str) : socket class
        - title (str = "") title
        """

        from geonodes import Node

        super().__init__(data_type=data_type, title=title)

        self.socket  = self.socket_class.Switch(condition)
        self.node    = self.socket.node

        self.socket._if = self

    # ====================================================================================================
    # Set option
    # ====================================================================================================

    def set_option(self, value):
        """ Implements socket.option property

        Arguments
        ---------
        - value (Socket) : socket to plug in the current option
        - defaut
        """

        from .treeclass import Tree
        
        if self.current_index == 0:
            self.node.false = value

        elif self.current_index == 1:
            self.node.true = value

        else:
            raise NodeError("Only one Else() is possible after a If()", keyword=".option", current_index=self.current_index)

# ====================================================================================================
# Index Switch
# ====================================================================================================

class IndexSwitch(IfElse):

    TYPE = "IndexSwitch"

    def __init__(self, data_type, index=None, *, title=""):
        """ Initialize IndexSwitch syntax mimicing

        Arguments
        ---------
        - data_type (str) : socket class
        - index (Integer=0) : index socket
        - title (str = "") title
        """

        from geonodes import Node

        super().__init__(data_type=data_type, is_default=True, title=title)

        self.switch_type = 'INDEX SWITCH'

        self.socket  = self.socket_class.IndexSwitch(index=index)
        self.node    = self.socket.node
        self.enum_items = self.node._bnode.index_switch_items
        self.enum_items.clear()

        self.socket._if = self

    # ====================================================================================================
    # Set option
    # ====================================================================================================

    def set_option(self, value):
        """ Implements socket.option property

        Arguments
        ---------
        - value (Socket) : socket to plug in the current option
        """

        from .treeclass import Tree
        from . import blender

        # ---------------------------------------------------------------------------
        # Create and plug the socket
        # ---------------------------------------------------------------------------

        self.enum_items.new()
        self.node[1 + self.current_index] = value

        # ---------------------------------------------------------------------------
        # Default value
        # ---------------------------------------------------------------------------

        if self.is_default:

            # Input index default value
            self.node._bnode.inputs[0].default_value = self.current_index

            # Socket linked to the node index
            sock = self.linked_selector_socket

            # Propagate if exists
            if sock is not None:

                socket = utils.get_socket_class(sock.type)(sock)
                socket.default_value = self.current_index

                # Change the modifiers
                ident = sock.identifier
                for mod in blender.get_geonodes_modifiers(Tree.current_tree()._btree):
                    if mod.get(ident, None) is not None:
                        mod[ident] = self.current_index        


# ====================================================================================================
# Menu Switch
# ====================================================================================================

class MenuSwitch(IfElse):

    TYPE = "MenuSwitch"

    def __init__(self, data_type, menu=None, *, name="A", title=""):
        """ Initialize IndexSwitch syntax mimicing

        Arguments
        ---------
        - data_type (str) : socket class
        - index (Integer=0) : index socket
        - title (str = "") title
        """

        from geonodes import Node

        super().__init__(data_type=data_type, is_default=True, title=title)

        self.switch_type = 'MENU SWITCH'

        self.socket     = self.socket_class.MenuSwitch(menu=menu)
        self.node       = self.socket.node
        self.enum_items = self.node._bnode.enum_items
        self.enum_items.clear()

        self.name = name

        # ---------------------------------------------------------------------------
        # Store in the current socket
        # ---------------------------------------------------------------------------

        self.socket._if = self

    # ====================================================================================================
    # Set option
    # ====================================================================================================

    def set_option(self, value):
        """ Implements socket.option property

        Arguments
        ---------
        - value (Socket) : socket to plug in the current option
        """

        from .treeclass import Tree
        from . import blender

        # ---------------------------------------------------------------------------
        # Build an unique name
        # ---------------------------------------------------------------------------

        names = [sock.name for sock in self.node._bnode.inputs if sock.type != 'CUSTOM']
        base = self.name
        for i in range(100):
            if i == 0:
                name = base
            else:
                name = f"{base} {i}"
            if name not in names:
                break

        # ---------------------------------------------------------------------------
        # Create and plug the socket
        # ---------------------------------------------------------------------------

        self.node._set_items('enum_items', {name: value}, clear=False)

        # ---------------------------------------------------------------------------
        # Default value
        # ---------------------------------------------------------------------------

        if self.is_default:

            # Menu socket default value
            self.node._bnode.inputs[0].default_value = name

            # Socket linked to the node index
            sock = self.linked_selector_socket

            if sock is not None:

                socket = utils.get_socket_class(sock.type)(sock)
                socket.default_value = name

                # Modifiers value has been reset to None
                ident = sock.identifier
                for mod in blender.get_geonodes_modifiers(Tree.current_tree()._btree):
                    if mod.get(ident):
                        mod[ident] = self.current_index + 2


# ====================================================================================================
# Else class
# ====================================================================================================

class Else(IfElse):

    TYPE = If.TYPE

    def __init__(self, socket, *, title=None):
        """ Block "else" in the if ... else ... mimicing

        See <!If>

        Raises
        ------
        - NodeError : if socket is not initialized with a <!If>

        Arguments
        ---------
        - value (Socket) : socket initialized with a <!If>
        - title (str = None) : Else title
        """

        super().__init__()
        self.from_socket(socket, title=title)

        if self._if.TYPE != If.TYPE:
            raise NodeError(f"Else() can be only used with If(), not {self._if.TYPE}(). Use Elif() rather than Else()")

        self.current_index += 1


# ====================================================================================================
# Elif class
# ====================================================================================================

class Elif(IfElse):
    def __init__(self, socket, *, name="B", default=False, title=None):
        """ Block "elif" in the if ... elif ... mimicing

        See <!If>

        This class adds an option to "Index Switch" or "Menu Switch" node.

        Raises
        ------
        - NodeError : if socket is not initialized with a <!If>

        Arguments
        ---------
        - socket (Socket) : socket initialized with a <!If>
        - name (str = "B") : 
        - menu (str = None) : the name of the option for "Menu Switch" (ignored in "Index Switch")
        - tip (str = "") : Layout label
        """

        super().__init__()
        self.from_socket(socket, title=title)

        if self._if.TYPE == If.TYPE:
            raise NodeError(f"Elif() cannot be be used with If(). Use Else() rather than Elif()")

        self.current_index += 1
        self._if.name       = name
        self.name           = name
        self._if.is_default = default

        self.TYPE = self._if.TYPE
        
