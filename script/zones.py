#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : zones
--------------
- Implements couples of nodes forming a zone : Simulation or Repeat

Zone arguments are set / get from one of the two nodes depending on the 'closed' status:
    - closed :
        - arguments are set to the input sockets of the INPUT node
        - arguments are get from the output sockets of the OUTPUT node
    - not closed
        - arguments are set to the input sockets of the OUTPUT node
        - arguments are get from the output sockets of the INPUT node

The closed parameter is managed through context management:

``` python
with Repeat(geometry=None, offset=(1, 2, 3), index=0, iteration=10) as repeat_block:

    repeat_block.geometry.offset = repeat_block.offset # Set Position Offset
    repeat_block.geometry = repeat_block.geometry.join(other_geometry)

    repeat_block.index += 1

repeat_block.geometry.to_output()
```

classes
-------
- IntFloat      : Base class for Integer and Float
- Integer       : DataSocket of type 'INT'
- Float         : DataSocket of type 'FLOAT'

functions
---------

updates
-------
- creation : 2024/07/23
"""


from .scripterror import NodeError
from . import utils
from .treeclass import Tree, Node

# ====================================================================================================
# A zone

class Zone:
    def init_zone(self, create_geometry=True, **kwargs):

        # ---- Add initial Geometry socket if necessary

        if create_geometry and 'geometry' not in kwargs.keys():
            all_sockets = {'Geometry': None, **kwargs}
        else:
            all_sockets = kwargs

        # ----- Create the simulation state items

        self._items.clear()
        for name, value in all_sockets.items():

            if value is None:
                input_type = 'GEOMETRY'
            else:
                input_type = utils.get_input_type(value)

            self._items.new(socket_type=input_type, name=name)

            self._input.plug_value_into_socket(value, self._input.in_socket(name))

        # ----- Variables used within the with statement

        self._locals = {name: self._input.out_socket(name) for name in kwargs.keys()}

        # ----- Ensure the proper sub class of geometries

        for k in self._locals.keys():
            geo = self._locals[k]
            if geo.SOCKET_TYPE == 'GEOMETRY':
                if all_sockets[k] is not None:
                    self._locals[k] = type(all_sockets[k])(geo)

        # ----- Let's active dynamic attributes
        # _closed = True  : variables point to input and output nodes
        # _closed = False : variables point to _locals dict

        self._closed = True

    def __str__(self):
        return f"<{type(self).__name__} Zone, loop variables: {list(self._locals.keys())}>"

    # ====================================================================================================
    # Context management

    def __enter__(self):
        self._closed = False
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._closed = True

        for name, value in self._locals.items():
            self._output.plug_value_into_socket(value, self._output.in_socket(name))

    # ====================================================================================================
    # Dynamic attributes

    def __getattr__(self, name):

        closed = self.__dict__.get('_closed')
        if closed is not None:
            if closed:
                val = self._output.out_socket(name)
                # Ensure proper geometry type
                loc_val = self._locals.get(name)
                if loc_val is not None and loc_val.SOCKET_TYPE == 'GEOMETRY':
                    val = type(loc_val)(val)
            else:
                val = self._locals.get(name)
                # Trying to access fixed sockets (such as 'Delta Time')
                if val is None:
                    val = self._input.out_socket(name)

            if val is not None:
                return val

        raise NodeError(f"{self} doesn't have input socket named '{name}'.")

    def __setattr__(self, name, value):

        if name == '_closed':
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
            self._output.plug_value_into_socket(value, name)


# ====================================================================================================
# Reapet zone

class Repeat(Zone):

    def __init__(self, iterations=1, **kwargs):

        tree = Tree.current_tree

        # ----- Create an link the input and output simulation nodes

        self._input  = Node('GeometryNodeRepeatInput')
        self._output = Node('GeometryNodeRepeatOutput')
        self._input._bnode.pair_with_output(self._output._bnode)

        self.init_zone(create_geometry=True, **kwargs)
        self._input.iterations = iterations

    @property
    def _items(self):
        return self._output._bnode.repeat_items


# ====================================================================================================
# Simulation zone

class Simulation(Zone):
    """ > Create a simulation zone**

    This class Simulation generates the two nodes of a simulation zone: simulation input and output nodes.
    The simulation exposes as class attributes the geometry and the simulation variables used in the simulation zone.

    The key of the keyword arguments is used to name the sockets of the input and output node.

    ``` python
    simul = Simulation(geometry=mesh, speed=(0, 0, 0))
    simul.geometry  # The geometry within the simulation zone
    simul.speed     # The speed within the simulation zone
    ```

    When the simulation loop is terminated, the changes on the simulation variables must be connected to
    the output nodes : ` simul.output.geometry = simul.geometry `. This is done automatically with the 'close' method :

    ``` python
    simul = Simulation(geometry=mesh, speed=(0, 0, 0))
    simul.geometry.faces.shade_smooth = True
    simul.speed += (0, 0, 1)
    simul.close()
    ```

    Bettter use the context manager through a `with` statement:

    ``` python
    with gn.Simulation(geometry=mesh, speed=(0, 0, 0)) as simul:
        simul.geometry.faces.shade_smooth = True
        simul.speed += (0, 0, 1)
    ```

    Once the simulation is closed, the variables are the output sockets of the simulation output node.
    They can be used to get the result of a simulation step:

    ``` python
    with gn.Simulation(geometry=mesh) as simul:
        # simul.geometry refers to the geometry inside the simulation zone
        simul.geometry.faces.shade_smooth = True

    # Outside the simulation zone, the geometry refers to the result of the simulation
    # Let's connect the result of the simulation to the output of the tree
    tree.og = simul.geometry
    ```

    ### A working demo:

    ``` python
    from geonodes.nodes import GeoNodes

    with GeoNodes("Simulation demo") as tree:

        with tree.Simulation(tree.ig) as simul:
            simul.geometry.VERTS.set_position(offset = tree.Random(-1, 1, seed=tree.frame).scale(.1))

    tree.og = simul.geometry
    ```

    Args:
    - **kwargs : variables to use within the loop. Each key word creates a variable accessible within the simulation step
      and, once the simulation closed, as the result of the simulation.
    """

    def __init__(self, **kwargs):

        # ----- Create an link the input and output simulation nodes

        self._input  = Node('GeometryNodeSimulationInput')
        self._output = Node('GeometryNodeSimulationOutput')
        self._input._bnode.pair_with_output(self._output._bnode)


        self.init_zone(create_geometry=True, **kwargs)

    @property
    def _items(self):
        return self._output._bnode.state_items
