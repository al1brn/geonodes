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

module : treeinterface
----------------------
- TreeInterface class

This module implements the TreeInterface class to
manage Tree input and output sockets creation and ordering.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


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
                        homo = snake_case(sepa + unique)
                        # Could be equal when socket starts with a figure
                        if homo != unique:
                            homonyms[homo] = socket

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
                        # Could be equal if unique starts with a figure
                        homo = snake_case(panel_name + sepa + unique)
                        if homo not in names:
                            homonyms[homo] = socket
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
        """ Get the socket by its name

        Arguments
        ---------
        - in_out (str) : str in ('INPUT', 'OUTPUT')
        - name (str) : searched named
        - as_argument (bool = True) : the name is argument or socket name
        - halt (bool = False) : raises an error if not found

        Returns
        -------
        - Node, Interface socket or list of sockets depending on the arguments
        """

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
        socket = names.get(socket_name)

        if socket is None and halt:
            raise NodeError(f"{in_out} socket '{name}' not found in '{self.btree.name}'.", valids=list(names.keys()))

        return socket

    # ====================================================================================================
    # Get or create a socket

    def get_create_socket(self, in_out, name, socket_type, panel="", force_create=False):
        """ Get a socket or create it if if doesn't exist

        Returns
        -------
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
            if (not force_create) and (item.name == name) and (item.socket_type == socket_type):
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

        if socket.description == DELETION:
            socket.description = ""

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

    # ====================================================================================================
    # Create a panel

    def create_panel(self, name: str, tip: str="", closed_by_default=False):
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
            panel.default_closed = closed_by_default
            return panel

        return self.btree.interface.new_panel(name, description=tip, default_closed=closed_by_default)

    # ====================================================================================================
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

    def set_out_geometry(self, name=None):
        """ Make sure the tree has an output geometry and that it is the first one

        If the tree has no output Geometry socket, one is created

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        """
        for nm, s in self.get_unique_names('OUTPUT', as_argument=False, include_homonyms='NO').items():
            if s.socket_type == 'NodeSocketGeometry':
                if name is None or nm == name:
                    self.move_socket_to(s, 0)
                    if s.description == DELETION:
                        s.description = ""
                    return

        if name is None:
            name = "Geometry"

        geo, _ = self.get_create_socket('OUTPUT', name, 'NodeSocketGeometry', panel="")
        self.btree.interface.move_to_parent(geo, None, 0)
        return geo

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
