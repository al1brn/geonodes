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
    
    def __init__(self, geometry=None, **kwargs):
        
        import geonodes as gn
        
        # ----- Create an link the input and output simulation nodes
        
        self.input  = nodes.SimulationInput()
        self.output = nodes.SimulationOutput()
        self.input.bnode.pair_with_output(self.output.bnode)
        
        # ----- Create the simulation state items
        
        for name, value in kwargs.items():
            if name.lower() != 'geometry':
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
        
            
            return sim.og


        
        
        
        
        