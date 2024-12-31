""" This module implements the TreeInterface class to
manage Tree input and output sockets creation and ordering.
"""

import bpy
from . import utils

import numpy as np

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

    def clear(self):
        self.btree.interface.clear()

    # ====================================================================================================
    # Utilities

    @staticmethod
    def ensure_uniques(names: list[str], single_digit: bool = False):
        """ Build a list of unique names from a list

        Doublons are suffixed by an index:
        - ['key', 'key', 'other'] -> ['key', 'key_001', 'other']

        Arguments
        ---------
        - names : list of names with possible doublons
        - single_digit : 'key_1' rather that 'key_001'

        Returns
        -------
        - list of str : doublons are suffixed by an index
        """
        homos  = {}
        uniques = []
        for name in names:
            count = homos.get(name)
            if count is None:
                uniques.append(name)
                homos[name] = 1
            else:
                if single_digit:
                    uniques.append(f"{name}_{count:d}")
                else:
                    uniques.append(f"{name}_{count:03d}")
                homos[name] = count + 1
        return uniques

    @staticmethod
    def get_socket_bl_idname(socket):
        if socket.bl_subtype_label is None or socket.bl_subtype_label == 'None':
            return socket.bl_idname
        else:
            return socket.bl_idname[:-len(socket.bl_subtype_label)]

    @staticmethod
    def socket_in_list(socket, names):
        if names is None:
            return False

        elif isinstance(names, str):
            names = [names]

        return (socket.name in names) or (socket.identifier in names) or (utils.socket_name(socket.name) in names)

    # ====================================================================================================
    # Get list of items

    # ----------------------------------------------------------------------------------------------------
    # Get items of a certain category

    def _get_items(self, item_type: str ='PANEL', in_out: str ='INPUT', panel: 'Parent Panel | str | None' = None):
        """ Get items matching the criteria passed in arguments

        Arguments
        ---------
        - item_type (str = 'PANEL') : str in ('PANELS', 'SOCKET')
        - in_out (str = 'INPUT') : str in ('INPUT', 'OUTPUT')
        - panel (bpy.types.NodeTreeInterfacePanel = None) : the panel the items must belong to

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfaceItem
        """
        items = []
        for item in self.btree.interface.items_tree:

            if item.item_type != item_type:
                continue

            if item_type == 'SOCKET':
                if item.in_out != in_out:
                    continue

            if panel is None:
                pass

            elif isinstance(panel, str):
                if item.parent.name != panel and utils.socket_name(item.parent.name) != panel:
                    continue

            else:
                if item.parent != panel:
                    continue

            items.append(item)

        keys = self.ensure_uniques([utils.socket_name(item.name) for item in items])

        return {key:item for key, item in zip(keys, items)}

    # ----------------------------------------------------------------------------------------------------
    # Get the output interface sockets

    def get_out_sockets(self):
        """ Get the output interface sockets

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfaceItem with in_out = 'OUTPUT'
        """
        return self._get_items('SOCKET', 'OUTPUT')

    # ----------------------------------------------------------------------------------------------------
    # Get the panels

    def get_panels(self):
        """ Get the panels

        Returns
        -------
        - dict : socket unique python name: bpy.types.NodeTreeInterfacePanel
        """
        return self._get_items('PANEL')

    # ----------------------------------------------------------------------------------------------------
    # Get the output interface sockets

    def get_in_sockets(self, panel_name: str | None=None):
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

    # ====================================================================================================
    # Get individual items

    def by_identifier(self, identifier):
        for item in self.btree.interface.items_tree:
            if item.item_type == 'SOCKET' and item.identifier == identifier:
                return item
        return None

    # ----------------------------------------------------------------------------------------------------
    # Get a panel by its name

    def get_panel(self, name: str, halt: bool = True):
        """ Get a panel by its name

        Arguments
        ---------
        - name : socket name
        - halt : raise an exception if not found

        Raises
        ------
        - AttributeError : if panel not found

        Returns
        -------
        - panel
        """
        panels = self.get_panels()
        panel = panels.get(name)
        if panel is not None:
            return panel

        for panel in panels.values():
            if panel.name == name:
                return panel

        if halt:
            raise AttributeError(f"Panelt '{name}' not found in {list(panels.keys())}")

        return None

    # ----------------------------------------------------------------------------------------------------
    # Get an output socket by its name

    def get_out_socket(self, name: str, halt: bool = True):
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

    def get_in_socket(self, name, panel_name: str | None = None, halt: bool = True):
        """ Get an input socket by its name

        The name of the panel can be specified either with the 'panel_name' argument or using dot syntax.
        In the following example, the two lines return the same socket:

        ``` python
        interface_socket = interface.get_in_socket('Socket Name', 'My Panel')
        interface_socket = interface.get_in_socket('My Panel.Socket Name')
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
        if panel_name is None:
            composed = name.split('.')
            if len(composed) == 2:
                panel_name = composed[0]
                name = composed[1]

        sockets = self.get_in_sockets(panel_name=panel_name)
        socket = sockets.get(name)
        if socket is not None:
            return socket

        for socket in sockets.values():
            if socket.name == name:
                return socket

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
        panel = self.get_panel(name, halt=False)
        if panel is not None:
            return panel

        return self.btree.interface.new_panel(name, description=tip, default_closed=False)

    # ----------------------------------------------------------------------------------------------------
    # Create an output socket

    def create_out_socket(self, name: str, socket_type: str, tip: str="", panel: str = ""):
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

    def create_in_socket(self, name: str, socket_type: str, tip: str="", panel: str = ""):
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

    def set_in_geometry(self, name: str | None = None, create: bool =False):
        """ Ensure that the Geometry input socket is the first

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        - create : create the socket if it doesn't exist
        """
        if name is None:
            name = "Geometry"
        sockets = self.get_in_sockets(panel_name="")
        geo = None
        for socket in sockets.values():
            if socket.socket_type == 'NodeSocketGeometry':
                geo = socket
                break

        if geo is None:
            if not create:
                return None
            geo = self.create_in_socket(name, socket_type = 'NodeSocketGeometry')

        self.btree.interface.move(geo, 0)
        return geo

    # ----------------------------------------------------------------------------------------------------
    # Ensure geometry out

    @property
    def has_out_geometry(self):
        sockets = self.get_out_sockets()
        if not len(sockets):
            return False
        return sockets[list(sockets.keys())[0]].socket_type == 'NodeSocketGeometry'

    def set_out_geometry(self, name="Geometry"):
        """ Make sure the tree has an output geometry and that it is the first one

        If the tree has no output Geometry socket, one is created

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        """
        if name is None:
            name = "Geometry"
        sockets = self.get_out_sockets()
        geo = None
        for socket in sockets.values():
            if socket.socket_type == 'NodeSocketGeometry':
                geo = socket
                break

        if geo is None:
            geo = self.create_out_socket(name, socket_type = 'NodeSocketGeometry')

        self.btree.interface.move(geo, 0)
        return geo

    # ====================================================================================================
    # Set the default value

    def set_default_value(self, identifier: str, value: 'Any' = None, update_socket: bool =True):
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
    # Link two nodes

    def link_nodes(self, from_node: 'Blender Node | None', to_node: 'Blender Node | None', include: list[str] | str | None =None, exclude: list[str] | str = [], panel: str = ""):
        """ Link two nodes

        The nodes are linked between sockets having the same name and the same type (and sub type)

        If one of the two nodes is None, the links are made with tree interface:

        ``` python
        math1 = Node('Math')
        math2 = Node('Math')

        # Link output socket of math1 to first input socket of math2
        inteface.link_nodes(math1, math2)

        # Create to group input sockets
        inteface.link_nodes(None, math2)

        # Create one group output socket linked to math1 output socket
        interface.link_nodes(math1, None)
        ```

        > [!NOTE]
        > If the tree doesn't have a Group Input or Output node, it is created in order to create the links

        When one of the node is a tree interface, the sockets are created.


        Arguments
        ---------
        - from_node : the node to link output sockets from
        - to_node : the node to link input sockets to
        - include : limit the links to this list
        - exclude : exlude sockets in the list
        - panel : panel name for sockets not in a panel

        Returns
        -------
        - list of created output sockets
        """

        # ----------------------------------------------------------------------------------------------------
        # Nodes can be groups or tree input / outputs

        create_group_inputs  = False
        create_group_outputs = False

        # ===== Input node interface if any

        if from_node is None:
            for node in self.btree.nodes:
                if node.bl_idname == 'NodeGroupInput':
                    from_node = node
                    break

        from_interface = None
        if from_node.bl_idname == 'NodeGroupInput':
            from_interface = self
            create_group_inputs = True

        elif from_node.bl_idname == 'GeometryNodeGroup':
            from_interface = TreeInterface(from_node.node_tree)

        # ===== Output node interface if any

        if to_node is None:
            for node in self.btree.nodes:
                if node.bl_idname == 'NodeGroupOutput':
                    to_node = node
                    break

        to_interface = None
        if to_node.bl_idname == 'NodeGroupOutput':
            to_interface = self
            create_group_outputs = True

        elif to_node.bl_idname == 'GeometryNodeGroup':
            to_interface = TreeInterface(to_node.node_tree)

        # ===== Sockets cant' be created on both sides

        if create_group_inputs and create_group_outputs:
            create_group_inputs, create_group_outputs = False, False

        # ----------------------------------------------------------------------------------------------------
        # Which list of sockets to loop on

        if create_group_outputs:
            target_sockets = from_node.outputs
            source_sockets = to_node.inputs
            source_is_from = False
        else:
            target_sockets = to_node.inputs
            source_sockets = from_node.outputs
            source_is_from = True

        create = create_group_outputs or create_group_inputs


        # ----------------------------------------------------------------------------------------------------
        # Let's loop

        sockets = []

        for target_socket in target_sockets:

            # ----- Nothing to do condtions

            # No virtual sockets

            if target_socket.type == 'CUSTOM':
                continue

            # Not already linked

            if target_socket.is_linked:
                continue

            # Must be in the include list
            if include is not None and not self.socket_in_list(target_socket, include):
                continue

            # Must not be in the exclude list
            if self.socket_in_list(target_socket, exclude):
                continue

            # ----- Do we have an acceptable candidate as source

            source_socket = None
            for sock in source_sockets:
                # Alredy used
                if sock in sockets:
                    continue

                if sock.name == target_socket.name and sock.bl_idname == target_socket.bl_idname:
                    source_socket = sock
                    break

            # ----- Not found : let's try to create it

            if source_socket is None:
                if not create:
                    continue

                # Creation parameters

                bl_idname = self.get_socket_bl_idname(target_socket)
                descr = target_socket.description

                source_panel = panel

                itf_item = None if to_interface is None else to_interface.by_identifier(target_socket.identifier)
                if itf_item is not None:
                    if descr == "":
                        descr = itf_item.description
                    if itf_item.parent.name != "":
                        source_panel = itf_item.parent.name

                # Let's create

                if create_group_outputs:
                    source_item = self.btree.interface.new_socket(target_socket.name, in_out='OUTPUT', socket_type=bl_idname, description=descr)
                    source_item.from_socket(from_node, target_socket)

                    for sock in to_node.inputs:
                        if sock.identifier == source_item.identifier:
                            source_socket = sock
                            break

                    assert(source_socket is not None)

                else:
                    source_item = self.btree.interface.new_socket(target_socket.name, in_out='INPUT', socket_type=bl_idname, description=descr)
                    source_item.from_socket(to_node, target_socket)

                    print("CREATE", source_item, "FROM", target_socket)

                    # We put it in the proper panel
                    if source_panel != "":
                        panel_item = self.create_panel(source_panel)
                        n = len(self.get_in_sockets(panel_name=source_panel))
                        self.btree.interface.move_to_parent(source_item, panel_item, n)

                    for sock in from_node.outputs:
                        if sock.identifier == source_item.identifier:
                            source_socket = sock
                            break

                    assert(source_socket is not None)

            # ----- Put the socket in the result

            sockets.append(source_socket)

            # ----- And we link at last !!!

            if source_is_from:
                self.btree.links.new(source_socket, target_socket)
            else:
                self.btree.links.new(target_socket, source_socket)

        return sockets

    # ====================================================================================================
    # Order the sockets

    def set_order(self, inputs: list[str] = [], panel: str = "", outputs: list[str] = []):
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
