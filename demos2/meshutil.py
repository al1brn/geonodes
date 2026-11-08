from geonodes import *

# ----------------------------------------------------------------------------------------------------
# Set cylinder topology
# ----------------------------------------------------------------------------------------------------

def set_cylinder_topology(cyl, nrings, nsegms):

    with Layout("Set Cylinder Topology"):
        bundle = Bundle.Combine(nrings=nrings, nsegms=nsegms)
        cyl.set_bundle(bundle)

    return cyl

# ----------------------------------------------------------------------------------------------------
# Set cylinder topology
# ----------------------------------------------------------------------------------------------------

def get_cylinder_topology(cyl):

    with Layout("Get Cylinder Topology"):
        bundle = cyl.get_bundle(remove=False)
        node = bundle.separate(signature={'nrings': Integer, 'nsegms': Integer})
        #nrings = bundle.get_item('nrings', socket_type='Integer')
        #nsegms = bundle.get_item('nsegms', socket_type='Integer')

        return node.nrings, node.nsegms

    return nrings, nsegms

# ----------------------------------------------------------------------------------------------------
# Fill a selection
# ----------------------------------------------------------------------------------------------------

def fill_selection(mesh, selection, center=None):
    with Layout("Fill Selection"):
        mesh = Mesh(mesh)
        if center is None:
            center = mesh.points.attribute_statistic(nd.position).mean
            
        mesh.edges[selection].extrude()
        top = mesh.top
        mesh.points[top].position = center
        mesh.points[top].merge(merge_id=1)

        return mesh

ordered_selection = Package("Ordered Selection", prefix="OSel")
curve_bones = Package("Curve Bones", prefix="CBone")
meshutil = Package("Meshutil")




# ====================================================================================================
# Curves
# ====================================================================================================

@meshutil.geo_modifier('Cross Splines')
def cross_splines():
    """# Cross Splines
    
    Curves
    """
    curve = Curve()
    use_resample = Boolean(False, "Resample")
    count = Integer(12, "Resolution")
    as_mesh = Boolean(False, "As Mesh")

    with Layout("Resample"):
        curve.switch(use_resample, Curve(curve).resample(count=count))
        nsplines = curve.splines.count
        npoints = curve.points.count // nsplines

    with Layout("Create crossed splines"):
        c = Curve.Line().resample(count=nsplines)
        bb = Cloud.Points(count=npoints)
        new_curve = Curve(bb.instance_on_points(instance=c).realize())

    # Example with nsplines = 3, npoints = 5
    #
    # Input
    # 0 > 0, 1, 2, 3, 4
    # 1 > 5, 6, 7, 8, 9
    # 2 > 10, 11, 12, 13, 14
    #
    # Output
    # 0> 0, 5, 10
    # 1> 1, 6, 11
    # 2> 2, 7, 12
    # 3> 3, 8, 13
    # 4> 4, 9, 14

    with Layout("Set position"):
        i_spline = (nd.index % nsplines)._lc("i Spline")
        i_point = (nd.index // nsplines)._lc("i Point")

        idx = i_spline*npoints + i_point
        new_curve.position = curve.points.sample_index(nd.position, index=idx)
        new_curve.radius = curve.points.sample_index(nd.radius, index=idx)

    with Layout("Mesh"):
        grid = Mesh.Grid(vertices_x=npoints, vertices_y=nsplines)
        grid.position = curve.points.sample_index(nd.position, index=i_spline*npoints + i_point)

    Geometry.Switch(as_mesh, new_curve, grid).out()
    npoints.out("Splines Count")
    nsplines.out("Points Count")

# ====================================================================================================
# Curves
# ====================================================================================================

@meshutil.geo_group('Subdivide Segment')
def subdivide_segment():
    """# Subdivide Segment
    
    Curves
    """

    curve = Curve()
    index = Integer(0, "Index", 0)
    sub = Integer(0, "Subdivisions")
    is_cyclic = Boolean(False, "Cyclic")

    count = curve.points.count
    index = gnmath.min(index, count-2)

    p0 = curve.points.sample_index(nd.position, index=index)
    p1 = curve.points.sample_index(nd.position, index=index+1)

    new_segment = Curve.Line(start=p0, end=p1).resample(count=2 + sub)
    new_curve = Curve.Line().resample(count=count + sub)
    new_curve.switch(is_cyclic, Curve.Circle(resolution=count + sub))

    new_curve.position = curve.points.sample_index(nd.position, index=nd.index)
    new_curve[(nd.index>index) & (nd.index <= index + sub)].position = new_segment.points.sample_index(nd.position, nd.index - index)
    new_curve[nd.index > index + sub].position = curve.points.sample_index(nd.position, index=nd.index - sub)

    new_curve.out()

# ====================================================================================================
# Cylinder Topology
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# New Cylinder
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_group('New Cylinder')
def new_cylinder():
    """# New Cylinder
    """

    nrings = Integer(2, "Rings", 2, 100)
    nsegms = Integer(12, "Segments", 3, 128)
    caps = Boolean(True, "Caps")
    radius = Float(1.0, "Radius")
    depth = Float(2.0, "Depth")
        
    new_cyl = Mesh.Cylinder(radius=radius, depth=depth, side_segments=nrings-1, vertices=nsegms, fill_type="None") 
    new_cyl.switch(caps,
              Mesh.Cylinder(radius=radius, depth=depth, side_segments=nrings-1, vertices=nsegms, fill_type="N-Gon"))

    nz = nd.normal.z
    new_cyl.faces.set("Cap", Integer.Switch(nz > 0.9, Integer.Switch(nz < -0.9, 0, -1), 1))
    new_cyl.transform(rotation=(0, pi, 0))
    new_cyl = set_cylinder_topology(new_cyl, nrings, nsegms)

    new_cyl.offset = (0, 0, depth/2)

    new_cyl.out()
    nrings.out("Rings Count")
    nsegms.out("Segments Count")

# ----------------------------------------------------------------------------------------------------
# Standard Cylinder input
# ----------------------------------------------------------------------------------------------------

def get_cylinder(use_create=True, name=None):
    
    cyl = Mesh(name=name)

    with Layout("Get Cylinder & topology"):        
        if use_create:
            nrings = Integer(2, "Rings", 2, 100)
            nsegms = Integer(12, "Segments", 3, 128)
            create = Boolean(False, "Create")
            
            with Layout("Create New Cylinder"):
                new_cyl = new_cylinder(rings=nrings, segments=nsegms)
                cyl.switch(create, new_cyl)

        nrings, nsegms = get_cylinder_topology(cyl)
    
    return cyl, nrings, nsegms

# ----------------------------------------------------------------------------------------------------
# Zone selection in a cylinder
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_group('Cylinder Selection')
def cylinder_selection():
    """ A zone is defined by ring and col indices plus number of rings and cols
    
    This Group is an helper to get position from a cylinder topology or set position
    to a cylinder.
    
    To pass selection between different topologies, the selected vertices are numbered
    from 0 to n-1 with an integer named Ranged. Outside the zone it is -1.
    
    To read positions from a cylinder zone (or more generally to sample cylinder vertices)
    pass a valid "Ranged" to the node and then use "Sample Index" output socket. The position
    is the cylinder sampled positions.
    
    To write position to a cylinder:
    - use  "Selection" output socket to select the vertices to set
    - connect "Ranged" output socket to another "Zone Selector" applied to the cylinder
    to get positions from
    - read "Position" from the seconde node
    
    
    The group returns:
    - Selection (Boolean) : True for vertices belonging to the zone
    - Sample Index (Integer) : index to use in sample_index
    - Position (Vector) : position of selected vertices using ranged input socket
    - Ranged (Integer) : index to use in another "Zone Selector" Group to read positions
        
    ``` python
    # zones must be the same size
    node_set = cylinder_selection(cyl, ...).node
    node_get = cylinder_selection(model, ranged=node_set.ranged, ...).node
    
    # Set cyl from model
    cyl.points[node_set.selection].position = node_get.position
    ```
    """
    
    cyl = Mesh()
    
    #use_ring = Boolean(True, "Ring")    
    ring_index = Integer(0, "Ring Index", -1)
    ring_count = Integer(1, "Ring Count", 1)
    
    #use_col = Boolean(False, "Col")
    col_index = Integer(-1, "Col Index", -1)
    col_count = Integer(1, "Col Count", 1)

    use_ring = ring_index >= 0
    use_col = col_index >= 0
    
    ranged = Integer(0, "Ranged", 0, tip="Range [0..n] computed from another cylindex index")
    
    with Layout("Cylinder Topology"):
        bundle = cyl.get_bundle(remove=False)
        raw_rings = bundle.get_item('nrings', socket_type='Integer')
        raw_segments = bundle.get_item('nsegms', socket_type='Integer')
        valid = (raw_rings > 0) & (raw_segments > 0)
        nrings = Integer(gnmath.max(raw_rings, 1))
        nsegms = Integer(gnmath.max(raw_segments, 1))

    with Layout("Zone Bounds"):
        # Rings stop at the end of the cylinder; columns wrap around its seam.
        start_ring = Integer(0).switch(use_ring, Integer(gnmath.min(gnmath.max(ring_index, 0), nrings)))
        count_rings = Integer(nrings).switch(use_ring,
            Integer(gnmath.min(gnmath.max(ring_count, 0), nrings-start_ring)))
        start_col = Integer(0).switch(use_col, ((col_index % nsegms)+nsegms) % nsegms)
        count_cols = Integer(nsegms).switch(use_col,
            Integer(gnmath.min(gnmath.max(col_count, 1), nsegms)))

    with Layout("Selection and Local Index"):
        i_ring = nd.index // nsegms
        i_col = nd.index % nsegms
        local_ring = i_ring-start_ring
        local_col = (i_col-start_col+nsegms) % nsegms
        selection = valid & (local_ring >= 0) & (local_ring < count_rings) & (local_col < count_cols)
        local_index = local_ring*count_cols + local_col
        local_index = Integer(-1).switch(selection, local_index)

    with Layout("Sample Zone"):
        valid_sample = valid & (ranged >= 0) & (ranged < count_rings*count_cols)
        absolute_index = (start_ring + ranged//count_cols)*nsegms + (start_col + ranged%count_cols) % nsegms
        sample_index = Integer(-1).switch(valid_sample, absolute_index)
        position = cyl.points.sample_index(nd.position, index=sample_index, clamp=False)

    selection.out("Selection")
    sample_index.out("Sample Index")
    position.out("Position")
    local_index.out("Ranged")

# ----------------------------------------------------------------------------------------------------
# Copy position
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_group('Cylinder Copy Position')
def cylinder_copy_position():
    """# Cylinder Copy Position
    
    Copy position
    """

    cyl = Mesh()
    
    with Panel("Target"):
        ring_index = Integer(0, "Ring Index", -1)
        ring_count = Integer(1, "Ring Count", 1)
        
        col_index = Integer(-1, "Col Index", -1)
        col_count = Integer(1, "Col Count", 1)

    with Panel("From"):
        model = Mesh(name="Model")
        model_ring_index = Integer(0, "Ring Index", -1)
        model_col_index = Integer(-1, "Col Index", -1)

    sel = cylinder_selection(
        cyl,
        ring_index=ring_index,
        ring_count=ring_count,
        col_index=col_index,
        col_count=col_count,
    )
    model_sel = cylinder_selection(
        model,
        ring_index=model_ring_index,
        ring_count=ring_count,
        col_index=model_col_index,
        col_count=col_count,
        ranged=sel.ranged
        )
    cyl[sel].position = model_sel.position

    cyl.out()

# ----------------------------------------------------------------------------------------------------
# View indices
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_group('View Cylinder Indices')
def view_cylinder_indices():
    """# View Cylinder Indices
    
    View indices
    """

    cyl, nrings, nsegms = get_cylinder(use_create=False)

    ring_index = Integer(0, "Ring Index", 0)
    ring_index = gnmath.min(ring_index, nrings - 1)
    name = String(name="Weld Name")
    ok_name = name.length() > 0
    name = "Weld " + name

    size = Float(1.0, "Size", 0, 10)
    rotz = Float.Angle(0, "Rotation")
    spread = Float(0.1, "Spread", 0, 10)
    offset = Vector(0, "Offset")

    sel = cylinder_selection(cyl, ring_index=ring_index)
    center = cyl.points[sel].attribute_statistic(nd.position).mean

    wid = Attribute(name, Integer).value
    for rep in repeat(nsegms, labels=None):
        idx = (ring_index*nsegms) + rep.iteration
        pos = cyl.points.sample_index(nd.position, index=idx)
        vrt_wid = cyl.points.sample_index(wid, index=idx)

        ind = rep.iteration.switch(ok_name, vrt_wid)
        s = ind.to_string().switch(ind == 0, "X")

        label = Curve(s.to_curves(size=size).realize()).fill()
        label.transform(rotation=(pi/2, 0, rotz))
        label.offset = pos + (pos - center).scale(spread)
        rep.labels += label

    for rep in repeat(nrings, labels=rep.labels):
        idx = (rep.iteration*nsegms)
        pos = cyl.points.sample_index(nd.position, index=idx)

        ind = rep.iteration
        s = ind.to_string()

        label = Curve(s.to_curves(size=size).realize()).fill()
        label.transform(rotation=(pi/2, 0, rotz))
        label.offset = pos + (pos - center).scale(spread)
        rep.labels += label

    labels = rep.labels
    labels.offset = offset

    labels.out()

# ----------------------------------------------------------------------------------------------------
# Add rings
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_group('Add Rings to Cylinder')
def add_rings_to_cylinder():
    """# Add Rings to Cylinder
    
    Add rings
    """

    cyl, nrings, nsegms = get_cylinder(use_create=False)

    count = Integer(1, "Count", 0)
    below = Boolean(False, "Below")

    new_cyl = new_cylinder(rings=nrings + count, segments=nsegms)

    node = cylinder_selection(new_cyl, 
                    ring_index=Integer(count).switch_false(below, 0),
                    ring_count=nrings)

    ranged = nd.index - Integer.Switch(below, 0, count*nsegms)
    new_cyl[node.selection].position = cyl.points.sample_index(nd.position, index=ranged)

    new_cyl.switch(count < 1, cyl).out()

# ----------------------------------------------------------------------------------------------------
# Dome Cylinder
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_group('Close Cylinder')
def close_cylinder():
    """# Close Cylinder
    
    Dome Cylinder
    """

    cyl, nrings, nsegms = get_cylinder(use_create=False)
    count = Integer(3, "Rings", 1)
    height = Float(1.0, "Height", 0.0)

    use_bot = Boolean(True, "Bottom")
    use_top = Boolean(True, "Top")
    use_flat = Boolean(False, "Flatten Last")
    use_append = Boolean(False, "Append")

    original = Mesh(cyl)
    count = count.max(1)
    # Without append, each cap consumes Count rings and needs an
    # untouched base ring plus a neighbouring ring for its direction.
    cap_count = Integer(use_bot) + Integer(use_top)
    valid = (nrings >= 2) & (nsegms >= 3) & (
        use_append | (nrings >= count*cap_count + 2))

    with Layout("Append Rings"):
        new_cyl = add_rings_to_cylinder(cyl, count=count, below=True)
        ok = use_append & use_bot
        cyl.switch(ok, new_cyl)
        nrings.switch(ok, nrings + count)

        new_cyl = add_rings_to_cylinder(cyl, count=count, below=False)
        ok = use_append & use_top
        cyl.switch(ok, new_cyl)
        nrings.switch(ok, nrings + count)

    for bot_cap in (True, False):
        with Layout("Bottom Cap" if bot_cap else "Top Cap"):

            i_ring = count if bot_cap else nrings - 1 - count

            sel = cylinder_selection(cyl, ring_index=i_ring)
            center = cyl.points[sel].attribute_statistic(nd.position)

            sel0 = cylinder_selection(cyl, ring_index=i_ring + 1 if bot_cap else i_ring - 1)
            center0 = cyl.points[sel0].attribute_statistic(nd.position)

            direc = (center - center0).normalize().scale(height.max(0.0))

            loop_count = Float(count).switch(use_flat, count + 1)
            for rep in repeat(count, cyl=cyl):

                last_iteration = use_flat.bnot() & (rep.iteration==count-1)

                angle = (rep.iteration + 1) * (pi/2) / loop_count
                # Force the final radius to zero, without cosine roundoff.
                sx = angle.cos().switch(last_iteration, 0.0)
                sy = angle.sin()
                ir = i_ring - 1 - rep.iteration if bot_cap else i_ring + 1 + rep.iteration
                c = cylinder_copy_position(rep.cyl, ring_index=ir, model=cyl, from_ring_index=i_ring)

                sel = cylinder_selection(c, ring_index=ir)
                c[sel].position = center + direc.scale(sy) + (nd.position - center).scale(sx)
                c[sel].set('Weld TOP', Integer.Switch(last_iteration, 0, 1 if bot_cap else 2))

                rep.cyl = c

            cyl.switch(use_bot if bot_cap else use_top, rep.cyl)

    original.switch(valid, cyl).out()

# ----------------------------------------------------------------------------------------------------
# Cylinder enveloppe
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_modifier('Bones Envelope')
def bones_envelope():
    """# Bones Envelope
    
    Cylinder enveloppe
    """
    
    curve = Curve()
    radius = Float(0.2, "Radius")
    use_cross = Boolean(False, "Cross Splines")
    
    use_resample = Boolean(False, "Resample")
    spline_resol = Integer(10, "Spline Resolution", 2, 100)
    
    use_interpolate = Boolean(False, "Interpolate")
    interp_resol = Integer(16, "Interpolation Resolution", 1, 100)
    with Panel("Finalize"):
        nsubdiv = Integer(0, "Subdivide", 0, 10)
        use_smooth = Boolean(True, "Shade Smooth")
    
    with Panel("Side Rounding"):
        ncaps = Integer(3, "Resolution", 0, 32)
    
    with Layout("Prepare"):
        curve.points.radius = radius
        curve.switch(use_resample, Curve(curve).resample(count=spline_resol))
        
        crossed = cross_splines(curve)
        
        interp = Curve(crossed)
        interp.splines.type = 'Bezier'
        interp.handle_type = 'Auto'
        interp.resample(count=interp_resol)
        
        crossed.switch(use_interpolate, interp)
        
        bones = Curve(Geometry.Switch(use_cross, cross_splines(crossed), crossed))
        nsplines = bones.splines.count
        npoints = bones.points.count // nsplines
        
    with Layout("Additional Points for rounding"):
        
        with Layout("Duplicate with more points"):
            new_npoints = npoints + 2*ncaps
            c = Curve.Line().resample(count=new_npoints)
            bb = Cloud.Points(count=nsplines)
            
            rounded = Curve(bb.instance_on_points(instance=c).realize())
        
        with Layout("Position and radius"):
            i_spline = nd.index // new_npoints
            i_point = nd.index % new_npoints
            
            idx = i_spline*npoints + i_point - ncaps
            rounded.position = bones.points.sample_index(nd.position, index=idx)
            rounded.points.radius = bones.points.sample_index(nd.radius, index=idx)
            
        with Layout("First additional points position and radius"):
            idx = i_spline*npoints
            sel = i_point < ncaps
            ag = (ncaps - i_point)/(ncaps+1)*(pi/2)

            tg = bones.points.sample_index(nd.curve_tangent, index=idx)
            nrm = bones.points.sample_index(nd.normal, index=idx)
            pos = bones.points.sample_index(nd.position, index=idx)
            r = bones.points.sample_index(nd.radius, index=idx)
            
            rounded[sel].position = pos - tg.scale(r*ag.sin())
            rounded[sel].set_normal_free(nrm)
            rounded[sel].radius = r*ag.cos()
            
        with Layout("Second addition points position and radius"):
            idx = (i_spline + 1)*npoints - 1
            sel = i_point >= ncaps + npoints
            ag = (i_point - ncaps - npoints + 1)/(ncaps+1)*(pi/2)
            
            tg  = bones.points.sample_index(nd.curve_tangent, index=idx)
            nrm = bones.points.sample_index(nd.normal, index=idx)
            pos = bones.points.sample_index(nd.position, index=idx)
            r = bones.points.sample_index(nd.radius, index=idx)

            rounded[sel].position = pos + tg.scale(r*ag.sin())
            rounded[sel].set_normal_free(nrm)
            rounded[sel].radius = r*ag.cos()
            
        with Layout("Switch is caps are required"):
            use_rounded = ncaps > 0
            bones.switch(use_rounded, rounded)
            npoints.switch(use_rounded, new_npoints)
            

    # For dev
    geos = []
    geos.append(bones)
    
    with Layout("First Side"):
        side0 = Curve(bones)
        side0.offset = nd.normal.scale(nd.radius)
        
    with Layout("Second Side"):
        side1 = Curve(bones)
        side1.offset = nd.normal.scale(-nd.radius)
        
    with Layout("Envelope"):
        
        nrings = nsplines
        nsegms = 2*npoints#*(npoints + cap_count)
        cyl = new_cylinder(rings=nrings, segments=nsegms)

        i_ring  = nd.index // nsegms
        i_point = nd.index % nsegms

        idx = i_ring*npoints + i_point
        cyl[i_point < npoints].position  = side0.points.sample_index(nd.position, index=idx)
        
        idx = (i_ring + 2)*npoints - 1 - i_point
        cyl[i_point >= npoints].position = side1.points.sample_index(nd.position, index=idx)
        cyl[(i_point % npoints) >= npoints].position = 0
        
    with Layout("Closing & Finalize"):
        
        cyl = close_cylinder(cyl, append=True).link_inputs(from_panel="Caps")
        
        # Need to flip ;-)
        cyl.flip_faces()
        
        cyl.subdivide(nsubdiv)
        
        cyl.faces.shade_smooth = use_smooth
        
    
    cyl.out()

# ====================================================================================================
# Rounded Joint
# ====================================================================================================

@meshutil.geo_group('Rounded Joint')
def rounded_joint():
    """ Rounded angle in the plane XZ.
    Positive is Z to X
    """
    
    pos = Vector(name="Position")
    start_angle = Float.Angle(0.0, "Start Angle")
    angle = Float.Angle(0, "Angle")
    resol = Integer(5, "Resol", 1)
    length = Float(1, "Length")
    
    with Layout("Preparation"):
        # Resol is the number of output points (one means a sharp joint).
        count = resol.max(1)
        turn = angle.clamp(-pi + .001, pi - .001)
        magnitude = turn.abs()
        is_null = magnitude < .00001
        safe_angle = magnitude.max(.00001)
        arc_length = length.max(0.0)
        radius = arc_length / safe_angle
        trim = radius * (magnitude / 2).tan()
        sign = Float.Switch(turn < 0, 1.0, -1.0)

    with Layout("Tangent Arc"):
        arc = Curve.Line().resample(count=count)
        t = nd.index / (count - 1).max(1)
        theta = magnitude * t
        local = Vector((sign * radius * (1.0-theta.cos()), 0,
                        radius * theta.sin() - trim))
        local = local.switch(is_null, Vector((0,0,(t-.5)*arc_length)))
        local = local.switch(count == 1, Vector((0,0,0)))
        arc.points.position = Rotation((0,start_angle,0)) @ local + pos

    arc.out()

# ====================================================================================================
# Build a Poly Line
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Bottom up
# ----------------------------------------------------------------------------------------------------

# Append a vertex to an open polyline.
@meshutil.geo_modifier('Build Poly Line')
def build_poly_line():
    """# Build Poly Line
    
    Append a vertex to an open polyline.
    """
    curve = Curve()
    use_position = Boolean(False, "Use Position")
    position = Vector((0,0,0), "Position")
    angle = Float.Angle(0.0, "Angle")
    length = Float.Distance(1.0, "Length", 0.0)
    plane_index = Integer.MenuSwitch({
        'XY': 0,
        'XZ': 1,
        'YZ': 2,
    }, menu=Input('Plane'), default_menu='XY')
    radius = Float(1.0, "Radius")

    with Layout("New Curve"):
        count = curve.points.count
        is_new = count < 2
        cag, sag = angle.cos(), angle.sin()
        target = Vector.Switch(use_position,
                Vector.IndexSwitch((cag, sag, 0), (sag, 0, cag), (0, cag, sag), index=plane_index).scale(length),
                position)
        new_curve = Curve.Line(end=target)
        new_curve.radius = radius

    with Layout("Target Point"):
        p0 = curve.points.sample_index(nd.position, index=count-2)
        p1 = curve.points.sample_index(nd.position, index=count-1)
        vect = (p1 - p0).normalize().scale(length)
        rot = Rotation.IndexSwitch((0, 0, angle), (0, angle, 0), (angle, 0, 0), index=plane_index)
        target = Vector.Switch(use_position,
                    p1 + rot @ vect,
                    position)

    with Layout("Append Point"):
        new_count = Integer(gnmath.max(count+1, 2))
        extended = Curve.Line().resample(count=new_count)
        extended.points.position = curve.points.sample_index(nd.position, index=nd.index)
        extended.points.radius = curve.points.sample_index(nd.radius, index=nd.index)

        last_sel = nd.index == new_count-1
        extended.points[last_sel].position = target
        extended.points[last_sel].radius = radius

    extended.switch(is_new, new_curve).out()

# ----------------------------------------------------------------------------------------------------
# Inverse kinematics
# ----------------------------------------------------------------------------------------------------

@meshutil.geo_modifier('Build Bones Curve')
def build_bones_curve():
    """# Build Bones Curve
    
    Inverse kinematics
    """

    curve = Curve()
    direc = Vector((0, 0, 1), "Direction", shape='Single')
    rotation = Rotation(0, "Rotation", hide_value=True)
    length = Float(1.0, "Length")
    
    count = curve.points.count
    
    # All positions to 0
    curve.position = 0
    direc = direc.normalize()

    for rep in repeat(curve.points.count - 1, curve=curve, rotation=rotation, length=length):

        idx = count-2 - rep.iteration
        sel = nd.index > idx

        rot = rep.curve.points.sample_index(rep.rotation, index=idx)
        lg = rep.curve.points.sample_index(rep.length, index=idx)

        rep.curve[sel].offset = direc.scale(lg)
        rep.curve[sel].position = rot @ nd.position
        
    rep.curve.out()


# ====================================================================================================
# Rounded angles
# ====================================================================================================

# Round every interior corner, retaining the ends and the spline structure.
@meshutil.geo_modifier('Round Joints')
def round_joints():
    """# Round Joints
    
    Round every interior corner, retaining the ends and the spline structure.
    """
    curve = Curve()
    selection = Boolean(True, "Selection", hide_value=True,
                        tip="Curve points whose corners should be rounded.")
    resolution = Integer(5, "Resolution", 0, 128)
    length = Float.Distance(1.0, "Length", 0.0,
        tip="Requested arc length at each corner, limited to fit adjacent segments.")
    original = Curve(curve)

    with Layout("Corner Geometry"):
        before = nd.offset_point_in_curve(point_index=nd.index, offset=-1)
        after = nd.offset_point_in_curve(point_index=nd.index, offset=1)
        p0 = curve.points.sample_index(nd.position, index=before.point_index_)
        p1 = curve.points.sample_index(nd.position, index=after.point_index_)
        incoming = nd.position-p0
        outgoing = p1-nd.position
        turn = incoming.normalize().dot(outgoing.normalize()).clamp(-1.0,1.0).acos()
        valid = selection & before & after & (turn > .00001) & (turn < pi-.00001)
        straight = curve.points.capture_attribute(
            selection & before & after & (turn <= .00001))
        radius = Float(0.0).switch(valid, length.max(0.0)/turn.max(.00001))

    with Layout("Rounded Polyline"):
        curve = curve.fillet(radius=radius, limit_radius=True, mode='Poly', count=resolution)

    with Layout("Straight Joints"):
        # Fillet adds Resolution points at a corner, but skips straight
        # joints. Insert the same number there, spread over Length.
        base = Curve(curve)
        previous = nd.offset_point_in_curve(point_index=nd.index, offset=-1)
        following = nd.offset_point_in_curve(point_index=nd.index, offset=1)
        p0 = base.points.sample_index(nd.position, index=previous.point_index_)
        p1 = base.points.sample_index(nd.position, index=following.point_index_)
        half_length = gnmath.min(length.max(0.0)/2,
            gnmath.min((nd.position-p0).length(), (p1-nd.position).length())/2)
        extent = (p1-nd.position).normalize().scale(half_length)
        for rep in repeat(base.points.count, curve=curve, added=Integer(0)):
            selected = base.points.sample_index(straight, index=rep.iteration)
            cuts = Integer.Switch(selected, 0, resolution)
            index = rep.iteration + rep.added
            center = base.points.sample_index(nd.position, index=rep.iteration)
            delta = base.points.sample_index(extent, index=rep.iteration)
            result = Curve(rep.curve)
            result.subdivide(cuts=Integer.Switch(nd.index == index, 0, cuts))
            t = Float(nd.index-index)/resolution.max(1)
            result.points[(cuts > 0) & (nd.index >= index)
                          & (nd.index <= index+cuts)].position = center + delta.scale(2*t-1)
            rep.curve = result
            rep.added += cuts
        curve = rep.curve

    with Layout("Output"):
        curve = curve.switch(resolution == 0, original)
        curve.out()

# ====================================================================================================
# A rounded shape surrounding a curve
# ====================================================================================================

# Surrounding Shape
@meshutil.geo_modifier('Surrounding Shape')
def surrounding_shape():
    """# Surrounding Shape
    """
    
    curve = Curve()
    resol = Integer(32, "Resolution", 12, 128)
    width = Float(1.0, "Width", 0)
    inflate = Float(1.0, "Inflate", 1.0)

    with Layout("Rounded Bezier"): 
        
        npoints = curve.points.count
        
        v0 = (nd.position - curve.points.sample_index(nd.position, index = nd.index - 1)).normalize()
        v1 = (curve.points.sample_index(nd.position, index = nd.index + 1) - nd.position).normalize()
        ag = gnmath.asin(v0.cross(v1).abs())
        
        xscale = width/2
        extend0 = curve.points.sample_index(nd.position - v1.scale(xscale), index=0)
        extend1 = curve.points.sample_index(nd.position + v0.scale(xscale), index=npoints - 1)
        
        ag.switch((nd.index == 0) | (nd.index==npoints - 1))
        
        curve.points.radius = ag.map_range(from_max=pi/2, to_min=1, to_max=inflate)
        
        curve.splines.type = 'BEZIER'
        curve.handle_type = 'Auto'
        curve.splines.resolution = 12

    with Layout("To mesh"):
        line = Curve.Line(start=(-width/2, 0, 0), end=(width/2, 0, 0))
        mesh = curve.to_mesh(profile_curve=line, scale=nd.radius)
        
    with Layout("Curve"):
        
        n = mesh.points.count
        n2 = n //2
        
        # Two additional points, exemple with n = 10, n2=5
        # [0, 1, 2, 3, 4] idx0=n2 [6, 7, 8, 9, 10] idx1=n + 1
        shape = Curve.Circle(resolution=n + 2)
        
        idx0 = n2
        idx1 = n + 1
        
        shape.points[nd.index < n2].position = mesh.points.sample_index(nd.position, index=nd.index*2)
        shape.points[nd.index > n2].position = mesh.points.sample_index(nd.position, index=n - (nd.index - n2 - 1)*2 - 1)
        
        shape.points[nd.index == idx0].position = extend1
        shape.points[nd.index == idx1].position = extend0
        
    with Layout("Back to Bezier for rounded extremities"):
        
        shape.splines.type = 'BEZIER'
        shape.handle_type = 'Auto'
        shape.resample(mode='Length', length=width/5)
        shape.resample(count=resol)
        
    shape.out()

# ====================================================================================================
# Create a cage surrounding vertical bones
# ====================================================================================================

@meshutil.geo_modifier('Cage Around Bones')
def cage_around_bones():
    """# Cage Around Bones
    
    Create a cage surrounding vertical bones
    """
    
    curve = Curve()
    bone_resol = Integer(6, "Segments Resolution", 2, 128)
    ring_resol = Integer(12, "Rings Resolution", 12, 128)
    
    width = Float(1.0, "Width", 0)
    inflate = Float(1.0, "Inflate", 1.0)
    
    curve.resample(count=bone_resol)
    nsplines = curve.splines.count

    cyl = new_cylinder(rings=bone_resol, segments=ring_resol)
    bones = Curve.Line().resample(count=nsplines)
    
    for rep in repeat(bone_resol, cyl=cyl):
        
        idx = rep.iteration
        bones.points.position = curve.points.sample_index(nd.position, index=nd.index*bone_resol + idx)
        
        shape = surrounding_shape(bones, resolution=ring_resol, width=width, inflate=inflate)

        sel_node = cylinder_selection(rep.cyl, ring_index=rep.iteration).node
        rep.cyl.points[sel_node.selection].position = shape.points.sample_index(nd.position, index=sel_node.ranged)
        
    cage = Mesh(rep.cyl)
    
    cage.faces.shade_smooth = False
    
    cage.out()

# ====================================================================================================
# Interpolate director offsets with a Gaussian radial basis
# ====================================================================================================

@meshutil.geo_group('Mesh Distort')
def mesh_distort():
    """# Mesh Distort
    
    Interpolate director offsets with a Gaussian radial basis
    """
    mesh = Mesh()
    selection = Boolean(True, "Selection", hide_value=True)
    move_selection = Boolean(False, "Move Selection", hide_value=True)
    offset = Vector(None, "Offset")
    distance = Float(1.0, "Distance", 0.0,
                     tip="Gaussian influence radius; weight is exp(-(d/Distance)^2).")

    radius = distance.max(0.000001)

    def influence(delta):
        return (-(delta.dot(delta) / (radius*radius))).exp()

    with Layout("Directors at rest"):
        directors = Mesh(mesh)
        director_offset = directors.points.capture_attribute(offset)
        directors = Mesh(directors.points[move_selection].separate())
        count = directors.points.count

    with Layout("Interpolation system"):
        # Each point stores one matrix entry A[row, column]. The vector
        # right-hand side is duplicated across the columns of each row.
        matrix = Cloud.Points(count=count*count)
        row = nd.index // count.max(1)
        column = nd.index % count.max(1)
        p0 = directors.points.sample_index(nd.position, index=row)
        p1 = directors.points.sample_index(nd.position, index=column)
        rhs = directors.points.sample_index(director_offset, index=row)
        matrix.points.set("A", influence(p0-p1))
        matrix.points.set("B", rhs)

    with Layout("Solve director coefficients"):
        # Gaussian elimination, followed by elimination above the pivot
        # (Gauss-Jordan). Distinct directors give a positive definite A.
        for rep in repeat(count, matrix=matrix):
            work = Cloud(rep.matrix)
            pivot_index = rep.iteration*count + rep.iteration
            pivot = work.points.sample_index(Float("A"), index=pivot_index)
            pivot_rhs = work.points.sample_index(Vector("B"), index=pivot_index)
            pivot_row = row == rep.iteration
            work.points[pivot_row].set("A", Float("A")/pivot)
            work.points[pivot_row].set("B", pivot_rhs/pivot)

            # Sample from the normalized matrix before changing either
            # field, so all rows use the same elimination step.
            multiplier = work.points.sample_index(
                Float("A"), index=row*count + rep.iteration)
            pivot_value = work.points.sample_index(
                Float("A"), index=rep.iteration*count + column)
            pivot_rhs = work.points.sample_index(
                Vector("B"), index=rep.iteration*count)
            work.points[pivot_row.bnot()].set(
                "A", Float("A") - multiplier*pivot_value)
            work.points[pivot_row.bnot()].set(
                "B", Vector("B") - pivot_rhs.scale(multiplier))
            rep.matrix = work
        matrix = rep.matrix

    with Layout("Interpolate displacement"):
        for rep in repeat(count, displacement=Vector((0, 0, 0))):
            center = directors.points.sample_index(nd.position, index=rep.iteration)
            coefficient = matrix.points.sample_index(
                Vector("B"), index=rep.iteration*count)
            rep.displacement += coefficient.scale(influence(nd.position-center))

        # Enforce the supplied offsets at the directors themselves,
        # avoiding small residual errors from the floating-point solve.
        displacement = Vector.Switch(move_selection, rep.displacement, offset)
        mesh[selection].offset = displacement
    mesh.out()

# ====================================================================================================
# Bones simulation
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Initialize a new Curve Bone from a Curve
# ----------------------------------------------------------------------------------------------------

@curve_bones.geo_group('New')
def cbone_new():
    """# CBone New
    
    Initialize a new Curve Bone from a Curve
    """
    
    curve = Curve()
    
    curve.points.set("Pos", nd.position)
    curve.points.set("Transform", Matrix.CombineTransform())
    
    with Layout("Normals"):
        pos0 = nd.position
        pos1 = curve.points.sample_index(nd.position, index=nd.index+1)
        segm = pos1 - pos0
        u = segm.normalize()
        
        curve.points.set("u", u)
        
        for rep_spline in repeat(curve.splines.count, curve=curve, index_offset=0):
            
            spline = Curve(Curve(curve).splines[nd.index == rep_spline.iteration].separate())
            npoints = spline.points.count
            
            with Layout("First Segment"):
                
                point_index = rep_spline.index_offset
                
                u = curve.points.sample_index(Vector("u"), index=point_index)
                
                z = u.dot((0, 0, 1))
                is_vert = z.abs() == 1.0
                
                perp = u.cross((0, 0, 1)).normalize()
                
                perp.switch(is_vert, Vector.Switch(z < 0, (1, 0, 0), (-1, 0, 0)))
                
                sel = nd.index == point_index
                rep_spline.curve[sel].set("Perp", perp)
                
            with Layout("Other segments"):
                for rep in repeat(npoints - 2, curve=rep_spline.curve, prev_u=u, prev_perp=perp):
                    
                    point_index = rep_spline.index_offset + rep.iteration + 1
                    
                    u = curve.points.sample_index(Vector("u"), index=point_index)
                    
                    z = rep.prev_u.dot(u)
                    is_aligned = z == 1.0
                    
                    perp = rep.prev_u.cross(u).normalize()
                    
                    perp.switch(is_aligned, rep.prev_perp)
                    
                    sel = nd.index == rep_spline.index_offset + rep.iteration + 1
                    rep.curve[sel].set("Perp", perp)
                    
                    rep.prev_u = u
                    rep.prev_perp = perp
                    
                rep_spline.curve = rep.curve
                rep_spline.index_offset += npoints
                    
        curve = rep_spline.curve
    
    curve.out()        
    
# ----------------------------------------------------------------------------------------------------
# Curve Bone rotation
# ----------------------------------------------------------------------------------------------------

@curve_bones.geo_group('Rotate')
def cbone_rotate():
    """# CBone Rotate
    
    Curve Bone rotation
    """
    
    curve = Curve()
    curve_index = Integer(0, "Curve Index")
    index = Integer(0, "Index")
    rot = Rotation(None, "Rotation")
    use_local = Boolean(True, "Local")
    
    with Layout("Index"):
        point_index = nd.points_of_curve(curve_index=curve_index, sort_index=index)._lc("Index")
        total = point_index.total
        last_index = point_index - index + total - 1
        
        sel = (nd.index >= point_index) & (nd.index <= last_index)
        
    with Layout("Local Rotation"):
        pos0 = curve.points.sample_index(nd.position, index=point_index)
        pos1 = curve.points.sample_index(nd.position, index=point_index + 1)
        perp = curve.points.sample_index(Vector("Perp"), index=point_index)
        
        to_local = nd.axes_to_rotation(
            primary_axis_1=pos1 - pos0, 
            secondary_axis_1=perp, 
            primary_axis='Z',
            secondary_axis='X')

    with Layout("Apply local rotation"):
        rot = Rotation.Switch(use_local, rot, to_local.invert() @ (rot @ to_local))
    
        transform = Matrix.CombineTransform(translation=-pos0)
        transform = Matrix.CombineTransform(translation=pos0, rotation=rot) @ transform
        curve.points[sel].set("Transform", transform @ Matrix("Transform"))
    
        curve.offset = -pos0
        curve[sel].position = rot @ nd.position
        curve[sel].set("Perp", rot @ Vector("Perp"))
        curve.offset = pos0
        
    curve.out()      

# ----------------------------------------------------------------------------------------------------
# Curve Bone Translation
# ----------------------------------------------------------------------------------------------------

@curve_bones.geo_group('Translate')
def cbone_translate():
    """# CBone Translate
    
    Curve Bone Translation
    """
    
    curve = Curve()
    curve_index = Integer(0, "Curve Index", 0)
    index = Integer(0, "Index")
    trans = Vector(name="Translation")
    
    with Layout("Index"):
        point_index = nd.points_of_curve(curve_index=curve_index, sort_index=index)._lc("Index")
        total = point_index.total
        last_index = point_index - index + total - 1
        
        sel = (nd.index >= point_index) & (nd.index <= last_index)
        
    with Layout("Compute the transformation"):
        transform = Matrix.CombineTransform(translation=trans)
        curve.points[sel].set("Transform", transform @ Matrix("Transform"))
        
    with Layout("Transform the Curve"):
        curve[sel].offset = trans
    
    curve.out()
    
# ----------------------------------------------------------------------------------------------------
# Curve Bone Influence
# ----------------------------------------------------------------------------------------------------

@curve_bones.geo_group('Distance')
def cbone_distance():
    """# CBone Distance
    
    Curve Bone Influence
    """
    
    curve = Curve()
    position = Vector(None, "Position", hide_value=True, default_input='Position')
    closed = Boolean(False, "Closed")
    
    with Layout("Prepare"):
        npoints = curve.points.count
        next_index = Integer.Switch(closed, nd.index + 1,
                                    (nd.index + 1).floored_modulo(npoints))
        pos1 = curve.points.sample_index(nd.position, index=next_index)
        segm = pos1 - nd.position
        segm_len = segm.length()
        segm = segm.normalize()
        
        curve.points.set("Pos0", nd.position)
        curve.points.set("Segm", segm)
        curve.points.set("Segm Len", segm_len)
        
    count = Integer.Switch(closed, curve.points.count - 1, curve.points.count)
    for rep in repeat(count, curve=curve, edge_index=-1, dist=0.0, proj=0.0):
        
        pos0 = curve.points.sample_index(Vector("Pos0"),        index=rep.iteration)
        segm = curve.points.sample_index(Vector("Segm"),        index=rep.iteration)
        segm_len = curve.points.sample_index(Float("Segm Len"), index=rep.iteration)
        
        v = position - pos0
        proj = v.dot(segm)
        ok = (proj >= 0) & (proj <= segm_len)
        
        rep.edge_index.switch(ok, rep.iteration)
        rep.dist.switch(ok, (v - segm.scale(proj)).length())
        rep.proj.switch(ok, proj/segm_len)
        
    (rep.edge_index >= 0).out("Is Valid")
    rep.edge_index.out("Index")
    rep.dist.out("Distance")
    rep.proj.out("Proj")
    
# ----------------------------------------------------------------------------------------------------
# Link a curve bones to a Mesh
# ----------------------------------------------------------------------------------------------------

@curve_bones.geo_modifier('Link')
def cbone_link():
    """# CBone Link
    
    Link a curve bones to a Mesh
    """
    
    mesh = Mesh()
    selection = Boolean(True, "Selection")
    curve = Curve(None, "Curve")
    distance = Float(1.0, "Distance")
    fall_off = Float.Factor(0.1, "Fall Off", 0, 1)
    closed = Boolean(False, "Closed")

    nsplines = curve.splines.count
    
    mesh.points.set("Bone Weight", 0.0)
    
    for rep in repeat(nsplines, mesh=mesh, total=0):

        spline = Curve(Curve(curve).splines[nd.index==rep.iteration].separate())
        npoints = spline.points.count
        
        sel = (Integer("Bone") == rep.iteration) | (Integer("Bone") < 0)
    
        node = cbone_distance(spline, nd.position, closed=closed).node
        d = node.distance
        weight = d.map_range(distance, distance + fall_off*distance, 1.0, 0.0)
        weight.switch_false(sel & node.is_valid, 0.0)
        
        change = Float("Bone Weight") < weight

        index = node.index
        is_first = index == 0
        is_last = index >= npoints-2
        prev_index = rep.total + (index - 1).floored_modulo(npoints)
        next_index = rep.total + (index + 1).floored_modulo(npoints)

        proj = node.proj
        
        rep.mesh.points[change].set("Bone Index",   rep.total + index)
        rep.mesh.points[change].set("Bone Proj",    proj)
        rep.mesh.points[change].set("Bone Has Prev", closed | is_first.bnot())
        rep.mesh.points[change].set("Bone Has Next", closed | is_last.bnot())
        rep.mesh.points[change].set("Bone Prev Index", prev_index)
        rep.mesh.points[change].set("Bone Next Index", next_index)
        rep.mesh.points[change].set("Bone Weight",  weight)

        rep.total += npoints

    mesh = rep.mesh

    mesh.points[selection.bnot()].set("Bone Weight", 0.0)
    
    mesh.out()
    
# ----------------------------------------------------------------------------------------------------
# Deform a mesh
# ----------------------------------------------------------------------------------------------------
    
@curve_bones.geo_modifier('Deform')
def cbone_deform():
    """# CBone Deform
    
    Deform a mesh
    """
    
    mesh = Mesh()
    curve = Curve(None, "Curve")
    blend = Float.Factor(0.5, "Blend", 0, 1)*0.5
    
    count = curve.points.count
    
    trf = curve.points.sample_index(Matrix("Transform"), index=Integer("Bone Index"))
    prev_trf = curve.points.sample_index(Matrix("Transform"), index=Integer("Bone Prev Index"))
    next_trf = curve.points.sample_index(Matrix("Transform"), index=Integer("Bone Next Index"))
    
    proj = Float("Bone Proj")
    
    fac1 = proj.map_range(0.0, 1.0, 0.0, 0.5)
    
    prev_pos = prev_trf @ nd.position
    new_pos = trf @ nd.position
    next_pos = next_trf @ nd.position
    
    fac0 = proj.map_range(0.0, blend, 0.5, 0.0)
    new_pos.switch(Boolean("Bone Has Prev") & (proj < blend), new_pos.mix(prev_pos, factor=fac0))
    
    fac1 = proj.map_range(1 - blend, 1.0, 0.0, 0.5)
    new_pos.switch(Boolean("Bone Has Next") & (proj > 1.0 - blend), new_pos.mix(next_pos, factor=fac1))
    
    mesh.points.position = Vector(Float("Bone Weight")).map_range(to_min=nd.position, to_max=new_pos)

    mesh.out()

# ====================================================================================================
# Curve Bone Demo
# ====================================================================================================

@curve_bones.geo_modifier('Demo')
def cbone_demo():
    """# CBone Demo
    
    Curve Bone Demo
    """

    rot = Rotation(None, "Initial Rotation")
    blend = Float.Factor(0.1, "Blend", 0, 1)
    
    rots = []
    for i in range(3):
        rots.append(Vector.Euler(None, f"Rotation {i}"))
    
    use_cubes = Boolean(False, "Show Joints")

    with Layout("Demo Mesh and Curve"):        
        cyl = new_cylinder(segments=16, rings=100, radius=0.1, depth=1, caps=True)
        cyl.transform(scale=(1, 0.7, 1))
        
        bone = Curve.Line((0, 0, -0.1), (0, 0, 1.1)).resample(count=4)

    with Layout("Start with an arbitrary orientation"):     
        cyl.position = rot @ nd.position
        bone.position = rot @ nd.position

    with Layout("Link Bone to Mesh and deform"):
        bone = cbone_new(bone)
        cyl = cbone_link(cyl, bone, distance=1)
    
        for i in range(3):
            bone = cbone_rotate(bone, index=i, rotation=rots[i])
        
        cyl = cbone_deform(cyl, bone, blend=blend)

    with Layout("Debug"):
        cubes = bone.instance_on_points(instance=Mesh.Cube(size=0.05))
        cubes.switch_false(use_cubes)
    
    (cyl + (bone, cubes)).out()

# ====================================================================================================
# Ordered Selection
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Ordered Selection length
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('Count')
def osel_count():
    """# OSel Count
    
    Ordered Selection length
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Selection Name")
    
    count = Mesh(mesh.points[Integer(sel_name) > 0].separate()).points.count
    
    count.out("Count")

# ----------------------------------------------------------------------------------------------------
# Ordered Selection Rename
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('Rename')
def osel_rename():
    """# OSel Rename
    
    Ordered Selection Rename
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    new_name = String("New Name", "New Name")
    use_remove = Boolean(True, "Remove")
    
    mesh.points.set(new_name, Integer(sel_name))
    rem = Mesh(mesh)
    rem.remove_named_attribute(name=sel_name)
    
    mesh.switch(use_remove,rem).out()


# ----------------------------------------------------------------------------------------------------
# Add selection
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('Add Selection')
def osel_add_selection():
    """# OSel Add Selection
    
    Add selection
    """
    
    mesh = Mesh()
    sel = Boolean(False, "Selection", hide_value=True)
    use_invert = Boolean(False, "Invert")
    sel_name = String("Selection", "Name")
    
    idx = Integer(sel_name)
    
    with Layout("Current Selection"):
        
        exists = mesh.points.sample_index(idx.exists, index=0)
        
        mesh.points[exists.bnot()].set(sel_name, 0)
        
        max_sel = mesh.points.attribute_statistic(Float(idx)).max_.to_integer()
        
    with Layout("Selection Order"):
        n = Mesh(Mesh(mesh).points[sel].separate()).points.count
        num = mesh.points.accumulate_field(Integer(sel)).leading
        mesh.points.set("tmp Sel", Integer.Switch(use_invert, num, n + 1 - num))
        
        mesh.points[sel].set(sel_name, max_sel + Integer("tmp Sel"))
        mesh.remove_named_attribute(name="tmp Sel")
        
    mesh.out()
    
# ----------------------------------------------------------------------------------------------------
# Merge another ordered selection
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('Append')
def osel_append():
    """# OSel Append
    
    Merge another ordered selection
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    other_name = String("Other", "Other Name")
    use_remove = Boolean(True, "Remove")
    
    count = osel_count(mesh, sel_name)
    
    other_idx = Integer(other_name)
    mesh.points[other_idx > 0].set(sel_name, count + other_idx)
    
    rem = Mesh(mesh)
    rem.remove_named_attribute(name=other_name)
    mesh.switch(use_remove, rem)
    
    mesh.out()

# ----------------------------------------------------------------------------------------------------
# Visualization
# ----------------------------------------------------------------------------------------------------
    
@ordered_selection.geo_modifier('Visualization')
def osel_visualization():
    """# OSel Visualization
    
    Visualization
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    size = Float(1.0, "Size")
    dist = Float(0.1, "Distance")
    ofs = Vector(0, "Offset")
    rot = Float.Angle(0, "Rotation")
    use_index = Boolean(False, "Index")
    
    for feel in mesh.points.for_each_element(pos = nd.position, normal=nd.normal, sel_num = Integer(sel_name)):
        idx = feel.sel_num.switch(use_index, feel.index)
        label = idx.to_string().to_curves(size=size).realize()
        label = Curve(label).fill()
        label.faces.material = "Colored Mat"
        label.faces.set('Color', Color("Black"))
        label.transform(rotation=(pi/2, 0, rot))
        
        pos1 =  feel.pos + feel.normal.scale(dist) + ofs
        
        label.offset = pos1
        label += Curve.Line(feel.pos, pos1)
        
        label.switch(feel.sel_num == 0)
        
        label.out()
        
    (mesh + feel.generated).out()
    
# ----------------------------------------------------------------------------------------------------
# Shift
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_modifier('Shift')
def osel_shift():
    """# OSel Shift
    
    Shift
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    shift = Integer(0, "Shift")
    
    idx = Integer(sel_name)
    sel = idx > 0
    
    count = Mesh(Mesh(mesh).points[sel].separate()).points.count
    
    mesh.points[sel].set(sel_name, (idx - 1 + shift).floored_modulo(count) + 1)
    
    mesh.out()
    
# ----------------------------------------------------------------------------------------------------
# Shift
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_modifier('Invert')
def osel_invert():
    """# OSel Invert
    
    Shift
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    use_invert = Boolean(True, "Invert")
    
    idx = Integer(sel_name)
    sel = idx > 0
    
    count = Mesh(Mesh(mesh).points[sel].separate()).points.count
    
    inverted = Mesh(mesh)
    
    inverted.points[sel].set(sel_name, count - idx + 1)
    
    mesh.switch(use_invert, inverted).out()
    
# ----------------------------------------------------------------------------------------------------
# Extract a sub ordered selection
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_modifier('Extract')
def osel_extract():
    """# OSel Extract
    
    Extract a sub ordered selection
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    use_invert = Boolean(False, "Invert")
    
    start = Integer(1, "Start", 1)
    count = Integer(1, "Count")
    x_name = String("", "Extraction Name")
    
    idx = Integer(sel_name)
    
    nsel = Mesh(Mesh(mesh).points[idx > 0].separate()).points.count
    
    new_idx = (idx - start).floored_modulo(nsel)
    
    sel = (idx > 0) & (new_idx < count)
    
    named = Mesh(mesh)
    named.points.set(x_name, new_idx + 1)
    inverted = Mesh(mesh)
    inverted.points.set(x_name, count - new_idx)
    named.switch(use_invert, inverted)
    
    named.points[sel.bnot()].set(x_name, 0)
    
    mesh.switch(x_name != "", named)
    
    mesh.out()
    sel.out()

# ----------------------------------------------------------------------------------------------------
# Extract Mesh
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('Get Line')
def osel_get_line():
    """# OSel Get Line
    
    Extract Mesh
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    
    pts = Mesh(mesh.points[Integer(sel_name) > 0].separate())
    
    pts.points.sort(sort_weight=Integer(sel_name))

    pts.out()
    
# ----------------------------------------------------------------------------------------------------
# Set position
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('Set Position')
def osel_set_position():
    """# OSel Set Position
    
    Set position
    """

    mesh = Mesh()
    sel_name = String("Selection", "Name")
    
    pts = Cloud(None, "Points")
    
    mesh[Integer(sel_name) > 0].position = pts.points.sample_index(nd.position, index=Integer(sel_name) - 1)
    
    mesh.out()
    
# ----------------------------------------------------------------------------------------------------
# Selection center and normal
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_modifier('Get Disk')
def osel_get_disk():
    """# OSel Get Disk
    
    Selection center and normal
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    
    sel = Integer(sel_name)>0
    
    center = mesh.points[sel].attribute_statistic(nd.position).mean
    
    line = osel_get_line(mesh, sel_name)
    
    disk = Mesh.Circle(fill_type="N-Gon", vertices=osel_count(mesh, sel_name))
    disk.position = line.points.sample_index(nd.position, index=nd.index)
    
    disk.out()
    center.out("Center")

# ----------------------------------------------------------------------------------------------------
# To Circle
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('To Circle')
def osel_to_circle():
    """# OSel To Circle
    
    To Circle
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    radius = Float(1.0, "Radius", 0)
    use_center = Boolean(True, "Default Center")
    center = Vector(0, "Center")
    factor = Float.Factor(1.0, "Factor", 0, 1)
    
    def_center = mesh.points[Integer(sel_name) > 0].attribute_statistic(nd.position).mean
    center.switch(use_center, def_center)

    new_pos = center + (nd.position - center).normalize().scale(radius)
    mesh[Integer(sel_name)>0].position = Vector(factor).map_range(to_min=nd.position, to_max=new_pos)

    mesh.out()
    
# ----------------------------------------------------------------------------------------------------
# Merge two selections
# ----------------------------------------------------------------------------------------------------

@ordered_selection.geo_group('Merge')
def osel_merge():
    """# OSel Merge
    
    Merge two selections
    """
    
    mesh = Mesh()
    sel_name = String("Selection", "Name")
    to_name = String("To", "To Selection")
    use_remove=Boolean(True, "Remove")
    
    line = osel_get_line(mesh, to_name)
    
    mesh = osel_set_position(mesh, sel_name, points=line)
    
    mesh.points.set("tmp Merge", Integer(sel_name))
    mesh.points[Integer(to_name)>0].set("tmp Merge", Integer(to_name))
    mesh = mesh.points[Integer("tmp Merge") > 0].merge(merge_id=Integer("tmp Merge"))
    
    mesh.remove_named_attribute(name="tmp Merge")

    rem = Mesh(mesh)
    rem.remove_named_attribute(name=sel_name)
    rem.remove_named_attribute(name=to_name)
    
    mesh.switch(use_remove, rem)
    
    mesh.out()
    
# ----------------------------------------------------------------------------------------------------
# Bridge between two ordered selection
# ----------------------------------------------------------------------------------------------------
    
@ordered_selection.geo_group('Bridge')
def osel_bridge():
    """# OSel Bridge
    
    Bridge between two ordered selection
    """
    
    mesh = Mesh()
    sel_name0 = String("Selection", "Name")
    sel_name1 = String("To", "To Name")
    resol = Integer(0, "Resolution", 0)
    closed = Boolean(False, "Closed")
    remove = Boolean(True, "Remove")
    bridge_name = String("", "Bridge Name")
    side_name = String("", "Side Name")
    
    use_flip = Boolean(False, "Flip")

    
    with Layout("Create the bridge"):

        line0 = osel_get_line(mesh, sel_name0)
        line1 = osel_get_line(mesh, sel_name1)
        
        nx = (resol + 2)._lc("nx")
        ny = line0.points.count._lc("ny")
        
        ny1 = line1.points.count
        
        ko = ny != ny1
        ko.warning("Selections don't have the same number of vertices: " + ny.to_string() + " and " + ny1.to_string())
        
        bridge = Mesh.Grid(vertices_x=nx, vertices_y=ny)
        line = Mesh.Line(count=nx)
        cyl = Mesh.Cylinder(vertices=ny, side_segments=nx-1, fill_type='None')
        
        bridge.switch(ny==1, line)
        bridge.switch(closed & (ny > 2), cyl)

        with Layout("Preserve integer attributes on boundaries"):
            names = mesh.points.get_attribute_names(Integer)
            boundary_row = nd.index // ny
            boundary_index = nd.index % ny
            for rep in repeat(names.list_length(), bridge=bridge):
                attr_name = names[rep.iteration]
                source_value = line0.points.sample_index(
                    Integer(attr_name), index=boundary_index)
                target_value = line1.points.sample_index(
                    Integer(attr_name), index=boundary_index)
                rep.bridge.points.set(attr_name, 0)
                rep.bridge.points[boundary_row == 0].set(attr_name, source_value)
                rep.bridge.points[boundary_row == nx-1].set(attr_name, target_value)
            bridge = Mesh(rep.bridge)

        # Bridge-specific attributes override the copied boundary values.
        bridge.set(sel_name0, 0)
        bridge.set(sel_name1, 0)
        
        named = Mesh(bridge)
        named.points.set(bridge_name, nd.index + 1)
        bridge.switch(bridge_name.length()>0, named)
        
    with Layout("Bridge points position"):
        
        i = (nd.index // ny)._lc("i")
        j = (nd.index % ny)._lc("j")
        
        p0 = line0.points.sample_index(nd.position, index=j)
        p1 = line1.points.sample_index(nd.position, index=j)
        
        fac = i/(nx - 1)
        
        bridge.position = p0.scale(1 - fac) + p1.scale(fac)
        flipped = Mesh(bridge)
        flipped.flip_faces()
        bridge.switch(use_flip, flipped)
        
    with Layout("Weld"):
        
        no_side = side_name.length()==0
        sideA = (side_name + " A").switch(no_side)
        sideB = (side_name + " B").switch(no_side)
        
        with Layout("Bridge Sides"):            
            bridge.points[i==0].set(sel_name0, j+1)
            bridge.points[i==nx-1].set(sel_name1, j+1)
            
            bridge.points[j==0].set(sideA, i+1)
            bridge.points[j==ny-1].set(sideB, nx - i)
            
        with Layout("Side extremities will be merged"):                
            mesh.points[Integer(sel_name0)==1].set(sideA, 1)
            mesh.points[Integer(sel_name0)==ny].set(sideB, resol + 2)
            
            mesh.points[Integer(sel_name1)==1].set(sideA, resol + 2)
            mesh.points[Integer(sel_name1)==ny].set(sideB, 1)

        with Layout("Bridge vertex indices"):
            # Match both copies of each boundary vertex before welding,
            # so merging preserves the bridge's 1-based numbering.
            named_mesh = Mesh(mesh)
            named_mesh.points.set(bridge_name, 0)
            source_index = Integer(sel_name0)
            target_index = Integer(sel_name1)
            named_mesh.points[source_index > 0].set(bridge_name, source_index)
            named_mesh.points[target_index > 0].set(
                bridge_name, (nx - 1)*ny + target_index)
            mesh.switch(bridge_name.length() > 0, named_mesh)
            
        with Layout("Weld"):                
            mesh += bridge

            idx = Integer(sel_name0)
            mesh.points[idx > 0].merge(merge_id=idx)
            
            idx = Integer(sel_name1)
            mesh.points[idx > 0].merge(merge_id=idx)

            rem = Mesh(mesh)
            rem.remove_named_attribute(name=sel_name0)
            rem.remove_named_attribute(name=sel_name1)

            mesh.switch(remove, rem)
        
    mesh.out()

# ====================================================================================================
# Split Hole
# ====================================================================================================

@ordered_selection.geo_group('Split Hole')
def osel_split_hole():
    """# OSel Split Hole
    
    Split Hole
    """
    
    mesh = Mesh()
    
    sel_name = String("Selection", "Name")
    
    count = Integer(1, "Count", 1)
    index0 = Integer(0, "Index 0", 0)
    index1 = Integer(0, "Index 1", 0)
    
    resol = Integer(0, "Resolution", 0)
    use_flip = Boolean(False, "Flip")
    
    nsel = osel_count(mesh, sel_name)
    
    with Layout("New loop A"):
        
        idx = Integer(sel_name) - 1
        shift = index1 + count - 1
        
        idx = (idx - shift).floored_modulo(nsel)
        idx_max = (index0 - 1 - shift).floored_modulo(nsel)
        
        mesh.points[(Integer(sel_name) > 0) & (idx < idx_max)].set("tmp Side A", resol + 3 + idx)
        
    with Layout("New loop B"):
        
        idx = Integer(sel_name) - 1
        shift = index0 + count - 1
        
        idx = (idx - shift).floored_modulo(nsel)
        idx_max = (index1 - 1 - shift).floored_modulo(nsel)
        
        mesh.points[(Integer(sel_name) > 0) & (idx < idx_max)].set("tmp Side B", resol + 3 + idx)
        
    with Layout("Build a bridge"):   
        mesh = osel_extract(mesh, sel_name, start=index0, count=count, invert=False, extraction_name="tmp A")
        mesh = osel_extract(mesh, sel_name, start=index1, count=count, invert=True,  extraction_name="tmp B")
        mesh = osel_bridge(mesh,
            name="tmp A", 
            to_name="tmp B", 
            flip=use_flip.bnot(),
            resolution=resol,
            side_name = "tmp Side",
            )
            
    with Layout("Rename Selections"):
        
        mesh.points.set(sel_name + " A", Integer("tmp Side A"))
        mesh.points.set(sel_name + " B", Integer("tmp Side B"))
        
        mesh.remove_named_attribute(name="tmp Side A")
        mesh.remove_named_attribute(name="tmp Side B")
        mesh.remove_named_attribute(name=sel_name)
        

    mesh.out()



def demo(rebuild=False):
    meshutil.build(rebuild=rebuild)
    curve_bones.build(rebuild=rebuild)
    ordered_selection.build(rebuild=rebuild)
