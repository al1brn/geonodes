#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:08:03 2023

@author: alain
"""

from geonodes.nodes.tree import GeoNodes
from geonodes.nodes.constants import current_tree
from geonodes.nodes import utils

# ====================================================================================================
# A zone

class Zone:
    def init_zone(self, create_geometry=True, **kwargs):

        # ----- Create the simulation state items
        # Geometry socket is created by default, it is first deleted

        self._items.clear()
        first = create_geometry
        for name, value in kwargs.items():

            if value is None:
                stype = 'GEOMETRY'
            else:
                stype = utils.get_value_socket_type(value)

            if create_geometry and first and stype != 'GEOMETRY':
                self._items.new(socket_type='GEOMETRY', name='Geometry')

            if stype == 'VALUE':
                stype = 'FLOAT'

            self._items.new(socket_type=stype, name=name)

            first = False

        # ----- Variables used within the with statement

        self._locals = {name: getattr(self._input, name) for name in kwargs.keys()}

        # ----- Let's active dynamic attributes
        # _closed = True  : variables point to input and output nodes
        # -close  = False : variables point to _locals dict

        self._closed = True

        # ----- Initialize the attributes

        for name, value in kwargs.items():
            setattr(self, name, value)


    def __str__(self):
        return f"<{type(self).__name__} Zone>"

    # ====================================================================================================
    # Context management

    def __enter__(self):
        self._closed = False
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._closed = True

        for name, value in self._locals.items():
            setattr(self._output, name, value)

    # ====================================================================================================
    # Dynamic attributes

    def __getattr__(self, name):

        closed = self.__dict__.get('_closed')
        if closed is not None:
            if closed:
                val = getattr(self._output, name)
            else:
                val = self._locals.get(name)
                # Trying to access fixed sockets
                if val is None:
                    val = getattr(self._input, name)

            if val is not None:
                return val

        raise AttributeError(f"{self} doesn't have input socket named '{name}'.")

    def __setattr__(self, name, value):

        if name == '_closed':
            super().__setattr__(name, value)
            return

        closed = self.__dict__.get('_closed')
        if closed is None:
            super().__setattr__(name, value)
            return

        ok = True
        if closed:
            if name in self._input.inputs.sockets_pynames().keys():
                setattr(self._input, name, value)
            else:
                ok = False
        else:
            if name in self._locals:
                self._locals[name] = value
            elif name in self._output.inputs.sockets_pynames().keys():
                setattr(self._output, name, value)
            else:
                ok = False

        if not ok:
            raise AttributeError(f"{self} has not socket named {name}!")



    def __getattr__OLD(self, name):

        closed = self.__dict__.get('_closed')
        if closed is not None:
            node = self.__dict__.get("_output") if closed else self.__dict__.get("_input")
            if node is not None:
                return getattr(node, name)

        raise AttributeError(f"{self} doesn't have input socket named '{name}'.")

    def __setattr__OLD(self, name, value):

        if name == '_closed':
            super().__setattr__(name, value)

        closed = self.__dict__.get('_closed')
        if closed is not None:
            node = self.__dict__.get("_input") if closed else self.__dict__.get("_output")
            if node is not None:
                setattr(node, name, value)
                return
        super().__setattr__(name, value)



# ====================================================================================================
# Reapet zone

class Repeat(Zone):

    def __init__(self, iterations=1, **kwargs):

        tree = current_tree()

        # ----- Create an link the input and output simulation nodes

        self._input  = tree.RepeatInput()
        self._output = tree.RepeatOutput()
        self._input.bnode.pair_with_output(self._output.bnode)

        if True:
            self.init_zone(create_geometry=True, **kwargs)
            self._input.iterations = iterations

        else:

            # ----- Create the simulation state items
            # Geometry socket is created by default, it is first deleted

            self._output.bnode.repeat_items.clear()
            for name, value in kwargs.items():

                if value is None:
                    raise AttributeError(f"Repeat initialization error: argument '{name}' must not be None.")
                else:
                    stype = utils.get_value_socket_type(value)

                self._output.bnode.repeat_items.new(socket_type=stype, name=name)

            self._closed = False

            # ----- Initialize the attributes

            self._input.iterations = iterations

            for name, value in kwargs.items():
                setattr(self, name, value)

    @property
    def _items(self):
        return self._output.bnode.repeat_items



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

        tree = current_tree()

        # ----- Create an link the input and output simulation nodes

        self._input  = tree.SimulationInput()
        self._output = tree.SimulationOutput()
        self._input.bnode.pair_with_output(self._output.bnode)


        if True:
            self.init_zone(create_geometry=True, **kwargs)

        else:

            # ----- Create the simulation state items
            # Geometry socket is created by default, it is first deleted

            self._output.bnode.state_items.clear()
            first = True
            for name, value in kwargs.items():

                if value is None:
                    if first:
                        stype = 'GEOMETRY'
                    else:
                        raise AttributeError(f"Simulation initialization error: argument '{name}' must not be None.")
                else:
                    stype = utils.get_value_socket_type(value)


                if first and stype != 'GEOMETRY':
                    self._output.bnode.state_items.new(socket_type='GEOMETRY', name='Geometry')

                self._output.bnode.state_items.new(socket_type=stype, name=name)

                first = False

            self._closed = True

            # ----- Initialize the attributes

            for name, value in kwargs.items():
                setattr(self, name, value)

    @property
    def _items(self):
        return self._output.bnode.state_items

    # ====================================================================================================
    # Create paths for trajectories

    @classmethod
    def Trajectories(cls, simulation, count=10):
        """ This constructor build a simulation zone building curves tracking points of another simulation zone.

        Args:
            - simulation (Simulation) : the simulation zone having a geometry of type Points
            - count (int=10) : the number of frames to use for tracking
        Returns:
            - simulation with curves attribute
        """

        import geonodes as gn

        tree = gn.Tree.TREE

        with tree.layout("POINTS TRAJECTORIES", color='UTIL'):

            # ----- Points from the other simulation
            # CAUTION: input of INPUT node
            cloud = gn.Points(simulation.input.inputs[0].connected_sockets()[0])

            # ----- One spline per point
            with tree.layout("One spline instance per point", color='UTIL'):
                curve = gn.Curve.Line(start=0, end=0).resample(count=count)
                insts = cloud.instance_on_points(instance=curve)
                curves = gn.Curve(insts.realize())

            #----- Simulation

            with cls(curves=curves) as simul:

                # ----- Points from the other simulation
                # CAUTION: input of OUTPUT node
                cur_cloud = gn.Points(simulation.output.outputs[0])
                pts = simul.curves.points

                # ----- Shift splines points position

                with tree.layout("Shift points position", color='UTIL'):
                    pts.position = pts.sample_index(pts, pts.position, index=pts.index + 1)

                # ----- Points new positions

                with tree.layout("Update position of last points", color='UTIL'):
                    pts[(pts.index % count).equal(count-1)].position = pts.sample_index(cur_cloud.points, cur_cloud.points.position, index=simul.curves.splines.index.capture())

        return simul


    # ====================================================================================================
    # Fluid simulation

    @classmethod
    def Fluid(cls, cloud, velocity=0, life=50, setup={}, acceleration={}, finish={}):
        """ Constructor building a basic simulation zone for fluid simulation.

        **Note**: the name of the geometry is '*cloud*'. Use ``` simul.cloud ``` to access to the points animated by the simulation.

        The nodes generated perform the standard operations:
        - add new points at each step
        - delete points older thant the life parameter
        - update the velocity with the acceleration
        - update the particles position with the updated velocity

        The acceleration nodes are generated through functions passed as argument.
        An template of the acceleration function must be:

        ``` python
        def gen(simul):
        ```

        The following example build a simple simulation from a mesh, with random initial speed and a gravity.

        ``` python
        import geonodes as gn

        with gn.Tree("Fluid", auto_capture=False) as tree:

            # Input geometry is supposed to be a mesh

            mesh = gn.Mesh(tree.ig)

            # Generate points on the surface

            points = mesh.faces.distribute_points(10).points

            # Random speed

            velocity = gn.Vector.Random((-1, -1, -1), (1, 1, 1), seed=tree.frame)

            # Fluid simulation with gravity

            simul = gn.Simulation.Fluid(points, velocity, 50,
                acceleration=gn.Simulation.func_gravity((0, 0, -10)),
                )

            tree.og = mesh + simul.cloud
        ```

        Simulation offers basic acceleration functions:
        - func_gravity      : constant acceleration
        - func_turbulence   : noisy acceleration
        - func_viscosity    : acceleration decreasing the speed
        - func_repulsion    : repulsion from the nearest particle
        - func_attraction   : attraction / repulsion from a location
        - func_surface_flow : acceleration along a surface slope
        - func_bounce       : bounce on a surface
        - func_group        : use a custom group to perform computations inside the simulation loop

        Custom nodes can be added at the begining and at the end of the simulation step with the arguments **setup** and **finish**.

        The same process is used to generate complementory nodes for the set up and the finalization of the zone.

        For instance, the following simulation simulates a fluid flowing on a surface:

        ``` python
        import geonodes as gn

        with gn.Tree("Flow", auto_capture=False) as tree:

            # The surface on which fluid will flow

            mesh = gn.Mesh(tree.ig)

            # Particles generation with null initial speed

            points   = mesh.faces.distribute_points(density=.1, seed=tree.frame).points
            velocity = gn.Vector()

            # Simulation with flow with viscosity and repulsion
            # Finish by making sure the particles stay on the surface and killing outside particles

            simul = gn.Simulation.Fluid(points, velocity, 30,
                acceleration={
                'flow'      : gn.Simulation.func_surface_flow(mesh, gravity=(0, 0, -10)),
                'viscosity' : gn.Simulation.func_viscosity(.2),
                'repulsion' : gn.Simulation.func_repulsion(.2),
                },
                finish = {
                'stick'     : gn.Simulation.func_stick_on_surface(mesh, kill_outside=True),
                }
            )

            # Mesh and particles

            tree.og = mesh + simul.cloud
        ```

        Args:
            - cloud (Points): the points generated at each steap
            - velocity (Vector) : the points velocity
            - life (Integer) : particles life
            - setup (dict or function) : function generating setup nodes or dict of such functions
            - acceleration (dict or function) : function generating acceleration nodes or dict of such functions
            - finish (dict or function) : function generating finalization nodes or dict of such functions
        """

        import geonodes as gn

        tree = cloud.node.tree

        # ----------------------------------------------------------------------------------------------------
        # Simulation zone

        cloud.points.store_named_vector("velocity", velocity)
        cloud.points.store_named_integer("age", 0)

        with cls(cloud=cloud) as simul:

            # ----- Set up

            if isinstance(setup, dict):
                for stu_name, stu in setup.items():
                    with tree.layout(f"Set up: {stu_name}"):
                        stu(simul=simul) #   , cloud=simul.cloud, velocity=s_velocity, age=s_age)

            else:
                with tree.layout(f"Set up"):
                    setup(simul=simul)  #, cloud=simul.cloud, velocity=s_velocity, age=s_age)

            # ----- Update the age, remove old particles

            with tree.layout("Update the age and remove old particles"):

                age = simul.cloud.named_integer("age") + 1
                simul.cloud.points.store_named_integer("age", age)
                simul.cloud.points[age.greater_than(life)].delete()

            # ----- New points with random velocity

            with tree.layout("Create new points with their velocity"):
                simul.cloud = gn.Points(simul.cloud + cloud)

            # ----- Accelerations

            if isinstance(acceleration, dict):
                a = gn.Vector((0, 0, 0))
                for acc_name, acc in acceleration.items():
                    with tree.layout(f"Acceleration: {acc_name}"):
                        a += acc(simul=simul)

            else:
                with tree.layout(f"Acceleration"):
                    a = acceleration(simul=simul)

            # ----- Update velocities and postions

            with tree.layout("Update velocity and positions"):
                vel     = simul.cloud.points.named_vector("velocity")
                new_vel = vel + a.scale(simul.delta_time)
                simul.cloud.points.position_offset = (vel + new_vel).scale(simul.delta_time/2)
                simul.cloud.points.store_named_vector("velocity", new_vel)

            # ----- Finishing

            if isinstance(finish, dict):
                for fin_name, fin in finish.items():
                    with tree.layout(f"Finish: {fin_name}"):
                        fin(simul=simul)

            else:
                with tree.layout(f"Finish"):
                    finish(simul=simul)

        return simul

    # ====================================================================================================
    # Accelerations

    # ----------------------------------------------------------------------------------------------------
    # A constant acceleration

    @staticmethod
    def func_gravity(gravity=(0, 0, -10)):
        """ Returns a function which builds a constant acceleration.

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_gravity(...))
        ```

        or, if more than one acceleration function is required

        ``` python
        simul = gn.Simulation.Fluid(acceleration={'gravity': gn.Simulation.func_gravity(...)})
        ```

        Args:
            - gravity (Vector) : the gravity vector

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        return lambda simul: gn.Vector(gravity)

    # ----------------------------------------------------------------------------------------------------
    # Noisy turbulence

    @staticmethod
    def func_turbulence(intensity=1, scale=.2, offset=(0, 0, 0), w=0.):
        """ Returns a function which builds a turbulencce for acceleration.

        The turbulence makes use of a 'Noise 4D' texture initialized with the function arguments.

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_turbulence(...))
        ```

        or, if more than one acceleration function is required

        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'   : gn.Simulation.func_gravity(),
            'turbulence': gn.Simulation.func_turbulence(...),
            })
        ```

        Args:
            - intensity (Float) : intensity of the turbulence
            - scale (Float) : scale of Noise node
            - offset (Vector) : offset to apply in the 'Vector' socket of the noise node
            - w (Float) : value of the 'W' socket of the noise node

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        def gen(simul):
            cloud = simul.cloud
            tree = cloud.node.tree
            return gn.Vector(gn.Texture.Noise4D(vector=cloud.points.position + offset, scale=scale, w=w).color).map_range(.5).scale(intensity)

        return gen

    # ----------------------------------------------------------------------------------------------------
    # Viscosity

    @staticmethod
    def func_viscosity(intensity=1, exponent=2):
        """ Returns a function which builds an acceleration simulating viscosity.

        The viscosity is a function of the velocity: ``` acc = -intensitty * speed**exponent ```

        This raw formula can return an acceleration which accelerates the particle in the other direction.
        To avoid this behavior, the acceleration norm is capped to ``` speed/delta_time ```.

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_viscosity(...))
        ```

        or, if more than one acceleration function is required

        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'   : gn.Simulation.func_gravity(),
            'viscosity' : gn.Simulation.func_viscosity(...),
            })
        ```

        Args:
            - intensity (Float) : intensity of the viscosity
            - exponent (Float) : exponent parameter of the acceleration

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        def gen(simul):

            velocity = simul.cloud.points.named_vector("velocity")

            # ----- Velocity norm

            n_vel = velocity.length

            # ----- acceleration norm

            a = intensity*n_vel**exponent

            # ----- Cap and smooth the viscosity

            a_max = n_vel/simul.delta_time
            a = a.map_range_smooth(0, a_max, 0, a_max)

            # ----- Return the acceleration

            return velocity.scale(-a/n_vel)

        return gen

    # ----------------------------------------------------------------------------------------------------
    # Repulsion

    @staticmethod
    def func_repulsion(intensity=1, exponent=2, d_min=.1, d_max=1):
        """ Returns a function which builds a repulstion acceleration with the nearest particle.

        The repulsion is base on the vector between the particle and its nearest neighbor.
        The acceleration is computed with the formula: ``` a = intensity * distance**(-exponent) ```

        To avoid division by zero, distance is minimized by the argument d_min.
        The repulsion is null when the distance is greater thant d_max

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_repulsion(...))
        ```

        or, if more than one acceleration function is required

        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'   : gn.Simulation.func_gravity(),
            'repulsion' : gn.Simulation.func_repulsion(...),
            })
        ```

        Args:
            - intensity (Float) : intensity of the repulstion
            - exponent (Float) : exponent parameter of the acceleration
            - d_min (Float) : minimum distance to avoid infinite acceleration
            - d_max (Float) : repulsion maximum distance

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        def gen(simul):

            cloud = simul.cloud

            # ----- Index of nearest

            index = cloud.points.index_of_nearest(position=cloud.points.index).index

            # ----- Vector between the particle and its nearest neighbor

            v = cloud.points.position - cloud.points.sample_index(cloud.points.position, index=index)

            # ----- Distance

            d = v.length

            # ----- Acceleration computed on the capped distance

            base = gn.max(d, d_min)
            a = -intensity*base**(-exponent)

            # ----- Return the acceleration

            return v.scale(a/d)

        return gen

    # ----------------------------------------------------------------------------------------------------
    # Attraction from a location

    @staticmethod
    def func_attraction(location=(0, 0, 0), intensity=10, exponent=-2, d_min=.2):
        """ Returns a function which builds an attraction acceleration towards the given location.

        The attraction can be used to simulate Newton gravity law with ``` exponent = -2```.

        The acceleration is computed with ``` a = intensity / distance**exponent ```

        To avoid infinite accelerations, the distance is minimized with d_min.

        Note that if the intensity is negative, the attractor becomes a repulsor!

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_attraction(...))
        ```

        or, if more than one acceleration function is required

        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'    : gn.Simulation.func_gravity(),
            'attraction' : gn.Simulation.func_attraction(...),
            })
        ```

        Args:
            - location (Vector) : location of the attractor
            - intensity (Float) : intensity of the attraction
            - exponent (Float) : exponent parameter of the acceleration
            - d_min (Float) : minimum distance to avoid infinite accelerations

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        def gen(simul):

            cloud = simul.cloud

            # ----- Vector to the attractor location

            v = location - cloud.points.position

            # ----- Minimum distance to the attractor

            d = v.length
            l = d.switch(d.less_than(d_min), d_min)

            # ----- Acceleration norm

            a = intensity*l**exponent

            # ----- Return the acceleration

            return v.scale(a/d)

        return gen

    # ====================================================================================================
    # Surface interaction

    # ----------------------------------------------------------------------------------------------------
    # Stick the particle on to the surface

    @staticmethod
    def func_stick_on_surface(mesh, kill_outside=False, z_max=50):
        """ Returns a function building nodes which place the particles on the surface.

        The algorithm using the raycats node to project the particles onto the surface, ```z_max``` is the latitude from which to project the particles.

        if particles are outside the surface, they can be deleted if kiil_outside is True.

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(finish=gn.Simulation.func_stick_on_surface(...))
        ```

        or, if more than one finish function is required

        ``` python
        simul = gn.Simulation.Fluid(finish={
            'stick' : gn.Simulation.func_stick_on_surface(...),
            })
        ```

        Args:
            - mesh (Mesh) : the surface
            - kill_outside (bool) : delete or not the particles outside the surface
            - z_max (float) : the altitude higher that the surface to raycast from

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        def gen(simul):

            cloud = simul.cloud

            # ----- Location to raycast from

            loc = cloud.points.position
            loc.z = z_max

            # ------ Raycast to the surface from the points locations

            node = cloud.points.raycast(target_geometry=mesh, source_position=loc, ray_length=2*z_max)

            # ----- Locate the where we have a hit

            cloud.points[node.is_hit].position = node.hit_position

            # ----- Delete the particles outside the surface

            if kill_outside:
                cloud.points[node.is_hit.b_not()].delete()

        return gen

    # ----------------------------------------------------------------------------------------------------
    # Acceleration along the slope

    @staticmethod
    def func_surface_flow(mesh, gravity=(0, 0, -10)):
        """ Returns a function which builds an acceleration following the surface slope.

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_surface_flow(...))
        ```

        or, if more than one acceleration function is required

        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'viscosity'  : gn.Simulation.func_viscosity(),
            'flow'       : gn.Simulation.func_surface_flow(...),
            })
        ```

        Args:
            - mesh (Mesh)       : the surface
            - gravity (Vector)  : gravity vector
            - intensity (Float) : intensity of the attraction
            - exponent (Float) : exponent parameter of the acceleration
            - d_min (Float) : minimum distance to avoid infinite accelerations

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        g = gn.Vector(gravity)

        def gen(simul):

            cloud = simul.cloud

            # ----- Get the normal at each point

            index  = simul.cloud.points.sample_nearest(mesh.faces)
            normal = simul.cloud.points.sample_index(mesh.faces, value=mesh.normal, index=index)

            # ----- Gravity component

            return normal.cross(g).cross(normal)

        return gen

    # ----------------------------------------------------------------------------------------------------
    # Bounce on the surface of an object

    @staticmethod
    def func_bounce(mesh, distance=.1, damp=0.):
        """ Returns a function creating a bounce simulation onto a mesh.

        The created nodes test if the points are below the closest surface. If it is the case,
        it places the points on the external side of the face an reflect the speed with the normal to thge surface.

        The function returned by this method can be used as the setpt argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(setup=gn.Simulation.func_bounce(...))


        Args:
            - mesh (Mesh)       : the surface
            - distance (float)  : distance from the surface
            - damp (float)      : damp factor

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        def gen(simul):

            cloud = simul.cloud

            velocity = cloud.points.named_vector("velocity")

            prox_node = cloud.points.proximity(target=mesh, source_position=cloud.points.position)
            v = prox_node.position - cloud.points.position

            rc_node = cloud.points.raycast(
                target_geometry  = mesh,
                source_position  = cloud.points.position,
                ray_direction    = v,
                ray_length       = 5*distance)

            sel = rc_node.is_hit * rc_node.hit_normal.dot(velocity).less_than(0)

            cloud.points.store_named_attribute("temp_sel", sel)
            sel = cloud.points.named_boolean("temp_sel")

            cloud.points[sel].position = rc_node.hit_position + rc_node.hit_normal.scale(distance)

            if True:
                cloud.points[sel].store_named_attribute("velocity", velocity.reflect(rc_node.hit_normal).scale(1-damp))
                simul.cloud = cloud
            else:
                new_vel = velocity.switch(sel, velocity.reflect(rc_node.hit_normal).scale(1-damp))
                cloud.points.store_named_attribute("velocity", new_vel)

        return gen

    # ----------------------------------------------------------------------------------------------------
    # Generation function calling a group

    @staticmethod
    def func_group(group_name, in_delta_time=None, in_cloud=None, out_cloud=None, out_socket=None):
        """ Returns a function creating a Group node of the given name and connect sockets.

        The Group can have input sockets for delta_time and cloud used in a fluid simulation.
        It can have an output sockets for cloud if the cloud has been changed.

        An additional output socket can be specified if the node must return a value such as an acceleration.

        If the sockets exist with this name, they will be connected automatically. If they have differente names,
        they must be provided using in_... and out_... arguments, for instance:
        - ``` in_cloud = None ``` : the cloud will be plugged to the input socket named 'cloud', 'points' or 'geometry' if it exists
        - ``` out_cloud = 'geometry' ``` : the cloud will be plugged to the input socket named 'vector'

        The same is done for the output socket: variables are updated to match to the corresponding outpout sockets.

        If the out_socket argument is not node, the generated function return the correspondint outpout socket of the group node.

        The function returned by this method can be used as an argument in a simulation zone creation method:

        ``` python
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_group("Custom Acceleration", out_socket='acceleration())
        ```

        Args:
            - group_name (string) : the name of the Group node
            - out_socket (str=None) : name of the output socket of the created group node to return
            - in_delta_time (str=None) : nema of the *delta time* input socket
            - in_cloud (str=None) : nema of the *cloud* input socket
            - in_velocity (str=None) : nema of the *velocity* input socket
            - in_age (str=None) : nema of the *age* input socket
            - out_cloud (str=None) : nema of the *cloud* output socket
            - out_velocity (str=None) : nema of the *velocity* output socket
            - out_age (str=None) : nema of the *age* output socket

        Returns:
            - function(**kwargs) : nodes generator
        """

        import geonodes as gn

        def gen(simul):

            cloud = simul.cloud

            # ----- Generate the group

            node = gn.Group(group_name)

            # ----- Input socket names

            in_d = in_delta_time
            in_c = in_cloud

            if in_d is None:
                if 'delta_time' in node.insockets.keys():
                    in_d = 'delta_time'
            if in_c is None:
                if 'cloud' in node.insockets.keys():
                    in_c = 'cloud'
                elif 'points' in node.insockets.keys():
                    in_c = 'points'
                elif 'geometry' in node.insockets.keys():
                    in_c = 'geometry'

            # ----- Connect the input sockets

            if in_d is not None:
                setattr(node, in_d, simul.delta_time)
            if in_c is not None:
                setattr(node, in_c, cloud)

            # ----- Output socket names

            out_c = out_cloud

            if out_c is None:
                if 'cloud' in node.outsockets.keys():
                    out_c = 'cloud'
                elif 'points' in node.outsockets.keys():
                    out_c = 'points'
                elif 'geometry' in node.outsockets.keys():
                    out_c = 'geometry'

            # ----- Connect the output sockets
            # Make the data sockets pointing to the outpout sockets of the node
            # using the stack method

            if out_c is not None:
                cloud.stack(node, out_c)

            simul.cloud = cloud

            # ----- Return the output socket if a name is given

            if out_socket is not None:
                return getattr(node, out_socket)
            else:
                return None

        return gen
