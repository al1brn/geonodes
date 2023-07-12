#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 08:08:16 2023

@author: alain
"""

# ====================================================================================================
# Create a matrix of points from to geometries having a POINT domain

class PointsMatrix:
    def __init__(self, x_geometry, y_geometry=None):
        """ Cross two geometries to perform computation on each couple of points between the two.
        
        This can be used to accumulate the effect of a set of points to each points of another geometry.
        For instance, imagine rain on the surface of water, each dip creating a moving wave.
        To compute the height of each surface vertex, one must add the wave of each dip.
        
        Both geometries must have a POINT domain: Mesh, Points or Curve.
        
        An intermediary cloud of points is created by instanciating 'y_geometry' on 'x_geometry' and then realizing
        the instances. The number of points of the resulting 'matrix' is the product of the numbers of points
        of the input geometries. Whatever the types of geometries, they are internally typecasted to 'Points'.
        
        **NOTE** Take care of the size of your geometries since multiplying big geometries could produce a huge number of points.
        
        **Naming conventions**:
        - method starting by x_ or y_ accept indices from geometies:
          - x_get : read values in the matrix with ``` x_geometry.index ```
        - method not starting by x_ or y_ accept indices in the matrix dimension
          - get : read values from the whole matrix with ``` matrix.index ```
          
        ### Computing cells
        
        A cell operation combines values from x dimension with values from y dimension and stores the result in the matrix,
        one value per cell, i.e. per couple (x index, y index). For instance, the following line multiply values from the
        two dimensions:
            
        ``` python
        # a is an attribute of x geometry and b an attribute of y geometry
        prod = matrix.set_x(a) * matrix.set_y(b)
        ```
        
        It is important to use ``` set_x ``` and ``` set_y ``` methods which explode the attribute on the whole matrix.
        
        ### Reading cells
        
        Cells are read along a dimension using ``` x_get ``` or ``` y_get ```. In the following example, the previous
        result is read in the x dimension, for y index = 2:
            
        ``` python
        x = matrix.x_get(prod, y_index=2)
        ``` 
        
        ### Total
        
        The main benefit of the matrix is the use of `Accumulate Field` node allowing to sum the values along a dimension.
        
        ``` python
        prod = matrix.set_x(a) * matrix.set_y(b)
        # Total along the  y dimension into the x dimension
        total = matrix.x_total(prod)
        ```
        
        ### Square matrices
        
        A square matrix is a matrix where the sizes of the dimensions are equal. Square matrices offer specicific features:
        - **set_diagonal**: set values in the diagonal cells
        - **get_diagonal**: read the cells of the diagonal
        - **set_triangle**: set values in the triangle cells
        
        In the following example, the sum of all possible products is performed:
            
        ``` python
        # Only one argument produces a square matrix
        matrix = PointsMatrix(cloud)
        # Products of the radius
        prod = matrix.set_x(cloud.points.radius) * matrix.set_y(cloud.points.radius)
        # To have only one instance of the products, set the triangle values to 0, including the diagonal
        prod = matrix.set_triangle(prod, 0, diagonal=True)
        # Sum per points
        prod_sum = matrix.x_total(prod)
        ```
        
        ### Selections
        
        The PointsMatrix class exposes selection methods / properties:
        - sel_x 
        - sel_y
        - diagonal_selection
        
        The selection are used to selectively change a matrix wide attribute with ``` switch ``` :
            
        ``` python
        # v is a value in the matrix scope
        # Set the value to zero for y index == 3
        v = v.switch(matrix.sel_x(y_index=3), 0)
        # Set the diagonal to 0 (equivalent to matrix.set_diagonal(v, 0))
        v = matrix.set_diagonal(v, 0)
        ```
        
        ### Example
        
        The following piece of code is a full demo of PointsMatrix. The results can be viewed with the 'Viewer' nodes.
            
        ``` python
        import geonodes as gn
                
        with gn.Tree("PointsMatrix Demo", auto_capture=False) as tree:
            
            # Let's build a 4x3 matrix
            
            xg = gn.Curve.Line(end=(3, 0, 0)).to_points(count=4).points
            yg = gn.Curve.Line(end=(0, 2, 0)).resample(count=3)
            
            mx = gn.PointsMatrix(xg, yg)
            
            # Values 10, 20, 30, 40 for the x direction
            x = mx.set_x((xg.points.index + 1)*10)
        
            # Values 1, 2, 3 for the y direction
            y = mx.set_y(yg.points.index + 1)
        
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
            
            # Visualize the matrix points by setting z to the distance between the points
            px = mx.set_x(xg.points.position)
            py = mx.set_y(yg.points.position)
            d = (py - px).length**4/100
            
            mx.matrix.points.position_offset = (0, 0, .1 + d)
            
            tree.og = xg + yg + mx.matrix       
        ```
        
        Args:
        - x_geometry (Mesh, Curve or Points) : first geometry of points
        - y_geometry (Mesh, Curve or Points) : second geometry of points
        """
        
        import geonodes as gn
        
        self.tree = x_geometry.node.tree
        
        if y_geometry is None:
            y_geometry = x_geometry
        
        with self.tree.layout("PointsMatrix: initialization", color='UTIL'):
            
            # ----- Domain size and indices
            
            for geo, prefix in zip((x_geometry, y_geometry), ('x', 'y')):
                cname = type(geo).__name__
                if cname == 'Mesh':
                    setattr(self, prefix + '_points', geo.verts)
                                        
                elif cname in ['Curve', 'Points']:
                    setattr(self, prefix + '_points', geo.points)
                else:
                    raise Exception(f"PointsMatrix accept only geometries with POINT domain (Mesh, Curve or Points), not '{cname}': {geo}")
                        
            # ----- The x and y geometries
            
            self.y_count = self.y_points.count
            
            # ----- The matrix
            
            insts = x_geometry.instance_on_points(instance=y_geometry)
            
            # ----- The matrix as a Points geometry
            
            self.matrix = gn.Points(insts.realize())
            
            # ----- The index of each geometry
            
            with self.tree.layout("PointsMatrix - index x", color='UTIL'):
                self.index_x = self.capture((self.matrix.points.index / self.y_count).to_integer(rounding_mode='FLOOR'))
                self.index_x.node.label = "index_x"
            
            with self.tree.layout("PointsMatrix - index y", color='UTIL'):
                self.index_y = self.capture((self.matrix.points.index % self.y_count).to_integer(rounding_mode='ROUND'))
                self.index_y.node.label = "index_y"
                
            
    # ----------------------------------------------------------------------------------------------------
    # Visualize the matrix points as a grid
    
    def to_grid_shape(self, size=.1, z=0):
        """ Arrange the matrix points into a grid shape (for tests).
        """
        with self.tree.layout("PointsMatrix - to grid shape", color='UTIL'):
            self.matrix.points.position = (self.index_x*size, self.index_y*size, z)
        
    # ====================================================================================================
    # Exploding dimension attributes to the whole matrix
    
    # ----------------------------------------------------------------------------------------------------
    # x attribute in the matrix
    
    def set_x(self, value):
        """ Value along x geometry is exploded in the whole matrix.
        
        Used in combination with 'set_y', allows to combine the two dimensions:
            
        Args:
        - value (any): an x_geometry attribute
        
        Returns:
        - matrix.points attribute
        """

        res = self.matrix.points.sample_index(self.x_points, value=value, index=self.index_x)
        res.node.label = 'set_x'
        return res

    # ----------------------------------------------------------------------------------------------------
    # y attribute in the matrix
        
    def set_y(self, value):
        """ Value along y geometry is exploded in the whole matrix.
        
        Used in combination with 'set_x', allows to combine the two dimensions:
            
        Args:
        - value (any): an y_geometry attribute
        
        Returns:
        - matrix.points attribute
        """
        
        res = self.matrix.points.sample_index(self.y_points, value=value, index=self.index_y)
        res.node.label = 'set_y'
        return res
    
    # ----------------------------------------------------------------------------------------------------
    # Capture an attribute into the matrix
    
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
    # Selection
    
    @property
    def diagonal_selection(self):
        """ Build the selection for the diagonal of a sqaure matrix.
        
        Returns:
        - Boolean in the matrix scope
        """
        
        res = self.index_x.equal(self.index_y)
        res.node.label = "Diag selection"
        return res
    
    def sel_x(self, y_index=0):
        """ Build the selection for a line along the x dimension.
        
        Args:
        - y_index (Integer): y index of the line
        
        Returns:
        - Boolean in the matrix scope
        """
        with self.tree.layout("PointsMatrix - x selection", color='UTIL'):
            index = self.index_x*self.y_count
            if not(isinstance(y_index, int) and y_index == 0):
                index = index + y_index
            return self.matrix.points.index.equal(index)
    
    def sel_y(self, x_index=0):
        """ Build the selection for a line along the y dimension.
        
        Args:
        - x_index (Integer): x index of the line
        
        Returns:
        - Boolean in the matrix scope
        """
        
        with self.tree.layout("PointsMatrix - y selection", color='UTIL'):
            index = self.index_y
            if not(isinstance(x_index, int) and x_index == 0):
                index = index + x_index*self.y_count
            return self.matrix.points.index.equal(index)
        
        
    # ====================================================================================================
    # Output : read with dimension index
        
    # ----------------------------------------------------------------------------------------------------
    # Get a value along x
    
    def x_get(self, value, y_index=0):
        """ Get a value from the matrix with index of the x geometry.
        
        Args:
        - value : a matrix attribute
        - y_index (Integer=0) : y index
        
        Returns:
        - value along the x axis
        """
        x_index = self.x_points.index
        return self.x_points.sample_index(self.matrix.points, value=value, index=x_index*self.y_count + y_index)
    
    def y_get(self, value, x_index=0):
        """ Get a value from the matrix with index of the y geometry.
        
        Args:
        - value : a matrix attribute
        - x_index (Integer=0) : x index
        
        Returns:
        - value along the y axis
        """
        return self.y_points.sample_index(self.matrix.points, value=value, index=(x_index * self.y_count) + self.y_points.index)
    
    # ====================================================================================================
    # Set the ID to x or y index

    # ----------------------------------------------------------------------------------------------------
    # Set ID x and y
    
    def set_id_x(self):
        """ Set matrix points ID to x index.
        
        Performed to compute the field accumulation along x axis.
        """
        self.matrix.points.ID = self.index_x
        
    def set_id_y(self):
        """ Set matrix points ID to y index.
        
        Performed to compute the field accumulation along y axis.
        """
        self.matrix.points.ID = self.index_y 
        
    
        
    ##### OLD            
    
    # ----------------------------------------------------------------------------------------------------
    # x attribute
            
    def x_attribute(self, value):
        """ x attribute is sampled on the x geometry with the global index.
        """
        res = self.matrix.points.sample_index(self.x_points, value=value, index=self.index_x)
        res.node.label = 'x_attribute'
        return res

    # ----------------------------------------------------------------------------------------------------
    # y attribute
        
    def y_attribute(self, value):
        """ y attribute is sampled on the y geometry with the global index.
        """
        res = self.matrix.points.sample_index(self.y_points, value=value, index=self.index_y)
        res.node.label = 'y_attribute'
        return res
        
        
    # ----------------------------------------------------------------------------------------------------
    # Get / set an attribute on the matrix
    
    def get_attribute(self, attribute):
        res = self.capture(attribute)
        res.node.label = "Get attribute"
        return res
        
    def set_attribute(self, attribute, value, selection=True):
        res = attribute.switch(selection, value)
        res.node.label = "Set attribute"
        return res
    
    def index(self, i, j):
        res = self.capture(i*self.y_count + j)
        res.node.label = "Matrix index"
        return res
    
    #def sample(self, i, j, value):
    #    res = self.matrix.points.sample_index()
    #    res.nodes = "Matrix sample"
    #    return res
    
    ### END OF OLD
        
    # ----------------------------------------------------------------------------------------------------
    # Accumulate
        
    def accumulate(self, value, group_id='x'):
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
        
        with self.tree.layout("PointsMatrix: accumulate", color='UTIL'):
            
            if group_id is not None:
                if group_id.lower() == 'x':
                    self.set_id_x()
                elif group_id.lower() == 'y':
                    self.set_id_y()
                else:
                    raise Exception(f"PointsMatrix.accumulate error: 'group_id' argument must be 'x' or 'y', not {group_id}")
                    
            return self.matrix.points.accumulate_field(value, group_id=self.matrix.points.ID)
        
    def x_total(self, value, set_id=True):
        """ Sum a matrix attribute along x axis.
        
        This method is equivalent to ``` x_get(accumulate(...).total) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The total along the x axis
        """
        group_id = 'x' if set_id else None
        return self.x_get(self.accumulate(value, group_id).total)
    
    def y_total(self, value, set_id=True):
        """ Sum a matrix attribute along y axis.
        
        This method is equivalent to ``` y_get(accumulate(...).total) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The total along the x axis
        """
        group_id = 'y' if set_id else None
        return self.y_get(self.accumulate(value, group_id).total)
    
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
        return self.x_get(self.accumulate(value, group_id).total)
    
    def y_leading(self, value, set_id=True):
        """ Leading sum a matrix attribute along y axis.
        
        This method is equivalent to ``` y_get(accumulate(...).leading) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The leading total along the y axis
        """
        group_id = 'y' if set_id else None
        return self.y_get(self.accumulate(value, group_id).total)
    
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
        return self.x_get(self.accumulate(value, group_id).total)
    
    def y_trailing(self, value, set_id=True):
        """ Trailing sum a matrix attribute along y axis.
        
        This method is equivalent to ``` y_get(accumulate(...).trailing) ```.
        
        Args:
        - value : a matrix attribute
        - set_id (bool=True) : set matrix ID to x_index if True
        
        Returns:
        - The trailing total along the y axis
        """
        group_id = 'y' if set_id else None
        return self.y_get(self.accumulate(value, group_id).total)
    
    # ====================================================================================================
    # For square matrix
    
    @property
    def diagonal_index(self):
        res = self.index_x*(self.y_count + 1)
        res.node.label = "Diag index"
        return res
    
    def get_diagonal(self, value):
        with self.tree.layout("PointsMatrix - Get diagonal", color='UTIL'):
            x_index = self.x_points.index
            return self.x_points.sample_index(self.matrix.points, value, index=x_index*(self.y_count + 1))
    
    def set_diagonal(self, attribute, value):
        with self.tree.layout("PointsMatrix - Set diagonal", color='UTIL'):
            res = self.set_attribute(attribute, value, self.diagonal_selection)
            res.node.label = "Set diagonal"
            return res
    
    def triangle_selection(self, diagonal=False):
        if diagonal:
            res = self.index_x.greater_equal(self.index_y)
        else:
            res = self.index_x.greater_than(self.index_y)
        res.node.label = "Triangle sel"
        return res
            

    def set_triangle(self, attribute, value, diagonal=False):
        res = self.set_attribute(attribute, value, self.triangle_selection(diagonal=diagonal))
        res.node.label = "Set triangle"
        return res
    
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
            
     
   