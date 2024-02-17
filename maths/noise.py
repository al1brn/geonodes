#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Sat Nov 18 08:30:10 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Custom Noise
"""

import numpy as np

# ====================================================================================================
# Primes generator

def get_primes(up_to):
    A = [  3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 
         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
         229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 
         373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 
         521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
         673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 
         839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]
    
    if up_to <= 1000:
        return A
    
    up_to = min(up_to, 10000000)
    a = np.resize(A, 1000)
    index = len(A)
    
    B = A
    
    for n in range(a[-1] + 2, up_to, 2):
        ok = True
        for d in B:
            if n % d == 0:
                ok = False
                break
            
        if ok:
            if index == len(a):
                a = np.resize(a, len(a) + 1000)
            a[index] = n
            index += 1
            
            if n == 1018057: # More than 100000, we must use another B
                # a[445] = 3163 -> 3163**2 = 10004569
                B = a[:446]
                
    return a[:index]

# ====================================================================================================
# Some theory

# Given two values and two tangents for parameters t at values 0 and 1
# f(0) = U
# f(1) = V
# f'(0) = u
# f(1) = v

# intermediary values are given by
# f(t)  = at3 + bt2 + ct + d
# f'(t) = 3at2 + 2bt + c
#
# Which is solved:
# a = 2U - 2V + u + v
# b = -3U + 3V - 2u - v
# c = u
# d = U

# =============================================================================================================================
# Custom Perlin Noise

class Perlin:
    
    RAND_COUNT = 1 << 15 #32749 #1 << 15
    MASK = RAND_COUNT - 1 # Quicker than modulo
    
    def __init__(self, dimension=3, max_slope=1., seed=0):
        
        self.rng       = np.random.default_rng(seed)
        self.dimension = dimension
        self._values   = self.rng.uniform(0, 1, Perlin.RAND_COUNT)
        
        # Slopes depending on the max_slope factor
        
        if True:
            # Uniform on the angles, not the tangent
            ag_max = np.arctan(max_slope)
            self._slopes   = np.tan(self.rng.uniform(-ag_max, ag_max, Perlin.RAND_COUNT))
        
        else:
            # Normal around no slope
            # Less good : kind of a grid appears on the maps
            self._slopes   = self.rng.uniform(0, max_slope, Perlin.RAND_COUNT)
        
        # 15 primes per outpout dimension
        #  0 - 5  : linearization of input indices into a single index
        #  5 - 10 : linearization of input indices into a single index
        # 10 - 15 : from one index to x, y and z
        
        self.primes = self.rng.choice(get_primes(100000)[1000:], (3, 15)) # 15 primes per output dimension
        
    # ====================================================================================================
    # Indices to linear
    #
    # Primes are used as tile size per dimensioin
    
    def linear_indices(self, indices, prime_index, out_dim):
        
        if self.dimension == 1:
            inds = indices
            
        else:
            tile_size = 1
            inds = np.array(indices[:, 0])
            
            for i in range(1, self.dimension):
                tile_size *= self.primes[out_dim, prime_index+i]
                inds += (indices[:, i] * tile_size) & Perlin.MASK
                
        return (inds*self.primes[out_dim, prime_index]) & Perlin.MASK
    
    # ====================================================================================================
    # Values 
        
    def values(self, indices, out_dim=0):
        
        return self._values[self.linear_indices(indices, 0, out_dim)]

    # ====================================================================================================
    # Slopes
        
    def slopes(self, indices, out_dim=0):
        
        inds = self.linear_indices(indices, 5, out_dim)
        
        if self.dimension == 1:
            return self._slopes[(inds * self.primes[out_dim, 10]) & Perlin.MASK]
    
        if self.dimension == 2:
            return np.stack((
                self._slopes[(inds*self.primes[out_dim, 10]) & Perlin.MASK],
                self._slopes[(inds*self.primes[out_dim, 11]) & Perlin.MASK],
                ), axis=-1)
        
        elif self.dimension == 3:
            return np.stack((
                self._slopes[(inds*self.primes[out_dim, 10]) & Perlin.MASK],
                self._slopes[(inds*self.primes[out_dim, 11]) & Perlin.MASK],
                self._slopes[(inds*self.primes[out_dim, 12]) & Perlin.MASK],
                ), axis=-1)
        
        else:
            return np.stack((
                self._slopes[(inds*self.primes[out_dim, 10]) & Perlin.MASK],
                self._slopes[(inds*self.primes[out_dim, 11]) & Perlin.MASK],
                self._slopes[(inds*self.primes[out_dim, 12]) & Perlin.MASK],
                self._slopes[(inds*self.primes[out_dim, 13]) & Perlin.MASK],
                ), axis=-1)

    # ====================================================================================================
    # Interpolation 1D
    # Base interpolation function
        
    @staticmethod
    def interpolate(U, V, u, v, x):
        
        # a = 2*U - 2*V + u + v
        # b = -3*U + 3*V -2*u - v
        # c = u
        # d = U
        
        if np.shape(U) == np.shape(u):
        
            res = U + u*x
            
            x2 = x*x
            res += (-3*U + 3*V -2*u - v)*x2
            
            return res + (2*U - 2*V + u + v)*x2*x
        
        else:

            res = U + (u*x)[:, None]
            
            x2 = x*x
            res += (-3*U + 3*V -2*u[:, None] - v[:, None])*x2[:, None]
            
            return res + (2*U - 2*V + u[:, None] + v[:, None])*(x2*x)[:, None]
    
    # ====================================================================================================
    # Generate noise
    
    def gen_noise(self, coords, out_dim=0):
        
        # ----- Corner indices

        p0 = np.floor(coords).astype(int)
        
        # ---------------------------------------------------------------------------
        # Only one dimension
        
        if self.dimension == 1:
            return self.interpolate(
                U = self.values(p0    , out_dim),
                V = self.values(p0 + 1, out_dim),
                u = self.slopes(p0    , out_dim),
                v = self.slopes(p0 + 1, out_dim),
                x = coords - p0)
        
        # ---------------------------------------------------------------------------
        # We must interpolate succesively the values and the slopes of the next
        # dimensions along current axis
        #
        # Let's use big arrays with stack values : slopes + values
        
        # ---- All the edges along x axis
        # Couple of successive edges form an edge in the next dimension
        
        if self.dimension == 2:
            edges = [[(0, 0), (1, 0)], [(0, 1), (1, 1)]]
            
        elif self.dimension == 3:
            edges = [
                [(0, 0, 0), (1, 0, 0)], [(0, 1, 0), (1, 1, 0)],
                [(0, 0, 1), (1, 0, 1)], [(0, 1, 1), (1, 1, 1)],
                ]
                
        else:
            edges = [
                [(0, 0, 0, 0), (1, 0, 0, 0)], [(0, 1, 0, 0), (1, 1, 0, 0)],
                [(0, 0, 1, 0), (1, 0, 1, 0)], [(0, 1, 1, 0), (1, 1, 1, 0)],
                [(0, 0, 0, 1), (1, 0, 0, 1)], [(0, 1, 0, 1), (1, 1, 0, 1)],
                [(0, 0, 1, 1), (1, 0, 1, 1)], [(0, 1, 1, 1), (1, 1, 1, 1)],
                ]
                
        # ----- The big arrays

        arrays = []
        for edge in edges:

            # We roll the slope to put the value at the end

            Us        = np.roll(self.slopes(p0 + edge[0], out_dim), 1, axis=-1)
            us        = np.array(Us[:, -1])
            Us[:, -1] = self.values(p0 + edge[0], out_dim)
            
            Vs        = np.roll(self.slopes(p0 + edge[1], out_dim), 1, axis=-1)
            vs        = np.array(Vs[:, -1])
            Vs[:, -1] = self.values(p0 + edge[1], out_dim)
            
            arrays.append(self.interpolate(Us, Vs, us, vs, coords[:, 0] - p0[:, 0]))
            
        # ----- Loop on the remainding dimensions
        
        for i_dim in range(1, 4):
            if len(arrays) == 2:
                assert(np.shape(arrays[0])[-1] == 2)
                return self.interpolate(
                    U = arrays[0][:, 1], 
                    V = arrays[1][:, 1], 
                    u = arrays[0][:, 0], 
                    v = arrays[1][:, 0], 
                    x = coords[:, i_dim] - p0[:, i_dim])
            
            new_arrays = []
        
            for i in range(len(arrays)//2):
                i0 = 2*i
                i1 = i0+1
                new_arrays.append(self.interpolate(
                    U = arrays[i0][:, 1:], 
                    V = arrays[i1][:, 1:],
                    u = arrays[i0][:, 0],
                    v = arrays[i1][:, 0],
                    x = coords[:, i_dim] - p0[:, i_dim]))
                
            arrays = new_arrays
                
        assert(False)
    
# ====================================================================================================
# Noise

class Noise:
    def __init__(self, dimension=3, scale=5., detail=2, roughness=.5, lacunarity=2, seed=0):
        
        self.perlin = Perlin(dimension=dimension, max_slope=.5, seed=seed)
        
        self.scale      = scale
        self.detail     = detail
        self.roughness  = roughness
        self.lacunarity = lacunarity
        
    # ====================================================================================================
    # Call the function
    
    def __call__(self, vectors, w=0, out_dim=0):
        
        if self.perlin.dimension == 1:
            shape = np.shape(vectors)
        else:
            shape = np.shape(vectors)[:-1]
        size = np.prod(shape, dtype=int)
            
        if self.perlin.dimension == 4:
            coords = np.empty(shape + (4,), float)
            coords[..., :3] = vectors
            coords[..., 3]  = w
            coords = np.reshape(coords, (size, 4))
        else:
            coords = np.reshape(vectors, (size, self.perlin.dimension))
        
        # Base Noise
        
        noise = self.perlin.gen_noise(coords, out_dim=out_dim)
        
        # Loop on the octaves
        
        octaves = int(self.detail)
        frac    = self.detail - octaves
        ok_frac = frac > .01
        if ok_frac:
            octaves += 1
        scale   = self.scale*1.
        ampl    = 1.
        for i_oct in range(octaves):
            scale *= self.lacunarity
            ampl  *= self.roughness
            if ok_frac and i_oct == octaves - 1:
                ampl *= frac
            noise += ampl*self.perlin.gen_noise(coords*scale, out_dim=out_dim)
            
        return np.reshape(noise, shape)

    # ====================================================================================================
    # Vector

    def x(self, coords, w=0):
        return self(coords, w=w, out_dim=0)
    
    def y(self, coords, w=0):
        return self(coords, w=w, out_dim=1)
    
    def z(self, coords, w=0):
        return self(coords, w=w, out_dim=2)
    
    def vector(self, coords, w=0):
        return np.stack((self.x(coords, w), self.y(coords, w), self.z(coords, w)), axis=-1)
    
    # ====================================================================================================
    # Generate a map 2D
        
    def noise_map(self, resolution=1024, z=0, w=0, out_dim=0):
        
        coords = np.stack(np.meshgrid(range(resolution), range(resolution)), axis=-1)/resolution

        if self.perlin.dimension > 2:
            coords = np.reshape(coords, (resolution**2, 2))
            coords = np.append(coords, np.ones((len(coords), 1), float)*z, axis=-1)
            coords = np.reshape(coords, (resolution, resolution, 3))
            
        return self(coords, w=w, out_dim=out_dim)
    
    
    
        
# ====================================================================================================
# Test

def demo(detail=2, roughness=.5, lacunarity=2, z=0):
    
    import geopy as gp
    
    grid = gp.Mesh.Grid(10, 10, 100, 100)
    grid.points.z = z
    grid.points.z = Noise(dimension=3, detail=detail, roughness=roughness, lacunarity=lacunarity)(grid.points.position)
    
    grid.to_object("Noise Demo")
    
def performances():

    from time import time
    
    print("Noise performances:")
    for count in [10000, 100000, 1000000]:
        for dim in [3, 4]:
            print(f"\n> {count:,d} points, dimension {dim}")
            for detail in range(6):
                top = time()
                _ = Noise(dimension=dim, detail=detail)(np.random.default_rng().uniform(-10, 10, (count, 3)))
                t = time()-top
                print(f"   Detail={detail} in {t:.1f} s")
                
    print("\nPerformances done\n")
    

if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    #performances()
        
    # ----- Dimension 1
        
    if True:
        details = [.5, 1.5, 2.5]
        for detail in details:
            noise = Noise(dimension=1, detail=detail, seed=2)
        
            x = np.linspace(-10, 10, 100)
            y = noise(x)
        
            plt.plot(x, y)
            
        plt.title(f"Detail in {details}")
        plt.show()
        
    if True:
        details = [1., 1.25, 1.5, 2.]
        for detail in details:
            noise = Noise(dimension=1, detail=detail, seed=2)
        
            x = np.linspace(-10, 10, 100)
            y = noise(x)
        
            plt.plot(x, y)
            
        plt.title(f"Detail in {details}")
        plt.show()
        
    if True:
        lacunarities = [1, 2, 3]
        for lacunarity in lacunarities:
            noise = Noise(dimension=1, lacunarity=lacunarity, seed=2)
        
            x = np.linspace(-10, 10, 100)
            y = noise(x)
        
            plt.plot(x, y)
            
        plt.title(f"Lacunarity in {lacunarities}")
        plt.show()
        
    # ----- Dimension 2
    
    if True:
        scale = 5
        details = [.5, 1.5, 2.5]
        z = 0
        for detail in details:
            
            noise = Noise(dimension=2, detail=detail, seed=2)
            
            plt.imshow(noise.noise_map(resolution=256, z=z))
            plt.title(f"detail: {detail}, scale: {scale}, z: {z:.1f}")
            plt.show()
    
    if True:
        scale = 5
        details = [.5, 1.5, 2.5]
        z = 0
        lacunarities = [1, 2, 3]
        for lacunarity in lacunarities:
            
            noise = Noise(dimension=2, lacunarity=lacunarity, seed=2)
            
            plt.imshow(noise.noise_map(resolution=256, z=z))
            plt.title(f"lacunarity: {lacunarity}, scale: {scale}, z: {z:.1f}")
            plt.show()
            
    # ----- Dimension 3
    
    if True:
        noise = Noise(dimension=3, detail=detail, seed=2)
        
        for z in np.linspace(0, .1, 5):
            plt.imshow(noise.noise_map(resolution=256, z=z))
            plt.title(f"Dimension 3, z: {z:.3f}")
            plt.show()
    
    # ----- Dimension 3
    
    if True:
        noise = Noise(dimension=4, detail=detail, seed=2)
        
        for w in np.linspace(0, .1, 5):
            plt.imshow(noise.noise_map(resolution=256, w=w))
            plt.title(f"Dimension 4, w: {w:.3f}")
            plt.show()
    

    

    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    