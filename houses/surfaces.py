#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:24:46 2023

@author: alain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 08:30:47 2023

@author: alain


"""

from time import time
from pathlib import Path

import numpy as np

from geopy.core import geo2D

# =============================================================================================================================
# A surface is defined by segments surrounding the surface
# Eeach segment, or wall, can be shared with another surface
# Surfaces sharing a common wall are grouped in a block
#
# A block can be:
# - The different roofs of a single house
# - the different houses in a city block

class Surface:
    
    def __init__(self, index, verts):
        self.index  = index
        self.verts  = np.array(verts)
        self.z      = np.min(self.verts[:, 2])
        self.shared = [-1]*len(self)
        self.area   = geo2D.area(self.verts)

    # ====================================================================================================
    # As an array of vertices
        
    def __len__(self):
        return len(self.verts)
    
    def __getitem__(self, index):
        return self.verts[index]
        
    def __setitem__(self, index, value):
        self.verts[index] = value

    # ====================================================================================================
    # Compute the shared walls with another shape    
        
    def shared_walls_with(self, other):
        
        new_verts  = []
        new_shared = []
        
        for ip0, (p0, p1) in enumerate(zip(self.verts, np.roll(self.verts, -1, axis=0))):
            
            new_verts.append(p0)
            new_shared.append(self.shared[ip0])
            
            seg_length = geo2D.length(p0, p1)
            
            for iq0, (q0, q1) in enumerate(zip(other.verts, np.roll(other.verts, -1, axis=0))):
                
                rel = geo2D.relation_to(p0, p1, q0, q1, maj_length=seg_length)
                
                if rel is None:
                    continue
                
                if rel['loc1'] <= 0:
                    # ......... P0 ....... P1 .........
                    # ... Q1 
                    # ......... Q1
                    if rel['loc0'] <= 0:
                        # The whole wall is inside the other one
                        # ......... P0 ....... P1 .........
                        #                      Q0 .........
                        #                            Q0 ...
                        new_shared[-1] = other.index
                        
                    else:
                        # ......... P0 ....... P1 .........
                        # ... Q1 ........ Q0 ..............
                        # ......... Q1 .. Q0 ..............
                        new_shared[-1] = other.index
                        new_verts.append(q0)
                        new_shared.append(-1)
                        
                else:
                    # .... P0 ........ P1 .........
                    # .......... Q1 
                    if rel['loc0'] <= 0:
                        # .... P0 ........ P1 .........
                        # .......... Q1 .. Q0 .........
                        # .......... Q1 ........ Q0 ...
                        new_verts.append(q1)
                        new_shared.append(other.index)
                    else:
                        # .... P0 ............. P1 ....
                        # ......... Q1 ... Q0 .........
                        new_verts.append(q1)
                        new_shared.append(other.index)
                        new_verts.append(q0)
                        new_shared.append(-1)
                        
                break # max one segment (let's suppose it)

        # ----------------------------------------------------------------------------------------------------
        # Let's update the vertices and the shared for a new neighbour
        
        self.verts = np.array(new_verts)
        self.shared = new_shared
        
        return other.index in new_shared

    # =============================================================================================================================
    # Debug
    
    def plot(self, title="Surface", others=[]):
        
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        def plot_surface(surf, fmt='-'):
            vs = np.resize(surf.verts, (len(surf)+1, 3))
            ax.plot(vs[:, 0], vs[:, 1], fmt, linewidth=1)
            for i in range(len(surf)):
                if surf.shared[i] < 0:
                    continue
                ax.plot((vs[i, 0], vs[i+1, 0]), (vs[i, 1], vs[i+1, 1]), '-r', linewidth=2)
                    
        plot_surface(self, 'o-')
        for other in others:
            plot_surface(other)
        
        plt.title(title)
        
# =============================================================================================================================
# House

class House(list):
    
    def __init__(self, index):
        super().__init__()
        self.index = index
    
    @classmethod
    def FromVerts(cls, index, verts, simplify=True):
        
        from geopy.houses import grid
        
        house = cls(index)
        
        if simplify:
            for vs in grid.simplify(verts):
                house.append(Surface(len(house), vs))
        else:
            house.append(Surface(0, verts))
            
        if len(house) > 0:
            for surface in house:
                for surf in house:
                    if surf == surface:
                        continue
                    surface.shared_walls_with(surf)
                
        return house
    
    @property
    def has_shared_walls(self):
        for surf in self:
            if np.sum(np.array(surf.shared) >= 0) > 0:
                return True
        return False
    
    def get_verts_shared_sizes(self):
        verts  = np.zeros((0, 3), float)
        shared = []
        sizes  = []
        for surf in self:
            verts = np.append(verts, surf.verts, axis=0)
            shared.extend(surf.shared)
            sizes.append(len(surf))
        return verts, shared, sizes
                
    # =============================================================================================================================
    # Debug
    
    def plot(self, title="House"):
        
        if len(self) == 0:
            return
        
        self[0].plot(title, others=self[1:])
        

if __name__ == '__main__':
    
    # ----------------------------------------------------------------------------------------------------
    # Test
    
    np.set_printoptions(precision=1)
    
    if False:
        verts = np.zeros((6, 3), float)
        verts[0] = (1.1,  3.5, 0)
        verts[1] = (9.4,  3.7, 0)
        verts[2] = (9.6, 12.5, 0)
        verts[3] = (5.7, 12.0, 0)
        verts[4] = (5.7,  7.1, 0)
        verts[5] = ( .9,  7.1, 0)
        
        surface = Surface(1, verts)
        print("area", surface.area)
        #print("vectors", [str(pt) for pt in surface.side_vectors])
        #print("lengths", surface.lengths)
        #print("angles", np.degrees(surface.angles)%(np.pi/2))
        #print("angle",  np.degrees(surface.average_angle), "°")
    
        vs = np.zeros((4, 3), float)
        vs[0] = (verts[4] + verts[5])/2
        vs[1] = verts[4]
        vs[2] = (verts[3] + verts[4])/2
        vs[3] = (vs[0, 0], vs[2, 1], 0)
        
        surf = Surface(2, vs)
        
        surface.shared_walls_with(surf)
        surface.plot("Shared", [surf])
        
    
    
    
    
    
    
    
    
    
    
    

