#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:08:03 2023

@author: alain
"""

#from geonodes.core.socket import DataSocket
#from geonodes.core.node import Node
#from geonodes.core.tree import Tree

from geonodes.nodes import nodes

# ====================================================================================================
# Simulation zone

class Simulation:
    """ Simulation zone
    
    This class Simulation generates two nodes: the simulation input and output nodes.
    
    Arguments are named sockets for the state items.
    Sockets are exposed in Simulation class with the names of the arguments, for instance:
        
        simul = Simulation(geometry=mesh, speed=(0, 0, 0))
        geo = simul.geometry  # Get the output socket 'Geometry' from the simulation input node
        speed = simul.speed
        # Some changes in geo and speed
        simul.geometry = geo # Set the input socket Geometry of the output simulation node
        simul.speed = speed
        
    To get the resulting values, read the socket from out node
        tree.og = simul.out_node.geometry   
    """
    
    def __init__(self, geometry, **kwargs):
        
        import geonodes as gn
        
        # ----- Create an link the input and output simulation nodes
        
        self.input  = nodes.SimulationInput()
        self.output = nodes.SimulationOutput()
        self.input.bnode.pair_with_output(self.output.bnode)
        
        # ----- Create the simulation state items
        
        for name, value in kwargs.items():
            if isinstance(value, bool):
                socket = gn.Boolean(value)
            elif isinstance(value, int):
                socket = gn.Integer(value)
            elif isinstance(value, float):
                socket = gn.Float(value)
            elif isinstance(value, str):
                socket = gn.String(value)
            elif isinstance(value, tuple):
                socket = gn.Vector(value)
            else:
                socket = value
                
            self.output.bnode.state_items.new(socket_type=socket.base_data_type, name=name.capitalize())
            
        # ----- Update in and out sockets dynamically created
        
        self.input.update_inout_sockets()
        self.output.update_inout_sockets()
        
        # ----- Plug the values to the simulation input node
        
        self.input.set_input_socket('geometry', geometry)
        for name, value in kwargs.items():
            self.input.set_input_socket(name.lower(), value)
            
        # ----- Create the output values of the simulation
        
        for socket in self.output.outputs:
            name = socket.name.lower()
            # Geometry is already initialized
            if name != 'geometry':
                setattr(self.output, socket.name.lower(), socket)
                
        # ----- Geometry class
        
        self.input.outsockets_classes['geometry']  = type(geometry)
        self.output.outsockets_classes['geometry'] = type(geometry)
                
        # ----- Short cuts
        
        self.output_geometry = self.output.geometry
        self.og = self.output.geometry
            
    def __str__(self):
        vs = list(self.input.insockets.keys())
        vs[0] += f" ({self.output.outsockets_classes['geometry'].__name__})"
        s = ", ".join(vs)
        return f"<Simulation zone: {s}>"

    def __getattr__(self, name):
        if name in ('input' 'output'):
            return super().__setattr__(name, {})

        elif name in self.input.outsockets.keys():
            return self.input.get_output_socket(name)
        
        else:
            raise AttributeError(f"Simulation: Unknown attribute name {name}")
            
    def __setattr__(self, name, value):

        if name in ('input', 'output'):
            super().__setattr__(name, value)
            
        elif name in self.output.insockets.keys():
            self.output.set_input_socket(name, value)
            
        elif name == 'delta_time':
            raise AttributeError("Simulation: the property 'delta_time' is read only")

        else:
            super().__setattr__(name, value)
            
    # ----------------------------------------------------------------------------------------------------
    # Create paths for trajectories
    
    @classmethod
    def Trajectories(cls, simul, count=10):
        """ This constructor build a simulation zone building curves tracking points of another simulation zone.
        
        Args:
            - simul (Simulation) : the simulation zone having a geometry of type Points
            - count (int=10) : the number of frames to use for tracking
        """
        
        import geonodes as gn
        
        tree = gn.Tree.TREE
        
        with tree.layout("POINTS TRAJECTORIES"):
            
            # ----- Points connected to the input socket Geometry of the simulation input node
            init_points = gn.Points(simul.input.inputs[0].connected_sockets()[0])
            
            # ----- Points connected to the input socket Geometry of the simulation output node
            # These points have the final position
            
            points = gn.Points(simul.output.inputs[0].connected_sockets()[0])

            with tree.layout("One spline instance per point"):
                curve = gn.Curve.Line(start=0, end=0).resample(count=count)
                insts = init_points.instance_on_points(instance=curve)
                insts.insts.store_named_attribute(name="temp", value=(0, 0, 0))
                
                splines = insts.realize()
                
            with tree.layout("Curves simulation"):
        
                sim = gn.Simulation(geometry=splines, instances=insts)
                
                # ----- Shift splines points position
                
                splines = sim.geometry
                with tree.layout("Shift points position"):
                    old_locs = splines.points.sample_index(value=splines.points.position, index=splines.points.index + 1)
                    splines.points.position = old_locs
        
                # ----- Points new positions
                    
                with tree.layout("Update position of last points"):
                    
                    #pts = gn.Points(simul.geometry)
                    
                    locs = points.points.sample_index(value=points.points.position)
                    insts = sim.instances
                    insts.insts.store_named_attribute(name="temp", value=locs)
                    
                    curve = insts.realize()
                    locs = curve.points.sample_index(value=curve.points.named_vector("temp"))
                    
                    splines.points[(splines.points.index % count).to_integer().equal(count-1)].position = locs
                    
                # ----- Update simulation variables
        
                sim.instances = insts
                sim.geometry = splines
        
            
            return sim
        
    # ====================================================================================================
    # Fluid simulation
    
    @classmethod
    def Fluid(cls, points, velocity, life, setup={}, acceleration={}, finish={}):
        """ Constructor building a basic simulation zone for fluid simulation.
        
        The nodes generated perform the standard operations:
        - add new points at each step
        - delete points older thant the life parameter
        - update the velocity with the acceleration
        - update the particles position with the updated velocity
            
        The acceleration nodes are generated through functions passed as argument.
        An template of the acceleration function must be:
            
        ``` python
        def gen(simul=None, points=None, velocity=None, age=None):
        ```
        
        Or use ``` **kwargs ``` for arguments which are not used for generation, for instance:

        ``` python
        def gen(simul=None, velocity=None, **kwargs):
            
            # An acceleration opposed to velocity
            
            return -velocity/simul.delta_time/3            
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
            
            tree.og = mesh + simul.og    
        ```
        
        Simulation offers basic acceleration functions:
        - func_gravity      : constant acceleration
        - func_turbulence   : noisy acceleration
        - func_viscosity    : acceleration decreasing the speed
        - func_repulsion    : repulsion from the nearest particle
        - func_attraction   : attraction / repulsion from a location
        - func_surface_flow : acceleration along a surface slope
            
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
            
            tree.og = mesh + simul.og
        ```
        
        Args:
            - points (Points): the points generated at each steap
            - velocity (Vector) : the points velocity
            - life (Integer) : particles life
            - setup (dict or function) : function generating setup nodes or dict of such functions
            - acceleration (dict or function) : function generating acceleration nodes or dict of such functions
            - finish (dict or function) : function generating finalization nodes or dict of such functions
        """
        
        import geonodes as gn
        
        tree = points.node.tree
        
        # ----------------------------------------------------------------------------------------------------
        # Simulation step
            
        simul = cls(geometry=points, velocity=velocity, age=0)
        
        # ----- Get the variables
        
        s_points   = simul.geometry
        s_velocity = simul.velocity
        s_age      = simul.age
        
        # ----- Set up
        
        if isinstance(setup, dict):
            for stu_name, stu in setup.items():
                with tree.layout(f"Set up: {stu_name}"):
                    stu(simul=simul, points=s_points, velocity=s_velocity, age=s_age)
                    
        else:
            with tree.layout(f"Set up"):
                setup(simul=simul, points=s_points, velocity=s_velocity, age=s_age)
        
        # ----- Update the age, remove old particles
        
        with tree.layout("Update the age and remove old particles"):
    
            s_age += 1
            
            new_age = s_points.points.capture_attribute(0)
            s_age += new_age
    
            s_points.points[s_age.greater_than(life)].delete()
            
        # ----- New points with random velocity
            
        with tree.layout("Create new points with random velocity"):
            
            new_vel = s_points.points.capture_attribute(velocity)
            s_points  = gn.Points(s_points + points)
            s_velocity += new_vel
    
        # ----- Accelerations
            
        if isinstance(acceleration, dict):
            a = gn.Vector((0, 0, 0))
            for acc_name, acc in acceleration.items():
                with tree.layout(f"Acceleration: {acc_name}"):
                    a += acc(simul=simul, points=s_points, velocity=s_velocity, age=s_age)
                    
        else:
            with tree.layout(f"Acceleration"):
                a = acceleration(simul=simul, points=s_points, velocity=s_velocity, age=s_age)
    
        # ----- Update velocities and postions
                
        with tree.layout("Update velocity and positions"):
            
            new_velocity = s_velocity + a.scale(simul.delta_time)
            s_points.points.position_offset = (s_velocity + new_velocity).scale(simul.delta_time/2)
            s_velocity = new_velocity
            
        # ----- Finishing
        
        if isinstance(finish, dict):
            for fin_name, fin in finish.items():
                with tree.layout(f"Finish: {fin_name}"):
                    fin(simul=simul, points=s_points, velocity=s_velocity, age=s_age)
                    
        else:
            with tree.layout(f"Finish"):
                finish(simul=simul, points=s_points, velocity=s_velocity, age=s_age)
        
        # ----- Update the variables
        
        simul.geometry = s_points
        simul.velocity = s_velocity
        simul.age      = s_age
        
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
        
        return lambda **kwargs: gn.Vector(gravity)
    
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
        
        def gen(points=None, **kwargs):
            tree = points.node.tree
            return gn.Vector(gn.Texture.Noise4D(vector=points.points.position + offset, scale=scale, w=w).color).map_range(.5).scale(intensity)
        
        return lambda **kwargs: gen(**kwargs)
    
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
    
        def gen(simul=None, velocity=None, **kwargs):
    
            # ----- Velocity norm
    
            n_vel = velocity.length
            
            # ----- acceleration norm
            
            a = intensity*n_vel**exponent
            
            # ----- Cap and smooth the viscosity
            
            a_max = n_vel/simul.delta_time
            a = a.map_range_smooth(0, a_max, 0, a_max)
            
            # ----- Return the acceleration
            
            return velocity.scale(-a/n_vel)
        
        return lambda **kwargs: gen(**kwargs)
    
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
        
        def gen(points=None, **kwargs):
            
            # ----- Index of nearest
            
            index = points.points.index_of_nearest(position=points.points.index).index
            
            # ----- Vector between the particle and its nearest neighbor
            
            v = points.points.position - points.points.sample_index(points.points.position, index=index)
            
            # ----- Distance
            
            d = v.length
            
            # ----- Acceleration computed on the capped distance
            
            base = d.map_range_smooth(d_min, d_max, d_min, d_max)
            a = -intensity*base**(-exponent)
            
            # ----- Return the acceleration
            
            return v.scale(a/d)
        
        return lambda **kwargs: gen(**kwargs)
    
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
    
        def gen(points=None, **kwargs):
            
            # ----- Vector to the attractor location
            
            v = location - points.points.position
            
            # ----- Minimum distance to the attractor
            
            d = v.length
            l = d.switch(d.less_than(d_min), d_min)
            
            # ----- Acceleration norm
            
            a = intensity*l**exponent
            
            # ----- Return the acceleration
            
            return v.scale(a/d)
        
        return lambda **kwargs: gen(**kwargs)
    
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
        
        def gen(points=None, **kwargs):
            
            # ----- Location to raycast from
            
            loc = points.points.position
            loc.z = z_max
            
            # ------ Raycast to the surface from the points locations
            
            node = points.points.raycast(target_geometry=mesh, source_position=loc, ray_length=2*z_max)
            
            # ----- Locate the where we have a hit
            
            points.points[node.is_hit].position = node.hit_position
            
            # ----- Delete the particles outside the surface
            
            if kill_outside:
                points.points[node.is_hit.b_not()].delete()
            
        return lambda **kwargs: gen(**kwargs)
    
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
        
        def gen(points=None, **kwargs):
            
            # ----- Get the normal at each point
            
            normal = mesh.sample_nearest_surface(value=mesh.points.normal, sample_position=points.points.position)
            
            # ----- Gravity component
            
            return normal.cross(g).cross(normal)
        
        return lambda **kwargs: gen(**kwargs)
    
    # ----------------------------------------------------------------------------------------------------
    # Generation function calling a group
    
    @staticmethod
    def func_group(group_name, out_socket=None, in_delta_time=None, in_points=None, in_velocity=None, in_age=None, out_points=None, out_velocity=None, out_age=None):
        """ Returns a function creating a Group node of the given name and connect sockets.
        
        The Group can have inpout sockets for delta_time, points, velocity and age used in a fluid simulation.
        It can have output sockets for points, velocity and age.
        
        If the sockets exist with this name, they will be connected automatically.If they have differente names,
        they must be provided using in_... and out_... arguments, for instance:
        - ``` in_velocity = None ``` : the velocity will be plugged to the input socket named 'velocity' if it exists
        - ``` in_velocity = 'vector' ``` : the velocity will be plugged to the input socket named 'vector'
        
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
            - in_points (str=None) : nema of the *points* input socket
            - in_velocity (str=None) : nema of the *velocity* input socket
            - in_age (str=None) : nema of the *age* input socket
            - out_points (str=None) : nema of the *points* output socket
            - out_velocity (str=None) : nema of the *velocity* output socket
            - out_age (str=None) : nema of the *age* output socket
        
        Returns:
            - function(**kwargs) : nodes generator
        """
        
        import geonodes as gn
        
        def gen(simul=None, points=None, velocity=None, age=None, **kwargs):
            
            # ----- Generate the group
            
            node = gn.Group("Sub")
    
            # ----- Input socket names
            
            in_d = in_delta_time
            in_p = in_points
            in_v = in_velocity
            in_a = in_age
            
            if in_d is None:
                if 'delta_time' in node.insockets.keys():
                    in_d = 'delta_time'
            if in_p is None:
                if 'points' in node.insockets.keys():
                    in_p = 'points'
            if in_v is None:
                if 'velocity' in node.insockets.keys():
                    in_v = 'velocity'
            if in_a is None:
                if 'age' in node.insockets.keys():
                    in_a = 'age'
    
            # ----- Connect the input sockets
    
            if in_d is not None:
                setattr(node, in_d, simul.delta_time)
            if in_p is not None:
                setattr(node, in_p, points)
            if in_v is not None:
                setattr(node, in_v, velocity)
            if in_a is not None:
                setattr(node, in_a, age)
    
            # ----- Output socket names
            
            out_p = out_points
            out_v = out_velocity
            out_a = out_age
            
            if out_p is None:
                if 'points' in node.outsockets.keys():
                    out_p = 'points'
            if out_v is None:
                if 'velocity' in node.outsockets.keys():
                    out_v = 'velocity'
            if out_a is None:
                if 'age' in node.outsockets.keys():
                    out_a = 'age'
    
            # ----- Connect the output sockets
            # Make the data sockets pointing to the outpout sockets of the node
            # using the stack method        
                    
            if out_p is not None:
                points.stack(node, out_p)
            if out_v is not None:
                velocity.stack(node, out_v)
            if out_a is not None:
                age.stack(node, out_a)
                
            # ----- Return the output socket if a name is given
                
            if out_socket is not None:
                return getattr(node, out_socket)
            else:
                return None
                
        return lambda **kwargs: gen(**kwargs)
         
        
            
            
                
        
    
            
        
        
        
        