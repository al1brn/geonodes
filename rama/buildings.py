#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:23:09 2023

@author: alain
"""

import numpy as np
from geopy.core.varrays import VArrays
from geopy.core.crowd import Crowd, BigCrowd
from geopy.maths.segments import Polygon

# ====================================================================================================
# A debug utility to quickly visualize shapes in Blender
#
# Place a shape at offset (x_ofs, y_ofs). It is up to the owner to manage this offset

class Builder:
    def __init__(self):

        self.verts = np.zeros((0, 3), float)
        self.faces = []
        self.mats  = []
        self.uvs   = np.zeros((0, 2), float)
        
        self.x_ofs = 0.
        self.y_ofs = 0.
        
    def to_object(self, obj):
        
        for face in self.faces:
            if len(face) < 4:
                raise Exception("Face < 4", face)
                
            for i in face:
                if i > len(self.verts):
                    raise Exception("Ooopsy")
        
        mesh = obj.data
        mesh.clear_geometry()
    
        mesh.from_pydata(self.verts, (), self.faces)
        mesh.polygons.foreach_set('material_index', self.mats)
        mesh.update()
        
    def __len__(self):
        return len(self.verts)
    
    def add_verts(self, verts):
        self.verts = np.append(self.verts, np.array(verts) + (self.x_ofs, self.y_ofs, 0), axis=0)
        
    def add_face(self, face, mat=0):
        self.faces.append(face)
        self.mats.append(mat)
        
    def add_shape(self, verts, mat=0):
        n = len(self.verts)
        if len(verts) < 4:
            return
        self.add_verts(np.array(verts))
        self.add_face([n + i for i in range(len(verts))], mat)
        
    def add_point(self, point, mat=0, side=.5):
        O = np.array(point)
        self.add_shape([O + (-side, -side, 0), O + (side, -side, 0), O + (side, side, 0), O + (-side, side, 0)], mat)
        

# ====================================================================================================
# Raw Buildings
#
# This class is used to transform the raw input of buildings shape into the final structure:
#
# Input
# -----
#
# The input is built be reading and selecting shapes from a downloaded shape file
# Passing by this intermediary data allows to refine the buildings management without
# reading again the whole inpout shape file.
#
# The input is a variable arrays of shapes plus the height:
# - positive : the height in m
# - negative : the heihght in levels
# - null     : unknown
#
# Output
# ------
#
# The output is two arrays:
# - Houses: simple houses which will be instantiated from house templates with a Crowd
# - Complex: complex houses which will be extruded dynamically from their shape
#
# A simple house is a shape with 4 corners.
#
# Houses
# ------
#
# Statistically, they represent 60% of the buildings
# The output files contains
# - location        : with altitude
# - scale           : x, y, z
# - rotation        : z
# - model           : model index
# - color           : All vertices share the same color which can be used by the shader
# - random          : a random number which can be used by the shader
#
# NOTE that in the input shapes are "closed" loops (i.e. the last point is equal to the first), when
# the shapes in the complex file are "open" loop as a Blender face.

class RawBuildings(VArrays):
    
    def __init__(self, house_indices=None, complex_materials=None):
        
        super().__init__(infos_count=2)
        self.house_indices     = house_indices
        self.complex_materials = complex_materials
        
        self.rng = np.random.default_rng()
            
    # ---------------------------------------------------------------------------
    # Random seed
    
    def set_seed(self, seed):
        self.rng = np.random.default_rng(seed)
        
    # ---------------------------------------------------------------------------
    # Get the locations & heights
        
    @property
    def locations(self):
        return self.items[self.offsets]
    
    @property
    def heights(self):
        return self._info[:, 1]
    
    # ----------------------------------------------------------------------------------------------------
    # Statistics
    #
    # Typical stats:
    # points  5 : 55.1%
    # points  6 : 9.2%
    # points  7 : 13.7%
    # points  8 : 3.8%
    # points  9 : 7.5%
    # 
    # No height: 99.8 %
    
    def stats(self):
        
        count = len(self)
        print("Buildings statistics")
        print(f"   total: {count}")
        for i in range(20):
            n = np.sum(self.sizes == i)
            print(f"    points {i:2d} : {n:5d} ({n/count*100:.1f}%)")
            
        n = np.sum(self.sizes >= 20)
        print(f"    points 20+: {n:5d} ({n/count*100:.1f}%)")
        print()
        
        heights = {0: 0}
        for i, h in enumerate(self.heights):
            if h == 0:
                heights[0] += 1
            else:
                if heights.get(h) is None:
                    heights[h] = 1
                else:
                    heights[h] += 1
                    
        print("Heights")
        for h in sorted(heights.keys()):
            print(f"     {h:5d}: {heights[h]} ({heights[h]/count*100:.1f}%)")
            
        print()
        
    # ----------------------------------------------------------------------------------------------------
    # Normalize the shape of a building:
    # 1) Suppress useless points
    # 2) Rotate around the center such as the longer segment is along x axis
    #
    # Returns:
    # - normalized shape (closed version)
    # - center
    # - angle
    
    @staticmethod
    def normalize_shape(shape, tolerance=0.1):
        
        # ----------------------------------------------------------------------------------------------------
        # Suppress the useless points
        
        # Points but the last which is equal to the first
        
        points  = [point for point in shape[:-1]]
        n = len(points)
        
        if len(shape) < 10:
        
            # Relative segment vector: segms[i] = vector points[i] -> points[i+1]
            
            segms = [points[(i+1)%n] - points[i] for i in range(n)]
            
            # Angles of each vector with the x axis
            
            angles = [np.arctan2(segm[1], segm[0]) for segm in segms]
            
            # Relative angle between the next and the previous segment
            
            rel_angles = [angles[i] - angles[(i-1)%n] for i in range(len(angles))]
            
            # ----- Suppress the points where the angle is less than the tolerance
            
            for _ in range(len(segms)):
                ok = True
                for i in range(len(rel_angles)):
                    if abs(rel_angles[i]) < tolerance:
                        del rel_angles[i]
                        del points[i]
                        ok = False
                        break
                    
                if ok:
                    break
    
        n = len(points)
        segms = [points[(i+1)%n] - points[i] for i in range(n)]
            
        # ----------------------------------------------------------------------------------------------------
        # With the simpler shape, we rotate to have the longer side on the x axis
        
        max_len = 0
        i_max = None
        for i, segm in enumerate(segms):
            l = np.linalg.norm(segm)
            if l > max_len:
                max_len = l
                i_max   = i
                
        # We change the starting point and reintroduce that last point
                
        points = np.array([points[i%n] for i in range(i_max, i_max + n + 1)])
        
        v = points[1] - points[0]
        ag = np.arctan2(v[1], v[0])
        
        center = (np.min(shape, axis=0) + np.max(shape, axis=0))/2
                
        M = np.array(( (np.cos(ag), np.sin(ag)), (-np.sin(ag), np.cos(ag)) ) )
        
        points[:, :2] = center[:2] + np.matmul(M, (points[:, :2] - center[:2]).T).T
        
        return points, center, ag    
    
    # ----------------------------------------------------------------------------------------------------
    # Get a sample of shapes
    # Return a structure per sample
    
    def get_samples(self, selection, count):
        
        shapes = []
        for ind in self.rng.choice(np.arange(len(self))[selection], count):
            
            points = self[ind].items
            norms, center, ag  = self.normalize_shape(points)
    
            p_min, p_max = np.min(points, axis=0), np.max(points, axis=0)
            size = p_max - p_min
            
            shapes.append({
                'points' : points,
                'norms'  : norms,
                'center' : center,
                'corner' : np.min(points, axis=0),
                'size'   : size,
                'scale'  : np.max(norms, axis=0) - np.min(norms, axis=0),
                'angle'  : ag,
                'height' : self._info[ind, 1],
            })
            
        return shapes    
    
    # ----------------------------------------------------------------------------------------------------
    # Visualize the shapes with a various number of points in a Blender object
        
    def vis_shapes(self, count, obj):
        
        builder = Builder()
    
        y_ofs = 0
        for points_count in range(5, 21):
        
            builder.x_ofs = 0
            y_size        = 0
            
            if points_count == 20:
                samples = self.get_samples(self.sizes >= points_count, count)
            else:
                samples = self.get_samples(self.sizes == points_count, count)
                
            for sample in samples:

                size   = sample['size']
                scale  = sample['scale']
                center = sample['center']
                
                corner = np.min(sample['points'], axis=0)
                
                # ----- The reference shape
                
                pts = sample['points'] - corner
                builder.add_shape(pts[:-1], mat=0)
                
                # ----- The first point                

                builder.add_point(pts[0], mat=2)
                builder.x_ofs += 1 + size[0]
                
                # ----- The normalized shape   
                
                pts = sample['norms'] - corner
                builder.add_shape(pts[:-1], mat=1)
                
                # ----- next loop  

                builder.x_ofs += 10 + scale[0]
                y_size = max(y_size, size[1])

                    
            builder.y_ofs += y_size + 10
            
        builder.to_object(obj)    
        
    # ----------------------------------------------------------------------------------------------------
    # Generate all the shape
        
    def gen_shapes(self, obj):
        
        builder = Builder()
        
        for i_bld in range(len(self)):
            
            pts = self[i_bld].items
            builder.add_shape(pts[:-1], mat=0)
            
        builder.to_object(obj)            
        
    # ----------------------------------------------------------------------------------------------------
    # House index
    #
    # Arguments
    # 
    # Compute a building index from a shape
    # - small area     --> cabane
    # - big area       --> building
    # - almost rect    --> house
    # - long rect      --> long house
    # - very long rect --> warehouse
    
    def house_index(self, shape_index, center, norms, ag, model_indices):
        """ Get a house model index for a shape.
        
        center, norms and ag are the result of normalize_shape. We suppose that
        we have 4 points.
        
        model_indices is structured:
            house type -> {model index -> {size}}
        
        Arguments
        ---------
        - shape_index   : index of the shape
        - center        : the center of the house
        - norms         : the normalized shape (longer side oriented along x axis)
        - ag            : shape rotation to fit the map
        - model_indices : the available models to pick into
        
        Returns
        -------
        - model_index   : index of the model
        - scale         : scale to apply
        - angle         : rotation to apply
        """
        
        # ----- Utilitty : select among the models of a given type
        
        def select(house_type):
            houses = model_indices[house_type]
            n = np.random.randint(len(houses))
            return houses[n]

        # ----- Main
        
        size    = np.max(norms, axis=0) - np.min(norms, axis=0)
        surface = size[0]*size[1]
        model   = select('House Single')
        height  = size[1]*self.rng.normal(.8, .1)

        if surface < 30:
            model = select('Cabane')
        
        elif surface > 300:
            model = select('Building')
            
        else:
            
            # ----- Neigbours
            
            nbs = self.neighbours(shape_index)
            
            # ----- The neighbour can be a small thing
            
            srf_max = None
            segm    = None
            for i, nbinf in enumerate(nbs):
                pts = self[nbinf[1]].items
                nsz = np.max(pts, axis=0) - np.max(pts, axis=0)
                srf = nsz[0]*nsz[1]
                if srf > 30:
                    if srf_max is None:
                        srf_max = srf
                        segm = nbinf[0]
                    else:
                        if srf > srf_max:
                            srf_max = srf
                            segm = nbinf[0]
                            
            # ----- Isolated
            
            if segm is None:
                ratio = size[0]/size[1]
                if ratio > 3:
                    model = select('Warehouse')
                
                elif ratio > 1.8:
                    model = select('House Long')
                    
            # ----- Street house
                    
            else:
                
                if segm % 2 == 0:
                    ag += np.pi/2
                    t = size[0]
                    size[0] = size[1]
                    size[1] = t
                    
                model  = select('Street House')

                if len(nbs) > 1:
                    model = select('DEBUG')

                height = model['size'][2]*self.rng.normal(1, .1)
                
        # ----- Let's adjust the scale and return
        
        scale = size/model['size']
        scale[2] = scale[0]
        
        return model['index'], scale, ag
        
    # ----------------------------------------------------------------------------------------------------
    # Generate the houses
    
    def gen_houses(self, model_indices, selection=None):
        
        locations = []
        scales    = []
        angles    = []
        indices   = []
        excluded  = []
        
        shape_indices = np.arange(len(self))
        if selection is not None:
            shape_indices = shape_indices[selection]
            
        self.cache_offsets() # Hope it enhances the performances
            
        for counter, sh_index in enumerate(shape_indices):
            
            if counter % 1000 == 0:
                print(f"Generate houses {counter//1000} k / {len(shape_indices)}")
            
            points = self[sh_index].items
            norms, center, ag  = self.normalize_shape(points)
            
            if len(norms) > 5:
                excluded.append(sh_index)
                continue
            
            model_index, scale, angle = self.house_index(sh_index, center, norms, ag, model_indices)

            locations.append(center)
            indices.append(model_index)
            scales.append(scale)
            angles.append(angle)
            
        print(f"{len(locations)} houses generated, {len(excluded)} remaining.")
            
        return {
            'locations': locations,
            'scales'   : scales,
            'angles'   : angles,
            'indices'  : indices,
            'excluded' : excluded,
            }
    
    # ----------------------------------------------------------------------------------------------------
    # for each building
    # - center
    # - min
    # - max
    
    @property
    def limits(self):
        if hasattr(self, 'limits_'):
            return self.limits_
        
        limits = np.zeros((len(self), 3, 2), float)
        for i, b in enumerate(self):
            limits[i, 1] = np.min(b.items, axis=0)[:2]
            limits[i, 2] = np.max(b.items, axis=0)[:2]
            limits[i, 0] = (limits[i, 1] + limits[i, 2])/2
            
        self.limits_ = limits
            
        return self.limits_
    
    # ----------------------------------------------------------------------------------------------------
    # Buildings which are close to a given one
    
    def close_buildings(self, index, distance=30):
        
        lims = self.limits[index]
        
        return np.where(np.logical_and(
            np.logical_and(self.limits[:, 0, 0] > lims[1, 0] - distance, self.limits[:, 0, 0] < lims[2, 0] + distance),
            np.logical_and(self.limits[:, 0, 1] > lims[1, 1] - distance, self.limits[:, 0, 1] < lims[2, 1] + distance)
            ))[0]
    
    # ----------------------------------------------------------------------------------------------------
    # Convert the shape of a building in a series of vectors
    
    def to_segments(self, index):
        verts = self[index].items
        return (verts[1:] - verts[:-1])[:, :2]

    # ----------------------------------------------------------------------------------------------------
    # Are two shapes neighbour ones
    
    def are_neighbours(self, index0, index1, epsilon=1):
        
        poly0 = Polygon(self[index0].items[:, :2], is_closed=True)
        poly1 = Polygon(self[index1].items[:, :2], is_closed=True)
        
        return poly0.share_segment_with(poly1)
    
    # ----------------------------------------------------------------------------------------------------
    # Get the neighbours of a house
    #
    # Return an array of triplets for each neighbourd
    # - index of the segment with a neighbour
    # - house index of the neighbour
    # - house segment index
    
    def neighbours(self, index, distance=100):
        
        close = self.close_buildings(index, distance=distance)
        ns = []
        for i in close:
            if i == index:
                continue
            
            segm_inds = self.are_neighbours(index, i)
            if segm_inds:
                ns.append((segm_inds[0], i, segm_inds[1]))
                
        return ns
    
    # ----------------------------------------------------------------------------------------------------
    # Debug
    # Get some house with neighbours
    
    def debug_with_neighbours(self, count=1000):
        res = []
        
        for i in range(len(self)):
            if i % 1000 == 0:
                print(f"Neighbours {i}, {len(res)}")
                
            nbs = self.neighbours(i)
            for nb in nb:
                res.append((i,) + nb)
            
            if len(res) > count:
                break
            
        print(f"Selection of houses with neighbours: {len(res)}")
        
        return res
            
    

# ====================================================================================================
# Buildings
#
# The input is a variable arrays of shapes plus the height:
# - positive : the height in m
# - negative : the heihght in levels
# - null     : unknown

class Buildings(VArrays):
    
    def __init__(self, mat_count=0):
        super().__init__(infos_count=2)
        self.mat_count = mat_count
        
    # ---------------------------------------------------------------------------
    # Add a base
    
    def add_polygon(self, poly, height=6, mat=0):
        self.append(poly)
        self._info[-1, 1] = int(heigth*100)
        self._info[-1, 2] = mat
        
    # ---------------------------------------------------------------------------
    # Get the locations
        
    @property
    def locations(self):
        return self.items[self.offsets]
    
        locs = np.zeros((len(self), 2), float)
        count = 0
        for base in self:
            if len(base.items):
                locs[count] = base.items[0]
            count += 1
        return locs
    
    # ---------------------------------------------------------------------------
    # Extrude
                
    def extrude(self, obj, inds=None):
        
        # ---------------------------------------------------------------------------
        # Select faces and vertices
        
        if inds is None:
            vas = self
            ids = None
        else:
            vas = self[inds]
            ids = np.arange(len(self))[inds]
            
        info = vas._info
        
        # ---------------------------------------------------------------------------
        # Vertices
        
        if vas.item_shape == (2,):
            verts  = np.insert(vas.items, 2, 0, axis=-1)
        else:
            verts  = vas.items
            
        # ---------------------------------------------------------------------------
        # Extrusion
        
        # ----- Duplicate the vertices
        # - the base
        # - the top
        # The top vertices will be move upwards in the loop
        
        nverts = len(verts)
        verts = np.append(verts, verts, axis=0)
        
        # ----- The other arrays

        faces = []
        mats  = np.zeros(0, int)
        uvmap = np.zeros((0, 2), float)
        layers = {
            'building': np.zeros(len(verts), int),
            'random':   np.zeros(len(verts), float),
            }
        
        # ----- Loop on the buildings

        offset = 0
        for i_bld, base in enumerate(vas._info):
            
            if i_bld % 10000 == 0:
                print(f"Extruding building {i_bld//1000} k /{len(vas)//1000}")
            
            # ---------------------------------------------------------------------------
            # Number of vertices for this building

            nbase = base[0]
            
            # ---------------------------------------------------------------------------
            # Let's write the vertex layers
            
            # Unique buildind id
            
            bld_id = i_bld if ids is None else ids[i_bld]
            layers['building'][offset:offset + nbase] = bld_id + 1
            layers['building'][offset + nverts:offset + nverts + nbase] = bld_id + 1
            
            # A random number
            
            rand = np.random.uniform(0, 1)
            layers['random'][offset:offset + nbase] = rand
            layers['random'][offset + nverts:offset + nverts + nbase] = rand

            # ---------------------------------------------------------------------------
            # We work with one vertex less
            
            n = nbase - 1  # Last vertex is equal to the first !

            # Prepare the uv map of the building

            uvs = np.zeros((n + 4*n, 2), float)

            # Extrude the building vertices with the height
            
            height = base[1]/100
            verts[nverts + offset:nverts + offset + n, 2] += height
            
            # ----- Top face (base face is useless)
            
            faces.append([nverts + offset + i for i in range(n)])
            uvs[:n] = verts[offset:offset + n, :2] - np.min(verts[offset:offset + n, :2], axis=0)
            
            # ----- Side faces and uvs
            
            uv_verts = np.append(verts[offset:offset+n, :2], [verts[offset, :2]], axis=0)
            dists = np.linalg.norm(uv_verts[1:] - uv_verts[:-1], axis=-1)
            
            uv_x = 0.
            for i in range(n):
                i0 = offset + i
                i1 = offset + (i + 1)%n
                faces.append([i1, nverts + i1, nverts + i0, i0])
                
                uvs[n + i*4:n + i*4 + 4] = [(uv_x + dists[i], 0), (uv_x + dists[i], height), (uv_x, height), (uv_x, 0)]
                uv_x += dists[i]
                
            uvmap = np.append(uvmap, uvs/100, axis=0)
            
            # ----- Materials
            
            if self.mat_count == 0:
                mat = 1
            else:
                mat = 1 + np.random.randint(0, self.mat_count+1)
                
            mats = np.append(mats, [0] + [mat]*n)
                
            # ----- Next building
            
            offset += nbase
            
        # ----------------------------------------------------------------------------------------------------
        # Build the object
        
        print("Building object...")
        
        mesh = obj.data
        mesh.clear_geometry()
        
        mesh.from_pydata(verts, (), faces)
        
        mesh.polygons.foreach_set('material_index', mats)
        
        uv_layer = mesh.uv_layers.new(name="UVMap")
        count = len(uvmap)
        uv_layer.data.foreach_set('uv', np.reshape(uvmap, count*2))
        
        # Vertex layes
        
        for name, layer in layers.items():
            
            v_layer = None
            if layer.dtype == int:
                v_layer = mesh.vertex_layers_int.new(name=name)
            elif layer.dtype == float:
                v_layer = mesh.vertex_layers_float.new(name=name)
            else:
                raise Exception(f"Impossible to set the vertex layer '{name}' of type {layer.dtype}. Only int and float are supported.")
                
            v_layer.data.foreach_set('value', layer)
            
        mesh.update()
        
        print("Buildings extruded.")

        return obj


    