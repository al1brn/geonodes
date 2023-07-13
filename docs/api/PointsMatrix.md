# Class PointsMatrix

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

### Constructor

```python
PointsMatrix(self, x_geometry, y_geometry=None)
```

 Cross two geometries to perform computation on each couple of points between the two.

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

#### Args:
- x_geometry (Mesh, Curve or Points) : first geometry of points
- y_geometry (Mesh, Curve or Points) : second geometry of points




## Content

**Properties**

[diagonal_selection](#diagonal_selection)

**Class and static methods**

[Demo](#Demo)

**Methods**

[accumulate](#accumulate) | [capture](#capture) | [sel_x](#sel_x) | [sel_y](#sel_y) | [set_id_x](#set_id_x) | [set_id_y](#set_id_y) | [set_x](#set_x) | [set_y](#set_y) | [to_grid_shape](#to_grid_shape) | [x_attribute](#x_attribute) | [x_get](#x_get) | [x_leading](#x_leading) | [x_total](#x_total) | [x_trailing](#x_trailing) | [y_attribute](#y_attribute) | [y_get](#y_get) | [y_leading](#y_leading) | [y_total](#y_total) | [y_trailing](#y_trailing)

## Properties

### diagonal_selection

 Build the selection for the diagonal of a sqaure matrix.

#### Returns:
- Boolean in the matrix scope




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### Demo

```python
@staticmethod
def Demo(nx=4, ny=3, name="PointsMatrix Demo")
```

 A demo of PointsMatrix?




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### accumulate

```python
def accumulate(self, value, group_id='x')
```

 Create an 'Accumulate Field' node to compute along one axis.

Once the node is created, the result can be read in the requested geometry using 'x_get' or 'y_get'.
The methods x_leading, x_trailing, x_total and their equivalent along the y axis can be used directly
when only one socket is required.

Before creating the node, the ID is set to x_index or y_index depending on the value of group_id.

#### Args:
- value : the value to accumulated
- group_id (str='x') : set id to x_index or y_index

#### Returns:
- 'Accumulate Field' node




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture

```python
def capture(self, value)
```

 Capture a value in the matrix.

This method simply calls ``` self.matrix.points.capture_attribute(value) ```.

#### Args:
- value : value to capture in the matrix

#### Returns:
- Attribute socket of the 'Capture Attribute' node attribute



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sel_x

```python
def sel_x(self, y_index=0)
```

 Build the selection for a line along the x dimension.

#### Args:
- y_index (Integer): y index of the line

#### Returns:
- Boolean in the matrix scope



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sel_y

```python
def sel_y(self, x_index=0)
```

 Build the selection for a line along the y dimension.

#### Args:
- x_index (Integer): x index of the line

#### Returns:
- Boolean in the matrix scope




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_id_x

```python
def set_id_x(self)
```

 Set matrix points ID to x index.

Performed to compute the field accumulation along x axis.



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_id_y

```python
def set_id_y(self)
```

 Set matrix points ID to y index.

Performed to compute the field accumulation along y axis.



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_x

```python
def set_x(self, value)
```

 Value along x geometry is exploded in the whole matrix.

Used in combination with 'set_y', allows to combine the two dimensions:
    
#### Args:
- value (any): an x_geometry attribute

#### Returns:
- matrix.points attribute




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_y

```python
def set_y(self, value)
```

 Value along y geometry is exploded in the whole matrix.

Used in combination with 'set_x', allows to combine the two dimensions:
    
#### Args:
- value (any): an y_geometry attribute

#### Returns:
- matrix.points attribute




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_grid_shape

```python
def to_grid_shape(self, size=.1, z=0)
```

 Arrange the matrix points into a grid shape (for tests).



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### x_attribute

```python
def x_attribute(self, value)
```

 x attribute is sampled on the x geometry with the global index.



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### x_get

```python
def x_get(self, value, y_index=0)
```

 Get a value from the matrix with index of the x geometry.

#### Args:
- value : a matrix attribute
- y_index (Integer=0) : y index

#### Returns:
- value along the x axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### x_leading

```python
def x_leading(self, value, set_id=True)
```

 Leading sum a matrix attribute along x axis.

This method is equivalent to ``` x_get(accumulate_node(...).leading) ```.

#### Args:
- value : a matrix attribute
- set_id (bool=True) : set matrix ID to x_index if True

#### Returns:
- The leading sum along the x axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### x_total

```python
def x_total(self, value, set_id=True)
```

 Sum a matrix attribute along x axis.

This method is equivalent to ``` x_get(accumulate(...).total) ```.

#### Args:
- value : a matrix attribute
- set_id (bool=True) : set matrix ID to x_index if True

#### Returns:
- The total along the x axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### x_trailing

```python
def x_trailing(self, value, set_id=True)
```

 Trailing sum a matrix attribute along x axis.

This method is equivalent to ``` x_get(accumulate_node(...).trailing) ```.

#### Args:
- value : a matrix attribute
- set_id (bool=True) : set matrix ID to x_index if True

#### Returns:
- The trailing sum along the x axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### y_attribute

```python
def y_attribute(self, value)
```

 y attribute is sampled on the y geometry with the global index.



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### y_get

```python
def y_get(self, value, x_index=0)
```

 Get a value from the matrix with index of the y geometry.

#### Args:
- value : a matrix attribute
- x_index (Integer=0) : x index

#### Returns:
- value along the y axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### y_leading

```python
def y_leading(self, value, set_id=True)
```

 Leading sum a matrix attribute along y axis.

This method is equivalent to ``` y_get(accumulate(...).leading) ```.

#### Args:
- value : a matrix attribute
- set_id (bool=True) : set matrix ID to x_index if True

#### Returns:
- The leading total along the y axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### y_total

```python
def y_total(self, value, set_id=True)
```

 Sum a matrix attribute along y axis.

This method is equivalent to ``` y_get(accumulate(...).total) ```.

#### Args:
- value : a matrix attribute
- set_id (bool=True) : set matrix ID to x_index if True

#### Returns:
- The total along the x axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### y_trailing

```python
def y_trailing(self, value, set_id=True)
```

 Trailing sum a matrix attribute along y axis.

This method is equivalent to ``` y_get(accumulate(...).trailing) ```.

#### Args:
- value : a matrix attribute
- set_id (bool=True) : set matrix ID to x_index if True

#### Returns:
- The trailing total along the y axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

