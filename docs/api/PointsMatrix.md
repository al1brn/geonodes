# Class PointsMatrix

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

### Constructor

```python
PointsMatrix(self, x_geometry, y_geometry)
```

 Cross two geometries to perform computation on each couple of points between the two.

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

#### Args:
- x_geometry (Mesh, Curve or Points) : first geometry of points
- y_geometry (Mesh, Curve or Points) : second geometry of points




## Content

**Class and static methods**

[Demo](#Demo) | [Rain](#Rain)

**Methods**

[accumulate_node](#accumulate_node) | [capture](#capture) | [set_id_x](#set_id_x) | [set_id_y](#set_id_y) | [x_attribute](#x_attribute) | [x_get](#x_get) | [x_leading](#x_leading) | [x_total](#x_total) | [x_trailing](#x_trailing) | [y_attribute](#y_attribute) | [y_get](#y_get) | [y_leading](#y_leading) | [y_total](#y_total) | [y_trailing](#y_trailing)

## Class and static methods

### Demo

```python
@staticmethod
def Demo(nx=4, ny=3, name="PointsMatrix Demo")
```

 A demo of PointsMatrix?




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Rain

```python
@staticmethod
def Rain()
```

 Simulate dips falling on water.




<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### accumulate_node

```python
def accumulate_node(self, value, group_id='x')
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

### set_id_x

```python
def set_id_x(self)
```

 Set matrix points ID to x index.



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_id_y

```python
def set_id_y(self)
```

 Set matrix points ID to y index.



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### x_attribute

```python
def x_attribute(self, value)
```

 x attribute is sampled on the x geometry with the global index.



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### x_get

```python
def x_get(self, value)
```

 Get a value from the matrix with index of the x geometry.

#### Args:
- value : a matrix attribute

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

This method is equivalent to ``` x_get(accumulate_node(...).total) ```.

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
def y_get(self, value)
```

 Get a value from the matrix with index of the y geometry.

#### Args:
- value : a matrix attribute

#### Returns:
- value along the y axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### y_leading

```python
def y_leading(self, value, set_id=True)
```

 Leading sum a matrix attribute along y axis.

This method is equivalent to ``` y_get(accumulate_node(...).leading) ```.

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

This method is equivalent to ``` y_get(accumulate_node(...).total) ```.

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

This method is equivalent to ``` y_get(accumulate_node(...).trailing) ```.

#### Args:
- value : a matrix attribute
- set_id (bool=True) : set matrix ID to x_index if True

#### Returns:
- The trailing total along the y axis



<sub>Go to [top](#class-PointsMatrix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

