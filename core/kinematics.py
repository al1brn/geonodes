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

from geonodes import KDTree


from geonodes.maths.transformations import Transformations, axis_vector, normalize
from geonodes.maths.functions import Function, keyed
from geonodes.maths import distribs, minmax

from geonodes.core.simulation import Action, Simulation
from geonodes.core.cloud import Cloud
from geonodes.core.mesh import Mesh
from geonodes.core.instances import Instances
from geonodes.core import blender
from geonodes.core import engine

PI  = np.pi
TAU = np.pi*2

TEST_NAN = True

# =============================================================================================================================
# Acceleration / Force on points

class Force(Action):
    def __init__(self, func, *args, is_force=True, **kwargs):
        super().__init__(func, *args, **kwargs)
        
        self.is_force = is_force
        
    def __call__(self, simulation):
        
        res = super().__call__(simulation)
        if res is None:
            return None

        if TEST_NAN:
            nan_count = np.sum(np.isnan(res))
            if nan_count > 0:
                print(f"CAUTION Force: {nan_count} nan values encountered in force computation")
        
        if self.is_force:
            simulation.points.acceleration += res/simulation.points.mass[:, None]
        else:
            simulation.points.acceleration += res
            
            
# ====================================================================================================
# Utilities

"""

def min_hard(value, max_value, a=1., return_ratio=False):
    if return_ratio:
        return min_hard(value, max_value)/value
    return np.minimum(max_value, value)

def min_hard_continuous(value, max_value, a=1., return_ratio=False):
    if return_ratio:
        return min_hard_continuous(value, max_value, a=a)/value
    
    p = 1/(1 + np.exp(10*(value/max_value - 1)))
    return value*p + (1-p)*max_value

# More accurate for speeds

def min_atan(value, max_value, a=1., return_ratio=False):
    if return_ratio:
        return min_atan(value, max_value, a=a)/value
    
    f = a*2*max_value/np.pi
    res = np.arctan(value/f)*f
    res[np.abs(max_value)<.0001] = 0
    
    return res

# Smoother for accelerations

def min_sigmoid(value, max_value, a=1., return_ratio=False):
    if return_ratio:
        return min_sigmoid(value, max_value, a=a)/value
    a *= .02
    return np.minimum(value, 2*max_value*(1/(1 + np.exp(-a*value)) - .5))

def minimize_vectors(vs, max_norm, smooth='HARD_CONTINUS', a=1.):
    if max_norm is None:
        return vs
    
    if smooth == 'SIGMOID':
        f = min_sigmoid
    elif smooth == 'ATAN':
        f = min_atan
    elif smooth == 'HARD_CONTINUS':
        f = min_hard_continuous
    else:
        f = min_hard
        
    return vs * f(np.maximum(.01, np.linalg.norm(vs, axis=-1)), max_norm, a=1., return_ratio=True)[..., None]


"""

# =============================================================================================================================
# Create / kill points

def create_points(simulation, position, **attributes):
    n = 1 if np.shape(position) == (3,) else len(position)
    return simulation.points.add(n, position=position, **attributes)
    
def emit(simulation, dist_func, *args, count=10, density=None, attributes={}, **kwargs):
    
    if density is not None:
        density *= simulation.dt
    count = int(count*simulation.dt)
    
    position, speed = dist_func(*args, count=count, density=density, seed=simulation.rng, **kwargs)
    
    return simulation.points.add(len(position), position=position, speed=speed, **attributes)
        
    
def kill_points(simulation, selection):
    simulation.points.delete(selection)
    
def kill_old(simulation, age, scale=None):
    
    ages = age if scale is None else simulation.rng.normal(age, scale, len(simulation.points))
    if simulation.count_down:
        selection = simulation.points.age < ages
    else:
        selection = simulation.points.age > ages
        
    if np.sum(selection) > 0:
        simulation.points.delete(selection)
    
def kill_z0(simulation, z=0, scale=None):

    zs = z if scale is None else simulation.rng.normal(z, scale, len(simulation.points))
    selection = simulation.points.position[:, 2] <= zs
    
    if np.sum(selection) > 0:
        simulation.points.delete(selection)

# =============================================================================================================================
# Misceleanous
    
def orient_to_speeds(simulation, track_axis='Z', up_axis='Y'):
    simulation.eulers = tracker(simulation.speed, track_axis=track_axis, up_axis=up_axis).eulers
    
# =============================================================================================================================
# Bounce on a infinite plane or disk

def bounce_on_plane(simulation, origin=(0, 0, 0), direction='Z', radius=None, epsilon=.1, energy_factor=.95, noise=None):
    
    z_axis = axis_vector(direction)
    rel_loc = simulation.points.position - origin
    
    # ----- Position of the particles along direction
    
    z = np.einsum('...i, ...i', z_axis, rel_loc)
    
    # ----- Incident speed
    
    in_speed = np.einsum('...i, ...i', simulation.points.speed, z_axis)
    
    # ----- Particles which will pass through the plane
    
    sel = np.logical_and(in_speed < 0, np.logical_and(z > -epsilon, z + in_speed*simulation.dt < epsilon))
    if not np.sum(sel):
        return
    
    # ----- Particles location in the plane
    
    xy = rel_loc - z_axis*z[:, None]
    
    # Possible constraint on a radus around  the origin
    
    if radius is not None:
        u, r = normalize(xy)
        np.logical_and(sel, r < radius, out=sel)
        if not np.sum(sel):
            return

    # ----- new speed
    
    new_speed = simulation.points.speed[sel] - z_axis*(2*in_speed)[sel, None]
    
    if noise is not None:
        new_speed += simulation.rng.uniform(-noise, noise, (len(new_speed), 3))
        
    E0 = np.sum(simulation.points.speed[sel]**2, axis=-1)
    E1 = np.sum(new_speed**2, axis=-1)
    new_speed *= (energy_factor*E1/E0)[:, None]
    
    simulation.points.speed[sel] = new_speed
    
# =============================================================================================================================
# Bounce on a surface

def bounce_on_surface(simulation, surface, epsilon=.1, energy_factor=.95, noise=None):
    
    # ----------------------------------------------------------------------------------------------------
    # Surface center and radius if not already computed
    
    if surface.get('centers') is None:
        
        surface['max_radius'] = np.max(np.sqrt(surface['areas']/TAU))
        
        centers = np.empty_like(surface['normals'])
        offset = 0
        for i, size in enumerate(surface['sizes']):
            centers[i] = np.average(surface['verts'][offset:offset+size], axis=0)
            offset += size
            
        surface['centers'] = centers
        
        surface['kdtree'] = KDTree(centers)
        
    # ----------------------------------------------------------------------------------------------------
    # Distance reachable by each ball
    
    u_speed, n_speed = normalize(simulation.points.speed)
    dist = n_speed*simulation.dt + surface['max_radius']
    
    # ----- Query the KDTree
    
    close_faces = surface['kdtree'].query_ball_point(simulation.points.position, dist)

    # ----- Loop on the balls close to a face
    
    for i_ball, face_inds in enumerate(close_faces):
        if not len(face_inds):
            continue
        
        loc   = simulation.points.position[i_ball]
        speed = simulation.points.speed[i_ball]
        
        for i_face in face_inds:
            
            z_axis  = surface['normals'][i_face]
            rel_loc = loc - surface['centers'][i_face]
            
            # Under the face
            z = np.dot(rel_loc, z_axis)
            if z < -epsilon:
                continue

            # Speed up
            in_speed = np.dot(speed, z_axis)
            if in_speed > 0:
                continue
            
            # Won't touch the face
            if z + in_speed*simulation.dt > epsilon:
                continue
            
            # Location on the face
            xy = rel_loc - z_axis*z
            
            
            # Too far from the center
            d2 = np.sum(xy**2)
            if d2*TAU > surface['areas'][i_face]:
                continue
            
            # We have a bounce :-)
            
            new_speed = simulation.points.speed[i_ball] - z_axis*(2*in_speed)
            
            if noise is not None:
                amp = np.max(np.abs(new_speed))
                new_speed += simulation.rng.uniform(-amp*noise, amp*noise, (3,))
                
            E0 = np.sum(new_speed**2)
            E1 = np.sum(speed**2)
            new_speed *= energy_factor*E1/E0
            simulation.points.speed[i_ball] = new_speed
            
    
    

            
# =============================================================================================================================
# Kinematics functions

# ----------------------------------------------------------------------------------------------------
# Gravity

def gravity(simulation, g=-9.86):
    g = simulation.keyed(g)
    return (0., 0., g) if np.shape(g) == () else g

# ----------------------------------------------------------------------------------------------------
# Centrifugal

def centrifugal(simulation, location=(0, 0, 0), omega=1, axis='Z', coriolis_factor=1.):
    
    vomega = -2*omega*axis
    
    # Locations relative to the bottom point
    
    rel_locs = simulation.position - location
    
    # Location on the axis and vector perpendicular
    
    loc_z  = np.einsum('...i, ...i', rel_locs, axis)
    loc_xy = rel_locs - axis*loc_z[..., None]
    
    rs = np.linalg.norm(loc_xy, axis=-1)
    
    # ----- Radial
    
    acc = loc_xy*(omega*omega)
    
    # ----- Plus Coriolis
    # Factor articially controls the intensity of the Coriolis force
    
    acc += np.cross(-2*omega*axis, simulation.points.speed)*coriolis_factor
    
    return acc  

# ----------------------------------------------------------------------------------------------------
# Central acceleration

def central_acc(simulation, location=(0, 0, 0), factor=1., power=-2, max_acc=None):
    
    rel_locs = simulation.position - location
    d2 = np.einsum('...i, ...i', rel_locs, rel_locs)
    if power != 3:
        d2 **= (power - 1)/2
        
    d2 *= factor
    if max_acc is not None:
        d2 = min_sigmoid(d2, max_acc)
        
    return (-d2)[..., None]*simulation.points.position

# ----------------------------------------------------------------------------------------------------
# Newton like law

def newton_law(simulation, G=1, power=2):
    
    # The force between two points P0 and P1 is given by:
    # F = G.m1.m2 / d^p
    # where d is the distance between them and p the power factor, p=2 in standard newton's law
    #
    # The result is a vector along the unary vector e between P0 and P1
    # f = F.e
    #
    # The vector v between P0 and P1 is : v = d.e
    # Hence: f = G.m1.m2 / d^p . v/d
    # f = G.m1.m2 / d^(p+1) . v
    #
    # We can compute easily d2 = d^2 which gives:
    # f = G.m1.m2 / d2^((p+1)/2) . v
    
    if not len(simulation.points):
        return
    
    v = simulation.points.position - simulation.points.position[:, None]
    d = np.clip(np.einsum('...i, ...i', v, v), .001, None)
    
    if power != 1:
        d = 1/d**((power+1)/2)
        
    d[range(len(v)), range(len(v))] = 0

    np.set_printoptions(formatter={'float': lambda x: f"{x:10.3f}"})    
    
    d *= G*simulation.points.mass
    
    a = np.sum(d[..., None]*v, axis=1)
    
    simulation.points.acceleration += a

# ----------------------------------------------------------------------------------------------------
# Viscosity from fuild speed at point locations
    
def viscosity(simulation, factor=1., power=2, max_force=None, fluid_speed=None):
    
    # ------ Points speed relative to the speed of the fluid
    
    if fluid_speed is None:
        rel_speed = simulation.points.speed
    else:
        rel_speed = simulation.points.speed - fluid_speed
        
    # ----- Directions and norm
    
    dirs, speeds = distribs.normalize_vectors(rel_speed, keep_zeros=True)
    
    # ----- Raw force
    
    force = factor*simulation.points.viscosity*(speeds**power)
    
    # ----- The force can't inverse the speed
    
    max_f = simulation.points.mass*speeds/simulation.dt
    if max_force is not None:
        max_f = np.minimum(max_force, max_f)

    # ----- Minimize the force

    if True:    
        force = minmax.minimize_vectors(force, max_f, delta=1.)
    else:
        force = min_atan(force, max_f)
        

    return dirs*(-force[:, None])
    

    
# ----------------------------------------------------------------------------------------------------
# Wind with viscosity and noise
    
def wind(self, force=5, axis='X', viscosity=1., power=2, noise=None, noise_scale=1., noise_detail=1., time_scale=1.):
    
    wind_speed = force*axis
        
    if noise is not None:
        
        noise_scale  = self.keyed(noise_scale)
        noise_detail = self.keyed(noise_detail)
        time_scale   = self.keyed(time_scale)
        
        bnoise = BNoise(scale=noise_scale/10, detail=noise_detail, dimension=4, noise_basis='PERLIN_ORIGINAL', seed=self.seed)
        wind_speed += noise*bnoise.vector(self.locations, w=self.t*time_scale)
            
    return self.viscosity(wind_speed, viscosity, power)
    
# ----------------------------------------------------------------------------------------------------
# Thrust

def thrust(self, thrust=1., axis=None, noise=None, noise_scale=1., noise_detail=1., time_scale=1.):
    
    if len(self) == 0:
        return []
    
    thrust = self.keyed(thrust, t=self.get_attribute('ages', None))
    axis   = self.keyed(axis)
    noise  = self.keyed(noise)
    
    #print(f"{self.t:.1f}: {thrust[:3]}")
    
    # ----- Axis is not defined, we use speed direction
    
    if axis is None:
        axis = Vectors.Axis(np.array(self.speeds)).a
        
    # ----- Axis is defined, we take the rotation of the point into account
    
    else:
        axis = self.matrices @ axis
        
    # ----- We can compute the force

    if np.shape(thrust) == ():
        force = thrust*axis
    else:
        force = np.array(thrust)[None, :]*axis
        
    # ----- Less borrowing
        
    if noise is not None:
        
        noise_scale  = self.keyed(noise_scale)
        noise_detail = self.keyed(noise_detail)
        time_scale   = self.keyed(time_scale)
        
        bnoise = BNoise(scale=noise_scale/10, detail=noise_detail, dimension=4, noise_basis='PERLIN_ORIGINAL', seed=self.seed)
        force += noise*bnoise.vector(self.locations, w=self.t*time_scale)
        
    return force

def add_thrust(self, *args, **kwargs):
    return self.add_force(Points.thrust, *args, **kwargs)
    
    
# ----------------------------------------------------------------------------------------------------
# Vortex

def add_vortex(self, 
        location     = (0, 0, 0), 
        axis         = 'Z', 
        omega        = 1., 
        vert_factor  = 1, 
        vert_power   = .5, 
        hrz_factor   = 1, 
        hrz_power    = -2, 
        angle        = PI/6, 
        viscosity    = 1., 
        power        = 2, 
        noise        = 0, 
        noise_scale  = 1., 
        noise_detail = 1.,
        time_scale   = 1.,
        ):

    bnoise = BNoise(scale=noise_scale, detail=noise_detail, dimension=4, noise_basis='PERLIN_ORIGINAL', seed=self.seed)
    
    axis = axis_vector(axis)
    def vortex(points, dt):
        
        # Locations relative to the bottom point
        
        rel_locs = points.locations - location
        
        # Location on the axis and vector perpendicular
        
        loc_z  = np.maximum(.001, np.abs(np.einsum('...i, ...i', rel_locs, axis)))
        loc_xy = rel_locs - axis*loc_z[:, None]
        
        rs = np.linalg.norm(loc_xy, axis=-1)
        
        # ----- Omega decreases with altitude
        
        omg = omega*vert_factor*np.power(loc_z, vert_power)
        
        # ----- Omega decreases with distance to the cone
        
        r_max = loc_z*np.tan(angle)
        
        omg *=hrz_factor*np.power(np.maximum(0.001, np.abs(rs - r_max)), hrz_power)
        
        # ----- We can compute  the speed
        
        # Unary vectors
        
        vortex_speed = np.cross(axis, loc_xy/(rs[:, None]))
        
        # We add some noise
        
        if noise != 0:
            vortex_speed += noise*bnoise.vector(points.locations, w=points.t*time_scale)
        
        # We scale with the rotation speed
        
        vortex_speed *= np.minimum(10, omg)[:, None]
        
        return Points.vicosity_acc(points, fluid_speeds=vortex_speed, factor=viscosity, power=power, dt=dt)

    self.add_force(vortex)    

# =============================================================================================================================
# Kinematics simulation

class Kinematics(Simulation):
    
    def __init__(self, geometry=None, init_func=None, count_down=False, max_force=None, max_acc=None, min_speed=None, max_speed=None, seed=0):
        
        super().__init__(init_func=init_func, seed=seed)
        
        if geometry is None:
            self.geometry = Cloud()
        else:
            self.geometry = geometry
        self.points   = self.geometry.points

        self.count_down = count_down
        self.max_force  = max_force
        self.max_acc    = max_acc
        self.min_speed  = min_speed
        self.max_speed  = max_speed

        self.points.new_vector_attribute('speed',        default=(0, 0, 0))
        self.points.new_vector_attribute('acceleration', default=(0, 0, 0))
        
        self.points.add_auto_attribute('mass',         'FLOAT'           , default = 1.)
        self.points.add_auto_attribute('age',          'FLOAT'           , default = 0)
        self.points.add_auto_attribute('locked',       'BOOLEAN'         , default = False)
        self.points.add_auto_attribute('last_pos',     'FLOAT_VECTOR'    , default = (0, 0, 0))
        self.points.add_auto_attribute('viscosity',    'FLOAT'           , default = .01)
        
        self.points.add_auto_attribute('scales',       'FLOAT_VECTOR'    , default = (1, 1, 1))
        
        # ----- Rotation
        
        self.points.add_auto_attribute('moment',       'FLOAT'           , default = 1.)
        self.points.add_auto_attribute('eulers',       'FLOAT_VECTOR'    , default = (0, 0, 0))
        self.points.add_auto_attribute('omega',        'FLOAT_VECTOR'    , default = (0, 0, 0))
        
        self.reset()
    
    # ====================================================================================================
    # Reset
    
    def reset(self):
        
        self.geometry.clear()
        
        super().reset()
        
    # ====================================================================================================
    # After each simulation loop: update position and speed
    
    def exec_step(self):
        
        super().exec_step()
        
        # ----- Update the speed and move the particles
        
        acc = self.points.acceleration

        # ---- Watch dog
        
        if TEST_NAN:
            nan_count = np.sum(np.isnan(acc))
            if nan_count > 0:
                print(f"CAUTION Simulation acceleration: {nan_count} nan values encountered in acceleration")
        
        if self.max_acc is not None:
            acc = minmax.minimize_vectors(acc, self.max_acc, delta=1)
            
        new_speed = self.points.speed + acc*self.dt     
        #print("EXEC_STEP BEF", np.linalg.norm(new_speed, axis=-1)[:5])
        new_speed = minmax.clip_vectors(new_speed, self.min_speed, self.max_speed, delta=.1)
        #print("EXEC_STEP AFT", np.linalg.norm(new_speed, axis=-1)[:5])
            
        self.points.position += (self.points.speed + new_speed)*(self.dt/2)
        self.points.speed = new_speed
        
        # Reset acceleration for next step
        
        self.points.acceleration = (0, 0, 0)
        
        # ----- Update the age
                
        if self.points.attribute_exists("age"):
            if self.count_down:
                self.points.age -= self.dt
            else:
                self.points.age += self.dt

    # ====================================================================================================
    # Actions and event
    
    def set_count(self, count):
        diff = count - len(self.points)
        if diff < 0:
            self.points.delete(np.arange(len(self)+diff, len(self)))
        elif diff > 0:
            self.add_points(np.zeros((diff, 3), float))         
        
    # ====================================================================================================
    # Forces / Accelerations 
        
    def force(self, func, *args, top=0, duration=None, **kwargs):
        self.append(Force(self.str_to_func(func), *args, top=top, duration=duration, is_force=True, **kwargs))
        
    def acceleration(self, func, *args, top=0, duration=None, **kwargs):
        self.append(Force(self.str_to_func(func), *args, top=top, duration=duration, is_force=False, **kwargs))
    
    def gravity(self, g=-9.86, top=0, duration=None):
        self.acceleration(gravity, g=g, top=top, duration=None)
        
    def central_acc(self, location=(0, 0, 0), factor=1., power=-2, max_acc=None, top=0, duration=None):
        self.acceleration(location=location, factor=factor, power=power, max_acc=max_acc, top=top, duration=duration)
        
    def centrifugal(self, location=(0, 0, 0), omega=1, axis='Z', coriolis_factor=1., top=0, duration=None):
        self.acceleration(centrifugal, location=location, omega=omega, axis=axis, coriolis_factor=coriolis_factor,
                              top=top, duration=duration)
        
    def viscosity(self, factor=1., power=2, max_force=None, fluid_speed=None):
        self.force(viscosity, factor=factor, power=power, max_force=max_force, fluid_speed=fluid_speed)
        
    # ====================================================================================================
    # Create / kill points
    
    def create(self, position, top=0, duration=0, **attributes):
        self.add_action(create_points, position, top=top, duration=duration, **attributes)
        
    def emit(self, dist_func, *args, top=0, duration=None, **kwargs):
        """ Equivalent to create but using a distribution function returning position and speed.
        """        
        self.add_action(emit, dist_func, *args, top=top, duration=duration, **kwargs)
    
    def kill(self, selection, top=0, duration=None):
        self.add_action(kill_points, selection, top=top, duration=duration)
        
    def kill_old(self, age, scale=None, top=0, duration=None):
        self.add_action(kill_old, age=age, scale=scale,top=top, duration=duration)
        
    def kill_z0(self, z=0, scale=None, top=0, duration=None):
        self.add_action(kill_z0, z=z, scale=scale,top=top, duration=duration)

    # ====================================================================================================
    # Misceleanous
        
    def orient_to_speeds(self, track_axis='Z', up_axis='Y', top=0, duration=None):
        self.add_action(orient_to_speed, track_axis=trackaxis, up_axis=up_axis, top=top, duration=duration)

    # ====================================================================================================
    # Emitters
    
    def add_emitter(self, dist_func, *args, top=0, duration=None, count=10, density=None, **kwargs):
        self.add_event(top, Simulation.emit, dist_func, *args, duration=duration, count=count, density=density, **kwargs)
        
    
    def emit_track_particles(self, tracked_points, distribution='SEGMENT', 
            radius=.1, count=0, density=1., 
            distance=None, speed=0., speed_scale=None, speed_angle_scale=None,
            stop_when_locked=False, attributes_transfer=None, **attributes):
        
        # Keyable arguments
        
        radius              = self.keyed(radius)
        count               = self.keyed(count)
        density             = self.keyed(density)
        distance            = self.keyed(distance)
        speed               = self.keyed(speed)
        speed_scale         = self.keyed(speed_scale)
        speed_angle_scale   = self.keyed(speed_angle_scale)
        
        # Short cut !
        
        position = tracked_points.position
        
        # ----- If distribution on a trajectory segment, we need the last locations
            
        if distribution == 'SEGMENT':
            last_pos = np.array(tracked_points.last_pos)
            tracked_points.last_pos = position
        else:
            last_pos = position
            
        # ----- The speeds of the points give the ejection direction
        
        tracked_speed_dir, tracked_speed_norm = distribs.normalize_vectors(tracked_points.speed, keep_zeros=True)
        tracked_speed_dir *= -1
        
        # ----- Particles can be emitted at a given distance behind the tracked points
        
        if distance is not None:
            position  = position + tracked_speed_dir*distance
            last_pos  = last_pos + tracked_speed_dir*distance

        # ----- Density and count
        
        if density is not None:
            density = density * self.dt
        
        count = self.rng.poisson(self.dt*count)        
            
        # ----- Loop on the tracked points
            
        for i_tracked, (p_pos, p_last) in enumerate(zip(position, last_pos)):
            
            if stop_when_locked and tracked_points.points.locked[i_tracked]:
                continue
                
            # ----- Segment distribution : we emit on a cylinder between last and current locations
            
            if distribution == 'SEGMENT':
                
                locs, speeds = distribs.cylinder_dist(p_last, p_pos, radius=radius, count=count, density=density,
                        scale=radius/3, seed=self.rng, speed=0, speed_dir='NORMAL')
                
            # ----- Sphere distribution : we emit on a sphere
                
            elif distribution == 'SPHERE':
                locs, speeds = dstribs.sphere_dist(radius, center=p_pos, scale=radius/3, count=count, density=density,
                                        speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale,
                                        seed=self.rng)

            else:
                raise Exception(f"emit_track_particles error: invalid distribution code: '{distribution}")
                
            # Add the points
            
            inds = self.points.add(len(locs), position=locs, speed=speed, **attributes)
            
            # Transfer attributes
            
            if attributes_transfer is not None:
                if isinstance(attributes_transfer, str):
                    attributes_transfer = [attributes_transfer]
                for name in attributes_transfer:
                    self.points.attributes[name][inds] = tracked_points.attributes[name][i_tracked]
            
            
    # ====================================================================================================
    # Baking
    
    # ----------------------------------------------------------------------------------------------------
    # Positions
    
    def sim_curves(self, duration=10., count=100, sub_steps=1):
        
        self.reset()
        
        curves = np.empty(self.shape + (count, 3))

        dt = duration/(count-1)
        for index in range(count):
            curves[..., index, :] = self.locations
            self.step(dt, sub_steps=sub_steps)
            
        return curves

    # ----------------------------------------------------------------------------------------------------
    # Bake particles
    # Location is saved only for live points
    
    def bake_particles(self, duration=10., count=100, sub_steps=1):

        self.reset()
            
        points_list = []
        
        dt = duration/(count-1)
        for index in range(count):
            points_list.append(self.clone())
            self.step(dt, sub_steps=sub_steps)
            
        return points_list
    
    # ----------------------------------------------------------------------------------------------------
    # Bake with ID
    
    def bake(self, duration=10., count=100, sub_steps=1):

        self.reset()
        self.create_ID()
        
        chaos = self.bake_particles(duration=duration, count=count, sub_steps=sub_steps)
        
        # ----- Let's rebuild with IDs
        # The ID of attributes gives the number of create IDs
        
        total = chaos[-1].attributes.ID
        
        points_list = []
        for points in chaos:
            
            all_points = Points(shape=total)
            points_list.append(all_points)

            all_points.attributes.copy(self.attributes)
            all_points.new_bool_attribute('alive', False)
            points.alive = False

            points.reshape(points.size)
            if len(points) == 0:
                continue
            
            points.new_bool_attribute('alive', True)
            points.alive = True
            
            IDs = points.ID
            all_points.a[IDs] = points.a
            all_points.attributes.set_selection(IDs, points.attributes)
            
            
        return points_list
    
    # ----------------------------------------------------------------------------------------------------
    # Key frames locations
    
    def set_key_frames(self, objects, frame, properties=['locations', 'scales', 'eulers']):
        
        from geonodes.core import blender
        
        if len(objects) != self.size:
            raise Exception(f"bake_locations error: {len(objects)} are provided for {self.size} points!")
            
        locs   = np.reshape(self.locations, (len(objects), 3))
        scales = np.reshape(self.scales,    (len(objects), 3))
        eulers = np.reshape(self.eulers.a,  (len(objects), 3))
        
        for obj, loc, scale, euler in zip(objects, locs, scales, eulers):
            if 'locations' in properties:
                blender.kf_set(obj, "location.x", frame, loc[0])
                blender.kf_set(obj, "location.y", frame, loc[1])
                blender.kf_set(obj, "location.z", frame, loc[2])

            if 'scales' in properties:
                blender.kf_set(obj, "scale.x", frame, scale[0])
                blender.kf_set(obj, "scale.y", frame, scale[1])
                blender.kf_set(obj, "scale.z", frame, scale[2])

            if 'eulers' in properties:
                blender.kf_set(obj, "rotation_euler.x", frame, euler[0])
                blender.kf_set(obj, "rotation_euler.y", frame, euler[1])
                blender.kf_set(obj, "rotation_euler.z", frame, euler[2])
    
    # ----------------------------------------------------------------------------------------------------
    # Compute the trajectories
    
    def get_trajectories(self, duration=10., count=100, sub_steps=1, dt=None):
        
        self.reset()
        self.create_ID()
        
        locs = []
        tops = []
        
        if dt is None:
            dt = duration/(count-1)
        else:
            duration = dt*(count-1)
            
        for index in range(count):
            
            # ----- Capture the locations if any
            
            IDs = self.ID
            if len(IDs) > 0:
                nb_ID = np.max(IDs) + 1
                
                n =  nb_ID - len(locs)
                if n > 0:
                    tops.extend([(index, index*dt)]*n)
                    locs.extend([[] for _ in range(n)])
                    
                for ID, loc in zip(IDs, self.locations):
                    locs[ID].append(list(loc))
                    
            self.step(dt, sub_steps=sub_steps)
        
        return {
            'frames':     np.array([top[0] for top in tops]), 
            'times':      np.array([top[1] for top in tops]), 
            'locations': [np.array(loc) for loc in locs],
            }
    
    # =============================================================================================================================
    # To mesh object
    
    def to_mesh_object(self, spec, model=None, update=False, attributes=[], shade_smooth=True):
        
        import bpy
        #from geonodes.core.meshbuilder import MeshBuilder
        
        #if model is not None and isinstance(model, (str, bpy.types.Object)):
        #    model = MeshBuilder.FromObject(model)
            
        # ----------------------------------------------------------------------------------------------------
        # Update an existing mesh with the proper number of vertices
        
        if update:
            mesh = blender.get_object(spec).data
            
            # ----- Update the vertices
            
            # No model : we have a cloud of vertices
            if model is None:
                n = 1
                mesh.vertices.foreach_set('co', np.array(self.locations.flatten()))
                
            # Model size duplicated by self.shape
            else:
                n = model.verts_len
                if n == 1:
                    verts = self @ model.verts
                else:
                    verts = self[..., None] @ model.verts
                    
                mesh.vertices.foreach_set('co', np.reshape(verts, verts.size))
                
            # ----- Update the attributes
            
            for name in ['scales', 'eulers']:
                if name in attributes:
                    blender.set_attribute(mesh, name, np.array(self.get_attribute(name)))
                    
            self.attributes.to_mesh(mesh, attributes=attributes, update=True)
                
            mesh.update()
        
        # ----------------------------------------------------------------------------------------------------
        # Let's create the object
        
        else:
            
            # ----- Create the mesh
        
            # A cloud of vertices
            if model is None:
                obj = blender.create_mesh_object(spec)
                mesh = obj.data
                
                mesh.clear_geometry()
                if not self.size:
                    return
                    
                mesh.vertices.add(self.size)
                mesh.vertices.foreach_set('co', self.locations.flatten())
                
                mesh.update()
                
            # Model duplicated along the shape
            else:
                mb = model*self.size
                mb.transform(self)
                
                obj = mb.to_object(spec, shade_smooth=shade_smooth)
                
            # ----- Create the attributes
            
            mesh = obj.data
            for name in ['scales', 'eulers']:
                blender.create_attribute(mesh, name, 'FLOAT_VECTOR', domain='POINT', value=np.array(self.get_attribute(name)))
                
            self.attributes.to_mesh(mesh, attributes=attributes, update=False)
            
    def to_cloud(self, spec, attributes=[]):
        
        from geonodes.core import blender
        
        obj = blender.create_mesh_object(spec)
        mesh = obj.data
        mesh.clear_geometry()
        mesh.from_pydata(np.array(self.locations), (), ())

        self.attributes.to_mesh(mesh, attributes=attributes, update=False)
        
        return obj
    
    # =============================================================================================================================
    # Some demos
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Newton law
    
    @staticmethod
    def demo_newton():
        
        # ----------------------------------------------------------------------------------------------------
        # Merge close planets
        
        def merge(simulation, r=.5):
            kdt = KDTree(simulation.points.position)
            merged    = []
            to_delete = []
            for i0, i1 in kdt.query_pairs(r):
                if i0 in merged or i1 in merged:
                    continue
                merged.extend([i0, i1])
                speed0, speed1 = simulation.points.speed[i0], simulation.points.speed[i1]
                m0, m1 = simulation.points.mass[i0], simulation.points.mass[i1]

                simulation.points.speed[i0] = (m0*speed0 + m1*speed1)/(m0 + m1)
                simulation.points.mass[i0] += m1
                
                to_delete.append(i1)
                
            if len(to_delete) > 0:
                simulation.points.delete(to_delete)


        # ----------------------------------------------------------------------------------------------------
        # Instanciates
        
        model = Mesh.IcoSphere()
        def update_viewport(simulation):
            insts = Instances(points=simulation.points, models=model, Scale=(.1*simulation.points.mass**(1/3))[:, None])
            insts.to_object("Demo Newton")
        

        # ----------------------------------------------------------------------------------------------------
        # Main
        
        rng = np.random.default_rng()
        count = 500
        
        kin = Kinematics(max_acc=20, max_speed=100)

        position, _ = distribs.disk_dist(20, count=count, seed=rng)
        speed, _ = distribs.disk_dist(10, 20, count=count, seed=rng)
        
        kin.create(position=position, speed=speed, mass=kin.rng.normal(10, 2, count))
        
        kin.add_action(merge, r=.5)

        kin.add_action(newton_law, G=1)
        
        if False:
            kin.go(update_viewport=lambda x : x.geometry.to_object("Demo Newton"))
        else:
            kin.go(update_viewport=update_viewport)
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # Reactor
    
    @staticmethod
    def demo_reactor():
        
        ctl = blender.get_empty("Reactor Control")
        ctl.location = (2, 2, 1)
        reactor = Mesh.Cylinder(fill_type=(None, 'NGON'), transformation=Transformations(position=(0, 0, 1)))
        reactor.to_object("Reactor")
        
        kin = Kinematics()
        kin.kill_old(age=.2, scale=.01)
        kin.add_action(emit, distribs.disk_dist, 1., 
                density     = lambda t: abs(100*ctl.location.z), 
                speed       = lambda t: abs(5*ctl.location.z),
                speed_scale = lambda t: abs(1*ctl.location.z),
                speed_dir   = (0, 0, -1))
        
        kin.go(update_viewport=lambda x : x.geometry.to_object("Reactor Particles"))
        
    # -----------------------------------------------------------------------------------------------------------------------------
    # Demo explode
    
    @staticmethod
    def demo_explode():
        
        rng = np.random.default_rng(0)
        
        rockets = Kinematics()
        rockets.points.age = 0
        rockets.emit(distribs.line_dist, (-10, 0, 0), (0, 10, 0), density=.1,
                    speed=20, speed_dir=(0, 0, 1), speed_scale=1, speed_dir_scale=.1)
        
        rockets.gravity()
        
        def explode(simulation):
            sel = np.argwhere(rockets.points.age >= 2)
            if len(sel) == 0:
                return
            
            sel = sel[0]
            
            for i in sel:
                count = 200
                if True:
                    speed = distribs.speed_dist(count, 10, distrib='RANDOM', speed_scale=1, seed=simulation.rng)
                else:
                    speed, _ = distribs.sphere_dist(10, count=count, scale=5, seed=simulation.rng)
                    
                simulation.points.add(count, position=rockets.points.position[i], speed=speed)
                
            rockets.points.delete(sel)
        
        particles = Kinematics()
        particles.gravity()
        particles.viscosity(10)
        particles.kill_old(3, .3)
        particles.add_action(explode)
        
        engine.init()
        
        rockets.to_engine(update_viewport=lambda x:x.geometry.to_object("Rockets"))
        particles.to_engine(update_viewport=lambda x:x.geometry.to_object("Particles"))
        
    # -----------------------------------------------------------------------------------------------------------------------------
    # Demo bounce
    
    def demo_plane_bounce():
        
        Mesh.Circle(radius=5).to_object("Demo Bounce Area")
        
        def update_viewport(balls):
            insts = Instances(points=balls.points, models=Mesh.IcoSphere(), Scale=.25)
            insts.to_object("Demo Bounce Balls")
        
        
        balls = Kinematics()
        balls.gravity()
        balls.points.age = 0
        balls.kill_old(20)
        
        balls.emit(distribs.rect_dist, 5, 5, center=(0, 0, 10), density=1, speed=3, speed_scale=.1, speed_dir='RANDOM')

        balls.add_action(bounce_on_plane, radius=5, epsilon=.25, energy_factor=.7, noise=.4)
        
        # bounce_on_plane(simulation, origin=(0, 0, 0), direction='Z', radius=None, epsilon=.1, energy_factor=.95, noise=None):

        #balls.go(update_viewport=lambda x : x.geometry.to_object("Demo Bounce Balls"))
        balls.go(update_viewport=update_viewport)
        
    def demo_surf_bounce():
        
        def update_viewport(balls):
            insts = Instances(points=balls.points, models=Mesh.IcoSphere(), Scale=.25)
            insts.to_object("Demo Bounce Balls")
        
        monkey = Mesh.Monkey(transformation=Transformations(scale=(10, 10, 10), rotation=(np.radians(-90), 0, 0)))
        monkey.to_object("Monkey")
        
        balls = Kinematics()
        balls.gravity()
        balls.points.age = 0
        balls.kill_old(20)

        balls.emit(distribs.rect_dist, 10, 10, center=(0, 0, 15), density=.1, speed=3, speed_scale=.1, speed_dir='RANDOM')
        

        balls.add_action(bounce_on_surface, monkey.faces.get_surface(), epsilon=.25, energy_factor=.3, noise=.1)
        
        balls.go(update_viewport=update_viewport, sub_steps=10)
        
        
        
        
        
        
    
            

    
    # =============================================================================================================================
    # Particles animation
    
    @staticmethod
    def anime_particles(points_list, model=None, name="Particles", dead_location=None, frame0=1, frame1=None, interpolation='LINEAR'):
        
        from geonodes.core.meshbuilder import MeshBuilder
        from geonodes.core.shapekeys import MeshShapeKeys
        
        frames = len(points_list)
        if frames == 0:
            return
        
        # ----- Number of particles
        
        count     = 0
        use_alive = False
        for points in points_list:
            count = max(count, points.size)
            use_alive = points.attributes.exists('alive') and points.attributes.exists('ID')

        # ----- Create the mesh
        
        if model is None:
            mb = MeshBuilder()
            mb.add_verts((0, 0, 0))
        else:
            mb = MeshBuilder(model)
            
        block_size = mb.verts_len
        mb = mb*count
        
        # ----- Frames shape keys 
        
        sks = MeshShapeKeys(mb, frames)
        
        sk_shape = np.shape(sks[0])
        base_points = np.reshape(sks[0], (count, block_size, 3))
        
        # ----- Loop with 0 at last key to keep origin 
        
        if not use_alive:
            work = TMatrices(shape=count)
        
        for ikey in reversed(range(frames)):
            
            points = points_list[ikey]
            
            if use_alive:
                points.scales[np.logical_not(points.alive)] = (0, 0, 0)
                if dead_location is not None:
                    points.locations[np.logical_not(points.alive)] = dead_location
                    
                sks[ikey] = np.reshape(points[:, None] @ base_points, sk_shape)
                
            else:
                work.scales = 0
                if dead_location is not None:
                    work.locations = dead_location
                
                work[:points.size] = points
                
                sks[ikey] = np.reshape(work[:, None] @ base_points, sk_shape)
                
        # ----- To object
        
        obj = sks.to_object(name)
        
        # ----- Animation

        if frame0 is not None:
            MeshShapeKeys.set_keyframes(obj, frame0=frame0, frame1=frame1, interpolation=interpolation)
        
        return obj
    
        
    # ====================================================================================================
    # Visualization
    
    def visu(self, size=10, resolution=100, z=0, speeds=0, scale=1., name="Field"):
        
        from geonodes.core.meshbuilder import MeshBuilder
        
        x, y = np.meshgrid(np.linspace(-size/2, size/2, resolution), np.linspace(-size/2, size/2, resolution))
        locs = np.stack((x, y, np.ones_like(x)*z), axis=-1)
        
        self.resize(locs.shape[:-1])
        self.locations = locs
        
        self.mass = 1
        self.viscosity = 1

        acc = self.get_acceleration(dt=.1)
        nacc = np.linalg.norm(acc, axis=-1)
        
        # ----- To object
        
        count = self.size

        mb = MeshBuilder.Circle(segments=3)*count
        mb.scale_x(.2)
        mb.scale(.05)
        
        mb.scale_y(nacc*scale)
        mb.toward(acc, track_axis='Y', up_axis='Z')
        mb.locate(locs)
        
        mb.to_object(name)
        
    # ====================================================================================================
    # Demos        
        
    # ----------------------------------------------------------------------------------------------------
    # Emitters
        
    @staticmethod
    def demo_emit(count=40, density=10, scale=.1, speed=5, speed_scale=.1, speed_angle_scale=.1, emitters=None):
        
        engine.init()
        
        simul = Simulation()
        simul.add_kill_old(3, .3)
        
        # ----- Emitters locations
        
        emit_count = 0
        center = np.zeros(3, float)
        delta  = 20
        
        def next_center(emit_count):
            emit_count += 1
            if emit_count % 4 == 0:
                center[0] = 0
                center[1] += delta
            else:
                center[0] += delta
            return emit_count
        
        # ----- Line emitter
        
        if emitters is None or 'line' in emitters:
            simul.add_emitter(distribs.line_dist, top=0, duration=10, count=count, density=density,
                    point0=(0, 0, 0), point1=(10, 10, 10), scale=scale,
                    speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, speed_pie_angle=TAU)
            emit_count = next_center(emit_count)
            
            
        if emitters is None or 'line' in emitters:
            simul.add_emitter(distribs.line_dist, top=1, duration=10, count=count, density=density,
                              point0=center+(0, 0, 0), point1=center+(10, 10, 10), scale=scale,
                               speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, speed_pie_angle=.05)
            emit_count = next_center(emit_count)

        if emitters is None or 'circle' in emitters:
            simul.add_emitter(distribs.circle_dist, top=2, duration=10, count=count, density=density,
                              radius=2, center=np.array(center), 
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, speed_pie_angle=.05)
            emit_count = next_center(emit_count)
            
        if emitters is None or 'curve' in emitters:
            curve = Curve.Spiral(start_radius=2, end_radius=4, height=4)
            curve.points.translate(center)
            
            simul.add_emitter(distribs.curve_dist, curve, top=3, duration=10, count=count, density=density,
                              t0=0., t1=1., scale=scale,
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, speed_pie_angle=.05)
            emit_count = next_center(emit_count)
            
        if emitters is None or 'rect' in emitters:
            simul.add_emitter(distribs.rect_dist, top=4, duration=10, count=count, density=density, 
                              a=6, b=4, center=np.array(center), scale=scale, z_scale=None,
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale)
            emit_count = next_center(emit_count)
            
        if emitters is None or 'disk' in emitters:
            simul.add_emitter(distribs.disk_dist, 4, top=5, duration=10, count=count, density=density,
                              center=np.array(center), scale=scale, z_scale=None,
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale)
            emit_count = next_center(emit_count)
            
        if emitters is None or 'cylinder' in emitters:
            simul.add_emitter(distribs.cylinder_dist, top=6, duration=10, count=count, density=density,
                              point0=center + (0, 0, 0), point1=center+(0, 0, 10), radius=3, scale=scale, 
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, )
            emit_count = next_center(emit_count)
            
        if emitters is None or 'sphere' in emitters:
            simul.add_emitter(distribs.sphere_dist, 4, top=7, duration=10, count=count, density=density,
                              center=np.array(center), scale=scale,
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, )
            emit_count = next_center(emit_count)
            
        if emitters is None or 'surface' in emitters:
            monkey = Mesh.Monkey()
            monkey.points.scale(3)
            monkey.points.translate(center)
            
            simul.add_emitter(distribs.surface_dist, monkey.faces.get_surface(), top=8, duration=10, count=count, density=density,
                              scale=scale,
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, )
            emit_count = next_center(emit_count)
            
        if emitters is None or 'cube' in emitters:
            simul.add_emitter(distribs.cube_dist, top=9, duration=10, count=count, density=density,
                              corner0=center + (-2, -2, -2), corner1=center+(2, 2, 2), scale=scale,
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, )
            emit_count = next_center(emit_count)
            
        if emitters is None or 'ball' in emitters:
            simul.add_emitter(distribs.ball_dist, 2, top=10, duration=10, count=count, density=density, scale=scale,
                              center=np.array(center), 
                              speed=speed, speed_scale=speed_scale, speed_angle_scale=speed_angle_scale, )
            emit_count = next_center(emit_count)
            
        # ----- Launch
            
        simul.to_engine(to_object="Demo Emit")
        
    # ----------------------------------------------------------------------------------------------------
    # Tracks
        
    def demo_track():
        
        # ----- Balls
        
        count = 20
        balls = Points()
        balls.init_simulation()
        balls.add_gravity()
        balls.add_action(lambda points: points.kill(points.z <= 0))
        
        locs, speeds = distribs.rect_dist(40, 5, count=count,
                            speed=50, speed_scale=3, speed_angle_scale=.2, seed=balls.seed)
                            
        balls.create(tops = balls.rng.uniform(0, 5, count),
            locations         = locs,
            speeds            = speeds,
            )
        
        balls.set_reset_state()
    
        # ----- Particles
            
        particles = Points()
        particles.init_simulation()
        particles.add_kill_old(3, .5)
        particles.add_viscosity()
        particles.add_emit_track(balls, distribution='SEGMENT', radius=.5, count=0, density=100., distance=None, 
            speed=10., speed_scale=3, speed_angle_scale=.5, stop_when_locked=False, seed=0)
        
        #balls.add(locations=balls.rng.uniform(-5, 5, (1000, 3)))
            
        particles.set_reset_state()
            
        def setup():
            print("SETUP INIT")
            balls.reset()
            particles.reset()
            print("SETUP DONE")
            
        def update(eng):
            balls.to_mesh_object("Balls")
            balls.step(1/24)
            
            particles.to_mesh_object("Particles")
            particles.step(1/24)
            
        engine.go(update, setup)        
        
        
            
            
        
# ====================================================================================================
# Demos

def demo_surface():
    # ----- Let's create Suzan
    
    monkey = MeshBuilder.Monkey()
    
    # ----- We select the faces facingupwards
    
    faces = monkey.normals()[:, 2] > 0.1
    surf = monkey.get_surface(faces)
    
    # ----- Let's locate points on the faces with a certain density
    
    locs, normals = Points.surf_locs(surf, density=100.)
    
    # ----- To object
    
    mb = MeshBuilder.Cube(size=.05)*len(locs)
    
    # Orient according the normals
    mb.toward(normals)
    
    # Locate at the points positions
    mb.locate(locs)
    
    monkey.append(mb)
    
    monkey.to_object("Points on Suzan", shade_smooth=False)

def demo_wind():
    import numpy as np
    
    from geonodes.core.points import Points
    from geonodes.core.meshbuilder import MeshBuilder
    
    from geonodes.core import engine
    
    engine.init()
    
    rng = np.random.default_rng(0)
    
    count = 200
    max_count = 10000
    points = Points(rng=rng)
    points.init_simulation()
    
    points.add_gravity()
    points.add_wind(
        force        = 20, 
        axis         = 'Y', 
        viscosity    = 1., 
        power        = 2, 
        noise        = 3, 
        noise_scale  = .5, 
        noise_detail = 3, 
        time_scale   = 10,
        )
    
    def update(scene):
        
        # Add some points
        n = min(count, max_count - len(points))
        if n > 0:
            points.add(
                position  = Points.normal_sphere_locs(count=n, scale=10, seed=points.seed) + (0, 0, 10),
                speed     = Points.normal_sphere_locs(count=n, scale=5, seed=points.seed),
                mass      = rng.normal(1, .3, n),
                viscosity = rng.normal(3, .5, n),
                )
    
        print("Count", len(points))
        print("Max speed", np.max(np.linalg.norm(points.speeds, axis=-1)))
                
        # Simulation
        
        points.step(1/25, sub_steps=1)
        
        #  Delete particle on the ground
        
        points.kill(points.z < 0)
        
        # ----- To object
        
        mb = MeshBuilder.Cube(.5)*len(points)
        mb.transform(points)
        mb.to_object("Wind")
    
    engine.go(update)
    
def demo_centrifugal():
    
    # ----- Free fall in a rotating frame
    # This demo illustrates free falls of 10 balls into a centrifugal frame
    # The trajectories of the balls are illustrated with curves
    
    import numpy as np
    
    from geonodes.core.points import Points
    from geonodes.core.meshbuilder import MeshBuilder
    from geonodes.core.curvebuilder import PolyBuilder
    
    from geonodes.core import engine
    
    engine.init()
    
    count = 10
    points = Points(locations=Points.line_locs((-10, -10, 0), (10, -10, 0), count))
    points.init_simulation(speeds=(0, 0, 0))
    
    points.add_centrifugal(omega=1)
    
    curves = points.sim_curves(duration=10, count=100, sub_steps=1)
    
    cb = PolyBuilder()
    cb.add_splines(curves)
    
    # ----- To object
    
    balls = MeshBuilder.UVSphere()*count
    balls.to_object("Balls")
    
    obj = cb.to_object("Centrifugal")
    obj.data.bevel_depth = .05
    obj.data.bevel_factor_end = 0
    
    def update(scene):
        obj.data.bevel_factor_end  = scene.time/10
        balls.locate(cb(scene.time/10))
        balls.update_object("Balls")
        
    engine.go(update)
    


    
    
    
     

    
    
    
        
        
        
        
        
        
        
        
        
            
    
    
    
