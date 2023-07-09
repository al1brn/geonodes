#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 08:08:16 2023

@author: alain
"""

# ====================================================================================================
# Create a matrix of points from to geometries having a POINT domain

class PointsMatrix:
    def __init__(self, x_geometry, y_geometry):
        """ Cross two geometries to perform computation on each couple of points between the two.
        
        This can be used to accumulate the effect of a set of points to each points of another geometry.
        For instance, imagine rain on the surface of water, each dip creating a moving wave.
        To compute the height of each surface vertex, one must add the wave of each dip.
        
        Both geometries must have a POINT domain: Mesh, Points or Curve.
        
        An intermediary cloud of points is created by instanciating 'y_geometry' on 'x_geometry' and then realizing
        the instances. The number of points of the resulting 'matrix' is the product of the numbers of points
        of the input geometries.
        
        **Note**: whatever the types of geometries, the 'matrix' geometry are internally typecasted to 'Points'.
        
        To mix the attributes of the two geometries, use *x_attribute* and *y_attribute* methods.
        These methods take an attribute of their corresponding geometry.
        
        The example below shows how to compute the distance between the points of one geometry to the points of a second geometry:
            
        ``` python
        mesh   = gn.Mesh.Cube().mesh
        points = gn.Points.Points(10)
        
        matrix = PointsMatrix(mesh, points)
        dists = (matrix.x_attribute(mesh.verts.position) - matrix.y_attribute(points.points.position).length
        
        # Sum of the distances in the mesh vertices
        
        mesh.verts.store_named_attribute("dists sum", matrix.x_total(dists))
        
        # Sum of the distances in the points
        
        points.points.store_named_attribute("dists sum", matrix.y_total(dists))
        ```
        
        The following piece of code is a full demo of PointsMatrix.
        The results can be viewed with the 'Viewer' nodes.
            
        ``` python
        import geonodes as gn
        
        with gn.Tree("PointsMatrix Demo", auto_capture=False) as tree:
            
            # Let's build a 4x3 matrix
            
            xg = gn.Curve.Line().resample(count=4)
            yg = gn.Points.Points(3)
            
            mx = PointsMatrix(xg, yg)
            
            # Values 10, 20, 30, 40 for the x direction
            x = mx.x_attribute((xg.points.index+1)*10)

            # Values 1, 2, 3 for the y direction
            y = mx.y_attribute(yg.points.index+1)

            # Matrix values are sums x + y
            # 11 21 31 41
            # 12 22 32 42
            # 13 23 33 43
            sum = x + y
            
            # View the result as named attribute in matrix
            mx.matrix.points.store_named_attribute("Sums", sum)
            mx.matrix.view()
            
            # Sums along x axis
            # 36 66 96 126
            xg.points.store_named_attribute("Total", mx.x_total(sum))
            xg.view()
            
            # Sums along y axis
            #  104
            #  108
            #  112
            yg.points.store_named_attribute("Total", mx.y_total(sum))
            yg.view()
            
            tree.og = xg + yg        
        ```
        
        Args:
        - x_geometry (Mesh, Curve or Points) : first geometry of points
        - y_geometry (Mesh, Curve or Points) : second geometry of points
        """
        
        self.tree = x_geometry.node.tree
        
        with self.tree.layout("PointsMatrix: initialization"):
            
            # ----- Size of each domain
            
            if False:
                for name, geo in zip(('x_count', 'y_count'), (x_geometry, y_geometry)):
                    cname = type(geo).__name__
                    if cname == 'Mesh':
                        setattr(self, name, geo.verts.count)
                    elif cname == 'Curve':
                        setattr(self, name, geo.points.count)
                    elif cname == 'Points':
                        setattr(self, name, geo.points.count)
                    else:
                        raise Exception(f"PointsMatrix accept only geometries with POINT domain (Mesh, Curve or Points), not '{cname}': {geo}")
            else:
                cname = type(y_geometry).__name__
                if cname == 'Mesh':
                    self.y_count = y_geometry.verts.count
                elif cname in ['Curve', 'Points']:
                    self.y_count = y_geometry.points.count
                else:
                    raise Exception(f"PointsMatrix accept only geometries with POINT domain (Mesh, Curve or Points), not '{cname}': {y_geometry}")
            
                        
            # ----- The x and y geometries typecasted to points
            
            #self.x_geometry = gn.Points(x_geometry)
            #self.y_geometry = gn.Points(y_geometry)
            self.x_geometry = x_geometry
            self.y_geometry = y_geometry

            # ----- The matrix
            
            insts = self.x_geometry.points.instance_on(instance=self.y_geometry)
            
            # ----- Make sure not to change the position of the y geometry points
            
            #insts.insts.position = 0
            
            # ----- The matrix as a Points geometry
            
            self.matrix = gn.Points(insts.realize())
            
            # ----- The index of each geometry
            
            with self.tree.layout("x index"):
                self.x_index = self.matrix.points.index / self.y_count
            
            with self.tree.layout("y index"):
                self.y_index = self.matrix.points.index % self.y_count
                
            # ----- ID set to x_index

            #self.matrix.points.ID = self.x_index 
    
    # ----------------------------------------------------------------------------------------------------
    # x attribute
            
    def x_attribute(self, value):
        """ x attribute is sampled on the x geometry with the global index.
        """
        res = self.x_geometry.points.sample_index(value=value, index=self.x_index)
        res.node.label = 'x_attribute'
        return res

    # ----------------------------------------------------------------------------------------------------
    # y attribute
        
    def y_attribute(self, value):
        """ y attribute is sampled on the y geometry with the global index.
        """
        res = self.y_geometry.points.sample_index(value=value, index=self.y_index)
        res.node.label = 'y_attribute'
        return res
        
    # ----------------------------------------------------------------------------------------------------
    # Capture a matrix attribute
    
    def capture(self, value):
        """ Capture a value in the matrix.
        
        This method simply calls ``` self.matrix.points.capture_attribute(value) ```.
        
        Args:
        - value : value to capture in the matrix
        
        Returns:
        - Attribute socket of the 'Capture Attribute' node attribute
        """
        return self.matrix.points.capture_attribute(value)
        
    # ----------------------------------------------------------------------------------------------------
    # Set ID x and y
    
    def set_id_x(self):
        """ Set matrix points ID to x index.
        """
        self.matrix.points.ID = self.x_index 
        
    def set_id_y(self):
        """ Set matrix points ID to y index.
        """
        self.matrix.points.ID = self.y_index 
        
    # ----------------------------------------------------------------------------------------------------
    # Get a value along x
    
    def x_get(self, value):
        """ Get a value from the matrix with index of the x geometry.
        
        Args:
        - value : a matrix attribute
        
        Returns:
        - value along the x axis
        """
        return self.matrix.points.sample_index(value, index=self.x_geometry.index*self.y_count)
    
    def y_get(self, value):
        """ Get a value from the matrix with index of the y geometry.
        
        Args:
        - value : a matrix attribute
        
        Returns:
        - value along the y axis
        """
        return self.matrix.points.sample_index(value, index=self.y_geometry.index)
        
    # ----------------------------------------------------------------------------------------------------
    # Accumulate
        
    def accumulate_node(self, value, group_id='x'):
        """ Create an 'Accumulate Field' node to compute along one axis.
        
        Once the node is created, the result can be read in the requested geometry using 'x_get' or 'y_get'.
        The methods x_leading, x_trailing, x_total and their equivalent along the y axis can be used directly
        when only one socket is required.
        
        Before creating the node, the ID is set to x_index or y_index depending on the value of group_id.
        
        Args:
        - value : the value to accumulated
        - group_id (str='x') : set id to x_index or y_index
        
        Returns:
        - 'Accumulate Field' node
        """
        
        with self.tree.layout("PointsMatrix: accumulate"):
            
            if group_id is not None:
                if group_id.lower() == 'x':
                    self.set_id_x()
                elif group_id.lower() == 'y':
                    self.set_id_y()
                else:
                    raise Exception(f"PointsMatrix.accumulate error: 'group_id' argument must be 'x' or 'y', not {group_ind}")
                    
            return self.matrix.points.accumulate_field(value, group_id=self.matrix.points.ID)
        
    def x_total(self, value, set_id=True):
        """ Sum a matrix attribute along x axis.
        
        This method is equivalent to ``` x_get(accumulate_node(...).total) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The total along the x axis
        """
        group_id = 'x' if set_id else None
        return self.x_get(self.accumulate_node(value, group_id).total)
    
    def y_total(self, value, set_id=True):
        """ Sum a matrix attribute along y axis.
        
        This method is equivalent to ``` y_get(accumulate_node(...).total) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The total along the x axis
        """
        group_id = 'y' if set_id else None
        return self.y_get(self.accumulate_node(value, group_id).total)
    
    def x_leading(self, value, set_id=True):
        """ Leading sum a matrix attribute along x axis.
        
        This method is equivalent to ``` x_get(accumulate_node(...).leading) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The leading sum along the x axis
        """
        group_id = 'x' if set_id else None
        return self.x_get(self.accumulate_node(value, group_id).total)
    
    def y_leading(self, value, set_id=True):
        """ Leading sum a matrix attribute along y axis.
        
        This method is equivalent to ``` y_get(accumulate_node(...).leading) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The leading total along the y axis
        """
        group_id = 'y' if set_id else None
        return self.y_get(self.accumulate_node(value, group_id).total)
    
    def x_trailing(self, value, set_id=True):
        """ Trailing sum a matrix attribute along x axis.
        
        This method is equivalent to ``` x_get(accumulate_node(...).trailing) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The trailing sum along the x axis
        """
        group_id = 'x' if set_id else None
        return self.x_get(self.accumulate_node(value, group_id).total)
    
    def y_trailing(self, value, set_id=True):
        """ Trailing sum a matrix attribute along y axis.
        
        This method is equivalent to ``` y_get(accumulate_node(...).trailing) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The trailing total along the y axis
        """
        group_id = 'y' if set_id else None
        return self.y_get(self.accumulate_node(value, group_id).total)
    
    # ====================================================================================================
    # Demos
    
    # ----------------------------------------------------------------------------------------------------
    # Simple demo
    
    @staticmethod
    def Demo(nx=4, ny=3, name="PointsMatrix Demo"):
        """ A demo of PointsMatrix?
        """
        
        import geonodes as gn
        
        with gn.Tree(name, auto_capture=False) as tree:
            
            # Let's build a (nx, ny) matrix
            
            xg = gn.Curve.Line().resample(count=nx)
            yg = gn.Points.Points(ny)
            
            mx = PointsMatrix(xg, yg)
            
            # Values 10, 20, 30, 40 for the x direction
            x = mx.x_attribute((xg.points.index+1)*10)

            # Values 1, 2, 3 for the y direction
            y = mx.y_attribute(yg.points.index+1)

            # Matrix values are sums x + y
            # 11 21 31 41
            # 12 22 32 42
            # 13 23 33 43
            sum = x + y
            
            # View the result as named attribute in matrix
            mx.matrix.points.store_named_attribute("Sums", sum)
            mx.matrix.view()
            
            # Sums along x axis
            # 36 66 96 126
            xg.points.store_named_attribute("Total", mx.x_total(sum))
            xg.view()
            
            # Sums along y axis
            #  104
            #  108
            #  112
            yg.points.store_named_attribute("Total", mx.y_total(sum))
            yg.view()
            
            tree.og = xg + yg
            
    # ----------------------------------------------------------------------------------------------------
    # Falling dips
    
    @staticmethod
    def Rain():
        """ Simulate dips falling on water.
        """
        
        import geonodes as gn
        
        with gn.Tree("Rain", auto_capture=False) as tree:
            
            # ---------------------------------------------------------------------------
            # Parameters
            
            rain    = gn.Float.Input(.1, "Rain intensity", min_value=0, max_value=1)
            a_min   = gn.Float.Input(.2, "Min Amplitude", min_value=0, max_value=2.)
            a_max   = gn.Float.Input(1., "Max Amplitude", min_value=.1, max_value=10)

            T       = gn.Float.Input(.5, "Time period", min_value=.1, max_value=5)
            nT      = gn.Float.Input(3, "Duration", min_value=1, max_value=10) 
            L       = gn.Float.Input(6., "Space period", min_value=.1, max_value=20)
            #nL      = gn.Float.Input(3, "Distance", min_value=1, max_value=10) 
            seed    = gn.Integer.Input(0, "Seed")
            
            # ------ Initial computations
            
            with tree.layout("Initialization"):
            
                density = rain.map_range(0, 1, 0, .001)
                
                c      = L/T             # Speed
                wt     = (2*gn.pi)/T     # Time pulsation
                wd     = (2*gn.pi)/L     # Space pulsation
                
                t_max  = T*nT            # Duration
                d_max  = L*nT            # Distance max
                life   = t_max + d_max/c # Duration of dip effect
                
                # ---------------------------------------------------------------------------
                # Before simulation zone
                
                # ----- Water surface is supposed to be a mesh 
                
                mesh = gn.Mesh(tree.ig)
                
                # ----- Generate random dips
                
                new_dips = mesh.faces.distribute_points(density=density, seed=seed + tree.frame).points
                new_dips.points.store_named_attribute("time", 0.)
                new_dips.points.store_named_attribute("amplitude", gn.Float.Random(a_min, a_max, seed=tree.frame))

            # ---------------------------------------------------------------------------
            # Simulation zone
            
            simul = gn.Simulation(mesh, dips=new_dips)
            
            water = simul.geometry
            dips  = gn.Points(simul.dips + new_dips)
            
            # ----- Time of each dip
            
            t = dips.points.named_float("time") + simul.delta_time
            dips.points.store_named_attribute("time", t)

            # ----- Delete all dips
            
            dips.points[t.greater_than(life)].delete()
            
            # ----- Multiply water vertices per dips
            # to compute the effect of each dip on each vertex

            mx = PointsMatrix(water, dips)
            
            # ----- Wave computation
            
            with tree.layout("Wave"):
                
                # ----- Distances between vertices and dips
                
                d = (mx.x_attribute(water.verts.position) - mx.y_attribute(dips.points.position)).length
                
                # ----- Amplitude
                
                amplitude = dips.points.named_float("amplitude")
                
                ampl = d.map_range_smooth(0, d_max, amplitude, 0)*gn.Float(t).map_range(0, t_max + d/c, 1, 0)
                
                # ----- Compute z
                
                z = ampl*gn.sin(wt*t - wd*d)
                z = z.switch(d.greater_than(c*t), 0)
                
                # ----- Sum the z dips per vertex
                    
                Z = mx.x_total(z)

            # ----- Update simulation
            
            water.verts.store_named_attribute("height", Z)

            simul.geometry = water
            simul.dips     = dips
            
            # ---------------------------------------------------------------------------
            # After Simulation zone
            
            mesh = simul.og

            p = mesh.verts.position
            z = mesh.verts.named_float("height")
            p.z = z
            mesh.verts.position = p
                
            mesh.faces.shade_smooth = True
                
            tree.og = mesh        
   