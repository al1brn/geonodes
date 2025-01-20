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

from . import utils
from . scripterror import NodeError

# =============================================================================================================================
# Root class

class IfElse:
    """ Root class for If, Else and Elif
    """
    def __enter__(self):
        from geonodes import Layout
        self.layout = Layout(self.layout_name)
        return self.socket

    def __exit__(self, type, exc_value, traceback):
        self.layout.pop()
        pass

    def __str__(self):
        return f"<'{self.node_name}' initialized with 'if_({self.current})'>"


# =============================================================================================================================
# If class

class If(IfElse):
    def __init__(self, socket_class, selector, name="Menu", tip=""):
        """ Initialize If syntax mimicing

        This class, together with <!Else> and <!Elif> classes, propose and alternative
        to the naive implementation of nodes "Switch", "Index Switch", "Menu Switch".

        Each class of the syntax mimicing set creats a syntaxic block into which one
        can create the optional socket.

        For instance, rather than writing:

        ``` python
        condition = Boolean(True, "Cone")

        geo = Geometry.Switch(condition, false=Mesh.Cube(), true=Mesh.Cone)
        geo.out()
        ```

        You can mimic if ... else ... syntax with:

        ``` python
        condition = Boolean(True, "Cone")

        with If(Geometry, condition) as geo:
            geo.option = Mesh.Cone()

        with Else(geo):
            geo.option = Mesh.Cube()

        geo.out()
        ```

        ### Comments

        The first argument of ***If*** is the class you want. The second argument is a <!Boolean>.

        > [!NOTE]
        > The second argument can also be an Integer or a String to create a "Index Switch"
        > or a "Menu Switch".

        It returns the output socket of the "Switch" Node.
        Note than the input sockets of node are not yet linked.
        The link is performed by setting the property `geo.option`.

        > [IMPORTANT]
        > `option` property depends upon the context. In the ***If** block, it is
        > the "True" input socket, in the ***Else*** block, it is the "False" input socket.

        ``` python
        with If(Geometry, condition) as geo:
            geo.option = Mesh.Cone()
            # is equivalent to
            geo.node.true = Mesh.Cone()

        with Else(geo):
            geo.option = Mesh.Cube()
            # is equivalent to
            geo.node.false = Mesh.Cube()
        ```

        The ***Else** is initialized with a socket previously created with a **If**.

        ### Index Switch

        "Index Switch" can be created by initializing ***If** with an <!Integer> value rather
        than a <!Boolean>.

        The following code create a "Index Switch" node with 4 entries.

        ``` python
        index = Integer(0, "Geometry Index")

        with If(Geometry, index) as geo:
            geo.option = Mesh.Cube()

        with Elif(geo):
            geo.option = Mesh.UVSphere()

        with Elif(geo):
            geo.option = Mesh.IcoSphere()

        with Elif(geo):
            geo.option = Mesh.Cone()

        geo.out()
        ```

        ### Menu Switch

        A "Menu Switch" works similarily by initializing the ***If*** with a ***python string**.

        > [!IMPORTANT]
        > The 'selector' argument is a a python string, not a <!String>. It is interpreted as the name
        > of the first menu option.

        Each ***Elif*** coming after takes a str "menu" argument as the name of the current entry.


        ``` python
        with If(Geometry, "Cube", name="Pick Shape") as geo:
            # "Cube" is the name of the first option in the menu
            geo.option = Mesh.Cube()

        with Elif(geo, "Sphere"):
            " "Sphere" is the name of the second option in the menu
            geo.option = Mesh.UVSphere()

        with Elif(geo):
            # "C" will be the name of the third option in the menu
            geo.option = Mesh.IcoSphere()

        with Elif(geo, "Cone):
            geo.option = Mesh.Cone()

        geo.out()
        ```

        > [!NOTE]
        > Each block is put in a layout frame.

        Raises
        ------
        - NodeError if `selector` argument is not an <!Boolean>, a <!Integer> or a str

        Arguments
        ---------
        - socket_class (type) : a class valid as input of the switch node
        - selector (Boolean, Integer or str) : Boolean and Integer: socket used to select the option,
          str: name of the first option in the menu
        - name (str = "Menu") : name of menu socket
        - tip (str = "") : user tip (used in menu creation and in Layout names)
        """

        from geonodes import Node

        self.socket_class = socket_class
        self.selector     = selector
        self.sel_type     = utils.get_socket_type(selector)
        self.current      = 0
        self.name         = name
        self.tip          = tip

        if self.sel_type == 'BOOLEAN':
            self.node_name = "Switch"

            self.socket  = self.socket_class.Switch(self.selector)
            self.node    = self.socket.node

            self.layout_name = f"If - {tip}"

        elif self.sel_type == 'INT':
            self.node_name = "Index Switch"

            self.socket  = self.socket_class.IndexSwitch(index=self.selector)
            self.node    = self.socket.node
            self.enum_items = self.node._bnode.index_switch_items
            self.enum_items.clear()

            self.layout_name = f"Index Switch (0) - {tip}"

        elif isinstance(selector, str):
            self.node_name = "Menu Switch"

            self.node    = Node("Menu Switch", {}, data_type=socket_class.SOCKET_TYPE)
            self.node._items.clear()

            self.socket  = self.node._out
            self.current_name = selector

            self.layout_name = f"Menu Switch ({selector}) - {tip}"

        else:
            raise NodeError(f"If() requires a Boolean, Integer or a python str, not {selector}.", keyword="If")

        self.socket._if = self

    # ----------------------------------------------------------------------------------------------------
    # Set option

    def set_option(self, socket):
        """ Implements socket.option property

        Arguments
        ---------
        - socket (Socket) : socket to plug in the current option
        """

        from geonodes import Tree

        if self.node_name == "Switch":

            if self.current == 0:
                self.node.true = socket

            elif self.current == 1:
                self.node.false = socket

            else:
                raise NodeError("Only one Else() is possible after a If()", keyword=".option")

        elif self.node_name == "Index Switch":

            self.enum_items.new()
            self.node[1 + self.current] = socket

        elif self.node_name == "Menu Switch":

            if self.current_name is None:
                name = 'ABCDEFEGHIJKLMNOPQRSTUVWXYZ'[self.current]
            else:
                name = self.current_name

            self.node._set_items({name: socket})

            menu_socket = Tree.new_input('NodeSocketMenu', name=self.name, value=None, description=self.tip)
            self.node["Menu"] = menu_socket

            if self.current == 0:
                menu_socket._bsocket.default_value = name
                menu_socket._interface_socket.default_value = name


# =============================================================================================================================
# Else class

class Else(IfElse):
    def __init__(self, socket):
        """ Block "else" in the if ... else ... mimicing

        See <!If>

        Raises
        ------
        - NodeError : if socket is not initialized with a <!If>

        Arguments
        ---------
        - socket (Socket) : socket initialized with a <!If>
        """
        if socket is None or socket._if is None:
            raise NodeError("Else() requires a socket created with If()", keyword="Else")

        self.socket = socket
        _if = socket._if
        self.tip = _if.tip

        if _if.node_name != "Switch":
            raise NodeError(f"If() has created a '{_if.node_name}' node, not a 'Switch' node. Use Elif() rather than Else()", keyword=".option")

        _if.current += 1

        self.layout_name = f"Else - {_if.tip}"

# =============================================================================================================================
# Elif class

class Elif(IfElse):
    def __init__(self, socket, menu=None, tip=""):
        """ Block "elif" in the if ... elif ... mimicing

        See <!If>

        This class adds an option to "Index Switch" or "Menu Switch" node.

        Raises
        ------
        - NodeError : if socket is not initialized with a <!If>

        Arguments
        ---------
        - socket (Socket) : socket initialized with a <!If>
        - menu (str = None) : the name of the option for "Menu Switch" (ignored in "Index Switch")
        - tip (str = "") : Layout label
        """
        if socket is None or socket._if is None:
            raise NodeError("Elif() requires a socket created with If()", keyword="Elif")

        self.socket = socket
        _if = socket._if
        self.tip = _if.tip

        _if.current += 1

        if _if.node_name == "Index Switch":
            self.layout_name = f"Index Switch ({_if.current}) - {tip}"

        elif _if.node_name == "Menu Switch":
            if menu is None:
                _if.current_name = None
            else:
                _if.current_name = str(menu)

            self.layout_name = f"Menu Switch ({_if.current_name}) - {tip}"

        elif _if.node_name == "Switch":
            raise NodeError(f"Use Else() rather than Elif() after a If() initialized with a Boolean.", keyword=".option")

        else:
            assert(False)
