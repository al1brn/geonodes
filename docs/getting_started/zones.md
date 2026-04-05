# Zones

**Zones** are made of paired nodes:

- Simulation
- Repeat
- For Each Element
- Closure
- Bundle

The loop zones are implemented with the `for` syntax when Closure and Bundle are implemented with `with` context.


# Closure

The two **Closure** zone nodes are created when instantiating a Closure class.
To create the nodes, use the ***with*** context:

``` python
    # Create a closure adding 1 to the input
    with Closure() as cl:
        a = Float(1.0, "Float")
        a += 1
        a.out("Plus One")
```

The closure evaluation is made using the **evaluate** method. This method
takes a **signature** argument which is a dict describing the closure inputs and outputs.

``` python
with GeoNodes("Closure"):

    # Create a closure adding to two entries 
    with Closure() as cl0:
        a = Float(1.0, "A")
        b = Float(1.0, "B")
        (a + b).out("Sum")

    # If evaluated immediately, the signature is read from the previous nodes.
    cl0.evaluate().out(panel = "Separate 0")

    # We can get the closure signature for future use
    sig = cl0.get_signature()

    # We can evaluate a closure using this signature
    cl1 = Closure(name="Closure 1")
    cl1.evaluate(signature=sig).out(panel="Signature 1")

    # We can evaluate another closure using a manual signature:
    # a couple of dicts for input and output
    sig = (
        {'A': 'Float', 'B': 'Float'},
        {'Sum': 'Float'})

    cl2 = Closure(name="Closure 2")
    cl2.evaluate(signature=sig).out(panel="Signature 2")

    # Selecting a closure
    # Note that since the closure coming from MenuSwitch
    # doesn't come from a zone, the ***with*** context relates
    # to the 'Menu Switch', not the zone (compare to the creation of cl0).
    
    with Closure.MenuSwitch() as cl:
        cl0.out("Closure 0")
        cl1.out("Closure 1")
        cl2.out("Closure 2")

    cl.node.menu = Input(default_value="Closure 0")

    cl.out()
```

## Loops

To make the code as clear and pythonistic as possible, the Geometry nodes loop zones
**Simulation**, **Repeat** and **For Each Element** are implemented as python iterator.

- **Simulation** and **Repeat** : Socket iterator
- **For Each Element** : Domain iterator

``` python
    mesh = Mesh()

    for simul in mesh.simulation():
        # Nodes are created in the Simulation zone
        pass

    for rep in mesh.repeat(10):
        # Nodes are created in the Repeat zone
        pass

    for feel in mesh.points.for_each():
        # nodes are created in the For Each Element zone
        pass
```

The object returned by the iterator exposes the input and output sockets.

!!! note

    Within the ***for*** iteration, the **ouput sockets** come from **input node** and the
    **input sockets** are those of the **output node**.
    Outside the ***for***, the **ouput sockets** come from **output node** and the
    **input sockets** are those of the **input node**.

!!! note
    Within the ***for*** iteration, the geometry is the geometry to compute. The for iteration must
    end with `xxx.out()` where `xxx` is the name of the Geometry class.
    Outside the ***for*** iteration, the geometry has jumped to the zone output node and cand be used
    to continue.

### Simulation

``` python
with GeoNodes("Simulation"):
    
    # Two input parameters
    count  = Integer(10, "Count", 1, 100)
    radius = Float(.1, "Radius", 0, 2)
    
    # Cloud of points
    cloud = Cloud.Points(count=count, position=Vector.Random((-5, -5, 5), (5, 5, 15)))
    
    # Gravity simulation with initial random speed
    for sim in simulation(cloud=cloud, Speed=Vector.Random(-1, 1)):
        
        # One speed per point
        speed = sim.cloud.points.capture_attribute(sim.speed)
        
        # Increment the posiion
        sim.cloud.position += speed*sim.delta_time
        
        # Acceleration
        speed += sim.delta_time*(0, 0, -9.81)
        
        # Bounce onfloor
        x, y, z = speed.xyz
        speed = speed.switch(nd.position.z.less_than(radius), (.9*x, .9*y, -.7*z))
        
        # Next iteration
        speed.out("Speed")

    # Getting the simulation result
    cloud = sim.cloud

    with Layout("Instantiate the balls"):
        mesh = Mesh.Grid(20, 20)
        mesh += cloud.instance_on(instance=Mesh.UVSphere(radius=radius))
        
    # Outside de the loop, out to Group Output Node
    mesh.out()
```

### Repeat

``` python
with GeoNodes("Repeat"):

    # Parameters
    levels = Integer(5, "Levels", 1, 10)
    size = Float(5, "Size", .1, 10)
    
    delta = size/levels
    
    cube = Mesh.Cube(size=(size, size, 1))
    
    for rep in cube.repeat(levels):
        
        sz = size - rep.iteration*delta
        floor = Mesh.Cube(size=(sz, sz, 1))
        floor.transform(translation=(0, 0, rep.iteration ))
        
        cube += floor
        
    cube.out()
```

### For Each Element

``` python
with GeoNodes("For Eeach"):
    
    # Let's assume the input geometry is a mesh
    mesh = Mesh()
    
    # The geometry to add at the center of each face
    sph = Mesh.UVSphere(radius=Input("Sphere Radius", default_value=.2))
    
    # Loop on the faces
    for feel in mesh.faces.for_each():
        # Position of the face
        pos = mesh.faces.sample_index(nd.position, 0)
        
        # Move the to the center
        sph.transform(translation=pos)
        
        # By default, out in the generated panel
        sph.out()
        
    # Join the generated geometry
    mesh += feel.generated
    
    mesh.out()
```
