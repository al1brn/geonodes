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

module : zones
----------------------
- Zone class
- Simulation class
- Repeat class
- ForEach class

This module implements the zones, i.e. the couple of input / output nodes
forming a zone such as Repeat, Simulation or Foreach

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

from .scripterror import NodeError
from . import utils
from .inoutcontext import InOutContext
from .signature import Signature
from .treeclass import Tree
from .nodeclass import Node

# ====================================================================================================
# Node Items
# ====================================================================================================

class NodeItems:

    def __init__(self, node, name, named_sockets={}, capture=[], **sockets):
        """ > Node items property

        Some nodes have xxx_items collection for dynamic sockets. This class manages this behavior,
        especially for zones (Simulation, Repeat, ForEachElement)
        """

        self._node     = node
        self._name     = name
        self._capture  = [s.lower() for s in capture]
        self._items    = getattr(node._bnode, name + '_items')

        # ----- Create the simulation state items in the output node

        if len(name) <= 6 or name[-6:] != '_items':
            items_name = name + '_items'
        else:
            items_name = name

        self._node._set_items(items_name, named_sockets=named_sockets, plug_items=True, **sockets)

    # ----------------------------------------------------------------------------------------------------

    def get_inout(self, index, input=True):
        if isinstance(index, int):
            socket_name = self._items[index].name
        else:
            socket_name = index

        sockets = self._node._bnode.inputs if input else self._node._bnode.outputs

        for i, bsocket in enumerate(sockets):

            if not input and (bsocket.identifier.lower() in self._capture):
                return self._node.data_socket(bsocket)

            if not bsocket.identifier.lower().startswith(self._name):
                continue

            if socket_name in [bsocket.name, bsocket.identifier, utils.snake_case(bsocket.name)]:
                if input:
                    return bsocket
                else:
                    return self._node.data_socket(bsocket)

        return None

    # ----------------------------------------------------------------------------------------------------

    def __getitem__(self, index):
        item = self.get_inout(index, input=False)
        if item is None:
            bnode = self._node._bnode

            for bsock in bnode.outputs:
                print("SOCKET", bsock.name)
                for k in dir(bsock):
                    print(f"- {k:15s} : {str(getattr(bsock, k)):25s}")
                print()

            raise NodeError(f"Socket '{index}' not found in items {self._name} of the node '{bnode.name}'",
                valids=[item for item in self._items])
        return item

    # ----------------------------------------------------------------------------------------------------

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)

        else:
            current = self.get_inout(name, input=True)
            if current is None:
                input_type = 'GEOMETRY' if value is None else utils.get_value_socket_type(value)
                self._items.new(input_type, name)
                current = self.get_inout(name, input=True)

            self._node.plug_value_into_socket(value, current)

    # ----------------------------------------------------------------------------------------------------

    def __getattr__(self, name):
        return self[name]

# ====================================================================================================
# A zone
# ====================================================================================================

class Zone(InOutContext):

    ITEMS_NAME   = None # Name of node 'xxx_items' property (dynamic if None)
    PLUG_ON_EXIT = True # Plug loop variables to output node when exiting (False for ForEachElement)
    TEMP_ZONE    = True

    def __str__(self):
        return f"<{type(self).__name__} Zone, loop variables: {list(self._locals.keys())}>"

    # ====================================================================================================
    # Initialization
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Layout
    # ----------------------------------------------------------------------------------------------------

    def init_layout(self):
        from geonodes import Layout
        if Zone.TEMP_ZONE:
            self._layout = Layout("$TEMP_ZONE")
        else:
            self._layout = None

    # ----------------------------------------------------------------------------------------------------
    # Zone
    # ----------------------------------------------------------------------------------------------------

    def init_zone(self, named_sockets={}, **sockets):
        """ > Two nodes zone

        **Zone** is the root class for <!Simulation>, <!Repeat> and <!ForEachElement> zones.

        #### With block

        A **Zone** is intended to be used in a **with** block:

        ``` python
        with Zone(...) as zone:
            ...
        ```

        #### Sockets definition

        The zone sockets can be defined in two ways:
        - using the **sockets** dict argument
        - using the **snake_case_sockets** key word arguments

        ``` python
        # Create a zone with 2 sockets:
        # - First Socket
        # - second_socket
        with Zone({"First Socket": Geometry()}, second_socket=Float(3.14)) as zone:
            ...
        ```

        <@zone_sockets.png center 600>

        > [!NOTE]
        > The sockets are created on the two nodes and, in both nodes, as input and output sockets.
        > Hence, a single name correspond two 4 sockets:
        > - input socket of the first node
        > - output socket of the first node
        > - input socket of the second node
        > - output socket of the second node

        #### Getting and setting zone sockets

        Zone sockets are accessed through their **snake_case** name whatever the manner they have
        been initialized:

        ``` python
        with Zone({"First Socket": Geometry()}, second_socket=Float(3.14)) as zone:
            a = zone.first_socket
            b = zone.second_socket
        ```

        Inside the **with** block:
        - **getting** a socket: output socket of the first node
        - **setting** a socket: input socket of the second node

        Outside the **with** block:
        - **getting** a socket: output socket of the second node
        - **setting** a socket: Error

        Even if it is not easy to describe, this is in fact quite straightforward:

        ``` python
        with Repeat(geometry=None, index=0, iterations=10) as repeat_zone:

            # Value of the current index
            index = repeat_zone.index

            # ...

            # Update the index for next loop
            repeat_zone.index = index + 1

            # Incrementing is also valid
            repeat_zone.index += 1

        # Outside the block, we have accees to the result of the loop
        geo = repeat_zone.geometry
        ```

        Properties
        ----------
        - _closed (bool) : in or out the zone
        - _locals (list) : list of zone properties

        Arguments
        ---------
        - defaults (dict = {}) : default sockets
        - sockets (dict = {}) : sockets to create, string names
        - snake_case_sockets : sockets to create, snake_case names
        """

        # ----- Create the simulation state items in the output node

        self._output._set_items(self.ITEMS_NAME, named_sockets=named_sockets, plug_items=False, **sockets)

        # ----- Plug the sockets in the input node

        all_sockets = {utils.snake_case(name): value for name, value in {**named_sockets, **sockets}.items()}
        for name, value in all_sockets.items():
            self._input.plug_value_into_socket(value, name)

        # ----- Variables used within the with statement

        sockets = self._input.get_socket_names('OUTPUT', as_argument=True)
        self._locals = {pname: sockets[pname] for pname in all_sockets.keys()}

        # ----- Ensure the proper sub class of geometries

        for pname in self._locals.keys():
            geo = self._locals[pname]
            if geo.SOCKET_TYPE == 'GEOMETRY':
                if all_sockets[pname] is not None:
                    self._locals[pname] = type(all_sockets[pname])(geo)

        self._closed = True

    # ====================================================================================================
    # Context management
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Pushing
    # ----------------------------------------------------------------------------------------------------

    def push(self):

        # ---------------------------------------------------------------------------
        # A Closed: drives the attributes to input / output nodes
        # ---------------------------------------------------------------------------

        self._closed = False

        # ---------------------------------------------------------------------------
        # B Push the layout
        # ---------------------------------------------------------------------------

        if self._layout is not None:
            self._layout.push()

        # ---------------------------------------------------------------------------
        # C Capture the input creation sockets
        # ---------------------------------------------------------------------------

        Tree.current_tree()._capture_inout.append(self)

    # ----------------------------------------------------------------------------------------------------
    # Poping
    # ----------------------------------------------------------------------------------------------------

    def pop(self):

        # ---------------------------------------------------------------------------
        # A Close the zone
        # ---------------------------------------------------------------------------

        self._closed = True

        # ---------------------------------------------------------------------------
        # B Pop the layout
        # ---------------------------------------------------------------------------

        if self._layout is not None:
            self._layout.pop()

        # ---------------------------------------------------------------------------
        # C end of capture
        # ---------------------------------------------------------------------------

        Tree.current_tree()._capture_inout.pop()

        # ---------------------------------------------------------------------------
        # Other: Plug the local variables to the output node inputs
        # ---------------------------------------------------------------------------

        if self._plug_on_exit:
            for name, value in self._locals.items():
                setattr(self._output, name, value)


    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.pop()
        return False
    
    # ====================================================================================================
    # Attributes
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Getting
    # ----------------------------------------------------------------------------------------------------

    def __getattr__(self, name):

        closed = self.__dict__.get('_closed')
        if closed is not None:

            # ----------------------------------------------------------------------------------------------------
            # After the zone

            if closed:

                val = getattr(self._output, name)

                # Ensure proper geometry type
                loc_val = self._locals.get(name)
                if loc_val is not None and loc_val.SOCKET_TYPE == 'GEOMETRY':
                    val = type(loc_val)(val)

            # ----------------------------------------------------------------------------------------------------
            # In the zone

            else:
                val = self._locals.get(name)
                # Trying to access fixed sockets (such as 'Delta Time')
                if val is None:
                    val = getattr(self._input, name)

            if val is not None:
                return val

        raise NodeError(f"{type(self).__name__} doesn't have input socket named '{name}'.")
    
    # ----------------------------------------------------------------------------------------------------
    # Setting
    # ----------------------------------------------------------------------------------------------------

    def __setattr__(self, name, value):

        if name in ('_closed', '_plug_on_exit'):
            super().__setattr__(name, value)
            return
        
        closed = self.__dict__.get('_closed')
        if closed is None:
            super().__setattr__(name, value)
            return

        if closed:
            raise NodeError(f"{self} is closed : impossible to set {name}!")

        if name in self._locals:
            self._locals[name] = value
        else:
            if True:
                setattr(self._output, name, value)
            else:
                self._output.plug_value_into_socket(value, name)

    # ====================================================================================================
    # InOutContext interface
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Create an input socket
    # ----------------------------------------------------------------------------------------------------

    def create_input_socket(self, bl_idname, name, value=None, panel="", **props):

        items = getattr(self._output._bnode, self.ITEMS_NAME)
        items.new(utils.bl_idname_to_socket_type(bl_idname), name)

        index = None
        socks = self._input._bnode.inputs
        for i, sock in enumerate(socks):
            if sock.name == name:
                index = i
                break

        assert index is not None, f"Strange {name}, {[sock.name for name in socks]}."

        socket = self._input[index]
        if hasattr(socket._bsocket, 'default_value') and value is not None:
            socket._bsocket.default_value = value

        return socket
    
    # ----------------------------------------------------------------------------------------------------
    # Create a new input socket from an existing node input socket
    # ----------------------------------------------------------------------------------------------------

    def create_input_from_socket(self, input_socket, name=None, panel="", **props):

        # Ensure name
        if name is None:
            name = utils.get_socket_name(input_socket)

        # Create new item and link it
        items = getattr(self._output._bnode, self.ITEMS_NAME)
        item_type = utils.get_bsocket(input_socket).type
        if item_type == 'VALUE':
            item_type = 'FLOAT'
        items.new(item_type, name)
        socket = self._input[len(items) - 1]
        self._tree.link(socket, input_socket)

        # Return the created socket
        return self._input_node[name]
    
    # ----------------------------------------------------------------------------------------------------
    # Output socket
    # ----------------------------------------------------------------------------------------------------

    def create_output_socket(self, socket, name=None, panel="", **props):

        # Ensure name
        if name is None:
            name = type(socket).__name__

        # bl_idname
        bl_idname = utils.get_bsocket(socket).bl_idname
        bl_idname, _, _ = utils.get_socket_subtype(bl_idname)

        # Exists ?
        in_socket = None
        for bsock in self._output._bnode.inputs:
            print(f"TEST: {name=}, {bl_idname=}, {bsock.name=}, {bsock.bl_idname=}")
            if bsock.name == name and bsock.bl_idname == bl_idname:
                in_socket = bsock
                break

        # Create
        if in_socket is None:
            self.create_input_socket(bl_idname, name)
            in_socket = self._output._bnode.inputs[-2]

        self._input._tree.link(socket, in_socket)

        return in_socket


    # ----------------------------------------------------------------------------------------------------
    # Get the signature
    # ----------------------------------------------------------------------------------------------------

    def get_signature(self, include: list = None, exclude: list = [], enabled_only=True, with_sockets: bool = False):
        return Signature(
            self._input.get_signature(include=include, exclude=exclude, only_enalbed=enabled_only, with_sockets=with_sockets).inputs,
            self._output.get_signature(include=include, exclude=exclude, only_enalbed=enabled_only, with_sockets=with_sockets).outputs
        )

# ====================================================================================================
# Reapet zone

class Repeat(Zone):

    ITEMS_NAME   = 'repeat_items'

    def __init__(self, named_sockets={}, iterations=1, **sockets):
        """ > Repeat zone

        > See <!Zone>

        ``` python
        from geonodes import *

        with GeoNodes("Demo Repeat"):

            with Repeat(Geometry=Geometry(), z=3, iterations=5) as repeat_zone:

                # Lopp geomety
                geo = repeat_zone.geometry

                # Offset upwards
                geo = geo.set_position(offset=(0, 0, repeat_zone.z))

                # Join to loop geometry (CAUTION: exponential growth)
                repeat_zone.geometry += geo

                # Net vertical offset
                repeat_zone.z *= 2

            # Result to output
            repeat_zone.geometry.out()
        ```

        Arguments
        ---------
        - sockets (dict = {}) : sockets to create
        - iterations (int = 1) : Iterations socket
        - snake_case_sockets : sockets to create
        """

        self._plug_on_exit = self.PLUG_ON_EXIT

        self.init_layout()

        self._input  = Node('GeometryNodeRepeatInput')
        self._output = Node('GeometryNodeRepeatOutput')
        self._input._bnode.pair_with_output(self._output._bnode)
        self._output._bnode.repeat_items.clear()

        self.init_zone(named_sockets, **sockets)
        self._input.iterations = iterations

# ====================================================================================================
# Simulation zone

class Simulation(Zone):

    ITEMS_NAME   = 'state_items'

    def __init__(self, named_sockets={}, **sockets):
        """ > Simulation zone

        > See <!Zone>

        ``` python
        from geonodes import *

        with GeoNodes("Demo Simulation"):

            cloud = Cloud.Points(count=100, position=Vector.Random(-5, 5))

            with Simulation(cloud=cloud, index=0) as sim_zone:

                # Current points
                cloud = sim_zone.cloud

                # Get the nearest index
                index = nd.index_of_nearest(position=nd.position).index

                # Nearest position
                nearest_pos = cloud.points.sample_index(nd.position, index=index)

                # Direction
                v = (nearest_pos - nd.position).normalize()

                #cloud.points.offset = v.normalize()*(dist-.5)/2 + Vector.Random(-.2, .2, seed=nd.scene_time.frame)
                cloud.points.offset = v*.1 + Vector.Random(-.2, .2, seed=nd.scene_time.frame)

                sim_zone.cloud = cloud

            # Result to output
            sim_zone.cloud.out()
        ```

        Arguments
        ---------
        - sockets (dict = {}) : sockets to create
        - snake_case_sockets : sockets to create
        """

        self._plug_on_exit = self.PLUG_ON_EXIT

        # ----- Create an link the input and output simulation nodes

        self.init_layout()

        self._input  = Node('GeometryNodeSimulationInput')
        self._output = Node('GeometryNodeSimulationOutput')
        self._input._bnode.pair_with_output(self._output._bnode)

        self.init_zone(named_sockets, **sockets)


# ====================================================================================================
# Reapet zone

class ForEachElement(Zone):

    ITEMS_NAME   = 'input_items'
    PLUG_ON_EXIT = False

    def __init__(self, geometry=None, selection=None, domain=None, named_sockets={}, **sockets):
        """ > For Each Element zone

        > See <!Zone>

        This loops has 3 items lists with their corresponding index:
        - input_items, active_input_index
        - main_items, active_main_index
        - generation_items, active_generation_index

        The zone initialization creates properties on the input_items.

        The output node of the zone has two subsets of sockets:
        - ***Main*** sockets
        - ***Generated*** sockets

        Sockets can be created in each subset by setting a property. They can be read once
        the block in closed:

        ``` python
        with ForEachElement() as feel:
            # Creating a socket in the main subset
            feel.main.vector = Vector()

            # Join the geometry
            feel.generated.geometry = Mesh.Cube()
        ```

        > [!NOTE]
        > It is recommended to use the `for_each` method of a domain rather than instantiate
        > the class

        ``` python
        cube = Mesh.Cube()
        with cube.faces.for_each(position=nd.position) as feel:
            pass
        ```

        Properties
        ----------
        - index (Integer) : Index socket
        - element (Geometry) : Element socket
        - main (Node like) : contains the sockets in the ***Main*** part of the output node
        - generated (Node like) : contains the sockets in the ***Generated*** part of the output node


        Arguments
        ---------
        - geometry (Geometry) : geometry to loop on
        - selection (Boolean) : element selection
        - domain (str) : domain name
        - sockets (dict = {}) : sockets to create
        - snake_case_sockets : sockets to create
        """

        self._plug_on_exit = self.PLUG_ON_EXIT

        tree = Tree.current_tree()

        # ----- Create an link the input and output simulation nodes

        self.init_layout()

        self._input  = Node('GeometryNodeForeachGeometryElementInput')
        self._output = Node('GeometryNodeForeachGeometryElementOutput')
        self._input._bnode.pair_with_output(self._output._bnode)

        if domain is not None:
            self._output._bnode.domain = domain
        self._input.geometry = geometry
        self._input.selection = selection

        self.main      = NodeItems(self._output, 'main', capture=['Geometry'])
        self.generated = NodeItems(self._output, 'generation')

        self.init_zone(named_sockets, **sockets)


# ====================================================================================================
# Loop syntax
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Root for loops
# ----------------------------------------------------------------------------------------------------

class Loop:
    def __init__(self, geometry):
        self.geometry = geometry
        self._done = False
        self._loop_var = None
        self._zone = None

    def __next__(self):

        # ---------------------------------------------------------------------------
        # Pop the zone
        # Zone is pushed in __next__
        # ---------------------------------------------------------------------------

        if self._done:            
            if self._zone is not None:
                # Geometry in locals
                locs = self._zone._locals
                locs[list(locs.keys())[0]] = self.geometry

                # Pop the zone
                self._zone.pop()

                # Geometry on zone outputs
                self.geometry._jump(self._zone._output[0])

                

            raise StopIteration

        self._done = True
        return self._loop_var
    

# ----------------------------------------------------------------------------------------------------
# Repeat loop
# ----------------------------------------------------------------------------------------------------

class RepeatLoop(Loop):
    def __init__(self, geometry, named_sockets={}, iterations=1, **sockets):
        """ Repeat loop

        ``` python
        with GeoNodes("Test"):
            g = Geometry()

            for iteration in g.repeat(Integer(10, "Loops", 0, 100)):
                g.transform(transation=.1)

            g.out()
        ```
        """
        super().__init__(geometry)
        self._zone = Repeat({'Geometry': geometry, **named_sockets}, iterations=iterations, **sockets)

    def __iter__(self):

        # ---------------------------------------------------------------------------
        # Push the zone
        # will be poped in __next__
        # ---------------------------------------------------------------------------

        self._zone.push()

        # Loop var : zone and iteration
        self._loop_var = self._zone, self._zone._input.iteration

        # The geometry becomes the second output socket
        self.geometry._jump(self._zone._input[1])

        return self

    
# ----------------------------------------------------------------------------------------------------
# For Each loop
# ----------------------------------------------------------------------------------------------------

class ForEachLoop:
    def __init__(self, geometry):
        self.geometry = geometry
        self._done = False

    def __iter__(self):
        return self

    def __next__(self):
        if self._done:
            raise StopIteration

        self._done = True
        return "Index", "Element"
    
# ----------------------------------------------------------------------------------------------------
# Simulation loop
# ----------------------------------------------------------------------------------------------------

class SimulationLoop:
    def __init__(self, geometry):
        self.geometry = geometry
        self._done = False

    def __iter__(self):
        return self

    def __next__(self):
        if self._done:
            # Stop the for-loop after one iteration
            raise StopIteration

        self._done = True
        return "delta time"


class Geometry:
    def repeat(self, n):
        return RepeatLoop(self, n)

    def for_each(self):
        return ForEachLoop(self)

    def simulation(self):
        return SimulationLoop(self)


