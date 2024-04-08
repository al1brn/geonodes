#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 10:27:01 2023

@author: alain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 07:45:22 2023

@author: alain
"""

import inspect

import numpy as np

"""
from geonodes.new_maths.transformations import Eulers, Transformations, axis_vector
from geonodes.new_maths.functions import Function, keyed
from geonodes.new_maths import distribs

from geonodes.new_core import blender
from geonodes.new_core.cloud import Cloud
from geonodes.new_core.mesh import Mesh
from geonodes.new_core.curve import Curve
"""

from geonodes.core import engine
from geonodes.core import blender
from geonodes.core.mesh import Mesh
from geonodes.maths import functions


PI  = np.pi
TAU = np.pi*2

# =============================================================================================================================
# A simulation si basically a loop calling actions
#
# The simulation maintains:
# - the current time
# - dt of each loop
#
# Sub steps can be defined if more loops are required between two frames
#
# Functions called at each step are stored in a list
# The call to the function can be disabled
# Enabling / disabling functions can be driven by time (ie event)

# =============================================================================================================================
# Action / Event
#
# Actions are called at each loop.
# An Action maintains a enabled flag which can incremented / decremented to disable or reenabled the action
# Action have a start time and a duration. By default, start time is 0 and duration is None for actions always active.
#
# Main loop is made of
#
# def step():
#   actions : after = False
#   exec_step()
#   actions : after = True

class Action:
    NOT_STARTED = 0
    ACTIVE      = 1
    DONE        = 2
    
    def __init__(self, func, *args, top=0, duration=None, after=False, **kwargs):
        """ An action is a function called at each loop.
        
        The function must accept simulation as first argument.
        
        Hereafter is an example of function simulating gravity;
        
        ``` python
        def gravity(simulation, g=-9.86):
            simulation.points.position += (0, 0, g*simulation.dt)
        ````
        
        Arguments
        ---------
            - func (function (simulation, *args, **kwargs)) : the function to call at each loop
            - top (float=0) : start time
            - duration (float=None) : duration. Never interrupted if None, is called once if equal to 0.
            - bef_after (int=0) : when the action is called : PREPARE = -1, RUN = 0, FINISH = 1
            - *args : args to pass to the function
            _ **kwargs : keyword arguments to pass to the function
        """
        
        self.func       = func
        self.args       = args
        self.kwargs     = kwargs
        
        self.enabled    = 0
        self.after      = after
        
        # ----- Event specific
        
        self.status      = Action.NOT_STARTED
        self.top         = top
        self.duration    = duration
        self.first_call  = True
        
    # ====================================================================================================
    # Representation
    
    def __str__(self):
        if self.top == 0 and self.duration is None:
            stime = "No timing"
        else:
            if self.duration == 0:
                stime = f"Event  at {self.top:.2f}"
            else:
                stime = f"start: {self.top:.2f} during {self.duration:.2f}"
            stime += f" {['Not started', 'Active', 'Done'].index(self.status)}"
            
        return f"<Action {self.func.__name__}, {stime}, {'enabled' if self.is_enabled else 'disabled'}>"
        
    # ----------------------------------------------------------------------------------------------------
    # Reset

    def reset(self):
        self.status     = Action.NOT_STARTED
        self.first_call = True
        
    # ====================================================================================================
    # Enabling / disabling
    
    @property
    def is_disabled(self):
        return self.enabled > 0

    @property
    def is_enabled(self):
        return self.enabled == 0

    def enable(self):
        self.enabled -= 1
        assert(self.enabled > 0)
        
    def disable(self):
        self.disabled += 1
        
    # ====================================================================================================
    # Event management 
    
    @property
    def is_timed(self):
        return self.start != 0 or self.duration is not None
        
    @property
    def is_not_started(self):
        return self.status == Action.NOT_STARTED
    
    @property
    def is_active(self):
        return self.status == Action.ACTIVE
    
    @property
    def is_done(self):
        return self.status == Action.DONE

    # ----- Start
    
    def start(self, t):
        self.status = Action.ACTIVE
        
        self.start_time = t
        self.first_call = True
        
    # ----- Done
        
    def done(self):
        self.status = Action.DONE
        
    # ====================================================================================================
    # Call the action from the simulation
    
    def call(self, simulation):
        
        t = simulation.t
        
        elapsed = 0 if self.first_call else t - self.start_time
        simulation.elapsed = elapsed
        
        args   = [functions.keyed(arg,  t=elapsed) for arg in self.args]
        kwargs = {k: functions.keyed(v, t=elapsed) for k, v in self.kwargs.items()}
        
        res = self.func(simulation, *args, **kwargs)

        return res
        
    def __call__(self, simulation):
        
        # ===== Disabled
        
        if self.is_disabled:
            return None
        
        # ===== Not an event
        
        #if not self.is_event:
        #    return self.func(simulation, *self.args, **self.kwargs)
            
        # ==== Is it time ?
        
        t = simulation.t
        
        # Done or not yet
        if self.is_done or t < self.top:
            return None
        
        # Already In progress
        if self.is_active:
            # Done ?
            if self.duration is not None:
                if self.start_time + self.duration < t:
                    self.done()
                    return None
            
        # Not started
        else:
            self.start(t)
            
        # ----- Call
        
        if True:
            res = self.call(simulation)
            self.first_call = False
            
            return res
        else:
            elapsed = 0 if self.first_call else t - self.start_time
            simulation.elapsed = elapsed
            
            args   = [functions.keyed(arg,  t=elapsed) for arg in self.args]
            kwargs = {k: functions.keyed(v, t=elapsed) for k, v in self.kwargs.items()}
            
            res = self.func(simulation, *args, **kwargs)
            self.first_call = False
    
            return res
    
# =============================================================================================================================
# Simulation
#
# A simulation is a list of actions

class Simulation(list):
    def __init__(self, init_func=None, seed=0):
        
        super().__init__()
        
        self.init_func  = init_func
        self.init_seed  = seed
        self.rng        = np.random.default_rng(self.init_seed)
        
        self.t          = 0.
        self.elapsed    = None
        self.step_count = 0
        self.halt       = False
    
    # ====================================================================================================
    # Reset
    
    def reset(self):
        
        self.rng = np.random.default_rng(self.init_seed)
        self.t          = 0.
        self.elapsed    = None
        self.step_count = 0
        self.halt       = False
        
        t0 = 0
        for action in self:
            action.reset()
            t0 = min(t0, action.top)
        self.t = t0
        
        # Initialization
        
        if self.init_func is not None:
            self.init_func(self)

    # ====================================================================================================
    # Randomness
    
    @property
    def seed(self):
        return self.rng.integers(1<<63)
        
    # ====================================================================================================
    # Key values
    # t can be the elapsed time of an action. Simulation time is taken if not provided
    
    def keyed(self, value, t=None):
        if isinstance(value, str):
            return axis_vector(value)
        else:
            if t is None:
                if self.elapsed is None:
                    t = self.t
                else:
                    t = self.elapsed
            return functions.keyed(value, t)
        
    # ====================================================================================================
    # Actions and event
    
    @classmethod
    def str_to_func(cls, func):
        if isinstance(func, str):
            return getattr(cls, func)
        elif hasattr(func, '__func__'):
            return func.__func__
        else:
            return func
        
    def add_action(self, func, *args, top=0, duration=None, after=False, **kwargs):
        self.append(Action(self.str_to_func(func), *args, top=top, duration=duration, after=after, **kwargs))
    
    def add_event(self, func, *args, top=0, after=False, **kwargs):
        self.append(Action(self.str_to_func(func), *args, top=top, duration=None, after=after, **kwargs))
        
    """
    # ====================================================================================================
    # Minimization
    
    @staticmethod
    def min_hard(value, max_value, a=1., return_ratio=False):
        if return_ratio:
            return Simulation.min_hard(value, max_value)/value
        return np.minimum(max_value, value)
    
    @staticmethod
    def min_hard_continuous(value, max_value, a=1., return_ratio=False):
        if return_ratio:
            return Simulation.min_hard_continuous(value, max_value, a=a)/value
        
        # Hard
        #return np.minimum(value, max_value)
        
        p = 1/(1 + np.exp(10*(np.minimum(value/max_value, 10) - 1)))
        return value*p + (1-p)*max_value

    # More accurate for speeds
    
    @staticmethod
    def min_atan(value, max_value, a=1., return_ratio=False):
        if return_ratio:
            return Simulation.min_atan(value, max_value, a=a)/value
        
        f = a*2*max_value/np.pi
        return np.arctan(value/f)*f
    
    # Smoother for accelerations
    
    @staticmethod
    def min_sigmoid(value, max_value, a=1., return_ratio=False):
        if return_ratio:
            return Simulation.min_sigmoid(value, max_value, a=a)/value
        a *= .02
        return np.minimum(value, 2*max_value*(1/(1 + np.exp(-a*value)) - .5))
    
    @staticmethod
    def minimize_vectors(vs, max_norm, smooth='SIGMOID', a=1.):
        if max_norm is None:
            return vs
        
        if smooth == 'SIGMOID':
            f = Simulation.min_sigmoid
        elif smooth == 'ATAN':
            f = Simulation.min_atan
        elif smooth == 'HARD_CONTINUOUS':
            f = Simulation.min_hard_continuous
        else:
            f = Simulation.min_hard
            
        return vs * f(np.maximum(.01, np.linalg.norm(vs, axis=-1)), max_norm, a=1., return_ratio=True)[..., None]
    
    # ====================================================================================================
    # Maximization
    
    @staticmethod
    def max_hard_continuous(value, min_value, return_ratio=False):
        if return_ratio:
            return Simulation.max_hard_continuous(value, min_value)/value
        
        # Hard
        return np.minimum(value, min_value)
        
        p = 1/(1 + np.exp(10*(np.minimum(value/min_value, 10) - 1)))
        return min_value*p + (1-p)*value
    
    @staticmethod
    def maximize_vectors(vs, min_norm, smooth='SIGMOID', a=1.):
        if min_norm is None:
            return vs
        
        f = Simulation.max_hard_continuous
            
        return vs * f(np.linalg.norm(vs, axis=-1), min_norm, return_ratio=True)[..., None]

    # ====================================================================================================
    # Maximization
    
    @staticmethod
    def clip_vectors(value, min_value=None, max_value=None):
        if min_value is not None:
            value = Simulation.maximize_vectors(value, min_value)
        if max_value is not None:
            value = Simulation.min_hard_continuous(value, max_value)
        return value
    """
    
    # ====================================================================================================
    # Forces and acceleration
    
    def increase_force(self, force, is_acc):
        assert(False)

    # ====================================================================================================
    # Simulation
    
    # ----------------------------------------------------------------------------------------------------
    # Function called in the step
    
    def exec_step(self):
        pass
    
    # ----------------------------------------------------------------------------------------------------
    # Simulation loop
    
    def step(self, dt, sub_steps=1):
        
        if False:
            print(f"Simulation step {self.step_count}: {self.t:.2f} s (dt {dt:.2f}), points: {len(self.points)}")
        
        dt_ = dt/sub_steps
        self.dt = dt_

        # ----- Halt !

        if self.halt:
            self.t += dt
            self.step_count += 1
            return
        
        # ----- If time < 0, steps until time >= 0
        
        if self.t < 0:
            count = int(-self.t / dt)
            self.t = -count*dt
            count += 1
        else:
            count = 1
            
        # ----- Loop on the steps and the sub steps
            
        for _ in range(count):
            for i in range(sub_steps):
                
                for action in self:
                    if action.after:
                        continue
                    self.elapsed = None
                    action(self)
                    
                self.exec_step()
                
                for action in self:
                    if not action.after:
                        continue
                    self.elapsed = None
                    action(self)
                    
                # ----- Next t
                        
                self.t += dt_
                self.step_count += 1
            
    # ====================================================================================================
    # Run the animation
                
    def to_engine(self, update_viewport=None, with_setup=True, sub_steps=1):
        
        def setup(eng):
            if False:
                print(f"Simulation reset")
            self.reset()
            
        def update(eng):
            if False:
                print("UPDATE", type(eng), eng.dt, hasattr(self, 'dt'))
                
            self.step(eng.dt, sub_steps=sub_steps)
            if update_viewport is not None:
                update_viewport(self)
                
        if isinstance(with_setup, bool):
            setup_func = setup if with_setup else None
        else:
            setup_func = with_setup
            
        engine.add(update, setup=setup_func)
        
    def go(self, update_viewport=None, with_setup=True, sub_steps=1):
        
        engine.init()
        
        self.to_engine(update_viewport=update_viewport, with_setup=with_setup, sub_steps=sub_steps)
        
    # ====================================================================================================
    # Animation demo
    
    @staticmethod
    def demo_follow():
        
        from mathutils import Vector
        
        cube = Mesh.Cube().to_object("Follows the control")
        ctl  = blender.get_empty("Control")
        
        cube.location = (20, 0, 0)
        ctl.location  = (0, 0, 0)
        
        def follow(simulation):
            v  = ctl.location - cube.location
            simulation.speed += v/25
            cube.location = cube.location + Vector(simulation.speed/25)
            
        sim = Simulation()
        sim.speed = np.array((10, 20, 30), float)
        sim.add_action(follow)
        
        sim.to_engine()
        
    @staticmethod
    def demo_rain(c=3, w=15, time_falloff=6, dist_falloff=3):
        
        water = Mesh.Grid(10, 10, 100, 100)
        
        # ----- Reset the height of each water point
        
        def reset_h(simulation):
            water.points.position[:, 2] = 0
            
        # ----- Add the heighotfor one dip
        
        def dip(simulation, location, amplitude, c=3, w=15, time_falloff=6, dist_falloff=3):
            
            # Distance of the water points to the dip location
            
            d = np.linalg.norm(water.points.position[:, :2] - location[:2], axis=-1)
            
            # Delay linked to the distance
            
            t = simulation.elapsed - d/c
            
            # Amplitude decreases with time and distance
            
            amp = -amplitude*np.exp(-t**time_falloff)*np.exp(-d**dist_falloff)
            
            # Amplitude only for positive time
            
            h = np.zeros(len(water.points))
            sel = t > 0
            if np.sum(sel) > 0:
                h[sel] = (amp*np.sin(w*t))[sel]
            
            water.points.z += h
            
        sim = Simulation()
        sim.add_action(reset_h)
        rng = np.random.default_rng(0)
        
        for _ in range(300):
            sim.add_action(dip, 
                location  = rng.uniform(-10, 10, 3), 
                amplitude = rng.normal(.2, .05),
                top       = rng.uniform(-2, 10),
                duration  = 4,
                c=c, w=w, time_falloff=time_falloff, dist_falloff=dist_falloff)
        
        sim.go(update_viewport=lambda _: water.to_object("Water"))
        

            
        

 
        
        
        
        
        
        
        
            
    
    
    
