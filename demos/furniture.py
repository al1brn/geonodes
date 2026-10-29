from geonodes import *
import bpy
import json as jsonlib

ROLE_LEFT = 0
ROLE_RIGHT = 1
ROLE_BOTTOM = 2
ROLE_TOP = 3
ROLE_SHELF = 4
ROLE_FACE = 5
ROLE_DRAWER = 6
ROLE_SEPARATOR = 7
ROLE_PLINTH = 8
DEFAULT_FURNITURE_COLOR = "#C49A6CFF"


def get_cut_sheet(obj_name, json=False):
    """Return grouped cuts as indented text or a JSON string.

    Each row contains res_id, count, size (XYZ in integer millimeters), and orient.
    Counts are summed for cuts with the same resource ID, size, and orientation.
    Text rows show length x width (orientation): count, in millimeters.
    """
    obj = bpy.data.objects.get(obj_name)
    if obj is None:
        raise ValueError(f"Object {obj_name!r} not found")

    depsgraph = bpy.context.evaluated_depsgraph_get()
    evaluated = obj.evaluated_get(depsgraph)
    geometry = evaluated.evaluated_geometry()
    cloud = geometry.pointcloud
    if cloud is None or len(cloud.points) == 0:
        return "[]" if json else ""

    attributes = cloud.attributes
    missing = [name for name in ("Res ID", "Count", "Size", "Orient") if name not in attributes]
    if missing:
        raise ValueError(f"Cut Sheet object {obj_name!r} is missing attributes: {', '.join(missing)}")

    cuts = {}
    for i in range(len(cloud.points)):
        res_id = attributes["Res ID"].data[i].value
        count = attributes["Count"].data[i].value
        size = tuple(round(value * 1000) for value in attributes["Size"].data[i].vector)
        orient = attributes["Orient"].data[i].value
        key = (res_id, size, orient)
        if key in cuts:
            cuts[key]["count"] += count
        else:
            cuts[key] = {"res_id": res_id, "count": count, "size": size, "orient": orient}

    rows = sorted(cuts.values(), key=lambda cut: cut["res_id"])
    if json:
        return jsonlib.dumps(rows, indent=2)

    lines = []
    current_resource = None
    for cut in rows:
        if cut["res_id"] != current_resource:
            current_resource = cut["res_id"]
            lines.append(str(current_resource))
        width, length, _ = cut["size"]
        lines.append(f"\t{length} x {width} ({cut['orient']}) : {cut['count']}")
    return "\n".join(lines)


def demo(rebuild=False):

    # ====================================================================================================
    # Shaders
    # ====================================================================================================

    with ShaderNodes("Furniture", replace_material=rebuild):
        color = snd.attribute(
            attribute_type='GEOMETRY', attribute_name="Color",
        ).color
        Shader.Principled(
            base_color=color,
            roughness=0.25,
            metallic=0.0,
        ).out()

    with ShaderNodes("Debug Block", replace_material=rebuild):
        debug_color = snd.attribute(
            attribute_type='GEOMETRY', attribute_name="Debug Block Color",
        ).color
        debug_opacity = snd.attribute(
            attribute_type='GEOMETRY', attribute_name="Debug Block Opacity",
        ).factor
        shader = Shader.Principled(base_color=debug_color, roughness=0.5)
        shader.mix(shader=Shader.Transparent(), factor=1 - debug_opacity).out()

    with ShaderNodes("Drawer", replace_material=rebuild):
        Shader.Principled(
            base_color="#F2F2F2FF",
            roughness=0.65,
            metallic=0.0,
        ).out()

    
    with ShaderNodes("Label", replace_material=rebuild):
        Shader.Principled(
            base_color=snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").color,
            roughness=0.9,
        ).out()

    # ====================================================================================================
    # A dimension line
    # ====================================================================================================

    with GeoNodes("Add Cote Line", is_group=True, rebuild=rebuild):

        mesh = Mesh(Geometry())
        bundle = mesh.get_bundle()

        show   = Boolean(True,          "Show")
        pos    = Vector.Translation(0,  "Position")
        i_axis = Integer(0,             "Axis", 0, 2)
        value  = Float.Distance(1.0,    "Value", -5.0, 5.0)
        invert = Boolean(False,         "Invert")

        with Panel("Aspect"):
            font_size  = Float(0.1,  "Font Size", 0.01)
            section    = Float(0.01,    "Section", 0)
        
        offset_a = Float(0, "Cote Offset A", hide_in_modifier=True)
        offset_b = Float(0, "Cote Offset B", hide_in_modifier=True)
        
        with Layout("Positions"):
            line_dir = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis)
            pos.switch(value.less_than(0), pos + line_dir.scale(value))
            d = abs(value)
            use_ext = d.less_than(section*10)
            
        with Layout("Line"):
            h   = section*4
            h2  = section*2
            
            cone = Mesh.Cone(radius_bottom=h2, depth=h)
            
            with Mesh.Switch(use_ext) as line:
                d_int = d - h
                
                line_int = Curve.Line((0, 0, h), (0, 0, d_int))
                line_int = line_int.to_mesh(profile_curve=Curve.Circle(radius=section/2))
                
                line_int += Mesh(cone).transform(translation=(0, 0, d_int))
                line_int += Mesh(cone).transform(translation=(0, 0, h), rotation=(0, pi, 0))
                
                line_int.out("False")
                
            with line:
                line_ext = Curve.Line((0, 0, 0), (0, 0, d))
                line_ext = line_ext.to_mesh(profile_curve=Curve.Circle(radius=section/2))
                
                h_in = 0.75*h
                
                line_ext += Mesh(cone).transform(translation=(0, 0, -h_in))
                line_ext += Mesh(cone).transform(translation=(0, 0, d + h_in), rotation=(0, pi, 0))
                
                line_ext.out("True")

            line.transform(translation=pos, rotation=Rotation().align_z_to_vector(line_dir))
            
            line = Mesh(line)
            
            line.faces.Color=Color("Black")
            line.faces.material = "Label"
            
        with Layout("Label"):
            s = (d*100).to_string(decimals=1)
            label = Curve(s.to_curves(size=font_size).realize())
            label = label.fill()
            label.transform(rotation=(pi/2, 0, 0))
            
            with Layout("Z Rotation"):
                z_rot = Float.Switch(invert, 0, pi) + Float.Switch(i_axis.equal(0), pi/2)
                label.transform(rotation=(0, 0, z_rot))
                
            bounds = label.points.attribute_statistic(nd.position).node
            vmin = bounds.min
            vmax = bounds.max
            
            lx0, ly0, lz0 = vmin.xyz
            size_x, size_y, size_z = (vmax - vmin).xyz
            
            offset = Vector.IndexSwitch(
                Vector.Switch(use_ext,
                    Vector((-size_x/2 - lx0, 0, section*3)),
                    Vector((d/2 + h + font_size/3 - lx0, 0, -size_z/2))
                    ),
                Vector.Switch(use_ext,
                    Vector((0, -size_y/2 - ly0, section*3)),
                    Vector((0, d/2 + h + font_size/3 - ly0, -size_z/2))
                    ),
                Vector((0,  font_size/3 - ly0, -size_z/2)),
                index=i_axis)
                
            label.transform(translation=pos + line_dir.scale(d/2) + offset)
            
            with Layout("Finalize"):
                label.faces.Color = Color.IndexSwitch(
                    Color((0.05, 0, 0)),
                    Color((0, 0.05, 0)),
                    Color((0, 0, 0.05)),
                    index=i_axis)
                    
                label.faces.material = "Label"
                        
                line += label
                
                line = Mesh(line).faces.set_shade_smooth()
                
        with Layout("User Offset"):
            
            dir_a = Vector.IndexSwitch(
                Vector((0, 1, 0)),
                Vector((0, 0, 1)),
                Vector((1, 0, 0)),
                index = i_axis)
            
            dir_b = Vector.IndexSwitch(
                Vector((0, 0, 1)),
                Vector((1, 0, 0)),
                Vector((0, 1, 0)),
                index = i_axis)
            
            p = pos + line_dir.scale(d/2) + dir_a.scale(offset_a) + dir_b.scale(offset_b)
            gizmo_a = offset_a.linear_gizmo(position=p, direction=dir_a, color_id='PRIMARY')
            gizmo_b = offset_b.linear_gizmo(position=p, direction=dir_b, color_id='SECONDARY')
            
            line.transform(translation=dir_a.scale(offset_a) + dir_b.scale(offset_b))
            
        line = Mesh(line)
        line.points.Content = Integer.IndexSwitch(0x0100, 0x0200, 0x0400, index=i_axis)
        line.points.set("Role", Integer(-1))
        #line.points.Axis = i_axis
        
        line.switch_false(show)

        mesh += line

        mesh.set_bundle(bundle)
        mesh.out()

    RES_SIG = {"Plank Name": String, "ID": Integer, "Width": Float, "Length": Float, "Thickness": Float, "Material": Material, "Color": Color}
    BLOCK_SIG = {
        "ID": Integer,
        "On Plinth": Boolean,
        "Location": Vector, 
        "Size": Vector,
        "Inner Location": Vector,
        "Inner Size": Vector,
        "Outer Location": Vector,
        "Outer Size": Vector,
        "Left Thickness": Float,
        "Right Thickness": Float,
        "Bottom Thickness": Float,
        "Top Thickness": Float,
        "Cuts": Bundle,
        }
    CUT_SIG = {
        "Plank Name": String, 
        "Res ID": Integer, 
        "Count": Integer,
        "Size": Vector, 
        "Orient": Integer,
        }
    
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
    BOT_MENU_GROUND = {"N": 0, "I": 1, "M": 2, "E": 3, "Plinth": 4}
    
    ORIENT_MENU = {"Normal": 0, "Transverse": 1} 

    # ====================================================================================================
    # Common Inputs
    # ====================================================================================================

    def block_input(def_name):
        block_name = String(def_name, "Block Name")
        block_dims = Integer.MenuSwitch(
            {"Block": 0, "Inner": 1, "Outer": 2},
            menu=Input("Dims", optional_label=True, expanded=True))
        return block_name, block_dims
    
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
            block_id.switch_false(block_id.exists, 0)
            block_id += 1
            bundle.set_item("Block ID", block_id)

        return bundle, block_id

    def new_res_id(bundle, res_name):
        with Layout("Resource ID"):

            is_plank = res_name == "Plank"
            is_shelf = res_name == "Shelf"

            res_id = bundle.get_item("Resource ID", socket_type='INTEGER')
            res_id.switch_false(res_id.exists, 2)
            res_id += 1

            res_id.switch(is_plank, 1)
            res_id.switch(is_shelf, 2)

            new_bundle = Bundle(bundle)
            new_bundle.set_item("Resource ID", res_id)
            bundle.switch(res_id > 2, new_bundle)

        return bundle, res_id
    


    def set_reference_block(bundle, name, location, size):
        path = "Blocks/" + name
        previous = bundle.get_item(path, socket_type='BUNDLE')
        exists = previous.exists
        previous.switch_false(exists, Bundle.Combine({"ID": Integer(0), "Cuts": Bundle()}))
        bundle, fresh_id = new_block_id(bundle)
        block_id = Integer.Switch(exists, fresh_id, previous.get_item("ID", socket_type='INTEGER'))
        bundle.set_item(path, Bundle.Combine({
            "ID": block_id, "Location": location, "Size": size,
            "Cuts": previous.get_item("Cuts", socket_type='BUNDLE'),
        }))
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
        mat = Material("Furniture", "Material")
        col = Color(DEFAULT_FURNITURE_COLOR, "Color")

        bundle, res_id = new_res_id(bundle, new_name)

        res_bundle = Bundle.Combine({
            "Plank Name" : new_name,
            "ID" : res_id,
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
        use_id = Boolean(False, "By ID")
        plank_name = String("Plank", "Plank Name")
        pid = Integer(1, "Plank ID", 1)

        with Layout("Default Resources"):
            plank_def = Bundle.Combine({
                "Plank Name" : "Plank",
                "ID" : 1,
                "Width": 0.6,
                "Length" : 2.5,
                "Thickness" : 0.018,
                "Material" : Material("Furniture"),
                "Color" : Color(DEFAULT_FURNITURE_COLOR),
            })
            shelf_def = Bundle.Combine({
                "Plank Name" : "Shelf",
                "ID" : 2,
                "Width": 0.6,
                "Length" : 2.5,
                "Thickness" : 0.012,
                "Material" : Material("Furniture"),
                "Color" : Color(DEFAULT_FURNITURE_COLOR),
            })
        
        bundle = geo.get_bundle()

        with Layout("By Name"):
            by_name = bundle.get_item("Resources/" + plank_name, socket_type="BUNDLE")
            missing_name = by_name.exists.bnot()

            is_plank = plank_name.equal("Plank")
            by_name.switch(missing_name & is_plank, plank_def)
            missing_name.switch(is_plank)

            is_shelf = plank_name.equal("Shelf")
            by_name.switch(missing_name & is_shelf, shelf_def)
            missing_name.switch(is_shelf)

        with Layout("By ID"):
            resources = bundle.get_item("Resources", socket_type='BUNDLE')
            resources.switch_false(resources.exists)
            paths = resources.get_nested_paths(mode="Data Type", data_type="Integer")

            for rep in repeat(paths.list_length(), resource=Bundle(), found=False):
                path = paths[rep.iteration]
                resource_id = resources.get_item(path, socket_type='INTEGER')
                is_id = path.slice(position=path.length() - 3, length=3) == "/ID"
                match = is_id & (resource_id == pid) & rep.found.bnot()
                resource_path = path.slice(length=path.length() - 3)
                candidate = resources.get_item(resource_path, socket_type='BUNDLE')
                rep.resource.switch(match, candidate)
                rep.found |= match

            by_id = Bundle(rep.resource)
            by_id.switch(rep.found.bnot() & (pid == 1), plank_def)
            by_id.switch(rep.found.bnot() & (pid == 2), shelf_def)
            missing_id = (rep.found | (pid == 1) | (pid == 2)).bnot()

        res_bundle = Bundle.Switch(use_id, by_name, by_id)
        missing = Boolean.Switch(use_id, missing_name, missing_id)
        message = String.Switch(
            use_id,
            "Resource '" + plank_name + "' not found",
            "Resource ID " + pid.to_string() + " not found",
        )
        missing.warning(message)

        node = res_bundle.separate(signature=RES_SIG)
        node.out()

    # ----------------------------------------------------------------------------------------------------
    # Define plinth dimensions
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Define Plinth", rebuild=rebuild):
        geo = Geometry()
        bundle = geo.get_bundle()
        plank_name = String("Plank", "Plank Name")
        resource_id = G().get_resource(geo, plank_name=plank_name).id

        height = Float.Distance(0.1, "Height", 0, shape="Single")
        recess_x = Float.Distance(0.05, "Recess X", 0, shape="Single")
        recess_y = Float.Distance(0.05, "Recess Y", 0, shape="Single")

        bundle.set_item("Names/Plinth Resource ID", resource_id)
        bundle.set_item("Names/Plinth Height", height)
        bundle.set_item("Names/Plinth Recess X", recess_x)
        bundle.set_item("Names/Plinth Recess Y", recess_y)
        geo.set_bundle(bundle)
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Read plinth dimensions
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Get Plinth Dimensions", is_group=True, rebuild=rebuild):
        geo = Geometry()
        bundle = geo.get_bundle()
        missing = Boolean(False)

        for name, fallback in (("Height", 0.07), ("Recess X", 0.02), ("Recess Y", 0.02)):
            value = bundle.get_item("Names/Plinth " + name, socket_type='FLOAT')
            exists = value.exists
            missing |= exists.bnot()
            value.switch_false(exists, fallback)
            value.out(name)

        resource_id = bundle.get_item("Names/Plinth Resource ID", socket_type='INTEGER')
        exists = resource_id.exists
        missing |= exists.bnot()
        resource_id.switch_false(exists, 1)
        resource_id.out("Resource ID")

        missing.warning("Use 'Define Plinth' to define plinth dimensions.")

    # ----------------------------------------------------------------------------------------------------
    # Capture resources from another object
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Capture Resources", rebuild=rebuild):

        geo = Geometry()

        source = Object(name="Object")
        source_bundle = source.info().geometry.get_bundle()
        bundle = geo.get_bundle()
        bundle.set_item("Resources", source_bundle.get_item("Resources", socket_type='BUNDLE'))
        bundle.set_item("Resource ID", source_bundle.get_item("Resource ID", socket_type='INTEGER'))

        nd.set_geometry_bundle(bundle=bundle).out()
        
    # ====================================================================================================
    # Capture furniture for derived views
    # ====================================================================================================

    with GeoNodes("Capture Furniture", rebuild=rebuild):

        use_geometry = Boolean.MenuSwitch(
            {"Object": False, "Geometry": True},
            menu=Input("Source", optional_label=True, expanded=True),
        )
        obj = Object(None, "Furniture")
        source_geometry = Geometry()
        furniture = Geometry.Switch(use_geometry, obj.info().geometry, source_geometry)
        furniture.out()

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
            "Door": 2,
            }, menu=Input("Setup", optional_label=True, expanded=True))
        orient = Boolean.MenuSwitch({"Normal": False, "Rotate": True}, menu=Input("Orientation", optional_label=True, expanded=True))
        
        with Layout("Create Plank"):
            size = Vector((length, width, res_node.thickness))
            plank = Mesh.Cube(size=size)
            
            # Grain orientation affects texture coordinates, never board dimensions.
            uv = plank.points.evaluate_on_domain(nd.position)
            uv = Vector.Switch(orient, uv, Vector((-uv.y, uv.x, uv.z)))
            plank.corners.store_uv("UV Map", uv)
            
            plank.faces.material = res_node.material
            plank.faces.set("Color", res_node.color)
            plank.points.set("Role", Integer.IndexSwitch(ROLE_SHELF, ROLE_LEFT, ROLE_FACE, index=setup))
            plank.points.set("Index", Integer(0))

        with Layout("Setup"):

            rot=Rotation.IndexSwitch(
                (0, 0, pi/2),
                (0, pi/2, pi/2),
                (0, pi/2, 0),
                index = setup)

            plank.transform(rotation=rot)
                
            node = plank.points.attribute_statistic(nd.position).node
            size = node.max - node.min
            
            plank.offset = size.scale(0.5)

        with Layout("Cut Sheet"):
            cut_bundle = Bundle.Combine({
                "Plank Name": res_node.plank_name,
                "Res ID": res_node.id,
                "Count" : 1,
                "Size" : Vector.Switch(
                    orient,
                    Vector((width, length, res_node.thickness)),
                    Vector((length, width, res_node.thickness)),
                ),
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
        
        plank = G().create_plank(geo, width=wy, length=lz, setup='Door').link_inputs()
        cut_bundle = plank.get_bundle(remove=True)
        cut_bundle.set_item("Count", count_y*count_z)
        
        ofsy = (0, wy + margin, 0)
        ofsz = (0, 0, lz + margin)
        
        planks = G().array(plank, count=count_y, offset_method="Offset", translation=ofsy)
        planks = G().array(planks, count=count_z, offset_method="Offset", translation=ofsz)

        planks = Mesh(planks.realize())
        planks.points.set("Index", nd.mesh_island().island_index)
        planks.set_bundle(cut_bundle)

        planks.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Create an array of shelves
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Create Shelves", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        
        height = Float.Distance(1.0, "Height")
        z = Float.Distance(0.1, "Z")
        count = Integer(0, "Count", 0)
        
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

        shelves.switch(count==1, single)
        shelves = Mesh(shelves.realize())
        shelves.points.set("Index", nd.mesh_island().island_index)
        shelves.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Create vertical separators
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Create Separators", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        
        height = Float.Distance(1.0, "Height")
        y = Float.Distance(0.1, "Y", 0)
        count = Integer(0, "Count", 0)
        
        width = Float.Distance(0.45, "Width", 0.1, 3)
        depth = Float.Distance(0.28, "Depth", 0.1, 3)
        backset = Float.Distance(0.01, "Backset", 0, 0.1)
        
        plank = G().create_plank(geo, width=depth - backset, length=height, setup='Flank').link_inputs()
        thick = plank.size.y
        plank = Mesh(plank)
        plank.points.set("Role", Integer(ROLE_SEPARATOR))

        with Layout("Single Separator"):
            single = Mesh(plank)
            single.offset = (0, y, 0)

        with Layout("Several Separators"):
            cut_bundle = plank.get_bundle(remove=True)
            cut_bundle.set_item("Count", count)
            
            width_int = width - thick*count
            
            dist = width_int/(count + 1)
            
            plank.offset = (0, dist, 0)
            separators = G().array(plank, count=count, offset_method="Offset", translation=(0, dist + thick, 0))
            
            separators.switch(count==0)
            separators.set_bundle(cut_bundle)

        separators.switch(count==1, single)
        separators = Mesh(separators.realize())
        separators.points.set("Index", nd.mesh_island().island_index)
        separators.out()
        
    # ====================================================================================================
    # Get Block properties
    # ====================================================================================================

    def block_exists(geo, block_name):
        with Layout("Block exists"):
            bundle = geo.get_bundle().get_item("Blocks/" + block_name, socket_type='BUNDLE')
            return bundle.exists._lc("Block Exists")

    # ----------------------------------------------------------------------------------------------------
    # All properties
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Get Block Properties", is_group=True, rebuild=rebuild):
        
        geo = Geometry()
        block_name, block_dims = block_input("Block")
        #block_name = String("Block", "Block Name")
        
        bundle = geo.get_bundle().get_item("Blocks/" + block_name, socket_type='BUNDLE')
        exists = bundle.exists
        nope = bundle.exists.bnot()

        nope.warning("Block '" + block_name + "' not found.")

        node = bundle.separate(signature=BLOCK_SIG)

        block_id = node.id.switch(nope)

        location = node.location.switch(nope)
        size = node.size.switch(nope)
        inner_location = node.inner_location.switch(nope)
        inner_size = node.inner_size.switch(nope)
        outer_location = node.outer_location.switch(nope)
        outer_size = node.outer_size.switch(nope)
        
        cuts = node.cuts.switch(nope)

        exists.out("Exists")

        block_name.switch(nope).out("Block Name")
        block_id.out("ID")
        node.on_plinth.switch(nope).out("On Plinth")

        location.out("Block Location")
        size.out("Block Size")
        inner_location.out("Inner Location")
        inner_size.out("Inner Size")
        outer_location.out("Outer Location")
        outer_size.out("Outer Size")

        for side, thickness in (
            ("Left", node.left_thickness),
            ("Right", node.right_thickness),
            ("Bottom", node.bottom_thickness),
            ("Top", node.top_thickness),
        ):
            thickness = thickness.switch(nope).max(0)
            (thickness > 1e-6).out("Has " + side + " Side")
            thickness.out(side + " Thickness")
        
        cuts.out("Cuts")

        lc = Vector.IndexSwitch(location, inner_location, outer_location, index=block_dims)
        sz = Vector.IndexSwitch(size, inner_size, outer_size, index=block_dims)

        lc.out("Location")
        sz.out("Size")

        x, y, z = lc.xyz
        sx, sy, sz = sz.xyz

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
        
        axis = Integer.MenuSwitch(
            {"X": 0, "Y": 1, "Z": 2, "All": 3},
            menu=Input("Axis", default="All", optional_label=True, expanded=True),
        )
        axis_values = []
        for axis_name, properties in (
            ("X", {"Back": node.x0, "Front": node.x1, "Center": node.x_center, "Depth": node.size_x}),
            ("Y", {"Left": node.y0, "Right": node.y1, "Center": node.y_center, "Width": node.size_y}),
            ("Z", {"Bottom": node.z0, "Top": node.z1, "Center": node.z_center, "Height": node.size_z}),
        ):
            axis_values.append(Float.MenuSwitch(properties, menu=Input("Property " + axis_name)))

        all_values = Float.MenuSwitch({
            "Back": node.x0, "Front": node.x1, "Depth": node.size_x,
            "Left": node.y0, "Right": node.y1, "Width": node.size_y,
            "Bottom": node.z0, "Top": node.z1, "Height": node.size_z,
            "X Center": node.x_center, "Y Center": node.y_center, "Z Center": node.z_center,
        }, menu=Input("Property"))
        value = Float.IndexSwitch(*axis_values, all_values, index=axis)

        value.out("Value")

    # ----------------------------------------------------------------------------------------------------
    # Get UI Location input
    # ----------------------------------------------------------------------------------------------------

    def ui_location_value(with_plinth=False, return_plinth=False, axis="All"):
        choices = {"Value": 0, "Block": 1, "Name": 2}
        if with_plinth:
            choices["Plinth"] = 3

        index = Integer.MenuSwitch(
            choices, 
            menu=Input("Def", optional_label=True, expanded=True))
            
        block_name = String("Block", "Block Name")
        prop = G().get_block_property(
            geo, 
            block_name=block_name, 
            dims=Input("Dims", optional_label=True, expanded=True), 
            axis=axis,
            **{("property" if axis == "All" else "property_" + axis.lower()): Input("Prop")})
        
        named = G().get_named_dimension(geo, name=Input("Name"))
        offset = Float.Distance(0, "Offset")

        values = [0, prop, named]
        if with_plinth:
            values.append(G()._get_plinth_dimensions(geo).height)

        value = Float.IndexSwitch(*values, index=index)
        if with_plinth:
            offset = Float.Switch(index == 3, offset, 0)
        value += offset
        if return_plinth:
            return value, index == 3
        return value

    # ----------------------------------------------------------------------------------------------------
    # Get a location input
    # ----------------------------------------------------------------------------------------------------
        
    def get_location(geo, name, with_plinth=False, return_plinth=False):
        with Panel(name, create_layout=True):
            return ui_location_value(
                with_plinth=with_plinth, return_plinth=return_plinth,
                axis={"X": "X", "Y": "Y", "Z": "Z", "Y Center": "Y", "Z Center": "Z",
                      "Offset Y": "Y", "Offset Z": "Z"}.get(name, "All"),
            )

    # ----------------------------------------------------------------------------------------------------
    # Get a dimension input
    # ----------------------------------------------------------------------------------------------------

    def get_dimension(geo, name, base):
        with Panel(name, create_layout=True):
            rel_incr = Boolean.MenuSwitch(
                {"Dimension": False, "Target": True}, 
                menu=Input("Mode", optional_label=True, expanded=True))

            value = ui_location_value(axis={"Size X": "X", "Size Y": "Y", "Size Z": "Z"}.get(name, "All"))
            value.switch(rel_incr, value - base)

            return value

    # ====================================================================================================
    # Define Blocks
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Debug
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Debug Block", rebuild=rebuild):

        geo = Geometry()
        bundle = geo.get_bundle()
        #name = String("Block", "Name")
        block = G().get_block_properties(geo).link_inputs().node

        show_frame = Boolean(True, "Show Frame")
        del_planks = Boolean(True, "Remove Planks")
        color = Color("Blue", "Color")
        opacity = Float.Factor(1, "Opacity", 0, 1)

        cube = Mesh.Cube(size=block.size)
        cube.offset = block.location + block.size.scale(0.5)
        cube.faces.set("Debug Block Color", color)
        cube.faces.set("Debug Block Opacity", opacity)
        cube.faces.material = Material("Debug Block")

        frame = Mesh(cube)
        frame.faces.delete('Only Faces')
        frame.switch_false(show_frame)
        debug = cube + frame

        remaining = Mesh(geo)
        remaining.points[del_planks & (Integer("Block ID") == block.id)].delete()
        geo = Geometry(remaining)
        geo += debug
        geo.set_bundle(bundle)
        geo.out()

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
        z, on_plinth = get_location(geo, "Z", with_plinth=True, return_plinth=True)

        sx = get_dimension(geo, "Size X", x)
        sy = get_dimension(geo, "Size Y", y)
        sz = get_dimension(geo, "Size Z", z)

        location = Vector((x, y, z))
        size = Vector((sx, sy, sz))

        with Layout("Create Bundle Entry"):

            bundle, block_id = new_block_id(bundle)
            block_bundle = Bundle.Combine({
                "ID": block_id,
                "On Plinth": on_plinth, 
                "Location": location, 
                "Size": size,
                "Inner Location": location,
                "Inner Size": size,
                "Outer Location": location,
                "Outer Size": size,
                "Left Thickness": Float(0),
                "Right Thickness": Float(0),
                "Bottom Thickness": Float(0),
                "Top Thickness": Float(0),
                "Cuts": Bundle()})
            
        with Layout("Frame"):
            block_frame = Mesh.Cube(size=size)
            block_frame.offset = size.scale(0.5) + location
            block_frame.faces.delete('Only Faces')
            block_frame.switch_false(show_frame)

        with Layout("Finalize"):

            bundle.set_item("Blocks/" + new_name, block_bundle)
            geo += block_frame

            geo.set_bundle(bundle)

        geo.out()

    # ====================================================================================================
    # Operations on blocks
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Duplicate block
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Block Duplicate", is_group=False, rebuild=rebuild):

        geo = Geometry()
        source = String("Source", "Source Name")
        target = String("Target", "Target Name")
        dupl_planks = Boolean(True, "Duplicate Planks")

        bundle = geo.get_bundle()

        with Layout(f"Copy Block"):

            source_bundle = bundle.get_item("Blocks/" + source, socket_type="BUNDLE")

            new_bundle = Bundle(bundle)

            props = source_bundle.separate(signature=BLOCK_SIG)
            new_bundle, new_id = new_block_id(new_bundle)

            source_id = props.id.switch_false(source_bundle.exists, -1)

            target_bundle = Bundle(source_bundle)
            target_bundle.set_item("ID", new_id)

            new_bundle.set_item("Blocks/" + target, target_bundle)
            bundle.switch(source_bundle.exists, new_bundle)

        with Layout("Duplicate Planks"):

            planks = Mesh(Mesh(geo).points[source_bundle.exists & (Integer("Block ID")==source_id)].separate())
            planks.points.set("Block ID", new_id)

            # Randomize uv map
            new_bundle = Bundle(bundle)
            new_bundle, seed = new_seed(new_bundle)
            uv_offset = Vector.Random((-10, -10, 0), (10, 10, 0), seed=seed, id=nd.mesh_island().island_index)
            planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)

            geo.switch(dupl_planks, geo + planks)
            bundle.switch(dupl_planks, new_bundle)

        geo.set_bundle(bundle)
        geo.out()
        source_bundle.exists.out("Exists")
        new_id.out("Block ID")

    # ----------------------------------------------------------------------------------------------------
    # Translate block
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Block Translate", is_group=False, rebuild=rebuild):

        geo = Geometry()
        block_name = String("Block", "Block Name")
        translation = Vector(0, "Translation")

        bundle = geo.get_bundle()

        with Layout("Translate Block"):

            path = "Blocks/" + block_name
            source_bundle = bundle.get_item(path, socket_type="BUNDLE")

            new_bundle = Bundle(bundle)

            props = source_bundle.separate(signature=BLOCK_SIG)

            block_id = props.id.switch_false(source_bundle.exists, -1)

            target_bundle = Bundle(source_bundle)
            for name, location in (
                ("Location", props.location),
                ("Inner Location", props.inner_location),
                ("Outer Location", props.outer_location),
            ):
                target_bundle.set_item(name, location + translation)

            new_bundle.set_item(path, target_bundle)
            bundle.switch(source_bundle.exists, new_bundle)

        with Layout("Planks"):
            planks = Mesh(Mesh(geo).points[source_bundle.exists & (Integer("Block ID")==block_id)].separate())
            remain = planks.inverted
            planks.offset = translation

            geo = remain + planks

        geo.set_bundle(bundle)
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Block symmetry
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Block Symmetry"):

        geo = Geometry()
        block_name = String("Block", "Block Name")

        sym_index = Integer.MenuSwitch(
            {"No" : 0, "Y": 1, "Z": 2},
            menu = Input("Symmetry", optional_label=True, expanded=True))

        ys = Float.Distance(0.0, "Y Center")
        zs = Float.Distance(0.0, "Z Center")

        ys2, zs2 = 2*ys, 2*zs

        bundle = geo.get_bundle()

        with Layout("Blocks Symmetry"):
            path = "Blocks/" + block_name
            source_bundle = bundle.get_item(path, socket_type="BUNDLE")

            new_bundle = Bundle(bundle)

            props = source_bundle.separate(signature=BLOCK_SIG)

            block_id = props.id.switch_false(source_bundle.exists, -1)

            sym_bundle = Bundle(source_bundle)
            for name, location, size in (
                ("Location", props.location, props.size),
                ("Inner Location", props.inner_location, props.inner_size),
                ("Outer Location", props.outer_location, props.outer_size),
            ):
                x0, y0, z0 = location.xyz
                _, y1, z1 = (location + size).xyz
                mirrored = Vector.IndexSwitch(
                    location,
                    (x0, ys2 - y1, z0),
                    (x0, y0, zs2 - z1),
                    index=sym_index,
                )
                sym_bundle.set_item(name, mirrored)

            sym_bundle.set_item("Left Thickness", Float.Switch(sym_index == 1, props.left_thickness, props.right_thickness))
            sym_bundle.set_item("Right Thickness", Float.Switch(sym_index == 1, props.right_thickness, props.left_thickness))
            sym_bundle.set_item("Bottom Thickness", Float.Switch(sym_index == 2, props.bottom_thickness, props.top_thickness))
            sym_bundle.set_item("Top Thickness", Float.Switch(sym_index == 2, props.top_thickness, props.bottom_thickness))

            new_bundle.set_item(path, sym_bundle)
            bundle.switch(source_bundle.exists, new_bundle)

        with Layout("Planks"):

            planks = Mesh(Mesh(geo).points[source_bundle.exists & (Integer("Block ID") == block_id)].separate())
            remain = planks.inverted

            x, y, z = nd.position.xyz
            planks.position = Vector.IndexSwitch(
                nd.position,
                (x, ys2 - y, z),
                (x, y, zs2 - z),
                index = sym_index,
            )
            flipped = Mesh(planks)
            flipped.flip_faces()
            planks.switch(sym_index!=0, flipped)
            geo = remain + planks
    
        geo.set_bundle(bundle)
        geo.out()                

    # ----------------------------------------------------------------------------------------------------
    # Sub block
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Duplicate Block"):

        geo = Geometry()

        new_name = String("Block", "New Name")

        source_name = String("Source", "Source Name")
        use_dupl_planks = Boolean(False, "Planks")

        sym_index = Integer.MenuSwitch(
            {"No" : 0, "Y": 1, "Z": 2},
            menu = Input("Symmetry", optional_label=True, expanded=True))

        ys = get_location(geo, "Y Center")
        zs = get_location(geo, "Z Center")

        ty = get_location(geo, "Offset Y")
        tz = get_location(geo, "Offset Z")

        count = Integer(1, "Count", 1, 10)
        count.switch(sym_index>0, 1)
        is_array = (sym_index == 0) & (count > 1)

        for rep in repeat(count, geo=geo, ty=ty, tz=tz, exists=False):

            with Layout("Duplicate the block"):

                dupl_name = String(new_name)
                dupl_name.switch(
                        is_array, 
                        String.Join(
                            dupl_name, 
                            rep.iteration.to_string(), 
                            delimiter=" "))

                dupl_geo = G()._block_duplicate(
                    rep.geo,
                    source_name = source_name,
                    target_name = dupl_name,
                    duplicate_planks = use_dupl_planks,
                )
                exists = dupl_geo.exists
                ((rep.iteration==0) & exists.bnot()).warning("Block '" + source_name + "' not found")

            with Layout("Translation"):
                new_geo = G()._block_translate(
                    dupl_geo,
                    block_name = dupl_name,
                    translation = (0, rep.ty, rep.tz),
                )
                dupl_geo.switch(exists & (sym_index==0), new_geo)

            rep.geo = dupl_geo
            rep.ty += ty
            rep.tz += tz
            rep.exists=exists

        geo = rep.geo
        exists = rep.exists

        with Layout("Symmetry Y"):
            new_geo = G()._block_symmetry(
                geo,
                block_name = new_name,
                symmetry = 'Y',
                y_center = ys,
            )
            geo.switch(exists & (sym_index==1), new_geo)

        with Layout("Symmetry Z"):
            new_geo = G()._block_symmetry(
                geo,
                block_name = new_name,
                symmetry = 'Z',
                z_center = zs,
            )
            geo.switch(exists & (sym_index==2), new_geo)

        with Layout("Total Size"):
            block_dims = G().get_block_properties(geo, block_name=source_name, dims='Block').node
            width = ((block_dims.size_y + count*ty)*1000).to_integer()
            height = ((block_dims.size_z + count*tz)*1000).to_integer()
            is_array.info(String.Join("Width: ", width.to_string(), ", height: ", height.to_string(), " mm"))

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

        block_dims = G().get_block_properties(geo, block_name=block_name, dims='Inner').node

        x, y, z = block_dims.location.xyz
        sx, sy, sz = block_dims.size.xyz

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
    # Separators
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Add Separators", rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()

        block_name = String("Block", "Block Name")

        block_dims = G().get_block_properties(geo, block_name=block_name, dims='Inner').node

        x, y, z = block_dims.location.xyz
        sx, sy, sz = block_dims.size.xyz

        with Panel("Separators", create_layout=True):
            
            separators = G().create_separators(
                geo,
                height = sz,
                width = sy,
                depth = sx,
            ).link_inputs()
            separators.offset = (x, y, z)

            bundle, planks = add_plank(bundle, block_name, None, separators, True)
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
            "Drawers" : 1,
        }, menu=Input("Type", optional_label=True, expanded=True))

        count = Integer(1, "Count", 1).max(1)
        count_y = Integer.Switch(face_type == 1, count, 1)
        count_z = Integer.Switch(face_type == 1, 1, count)

        block_dims = G().get_block_properties(geo, block_name=block_name).node

        with Layout("Configuration"): #("Panel", create_layout=True):
            front_side = Integer.MenuSwitch({
                "None": 0, "Overlay": 1, "Inset": 2,
            }, menu=Input("Front", optional_label=True, expanded=True))
            front_side_name = String("Plank", "Front Name")
            front_margin = Float.Distance(0, "Margin", 0)
            thickness = G().get_resource(geo, plank_name=front_side_name).thickness

            left_shared = Boolean(False, "Left Shared")
            right_shared = Boolean(False, "Right Shared")
            bottom_shared = Boolean(False, "Bottom Shared")
            top_shared = Boolean(False, "Top Shared")

            left_cover = Float.Switch(left_shared, block_dims.left_thickness, block_dims.left_thickness / 2)
            right_cover = Float.Switch(right_shared, block_dims.right_thickness, block_dims.right_thickness / 2)
            bottom_cover = Float.Switch(bottom_shared, block_dims.bottom_thickness, block_dims.bottom_thickness / 2)
            top_cover = Float.Switch(top_shared, block_dims.top_thickness, block_dims.top_thickness / 2)
            overlay_origin = block_dims.inner_location - Vector((0, left_cover, bottom_cover))
            overlay_size = block_dims.inner_size + Vector((
                0, left_cover + right_cover, bottom_cover + top_cover,
            ))

            inset = front_side == 2
            origin = Vector.Switch(front_side == 1, block_dims.inner_location, overlay_origin)
            size = Vector.Switch(front_side == 1, block_dims.inner_size, overlay_size)
            x, y, z = origin.xyz
            location = Vector((x + size.x - Float.Switch(inset, 0, thickness), y, z))

            front = G().create_faces(
                geo, plank_name=front_side_name,
                width=size.y - 2*front_margin,
                length=size.z - 2*front_margin,
                count_y=count_y,
                count_z=count_z,
            ).link_inputs()
            front = Mesh(front)
            front.points.set("Role", Integer.Switch(face_type == 1, ROLE_FACE, ROLE_DRAWER))
            front.offset = location + Vector((0, front_margin, front_margin))
            bundle, planks = add_plank(bundle, block_name, None, front, front_side != 0)
            planks = Mesh(planks)

        with Layout("Finalize"):
            bundle, seed = new_seed(bundle)
            uv_offset = Vector.Random(
                (-10, -10, 0), (10, 10, 0), seed=seed,
                id=nd.mesh_island().island_index,
            )
            planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)
            planks.points.set("Block ID", block_dims.id)

            geo += planks
            geo.set_bundle(bundle)

        geo.out()        

    # ----------------------------------------------------------------------------------------------------
    # Box
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Add Box", rebuild=rebuild):
        
        geo = Geometry()
        bundle = geo.get_bundle()

        block_name = String("Block", "Block Name")

        block_dims = G().get_block_properties(geo, block_name=block_name).node

        x, y, z = block_dims.location.xyz
        sx, sy, sz = block_dims.size.xyz
        on_ground = z == 0
        plinth = G()._get_plinth_dimensions(geo).node
        plinth_height = plinth.height
        force_bot_ext = block_dims.on_plinth & (z == plinth_height)

        with Panel("Sides", create_layout=True):
            left_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Left", expanded=True))
            left_side_name = String("Plank", "Left Name")
            left_existing = Boolean(False, "Existing Plank", shape="Single")
            left_plank_node = G().get_resource(geo, plank_name=left_side_name)

            right_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Right", expanded=True))
            right_side_name = String("Plank", "Right Name")
            right_existing = Boolean(False, "Existing Plank", shape="Single")
            right_plank_node = G().get_resource(geo, plank_name=right_side_name)
            
            top_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Top", expanded=True))
            top_side_name = String("Plank", "Top Name")
            top_existing = Boolean(False, "Existing Plank", shape="Single")
            top_plank_node = G().get_resource(geo, plank_name=top_side_name)

            bot_side = Integer.MenuSwitch(BOT_MENU_GROUND, menu=Input("Bot", expanded=True))
            requested_plinth = bot_side == 4
            (requested_plinth & on_ground.bnot() & force_bot_ext.bnot()).warning(
                "Bottom Plinth is only available when Z = 0.",
            )
            bot_side.switch(requested_plinth & on_ground.bnot(), SIDE_NONE)
            bot_side.switch(on_ground & ((bot_side == SIDE_MID) | (bot_side == SIDE_EXT)), SIDE_INT)
            bot_side.switch(force_bot_ext, SIDE_EXT)
            use_plinth = bot_side == 4
            bot_side_name = String("Plank", "Bot Name")
            bot_existing = Boolean(False, "Existing Plank", shape="Single")
            bot_plank_node = G().get_resource(geo, plank_name=bot_side_name)

        with Panel("Corners"):
            join_tl = Integer.MenuSwitch(JOIN_MENU, menu = Input("Top Left", expanded=True))
            join_tr = Integer.MenuSwitch(JOIN_MENU, menu = Input("Top Right", expanded=True))
            join_bl = Integer.MenuSwitch(JOIN_MENU, menu = Input("Bot Left", expanded=True))
            join_br = Integer.MenuSwitch(JOIN_MENU, menu = Input("Bot Right", expanded=True))

        with Layout("Existing Bounds"):
            inner_end = block_dims.inner_location + block_dims.inner_size
            outer_end = block_dims.outer_location + block_dims.outer_size

        with Layout("Sides"):
            left_thick = Float.Switch(left_side==0, left_plank_node.thickness)
            left_y0 = Float.IndexSwitch(0, 0, -left_thick/2, -left_thick, index=left_side)
            left_y1 = left_y0 + left_thick
            preserve_left = block_dims.has_left_side | (left_side == SIDE_NONE)
            left_y0.switch(preserve_left, block_dims.outer_location.y - y)
            left_y1.switch(preserve_left, block_dims.inner_location.y - y)

            right_thick = Float.Switch(right_side==0, right_plank_node.thickness)
            right_y0 = sy + Float.IndexSwitch(0, -right_thick, -right_thick/2, 0, index=right_side)
            right_y1 = right_y0 + right_thick
            preserve_right = block_dims.has_right_side | (right_side == SIDE_NONE)
            right_y0.switch(preserve_right, inner_end.y - y)
            right_y1.switch(preserve_right, outer_end.y - y)

            bot_thick = Float.Switch(bot_side==0, bot_plank_node.thickness)
            bot_z0 = Float.IndexSwitch(
                0, 0, -bot_thick/2, -bot_thick, plinth_height - z - bot_thick,
                index=bot_side,
            )
            bot_z1 = bot_z0 + bot_thick
            preserve_bot = block_dims.has_bottom_side | (bot_side == SIDE_NONE)
            bot_z0.switch(preserve_bot, Float.Switch(
                block_dims.has_bottom_side,
                block_dims.outer_location.z - z,
                block_dims.inner_location.z - block_dims.bottom_thickness - z,
            ))
            bot_z1.switch(preserve_bot, block_dims.inner_location.z - z)

            top_thick = Float.Switch(top_side==0, top_plank_node.thickness)
            top_z0 = sz + Float.IndexSwitch(0, -top_thick, -top_thick/2, 0, index=top_side)
            top_z1 = top_z0 + top_thick
            preserve_top = block_dims.has_top_side | (top_side == SIDE_NONE)
            top_z0.switch(preserve_top, inner_end.z - z)
            top_z1.switch(preserve_top, outer_end.z - z)

            raised_bottom = use_plinth | (
                block_dims.has_bottom_side
                & (block_dims.inner_location.z - block_dims.bottom_thickness > z)
            )
            outer_bot_z = Float.Switch(raised_bottom, z + bot_z0, block_dims.outer_location.z)

        # ---------------------------------------------------------------------------
        # Sides
        # ---------------------------------------------------------------------------
            
        with Layout("Left Side"):
            left_z0 = Float.IndexSwitch(bot_z1, bot_z0, bot_z0, index=join_bl) 
            left_z1 = Float.IndexSwitch(top_z0, top_z1, top_z1, index=join_tl)
            left_z0.switch(block_dims.has_bottom_side, bot_z1)
            left_z0.switch(raised_bottom, 0)
            left_z1.switch(block_dims.has_top_side, top_z0)
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
            plank = Mesh(plank)
            plank.points.set("Role", Integer(ROLE_LEFT))
            plank.offset = left_location
            bundle, planks = add_plank(bundle, block_name, None, plank, (left_side != SIDE_NONE) & left_existing.bnot() & block_dims.has_left_side.bnot())
            
        with Layout("Right Side"):
            right_z0 = Float.IndexSwitch(bot_z1, bot_z0, bot_z0, index=join_br) 
            right_z1 = Float.IndexSwitch(top_z0, top_z1, top_z1, index=join_tr)
            right_z0.switch(block_dims.has_bottom_side, bot_z1)
            right_z0.switch(raised_bottom, 0)
            right_z1.switch(block_dims.has_top_side, top_z0)
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
            plank = Mesh(plank)
            plank.points.set("Role", Integer(ROLE_RIGHT))
            plank.offset = right_location
            bundle, planks = add_plank(bundle, block_name, planks, plank, (right_side != SIDE_NONE) & right_existing.bnot() & block_dims.has_right_side.bnot())
            
        with Layout("Bottom Side"):
            bot_y0 = Float.IndexSwitch(left_y0, left_y1, left_y0, index=join_bl) 
            bot_y1 = Float.IndexSwitch(right_y1, right_y0, right_y1, index=join_br)
            bot_y0.switch(block_dims.has_left_side, left_y1)
            bot_y1.switch(block_dims.has_right_side, right_y0)
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
            plank = Mesh(plank)
            plank.points.set("Role", Integer(ROLE_BOTTOM))
            plank.offset = bot_location
            bundle, planks = add_plank(bundle, block_name, planks, plank, (bot_side != SIDE_NONE) & bot_existing.bnot() & block_dims.has_bottom_side.bnot())
            
        with Layout("Top Side"):
            top_y0 = Float.IndexSwitch(left_y0, left_y1, left_y0, index=join_tl) 
            top_y1 = Float.IndexSwitch(right_y1, right_y0, right_y1, index=join_tr)
            top_y0.switch(block_dims.has_left_side, left_y1)
            top_y1.switch(block_dims.has_right_side, right_y0)
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
            plank = Mesh(plank)
            plank.points.set("Role", Integer(ROLE_TOP))
            plank.offset = top_location
            bundle, planks = add_plank(bundle, block_name, planks, plank, (top_side != SIDE_NONE) & top_existing.bnot() & block_dims.has_top_side.bnot())

        with Layout("Plinth"):
            resource = G().get_resource(
                geo, by_id=True, plank_id=plinth.resource_id,
            ).node
            has_left = block_dims.has_left_side | (left_side != SIDE_NONE)
            has_right = block_dims.has_right_side | (right_side != SIDE_NONE)
            plinth_left = Float.Switch(has_left, plinth.recess_y, left_y1)
            plinth_right = Float.Switch(has_right, sy - plinth.recess_y, right_y0)
            plinth_depth = sx - plinth.recess_x
            plinth_length = plinth_height - z - bot_thick
            create_plinth = use_plinth & block_dims.has_bottom_side.bnot() & bot_existing.bnot()

            front = Mesh(G().create_plank(
                geo, plank_name=resource.plank_name,
                width=plinth_right - plinth_left,
                length=plinth_length,
                setup='Door', orientation='Rotate',
            ))
            front.offset = (
                x + plinth_depth - resource.thickness,
                y + plinth_left,
                z,
            )
            front.points.set("Role", Integer(ROLE_PLINTH))
            front.points.set("Index", Integer(0))
            bundle, planks = add_plank(bundle, block_name, planks, front, create_plinth)

            for index, side_y, has_side in (
                (1, plinth_left, has_left),
                (2, plinth_right - resource.thickness, has_right),
            ):
                side = Mesh(G().create_plank(
                    geo, plank_name=resource.plank_name,
                    width=plinth_depth,
                    length=plinth_length,
                    setup='Flank',
                ))
                side.offset = (x, y + side_y, z)
                side.points.set("Role", Integer(ROLE_PLINTH))
                side.points.set("Index", Integer(index))
                bundle, planks = add_plank(
                    bundle, block_name, planks, side, create_plinth & has_side.bnot(),
                )

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

            path = "Blocks/" + block_name + "/"
            bundle.set_item(path + "Inner Location", Vector((
                block_dims.inner_location.x, y + left_y1, z + bot_z1,
            )))
            bundle.set_item(path + "Inner Size", Vector((
                block_dims.inner_size.x, right_y0 - left_y1, top_z0 - bot_z1,
            )))
            bundle.set_item(path + "Outer Location", Vector((
                block_dims.outer_location.x, y + left_y0, outer_bot_z,
            )))
            bundle.set_item(path + "Outer Size", Vector((
                block_dims.outer_size.x, right_y1 - left_y0, z + top_z1 - outer_bot_z,
            )))

            for side, requested, previous, preserve in (
                ("Left", left_thick, block_dims.left_thickness, preserve_left),
                ("Right", right_thick, block_dims.right_thickness, preserve_right),
                ("Bottom", bot_thick, block_dims.bottom_thickness, preserve_bot),
                ("Top", top_thick, block_dims.top_thickness, preserve_top),
            ):
                bundle.set_item(path + side + " Thickness", Float.Switch(preserve, requested, previous))

            # Join
            geo += planks
            geo.set_bundle(bundle)

        geo.out()

    # ====================================================================================================
    # Add a complete block
    # ====================================================================================================

    with GeoNodes("Add Block", rebuild=rebuild):
        geo = Geometry()
        new_name = String("Block", "New Name")

        geo = G().define_block(
            geo, new_name=new_name,
        ).link_inputs(from_panel="Block")

        geo = G().add_box(
            geo, block_name=new_name,
        ).link_inputs()

        geo = G().add_shelves(
            geo, block_name=new_name,
        ).link_inputs()

        geo = G().add_separators(
            geo, block_name=new_name,
        ).link_inputs()

        geo = G().add_face(
            geo, block_name=new_name,
        ).link_inputs(from_panel="Door")

        geo.out()

    # ====================================================================================================
    # Select a plank
    # ====================================================================================================

    with GeoNodes("Select Plank", is_group=True, rebuild=rebuild):
        geo = Geometry()
        all_blocks = Boolean(False, "All Blocks")
        block_name = String("Block", "Block Name")
        block = geo.get_bundle().get_item("Blocks/" + block_name, socket_type='BUNDLE')
        exists = block.exists
        block_id = block.get_item("ID", socket_type='INTEGER')
        (all_blocks.bnot() & exists.bnot()).warning("Block '" + block_name + "' not found.")
        selection = Boolean.Switch(all_blocks, exists & (Integer("Block ID") == block_id), True)
        role = Integer.MenuSwitch({
            "Left": ROLE_LEFT,
            "Right": ROLE_RIGHT,
            "Bottom": ROLE_BOTTOM,
            "Top": ROLE_TOP,
            "Shelf": ROLE_SHELF,
            "Separator": ROLE_SEPARATOR,
            "Plinth": ROLE_PLINTH,
            "Door": ROLE_FACE,
            "Drawer": ROLE_DRAWER,
        }, menu=Input("Role", optional_label=True))
        all_indices = Boolean(False, "All")
        index = Integer(0, "Index", 0)

        matches_index = Boolean.Switch(all_indices, Integer("Index") == index, True)
        selection &= Integer("Role") == role
        selection &= matches_index

        selection.out("Selection")

        block_name.out("Block Name")
        block_id.switch_false(exists & all_blocks.bnot(), -1).out("Block Id")

    # ====================================================================================================
    # Open door
    # ====================================================================================================

    with GeoNodes("Open Door", rebuild=rebuild):
        geo = Geometry()
        selection = G().select_plank(
            geo,
            role='Door', 
            all=False).link_inputs()
        axis = Integer.MenuSwitch(
            {"Z": 0, "Y": 1},
            menu=Input("Axis", default="Z", optional_label=True, expanded=True),
        )
        right_side = Boolean.MenuSwitch(
            {"Left": False, "Right": True},
            menu=Input("Side", optional_label=True, expanded=True),
        )
        top_side = Boolean.MenuSwitch(
            {"Top": True, "Bottom": False},
            menu=Input("Horizontal Side", optional_label=True, expanded=True),
        )
        angle = Float.Angle(0, "Angle", 0, pi)

        dim_node = Mesh(geo).points[selection].attribute_statistic(nd.position).node

        x0, y0, z0 = dim_node.min.xyz
        x1, y1, z1 = dim_node.max.xyz

        # Y grows from left to right; both hinge sides open toward +X.
        z_axis = Vector.Switch(right_side, (x1, y0, 0), (x1, y1, 0))
        rot = Rotation.Switch(right_side, (0, 0, -angle), (0, 0, angle))
        y_axis = Vector.Switch(top_side, (x1, 0, z0), (x1, 0, z1))
        y_rot = Rotation.Switch(top_side, (0, angle, 0), (0, -angle, 0))
        pivot = Vector.Switch(axis == 1, z_axis, y_axis)
        rot.switch(axis == 1, y_rot)

        geo = Mesh(geo)
        geo[selection].position = pivot + rot @ (nd.position - pivot)

        geo.out()

    # ====================================================================================================
    # Subdivide a block
    # ====================================================================================================

    with GeoNodes("Divide Block", is_group=False, rebuild=rebuild):

        geo = Geometry()
        block_name = String("Block", "Block Name")
        suffix = String("Part", "Name Suffix")

        is_vert = Boolean.MenuSwitch(
            {"Vertical": True, "Horizontal": False},
            menu=Input("Orientation", optional_label=True, expanded=True))
        count = Integer(1, "Count", 0, 10)
        even = Boolean(True, "Even")
        plank_name = String("Plank", "Plank")
        create_planks = plank_name.length() > 0
        half_thickness = G().get_resource(geo, plank_name=plank_name).thickness / 2
        half_thickness.switch_false(create_planks)

        props = G().get_block_properties(geo, block_name=block_name, dims='Inner').node

        x, y, z = props.inner_location.xyz
        sx, sy, sz = props.inner_size.xyz
        total = Float.Switch(is_vert, sy, sz)
        origin = Float.Switch(is_vert, y, z)

        line = Mesh.Line(count=10)
        for i in range(10):
            size = Float.Distance(0.3, f"Size {i}", 0.1).clamp(0, total)
            line[nd.index == i].position = (size, 0, 0)

        for rep in repeat(count, geo=geo, pos=0.0, stop=False):
            size = line.points.sample_index(nd.position.x, index=rep.iteration)
            target = (rep.pos + size).min(total)
            # Offset separator centers so every compartment has the same inner size.
            even_target = (rep.iteration + 1) * (total + 2 * half_thickness) / count.max(1)
            target.switch(even, (even_target - half_thickness).clamp(0, total))
            first = rep.iteration == 0
            at_end = target >= total

            sub_name = String.Join(block_name, suffix, rep.iteration.to_string(), delimiter=" ")
            bounds = {}

            for prefix, parent_location, parent_size, inset in (
                ("", props.block_location, props.block_size, 0),
                ("Inner ", props.inner_location, props.inner_size, half_thickness),
                ("Outer ", props.outer_location, props.outer_size, -half_thickness),
            ):
                px, py, pz = parent_location.xyz
                psx, psy, psz = parent_size.xyz
                parent_start = Float.Switch(is_vert, py, pz)
                parent_end = parent_start + Float.Switch(is_vert, psy, psz)
                start = Float.Switch(first, origin + rep.pos + inset, parent_start)
                end = Float.Switch(at_end, origin + target - inset, parent_end)
                sub_size = (end - start).max(0)

                bounds[prefix + "Location"] = Vector((
                    px,
                    Float.Switch(is_vert, start, py),
                    Float.Switch(is_vert, pz, start),
                ))
                bounds[prefix + "Size"] = Vector((
                    psx,
                    Float.Switch(is_vert, sub_size, psy),
                    Float.Switch(is_vert, psz, sub_size),
                ))

            thickness = 2 * half_thickness
            bounds["Left Thickness"] = Float.Switch(
                is_vert, Float.Switch(first, thickness, props.left_thickness), props.left_thickness,
            )
            bounds["Right Thickness"] = Float.Switch(
                is_vert, Float.Switch(at_end, thickness, props.right_thickness), props.right_thickness,
            )
            bounds["Bottom Thickness"] = Float.Switch(
                is_vert, props.bottom_thickness, Float.Switch(first, thickness, props.bottom_thickness),
            )
            bounds["Top Thickness"] = Float.Switch(
                is_vert, props.top_thickness, Float.Switch(at_end, thickness, props.top_thickness),
            )

            bundle, block_id = new_block_id(rep.geo.get_bundle())
            bundle.set_item("Blocks/" + sub_name, Bundle.Combine({
                "ID": block_id,
                "On Plinth": Boolean(False),
                **bounds,
                "Cuts": Bundle(),
            }))
            created = Geometry(rep.geo)
            created.set_bundle(bundle)

            with Layout("Shared Plank"):
                vertical_plank = G().create_plank(
                    created, plank_name=plank_name, width=sx, length=sz, setup='Flank',
                )
                horizontal_plank = G().create_plank(
                    created, plank_name=plank_name, width=sx, length=sy, setup='Shelf',
                )
                left_plank = Mesh(Mesh.Switch(is_vert, vertical_plank, horizontal_plank))
                left_plank.offset = Vector.Switch(
                    is_vert,
                    (x, origin + rep.pos - half_thickness, z),
                    (x, y, origin + rep.pos - half_thickness),
                )
                left_plank.points.set("Block ID", block_id)
                left_plank.points.set("Role", Integer.Switch(is_vert, ROLE_LEFT, ROLE_BOTTOM))

                bundle, planks = add_plank(
                    created.get_bundle(), sub_name, None, left_plank, first.bnot(),
                )
                bundle, seed = new_seed(bundle)
                uv_offset = Vector.Random(
                    (-10, -10, 0), (10, 10, 0), seed=seed,
                    id=nd.mesh_island().island_index,
                )
                planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)

                with_plank = created + planks
                with_plank.set_bundle(bundle)

                created.switch(create_planks, with_plank)


            rep.geo.switch_false(rep.stop, created)
            rep.pos = target
            rep.stop = rep.stop | at_end

        geo = rep.geo
        geo.out()

    # ====================================================================================================
    # A Drawer
    # ====================================================================================================

    with GeoNodes("Create Drawer Box", is_group=True, rebuild=rebuild):

        SIDE_MARGIN = 0.02
        BOT_MARGIN = 0.01
        TOP_MARGIN = 0.015
        THICK = 0.015

        width = Float.Distance(0.6, "Width", 4*THICK, 1.0, shape="Single")
        height = Float.Distance(0.2, "Height", 4*THICK, 1.0, shape="Single")
        depth = Float.Distance(0.3, "Depth", 4*THICK, 1.0, shape="Single")
        mat = Material("Drawer", "Material")

        sx, sy, sz = depth, width - 2*SIDE_MARGIN, height - BOT_MARGIN - TOP_MARGIN

        drawer = Mesh.Cube(size=(sx, sy, sz))
        
        cube = Mesh.Cube(size=(sx - 2*THICK, sy-2*THICK, sz))
        cube.offset = (0, 0, THICK)

        drawer -= cube
        drawer.offset = (-depth/2, width/2, height/2)
        drawer.faces.material = mat

        drawer.points.set("Block ID", 0)

        drawer.out("Mesh")

    # ====================================================================================================
    # Open a Drawer
    # ====================================================================================================

    with GeoNodes("Open Drawer", rebuild=rebuild):

        geo = Mesh(Geometry())

        selection = G().select_plank(
            geo,
            role='Drawer', 
            all=False).link_inputs()
        factor = Float.Factor(0.5, "Factor", 0, 1)

        dim_node = Mesh(geo).points[selection].attribute_statistic(nd.position).node

        _, sy, sz = (dim_node.max - dim_node.min).xyz

        block_size = G().get_block_properties(geo, block_name=selection.block_name, dims='Inner').size
        sx = block_size.x
        drawer_box = G().create_drawer_box(width=sy, height=sz, depth=sx).link_inputs()

        drawer_box.offset = dim_node.min

        open_offset = (factor.interpolate(0, sx - 0.02), 0, 0)
        drawer_box.offset = open_offset
        geo[selection].offset = open_offset

        geo += drawer_box
        geo.out()

    # ====================================================================================================
    # Change plank material
    # ====================================================================================================

    with GeoNodes("Change Plank Material", rebuild=rebuild):
        geo = Mesh(Geometry())
        selection = G().select_plank(geo).link_inputs()
        material = Material("Furniture", "Material")
        color = Color(DEFAULT_FURNITURE_COLOR, "Color")

        geo.faces[selection].material = material
        geo.faces[selection].set("Color", color)
        geo.out()

    # ====================================================================================================
    # Replace planks
    # ====================================================================================================

    with GeoNodes("Replace Plank", rebuild=rebuild):
        geo = Geometry()
        bundle = geo.get_bundle()
        selection = G().select_plank(geo).link_inputs()

        use_geometry = Boolean.MenuSwitch(
            {"Objet": False, "Geometry": True},
            menu=Input("Source", hide_in_modifier=True, optional_label=True, expanded=True),
        )
        obj = Object(name="Object")
        replacement_geometry = Geometry(name="Replacement Geometry")
        replacement = Geometry.Switch(use_geometry, obj.info().geometry, replacement_geometry)
        replacement = replacement.realize()
        replacement_bounds = replacement.bounding_box()
        replacement_size = replacement_bounds.max_ - replacement_bounds.min_
        selection = selection & (Mesh(replacement_bounds).points.count > 0)

        planks = Mesh(Mesh(geo).points[selection].separate())
        remaining = planks.inverted
        instances = planks.points.split_to_instances(group_id=Integer("Index"))

        for plank in instances.insts.for_each():
            original = Mesh(Instances(plank.element).realize())
            bounds = original.points.attribute_statistic(nd.position)
            target_size = bounds.max_ - bounds.min_
            scale = Vector(tuple(
                Float.Switch(abs(source_size) > 1e-8, 1, target / source_size)
                for source_size, target in zip(replacement_size.xyz, target_size.xyz)
            ))

            resized = Geometry(replacement)
            resized.transform(translation=-replacement_bounds.min_)
            resized.transform(scale=scale, translation=bounds.min_)
            resized = Mesh(resized)
            for attribute in ("Block ID", "Role", "Index"):
                resized.points.set(attribute, original.points.sample_index(Integer(attribute), index=0))
            plank.geometry = resized

        geo = remaining + plank.generated
        geo.set_bundle(bundle)
        geo.out()

    # ====================================================================================================
    # Delete planks
    # ====================================================================================================

    with GeoNodes("Delete Plank", rebuild=rebuild):
        geo = Mesh(Geometry())
        bundle = geo.get_bundle()
        selection = G().select_plank(geo).link_inputs()
        geo.points[selection].delete()
        geo.set_bundle(bundle)
        geo.out()

    # ====================================================================================================
    # Block dimensions and positions
    # ====================================================================================================

    with GeoNodes("Add Cotes", rebuild=rebuild):
        geo = Geometry()
        block = G().get_block_properties(geo).link_inputs().node

        with Panel("Origin"):
            origin = Vector(tuple(get_location(geo, axis) for axis in "XYZ"))

        with Panel("Aspect"):
            font_size = Float(0.1, "Font Size", 0.01)
            section = Float(0.01, "Section", 0)

        for axis, axis_name, dimension_name in ((0, "X", "Depth"), (1, "Y", "Width"), (2, "Z", "Height")):
            with Panel(axis_name, create_layout=True):
                show_dimension = Boolean(False, dimension_name)
                show_location = Boolean(False, "Location " + axis_name)
                invert = Boolean(False, "Invert")

                geo = G().add_cote_line(
                    geo, show=show_dimension & block.exists,
                    position=block.location, axis=axis, value=block.size.xyz[axis],
                    invert=invert, font_size=font_size, section=section,
                    cote_offset_a=Float(0, "Dimension Offset A", hide_in_modifier=True),
                    cote_offset_b=Float(0, "Dimension Offset B", hide_in_modifier=True),
                )
                geo = G().add_cote_line(
                    geo, show=show_location & block.exists,
                    position=origin, axis=axis,
                    value=block.location.xyz[axis] - origin.xyz[axis],
                    invert=invert, font_size=font_size, section=section,
                    cote_offset_a=Float(0, "Location Offset A", hide_in_modifier=True),
                    cote_offset_b=Float(0, "Location Offset B", hide_in_modifier=True),
                )

        geo.out()

    # ====================================================================================================
    # Cut Sheet
    # ====================================================================================================

    with GeoNodes("Cut Sheet", rebuild=rebuild):

        obj = Object(None, "Furniture")
        geo = obj.info().geometry
        bundle = geo.get_bundle()
        
        with Layout("Object width Resource ID / Resource Name"):
            for i in range(2):
                label = "1 : Plank" if i == 0 else "2 : Shelf"
                label_curve = Curve(String(label).to_curves(size=0.1).realize()).fill()
                label_curve.offset = 0, i*(-0.2), 0
                if i == 0:
                    labels = label_curve
                else:
                    labels += label_curve
                

            with Layout("Resource names"):
                res_bundle = bundle.get_item("Resources", socket_type='BUNDLE')
                
                paths = res_bundle.get_nested_paths(
                    mode = "Data Type",
                    data_type = "String",
                    )
                    
                res_count = paths.list_length()
                for rep in repeat(res_count, labels=labels, offset=-0.4):
                    path = paths[rep.iteration]

                    res_name = res_bundle.get_item(path, socket_type="STRING")
                    is_predef = (res_name == "Plank") | (res_name == "Shelf")
                    res_id = res_bundle.get_item(path.replace("Plank Name", "ID"), socket_type="INTEGER")
                    
                    label = res_id.to_string() + " : "
                    label += res_bundle.get_item(path, socket_type="STRING")
                    
                    label_curve = Curve(label.to_curves(size=0.1).realize()).fill()
                    label_curve.offset = 0, rep.offset, 0
                    
                    rep.labels += label_curve.switch(is_predef)
                    rep.offset += Float.Switch(is_predef, -0.2)
                    
                labels = Mesh(rep.labels)

            with Layout("Block names"):
                blocks = bundle.get_item("Blocks", socket_type='BUNDLE')
                paths = blocks.get_nested_paths(mode="Data Type", data_type="Integer")
                column_x = labels.points.attribute_statistic(nd.position).node.max.x + 0.3

                # Each block has one ID; ignore integer fields inside its cuts.
                for rep in repeat(paths.list_length(), labels=labels, offset=0.0):
                    path = paths[rep.iteration]
                    is_block = path.slice(position=path.length() - 3) == "/ID"
                    block_name = path.slice(position=0, length=path.length() - 3)
                    label_curve = Curve(block_name.to_curves(size=0.1).realize()).fill()
                    label_curve.offset = column_x, rep.offset, 0
                    rep.labels += label_curve.switch_false(is_block)
                    rep.offset -= Float.Switch(is_block, 0, 0.2)

                labels = Mesh(rep.labels)
            
            with Layout("Cuts per resource name"):
                res_bundle = bundle.get_item("Blocks", socket_type='BUNDLE')
                
                paths = res_bundle.get_nested_paths(
                    mode = "Data Type",
                    data_type = "Bundle"
                    )
                    
                for rep in repeat(paths.list_length(), cloud_pts=Cloud.Points(count=0)):
                    
                    path = paths[rep.iteration]
                    
                    cuts_bundles = res_bundle.get_item(path, socket_type="BUNDLE")
                    
                    for rep_cut in repeat(cuts_bundles.list_length(), cloud_pts=rep.cloud_pts):
                        
                        cut = cuts_bundles[rep_cut.iteration]
                        cut_node = cut.separate(signature=CUT_SIG)
                        
                        pt = Cloud.Points(count=1)
                        pt.set("Res ID", cut_node.res_id)
                        pt.set("Count", cut_node.count)
                        pt.set("Size", cut_node.size)
                        pt.set("Orient", cut_node.orient)
                        
                        rep_cut.cloud_pts += pt
                        
                    rep.cloud_pts = rep_cut.cloud_pts
                    
                cloud_pts = rep.cloud_pts
                    
        
            (labels + cloud_pts).out()

    
