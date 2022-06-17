
# Class Domain

Root class for domains: PointDomain, FaceDomain, EdgeDomain, CornerDomain, CurveDomain and Instance

Fields are properties of domains.

Initialization is made in method init_socket called by initializer Socket.__init__

Domains classes


Domain classes are implemented as properties of geometries:
- Mesh owns `point`, `edge`, `face` and `corner` properties (`vertex` and `face_corner`
can be used rather than `point` and `corner`)
- Curve owns `point` and `spline` (`control_point` can be used rather than `point`)
- Points owns `point`
- Instances has no domain properties, fields are direct properties of this class
  
To get the index of a point, use the syntax:

```python
position = mesh.point.position
```

Thanks to this syntax, you always know which field you want.

```python
# mesh, curve and instances are initialized respectively as Mesh, Curve ans Instances

mesh.point.position  # position of the vertices
mesg.vertex.position # same
mesh.face.position   # position of the faces
mesh.face.area       # faces area
curve.point.position # location of the curve control_points
instances.index      # Indices of the individual instances
instances.position   # Location of the instances
```



## named_field

> Named field
  
Exposed methods are get_named_attribute and set_named_attribute to be closed to the name of the nodes
These methods use the named_field method (not named named_attribute to avoid misusing).

named_field creates an instance of NamedField and store it in a dedciated dictionnary

Raise an error if different data types are used for the same name


## get_named_attribute

> Get a named attribute socket
  
Make use named_field method


## set_named_attribute

> Set a named attribute socket
  
Make use named_field method

If data_type is None, the data_type is infered from the type of the value


## set_named_boolean

NOT SUPPORTED YET
ef get_named_byte_color(self, name):
return self.get_named_attribute(name, data_type='BYTE_COLOR')

