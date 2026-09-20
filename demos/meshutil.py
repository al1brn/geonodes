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

def demo():

    # ====================================================================================================
    # Curves
    # ====================================================================================================

    with GeoNodes("Cross Splines"):
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
    # Selection utilities
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Number selected vertices
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Number Selection", is_group=True):
        
        mesh = Mesh()
        selection = Boolean(name="Selection", hide_value=True)
        name = String("Number", name="Name", tip="Weld prefix is added automatically. IDs are 1..N; zero means no weld.")
        
        n = mesh.points.accumulate_field(value=Integer(selection)).leading
        
        weld_name = String("Weld ") + name
        mesh.points.set(weld_name, Integer.Switch(selection, 0, n))
        
        mesh.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Extract selected vertices
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes("Extract Selection", is_group=True):
        
        mesh = Mesh()
        selection = Boolean(name="Selection", hide_value=True)
        name = String("Number", name="Name", tip="Weld prefix is added automatically. IDs are 1..N; zero means no weld.")
        reversed = Boolean(False, "Reversed")

        mesh = G().number_selection(mesh, selection=selection, name=name)
        xmesh = Mesh(mesh.points[selection].separate())
        
        n = xmesh.points.count
        rev_mesh = Mesh(xmesh)
        rev_mesh.position = xmesh.points.sample_index(nd.position, index=n-1-nd.index)
        
        xmesh.switch(reversed, rev_mesh).out()
        
    # ----------------------------------------------------------------------------------------------------
    # Weld a selection
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes("Weld Selections", is_group=True):
        
        use_bridge = Boolean(False, "Bridge")
        use_merge = Boolean(True, "Merge")
        name = String("Selection", name="Weld Name", tip="Weld prefix is added automatically. Merge only positive IDs.")
        weld_name = String("Weld ") + name
        
        mesh1 = Mesh(name="Weld")
        sel1 = Boolean(name="Selection", hide_value=True)
        mesh2 = Mesh(name="To Mesh")
        sel2 = Boolean(name="Selection", hide_value=True)
        use_reversed = Boolean(False, "Reversed")
        
        mesh1 = G().number_selection(mesh1, selection=sel1, name=name)
        mesh2 = G().number_selection(mesh2, selection=sel2, name=name)
        
        target = G().extract_selection(mesh2, selection=sel2, name=name, reversed=use_reversed)
        
        with Layout("Move Selection 1"):
            moved = Mesh(mesh1)    
            moved[sel1].position = target.points.sample_index(nd.position, index=nd.named_attribute(name=weld_name, data_type='INT')-1)
            
        with Layout("Bridge"):
            bridged = Mesh(mesh1)
            edge_sel = bridged.points.evaluate_on_domain(sel1)
            bridged = bridged.edges[edge_sel].extrude()
            top = bridged.top
            sel1 = bridged.edges.evaluate_on_domain(top)
            bridged = G().number_selection(bridged, selection=sel1, name=name)
            bridged[sel1].position = target.points.sample_index(nd.position, index=nd.named_attribute(name=weld_name, data_type='INT')-1)
            
        mesh1 = Mesh(Mesh.Switch(use_bridge, moved, bridged))

        with Layout("Match Weld IDs"):
            # Positions have already been sampled in the requested order.
            # Match each moved vertex to the original ID on the target mesh.
            weld_id = nd.named_attribute(name=weld_name, data_type='INT')
            merge_id = Integer.Switch(use_reversed, weld_id, target.points.count+1-weld_id)
            mesh1.points[weld_id > 0].set(weld_name, merge_id)
        
        with Layout("Optional Merge"):
            merged = Mesh(mesh1 + mesh2)
            wid = nd.named_attribute(name=weld_name, data_type='INT')
            merged.points[wid > 0].merge(merge_id=wid)
            # The unmerged branch never joins the meshes, preserving indices.
            mesh1.switch(use_merge, merged).out("Mesh")
            mesh2.out("To Mesh")

    # ----------------------------------------------------------------------------------------------------
    # Patch a grid between two selections
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Patch with a Grid"):

        mesh = Mesh()
        use_merge = Boolean(True, "Merge")
        name = String("Patch", name="Name",
                      tip="Names the four Weld <name> Front/Side 1/2 attributes. Zero means no weld; positive values identify border vertices.")
        sel0 = Boolean(name="Selection 1", hide_value=True)
        sel1 = Boolean(name="Selection 2", hide_value=True)
        use_reversed = Boolean(False, "Reversed")
        subdivisions = Integer(0, "Subdivisions", 0,
                               tip="Number of intermediate rows between the two selections.")
        use_flip = Boolean(False, "Flip Faces")
        original = Mesh(mesh)

        with Layout("Weld Names"):
            front0 = String("Weld ") + name + " Front 1"
            front1 = String("Weld ") + name + " Front 2"
            side0 = String("Weld ") + name + " Side 1"
            side1 = String("Weld ") + name + " Side 2"

        with Layout("Front IDs"):
            n0 = mesh.points.accumulate_field(value=Integer(sel0)).leading
            n1 = mesh.points.accumulate_field(value=Integer(sel1)).leading
            mesh.points.set(front0, Integer.Switch(sel0, 0, n0))
            mesh.points.set(front1, Integer.Switch(sel1, 0, n1))

        with Layout("Prepare Selections"):
            pts0 = Mesh(Mesh(mesh).points[sel0].separate())
            pts1 = Mesh(Mesh(mesh).points[sel1].separate())
            count0 = pts0.points.count
            count1 = pts1.points.count
            valid = (count0 == count1) & (count0 >= 2)
            (count0 != count1).warning("Selections must contain the same number of vertices; no patch created.")
            (count0 < 2).warning("A patch needs at least two vertices on each side; no patch created.")
            width = Integer(gnmath.max(count0, 2))
            rows = Integer(gnmath.max(subdivisions, 0)+2)

        with Layout("Source Corners"):
            # Copy the side IDs onto the matching source corners as well:
            # otherwise merging a front would average them with zero.
            f0 = nd.named_attribute(name=front0, data_type='INT')
            f1 = nd.named_attribute(name=front1, data_type='INT')
            first1 = Integer.Switch(use_reversed, 1, count1)
            last1 = Integer.Switch(use_reversed, count1, 1)
            mesh.points.set(side0, Integer(0).switch(f0 == 1, 1).switch(f1 == first1, rows))
            mesh.points.set(side1, Integer(0).switch(f0 == count0, 1).switch(f1 == last1, rows))

        with Layout("Grid"):
            grid = Mesh.Grid(vertices_x=width, vertices_y=rows)
            # Derive coordinates from the primitive positions, independent of
            # Blender's internal grid vertex ordering.
            column = Integer(((nd.position.x + .5)*(width-1)).round())
            row = Integer(((nd.position.y + .5)*(rows-1)).round())
            target_index = Integer.Switch(use_reversed, column, count1-1-column)
            p0 = pts0.points.sample_index(nd.position, index=column)
            p1 = pts1.points.sample_index(nd.position, index=target_index)
            grid.points.set(front0, Integer.Switch(row == 0, 0, column+1))
            grid.points.set(front1, Integer.Switch(row == rows-1, 0, target_index+1))
            grid.points.set(side0, Integer.Switch(column == 0, 0, row+1))
            grid.points.set(side1, Integer.Switch(column == width-1, 0, row+1))
            grid.points.position = p0.mix(p1, factor=Float(row)/(rows-1))
            grid[use_flip].flip_faces()

        with Layout("Optional Merge and Outputs"):
            merged = Mesh(mesh + grid)
            for front in (front0, front1):
                merge_id = nd.named_attribute(name=front, data_type='INT')
                merged.points[merge_id > 0].merge(merge_id=merge_id)
            # Without a merge the input topology and the patch stay separate.
            mesh.switch(use_merge, merged)
            original.switch(valid, mesh).out("Mesh")
            grid.out("Patch")

    # ----------------------------------------------------------------------------------------------------
    # Weld mesh pieces
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Weld Mesh Pieces", is_group=True):
        mesh = Mesh()
        names = mesh.points.get_attribute_names()
        for rep in repeat(names.list_length(), mesh=mesh):
            name = names[rep.iteration]
            ok = name.match_string(operation='Starts With', key="Weld ")

            wid = Attribute(name, Integer).value
            welded = Mesh(rep.mesh)[wid > 0].merge_points(merge_id=wid)

            rep.mesh.switch(ok, welded)

        mesh = rep.mesh
        mesh.remove_named_attribute(pattern_mode='Wildcard', name='Weld *')
        mesh.out()

    # ====================================================================================================
    # Curves
    # ====================================================================================================

    with GeoNodes("Subdivide Segment", is_group=True):

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

    with GeoNodes("New Cylinder", is_group=True):

        nrings = Integer(2, "Rings", 2, 100)
        nsegms = Integer(12, "Segments", 3, 128)
            
        new_cyl = Mesh.Cylinder(side_segments=nrings-1, vertices=nsegms, fill_type="N-Gon")
        nz = nd.normal.z
        new_cyl.faces.set("Cap", Integer.Switch(nz > 0.9, Integer.Switch(nz < -0.9, 0, -1), 1))
        new_cyl.transform(rotation=(0, pi, 0))
        new_cyl = set_cylinder_topology(new_cyl, nrings, nsegms)

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
                    new_cyl = G().new_cylinder(rings=nrings, segments=nsegms)
                    cyl.switch(create, new_cyl)

            nrings, nsegms = get_cylinder_topology(cyl)
        
        return cyl, nrings, nsegms

    # ----------------------------------------------------------------------------------------------------
    # Zone selection in a cylinder
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Cylinder Selection", is_group=True):
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
        node_set = G().cylinder_selection(cyl, ...).node
        node_get = G().cylinder_selection(model, ranged=node_set.ranged, ...).node
        
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

    with GeoNodes("Cylinder Copy Position", is_group=True):

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

        sel = G().cylinder_selection(
            cyl,
            ring_index=ring_index,
            ring_count=ring_count,
            col_index=col_index,
            col_count=col_count,
        )
        model_sel = G().cylinder_selection(
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

    with GeoNodes("View Cylinder Indices", is_group=True):

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

        sel = G().cylinder_selection(cyl, ring_index=ring_index)
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

    with GeoNodes("Add Rings to Cylinder", is_group=True):

        cyl, nrings, nsegms = get_cylinder(use_create=False)

        count = Integer(1, "Count", 0)
        below = Boolean(False, "Below")

        new_cyl = G().new_cylinder(rings=nrings + count, segments=nsegms)

        node = G().cylinder_selection(new_cyl, 
                        ring_index=Integer(count).switch_false(below, 0),
                        ring_count=nrings)

        ranged = nd.index - Integer.Switch(below, 0, count*nsegms)
        new_cyl[node.selection].position = cyl.points.sample_index(nd.position, index=ranged)

        new_cyl.switch(count < 1, cyl).out()

    # ----------------------------------------------------------------------------------------------------
    # Dome Cylinder
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Close Cylinder", is_group=True):

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
            new_cyl = G().add_rings_to_cylinder(cyl, count=count, below=True)
            ok = use_append & use_bot
            cyl.switch(ok, new_cyl)
            nrings.switch(ok, nrings + count)

            new_cyl = G().add_rings_to_cylinder(cyl, count=count, below=False)
            ok = use_append & use_top
            cyl.switch(ok, new_cyl)
            nrings.switch(ok, nrings + count)

        for bot_cap in (True, False):
            with Layout("Bottom Cap" if bot_cap else "Top Cap"):

                i_ring = count if bot_cap else nrings - 1 - count

                sel = G().cylinder_selection(cyl, ring_index=i_ring)
                center = cyl.points[sel].attribute_statistic(nd.position)

                sel0 = G().cylinder_selection(cyl, ring_index=i_ring + 1 if bot_cap else i_ring - 1)
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
                    c = G().cylinder_copy_position(rep.cyl, ring_index=ir, model=cyl, from_ring_index=i_ring)

                    sel = G().cylinder_selection(c, ring_index=ir)
                    c[sel].position = center + direc.scale(sy) + (nd.position - center).scale(sx)
                    c[sel].set('Weld TOP', Integer.Switch(last_iteration, 0, 1 if bot_cap else 2))

                    rep.cyl = c

                cyl.switch(use_bot if bot_cap else use_top, rep.cyl)

        original.switch(valid, cyl).out()

    # ----------------------------------------------------------------------------------------------------
    # Weld Cylinders
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Weld Cylinders", is_group=True):

        use_debug = Boolean(False, "Debug")
        use_bridge = Boolean(False, "Bridge")

        with Panel("Weld"):
            w_cyl, w_nrings, w_nsegms = get_cylinder(use_create=False, name="Weld")
            w_index = Integer(0, "Index", 1)
            unchanged = Curve(w_cyl)

        with Panel("On top"):
            t_cyl, t_nrings, t_nsegms = get_cylinder(use_create=False, name="To Mesh")
            t_index = Integer(0, "Index", 1)
            unchanged += t_cyl

        count = Integer(32, "Count", 0)

        with Layout("Prepare Selections"):
            count = gnmath.min(count, gnmath.min(w_nsegms, t_nsegms))
            w_node = G().cylinder_selection(w_cyl, ring_index=0,
                                      col_index=w_index, col_count=count)
            t_node = G().cylinder_selection(t_cyl, ring_index=t_nrings-1,
                                      col_index=t_index, col_count=count)
            w_selection = w_node.selection & (count > 0)
            t_selection = t_node.selection & (count > 0)

            # Number Selection follows vertex order. Preserve the requested
            # cyclic order, including zones crossing the end of a ring.
            w_cyl.points[w_selection].sort(sort_weight=w_node.ranged)
            t_cyl.points[t_selection].sort(sort_weight=t_node.ranged)

        with Layout("Weld Selections"):
            weld = G().weld_selections(bridge=use_bridge, weld=w_cyl, to_mesh=t_cyl).node
            weld["Selection"] = w_selection
            weld["Selection_1"] = t_selection
            result = weld._out

        result.switch(use_debug, unchanged).out()

    # ----------------------------------------------------------------------------------------------------
    # Cylinder enveloppe
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Bones Envelope"):
        
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
            
            crossed = G().cross_splines(curve)
            
            interp = Curve(crossed)
            interp.splines.type = 'Bezier'
            interp.handle_type = 'Auto'
            interp.resample(count=interp_resol)
            
            crossed.switch(use_interpolate, interp)
            
            bones = Curve(Geometry.Switch(use_cross, G().cross_splines(crossed), crossed))
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
                rounded[sel].normal = nrm
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
                rounded[sel].normal = nrm
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
            cyl = G().new_cylinder(rings=nrings, segments=nsegms)

            i_ring  = nd.index // nsegms
            i_point = nd.index % nsegms

            idx = i_ring*npoints + i_point
            cyl[i_point < npoints].position  = side0.points.sample_index(nd.position, index=idx)
            
            idx = (i_ring + 2)*npoints - 1 - i_point
            cyl[i_point >= npoints].position = side1.points.sample_index(nd.position, index=idx)
            cyl[(i_point % npoints) >= npoints].position = 0
            
        with Layout("Closing & Finalize"):
            
            cyl = G().close_cylinder(cyl, append=True).link_inputs(from_panel="Caps")
            
            # Need to flip ;-)
            cyl.flip_faces()
            
            cyl.subdivide(nsubdiv)
            
            cyl.faces.shade_smooth = use_smooth
            
        
        cyl.out()

    # ====================================================================================================
    # Rounded Joint
    # ====================================================================================================

    with GeoNodes("Rounded Joint", is_group=True):
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

    # Append a vertex to an open polyline.
    with GeoNodes("Build Poly Line"):
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

    # ====================================================================================================
    # Rounded angles
    # ====================================================================================================

    # Round every interior corner, retaining the ends and the spline structure.
    with GeoNodes("Round Joints"):
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
    with GeoNodes("Surrounding Shape"):
        
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

    with GeoNodes("Cage Around Bones"):
        
        curve = Curve()
        bone_resol = Integer(6, "Segments Resolution", 2, 128)
        ring_resol = Integer(12, "Rings Resolution", 12, 128)
        
        width = Float(1.0, "Width", 0)
        inflate = Float(1.0, "Inflate", 1.0)
        
        curve.resample(count=bone_resol)
        nsplines = curve.splines.count

        cyl = G().new_cylinder(rings=bone_resol, segments=ring_resol)
        bones = Curve.Line().resample(count=nsplines)
        
        for rep in repeat(bone_resol, cyl=cyl):
            
            idx = rep.iteration
            bones.points.position = curve.points.sample_index(nd.position, index=nd.index*bone_resol + idx)
            
            shape = G().surrounding_shape(bones, resolution=ring_resol, width=width, inflate=inflate)

            sel_node = G().cylinder_selection(rep.cyl, ring_index=rep.iteration).node
            rep.cyl.points[sel_node.selection].position = shape.points.sample_index(nd.position, index=sel_node.ranged)
            
        cage = Mesh(rep.cyl)
        
        cage.faces.shade_smooth = False
        
        cage.out()

        raise Break()        




        
        cyl = Mesh.Cylinder(side_segments=bone_resol-1, vertices=ring_resol).transform(rotation=Rotation((0, pi, 0)))
        i_ring = nd.index // ring_resol
        
        bones = Curve.Line().resample(count=nsplines)
        
        for rep in repeat(bone_resol, cyl=cyl):
            
            idx = rep.iteration
            bones.points.position = curve.points.sample_index(nd.position, index=nd.index*bone_resol + idx)
            
            shape = G().surrounding_shape(bones, resolution=ring_resol, width=width, inflate=inflate)
            
            rep.cyl.points[i_ring==idx].position = shape.points.sample_index(nd.position, index=nd.index%ring_resol)
            
        cage = Mesh(rep.cyl)
        
        cage.faces.shade_smooth = False
        
        cage.out()
