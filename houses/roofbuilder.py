#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 06:07:19 2023

@author: alain
"""

import numpy as np
from math import cos, sin, pi, atan2
from mathutils import Vector, Matrix

from geopy.core import geo2D
from geopy.core.meshbuilder import MeshBuilder

from geopy.houses.constants import *

ZERO = 0.01

def svect(v, ok_z=False):
    return f"[{v[0]:4.1f} {v[1]:4.1f}]"

# ====================================================================================================
# Profile 

class Profile(list):
    def __init__(self, *pts, location=(0., 0., 0.), angle=0.):
        """ Roof profile.
        
        A profile is defined by a list of points where z is function of x.
        
        The profile is located and rotated along the walls of a building.
        The points of the profile can be moved along y axis to extrude the shape of the roof.
        
        The intersection between two profiles can be calculated to form a full roof.
        
        **Note** : 'angle' correspond to a *horizontal* profile, i.e. a *vertical* roof pane.
        
        The conventions are: 
            - z are decreasing from the top of the roof down to the bottom.
            - x are growing from negative values to 0
            
        With theses convention, the last point should always be (0, 0, 0). 
        A simple slope of height 2 and width 3 is initialized with:
        
        ``` python
        profile = Profile((-3., 0., 2.), (0., 0., 0.))
        ```
        
        Args:
            - *pts (Vectors) : The list of points along the roof profile
            - location (Vector = (0, 0, 0)) : the location of the profile
            - angle (float = 0.) : the rotation of the profile
        """
        
        super().__init__()
        self.extend([Vector(pt) for pt in pts])
        self.location = Vector(location)
        self.angle    = angle
        
    def __str__(self):
        return f"<Profile of {len(self)} points: [{self.x0:.1f} {self.x1:.1f}] -> [{self.z1:.1f} {self.z0:.1f}]>"
        
    @property
    def xs(self):
        """ List of x values.
        
        Returns:
            - array of floats : the x values of the profile points.
        """
        return [v.x for v in self]
        
    @property
    def zs(self):
        """ List of z values.
        
        Returns:
            - array of floats : the z values of the profile points.
        """
        return [v.z for v in self]
        
    @property
    def z0(self):
        """ Minimum z value.
        
        Returns:
            - float : minimum z value
        """
        return self[-1].z
        
    @property
    def z1(self):
        """ Maximum z value.
        
        Returns:
            - float : maximum z value
        """
        return self[0].z
        
    @property
    def x0(self):
        """ Minimum x value.
        
        Returns:
            - float : minimum x value
        """
        return self[0].x
        
    @property
    def x1(self):
        """ Maximum x value.
        
        Returns:
            - float : maximum x value
        """
        return self[-1].x
    
    @property
    def width(self):
        return self.x1 - self.x0
    
    @property
    def height(self):
        return self.z1 - self.z0
    
    def scale(self, scale_x, scale_z=None, max_slope=1, max_height=2.5):
        
        new_width = self.width*scale_x
        new_height = self.height*(scale_x if scale_z is None else scale_z)
        if new_height/new_width > max_slope:
            scale_z = max_slope*new_width/self.height
            
        if new_height > max_height:
            scale_z = max_height/self.height
        
        for v in self:
            v.x *= scale_x
            v.z *= scale_x if scale_z is None else scale_z
            
    def change_width(self, width, max_slope=.9, max_height=2.5):
        prof = Profile(*self)
        prof.scale(width/self.width, max_slope=max_slope, max_height=max_height)
        return prof
    
    @property
    def bot_slope(self):
        """ Slope of the last wsegmet of the profile.
        
        Used to compute the overhang.
        
        Returns:
            - float : slope of the last segment
        """
        return -(self[-1].z - self[-2].z)/(self[-1].x - self[-2].x)
    
    # ====================================================================================================
    # Some constructors
        
    @classmethod
    def Slope(cls, width, height, max_slope=1, location=(0, 0, 0), angle=0.):
        """ Create a simple slope roof profile.
        
        Args:
            - width (float) : profile width (typically half of the building width)
            - height (float) : profile height (roof height)
            - location (Vector = (0, 0, 0)) : the location of the profile
            - angle (float = 0.) : the rotation of the profile
        
        Returns:
            - Profile : a roof profile
        """
        slope = height/width
        if slope > max_slope:
            height = max_slope*width
        return cls((-width, 0, height), (0, 0, 0), location=location, angle=angle)
        
    @classmethod
    def Ridge(cls, width, height, ridge_width, ridge_height, location=(0, 0, 0), angle=0.):
        """ Create a roof profile with a ridge.
        
        Args:
            - width (float) : profile width (typically half of the building width)
            - height (float) : profile height (roof height)
            - ridge_width (float) : x location of the ridge
            - ridge_height (float) : z location of the ridge
            - location (Vector = (0, 0, 0)) : the location of the profile
            - angle (float = 0.) : the rotation of the profile
        
        Returns:
            - Profile : a roof profile
        """
        return cls((-width, 0, height), (-ridge_width, 0, ridge_height), (0, 0, 0), location=location, angle=angle)
    
    @classmethod
    def Circular(cls, width, height, count=5, exp=1, location=(0, 0, 0), angle=0.):
        """ Create a circular roof profile.
        
        Args:
            - width (float) : profile width (typically half of the building width)
            - height (float) : profile height (roof height)
            - count (int=5) : number of segments
            - location (Vector = (0, 0, 0)) : the location of the profile
            - angle (float = 0.) : the rotation of the profile
        
        Returns:
            - Profile : a roof profile
        """
        return cls(*[(width*(sin(ag) - 1), 0, height*cos(ag)) for ag in [i**exp*pi/2/(count-1)**exp for i in range(count)]],
                   location=location, angle=angle)

        return cls(*[(width*(sin(ag) - 1), 0, height*cos(ag)) for ag in [i*pi/2/(count-1) for i in range(count)]],
                   location=location, angle=angle)
    
    @classmethod
    def CircularInverse(cls, width, height, count=5, exp=1, location=(0, 0, 0), angle=0.):
        """ Create an inversed circular roof profile.
        
        Args:
            - width (float) : profile width (typically half of the building width)
            - height (float) : profile height (roof height)
            - count (int=5) : number of segments
            - location (Vector = (0, 0, 0)) : the location of the profile
            - angle (float = 0.) : the rotation of the profile
        
        Returns:
            - Profile : a roof profile
        """
        return cls(*[(-width*cos(ag), 0, height*(1-sin(ag))) for ag in [i**exp*pi/2/(count-1)**exp for i in range(count)]],
                   location=location, angle=angle)
    
    # ====================================================================================================
    # Returns a covpy with an overhang
    
    def overhanged(self, overhang=.2):
        """ Returns a copy with an overhang outside of the wall.
        
        If the bottom slope is high, the last part of the roof could go very low.
        It is capped to 30 cm.
        
        Args:
            - overhange (float=.2) : the x value to extend the profile
            
        Returns:
            - Profile : a profile a going a little bit farther in the x direction.
        """
        
        if overhang < ZERO:
            return self
        
        prof = Profile(*self, location=self.location, angle=self.angle)
        
        new_x = self.x1 + overhang
        new_z = self.z(new_x)
        
        # ------ For almost vertical slope too long overhang
        
        if new_z - prof[-1].z < -.3:
            prof[-1].z -= .3
            prof[-1].x += .3/self.bot_slope
            
        # ----- Overhang is good
        else:
            prof[-1].x = new_x
            prof[-1].z = new_z
            
        return prof
        

    # ====================================================================================================
    # x and z relationship
        
    def z(self, x):
        """ z function of x.
        
        The profile points provide a function giving z from x.
        
        Args:
            - x : float
        
        Returns:
            - float : z
        """
        
        if x <= self.x0:
            p0 = self[0]
            p1 = self[1]
            
        elif x >= self.x1:
            p0 = self[-2]
            p1 = self[-1]
            
        else:
            for i, pt  in enumerate(self):
                if x <= pt.x:
                    p0 = self[i-1]
                    p1 = pt
                    break
                
        return p0.z + (x - p0.x)/(p1.x - p0.x)*(p1.z - p0.z)
    
    def x(self, z):
        """ x function of z.
        
        The profile points provide a function giving x from z.
        
        Args:
            - z : float
        
        Returns:
            - float : x
        """
        
        if z >= self.z1:
            p0 = self[0]
            p1 = self[1]
            
        elif z <= self.z0:
            p0 = self[-2]
            p1 = self[-1]
            
        else:
            for i, pt  in enumerate(self):
                if z >= pt.z:
                    p0 = self[i-1]
                    p1 = pt
                    break
                
        return p0.x + (z - p0.z)/(p1.z - p0.z)*(p1.x - p0.x)
    
    # ====================================================================================================
    # Location in space
    
    @property
    def rotation_matrix(self):
        """ Rotation Matrix.
        
        Returns:
            Matrix : rotation matrix around z axis of 'angle'
        """
        return Matrix.Rotation(self.angle, 3, 'Z')
    
    def located(self, y=0.):
        """ Profile points located a y, translated and rotated.
        
        The profile points are first translate at the required 'y' location.
        They are then rotated and translated according the 'location' and 'angle' atrributes.
        
        Returns:
            - list of points : the profile points
        """
        
        M = self.rotation_matrix
        return [self.location + M @ (v + Vector((0., y, 0.))) for v in self]
    
    def locate_zs(self, zs, y=0.):
        """ Locate points at the provided coordinates along z axis.
        
        This method is used to compute the intersection with another profile. The other profile
        gives the 'z' values of the intersection points which are required.
        
        Args:
            - zs (list of floats) : the z values
            - y (float) : the y value
            
        Returns:
            - list of Vectors : points on the profile with the required 'z'.
        """
        
        M = self.rotation_matrix
        return [self.location + M @ Vector((self.x(z), y, z)) for z in zs]
    
    # ====================================================================================================
    # Intersection with another profile
    
    def intersect(self, other, overhang=None):
        """ Intersection with another profile.
        
        The intersection is computed by moving the other profile relatively to the current profile.
        
        Once move, the current profile is located at the origine and is not rotated. The extrusion
        is a set of lines along y axis. Their equation is 'x = constant'.
        
        The extrusion lines of the othe profile are lines passing via the rotated points and in the direction
        given by the angle.
        
        The intersection is given by the intersection of these two sets of lines.
        
        **Note** : this is not a completely symmetrical function because the points are calculated on the z values
        of the current Profile.
        
        Args:
            - other (Profile) : the profile to intesect with
            - overhang (float = None) : if not None, compute the intesection with the overhanged versions
            
        Returns:
            - list of Vector : the intesection line between the two profiles
        """
        
        # ----- Let's work with the overhanged versions if ncessary
        
        if overhang is not None:
            return self.overhanged(overhang).intersect(other.overhanged(overhang))
        
        # ----------------------------------------------------------------------------------------------------
        # First, let's place the other profile in the referential of the current profile
        
        M = Matrix.Rotation(-self.angle, 3, 'Z')
        
        # Let's compute the projection of the z values on to the other profile

        verts = [M @ (v - self.location) for v in other.locate_zs(self.zs, 0)]
        
        # We can only use values in the range of the other profile z values

        z0 = max(self.z0, other.z0)
        z1 = min(self.z1, other.z1)

        # All the lines of the other profile have the same slope in the (x, y) plane

        angle = other.angle - self.angle
        slope = -cos(angle)/sin(angle)
        
        # ----------------------------------------------------------------------------------------------------
        # We can now compute the intersection ridge
        
        points = []
        for v in verts:
            if v.z < z0 - ZERO or v.z >z1 + ZERO:
                continue
            
            x = self.x(v.z)
            points.append(Vector((x, v.y + (x - v.x)*slope, v.z)))
            
        assert(points)
        
        # ----------------------------------------------------------------------------------------------------
        # The intersection was calculated in the current profile
        # We must return the result in the world coordinates
            
        M = Matrix.Rotation(self.angle, 3, 'Z')
        ridge = [self.location + M @ v for v in points]
            
        return ridge    

    # ====================================================================================================
    # Debug
    
    def to_object(self, name="Profile", length=10):
        
        mb = MeshBuilder()

        M = self.rotation_matrix
        larg = Vector((0, length/2, 0))
        
        mb.add_verts([self.location + (M @ (v - larg)) for v in self])
        mb.add_verts([self.location + (M @ (v + larg)) for v in self])
 
        n = len(self)
        mb.add_faces([[i, i+1, n+i+1, n+i] for i in range(len(self)-1)])
        mb.to_object(name)
        
# ====================================================================================================
# Roof Sides

# ----------------------------------------------------------------------------------------------------
# Root for Gabble or Pane

class RoofSide:
    def __init__(self, p0, p1):
        """ A RoofSide is used to described how to render a wall.
        
        A full roof can be seen as a closed chain of roof sides.
        
        A roof side can be a profile or a gable.
        
        **Note** : the segment are oriented: the roof is place on the left when going from p0 to p1.
        
        Args:
            - p0 (Vector) : first point of the wall segment
            - p1 (Vector) : second point of the wall segment
        """
    
        self.p0 = Vector(p0)
        self.p1 = Vector(p1)
        self.length = (self.p1 - self.p0).length
        self.angle = -atan2(self.p1.x - self.p0.x, self.p1.y - self.p0.y)
        
        self.prev_pane  = None
        self.next_pane = None
        
        self.has_profile = False
        
    def __str__(self):
        return f"<{type(self).__name__}: {svect(self.p0)} {svect(self.p1)}, location: {svect((self.p0 + self.p1)/2)}, length: {self.length:4.1f}, angle: {np.degrees(self.angle):.0f}°"
    
    # ====================================================================================================
    # Contains a point
    
    def contains(self, p):
        
        p  = Vector(( p[0],  p[1]))
        p0 = Vector((self.p0[0], self.p0[1]))
        p1 = Vector((self.p1[0], self.p1[1]))
        
        v0, v1 = p - p0, p - p1        
        l0, l1 = v0.length, v1.length
        
        if l0 < ZERO or l1 < ZERO:
            return True
        
        u = (p1 - p0).normalized()
        
        if False:
            O = p0
            print(f"P0: [0, 0] P1: [{(p1-O).x:5.1f}, {(p1-O).y:5.1f}], P: [{(p-O).x:5.1f}, {(p-O).y:5.1f}] -> {abs(v0.dot(u) - l0) < ZERO}, {(v0.dot(u) - l0):5.1f}")
        
        if l0 > l1:
            return abs(v0.dot(u) - l0) < ZERO
        else:
            return abs(v1.dot(u) - l1) < ZERO

    def to_builder(self, mb, height=0.):
        pass
    
    # ====================================================================================================
    # Plug a rectangular surface
    
    def plug_rectangle(self, rect, profile):

        rel = geo2D.connected_side(self.p0, self.p1, rect)
        assert(rel is not None)
        
        roof = Roof.Rectangular(rect, profile, start_index=rel['minor_index'], connect=True)
        
        return roof
    
    def elevate_contour(self, verts):
        zs = np.array(verts)
        zs[:, 2] = 0
        return zs
    
    
# ----------------------------------------------------------------------------------------------------
# Root for Gabble or Pane

class RoofDebug(RoofSide):
    def to_builder(self, mb, height=0.):
        h = 10
        mb.add_surface(np.array([self.p0, self.p1, self.p1 + Vector((0, 0, h)), self.p0 + Vector((0, 0, h))]) + (0, 0, height))

# ----------------------------------------------------------------------------------------------------
# A gable, with a possible cut
        
class Gable(RoofSide):
    def __init__(self, p0, p1, cut=None):
        """ A gable roof side.
        
        A gable, or pinion, doesn't roof pane. It is used to elevate the wall up to the neighbour roof sides.
        
        Args:
            - p0 (Vector) : first point of the wall segment
            - p1 (Vector) : second point of the wall segment
            - cut (Profile=None) : roof cut at the top of the gable (not yet implemented)
        """
        
        super().__init__(p0, p1)
        self.cut = cut
        
    # ====================================================================================================
    # To builder
        
    def to_builder(self, mb, height=0.):
        v0 = self.prev_pane.ridge1(dx=0, dy=0)
        v1 = self.next_pane.ridge0(dx=0, dy=0)
        
        mb.add_surface(np.array(v0 + [p for p in reversed(v1)]) + (0, 0, height), mat=WALL)
        
# ----------------------------------------------------------------------------------------------------
# A profiled pane

class RoofPane(RoofSide):
    def __init__(self, p0, p1, profile):
        """ A roof pane.
        
        A roof pane is based on a profile. It computes the intersection with its two neighbour sides.
        
        When a neighbour is a gable, it stops with a certain overhang.
        When a neighbour is another roof pane, it computes the intersection ridge with it.
        
        A roof pane can also be plugged in another roof.
        
        The profile passed in argument is located and oriented as necessary.
        
        Args:
            - p0 (Vector) : first point of the wall segment
            - p1 (Vector) : second point of the wall segment
            - profile (Profile) : the roof profile.
        """
        
        super().__init__(p0, p1)
        
        self.profile = Profile(*profile, location=(self.p0 + self.p1)/2, angle=self.angle)
        self.has_profile = True
        
        self.left_plug  = None
        self.right_plug = None
        
        self.extends = []
        
    # ====================================================================================================
    # The ridges
    
    # ----------------------------------------------------------------------------------------------------
    # Left ridge
        
    def ridge0(self, dx=0., dy=0.):
        """ First, or left, ridge.
        
        Three possible cases can occur:
            - the roof pane is plugged into another roof pane
            - the roof pane intersects with with another roof pane
            - the roof ends on to a gable
            
        This for the two extremities.
        
        Args:
            - dx (float=0.) : overhang along x
            - dy (float=0.) : overhang along y
            
        Returns:
            - list of Vectors : the left most part of the pane
        """
        
        # ----- Plug into another roof
        
        if self.left_plug is not None:
            return self.profile.intersect(self.left_plug.profile, overhang=dx)
        
        # ----- Previous pane has also a profile
        
        if self.prev_pane.has_profile:
            return self.profile.intersect(self.prev_pane.profile, overhang=dx)
        
        # ----- Previous pane is a gable
        
        points = self.profile.overhanged(dx).located(-self.length/2 - dy)
        
        ag = pi/2 - (self.angle - self.prev_pane.angle)
        if abs(ag) > ZERO:
            M = Matrix.Rotation(ag, 3, 'Z')
            O = self.profile.located(-self.length/2 - dy)[-1]
            for i in range(len(points)):
                points[i] = O + M @ (points[i] - O)
        return points
    
    # ----------------------------------------------------------------------------------------------------
    # Right ridge
            
    def ridge1(self, dx=0, dy=0):
        """ Second, or right, ridge.
        
        Three possible cases can occur:
            - the roof pane is plugged into another roof pane
            - the roof pane intersects with with another roof pane
            - the roof ends on to a gable
            
        This for the two extremities.
        
        Args:
            - dx (float=0.) : overhang along x
            - dy (float=0.) : overhang along y
            
        Returns:
            - list of Vectors : the left most part of the pane
        """
        
        # ----- Plug into another roof
        
        if self.right_plug is not None:
            return self.profile.intersect(self.right_plug.profile, overhang=dx)
        
        # ----- Next pane has also a profile
        
        if self.next_pane.has_profile:
            return self.profile.intersect(self.next_pane.profile, overhang=dx)

        # ----- Next pane is a gable
        
        points = self.profile.overhanged(dx).located(self.length/2 + dy)

        ag = pi/2 - (self.next_pane.angle - self.angle)
        if abs(ag) > ZERO:
            M = Matrix.Rotation(-ag, 3, 'Z')
            O = self.profile.located(self.length/2 + dy)[-1]
            for i in range(len(points)):
                points[i] = O + M @ (points[i] - O)
                
        return points

    # ====================================================================================================
    # Build the pane
    
    def build(self):
        
        # LATER
    
        # ----- Sorted bot neighbours
        
        exts = sorted([index for index, (loc, _) in enumerate(self.extends) if loc[1] < 0],
                     key=lambda index: self.extends[index][0][0])
        
        # ----- Bottom shape depending on the neighbour surfaces
        
        overhang = .2
        locs  = [(self.x0, 0, -overhang)]  # x location, y extra, x overhang
        
        def move_x(x, ovh):
            if x - locs[-1][0] > ZERO:
                locs.append((x, locs[-1][1], ovh))
            
        def move_y(extra):
            if abs(extra - locs[-1][1]) > ZERO:
                locs.append((locs[-1][0], extra, locs[-1][2]))
                
        for i in exts:
            loc, bounds = self.extends[i]
            x0, x1 = loc[0] - bounds[0]/2, loc[0] + bounds[0]/2
            extra = bounds[1]
            
            move_x(x0, -overhang)
            move_y(-extra)
            move_x(x1, overhang)
            move_y(0)
            
        move_x(self.x1, overhang)
        
        # ---- Build the faces
        
        left_prof  = self.profile.profile(x=self.x0 - overhang)
        right_prof = self.profile.profile(x=self.x1 + overhang)
        
        to_z   = self.profile.z + self.profile.height
        from_z = to_z - .7
        
        if len(left_prof) == 3:
            pane = Roof.side_cut([left_prof[0], left_prof[1]], from_z, to_z, .7)
            pane.extend(Roof.side_cut([right_prof[1], right_prof[0]], from_z, to_z, -.7))
            mb.add_surface(pane)
            
        pane = self.left_side.pane_left()
        pane.extend([self.profile.point(loc[0] + loc[2], self.y0 + loc[1] - overhang) for loc in locs])
        pane.extend(self.right_side.pane_right())
        
        mb.add_surface(pane)
        
        pane = self.left_side.left_roof_pane()
        if pane is not None:
            mb.add_surface(pane, mat=ROOF)
            
        # ----- Left gable
        
        wall = self.left_side.left_gable()
        if wall is not None:
            mb.add_surface(wall, mat=WALL)
        
        # ----- Extra wall
        
        if self.profile.z > ZERO:
            for i, loc in enumerate(locs[:-1]):
                nxt = locs[i+1]
                v0 = (loc[0], self.y0 + loc[1], 0)
                v1 = (nxt[0], self.y0 + nxt[1], 0)
                mb.add_surface([v0, v1, (v1[0], v1[1], self.profile.z_roof(v1[1]) - ZERO), (v0[0], v0[1], self.profile.z_roof(v0[1]) - ZERO)], mat=WALL)
                
            
    # ====================================================================================================
    # Plug a rectangular surface
    
    def plug_rectangle(self, rect, profile):
        
        rel = geo2D.connected_side(self.p0, self.p1, rect)
        assert(rel is not None)
        
        index = rel['minor_index']
        
        roof = Roof.Rectangular(rect, profile, start_index=index, connect=True)
        
        # Strange.... (certainly due to orientation)
        index = (index + 1) % 4
        
        roof[(index - 1)%len(roof)].right_plug = self
        roof[(index + 1)%len(roof)].left_plug  = self
        roof[index] = RoofSide(roof[index].p0, roof[index].p1)
        
        return roof
    
    # ====================================================================================================
    # Return the base contour
    
    def base(self):
        
        v0 = self.ridge0(dx=0, dy=0)
        v1 = self.ridge1(dx=0, dy=0)
        
        return np.array(v0 + [p for p in reversed(v1)])

    # ====================================================================================================
    # Return the elevated contour
    
    def elevate_contour(self, verts, mb):
        
        v0 = self.ridge0()
        v1 = self.ridge1()
        
        angle = geo2D.segment_angle(self.p0, self.p1)
        
        left  = geo2D.rotate([v for v in reversed(v0)], -angle, pivot=self.p0)
        right = geo2D.rotate([v for v in reversed(v1)], -angle, pivot=self.p0)
        
        contour = geo2D.rotate(verts, -angle, pivot=self.p0)
        
        # ----- Points below the pane
        series = []
        for i, p in enumerate(contour):
            ld = geo2D.distance_to_line(left, p)
            if ld is None or ld < 0:
                continue
            
            rd = geo2D.distance_to_line(right, p)
            if rd is None or rd > 0:
                continue
            
            if len(series) == 0 or series[-1][-1][0] != i-1:
                series.append([[i, p, ld, None]])
            else:
                series[-1].append([i, p, ld, None])
                
        # ----- Join last to first
        if len(series) > 1:
            if series[-1][-1][0] == len(contour)-1 and series[0][0][0] == 0:
                series[0] = series[-1] + series[0]
                del series[-1]
                
        INDEX, POINT, LEFT, DIREC = 0, 1, 2, 3

        # ----- Directions
        for serie in series:
            for i, item in enumerate(serie):
                if i == 0:
                    item[DIREC] = 0
                else:
                    diff = item[LEFT] - serie[i-1][LEFT]
                    if abs(diff) < ZERO:
                        item[DIREC] = serie[i-1][DIREC]
                    else:
                        item[DIREC] = -1 if diff < 0 else 1
                        for j in reversed(range(i)):
                            if serie[j][DIREC] == 0:
                                serie[j][DIREC] = item[DIREC]
                            else:
                                break
                            
        print('*'*20)
        print("\nSeries", len(series))
        for isr, sr in enumerate(series):
            print(f"{isr}: {[item[INDEX] for item in sr]} {[item[DIREC] for item in sr]}")
            print([f"{item[LEFT]:4.1f}" for item in sr])
                
        # ----- Split the series with their direction
        parts = []
        for serie in series:
            cur = None
            for item in serie:
                if cur is None or cur[-1][DIREC] != item[DIREC]:
                    cur = [item]
                    parts.append(cur)
                else:
                    cur.append(item)
                    
        print("\nParts", len(parts))
        for isr, sr in enumerate(parts):
            print(f"{isr}: {[item[INDEX] for item in sr]} {[item[DIREC] for item in sr]}")
            print([f"{item[LEFT]:4.1f}" for item in sr])
            
        # ----------------------------------------------------------------------------------------------------
        # Build the parts of the pane
                
        cut = [v for v in reversed(v0)]
        cut.extend(v1)
        
        return np.array(cut)
    
    
        
        y0 = self.p0[1]
        for item in insides:
            v = item[0]
            v[2] = self.profile.z(p[1] - y0)
            cut.append(v)
        
        cut.extend(v1)
        
        # DEBUG
        mb.add_surface(cut)

        return np.array(cut)
    
    
    # ====================================================================================================
    # To builder
        
    def to_builder(self, mb, height=0.):
        
        v0 = np.array(self.ridge0(dx=.2, dy=.2)) + (0, 0, height)
        v1 = np.array(self.ridge1(dx=.2, dy=.2)) + (0, 0, height)
        
        # ----- UV Map
        
        n = len(v0) - 1
        assert(n == len(v1) - 1)
        
        widths = np.append([0], np.cumsum(np.linalg.norm(np.roll(v0, -1, 0)[1:] - v0[:-1], axis=-1)))
        length = geo2D.length(self.p0, self.p1)
        
        uvs = np.zeros((n, 4, 2), float)
        uvs[:, [1, 2], 0] = length
        uvs[:, 0, 1] = widths[:n]
        uvs[:, 1, 1] = widths[:n]
        uvs[:, 2, 1] = widths[1:]
        uvs[:, 3, 1] = widths[1:]
        uvs = np.reshape(uvs, (n*4, 2))
        
        # ----- Add the surfaces

        ofs0, n = mb.add_verts(v0)
        ofs1, _ = mb.add_verts(v1)
        
        mb.add_faces([[ofs0 + i, ofs0 + i + 1, ofs1 + i + 1, ofs1 + i] for i in range(n-1)], mat=ROOF, UVMap=uvs)
        
# ====================================================================================================
# A roof made of sides
        
class Roof(list):
    
    def __init__(self): #, sides, profile, options=[]):
        super().__init__()
        self.contour = None
        self.flat    = False
        
    # ====================================================================================================
    # Rectangular roof
        
    @classmethod
    def Rectangular(cls, verts, profile, start_index=0, connect=True):
        
        assert(len(verts)==4)
        
        lgs = geo2D.lengths(verts)
        width = lgs[start_index]
        profile = profile.change_width(width/2)
        
        roof  = cls()
        for i in range(4):
            p0 = verts[(start_index + i)     % 4]
            p1 = verts[(start_index + i + 1) % 4]
            
            if i % 2 == 0:
                roof.add_gable(p0, p1)
            else:
                roof.add_pane(p0, p1, profile=profile)
                
        if connect:
            roof.connect_sides()
            
        return roof
    
    # ====================================================================================================
    # Cover a complex contour
    
    @classmethod
    def CoverContour(cls, contour, profile, overhang=.2):
        
        angle = geo2D.average_angle(contour)
        
        #P0 = np.min(contour, axis=0)
        #P1 = np.max(contour, axis=0)
        #O = (P0 + P1)/2
        
        O = (0, 0, 0)
        dims  = geo2D.rotate(contour, -angle, pivot=O)
        p0 = np.min(dims, axis=0)
        p1 = np.max(dims, axis=0)
        
        length = p1[0] - p0[0] + 2*overhang
        width  = p1[1] - p0[1] + 2*overhang
        
        ovh = overhang + .3 # Some margin
        
        corners = np.array([(p0[0] - ovh, p0[1] - ovh, 0), (p1[0] + ovh, p0[1] - ovh, 0), (p1[0] + ovh, p1[1] + ovh, 0), (p0[0] - ovh, p1[1] + ovh, 0)])
        corners[:, 2] = p0[2]
        rect = geo2D.rotate(corners, angle, pivot=0)
        
        roof = cls.Rectangular(rect, profile)
        roof.contour = contour
        
        # BOOLEAN BUG :-(
        if len(contour) > 10:
            roof.flat = True
        
        return roof

    # ====================================================================================================
    # Building methods
    
    def add_pane(self, p0, p1, profile, extends=[]):
        self.append(RoofPane(p0, p1, profile))
        return self[-1]
        
    def add_gable(self, p0, p1, cut=None):
        self.append(Gable(p0, p1))
        return self[-1]
        
    def add_hidden(self, p0, p1):
        self.append(RoofSide(p0, p1))
        return self[-1]
    
    def connect_sides(self):
        for i, pane in enumerate(self):
            pane.prev_pane = self[(i-1)%len(self)]
            pane.next_pane = self[(i+1)%len(self)]

    # ====================================================================================================
    # To builder
    
    def to_builder(self, mb, height=0.):
        
        if self.contour is None:
            for i, pane in enumerate(self):
                pane.to_builder(mb, height=height)
                
        elif self.flat:
            base = mb.add_surface(geo2D.inset(self.contour, .2), mat=FLAT_ROOF)
            mb.extrude(mb.get_face_ring(base), height=.3, mat=ROOF_BORDER, top_mat=FLAT_ROOF)
                
        else:
            # ----------------------------------------------------------------------------------------------------
            # Cut the roof with an inset body
            
            # House inset with the proper overhang
            
            house = MeshBuilder()
            base  = house.add_surface(geo2D.inset(self.contour, -.2))
            house.extrude(house.get_face_ring(base), height=10, top_mat=0)

            # Solidifed roof
            
            roof = MeshBuilder()
            for pane in self:
                if isinstance(pane, Gable):
                    continue
                pane.to_builder(roof)
                
            roof.remove_doubles(.01)
            solidified = roof.solidify(thickness=.1, offset=1.)
            
            # Boolean

            cut_roof = solidified.intersect(house, solver='FAST')
            cut_roof.verts[:, 2] += height
            
            cut_roof.unwrap_faces()
            
            # Roof border material is WALLL not ROOF
            # change to ROOF BORDER

            cut_roof.change_material(WALL, ROOF_BORDER)
            
            mb.append(cut_roof)
            
            # ----------------------------------------------------------------------------------------------------
            # Cut the house with the roof to obtain the gables
            
            # house without inset
            
            house = MeshBuilder()
            base  = house.add_surface(self.contour, mat=WALL)
            house.extrude(house.get_face_ring(base), height=10, top_mat=0)

            # Extrude the roof upwards to a higher altitude
            
            faces = roof.extrude_faces([i for i in range(roof.faces_count)], height=20, top_mat=0)
            roof.remove_doubles(.01)
            
            # Cut the house with the roof

            walls = house.difference(roof, solver='FAST')
            walls.verts[:, 2] += height
            
            walls.unwrap_faces(offset=(0, height))
            
            mb.append(walls)
            
            
    # ====================================================================================================
    # Plug another roof
            
    def plug(self, index, roof, roof_index):
        
        pane = self[index]
        if isinstance(pane, Gable):
            pass

        elif isinstance(pane, RoofPane):
            roof[(roof_index - 1)%len(roof)].right_plug = pane
            roof[(roof_index + 1)%len(roof)].left_plug  = pane
            roof[roof_index] = RoofSide(roof[roof_index].p0, roof[roof_index].p1)
            
        return roof
    
   
    
    # ====================================================================================================
    # Replace by RoofSide.plug_rectangle
            
    def plugged_roof_OLD(self, main_surface, plugged_surface, relation):
        # Relation:
        # - from_index, to_index
        # - start_to_0, end_to_0, end_1
        # - length, width
        
        # ----- The shared segment
        
        v0 = main_surface.verts[relation['to_index']]
        v1 = main_surface.verts[(relation['to_index'] + 1)%len(main_surface.verts)]
        
        # ----- Find the roof side which is plugged
        
        ok = False
        for i_side, roof_side in enumerate(self):
            if roof_side.contains(v0) and roof_side.contains(v1):
                ok = True
                break
            
        if not ok:
            return None
        
        # ----- The profile of the roof to create
        
        profile = Profile(*self.profile)
        profile.scale(relation["width"]/profile.width)
        
        # ----- Create the roof (supposed to be four sides)
        
        walls = plugged_surface.get_full_walls()
        i_wall0 = None
        for i_wall, wall in enumerate(walls):
            if relation['from_index'] in wall['segments']:
                i_wall0 = i_wall
                break
        
        assert(i_wall0 is not None)
        
        roof  = Roof()
        for i in range(4):
            wall = walls[(i_wall0  + i) % 4]
            p0 = wall['wall'][0]
            p1 = wall['wall'][1]
            
            if i % 2 == 0:
                if i == 0:
                    self.add_hidden(p0, p1)
                else:
                    self.add_gable(p0, p1)
            else:
                self.add_pane(p0, p1, profile=profile)
                
        roof.connect_sides()
        
        return roof
        
    
    # ====================================================================================================
    # Debug / Demo
    
    @staticmethod
    def demo():
        
        def show_surface(verts, name="Walls"):
            mb = MeshBuilder()
            index, _ = mb.add_surface(verts - (0, 0, 3))
            mb.extrude(mb.get_face_ring(index), (0, 0, 3))
            mb.to_object(name)
            
        surface = np.array((
            (0, 0, 0), (18, 0, 0), (18, 6, 0), (0, 6, 0)
            ), float)
        
        plug_surf = np.array((
            (3, -7, 0), (6, -7, 0), (6, 0, 0), (3, 0, 0)
            ), float)
        
        extends = [
            np.array(( (3, -2, 0), (5, -2, 0), (5, 0, 0), (3, 0, 0) ), float),
            np.array(( (0, -1, 0), (1, -1, 0), (1, 0, 0), (0, 0, 0) ), float),
            np.array(( (7, -1, 0), (8, -1, 0), (8, 0, 0), (7, 0, 0) ), float),
            np.array(( (3, 4, 0), (5, 4, 0), (5, 5, 0), (3, 5, 0) ), float),
            ]
        
        show_surface(surface)
        show_surface(plug_surf, "Plug")

        
        # ----- Main roof
        
        roof = Roof()
        profile = Profile.Circular(3, 2.5, 2)
        for i, p0 in enumerate(surface):
            p1 = surface[(i+1)%len(surface)]
            if True or i%2 == 0:
                roof.add_pane(p0, p1, profile)
            else:
                roof.add_gable(p0, p1)
            
        roof.connect_sides()
        
        # ----- Plug roof
        
        plug = Roof()
        plug_prof = Profile.Circular(1.5, 1.25, 2)
        for i, p0 in enumerate(plug_surf):
            p1 = plug_surf[(i+1)%len(plug_surf)]
            if i%2 == 1:
                plug.add_pane(p0, p1, plug_prof)
            else:
                plug.add_gable(p0, p1)
                
        plug.connect_sides()

        plug[3].left_plug = roof[0]
        plug[1].right_plug = roof[0]
            
    
        mb = MeshBuilder()
        
        roof.to_builder(mb)
        plug.to_builder(mb)
        
        mb.check()

        mb.to_object("Demo")
        
    
    

        


    