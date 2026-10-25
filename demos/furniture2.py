from geonodes import *

def demo(rebuild=True):
    
    RES_SIG = {"Plank Name": String, "Width": Float, "Length": Float, "Thickness": Float, "Material": Material, "Color": Color}
    BLOCK_SIG = {
        "ID": Integer,
        "Location": Vector, 
        "Size": Vector, 
        "Inner Location": Vector,
        "Inner Size": Vector,
        "Cuts": Bundle,
        }
    CUT_SIG = {"Plank Name": String, "Count": Integer, "Size": Vector, "Orient": Integer}
    
    LEFT = 0
    RIGHT = 1
    BOT = 2
    TOP = 3
    BACK = 4
    FRONT = 5
    
    SIDE_NAMES = ["Left", "Right", "Bottom", "Top", "Back", "Front"]
    
    CORNER_TL = 0
    CORNER_TR = 1
    CORNER_BL = 2
    CORNER_BR = 3
    
    CORNER_NAMES = ["Top Left", "Top Right", "Bot Left", "Bot Right"]
    
    JOIN_OVERLAY = 0
    JOIN_INSET = 1
    JOIN_MITERED = 2
    
    JOIN_NAMES = ["Overlay", "Inset", "Mitered"]
    JOIN_MENU = {name: i for i, name in enumerate(JOIN_NAMES)}
    
    SIDE_NONE = 0
    SIDE_INT = 1
    SIDE_MID = 2
    SIDE_EXT = 3
    
    SIDE_MENU = {"None": 0, "Int": 1, "Mid": 2, "Ext": 3} 
    
    ORIENT_MENU = {"Normal": 0, "Transverse": 1} 
    
    # ====================================================================================================
    # Seed
    # ====================================================================================================
    
    def new_seed(bundle):
        with Layout("Seed"):
            seed = bundle.get_item("Seed", socket_type='INTEGER')
            seed.switch_false(seed.exists, 0)
            seed += 1
            bundle.set_item("Seed", seed)

        return bundle, seed

    def new_block_id(bundle):
        with Layout("Block ID"):
            block_id = bundle.get_item("Block ID", socket_type='INTEGER')
            block_id.switch_false(block_id.exists, 1)
            block_id += 1
            bundle.set_item("Block ID", block_id)

        return bundle, block_id
    
    # ====================================================================================================
    # Named Dimensions
    # ====================================================================================================
    
    # ----------------------------------------------------------------------------------------------------
    # Define 5 named dimensions
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Define Named Dimensions", rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()

        for i in range(5):
            dimension_name = String("ABCDE"[i], "Name")
            value = Float.Distance(0.0, "Value", shape="Single")
            bundle.set_item("Names/" + dimension_name, value)

        nd.set_geometry_bundle(bundle=bundle).out()

    # ----------------------------------------------------------------------------------------------------
    # Get a named dimension
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes("Get Named Dimension", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()
        
        dimension_name = String("Dimension", "Name")
        
        value = bundle.get_item("Names/" + dimension_name, socket_type='FLOAT')
        
        value.out("Value")    
    
    
    # ====================================================================================================
    # Resource Management
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Resource Definition
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Define Resource", rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()

        new_name = String("Plank", "New Name")
        
        width = Float.Distance(0.35, "Width", 0.1, 3.0)
        length = Float.Distance(3.0, "Length", 0.1, 3.0)
        thickness = Float.Distance(0.018, "Thickness", 0.001, 0.2)
        mat = Material("Wood", "Material")
        col = Color("Blue", "Color")

        res_bundle = Bundle.Combine({
            "Plank Name" : new_name,
            "Width": width,
            "Length" : length,
            "Thickness" : thickness,
            "Material" : mat,
            "Color" : col,
        })

        bundle.set_item("Resources/" + new_name, res_bundle)
        nd.set_geometry_bundle(bundle=bundle).out()

    # ----------------------------------------------------------------------------------------------------
    # Get resource
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Get Resource", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        plank_name = String("Plank", "Plank Name")

        with Layout("Default Resources"):
            plank_def = Bundle.Combine({
                "Plank Name" : "Plank",
                "Width": 0.6,
                "Length" : 2.5,
                "Thickness" : 0.018,
                "Material" : Material("Wood"),
                "Color" : Color("Blue"),
            })
            shelf_def = Bundle.Combine({
                "Plank Name" : "Shelf",
                "Width": 0.6,
                "Length" : 2.5,
                "Thickness" : 0.012,
                "Material" : Material("Wood"),
                "Color" : Color("Blue"),
            })
        
        bundle = geo.get_bundle()
        res_bundle = bundle.get_item("Resources/" + plank_name, socket_type="BUNDLE")

        ko = res_bundle.exists.bnot()

        is_plank = plank_name.equal("Plank")
        res_bundle.switch(ko & is_plank, plank_def)
        ko.switch(is_plank)

        is_shelf = plank_name.equal("Shelf")
        res_bundle.switch(ko & is_shelf, shelf_def)
        ko.switch(is_shelf)

        ko.warning("Resource '" + plank_name + "' not found")

        node = res_bundle.separate(signature=RES_SIG)
        node.out()

    # ----------------------------------------------------------------------------------------------------
    # Capture resources from another object
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Capture Resources", rebuild=rebuild):

        geo = Geometry()

        source = Object(name="Object")
        source_bundle = source.info().geometry.get_bundle()
        bundle = geo.get_bundle()
        resources = bundle.get_item("Resources", socket_type='BUNDLE')
        source_resources = source_bundle.get_item("Resources", socket_type='BUNDLE')

        # Join keeps the first bundle's value when resource names collide.
        bundle.set_item("Resources", resources + source_resources)

        nd.set_geometry_bundle(bundle=bundle).out()
        
    # ====================================================================================================
    # Create Plank From Resource
    # ====================================================================================================

    def add_cut_sheet(bundle, block_name, cut_bundle):

        with Layout("Add Cut Sheet"):

            cut_node = cut_bundle.separate(signature=CUT_SIG)
            ok = cut_node.count > 0

            cuts_path = String.Join("Blocks", block_name, "Cuts", cut_node.plank_name, delimiter="/")
            cuts = bundle.get_item(cuts_path, socket_type="BUNDLE", structure_type="LIST")
            cuts.switch_false(cuts.exists)

            cuts.list_append(cut_bundle)
            new_bundle = Bundle(bundle)
            new_bundle.set_item(cuts_path, cuts)

            bundle.switch(ok, new_bundle)

            return bundle
    
    # ----------------------------------------------------------------------------------------------------
    # Create a Single Plank
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Create Plank", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        
        res_node = G().get_resource(geo).link_inputs().node
        width = Float.Distance(0.3, "Width", 0.1, 3)
        length = Float.Distance(1.0, "Length", 0.1, 3)
        setup = Integer.MenuSwitch({
            "Shelf": 0,
            "Flank": 1,
            "Face": 2,
            }, menu=Input("Setup", optional_label=True, expanded=True))
        orient = Boolean.MenuSwitch({"Normal": False, "Rotate": True}, menu=Input("Orientation", optional_label=True, expanded=True))
        
        with Layout("Create Plank"):
            size = Vector((length, width, res_node.thickness))
            size.switch(orient, (width, length, res_node.thickness))
            plank = Mesh.Cube(size=size)
            
            plank.corners.store_uv("UV Map", plank.points.evaluate_on_domain(nd.position))
            
            plank.faces.material = res_node.material
            plank.faces.set("Color", res_node.color)

        with Layout("Orientation"):
            
            rot_index = setup
            rot_index.switch(orient, setup + 3)
            
            rot=Rotation.IndexSwitch(
                (0, 0, pi/2),
                (0, pi/2, pi/2),
                (0, pi/2, 0),
                (0, 0, 0),
                (pi/2, 0, 0),
                (0, pi/2, 0),
                index = rot_index)

            plank.transform(rotation=rot)
            plank.switch(rot_index==5, Mesh(plank).transform(rotation=(pi/2, 0, 0)))
                
            node = plank.points.attribute_statistic(nd.position).node
            size = node.max - node.min
            
            plank.offset = size.scale(0.5)

        with Layout("Cut Sheet"):
            cut_bundle = Bundle.Combine({
                "Plank Name": res_node.plank_name,
                "Count" : 1,
                "Size" : size,
                "Orient" : Integer.Switch(orient, 0, 1),
            })
            plank.set_bundle(cut_bundle)
            
        plank.out()
        size.out("Size")
        
    # ----------------------------------------------------------------------------------------------------
    # Create an array of planks
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Create Faces", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        
        width = Float.Distance(0.3, "Width", 0.1, 3)
        length = Float.Distance(1.0, "Length", 0.1, 3)
        
        count_y = Integer(1, "Count Y", 1)
        count_z = Integer(1, "Count Z", 1)
        
        margin = Float.Distance(0.005, "Margin", 0)
        
        my = margin*(count_y-1)
        mz = margin*(count_z-1)
        
        wy = (width - my)/count_y
        lz = (length - mz)/count_z
        
        plank = G().create_plank(geo, width=wy, length=lz, setup='Face').link_inputs()
        cut_bundle = plank.get_bundle(remove=True)
        cut_bundle.set_item("Count", count_y*count_z)
        
        ofsy = (0, wy + margin, 0)
        ofsz = (0, 0, lz + margin)
        
        planks = G().array(plank, count=count_y, offset_method="Offset", translation=ofsy)
        planks = G().array(planks, count=count_z, offset_method="Offset", translation=ofsz)

        planks.set_bundle(cut_bundle)
        
        planks.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Create an array of shelves
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Create Shelves", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        
        height = Float.Distance(1.0, "Height")
        z = Float.Distance(0.1, "Z")
        count = Integer(1, "Count", 0)
        
        width = Float.Distance(0.45, "Width", 0.1, 3)
        depth = Float.Distance(0.28, "Depth", 0.1, 3)
        backset = Float.Distance(0.01, "Backset", 0, 0.1)
        
        plank = G().create_plank(geo, width=depth - backset, length=width, setup='Shelf').link_inputs()
        thick = plank.size.z

        with Layout("Single Shelf"):
            single = Mesh(plank)
            single.offset = (0, 0, z)

        with Layout("Several Shelves"):
            cut_bundle = plank.get_bundle(remove=True)
            cut_bundle.set_item("Count", count)
            
            height_int = height - thick*count
            
            dist = height_int/(count + 1)
            
            plank.offset = (0, 0, dist)
            shelves = G().array(plank, count=count, offset_method="Offset", translation=(0, 0, dist + thick))
            
            shelves.switch(count==0)
            shelves.set_bundle(cut_bundle)

        shelves.switch(count==1, single).out()
        
    # ====================================================================================================
    # Get Block properties
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # All properties
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Get Block Properties", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        block_name = String("Block", "Block Name")
        
        bundle = geo.get_bundle().get_item("Blocks/" + block_name, socket_type='BUNDLE')
        nope = bundle.exists.bnot()

        nope.warning("Block '" + block_name + "' not found.")

        node = bundle.separate(signature=BLOCK_SIG)

        block_id = node.id.switch(nope)
        location = node.location.switch(nope)
        size = node.size.switch(nope)
        in_loc = node.inner_location.switch(nope)
        in_size = node.inner_size.switch(nope)
        cuts = node.cuts.switch(nope)

        block_name.switch(nope).out("Block Name")
        block_id.out("ID")
        location.out("Location")
        size.out("Size")
        in_loc.out("Inner Location")
        in_size.out("Inner Size")
        cuts.out("Cuts")

        x, y, z = location.xyz
        sx, sy, sz = size.xyz

        x.out("X0")
        y.out("Y0")
        z.out("Z0")

        (x + sx).out("X1")
        (y + sy).out("Y1")
        (z + sz).out("Z1")

        sx.out("Size X")
        sy.out("Size Y")
        sz.out("Size Z")

        (x + sx/2).out("X Center")
        (y + sy/2).out("Y Center")
        (z + sz/2).out("Z Center")

    # ----------------------------------------------------------------------------------------------------
    # Single Property
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Get Block Property", is_group=True, rebuild=rebuild):
        
        geo = Geometry()

        node = G().get_block_properties(geo).link_inputs().node
        
        value = Float.MenuSwitch({
            "X0": node.x0, "Y0": node.y0, "Z0" : node.z0,
            "X1": node.x1, "Y1": node.y1, "Z1" : node.z1,
            "Size X": node.size_x, "Size Y": node.size_y, "Size Z" : node.size_z,
            "X Center": node.x_center, "Y Center": node.y_center, "Z Center" : node.z_center,
        }, menu=Input("Property"))
        
        value.out("Value")

    # ----------------------------------------------------------------------------------------------------
    # Get UI Location input
    # ----------------------------------------------------------------------------------------------------

    def ui_location_value():
        index = Integer.MenuSwitch(
            {"Value": 0, "Block": 1, "Name": 2}, 
            menu=Input("Def", optional_label=True, expanded=True))
            
        block_name = String("Block", "Block Name")
        prop = G().get_block_property(geo, block_name=block_name, property=Input("Prop"))
        
        named = G().get_named_dimension(geo, name=Input("Name"))
        offset = Float.Distance(0, "Offset")

        value = Float.IndexSwitch(
            0,
            prop,
            named,
            index=index,
        )
        return value + offset

    # ----------------------------------------------------------------------------------------------------
    # Get a location input
    # ----------------------------------------------------------------------------------------------------
        
    def get_location(geo, name):
        with Panel(name, create_layout=True):
            return ui_location_value()

    # ----------------------------------------------------------------------------------------------------
    # Get a dimension input
    # ----------------------------------------------------------------------------------------------------

    def get_dimension(geo, name, base):
        with Panel(name, create_layout=True):
            rel_incr = Boolean.MenuSwitch(
                {"Dimension": False, "Target": True}, 
                menu=Input("Mode", optional_label=True, expanded=True))

            value = ui_location_value()
            value.switch(rel_incr, value - base)

            return value

    # ====================================================================================================
    # Define Blocks
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Base Creation
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Define Block", rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()
        
        show_frame = Boolean(False, "Show Frame")
        new_name = String("Block", "New Name")
        
        x = get_location(geo, "X")
        y = get_location(geo, "Y")
        z = get_location(geo, "Z")
            
        sx = get_dimension(geo, "Size X", x)
        sy = get_dimension(geo, "Size Y", y)
        sz = get_dimension(geo, "Size Z", z)
            
        with Layout("Create Bundle Entry"):
            location = Vector((x, y, z))
            size = Vector((sx, sy, sz))

            bundle, block_id = new_block_id(bundle)
            block_bundle = Bundle.Combine({
                "ID": block_id, 
                "Location": location, 
                "Size": size,
                "Inner Location" : location,
                "Inner Size" : size,
                "Cuts": Bundle()})
            
        with Layout("Frame"):
            block_frame = Mesh.Cube(size=(sx, sy, sz))
            block_frame.offset = size.scale(0.5) + location
            block_frame.faces.delete('Only Faces')
            block_frame.switch_false(show_frame)

        with Layout("Finalize"):

            bundle.set_item("Blocks/" + new_name, block_bundle)
            geo += block_frame

            geo.set_bundle(bundle)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Sub block
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Create Sub Block"):

        geo = Geometry()

        show_frame = Boolean(True, "Show Frame")
        new_name = String("Block", "New Name")

        parent_name = String("Parent", "Parent Name")
        loc_type = Integer.MenuSwitch({
            "Column" : 0,
            "Row" : 1,
        }, menu=Input("Type", optional_label=True, expanded=True))

        parent_node = G().get_block_properties(geo, block_name=parent_name).node

        y = Float.Distance(0.0, "Y", 0).clamp(parent_node.y0, parent_node.y1 - 0.1)
        sy = Float.Distance(1.0, "Width", 0.1).clamp(0.1, parent_node.y1 - y)

        z = Float.Distance(0.0, "Z", 0).clamp(parent_node.z0, parent_node.z1 - 0.1)
        sz = Float.Distance(1.0, "Height", 0.1).clamp(0.1, parent_node.z1 - z)

        col_geo = G().define_block(
            geo,
            new_name = new_name,
            show_frame=show_frame,

            x_offset = parent_node.x0,
            y_offset = parent_node.y0,
            z_offset = parent_node.z0 + z,

            size_x_offset = parent_node.size_x,
            size_y_offset = parent_node.size_y,
            size_z_offset = sz,
        )

        row_geo = G().define_block(
            geo,
            new_name = new_name,
            show_frame=show_frame,

            x_offset = parent_node.x0,
            y_offset = parent_node.y0 + y,
            z_offset = parent_node.z0,

            size_x_offset = parent_node.size_x,
            size_y_offset = sy,
            size_z_offset = parent_node.size_z,
        )

        Geometry.IndexSwitch(col_geo, row_geo, index=loc_type).out()

    # ----------------------------------------------------------------------------------------------------
    # Sub block
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Duplicate Block"):

        geo = Geometry()

        show_frame = Boolean(True, "Show Frame")
        new_name = String("Block", "New Name")

        source_name = String("Source", "Source Name")
        use_dupl_planks = Boolean(False, "Planks")

        sym_index = Integer.MenuSwitch(
            {"No" : 0, "Y": 1, "Z": 2},
            menu = Input("Symmetry", optional_label=True, expanded=True))

        ys = Float.Distance(0.0, "Y Center")
        zs = Float.Distance(0.0, "Z Center")

        source_node = G().get_block_properties(geo, block_name=source_name).node

        translated_geo = G().define_block(
            geo,
            new_name = new_name,
            show_frame=show_frame,

            size_x_offset = source_node.size_x,
            size_y_offset = source_node.size_y,
            size_z_offset = source_node.size_z,
        ).link_inputs(include=["X", "Y", "Z"])

        y_geo = G().define_block(
            geo,
            new_name = new_name,
            show_frame=show_frame,

            x_offset = source_node.x0,
            y_offset = ys - source_node.y1,
            z_offset = source_node.z0,

            size_x_offset = source_node.size_x,
            size_y_offset = source_node.size_y,
            size_z_offset = source_node.size_z,
        )

        z_geo = G().define_block(
            geo,
            new_name = new_name,
            show_frame=show_frame,

            x_offset = source_node.x0,
            y_offset = source_node.y0,
            z_offset = zs - source_node.z1,

            size_x_offset = source_node.size_x,
            size_y_offset = source_node.size_y,
            size_z_offset = source_node.size_z,
        )

        geo = Geometry.IndexSwitch(translated_geo, y_geo, z_geo, index=sym_index)

        dupl_geo = Geometry(geo)

        with Layout("Duplicate Cuts"):
            path0 = String.Join("Blocks", source_name, "Cuts", delimiter="/")
            path1 = String.Join("Blocks", new_name, "Cuts", delimiter="/")
            bundle = dupl_geo.get_bundle()
            bundle = bundle.set_item(path1, bundle.get_item(path0, socket_type="BUNDLE"))

        with Layout("Duplicate Planks"):
            block_id = source_node.id
            new_block_node = G().get_block_properties(dupl_geo, block_name=new_name)
            new_block_id = new_block_node.id

            # Mirror the inner bounds inside the block, keeping positive sizes.
            inner_offset = source_node.inner_location - source_node.location
            ox, oy, oz = inner_offset.xyz
            sy = source_node.size.y
            sz = source_node.size.z
            inner_size = source_node.inner_size
            inner_offset = Vector.IndexSwitch(
                inner_offset,
                (ox, sy - oy - inner_size.y, oz),
                (ox, oy, sz - oz - inner_size.z),
                index=sym_index,
            )
            inner_location = new_block_node.location + inner_offset
            bundle.set_item(
                String.Join("Blocks", new_name, "Inner Location", delimiter="/"),
                inner_location,
            )
            bundle.set_item(
                String.Join("Blocks", new_name, "Inner Size", delimiter="/"),
                inner_size,
            )

            planks = Mesh(Mesh(dupl_geo).points[Integer("Block ID")==block_id].separate())
            planks.points.set("Block ID", new_block_id)

            centered = Mesh(planks)
            centered.offset = -source_node.location - source_node.size.scale(0.5)

            tr_planks = Mesh(centered)

            centered.flip_faces()
            y_planks = Mesh(centered).transform(scale=(1, -1, 1))
            z_planks = Mesh(centered).transform(scale=(1, 1, -1))

            new_planks = Mesh(Mesh.IndexSwitch(tr_planks, y_planks, z_planks, index=sym_index))
            new_planks.offset = new_block_node.location + new_block_node.size.scale(0.5)

            # Randomize uv map
            bundle, seed = new_seed(bundle)
            uv_offset = Vector.Random((-10, -10, 0), (10, 10, 0), seed=seed, id=nd.mesh_island().island_index)
            new_planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)

            dupl_geo += new_planks
            dupl_geo.set_bundle(bundle)

            geo.switch(use_dupl_planks, dupl_geo)

        geo.out()

    # ====================================================================================================
    # Create Planks in a block
    # ====================================================================================================

    # ---------------------------------------------------------------------------
    # Adding a plank to planks
    # ---------------------------------------------------------------------------
        
    with GeoNodes(".Add Plank", is_group=True, rebuild=rebuild):
        bundle = Bundle(name="Bundle")
        block_name = String("Block", "Block Name")
        planks = Mesh(name="Planks")
        plank = Mesh(name="Plank")
        ok = Boolean(True, "Enabled")

        plank.switch_false(ok)
        cut = plank.get_bundle(remove=True)
        planks += plank
        bundle.switch(ok, add_cut_sheet(Bundle(bundle), block_name, cut))

        planks.out("Planks")
        bundle.out("Bundle")

    def add_plank(bundle, block_name, planks, plank, ok):
        """Call the shared group that adds a plank and records its cut."""
        result = G()._add_plank(
            bundle=bundle,
            block_name=block_name,
            planks=planks,
            plank=plank,
            enabled=ok,
        )
        return result.node.bundle, Mesh(result)

    # ----------------------------------------------------------------------------------------------------
    # Shelves
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Add Shelves", rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()

        block_name = String("Block", "Block Name")

        block_dims = G().get_block_properties(geo, block_name=block_name).node

        x, y, z = block_dims.inner_location.xyz
        sx, sy, sz = block_dims.inner_size.xyz

        with Panel("Shelves", create_layout=True):
            
            shelves = G().create_shelves(
                geo,
                height = sz,
                width = sy,
                depth = sx,
            ).link_inputs()
            shelves.offset = (x, y, z)

            bundle, planks = add_plank(bundle, block_name, None, shelves, True)
            planks = Mesh(planks)

        # ---------------------------------------------------------------------------
        # Finalize
        # ---------------------------------------------------------------------------

        with Layout("Finalize"):

            # Randomize uv map
            bundle, seed = new_seed(bundle)
            uv_offset = Vector.Random((-10, -10, 0), (10, 10, 0), seed=seed, id=nd.mesh_island().island_index)
            planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)

            # Block id
            planks.points.set("Block ID", block_dims.id)

            # Join
            geo += planks
            geo.set_bundle(bundle)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Front Face
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Add Face", rebuild=rebuild):

        geo = Geometry()
        bundle = geo.get_bundle()
        block_name = String("Block", "Block Name")

        face_type = Integer.MenuSwitch({
            "Door" : 0,
            "Double" : 1,
            "Drawers" : 2 
        }, menu=Input("Type", optional_label=True, expanded=True))

        count_y = Integer.IndexSwitch(1, 2, 1, index=face_type)
        count_z = Integer.IndexSwitch(1, 1, Integer(3, "Count", 1), index=face_type)

        block_dims = G().get_block_properties(geo, block_name=block_name).node

        front_location = bundle.get_item(
            String.Join("Blocks", block_name, "Front Location", delimiter="/"),
            socket_type='VECTOR',
        )
        x, y, z = block_dims.location.xyz
        sx, sy, sz = block_dims.size.xyz
        front_location.switch_false(front_location.exists, (x + sx, y, z))
        front_size = bundle.get_item(
            String.Join("Blocks", block_name, "Front Size", delimiter="/"),
            socket_type='VECTOR',
        )
        front_size.switch_false(front_size.exists, block_dims.size)

        with Layout("Configuration"): #("Panel", create_layout=True):
            front_side = Integer.MenuSwitch({
                "Overlay": 0, "Inset": 1,
            }, menu=Input("Front", optional_label=True, expanded=True))
            front_side_name = String("Plank", "Front Name")
            front_margin = Float.Distance(0, "Margin", 0)
            thickness = G().get_resource(geo, plank_name=front_side_name).thickness

            ix, iy, iz = block_dims.inner_location.xyz
            isx, isy, isz = block_dims.inner_size.xyz
            inset_location = Vector((ix + isx - thickness, iy, iz))
            location = Vector.Switch(front_side == 1, front_location, inset_location)
            size = Vector.Switch(front_side == 1, front_size, block_dims.inner_size)

            front = G().create_faces(
                geo, plank_name=front_side_name,
                width=size.y - 2*front_margin,
                length=size.z - 2*front_margin,
                count_y=count_y,
                count_z=count_z,
            ).link_inputs()
            front.offset = location + Vector((0, front_margin, front_margin))
            bundle, planks = add_plank(bundle, block_name, None, front, True)
            planks = Mesh(planks)

        with Layout("Finalize"):
            bundle, seed = new_seed(bundle)
            uv_offset = Vector.Random(
                (-10, -10, 0), (10, 10, 0), seed=seed,
                id=nd.mesh_island().island_index,
            )
            planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)
            planks.points.set("Block ID", block_dims.id)

            inner_size = Vector(block_dims.inner_size)
            inner_size.switch(front_side == 1, (isx - thickness, isy, isz))
            bundle.set_item(
                String.Join("Blocks", block_name, "Inner Size", delimiter="/"),
                inner_size,
            )
            geo += planks
            geo.set_bundle(bundle)

        geo.out()        

    # ----------------------------------------------------------------------------------------------------
    # Box
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Add Box Planks", rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()

        block_name = String("Block", "Block Name")

        block_dims = G().get_block_properties(geo, block_name=block_name).node

        x, y, z = block_dims.location.xyz
        sx, sy, sz = block_dims.size.xyz
            
        with Panel("Corners"):
            join_tl = Integer.MenuSwitch(JOIN_MENU, menu = Input("Top Left", expanded=True))
            join_tr = Integer.MenuSwitch(JOIN_MENU, menu = Input("Top Right", expanded=True))
            join_bl = Integer.MenuSwitch(JOIN_MENU, menu = Input("Bot Left", expanded=True))
            join_br = Integer.MenuSwitch(JOIN_MENU, menu = Input("Bot Right", expanded=True))
                
        with Panel("Sides", create_layout=True):
            left_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Left", optional_label=True, expanded=True))
            left_side_name = String("Plank", "Left Name")
            left_plank_node = G().get_resource(geo, left_side_name)
            left_thick = Float.Switch(left_side==0, left_plank_node.thickness)
            left_y0 = Float.IndexSwitch(0, 0, -left_thick/2, -left_thick, index=left_side)
            left_y1 = left_y0 + left_thick

            right_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Right", optional_label=True, expanded=True))
            right_side_name = String("Plank", "Right Name")
            right_plank_node = G().get_resource(geo, right_side_name)
            right_thick = Float.Switch(right_side==0, right_plank_node.thickness)
            right_y0 = sy + Float.IndexSwitch(0, -right_thick, -right_thick/2, 0, index=right_side)
            right_y1 = right_y0 + right_thick
            
            bot_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Bot", optional_label=True, expanded=True))
            bot_side_name = String("Plank", "Bot Name")
            bot_plank_node = G().get_resource(geo, bot_side_name)
            bot_thick = Float.Switch(bot_side==0, bot_plank_node.thickness)
            bot_z0 = Float.IndexSwitch(0, 0, -bot_thick/2, -bot_thick, index=bot_side)
            bot_z1 = bot_z0 + bot_thick

            top_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Top", optional_label=True, expanded=True))
            top_side_name = String("Plank", "Top Name")
            top_plank_node = G().get_resource(geo, top_side_name)
            top_thick = Float.Switch(top_side==0, top_plank_node.thickness)
            top_z0 = sz + Float.IndexSwitch(0, -top_thick, -top_thick/2, 0, index=top_side)
            top_z1 = top_z0 + top_thick

        # ---------------------------------------------------------------------------
        # Sides
        # ---------------------------------------------------------------------------
            
        with Layout("Left Side"):
            left_z0 = Float.IndexSwitch(bot_z1, bot_z0, bot_z0, index=join_bl) 
            left_z1 = Float.IndexSwitch(top_z0, top_z1, top_z1, index=join_tl)
            left_width = sx
            left_length = left_z1 - left_z0
            left_location = (x, y + left_y0, z + left_z0)
            
            plank = G().create_plank(
                geo,
                plank_name = left_side_name,
                width = left_width,
                length = left_length,
                setup = 'Flank',
            )
            plank.offset = left_location
            bundle, planks = add_plank(bundle, block_name, None, plank, left_side != 0)
            
        with Layout("Right Side"):
            right_z0 = Float.IndexSwitch(bot_z1, bot_z0, bot_z0, index=join_br) 
            right_z1 = Float.IndexSwitch(top_z0, top_z1, top_z1, index=join_tr)
            right_width = sx
            right_length = right_z1 - right_z0
            right_location = (x, y + right_y0, z + right_z0)
            
            plank = G().create_plank(
                geo,
                plank_name = right_side_name,
                width = right_width,
                length = right_length,
                setup = 'Flank',
            )
            plank.offset = right_location
            bundle, planks = add_plank(bundle, block_name, planks, plank, right_side != 0)
            
        with Layout("Bottom Side"):
            bot_y0 = Float.IndexSwitch(left_y0, left_y1, left_y0, index=join_bl) 
            bot_y1 = Float.IndexSwitch(right_y1, right_y0, right_y1, index=join_br)
            bot_width = sx
            bot_length = bot_y1 - bot_y0
            bot_location = (x, y + bot_y0, z + bot_z0)
            
            plank = G().create_plank(
                geo,
                plank_name = bot_side_name,
                width = bot_width,
                length = bot_length,
                setup = 'Shelf',
            )
            plank.offset = bot_location
            bundle, planks = add_plank(bundle, block_name, planks, plank, bot_side != 0)
            
        with Layout("Top Side"):
            top_y0 = Float.IndexSwitch(left_y0, left_y1, left_y0, index=join_tl) 
            top_y1 = Float.IndexSwitch(right_y1, right_y0, right_y1, index=join_tr)
            top_width = sx
            top_length = top_y1 - top_y0
            top_location = (x, y + top_y0, z + top_z0)
            
            plank = G().create_plank(
                geo,
                plank_name = top_side_name,
                width = top_width,
                length = top_length,
                setup = 'Shelf',
            )
            plank.offset = top_location
            bundle, planks = add_plank(bundle, block_name, planks, plank, top_side != 0)

        planks = Mesh(planks)

        # ---------------------------------------------------------------------------
        # Finalize
        # ---------------------------------------------------------------------------

        with Layout("Finalize"):

            # Randomize uv map
            bundle, seed = new_seed(bundle)
            uv_offset = Vector.Random((-10, -10, 0), (10, 10, 0), seed=seed, id=nd.mesh_island().island_index)
            planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)

            # Block id
            planks.points.set("Block ID", block_dims.id)

            # Inner location and size
            path = String.Join("Blocks", block_name, "Inner Location", delimiter="/")
            bundle.set_item(path, Vector((x, y + left_y1, z + bot_z1)))
            path = String.Join("Blocks", block_name, "Inner Size", delimiter="/")
            bundle.set_item(path, Vector((sx, right_y0 - left_y1, top_z0 - bot_z1)))

            # Preserve the front outline, including panels outside the block.
            bundle.set_item(
                String.Join("Blocks", block_name, "Front Location", delimiter="/"),
                Vector((x + sx, y + left_y0, z + bot_z0)),
            )
            bundle.set_item(
                String.Join("Blocks", block_name, "Front Size", delimiter="/"),
                Vector((sx, right_y1 - left_y0, top_z1 - bot_z0)),
            )

            # Join
            geo += planks
            geo.set_bundle(bundle)

        geo.out()



    # ====================================================================================================
    # Bundles
    # ====================================================================================================

    with GeoNodes("Add Column Component", rebuild=rebuild):

        geo = Geometry()
        col_name = String("Column", "Column Name")
        new_name = String("Block", "New Name")

        comp_type = Integer.MenuSwitch({
            "Shelves" : 0,
            "Doors" : 1,
            "Drawers" : 2,
        }, menu = Input("Component", optional_label=True, expanded=True))

        with Panel("Component", create_layout=True):
            res_name = String("Plank", "Resource")

            geo = G().create_sub_block(
                geo,
                show_frame=False,
                new_name = new_name,
                parent_name = col_name,
                type = "Column",
            ).link_inputs(exclude=["Y", "Width"])

            geo = G().add_box_planks(
                geo,
                block_name = new_name,
                sides_left = 'None',
                sides_right = 'None',
                sides_top = 'Int',
                sides_bot = 'Int',
                sides_bot_name = res_name,
                sides_top_name = res_name,
            )

        with Layout("Shelves"):
            shelves = G().add_shelves(
                geo, 
                block_name = new_name,
                ).link_inputs()

        with Layout("Doors"):
            doors = G().add_face(
                geo,
                block_name=new_name,
                type='Door',
                count=1,
            ).link_inputs()

        with Layout("Drawers"):
            drawers = G().add_face(
                geo,
                block_name=new_name,
                type='Drawers',
            ).link_inputs()

        geo = Geometry.IndexSwitch(shelves, doors, drawers, index=comp_type)

        geo.out()











    
        
        

