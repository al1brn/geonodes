#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 19:17:04 2023

@author: alain

Transform a slow to read OSM file into a quick to read numpy arrays.
The lat lon are transformed into lambert 93 coordinates

OSM:
    - node     : lat lon
    - way      : list of nodes
    - relation : list of ways
    
Numpy:
    - nodes : array of vectors 2D in Lambert 93 coordinates
    - ways  : variable arrays of Lambert 93 coordinates
    - rels  : variable arrays of way ids
    
In OSM, items are refered by a unique key, in numpy version, we use the array index instead
    
tags are converted in dictionaries
    
shape files are read with osmium.
"""

import numpy as np
import pickle

import sys
import time

sys.path.append("/Users/alain/Documents/blender/scripts/modules")
from geopy.gis.lamb93 import to_xy
from geopy.core.varrays import VArrays
from geopy.core.meshbuilder import Builder
from geopy.maths.segments import Polygon

        
# =============================================================================================================================
# A numpy bases version of OSM ways

class Ways:
    def __init__(self):
        
        # ----- The nodes
        
        self.nodes = np.zeros((0, 2), float)
        
        # ----- The ways
        
        self.ways = VArrays()
        self.ways.items = np.zeros((0,), int)
        
        # ----- The relations
        # VArrays info is uzed to key the relations
        
        self.rels = VArrays()
        self.rels.items = np.zeros((0,), int)
        
        # ----- The tags
        
        self.ways_tags  = []
        self.rels_tags  = []
        
    # ----------------------------------------------------------------------------------------------------
    # Representation
    
    def __str__(self):
        return f"<Ways data: {len(self.rels)} relations, {len(self.ways)} ways and {len(self.nodes)} points>"
        
    # ----------------------------------------------------------------------------------------------------
    # Save to a file
    
    def save(self, file_name):
        
        np.savez(file_name,
            nodes=self.nodes,
            ways_info=self.ways._info,   ways_items=self.ways.items,
            rels_info=self.rels._info,   rels_items=self.rels.items,
            )
        
        with open(str(file_name) + '.pkl', 'wb') as f:
            pickle.dump({'ways_tags': self.ways_tags, 'rels_tags': self.rels_tags}, f)
        
    # ----------------------------------------------------------------------------------------------------
    # Load from a file
    
    @classmethod
    def load(cls, file_name):
        
        ways = cls()
        
        ars = np.load(str(file_name) + ".npz")
        
        ways.nodes = ars['nodes']
        
        ways.ways.items = ars['ways_items']
        ways.ways._info = ars['ways_info']
        
        ways.rels.items = ars['rels_items']
        ways.rels._info = ars['rels_info']
        
        with open(str(file_name) + '.pkl', 'rb') as f:
            d = pickle.load(f)
            ways.ways_tags  = d['ways_tags']
            ways.rels_tags  = d['rels_tags']
        
        return ways
    
    # ====================================================================================================
    # Convert OSM shape file into a numpy version
    
    @staticmethod
    def convert(source_file, target_file, limit=None):
        
        import osmium as osm
        
        # ----------------------------------------------------------------------------------------------------
        # OSM Reader

        class ToArrays(osm.SimpleHandler):
            def __init__(self, limit=None):
        
                osm.SimpleHandler.__init__(self)
                
                self.limit = limit
                
                #  ----- The Ways instance to build
                
                self.ways = Ways()
                
                #  ----- Key converters
                
                self.nodes = []
                
                self.node_keys = {}
                self.way_keys  = {}
                
            # ----------------------------------------------------------------------------------------------------
            # Convert lat lon to Lmabert 93 x, y coordinates
            
            def nodes_to_xy(self, nodes):
                
                lonlats = []
                for n in nodes:
                    try:
                        lonlats.append((n.lon, n.lat))
                    except:
                        pass
                        
                if len(lonlats) == 0:
                    return None
                
                # ----- Conversion to xy
                
                lls   = np.array(lonlats)
                verts = np.zeros((len(lls), 2), float)
                verts[:, 0], verts[:, 1] = to_xy(lls[:, 0], lls[:, 1])
                
                shape = []
                for n, vert in zip(nodes, verts):
                    
                    key = n.ref
                    index = self.node_keys.get(key)
                    if index is None:
                        index = len(self.nodes)
                        self.node_keys[key] = index
                        self.nodes.append(vert)
                        
                    shape.append(index)
                    
                return shape
                
            def way(self, w):
                
                if len(self.ways.ways) % 10000 == 0:
                    print(f"way {len(self.ways.ways)//1000} k")
                    
                if self.limit is not None:
                    if len(self.ways.ways) > self.limit:
                        return
                
                # ----- Convert the nodes coordinates
                
                shape = self.nodes_to_xy(w.nodes)
                if shape is None:
                    return
                
                index = len(self.ways.ways)
                self.ways.ways.append(shape)
                self.way_keys[w.id] = index

                self.ways.ways_tags.append({tag.k: tag.v for tag in w.tags})
                
            def relation(self, r):
                
                if len(self.ways.rels) % 10000 == 0:
                    print(f"relation {len(self.ways.rels)//1000} k")

                new_rel = [self.way_keys.get(m.ref, -1) for m in r.members]
                if len(new_rel) == 0:
                    return
                
                self.ways.rels.append(new_rel)

                self.ways.rels_tags.append({tag.k: tag.v for tag in r.tags})

                
        # ----------------------------------------------------------------------------------------------------
        # Main
            
        to_arrays = ToArrays(limit=limit)
        to_arrays.apply_file(source_file, locations=True)
        
        ways = to_arrays.ways
        ways.nodes = np.array(to_arrays.nodes)
        
        to_arrays.ways.save(target_file)
        
        ways = to_arrays.ways
        
    # ====================================================================================================
    # Extract ways
    
    def extract_to(self, file_name, ways_selection=None, verts_selection=None):
        
        ways = Ways()
        
        node_keys = {}
        way_keys  = {}
        nodes     = []
        
        print("Extracting....")
        
        indices = np.arange(len(self.ways))
        if ways_selection is not None:
            indices = indices[ways_selection]
            
        # ----- Loop on the ways
        
        for i_way in indices:
            
            #if i_way == 300000:
            #    break
            
            if i_way % 10000 == 0:
                print(f"Way {i_way//1000} k")
                
            if verts_selection is not None:
                if not verts_selection(self.way_verts(i_way)):
                    continue
            
            way = self.ways[i_way].items
            new_way = []
            for key in way:
                idx = node_keys.get(key)
                if idx is None:
                    idx = len(nodes)
                    node_keys[key] = idx
                    nodes.append(self.nodes[key])
                new_way.append(idx)
                
            way_keys[i_way] = len(ways.ways)
            
            ways.ways.append(new_way)
            ways.ways_tags.append(self.ways_tags[i_way])
            
        # ----- Extract the vertices
            
        #ways.nodes = self.nodes[list(node_keys.values())]
        ways.nodes = np.array(nodes)
        
        del nodes
        
        # ----- The relations
        
        for i_rel in range(len(self.rels)):
            
            if i_rel % 10000 == 0:
                print(f"Way {i_rel//1000} k")
                
            rel = self.rels[i_rel].items
            
            new_rel = []
            for key in rel:
                idx = way_keys.get(key)
                if idx is None:
                    new_rel = None
                    break
                
                new_rel.append(idx)
                
            if new_rel is None:
                continue
            
            ways.rels.append(new_rel)
            ways.rels_tags.append(self.rels_tags[i_rel])
            
        print("Extraction done:")
            
        ways.save(file_name)
        
        del node_keys, way_keys
        
        ways = Ways.load(file_name)
        print(ways)
        
    # ====================================================================================================
    # Merge with another base
    
    def merge_with(self, other):
        
        nnodes = len(self.nodes)
        nways  = len(self.ways)
        
        self.nodes = np.append(self.nodes, other.nodes, axis=0)
        
        other.ways.items += nnodes
        self.ways.join(other.ways)
        self.ways_tags.extend(other.ways_tags)
        
        other.rels.items += nways
        self.rels.join(other.rels)
        self.rels_tags.extend(other.rels_tags)
        
        other.ways.items -= nnodes
        other.rels.items -= nways
        
    # ====================================================================================================
    # Ways containing given nodes --> Finding ways sharing nodes
    
    def ways_of_node(self, node_index):
        
        if not hasattr(self, 'ways_of_nodes_'):
            self.ways_of_nodes_ = self.ways.reversed_indices
            
        return np.unique(self.ways_of_nodes_[self.ways.items == node_index])
    
    def sharing_nodes(self, way_index):
        ways = self.ways_of_node(self.ways[way_index].items)
        return ways[ways != way_index]

    # ====================================================================================================
    # Explore the content
    
    def way_verts(self, index):
        if hasattr(index, '__len__'):
            return [self.way_verts(i) for i in index]
        else:
            return self.nodes[self.ways[index].items]
        
    def rel_verts(self, index):
        return self.way_shape(self.rels[index].items)
    
    # ----------------------------------------------------------------------------------------------------
    # Plot a way

    def plot_way(self, index, ax=None, mode='-k'):
        
        import matplotlib.pyplot as plt

        show = ax is None
        if show:
            fig, ax = plt.subplots()
            
        if hasattr(index, '__len__'):
            for k in index:
                self.plot_way(k, ax, mode)
                
        else:
            verts = self.way_verts(index)
            if verts is None:
                print(f"way {index} is None")
                return
            
            for k, v in self.ways_tags[index].items():
                print(f"{k:15s}: {v}")
            
            ax.plot(verts[:, 0], verts[:, 1], mode)
            
        if show:
            sw = str(index)
            plt.title(f"Way {sw:10s}")
            plt.show()
            
    def plot_rel(self, index):

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        
        for k in self.rels[index].items:
            self.plot_way(k, ax, mode='-')
            
        plt.title(f"Relation {index}")
        plt.show()
        
        for k, v in self.rels_tags[index].items():
            print(f"{k:15s}: {v}")
        
    # ----------------------------------------------------------------------------------------------------
    # To object
    
    def to_object(self, indices, obj, mode='LINES', center=(0, 0), dist_max=None):
        
        from geopy.core import blender
        if isinstance(obj, str):
            obj = blender.create_mesh_object(obj)
            
        v_dim = 3 if mode == 'EXTRUDE' else 2
        
        verts = np.zeros((0, v_dim), float)
        edges = []
        faces = []
        
        def add_way(w_index, way_mode=mode):
            
            nonlocal verts, edges, faces
            
            vs = self.way_verts(w_index)
            
            if center is not None:
                vs -= center
                
                if dist_max is not None:
                    
                    v_min = np.min(vs, axis=0)
                    v_max = np.max(vs, axis=0)
                    
                    if v_min[0] > dist_max:
                        return
                    if v_max[0] < -dist_max:
                        return
                    if v_min[1] > dist_max:
                        return
                    if v_max[1] < -dist_max:
                        return
                    
            if v_dim == 3:
                vs = np.insert(vs, 2, 0, axis=-1)
            
            nverts = len(verts)
            verts = np.append(verts, vs, axis=0)
            
            if way_mode=='LINES':
                edges.extend([[nverts+i, nverts+i+1] for i in range(len(vs)-1)])
                
            elif way_mode == 'FACES':
                faces.append([nverts+i for i in range(len(vs))])
                
            elif way_mode == 'EXTRUDE':
                n = len(vs)
                
                size = np.max(vs, axis=0) - np.min(vs, axis=0)
                surf = size[0]*size[1]
                if surf < 60:
                    height = 1
                else:
                    height = np.random.normal(15, 3)
                
                vs[:, 2] = height
                verts = np.append(verts, vs, axis=0)
                
                faces.append([nverts + n + i for i in range(len(vs))])
                for i in range(len(vs)):
                    faces.append([nverts+i, nverts+(i+1)%n, nverts + n + (i+1)%n, nverts + n + i])
                
        
        if hasattr(indices, '__len__'):
            for k in indices:
                way_mode = mode
                if self.ways_tags[k].get('wall', 'yes') == 'no':
                    way_mode = 'FACES'                    
                add_way(k, way_mode)
                
        else:
            add_way(indices)
            
        if center is None:
            center = (np.min(verts, axis=0) + np.max(verts, axis=0))/2
            verts[:, :2] -= center[:2]
            
        if v_dim == 2:
            verts = np.insert(verts, 2, 0, axis=-1)
        
        obj.data.clear_geometry()
        if mode == 'LINES':
            obj.data.from_pydata(verts, edges, ())
        else:
            obj.data.from_pydata(verts, (), faces)
            
        return center
        
    # ----------------------------------------------------------------------------------------------------
    # All the available tag keys
    
    def tags_keys(self):
        keys = set()
        for tags in self.ways_tags:
            keys.update(set(tags.keys()))
        return keys
    
    def tag_values(self, key):
        values = {}
        for tags in self.ways_tags:
            if key in tags.keys():
                value = tags[key]
                values[value] = values.get(value, 0) + 1
        return values
    
    def get_ways(self, **kwargs):
        ways = []
        for i_way, tags in enumerate(self.ways_tags):
            for k, v in kwargs.items():
                tag_v = tags.get(k, 'NOPE')
                if isinstance(v, list):
                    ok = tag_v in v
                else:
                    ok = tag_v == v
                    
                if ok:
                    ways.append(i_way)
                break
            
        return ways
    
    def get_rels(self, **kwargs):
        rels = []
        for i_rel, tags in enumerate(self.rels_tags):
            for k, v in kwargs.items():
                if tags.get(k, 'NOPE') == v:
                    rels.append(i_rel)
                break
            
        return rel
    
    # ====================================================================================================
    # Neighbourhood

    # ----------------------------------------------------------------------------------------------------
    # For each shape
    # - center
    # - min
    # - max
    
    @property
    def limits(self):
        
        if not hasattr(self, 'limits_'):
            
            print('Compute limits', end='')
        
            limits = np.zeros((len(self.ways), 3, 2), float)
            for i, way in enumerate(self.ways):
                
                if i % 10000 == 0:
                    print('.', end='')
                
                vs = self.nodes[way.items]

                limits[i, 1] = np.min(vs, axis=0)[:2]
                limits[i, 2] = np.max(vs, axis=0)[:2]
                limits[i, 0] = (limits[i, 1] + limits[i, 2])/2
                
            self.limits_ = limits
            
            print()
            
        return self.limits_
    
    # ----------------------------------------------------------------------------------------------------
    # Buildings which are close to a given one
    
    def close_buildings(self, index, distance=40):
        
        lims = self.limits[index]
        
        return np.where(np.logical_and(
            np.logical_and(self.limits[:, 0, 0] > lims[1, 0] - distance, self.limits[:, 0, 0] < lims[2, 0] + distance),
            np.logical_and(self.limits[:, 0, 1] > lims[1, 1] - distance, self.limits[:, 0, 1] < lims[2, 1] + distance)
            ))[0]

    # ----------------------------------------------------------------------------------------------------
    # Are two shapes neighbour ones
    
    def are_neighbours(self, index0, index1, epsilon=1):
        
        poly0 = Polygon(self.nodes[self.ways[index0].items])
        poly1 = Polygon(self.nodes[self.ways[index1].items])
        
        #debug = poly0.share_segment_with(poly1)
        #if debug:
        #    print("--->", index0, index1, "are_neighbours")
        
        return poly0.share_segment_with(poly1)
    
    
    # ----------------------------------------------------------------------------------------------------
    # Return the blind sides of a polygon
    # A blind side is shared with another polygon
    # Blinds sides are return as bits in a integer
    
    def blind_sides(self, index, epsilon=.5):
        
        candidates = self.close_buildings(index, distance=2*epsilon)

        poly =  Polygon(self.nodes[self.ways[index].items])
        blinds = 0
        for candidate in candidates:
            poly = Polygon(self.nodes[self.ways[candidate].items])
            i_seg, _ = poly.share_segment_with(poly, epsilon=epsilon)
            if i_seg is not None:
                blinds |= 1 << i_seg
        return blinds
    
    
    # ----------------------------------------------------------------------------------------------------
    # Get the neighbours of a house
    #
    # Return
    # - an array of triplets for each neighbourd
    #   - index of the segment with a neighbour
    #   - house index of the neighbour
    #   - house segment index
    #   - facade index (longer segment without neighbour)
    # - The face index
    # - The number of houses in the neighbourhood
    
    def neighbours(self, index, distance=100, return_facade=False, return_neighbourhood=False):
        
        close = self.close_buildings(index, distance=distance)
        
        ns = []
        if return_facade:
            verts = self.way_verts(index)
            facade = 0
            facade_l2 = (verts[1, 0] - verts[0, 0])**2 + (verts[1, 1] - verts[0, 1])**2  
        
        for i in close:
            if i == index:
                continue
            
            segm_inds = self.are_neighbours(index, i)
            if segm_inds:
                ns.append((segm_inds[0], i, segm_inds[1]))
            else:
                # LATER....
                l2 = (verts[1, 0] - verts[0, 0])**2 + (verts[1, 1] - verts[0, 1])**2 
                
        if return_neighbourhood:
            return ns, len(close)
        else:
            return ns
    
    # ----------------------------------------------------------------------------------------------------
    # Normalize the shape of a building:
    # 1) Suppress useless points
    # 2) Rotate around the center such as the longer segment is along x axis
    #
    # Returns:
    # - normalized shape (closed version)
    # - center
    # - angle
    # - segment mapping : initial index --> normalized index
    
    @staticmethod
    def normalize_shape(shape, tolerance=0.1):
        
        # ----------------------------------------------------------------------------------------------------
        # Suppress the useless points
        
        # Points but the last which is equal to the first
        
        points  = [point for point in shape[:-1]]
        n       = len(points)
        mapping = None
        
        if len(shape) < 10:
        
            # Relative segment vector: segms[i] = vector points[i] -> points[i+1]
            
            segms = [points[(i+1)%n] - points[i] for i in range(n)]
            
            # Angles of each vector with the x axis
            
            angles = [np.arctan2(segm[1], segm[0]) for segm in segms]
            
            # Relative angle between the next and the previous segment
            
            rel_angles = [angles[i] - angles[(i-1)%n] for i in range(len(angles))]
            
            mapping = [0]*n
            for i in reversed(range(n)):
                if abs(rel_angles[i]) < tolerance:
                    del rel_angles[i]
                    del points[i]
                    mapping[i] = -1
                    
            n = len(points)
                    
            # ----- Create the mapping

            if mapping[0] == -1:
                mapping[0] = n - 1
    
            for i in range(1, len(mapping)):
                if mapping[i] == -1:
                    mapping[i] = mapping[i-1]
                else:
                    mapping[i] = (mapping[i-1] + 1)%n
    
                
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
                
        # We change the starting point and reintroduce the last point
        # 0, 1, 2, ... i_max ..., n-2, n-1 --> i_max ... n-2, n-1, 0, 1, ... i_max-1
                
        points = np.array([points[i%n] for i in range(i_max, i_max + n + 1)])
        
        v = points[1] - points[0]
        ag = np.arctan2(v[1], v[0])
        
        center = (np.min(shape, axis=0) + np.max(shape, axis=0))/2
                
        M = np.array(( (np.cos(ag), np.sin(ag)), (-np.sin(ag), np.cos(ag)) ) )
        
        points[:, :2] = center[:2] + np.matmul(M, (points[:, :2] - center[:2]).T).T
        
        # ----- Build the segments mapping
        
        if mapping is None:
            seg_map = [(i_max+i)%(len(shape)-1) for i in range(len(shape)-1)]
            
        else:
            seg_map = [(v - i_max)%n for v in mapping]
            
        # ----- Return the result
        
        size = np.max(points, axis=0) - np.min(points, axis=0)
        
        return {
            'points'  : points,
            'size'    : size,
            'surf'    : size[0]*size[1],
            'center'  : center,
            'angle'   : ag,
            'seg_map' : seg_map,
            }
    
    # ====================================================================================================
    # Extrude building per type
    
    # ----------------------------------------------------------------------------------------------------
    # Extrude building = apartments
    
    def apartments(self, obj="Apartments", levels=12, top_mats = [0], mats=[1]):
        
        print("Extuding apartments")
        
        builder = Builder()

        for i_way in self.get_ways(building=['apartments', 'terrace']):
            
            rng = np.random.default_rng(i_way)
            
            verts = np.insert(self.way_verts(i_way), 2, 0, axis=-1)
            h = (levels*3)*rng.normal(1, .3)
            builder.extrude(verts, h, mat=rng.choice(mats), top_mat=rng.choice(top_mats))
            
        builder.uvs /= 100
        
        builder.to_object(obj)
        

    # ----------------------------------------------------------------------------------------------------
    # Extrude building = retail
    
    def retail(self, obj="Retail", top_mats = [0], mats=[1]):
        
        print("Extuding retail")
        
        builder = Builder()
        
        for i_way in self.get_ways(building=['retail', 'commercial']):
            
            rng = np.random.default_rng(i_way)
            
            verts = np.insert(self.way_verts(i_way), 2, 0, axis=-1)
            h = 8*rng.normal(1, .1)
            builder.extrude(verts, h, mat=rng.choice(mats), top_mat=rng.choice(top_mats))
            
        builder.uvs /= 100
        
        builder.to_object(obj)
        
    # ====================================================================================================
    # Extract the shapes implemented as models instances
    
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
    # Get the houses shapes which will be generated with a crowd of models
    #
    # Houses with neighbours:
    # - city houses oriented along the street
    #
    # Houses without neighbour:
    # - random instances
    
    def get_houses_crowd(self, selection, models, max_count=None):
        
        locations = []
        scales    = []
        angles    = []
        indices   = []
        excluded  = []
        
        counter = 0
        
        for i_way in selection:
            
            if i_way not in [2433, 5369,5377,5385,5386,5389,5390,5397,5401,5411,5453,5462,5465,5466]:
                continue
            
            
            if counter % 1000 == 0:
                print(f"Houses crowd {counter//1000} k / {len(selection)}")
            counter += 1
            
            if max_count is not None:
                if counter > max_count:
                    break
            
            rng = np.random.default_rng(i_way)
            
            # ----- The normalized shape
            
            shape = self.way_verts(i_way)
            
            # ----- Complex shapes are excluded (they must be extruded individually)
            
            if len(shape) > 7:
                excluded.append(i_way)
                continue
            
            # ----- Get normalization & neighbours
            
            norm = self.normalize_shape(shape)
            if len(norm['points']) > 5:
                excluded.append(i_way)
                continue
            
            # ----- Big surfaces are excluded
            
            if norm['surf'] > 200:
                excluded.append(i_way)
                continue
            
            nbs = self.neighbours(i_way)
            
            angle          = norm['angle']
            rotated        = False
            with_neighbour = False
            
            # ----- 3 neighbours, let's make sure x is visible
            
            if len(nbs) >= 3:
                print(i_way, ": 3 Neighbours")
                
                
                free = [True] * 4
                for i_s, _, _ in nbs:
                    free[norm['seg_map'][i_s]] = False
                i_free = 0
                for i, f in enumerate(free):
                    if f:
                        i_free = i
                        break
                    
                print(i_way, free)
                    
                rotated = (i_free % 2) == 0
                angle += (i_free+1)*np.pi/2
                with_neighbour = True
                
            else:
                continue
            
                # ----- Neighbours must be houses
                
                i_neighbour = None
                i_segment   = None
                
                for i_s, i_n, _ in nbs:
                    
                    #print("   neighbour", i_n, self.ways_tags[i_n].get('building'), self.ways_tags[i_n])
                    
                    if self.ways_tags[i_n].get('building') is None:
                        continue
                    
                    nvs = self.way_verts(i_n)
                    pmin, pmax = np.min(nvs, axis=0), np.max(nvs, axis=0)
                    psize  = pmax - pmin
                    
                    if min(psize[0], psize[1]) < 5:
                        continue
                    
                    if psize[0]*psize[1] < 30:
                        continue
                    
                    i_neighbour = i_n
                    i_segment   = i_s
                    
                    break
                
                with_neighbour = i_neighbour is not None
                if with_neighbour:
                    if (norm['seg_map'][i_segment] % 2) == 1:
                        angle += np.pi/2
                        rotated = True

            # ----- We have a neighbour, let's orient it properly
            # Street facade is along x axis
            # Is neighbour segment is 0 or 2, with must rotate 90°
                
            if with_neighbour:
                if rotated:
                    model = models['DEBUG'][2]
                else:
                    model = models['DEBUG'][1]
                
            # ----- No house neighbour: single house
            
            else:
                model = models['DEBUG'][0]
                
            # ----- House is selected, we can add it
            
            indices.append(model['index'])
            locations.append(norm['center'])
            angles.append(angle)
            
            height = 10*rng.normal(1, .2)
            scale  = (norm['size'][0], norm['size'][1], height)/model['size']
            if rotated:
                scales.append((scale[1], scale[0], scale[2]))
            else:
                scales.append(scale)

        print(f"{len(locations)} houses generated, {len(excluded)} remaining.")
        
        locations = np.insert(locations, 2, 0, axis=-1)
            
        return {
            'locations': locations,
            'scales'   : scales,
            'angles'   : angles,
            'indices'  : indices,
            'excluded' : excluded,
            }    
        
    
    
      
