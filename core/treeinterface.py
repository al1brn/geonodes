""" This module implements the TreeInterface class to
manage Tree input and output sockets creation and ordering.
"""

import bpy
from . import utils

import numpy as np

from . scripterror import NodeError

DELETION = '__deletion marker__'

# =============================================================================================================================
# Tree Interface

class TreeInterface:

    def __init__(self, btree):
        """ Acces to tree interface

        This class allows to create and manage panels and socket interface

        Arguments
        ---------
        - btree : Blender Tree
        """
        self.btree  = btree

    def __str__(self):
        in_count = len([item for item in self.btree.interface.items_tree if item.item_type == 'SOCKET' and item.in_out == 'INPUT'])
        out_count = len([item for item in self.btree.interface.items_tree if item.item_type == 'SOCKET' and item.in_out == 'OUTPUT'])
        panel_count = len([item for item in self.btree.interface.items_tree if item.item_type == 'PANEL'])
        return f"<TreeInterface of '{self.btree.name}': {panel_count} panel(s), {in_count} input socket(s), {out_count} output socket(s)>"

    def __repr__(self):
        s = f"{str(self)}\n- "

        names = self.get_unique_names('INPUT', False)
        s += "\n- ".join(names)

        #s += "\n\nArguments:\n- "
        #names = self.get_unique_names('INPUT', True)
        #s += "\n- ".join(names)
        return s + "\n"

    # ====================================================================================================
    # Clearing

    def clear(self, all=True):
        """ Clear all sockets
        """
        if all:
            self.btree.interface.clear()
        else:
            to_delete = []
            for item in self.btree.interface.items_tree:
                if item.description == DELETION:
                    to_delete.append(item)
            for item in to_delete:
                self.btree.interface.remove(item)

    def set_tip_delete(self):
        """ Mark all sockets to be deleted
        """
        for item in self.btree.interface.items_tree:
            item.description = DELETION

    # ====================================================================================================
    # Utilities

    def move_socket_to(self, socket, index):
        """ NodeTreeInterface move and move_to_parent are apparently bugged
        """

        parent = socket.parent
        panel = parent.name
        sockets = self.get_items('SOCKET', socket.in_out, panel=panel)

        cur_index = sockets.index(socket)
        if cur_index == index:
            return socket

        del sockets[cur_index]
        sockets.insert(index, socket)

        for sock in reversed(sockets):
            if parent is None:
                self.btree.interface.move(sock, 0)
            else:
                self.btree.interface.move_to_parent(sock, parent, 0)

        return socket

    @staticmethod
    def socket_in_list_OLD(socket, names):
        if names is None:
            return False

        elif isinstance(names, str):
            names = [names]

        return (socket.name in names) or (socket.identifier in names) or (utils.snake_case(socket.name) in names)

    # ====================================================================================================
    # Unique names

    def get_unique_names(self, in_out, as_argument=True, include_homonyms='MERGE'):
        """ Get the unique names of the sockets

        Sockets and panels can share the same names. To avoid homonyms, the names are suffixed
        by an index when necessary.
        Sockets can be prefixed by the name of their panel.

        Panel prefix is not mandatory if there is no homonym at top level.

        Imagine we have the following structure:
        - Integer : integer (or _integer)
        - Float : float (or _float)
        - Integer : integer_1 (or _integer_1)
        - Panel : panel
          - String : string (the only socket named String, panel_string is also valid)
          - Integer : panel_integer
          - Float : panel_float
          - Boolean : panel_boolean (because Boolean exists in another panel)
        - Panel : panel_1
          - Integer : panel_1_integer
          - Integer : panel_1_integer_1
          - Boolean : panel_1_boolean

        > [!NOTE]
        > geonodes doesn't create panels sharing the same name. But a Group can be created where
        > it is the case.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - as_argument (bool = True) : return snake_case rather than keeping caps
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ----------------------------------------------------------------------------------------------------
        # snake_case or not

        def snake_case(name):
            if as_argument:
                return utils.snake_case(name)
            else:
                return name

        sepa = '_' if as_argument else ' > '

        # ----------------------------------------------------------------------------------------------------
        # Let's start by naming the panels

        names  = [""]
        panels = [None]
        for item in self.btree.interface.items_tree:

            if item.item_type != 'PANEL':
                continue

            names.append(snake_case(item.name))
            panels.append(item)

        panel_names = {k: v for k, v in zip(utils.ensure_uniques(names, single_digit=True), panels)}

        # ----------------------------------------------------------------------------------------------------
        # List of the sockets in each panel

        panels = {}
        for panel_name, panel in panel_names.items():

            socket_names = []
            sockets      = []
            for item in self.btree.interface.items_tree:
                if item.item_type != 'SOCKET' or item.in_out != in_out:
                    continue
                if (panel_name == "" and item.parent.name != ""):
                    continue
                if panel_name != "" and item.parent != panel:
                    continue

                socket_names.append(snake_case(item.name))
                sockets.append(item)

            panels[panel_name] = {'raw_sc': socket_names, 'uniques': utils.ensure_uniques(socket_names, single_digit=True), 'sockets': sockets}

        # ----------------------------------------------------------------------------------------------------
        # Final dictionary with two entries per socket
        # - The short version without panel prefix (when possible)
        # - The long version with panel prefix

        names = {}
        homonyms = {}
        for panel_name, dicts in panels.items():
            for raw_sc, unique, socket in zip(dicts['raw_sc'], dicts['uniques'], dicts['sockets']):

                if panel_name == "":
                    names[unique] = socket
                    if as_argument:
                        homonyms[snake_case(sepa + unique)] = socket

                else:
                    # Short version ?
                    single = True
                    for p_name, p_dicts in panels.items():
                        if p_name == panel_name:
                            continue
                        if unique in p_dicts['uniques']:
                            single = False
                            break

                    if single:
                        names[unique] = socket
                        homonyms[snake_case(panel_name + sepa + unique)] = socket
                    else:
                        names[snake_case(panel_name + sepa + unique)] = socket

        if include_homonyms == 'MERGE':
            return {**names, **homonyms}
        elif include_homonyms == 'NO':
            return names
        elif include_homonyms == 'SEPARATE':
            return names, homonyms
        else:
            raise TypeError(f"include_homonyms must be in ('MERGE', 'NO', 'SEPARATE')")

    # ====================================================================================================
    # Get individual items

    # ----------------------------------------------------------------------------------------------------
    # Get a panel by its name

    def get_panel(self, name: str, halt: bool = True):
        """ Get a panel by its name

        Arguments
        ---------
        - name : panel name, can be true name or the snake case version
        - halt : raise an exception if not found

        Raises
        ------
        - AttributeError : if panel not found

        Returns
        -------
        - panel
        """
        if name == "" or name is None:
            return None

        panels = []
        for item in self.btree.interface.items_tree:
            if item.item_type == 'PANEL':
                if item.name == name:
                    return item
                panels.append(item.name)

        if halt:
            raise AttributeError(f"Panel '{name}' not found in {panels}")

        return None

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its identifier

    def by_identifier(self, identifier):
        for item in self.btree.interface.items_tree:
            if item.item_type == 'SOCKET' and item.identifier == identifier:
                return item

        raise NodeError(f"TreeInterface socket with identifier '{identifier}' not found in tree '{self.btree.name}'.")

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its socket name

    def by_name(self, in_out, name, as_argument=True, halt=True):

        assert(in_out in ('INPUT', 'OUTPUT'))

        if as_argument:
            socket_name = name
        else:
            parts = name.split('>')
            if len(parts) == 2:
                socket_name = parts[0].strip() + ' > ' + parts[1].strip()
            else:
                socket_name = name

        names = self.get_unique_names(in_out=in_out, as_argument=as_argument)
        socket = names.get(socket_name, None)

        if socket is None and halt:
            raise NodeError(f"{in_out} socket '{name}' not found in '{self.btree.name}'.", valids=list(names.keys()))

        return socket

    # ====================================================================================================
    # Get or create a socket

    def get_create_socket(self, in_out, name, socket_type, panel=""):
        """ Get a socket or create it if if doesn't exist

        Returns
        - couple socket, created : Socket and True if created
        """
        assert(in_out in ('INPUT', 'OUTPUT'))

        if panel is None:
            panel = ""

        # ----------------------------------------------------------------------------------------------------
        # Ensure the panel exists

        parent = self.create_panel(panel)
        if parent is not None:
            parent.description = ""

        # ----------------------------------------------------------------------------------------------------
        # Search the name in the list of sockets

        insertion_index = 0
        socket_index = None
        socket = None

        index = 0
        for item in self.btree.interface.items_tree:
            if item.item_type == 'PANEL' or item.in_out != in_out:
                continue
            if item.parent.name != panel:
                continue

            # ----- Found
            if item.name == name and item.socket_type == socket_type:
                socket_index = index
                socket = item
                if insertion_index is None:
                    insertion_index = socket_index
                break

            # ---- First unused entry
            if item.description != DELETION:
                insertion_index += 1

        # ----------------------------------------------------------------------------------------------------
        # Not found : we create it

        if socket is None:
            socket = self.btree.interface.new_socket(name, in_out=in_out, socket_type=socket_type, parent=parent)
            created = True
        else:
            # Suppress the deletion marker
            socket.description = ""
            created = False

        # ----------------------------------------------------------------------------------------------------
        # Let's locate the socket at the right position

        self.move_socket_to(socket, insertion_index)

        # ----------------------------------------------------------------------------------------------------
        # Done

        return socket, created

    # ====================================================================================================
    # Get list of items

    # ----------------------------------------------------------------------------------------------------
    # Get items of a certain category

    def get_items(self, item_type, in_out, panel = None):
        """ Get items matching the criteria passed in arguments

        Arguments
        ---------
        - item_type (str in ('PANELS', 'SOCKET')) : item type
        - in_out (str in ('INPUT', 'OUTPUT') : Input or output for sockets
        - panel (panel name) : the panel the items belong to

        Returns
        -------
        - list : list of items
        """
        items = []
        for item in self.btree.interface.items_tree:

            if item.item_type != item_type:
                continue

            if item_type == 'SOCKET':
                if item.in_out != in_out:
                    continue

                if panel is not None:
                    if isinstance(panel, str):
                        if item.parent.name != panel:
                            continue
                    elif item.parent != panel:
                        continue

            items.append(item)

        return items

    # ----------------------------------------------------------------------------------------------------
    # Get the output interface sockets

    def get_out_sockets_OLD(self):
        """ Get the output interface sockets

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfaceItem with in_out = 'OUTPUT'
        """
        return self._get_items('SOCKET', 'OUTPUT')

    # ----------------------------------------------------------------------------------------------------
    # Get the panels

    def get_panels_OLD(self):
        """ Get the panels

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfacePanel
        """
        return self._get_items('PANEL')

    # ----------------------------------------------------------------------------------------------------
    # Get the input interface sockets

    def get_in_sockets_OLD(self, panel_name: str | None=None):
        """ Get the output interface sockets

        Argument 'panel_name' is the name of the panel the required sockets belong to.
        If None, all the sockets are returned
        If equal to empty str "", it returns the sockets wich are directly parenty to the tree interface

        Arguments
        ---------
        - panel_name  : the name of the panel the sockets belong to

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfaceItem with in_out = 'INPUT'
        """
        panel = None
        if panel_name is None:
            pass

        elif panel_name == "":
            panel = ""

        else:
            panels = self.get_panels()
            panel = panels.get(panel_name)
            if panel is None:
                for p in panels.values():
                    if p.name == panel_name:
                        panel = p
                        break
                if panel is None:
                    return {}
                    raise Exception(f"Panel '{panel_name}' not found in {list(panels.keys())}")

        return self._get_items('SOCKET', 'INPUT', panel=panel)

    # ----------------------------------------------------------------------------------------------------
    # Get the possible input socket name

    def get_in_socket_names_OLD(self):

        socket_names = {}
        for index, (key, socket) in enumerate(self.get_in_sockets().items()):
            socket_names[socket.identifier] = [key, socket.identifier, socket.name, utils.snake_case(socket.name), socket.parent.name + "." + socket.name, utils.snake_case(socket.parent.name + '_' + socket.name)]

        return socket_names

    # ----------------------------------------------------------------------------------------------------
    # Get the socket argument names

    def get_arg_names_OLD(self):

        # ----- We start with sockets which are not in a panel
        top_keys = [utils.snake_case(sock.name) for sock in self.get_in_sockets(panel_name="").values()]

        # ----- The keys of each panel
        panels = list(self.get_panels().keys())
        panel_keys = {}
        for panel in panels:
            panel_keys[utils.snake_case(panel)] = [utils.snake_case(sock.name) for sock in self.get_in_sockets(panel_name=panel).values()]

        # ----- Let's build a full list

        args = list(top_keys)
        for panel, keys in panel_keys.items():
            for key in keys:
                with_panel = False
                if key in top_keys:
                    with_panel = True
                else:
                    for p in panels:
                        if p == panel:
                            continue
                        if key in panel_keys[p]:
                            with_panel = True
                            break
                if with_panel:
                    args.append(panel + '_' + key)
                else:
                    args.append(key)

        # ----- We ensure uniques

        return utils.ensure_uniques(args, single_digit=True)

    # ====================================================================================================
    # Get an output socket by its name

    def get_out_socket_OLD(self, name: str, halt: bool = True):
        """ Get an output socket by its name

        Arguments
        ---------
        - name : socket name
        - halt : raise an exception if not found

        Raises
        ------
        - AttributeError : if socket not found

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfaceItem with in_out = 'INPUT'
        """
        sockets = self.get_out_sockets()
        socket = sockets.get(name)
        if socket is not None:
            return socket

        for socket in sockets.values():
            if socket.name == name:
                return socket

        if halt:
            raise AttributeError(f"Output socket '{name}' not found in {list(sockets.keys())}")

        return None

    # ----------------------------------------------------------------------------------------------------
    # Get an input socket by its name

    def get_in_socket_OLD(self, name, panel_name: str | None = None, halt: bool = True):
        """ Get an input socket by its name

        The name of the panel can be specified either with the 'panel_name' argument or by concatenation
        In the following example, the lines return the same socket:

        ``` python
        interface_socket = interface.get_in_socket('Socket Name', 'My Panel')
        interface_socket = interface.get_in_socket('My Panel Socket Name')
        interface_socket = interface.get_in_socket('my_panel Socket Name')
        interface_socket = interface.get_in_socket('my_panel_socket_name')
        interface_socket = interface.get_in_socket('My Panel socket_name')
        ```

        If 'panel_name' is an empty string, the socket is searched in the sockets which are not
        in a panel.

        Arguments
        ---------
        - name : socket name
        - panel_name : name of the panel the socket belongs to
        - halt : raise an exception if not found

        Raises
        ------
        - AttributeError : if socket not found

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfaceItem with in_out = 'INPUT'
        """

        # ----- Particular case : name is the index

        if isinstance(name, int):
            sockets = self.get_in_sockets()
            key = list(sockets.keys())[name]
            return sockets[key]

        # ----- Name is a string
        # Let's build the full path including the panel name

        if panel_name is None:
            full_name = name
        else:
            full_name = utils.snake_case(panel_name + '_' + name)

        # ----- get_in_socket_names returns all the possible names

        socket_names = self.get_in_socket_names()

        # ---- Loop on the candidates, return the first matching socket

        for identifier, names in socket_names.items():
            if full_name in names:
                return self.by_identifier(identifier)

        if halt:
            if panel_name is None:
                raise Exception(f"Input socket '{name}' not found in {list(sockets.keys())}")
            else:
                raise Exception(f"Input socket '{name}' not found in panel '{panel_name}' sockets {list(sockets.keys())}")

        return None

    # ====================================================================================================
    # Creations

    # ----------------------------------------------------------------------------------------------------
    # Create a panel

    def create_panel(self, name: str, tip: str=""):
        """ Create a panel

        > [!NOTE]
        > The panel is not created if a panel with the same name already exists

        Arguments
        ---------
        - name : panel name
        - tip : description

        Returns
        -------
        - Panel
        """
        if name is None or name == "":
            return None

        panel = self.get_panel(name, halt=False)
        if panel is not None:
            return panel

        return self.btree.interface.new_panel(name, description=tip, default_closed=False)

    # ----------------------------------------------------------------------------------------------------
    # Create an output socket

    def create_out_socket_OLD(self, name: str, socket_type: str, tip: str="", panel: str = ""):
        """ Create an output socket

        > [!NOTE]
        > The sockets is created even if a socket with the same name already exists

        Arguments
        ---------
        - name : socket name
        - socket_type: socket type
        - tip : description
        - panel : panel name

        Returns
        -------
        - Socket
        """
        parent = None
        if panel != "":
            parent = self.create_panel(panel)

        return self.btree.interface.new_socket(name, description=tip, in_out='OUTPUT', socket_type=socket_type, parent=parent)

    # ----------------------------------------------------------------------------------------------------
    # Create an input socket

    def create_in_socket_OLD(self, name: str, socket_type: str, tip: str="", panel: str = ""):
        """ Create an output socket

        > [!NOTE]
        > The sockets is created even if a socket with the same name already exists

        Arguments
        ---------
        - name : socket name
        - socket_type: socket type
        - tip : description
        - panel : panel name

        Returns
        -------
        - Socket
        """
        parent = None
        if panel != "":
            parent = self.create_panel(panel)

        socket = self.btree.interface.new_socket(name, description=tip, in_out='INPUT', socket_type=socket_type, parent=parent)

        if False:
            if socket_type == 'NodeSocketGeometry' and panel == "":
                sockets = self.get_in_sockets(panel_name="")
                ok = False
                for sock in sockets.values():
                    if sock.socket_type == 'NodeSocketGeometry' and sock.index == 0:
                        ok = True
                        break
                if not ok:
                    self.btree.interface.move(socket, 0)

        return socket

    # ----------------------------------------------------------------------------------------------------
    # Ensure geometry in

    def set_in_geometry(self, name: str | None = None, create: bool = False):
        """ Ensure that the Geometry input socket is the first

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        - create : create the socket if it doesn't exist
        """

        if name is None:
            name = "Geometry"

        sockets = self.get_items('SOCKET', 'INPUT', panel="")
        geo = None
        for socket in sockets:
            if socket.socket_type == 'NodeSocketGeometry':
                geo = socket
                break

        if geo is None:
            if not create:
                return None
            geo, _ = self.get_create_socket('INPUT', name, 'NodeSocketGeometry', panel="")

        self.btree.interface.move_to_parent(geo, None, 0)
        return geo

    # ----------------------------------------------------------------------------------------------------
    # Ensure geometry out

    @property
    def has_out_geometry_OLD(self):
        sockets = self.get_items('SOCKET', 'OUTPUT')
        if not len(sockets):
            return False
        return sockets[0].socket_type == 'NodeSocketGeometry'

    def set_out_geometry(self, name="Geometry"):
        """ Make sure the tree has an output geometry and that it is the first one

        If the tree has no output Geometry socket, one is created

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        """
        if name is None:
            name = "Geometry"

        geo, _ = self.get_create_socket('OUTPUT', name, 'NodeSocketGeometry', panel="")
        self.btree.interface.move_to_parent(geo, None, 0)
        return geo

    # ====================================================================================================
    # Set the default value

    def set_default_value_OLD(self, identifier: str, value: 'Any' = None, update_socket: bool =True):
        """ Set the default value of an input socket

        Arguments
        ---------
        - identifier : socket identifier
        - value : value suitable for the socket type
        - update_socket : update socket default value

        Returns
        -------
        - Any : default value which was set or None if socket has node default value
        """

        if value is None:
            return None

        item = self.by_identifier(identifier)
        blid = item.socket_type

        if blid == 'NodeSocketString':
            item.default_value = str(value)

        elif blid == 'NodeSocketBool':
            item.default_value = bool(value)

        elif blid == 'NodeSocketMaterial':
            item.default_value = utils.get_blender_resource('MATERIAL', str(value))

        elif blid == 'NodeSocketVector':
            if hasattr(value, '__len__'):
                item.default_value = tuple(value)
            else:
                item.default_value = tuple(np.resize(value, 3))

        elif blid == 'NodeSocketInt':
            item.default_value = int(value)

        elif blid == 'NodeSocketMenu':
            menu_node = None
            for link in self.btree.links:
                if link.from_node.bl_idname == 'NodeGroupInput' and link.from_socket.identifier == identifier:
                    menu_node = link.to_node
                    break

            if menu_node is None:
                return None

            for socket in menu_node.inputs[1:]:
                if isinstance(value, str):
                    item.default_value = value
                else:
                    n = len(menu_node.inputs) - 2
                    if value < 0 or value > n-1:
                        raise Exception(f"Menu default value error: {value} is invalid, Menu as {n} items {[sock.name for sock in menu_node.inputs[1:n+1]]}")
                    item.default_value = menu_node.inputs[1 + value].name

        elif blid == 'NodeSocketCollection':
            item.default_value = utils.get_blender_resource('COLLECTION', str(value))

        elif blid == 'NodeSocketGeometry':
            return None

        elif blid == 'NodeSocketTexture':
            item.default_value = utils.get_blender_resource('TEXTURE', str(value))

        elif blid == 'NodeSocketFloat':
            item.default_value = value

        elif blid == 'NodeSocketColor':
            if hasattr(value, '__len__'):
                if len(value) == 3:
                    item.default_value = (value[0], value[1], value[2], 1)
                else:
                    item.default_value = tuple(value)
            else:
                item.default_value = (value, value, value, 1)

        elif blid == 'NodeSocketObject':
            item.default_value = utils.get_blender_resource('OBJECT', str(value))

        elif blid == 'NodeSocketRotation':
            if hasattr(value, '__len__'):
                item.default_value = tuple(value)
            else:
                item.default_value = tuple(np.resize(value, 3))

        elif blid == 'NodeSocketMatrix':
            return None

        elif blid == 'NodeSocketImage':
            item.default_value = utils.get_blender_resource('IMAGE', str(value))

        else:
            assert(False)

        # ----------------------------------------------------------------------------------------------------
        # Update socket

        if update_socket:
            for node in self.btree.nodes:
                if node.bl_idname == 'NodeGroupInput':
                    for socket in node.outputs:
                        if socket.identifier == identifier:
                            socket.default_value = item.default_value
                            break
                    break

        return item.default_value

    # ====================================================================================================
    # Order the sockets

    def set_order_OLD(self, inputs: list[str] = [], panel: str = "", outputs: list[str] = []):
        """ Order the sockets

        Raises
        ------
        - AttributeError if a socket is not found in one of the lists

        Arguments
        ---------
        - inputs : names of the input sockets in the target order
        - outputs : names of the output socket in the target order
        """
        for name in reversed(inputs):
            item = self.get_in_socket(name, panel_name=panel)
            self.btree.interface.move(item, 0)

        for name in reversed(outputs):
            item = self.get_out_socket(name)
            self.btree.interface.move(item, 0)

    # ====================================================================================================
    # Tests

    def demo_create_all_sockets(self):

        blids = ('NodeSocketString', 'NodeSocketBool', 'NodeSocketMaterial', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketMenu',
            'NodeSocketCollection', 'NodeSocketGeometry', 'NodeSocketTexture', 'NodeSocketFloat', 'NodeSocketColor',
            'NodeSocketObject', 'NodeSocketRotation', 'NodeSocketMatrix', 'NodeSocketImage')

        out_sockets={}
        for blid in blids:
            out_sockets[blid] = self.create_in_socket(blid[10:], blid)

        input_node = self.btree.nodes.get('Group Input')

        # ===== Menu

        if input_node is not None:
            menu_node   = self.btree.nodes.new('GeometryNodeMenuSwitch')
            menu_socket = input_node.outputs['Menu']
            self.btree.links.new(menu_socket, menu_node.inputs[0])
