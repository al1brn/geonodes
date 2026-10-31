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


furniture = Package("Furniture")


# ====================================================================================================
# Shaders
# ====================================================================================================

@furniture.shader_material('Furniture')
def furniture_material():
    color = snd.attribute(
        attribute_type='GEOMETRY', attribute_name="Color",
    ).color
    Shader.Principled(
        base_color=color,
        roughness=0.25,
        metallic=0.0,
    ).out()

@furniture.shader_material('Debug Block')
def debug_block_material():
    debug_color = snd.attribute(
        attribute_type='GEOMETRY', attribute_name="Debug Block Color",
    ).color
    debug_opacity = snd.attribute(
        attribute_type='GEOMETRY', attribute_name="Debug Block Opacity",
    ).factor
    shader = Shader.Principled(base_color=debug_color, roughness=0.5)
    shader.mix(shader=Shader.Transparent(), factor=1 - debug_opacity).out()

@furniture.shader_material('Drawer')
def drawer_material():
    Shader.Principled(
        base_color="#F2F2F2FF",
        roughness=0.65,
        metallic=0.0,
    ).out()


@furniture.shader_material('Label')
def label_material():
    Shader.Principled(
        base_color=snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").color,
        roughness=0.9,
    ).out()

# ====================================================================================================
# A dimension line
# ====================================================================================================

@furniture.geo_group('Add Cote Line')
def add_cote_line():

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
    "Name": String,
    "Type": Integer,  # -1: Root, 0: construction, 1: decoration, 2: inactive
    "Parent Block ID": Integer,
    "Decoration Mode": Integer,
    "Deco Index": Integer,
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

def get_blocks(bundle):
    blocks = Bundle(bundle).get_item("Blocks", socket_type='BUNDLE', structure_type='LIST')
    root = Bundle.Combine({
        "Name": String("Root"),
        "Type": Integer(-1),
        "Parent Block ID": Integer(0),
        "Decoration Mode": Integer(0),
        "Deco Index": Integer(0),
        "On Plinth": Boolean(False),
        **{prefix + "Location": Vector(0) for prefix in ("", "Inner ", "Outer ")},
        **{prefix + "Size": Vector(0) for prefix in ("", "Inner ", "Outer ")},
        **{side + " Thickness": Float(0) for side in ("Left", "Right", "Bottom", "Top")},
        "Cuts": Bundle(),
    })
    root_list = Bundle.List(root)
    blocks.switch_false(blocks.exists, root_list)
    blocks.switch(blocks.list_length() == 0, root_list)
    return blocks

@furniture.geo_group('.Block Index')
def _block_index():
    bundle = Bundle(name="Bundle")
    name = String("Block", "Name")
    blocks = get_blocks(bundle)
    for search in repeat(blocks.list_length(), index=-1):
        matches = blocks[search.iteration].get_item("Name", socket_type='STRING') == name
        search.index.switch(matches, search.iteration)
    search.index.out("Index")

def block_index(bundle, name):
    return _block_index(bundle=bundle, name=name)

def set_block(bundle, block_id, block):
    blocks = get_blocks(bundle)
    with Closure() as replacement:
        index = Integer(0, "Index")
        Bundle.Switch(index == block_id, blocks[index], block).out("Block")
    bundle.set_item("Blocks", replacement.to_list(blocks.list_length()), structure_type='LIST')
    return bundle

def store_named_block(bundle, name, block):
    index = block_index(bundle, name)
    block = Bundle(block)
    block.set_item("Name", name)
    appended = get_blocks(bundle)
    appended.list_append(block)
    updated = set_block(Bundle(bundle), index, block)
    added = Bundle(bundle)
    added.set_item("Blocks", appended, structure_type='LIST')
    bundle.switch(index >= 0, updated)
    bundle.switch(index < 0, added)
    return bundle

def transform_decoration_blocks(bundle, parent_id, transform, use_size=True):
    blocks = get_blocks(bundle)
    for child in repeat(blocks.list_length(), bundle=bundle):
        block = blocks[child.iteration]
        matches = block.get_item("Type", socket_type='INTEGER') == 1
        matches &= block.get_item("Parent Block ID", socket_type='INTEGER') == parent_id
        updated_block = Bundle(block)
        for prefix in ("", "Inner ", "Outer "):
            location = block.get_item(prefix + "Location", socket_type='VECTOR')
            size = block.get_item(prefix + "Size", socket_type='VECTOR') if use_size else None
            updated_block.set_item(prefix + "Location", transform(location, size))
        updated = set_block(Bundle(child.bundle), child.iteration, updated_block)
        child.bundle.switch(matches, updated)
    return child.bundle

def get_resources(bundle):
    resources = Bundle(bundle).get_item("Resources", socket_type='BUNDLE', structure_type='LIST')
    resources.switch_false(resources.exists)
    return resources

def default_resource():
    return Bundle.Combine({
        "Name": String("Default"),
        "Width": Float(0.6),
        "Length": Float(2.5),
        "Thickness": Float(0.018),
        "Material": Material("Furniture"),
        "Color": Color(DEFAULT_FURNITURE_COLOR),
    })

@furniture.geo_group('.Resource Index')
def _resource_index():
    bundle = Bundle(name="Bundle")
    name = String("Default", "Name")
    resources = get_resources(bundle)
    for search in repeat(resources.list_length(), index=-1):
        matches = resources[search.iteration].get_item("Name", socket_type='STRING') == name
        search.index.switch(matches, search.iteration)
    search.index.out("Index")

def resource_index(bundle, name):
    return _resource_index(bundle=bundle, name=name)

# ====================================================================================================
# Named Dimensions
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Define 5 named dimensions
# ----------------------------------------------------------------------------------------------------

@furniture.geo_modifier('Define Named Dimensions')
def define_named_dimensions():
    
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
    
@furniture.geo_group('Get Named Dimension')
def get_named_dimension():
    
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

@furniture.geo_modifier('Define Resource')
def define_resource():
    
    geo = Geometry()
    bundle = geo.get_bundle()

    new_name = String("Default", "New Name")
    
    width = Float.Distance(0.35, "Width", 0.1, 3.0)
    length = Float.Distance(3.0, "Length", 0.1, 3.0)
    thickness = Float.Distance(0.018, "Thickness", 0.001, 0.2)
    mat = Material("Furniture", "Material")
    col = Color(DEFAULT_FURNITURE_COLOR, "Color")

    resources = get_resources(bundle)
    index = resource_index(bundle, new_name)

    res_bundle = Bundle.Combine({
        "Name": new_name,
        "Width": width,
        "Length" : length,
        "Thickness" : thickness,
        "Material" : mat,
        "Color" : col,
    })

    with Closure() as replacement:
        i = Integer(0, "Index")
        Bundle.Switch(i == index, resources[i], res_bundle).out("Resource")
    updated = Bundle(replacement.to_list(resources.list_length()))
    appended = Bundle(resources)
    appended.list_append(res_bundle)
    resources = Bundle.Switch(index < 0, updated, appended)
    bundle.set_item("Resources", resources, structure_type='LIST')
    nd.set_geometry_bundle(bundle=bundle).out()

# ----------------------------------------------------------------------------------------------------
# Get resource
# ----------------------------------------------------------------------------------------------------

@furniture.geo_group('Get Resource')
def get_resource():
    geo = Geometry()
    use_id = Boolean(False, "By ID")
    plank_name = String("Default", "Plank Name")
    pid = Integer(0, "Plank ID", 0)
    bundle = geo.get_bundle()
    resources = get_resources(bundle)
    count = resources.list_length()
    fallback_index = resource_index(bundle, String("Default")).max(0)
    named_index = resource_index(bundle, plank_name)
    valid_id = (pid >= 0) & (pid < count)
    by_name = Integer.Switch(named_index >= 0, fallback_index, named_index)
    by_id = Integer.Switch(valid_id, fallback_index, pid)
    index = Integer.Switch(use_id, by_name, by_id)
    selected = Bundle.Switch(count == 0, resources[index], default_resource())
    selected.set_item("Plank Name", selected.get_item("Name", socket_type='STRING'))
    selected.set_item("ID", index)

    missing_name = (plank_name != "Default") & (named_index < 0)
    missing_id = valid_id.bnot() & ((count > 0) | (pid != 0))
    missing = Boolean.Switch(use_id, missing_name, missing_id)
    message = String.Switch(
        use_id,
        "Resource '" + plank_name + "' not found",
        "Resource ID " + pid.to_string() + " not found",
    )
    missing.warning(message)
    selected.separate(signature=RES_SIG).out()

# ----------------------------------------------------------------------------------------------------
# Define plinth dimensions
# ----------------------------------------------------------------------------------------------------

@furniture.geo_modifier('Define Plinth')
def define_plinth():
    geo = Geometry()
    bundle = geo.get_bundle()
    plank_name = String("Default", "Plank Name")
    resource_id = get_resource(geo, plank_name=plank_name).id

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

@furniture.geo_group('.Get Plinth Dimensions')
def _get_plinth_dimensions():
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
    resource_id.switch_false(exists, get_resource(geo).id)
    resource_id.out("Resource ID")

    missing.warning("Use 'Define Plinth' to define plinth dimensions.")

# ----------------------------------------------------------------------------------------------------
# Capture resources from another object
# ----------------------------------------------------------------------------------------------------

def merge_resources(bundle, incoming, replace_existing):
    for resource in repeat(
        incoming.list_length(), bundle=bundle, mapping=Integer(0).to_list(count=0),
    ):
        candidate = incoming[resource.iteration]
        name = candidate.get_item("Name", socket_type='STRING')
        index = resource_index(resource.bundle, name)
        current = get_resources(resource.bundle)
        target = Integer.Switch(index >= 0, current.list_length(), index)
        with Closure() as replacement:
            i = Integer(0, "Index")
            Bundle.Switch(i == index, current[i], candidate).out("Resource")
        replaced = Bundle(replacement.to_list(current.list_length()))
        appended = Bundle(current)
        appended.list_append(candidate)
        merged = Bundle.Switch(index < 0, current, appended)
        merged.switch((index >= 0) & replace_existing, replaced)
        updated = Bundle(resource.bundle)
        updated.set_item("Resources", merged, structure_type='LIST')
        resource.bundle = updated
        resource.mapping.list_append(target)
    return resource.bundle, resource.mapping

def existing_resources_input():
    return Boolean.MenuSwitch(
        {"Keep": False, "Replace": True},
        menu=Input("Existing", default="Keep", optional_label=True, expanded=True),
    )

@furniture.geo_modifier('Capture Resources')
def capture_resources():
    geo = Geometry()
    source = Object(name="Object")
    replace_existing = existing_resources_input()
    incoming = get_resources(source.info().geometry.get_bundle())
    bundle, _ = merge_resources(geo.get_bundle(), incoming, replace_existing)
    nd.set_geometry_bundle(bundle=bundle).out()

# ====================================================================================================
# Create Plank From Resource
# ====================================================================================================

def add_cut_sheet(bundle, block_name, cut_bundle):

    with Layout("Add Cut Sheet"):

        cut_node = cut_bundle.separate(signature=CUT_SIG)
        ok = cut_node.count > 0

        index = block_index(bundle, block_name)
        block = get_blocks(bundle)[index]
        cuts_path = "Cuts/" + cut_node.plank_name
        cuts = block.get_item(cuts_path, socket_type="BUNDLE", structure_type="LIST")
        cuts.switch_false(cuts.exists)
        cuts.list_append(cut_bundle)
        block.set_item(cuts_path, cuts)
        updated = set_block(Bundle(bundle), index, block)
        bundle.switch(ok, updated)

        return bundle

# ----------------------------------------------------------------------------------------------------
# Create a Single Plank
# ----------------------------------------------------------------------------------------------------

@furniture.geo_group('Create Plank')
def create_plank():
    
    geo = Geometry()
    
    res_node = get_resource(geo).link_inputs().node
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
        
        plank.points.set("Res ID", res_node.id)
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

@furniture.geo_group('Create Faces')
def create_faces():
    
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
    
    plank = create_plank(geo, width=wy, length=lz, setup='Door').link_inputs()
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

@furniture.geo_group('Create Shelves')
def create_shelves():
    
    geo = Geometry()
    
    height = Float.Distance(1.0, "Height")
    z = Float.Distance(0.1, "Z")
    count = Integer(0, "Count", 0)
    
    width = Float.Distance(0.45, "Width", 0.1, 3)
    depth = Float.Distance(0.28, "Depth", 0.1, 3)
    backset = Float.Distance(0.01, "Backset", 0, 0.1)
    
    plank = create_plank(geo, width=depth - backset, length=width, setup='Shelf').link_inputs()
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

@furniture.geo_group('Create Separators')
def create_separators():
    
    geo = Geometry()
    
    height = Float.Distance(1.0, "Height")
    y = Float.Distance(0.1, "Y", 0)
    count = Integer(0, "Count", 0)
    
    width = Float.Distance(0.45, "Width", 0.1, 3)
    depth = Float.Distance(0.28, "Depth", 0.1, 3)
    backset = Float.Distance(0.01, "Backset", 0, 0.1)
    
    plank = create_plank(geo, width=depth - backset, length=height, setup='Flank').link_inputs()
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
    return block_index(geo.get_bundle(), block_name) >= 0

# ----------------------------------------------------------------------------------------------------
# All properties
# ----------------------------------------------------------------------------------------------------

@furniture.geo_group('Get Block Properties')
def get_block_properties():
    
    geo = Geometry()
    block_name, block_dims = block_input("Block")
    #block_name = String("Block", "Block Name")
    
    blocks = get_blocks(geo.get_bundle())
    block_id = block_index(geo.get_bundle(), block_name)
    bundle = blocks[block_id]
    exists = block_id >= 0
    nope = exists.bnot()

    nope.warning("Block '" + block_name + "' not found.")

    node = bundle.separate(signature=BLOCK_SIG)

    block_id = Integer.Switch(nope, block_id, -1)

    location = node.location.switch(nope)
    size = node.size.switch(nope)
    inner_location = node.inner_location.switch(nope)
    inner_size = node.inner_size.switch(nope)
    outer_location = node.outer_location.switch(nope)
    outer_size = node.outer_size.switch(nope)
    
    cuts = node.cuts.switch(nope)

    exists.out("Exists")

    node.type.out("Type")
    node.parent_block_id.out("Parent Block ID")
    node.decoration_mode.out("Decoration Mode")
    node.deco_index.out("Deco Index")

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

@furniture.geo_group('Get Block Property')
def get_block_property():
    
    geo = Geometry()

    node = get_block_properties(geo).link_inputs().node
    
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

def ui_location_value(geo, with_plinth=False, return_plinth=False, axis="All"):
    choices = {"Value": 0, "Block": 1, "Name": 2}
    if with_plinth:
        choices["Plinth"] = 3

    index = Integer.MenuSwitch(
        choices, 
        menu=Input("Def", optional_label=True, expanded=True))
        
    block_name = String("Block", "Block Name")
    prop = get_block_property(
        geo, 
        block_name=block_name, 
        dims=Input("Dims", optional_label=True, expanded=True), 
        axis=axis,
        **{("property" if axis == "All" else "property_" + axis.lower()): Input("Prop")})
    
    named = get_named_dimension(geo, name=Input("Name"))
    offset = Float.Distance(0, "Offset")

    values = [0, prop, named]
    if with_plinth:
        values.append(_get_plinth_dimensions(geo).height)

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
            geo,
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

        value = ui_location_value(geo, axis={"Size X": "X", "Size Y": "Y", "Size Z": "Z"}.get(name, "All"))
        value.switch(rel_incr, value - base)

        return value

# ====================================================================================================
# Add an external furniture module
# ====================================================================================================

@furniture.geo_modifier('Add External Block')
def add_external_block():
    geo = Geometry()
    use_geometry = Boolean.MenuSwitch(
        {"Object": False, "Geometry": True},
        menu=Input("Source", optional_label=True, expanded=True),
    )
    obj = Object(None, "Furniture")
    source_geometry = Geometry(name="Source Geometry")
    furniture = Geometry.Switch(use_geometry, obj.info().geometry, source_geometry)
    source_block = String("Block", "Source Block")
    source_properties = get_block_properties(
        furniture, block_name=source_block, dims='Block',
    ).node
    with Panel("Location"):
        location = Vector(tuple(get_location(geo, axis) for axis in "XYZ"))
    translation = location - source_properties.block_location
    replace_existing = existing_resources_input()
    local_bundle = geo.get_bundle()
    source_bundle = furniture.get_bundle()
    local_blocks = get_blocks(local_bundle)
    incoming_blocks = get_blocks(source_bundle)
    block_offset = local_blocks.list_length() - 1

    with Layout("Merge resources"):
        # Materialize implicit resources before their indices change meaning.
        local_resources = get_resources(local_bundle)
        local_resources.switch(
            (local_resources.list_length() == 0) & (local_blocks.list_length() > 1),
            Bundle.List(default_resource()),
        )
        local_bundle.set_item("Resources", local_resources, structure_type='LIST')
        incoming = get_resources(source_bundle)
        incoming.switch(incoming.list_length() == 0, Bundle.List(default_resource()))
        merged_bundle, resource_map = merge_resources(local_bundle, incoming, replace_existing)

    with Layout("Append imported blocks"):
        for imported in repeat(incoming_blocks.list_length() - 1, blocks=local_blocks):
            block = Bundle(incoming_blocks[imported.iteration + 1])
            for prefix in ("", "Inner ", "Outer "):
                position = block.get_item(prefix + "Location", socket_type='VECTOR')
                block.set_item(prefix + "Location", position + translation)
            parent = block.get_item("Parent Block ID", socket_type='INTEGER')
            block.set_item("Parent Block ID", Integer.Switch(parent > 0, parent, parent + block_offset))
            cuts = block.get_item("Cuts", socket_type='BUNDLE')
            paths = cuts.get_nested_paths(mode="Data Type", data_type="Bundle")
            for resource in repeat(paths.list_length(), cuts=cuts):
                path = paths[resource.iteration]
                entries = cuts.get_item(path, socket_type='BUNDLE', structure_type='LIST')
                with Closure() as remap:
                    index = Integer(0, "Index")
                    entry = Bundle(entries[index])
                    old_id = entry.get_item("Res ID", socket_type='INTEGER')
                    entry.set_item("Res ID", resource_map[old_id])
                    entry.out("Entry")
                updated = Bundle(resource.cuts)
                updated.set_item(path, remap.to_list(entries.list_length()), structure_type='LIST')
                resource.cuts = updated
            block.set_item("Cuts", resource.cuts)
            imported.blocks.list_append(block)

    with Layout("Remap geometry references"):
        plank_offset = Integer(Mesh(geo).points.attribute_statistic(Integer("Plank ID")).max_)
        # Store attributes without realizing decoration instances.
        mesh = Mesh(furniture)
        for attribute in ("Block ID", "Support Block ID"):
            old_id = Integer(attribute)
            mesh.points[old_id > 0].set(attribute, old_id + block_offset)
        old_plank = Integer("Plank ID")
        mesh.points[old_plank > 0].set("Plank ID", old_plank + plank_offset)
        old_resource = Integer("Res ID")
        mesh.points[old_resource.exists].set("Res ID", resource_map[old_resource])
        # Apply the selected destination resources to imported boards.
        resources = get_resources(merged_bundle)
        for material in repeat(resources.list_length(), mesh=mesh):
            resource = resources[material.iteration]
            boards = Mesh(material.mesh)
            reference = Integer("Res ID")
            selection = reference.exists & (reference == material.iteration)
            boards.faces[selection].material = resource.get_item("Material", socket_type='MATERIAL')
            boards.faces[selection].set("Color", resource.get_item("Color", socket_type='RGBA'))
            material.mesh = boards
        mesh = Mesh(material.mesh)
        instances = Instances(mesh)
        for attribute in ("Block ID", "Support Block ID"):
            old_id = Integer(attribute)
            instances.insts[old_id > 0].set(attribute, old_id + block_offset)
        old_plank = Integer("Plank ID")
        instances.insts[old_plank > 0].set("Plank ID", old_plank + plank_offset)
        old_resource = Integer("Res ID")
        instances.insts[old_resource.exists].set("Res ID", resource_map[old_resource])

    # Import named parameters without discarding unrelated local parameters.
    result_bundle = Bundle(merged_bundle)
    source_names = source_bundle.get_item("Names", socket_type='BUNDLE')
    local_names = local_bundle.get_item("Names", socket_type='BUNDLE')
    parameters = source_names.get_nested_paths(mode="Data Type", data_type="Float")
    for parameter in repeat(parameters.list_length(), names=local_names):
        path = parameters[parameter.iteration]
        updated = Bundle(parameter.names)
        updated.set_item(path, Bundle(source_names).get_item(path, socket_type='FLOAT'))
        parameter.names = updated
    source_plinth = source_names.get_item("Plinth Resource ID", socket_type='INTEGER')
    names = Bundle(parameter.names)
    with_plinth = Bundle(names)
    with_plinth.set_item("Plinth Resource ID", resource_map[source_plinth])
    names.switch(source_plinth.exists, with_plinth)
    result_bundle.set_item("Names", names)
    result_bundle.set_item("Blocks", imported.blocks, structure_type='LIST')
    imported_geometry = Geometry(instances)
    imported_geometry.transform(translation=translation)
    result = geo + imported_geometry
    result.set_bundle(result_bundle)
    result.out()

# ====================================================================================================
# Define Blocks
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Debug
# ----------------------------------------------------------------------------------------------------

@furniture.geo_modifier('Debug Block')
def debug_block():

    geo = Geometry()
    bundle = geo.get_bundle()
    #name = String("Block", "Name")
    block = get_block_properties(geo).link_inputs().node

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

def decoration_input(name):
    return Integer.MenuSwitch(
        {"No": 0, "Items": 1, "Compositions": 2},
        menu=Input(name, optional_label=True, expanded=True),
    )

def decoration_inputs():
    with Panel("Decoration"):
        return {
            name: decoration_input(name)
            for name in ("Bottom Deco", "Shelf Deco", "Top Deco")
        }

@furniture.geo_modifier('Define Block')
def define_block():
    
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

        block_bundle = Bundle.Combine({
            "On Plinth": on_plinth,
            "Type": Integer(0),
            "Parent Block ID": Integer(0),
            "Decoration Mode": Integer(0),
            "Deco Index": Integer(0),
            **{name: Integer(0) for name in ("Bottom Deco", "Shelf Deco", "Top Deco")},
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

        bundle = store_named_block(bundle, new_name, block_bundle)
        geo += block_frame

        geo.set_bundle(bundle)

    geo.out()

# ====================================================================================================
# Operations on blocks
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Duplicate block
# ----------------------------------------------------------------------------------------------------

@furniture.geo_modifier('.Block Duplicate')
def _block_duplicate():

    geo = Geometry()
    source = String("Source", "Source Name")
    target = String("Target", "Target Name")
    dupl_planks = Boolean(True, "Duplicate Planks")

    bundle = geo.get_bundle()

    with Layout("Copy Block"):
        source_id = block_index(bundle, source)
        source_bundle = get_blocks(bundle)[source_id]
        exists = source_id >= 0
        new_bundle = Bundle(bundle)
        new_id = get_blocks(bundle).list_length()
        target_bundle = Bundle(source_bundle)
        target_bundle.set_item("Name", target)
        new_bundle = store_named_block(new_bundle, target, target_bundle)
        bundle.switch(exists, new_bundle)

    with Layout("Duplicate decoration blocks"):
        source_blocks = get_blocks(bundle)
        for child in repeat(source_blocks.list_length(), bundle=bundle):
            original = source_blocks[child.iteration]
            matches = original.get_item("Type", socket_type='INTEGER') == 1
            matches &= original.get_item("Parent Block ID", socket_type='INTEGER') == source_id
            copied = Bundle(original)
            copied.set_item("Parent Block ID", new_id)
            child_name = String.Join(
                target, "Deco", original.get_item("Deco Index", socket_type='INTEGER').to_string(),
                delimiter=" ",
            )
            updated = store_named_block(Bundle(child.bundle), child_name, copied)
            child.bundle.switch(exists & matches, updated)
        bundle = child.bundle

    with Layout("Duplicate Planks"):

        max_plank_id = Integer(Mesh(geo).points.attribute_statistic(Integer("Plank ID")).max_)
        planks = Mesh(Mesh(geo).points[exists & (Integer("Block ID")==source_id)].separate())
        planks.points.set("Block ID", new_id)
        planks.points.set("Plank ID", Integer("Plank ID") + max_plank_id)

        # Randomize uv map
        new_bundle = Bundle(bundle)
        new_bundle, seed = new_seed(new_bundle)
        uv_offset = Vector.Random((-10, -10, 0), (10, 10, 0), seed=seed, id=nd.mesh_island().island_index)
        planks.corners.store_uv("UV Map", Vector("UV Map") + uv_offset)

        geo.switch(dupl_planks, geo + planks)
        bundle.switch(dupl_planks, new_bundle)

    geo.set_bundle(bundle)
    geo.out()
    exists.out("Exists")
    new_id.out("Block ID")

# ----------------------------------------------------------------------------------------------------
# Translate block
# ----------------------------------------------------------------------------------------------------

@furniture.geo_modifier('.Block Translate')
def _block_translate():

    geo = Geometry()
    block_name = String("Block", "Block Name")
    translation = Vector(0, "Translation")

    bundle = geo.get_bundle()

    with Layout("Translate Block"):

        block_id = block_index(bundle, block_name)
        source_bundle = get_blocks(bundle)[block_id]
        exists = block_id >= 0

        new_bundle = Bundle(bundle)

        props = source_bundle.separate(signature=BLOCK_SIG)



        target_bundle = Bundle(source_bundle)
        for name, location in (
            ("Location", props.location),
            ("Inner Location", props.inner_location),
            ("Outer Location", props.outer_location),
        ):
            target_bundle.set_item(name, location + translation)

        new_bundle = set_block(new_bundle, block_id, target_bundle)
        bundle.switch(exists, new_bundle)

        bundle = transform_decoration_blocks(
            bundle, block_id, lambda location, size: location + translation, use_size=False,
        )

    with Layout("Planks"):
        planks = Mesh(Mesh(geo).points[exists & (Integer("Block ID")==block_id)].separate())
        remain = planks.inverted
        planks.offset = translation

        geo = remain + planks

    geo.set_bundle(bundle)
    geo.out()

# ----------------------------------------------------------------------------------------------------
# Block symmetry
# ----------------------------------------------------------------------------------------------------

@furniture.geo_modifier('.Block Symmetry')
def _block_symmetry():

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
        block_id = block_index(bundle, block_name)
        source_bundle = get_blocks(bundle)[block_id]
        exists = block_id >= 0

        new_bundle = Bundle(bundle)

        props = source_bundle.separate(signature=BLOCK_SIG)



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

        new_bundle = set_block(new_bundle, block_id, sym_bundle)
        bundle.switch(exists, new_bundle)

        def mirror_decoration(location, size):
            x0, y0, z0 = location.xyz
            _, y1, z1 = (location + size).xyz
            return Vector.IndexSwitch(
                location, (x0, ys2 - y1, z0), (x0, y0, zs2 - z1), index=sym_index,
            )

        bundle = transform_decoration_blocks(bundle, block_id, mirror_decoration)

    with Layout("Planks"):

        planks = Mesh(Mesh(geo).points[exists & (Integer("Block ID") == block_id)].separate())
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

@furniture.geo_modifier('Duplicate Block')
def duplicate_block():

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

            dupl_geo = _block_duplicate(
                rep.geo,
                source_name = source_name,
                target_name = dupl_name,
                duplicate_planks = use_dupl_planks,
            )
            exists = dupl_geo.exists
            ((rep.iteration==0) & exists.bnot()).warning("Block '" + source_name + "' not found")

        with Layout("Translation"):
            new_geo = _block_translate(
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
        new_geo = _block_symmetry(
            geo,
            block_name = new_name,
            symmetry = 'Y',
            y_center = ys,
        )
        geo.switch(exists & (sym_index==1), new_geo)

    with Layout("Symmetry Z"):
        new_geo = _block_symmetry(
            geo,
            block_name = new_name,
            symmetry = 'Z',
            z_center = zs,
        )
        geo.switch(exists & (sym_index==2), new_geo)

    with Layout("Total Size"):
        block_dims = get_block_properties(geo, block_name=source_name, dims='Block').node
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
    
@furniture.geo_group('.Add Plank')
def _add_plank():
    existing_geometry = Geometry(name="Existing Geometry")
    bundle = Bundle(name="Bundle")
    block_name = String("Block", "Block Name")
    planks = Mesh(name="Planks")
    plank = Mesh(name="Plank")
    ok = Boolean(True, "Enabled")

    plank.switch_false(ok)
    cut = plank.get_bundle(remove=True)
    # New boards are connected mesh islands, including realized arrays.
    existing = Mesh(existing_geometry + planks)
    max_plank_id = Integer(existing.points.attribute_statistic(Integer("Plank ID")).max_)
    plank.points.set("Plank ID", max_plank_id + 1 + nd.mesh_island().island_index)
    planks += plank
    bundle.switch(ok, add_cut_sheet(Bundle(bundle), block_name, cut))

    planks.out("Planks")
    bundle.out("Bundle")

def add_plank(existing_geometry, bundle, block_name, planks, plank, ok):
    """Call the shared group that adds a plank and records its cut."""
    result = _add_plank(
        existing_geometry=existing_geometry,
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

@furniture.geo_modifier('Add Shelves')
def add_shelves():
    
    geo = Geometry()
    bundle = geo.get_bundle()

    block_name = String("Block", "Block Name")

    block_dims = get_block_properties(geo, block_name=block_name, dims='Inner').node

    x, y, z = block_dims.location.xyz
    sx, sy, sz = block_dims.size.xyz

    with Panel("Shelves", create_layout=True):
        
        shelves = create_shelves(
            geo,
            height = sz,
            width = sy,
            depth = sx,
        ).link_inputs()
        shelves.offset = (x, y, z)
        shelf_deco = decoration_input("Shelf Deco")

        bundle, planks = add_plank(geo, bundle, block_name, None, shelves, True)
        parent = get_blocks(bundle)[block_dims.id]
        parent.set_item("Shelf Deco", shelf_deco)
        bundle = set_block(bundle, block_dims.id, parent)
        planks = Mesh(planks)

    with Layout("Decoration blocks"):
        # Use the actual shelf bounds: a single shelf may have a custom Z.
        shelf_instances = planks.points.split_to_instances(group_id=Integer("Plank ID"))
        shelf_count = shelf_instances.insts.count
        original_bundle = Bundle(bundle)
        for compartment in repeat(shelf_count + 1, bundle=bundle, floor=z):
            next_shelf = Mesh(planks)
            next_shelf.points[Integer("Index") == compartment.iteration].separate()
            limits = next_shelf.points.attribute_statistic(nd.position).node
            last = compartment.iteration == shelf_count
            ceiling = Float.Switch(last, limits.min.z, z + sz)
            location = Vector((x, y, compartment.floor))
            size = Vector((sx, sy, (ceiling - compartment.floor).max(0)))
            updated = Bundle(compartment.bundle)
            name = String.Join(
                block_name, "Deco", compartment.iteration.to_string(), delimiter=" ",
            )
            updated = store_named_block(updated, name, Bundle.Combine({
                "Type": Integer(1),
                "Parent Block ID": block_dims.id,
                "Deco Index": compartment.iteration,
                "Decoration Mode": shelf_deco,
                "On Plinth": Boolean(False),
                **{prefix + "Location": location for prefix in ("", "Inner ", "Outer ")},
                **{prefix + "Size": size for prefix in ("", "Inner ", "Outer ")},
                **{side + " Thickness": Float(0) for side in ("Left", "Right", "Bottom", "Top")},
                "Cuts": Bundle(),
            }))
            compartment.bundle = updated
            compartment.floor = Float.Switch(last, limits.max.z, ceiling)
        bundle = Bundle(original_bundle)
        bundle.switch(block_dims.exists, compartment.bundle)

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

@furniture.geo_modifier('Add Separators')
def add_separators():
    
    geo = Geometry()
    bundle = geo.get_bundle()

    block_name = String("Block", "Block Name")

    block_dims = get_block_properties(geo, block_name=block_name, dims='Inner').node

    x, y, z = block_dims.location.xyz
    sx, sy, sz = block_dims.size.xyz

    with Panel("Separators", create_layout=True):
        
        separators = create_separators(
            geo,
            height = sz,
            width = sy,
            depth = sx,
        ).link_inputs()
        separators.offset = (x, y, z)
        separator_deco = decoration_input("Separator Deco")

        bundle, planks = add_plank(geo, bundle, block_name, None, separators, True)
        planks = Mesh(planks)

    with Layout("Subdivide decoration blocks"):
        original_bundle = Bundle(bundle)
        blocks = get_blocks(bundle)
        separator_count = planks.points.split_to_instances(group_id=Integer("Plank ID")).insts.count
        # Retain every slot. Volumes replaced by the new partition are disabled,
        # then reused by name; extra compartments are appended.
        for keep in repeat(blocks.list_length(), bundle=bundle, count=0):
            child = blocks[keep.iteration]
            matches = child.get_item("Type", socket_type='INTEGER') == 1
            matches &= child.get_item("Parent Block ID", socket_type='INTEGER') == block_dims.id
            inactive = Bundle(child)
            inactive.set_item("Type", Integer(2))
            updated = set_block(Bundle(keep.bundle), keep.iteration, inactive)
            keep.bundle.switch(matches & (separator_count > 0), updated)
            keep.count += Integer.Switch(matches, 0, 1)

        for volume in repeat(blocks.list_length() + 1, bundle=keep.bundle, count=0):
            fallback = volume.iteration == blocks.list_length()
            child = blocks[volume.iteration.min((blocks.list_length() - 1).max(0))]
            matches = child.get_item("Type", socket_type='INTEGER') == 1
            matches &= child.get_item("Parent Block ID", socket_type='INTEGER') == block_dims.id
            active = Boolean.Switch(fallback, matches, keep.count == 0)
            location = Vector.Switch(
                fallback, child.get_item("Location", socket_type='VECTOR'), block_dims.location,
            )
            size = Vector.Switch(
                fallback, child.get_item("Size", socket_type='VECTOR'), block_dims.size,
            )
            mode = Integer.Switch(
                fallback, child.get_item("Decoration Mode", socket_type='INTEGER'), separator_deco,
            )
            vx, vy, vz = location.xyz
            dx, dy, dz = size.xyz
            for part in repeat(
                separator_count + 1, bundle=volume.bundle, count=volume.count, left=vy,
            ):
                separator = Mesh(planks)
                separator.points[Integer("Index") == part.iteration].separate()
                limits = separator.points.attribute_statistic(nd.position).node
                last = part.iteration == separator_count
                right = Float.Switch(last, limits.min.y.clamp(vy, vy + dy), vy + dy)
                width = (right - part.left).max(0)
                valid = active & (width > 0) & block_dims.exists
                name = String.Join(block_name, "Deco", part.count.to_string(), delimiter=" ")
                part_location = Vector((vx, part.left, vz))
                part_size = Vector((dx, width, dz))
                updated = Bundle(part.bundle)
                updated = store_named_block(updated, name, Bundle.Combine({
                    "Type": Integer(1),
                    "Parent Block ID": block_dims.id,
                    "Deco Index": part.count,
                    "Decoration Mode": mode,
                    "On Plinth": Boolean(False),
                    **{prefix + "Location": part_location for prefix in ("", "Inner ", "Outer ")},
                    **{prefix + "Size": part_size for prefix in ("", "Inner ", "Outer ")},
                    **{side + " Thickness": Float(0) for side in ("Left", "Right", "Bottom", "Top")},
                    "Cuts": Bundle(),
                }))
                part.bundle.switch(valid, updated)
                part.count += Integer.Switch(valid, 0, 1)
                part.left = Float.Switch(last, limits.max.y.clamp(vy, vy + dy), right)
            volume.bundle = part.bundle
            volume.count = part.count
        bundle = Bundle(original_bundle)
        bundle.switch(block_dims.exists & ((separator_count > 0) | (keep.count == 0)), volume.bundle)

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

@furniture.geo_modifier('Add Face')
def add_face():

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

    block_dims = get_block_properties(geo, block_name=block_name).node

    with Layout("Configuration"): #("Panel", create_layout=True):
        front_side = Integer.MenuSwitch({
            "None": 0, "Overlay": 1, "Inset": 2,
        }, menu=Input("Front", optional_label=True, expanded=True))
        front_side_name = String("Default", "Front Name")
        front_margin = Float.Distance(0, "Margin", 0)
        thickness = get_resource(geo, plank_name=front_side_name).thickness

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

        front = create_faces(
            geo, plank_name=front_side_name,
            width=size.y - 2*front_margin,
            length=size.z - 2*front_margin,
            count_y=count_y,
            count_z=count_z,
        ).link_inputs()
        front = Mesh(front)
        front.points.set("Role", Integer.Switch(face_type == 1, ROLE_FACE, ROLE_DRAWER))
        front.offset = location + Vector((0, front_margin, front_margin))
        bundle, planks = add_plank(geo, bundle, block_name, None, front, front_side != 0)
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

@furniture.geo_modifier('Add Box')
def add_box():
    
    geo = Geometry()
    bundle = geo.get_bundle()

    block_name = String("Block", "Block Name")

    block_dims = get_block_properties(geo, block_name=block_name).node

    x, y, z = block_dims.location.xyz
    sx, sy, sz = block_dims.size.xyz
    on_ground = z == 0
    plinth = _get_plinth_dimensions(geo).node
    plinth_height = plinth.height
    force_bot_ext = block_dims.on_plinth & (z == plinth_height)

    with Panel("Sides", create_layout=True):
        left_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Left", expanded=True))
        left_side_name = String("Default", "Left Name")
        left_existing = Boolean(False, "Existing Plank", shape="Single")
        left_plank_node = get_resource(geo, plank_name=left_side_name)

        right_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Right", expanded=True))
        right_side_name = String("Default", "Right Name")
        right_existing = Boolean(False, "Existing Plank", shape="Single")
        right_plank_node = get_resource(geo, plank_name=right_side_name)
        
        top_side = Integer.MenuSwitch(SIDE_MENU, menu=Input("Top", expanded=True))
        top_deco = decoration_input("Top Deco")
        top_side_name = String("Default", "Top Name")
        top_existing = Boolean(False, "Existing Plank", shape="Single")
        top_plank_node = get_resource(geo, plank_name=top_side_name)

        bot_side = Integer.MenuSwitch(BOT_MENU_GROUND, menu=Input("Bot", expanded=True))
        bottom_deco = decoration_input("Bottom Deco")
        requested_plinth = bot_side == 4
        (requested_plinth & on_ground.bnot() & force_bot_ext.bnot()).warning(
            "Bottom Plinth is only available when Z = 0.",
        )
        bot_side.switch(requested_plinth & on_ground.bnot(), SIDE_NONE)
        bot_side.switch(on_ground & ((bot_side == SIDE_MID) | (bot_side == SIDE_EXT)), SIDE_INT)
        bot_side.switch(force_bot_ext, SIDE_EXT)
        use_plinth = bot_side == 4
        bot_side_name = String("Default", "Bot Name")
        bot_existing = Boolean(False, "Existing Plank", shape="Single")
        bot_plank_node = get_resource(geo, plank_name=bot_side_name)

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
        
        plank = create_plank(
            geo,
            plank_name = left_side_name,
            width = left_width,
            length = left_length,
            setup = 'Flank',
        )
        plank = Mesh(plank)
        plank.points.set("Role", Integer(ROLE_LEFT))
        plank.offset = left_location
        bundle, planks = add_plank(geo, bundle, block_name, None, plank, (left_side != SIDE_NONE) & left_existing.bnot() & block_dims.has_left_side.bnot())
        
    with Layout("Right Side"):
        right_z0 = Float.IndexSwitch(bot_z1, bot_z0, bot_z0, index=join_br) 
        right_z1 = Float.IndexSwitch(top_z0, top_z1, top_z1, index=join_tr)
        right_z0.switch(block_dims.has_bottom_side, bot_z1)
        right_z0.switch(raised_bottom, 0)
        right_z1.switch(block_dims.has_top_side, top_z0)
        right_width = sx
        right_length = right_z1 - right_z0
        right_location = (x, y + right_y0, z + right_z0)
        
        plank = create_plank(
            geo,
            plank_name = right_side_name,
            width = right_width,
            length = right_length,
            setup = 'Flank',
        )
        plank = Mesh(plank)
        plank.points.set("Role", Integer(ROLE_RIGHT))
        plank.offset = right_location
        bundle, planks = add_plank(geo, bundle, block_name, planks, plank, (right_side != SIDE_NONE) & right_existing.bnot() & block_dims.has_right_side.bnot())
        
    with Layout("Bottom Side"):
        bot_y0 = Float.IndexSwitch(left_y0, left_y1, left_y0, index=join_bl) 
        bot_y1 = Float.IndexSwitch(right_y1, right_y0, right_y1, index=join_br)
        bot_y0.switch(block_dims.has_left_side, left_y1)
        bot_y1.switch(block_dims.has_right_side, right_y0)
        # A plinth raises the bottom between the full-height side panels.
        bot_y0.switch(use_plinth, left_y1)
        bot_y1.switch(use_plinth, right_y0)
        bot_width = sx
        bot_length = bot_y1 - bot_y0
        bot_location = (x, y + bot_y0, z + bot_z0)
        
        plank = create_plank(
            geo,
            plank_name = bot_side_name,
            width = bot_width,
            length = bot_length,
            setup = 'Shelf',
        )
        plank = Mesh(plank)
        plank.points.set("Role", Integer(ROLE_BOTTOM))
        plank.offset = bot_location
        bundle, planks = add_plank(geo, bundle, block_name, planks, plank, (bot_side != SIDE_NONE) & bot_existing.bnot() & block_dims.has_bottom_side.bnot())
        
    with Layout("Top Side"):
        top_y0 = Float.IndexSwitch(left_y0, left_y1, left_y0, index=join_tl) 
        top_y1 = Float.IndexSwitch(right_y1, right_y0, right_y1, index=join_tr)
        top_y0.switch(block_dims.has_left_side, left_y1)
        top_y1.switch(block_dims.has_right_side, right_y0)
        top_width = sx
        top_length = top_y1 - top_y0
        top_location = (x, y + top_y0, z + top_z0)
        
        plank = create_plank(
            geo,
            plank_name = top_side_name,
            width = top_width,
            length = top_length,
            setup = 'Shelf',
        )
        plank = Mesh(plank)
        plank.points.set("Role", Integer(ROLE_TOP))
        plank.offset = top_location
        bundle, planks = add_plank(geo, bundle, block_name, planks, plank, (top_side != SIDE_NONE) & top_existing.bnot() & block_dims.has_top_side.bnot())

    with Layout("Plinth"):
        resource = get_resource(
            geo, by_id=True, plank_id=plinth.resource_id,
        ).node
        has_left = block_dims.has_left_side | (left_side != SIDE_NONE)
        has_right = block_dims.has_right_side | (right_side != SIDE_NONE)
        plinth_left = Float.Switch(has_left, plinth.recess_y, left_y1)
        plinth_right = Float.Switch(has_right, sy - plinth.recess_y, right_y0)
        plinth_depth = sx - plinth.recess_x
        plinth_length = plinth_height - z - bot_thick
        create_plinth = use_plinth & block_dims.has_bottom_side.bnot() & bot_existing.bnot()

        front = Mesh(create_plank(
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
        bundle, planks = add_plank(geo, bundle, block_name, planks, front, create_plinth)

        for index, side_y, has_side in (
            (1, plinth_left, has_left),
            (2, plinth_right - resource.thickness, has_right),
        ):
            side = Mesh(create_plank(
                geo, plank_name=resource.plank_name,
                width=plinth_depth,
                length=plinth_length,
                setup='Flank',
            ))
            side.offset = (x, y + side_y, z)
            side.points.set("Role", Integer(ROLE_PLINTH))
            side.points.set("Index", Integer(index))
            bundle, planks = add_plank(
                geo, bundle, block_name, planks, side, create_plinth & has_side.bnot(),
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

        parent = get_blocks(bundle)[block_dims.id]
        for name, mode, side in (
            ("Bottom Deco", bottom_deco, bot_side),
            ("Top Deco", top_deco, top_side),
        ):
            previous = parent.get_item(name, socket_type='INTEGER')
            parent.set_item(name, Integer.Switch(side != SIDE_NONE, previous, mode))
        parent.set_item("Inner Location", Vector((
            block_dims.inner_location.x, y + left_y1, z + bot_z1,
        )))
        parent.set_item("Inner Size", Vector((
            block_dims.inner_size.x, right_y0 - left_y1, top_z0 - bot_z1,
        )))
        parent.set_item("Outer Location", Vector((
            block_dims.outer_location.x, y + left_y0, outer_bot_z,
        )))
        parent.set_item("Outer Size", Vector((
            block_dims.outer_size.x, right_y1 - left_y0, z + top_z1 - outer_bot_z,
        )))

        for side, requested, previous, preserve in (
            ("Left", left_thick, block_dims.left_thickness, preserve_left),
            ("Right", right_thick, block_dims.right_thickness, preserve_right),
            ("Bottom", bot_thick, block_dims.bottom_thickness, preserve_bot),
            ("Top", top_thick, block_dims.top_thickness, preserve_top),
        ):
            parent.set_item(side + " Thickness", Float.Switch(preserve, requested, previous))

        bundle = set_block(bundle, block_dims.id, parent)

        # Join
        geo += planks
        geo.set_bundle(bundle)

    geo.out()

# ====================================================================================================
# Define decoration independently, including after duplication
# ====================================================================================================

@furniture.geo_modifier('Define Decoration')
def define_decoration():
    geo = Geometry()
    block_name = String("Block", "Block Name")
    settings = decoration_inputs()
    bundle = geo.get_bundle()
    index = block_index(bundle, block_name)
    block = get_blocks(bundle)[index]
    exists = index >= 0
    exists.bnot().warning("Block '" + block_name + "' not found.")
    for name, value in settings.items():
        block.set_item(name, value)
    updated = Bundle(bundle)
    updated = set_block(updated, index, block)
    bundle.switch(exists, updated)
    geo.set_bundle(bundle)
    geo.out()

# ====================================================================================================
# Add a complete block
# ====================================================================================================

@furniture.geo_modifier('Add Block')
def add_block():
    geo = Geometry()
    new_name = String("Block", "New Name")

    geo = define_block(
        geo, new_name=new_name,
    ).link_inputs(from_panel="Block")

    geo = add_box(
        geo, block_name=new_name,
    ).link_inputs()

    geo = add_shelves(
        geo, block_name=new_name,
    ).link_inputs()

    geo = add_separators(
        geo, block_name=new_name,
    ).link_inputs()

    geo = add_face(
        geo, block_name=new_name,
    ).link_inputs(from_panel="Door")

    geo.out()

# ====================================================================================================
# Select a plank
# ====================================================================================================

@furniture.geo_group('Select Plank')
def select_plank():
    geo = Geometry()
    all_blocks = Boolean(False, "All Blocks")
    block_name = String("Block", "Block Name")
    block_id = block_index(geo.get_bundle(), block_name)
    exists = block_id >= 0
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

@furniture.geo_modifier('Open Door')
def open_door():
    geo = Geometry()
    selection = select_plank(
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

@furniture.geo_modifier('Divide Block')
def divide_block():

    geo = Geometry()
    block_name = String("Block", "Block Name")
    suffix = String("Part", "Name Suffix")

    is_vert = Boolean.MenuSwitch(
        {"Vertical": True, "Horizontal": False},
        menu=Input("Orientation", optional_label=True, expanded=True))
    count = Integer(1, "Count", 0, 10)
    even = Boolean(True, "Even")
    plank_name = String("Default", "Plank")
    separator_deco = decoration_input("Separator Deco")
    create_planks = plank_name.length() > 0
    half_thickness = get_resource(geo, plank_name=plank_name).thickness / 2
    half_thickness.switch_false(create_planks)

    props = get_block_properties(geo, block_name=block_name, dims='Inner').node

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

        bundle = rep.geo.get_bundle()
        block_id = get_blocks(bundle).list_length()
        parent_block = get_blocks(bundle)[props.id]
        bundle = store_named_block(bundle, sub_name, Bundle.Combine({
            "Type": Integer(0),
            "Parent Block ID": Integer(0),
            "Decoration Mode": Integer(0),
            "Deco Index": Integer(0),
            "On Plinth": Boolean(False),
            **{
                key: parent_block.get_item(key, socket_type='INTEGER')
                for key in ("Bottom Deco", "Shelf Deco", "Top Deco")
            },
            "Shelf Deco": Integer.Switch(
                is_vert & create_planks,
                parent_block.get_item("Shelf Deco", socket_type='INTEGER'),
                separator_deco,
            ),
            **bounds,
            "Cuts": Bundle(),
        }))
        created = Geometry(rep.geo)
        created.set_bundle(bundle)

        with Layout("Shared Plank"):
            vertical_plank = create_plank(
                created, plank_name=plank_name, width=sx, length=sz, setup='Flank',
            )
            horizontal_plank = create_plank(
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
            left_plank.points.set("Block Divider", Boolean(True))

            bundle, planks = add_plank(
                created, created.get_bundle(), sub_name, None, left_plank, first.bnot(),
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

@furniture.geo_group('Create Drawer Box')
def create_drawer_box():

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

@furniture.geo_modifier('Open Drawer')
def open_drawer():

    geo = Mesh(Geometry())

    selection = select_plank(
        geo,
        role='Drawer', 
        all=False).link_inputs()
    factor = Float.Factor(0.5, "Factor", 0, 1)

    dim_node = Mesh(geo).points[selection].attribute_statistic(nd.position).node

    _, sy, sz = (dim_node.max - dim_node.min).xyz

    block_size = get_block_properties(geo, block_name=selection.block_name, dims='Inner').size
    sx = block_size.x
    drawer_box = create_drawer_box(width=sy, height=sz, depth=sx).link_inputs()

    drawer_box.offset = dim_node.min

    open_offset = (factor.interpolate(0, sx - 0.02), 0, 0)
    drawer_box.offset = open_offset
    geo[selection].offset = open_offset

    geo += drawer_box
    geo.out()

# ====================================================================================================
# Change plank material
# ====================================================================================================

@furniture.geo_modifier('Change Plank Material')
def change_plank_material():
    geo = Mesh(Geometry())
    selection = select_plank(geo).link_inputs()
    material = Material("Furniture", "Material")
    color = Color(DEFAULT_FURNITURE_COLOR, "Color")

    geo.faces[selection].material = material
    geo.faces[selection].set("Color", color)
    geo.out()

# ====================================================================================================
# Replace planks
# ====================================================================================================

@furniture.geo_modifier('Replace Plank')
def replace_plank():
    geo = Geometry()
    bundle = geo.get_bundle()
    selection = select_plank(geo).link_inputs()

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
    instances = planks.points.split_to_instances(group_id=Integer("Plank ID"))

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
        for attribute in ("Block ID", "Role", "Index", "Plank ID", "Res ID"):
            resized.points.set(attribute, original.points.sample_index(Integer(attribute), index=0))
        plank.geometry = resized

    geo = remaining + plank.generated
    geo.set_bundle(bundle)
    geo.out()

# ====================================================================================================
# Delete planks
# ====================================================================================================

@furniture.geo_modifier('Delete Plank')
def delete_plank():
    geo = Mesh(Geometry())
    bundle = geo.get_bundle()
    selection = select_plank(geo).link_inputs()
    geo.points[selection].delete()
    geo.set_bundle(bundle)
    geo.out()

# ====================================================================================================
# Block dimensions and positions
# ====================================================================================================

@furniture.geo_modifier('Add Cotes')
def add_cotes():
    geo = Geometry()
    block = get_block_properties(geo).link_inputs().node

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

            geo = add_cote_line(
                geo, show=show_dimension & block.exists,
                position=block.location, axis=axis, value=block.size.xyz[axis],
                invert=invert, font_size=font_size, section=section,
                cote_offset_a=Float(0, "Dimension Offset A", hide_in_modifier=True),
                cote_offset_b=Float(0, "Dimension Offset B", hide_in_modifier=True),
            )
            geo = add_cote_line(
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

@furniture.geo_modifier('Cut Sheet')
def cut_sheet():

    obj = Object(None, "Furniture")
    geo = obj.info().geometry
    bundle = geo.get_bundle()
    
    with Layout("Resource and block names"):
        with Layout("Resource names"):
            resources = get_resources(bundle)
            resources.switch(resources.list_length() == 0, Bundle.List(default_resource()))
            for rep in repeat(resources.list_length(), labels=Geometry.Join(), offset=0.0):
                name = resources[rep.iteration].get_item("Name", socket_type='STRING')
                label = rep.iteration.to_string() + " : " + name
                label_curve = Curve(label.to_curves(size=0.1).realize()).fill()
                label_curve.offset = 0, rep.offset, 0
                rep.labels += label_curve
                rep.offset -= 0.2
            labels = Mesh(rep.labels)

        with Layout("Block names"):
            blocks = get_blocks(bundle)
            column_x = labels.points.attribute_statistic(nd.position).node.max.x + 0.3
            for rep in repeat(blocks.list_length() - 1, labels=labels, offset=0.0):
                name = blocks[rep.iteration + 1].get_item("Name", socket_type='STRING')
                label_curve = Curve(name.to_curves(size=0.1).realize()).fill()
                label_curve.offset = column_x, rep.offset, 0
                rep.labels += label_curve
                rep.offset -= 0.2
            labels = Mesh(rep.labels)

        with Layout("Cuts per resource name"):
            for rep in repeat(blocks.list_length() - 1, cloud_pts=Cloud.Points(count=0)):
                cuts = blocks[rep.iteration + 1].get_item("Cuts", socket_type='BUNDLE')
                resources = cuts.get_nested_paths(mode="Data Type", data_type="Bundle")
                for resource in repeat(resources.list_length(), cloud_pts=rep.cloud_pts):
                    entries = cuts.get_item(resources[resource.iteration], socket_type='BUNDLE', structure_type='LIST')
                    for cut in repeat(entries.list_length(), cloud_pts=resource.cloud_pts):
                        node = entries[cut.iteration].separate(signature=CUT_SIG)
                        pt = Cloud.Points(count=1)
                        pt.set("Res ID", node.res_id)
                        pt.set("Count", node.count)
                        pt.set("Size", node.size)
                        pt.set("Orient", node.orient)
                        cut.cloud_pts += pt
                    resource.cloud_pts = cut.cloud_pts
                rep.cloud_pts = resource.cloud_pts
            cloud_pts = rep.cloud_pts

        (labels + cloud_pts).out()

# ====================================================================================================
# Decoration
# ====================================================================================================

def block_by_id(geo, block_id):
    return get_blocks(geo.get_bundle())[block_id]

# ----------------------------------------------------------------------------------------------------
# Show Deco id
# ----------------------------------------------------------------------------------------------------

@furniture.geo_modifier('Show Decoration IDs')
def show_decoration_ids():

    geo = Geometry()
    bundle = geo.get_bundle()

    show = Boolean(True, "Show")
    font_size = Float(1.0, "Font Size")

    blocks = get_blocks(bundle)
    for rep in repeat(blocks.list_length(), labels=None):

        block_id = rep.iteration
        block = blocks[rep.iteration].separate(signature=BLOCK_SIG)
        
        label = block_id.to_string().to_curves(
            size=font_size,
            align_x="Center",
            align_y="Middle",
            ).realize()
        label = Curve(label)
        label = label.fill()

        label.switch((rep.iteration==0) | (block.type!=1))
        label.transform(rotation=(pi/2, 0, pi/2))

        label.offset = block.inner_location + block.inner_size.scale(0.5)
        rep.labels += label

    labels = rep.labels.switch_false(show)
    geo += labels

    geo.set_bundle(bundle)

    geo.out()

# ----------------------------------------------------------------------------------------------------
# Extract a composition
# ----------------------------------------------------------------------------------------------------

@furniture.geo_group('.Extract Composition')
def _extract_composition():

    geo = Geometry()
    block_id = Integer(0, "Block ID")
    instances = Instances(None, "Instances")
    block = block_by_id(geo, block_id)
    location = block.get_item("Inner Location", socket_type='VECTOR')
    size = block.get_item("Inner Size", socket_type='VECTOR')
    seed = Integer(0, "Seed")

    shelf_depth, shelf_width, available_height = size.xyz

    attempts = Integer((instances.insts.count * 0.4).ceil()).max(5)
    for rep in repeat(attempts, index=-1, stop=False, seed=seed):
        index = Integer.Random(0, (instances.insts.count - 1).max(0), id=0, seed=rep.seed.hash_value(9173))
        selected = Instances(instances)
        selected.insts[nd.index==index].separate()
        sel_mesh = Mesh(selected.realize())
        dims = sel_mesh.points[nd.position.z > 0].attribute_statistic(nd.position).node
        height_dims = sel_mesh.points.attribute_statistic(nd.position).node

        candidate_size = dims.max - dims.min
        ok = rep.stop.bnot() & (candidate_size.y <= shelf_width)
        ok &= (height_dims.max.z - height_dims.min.z) <= available_height

        rep.index.switch((rep.iteration==0) | ok, index)
        rep.stop = rep.stop | ok
        rep.seed = rep.seed.hash_value(934487)

    index = rep.index
    selected = Instances(instances)
    selected.insts[nd.index == index].separate()
    sel_mesh = Mesh(selected.realize())

    island_count = sel_mesh.points.sample_index(nd.mesh_island().island_count, index=0)

    with Layout("Search Base Face"):
        for rep in repeat(island_count, mesh=Mesh(Geometry.Join()), base_exists=False, base_loc=(0.0, 0.0, 0.0), base_size=(0.0, 0.0, 0.0)):
            island = Mesh(Mesh(sel_mesh).points[nd.mesh_island().island_index==rep.iteration].separate())
            island_dims = island.points.attribute_statistic(nd.position).node
            island_size = island_dims.max - island_dims.min

            is_base = island.points.count == 4
            is_base &= island_size.z == 0

            rep.mesh.switch_false(is_base, rep.mesh + island)

            rep.base_exists |= is_base
            rep.base_loc.switch(is_base, island_dims.min)
            rep.base_size.switch(is_base, island_size)

        with Layout("Item Location and size"):
            item_mesh = Mesh(rep.mesh)
            x_base, y_base, _ = rep.base_loc.xyz
            w_base = rep.base_size.y

            item_dims = item_mesh.points.attribute_statistic(nd.position).node
            item_loc = item_dims.min
            x_item, y_item, _ = item_loc.xyz
            item_size = item_dims.max - item_dims.min
            item_depth, item_width, item_height = item_size.xyz

        with Layout("Left Margin"):
            left_space = y_item - y_base
            right_space = y_base + w_base - item_dims.max.y

            align_left = rep.base_exists & (left_space < right_space)
            align_right = rep.base_exists & (left_space > right_space)

            available = shelf_width - item_width
            left_margin = Float.Random(available*0.25, available*0.75, id=0, seed=seed.hash_value(386223))

            left_margin.switch(align_left, left_space)
            left_margin.switch(align_right, shelf_width - item_width - right_space)

        with Layout("Depth Margin"):

            available = shelf_depth - item_depth
            back_margin = Float.Random(available*0.25, available*0.75, id=0, seed=seed.hash_value(4836002))

            back_margin.switch(rep.base_exists, x_item - x_base)

        item_mesh.offset = location - item_loc + (back_margin, left_margin, 0)

        fits = (instances.insts.count > 0) & (item_mesh.points.count > 0)
        fits &= item_width <= shelf_width
        fits &= item_height <= available_height
        remaining = Instances(instances)
        remaining.insts[fits & (nd.index == index)].delete()
        remaining.out("Instances")
        item_mesh.switch_false(fits).out("Mesh")


@furniture.geo_group('.Extract Items')
def _extract_items():
    geo = Geometry()
    block_id = Integer(0, "Block ID")
    instances = Instances(None, "Instances")
    block = block_by_id(geo, block_id)
    location = block.get_item("Inner Location", socket_type='VECTOR')
    size = block.get_item("Inner Size", socket_type='VECTOR')
    max_items = Integer(10, "Max Items", 0, 20)
    dist_min = Float.Distance(.01, "Min Distance", 0)
    dist_max = Float.Distance(.05, "Distance", 0)
    delete_items = Boolean(True, "Delete Items")
    seed = Integer(0, "Seed")
    depth, width, height = size.xyz

    for item in repeat(
        max_items.max(0), available=instances, decorations=Geometry.Join(),
        used=0.0, stop=False,
    ):
        available = Instances(item.available)
        item_seed = seed + item.iteration * 104729
        index = Integer.Random(
            0, (available.insts.count - 1).max(0), id=0, seed=item_seed,
        )
        chosen = Cloud.Points(count=1).points.instance_on(
            instance=available, pick_instance=True, instance_index=index,
        )
        mesh = Mesh(Instances(chosen).realize())
        bounds = mesh.points.attribute_statistic(nd.position).node
        item_size = bounds.max - bounds.min
        gap = Float.Random(
            dist_min, dist_max.max(dist_min), id=0, seed=item_seed + 1,
        )
        gap.switch(item.iteration == 0, 0)
        end = item.used + gap + item_size.y
        fits = (available.insts.count > 0) & (mesh.points.count > 0)
        fits &= (end <= width) & (item_size.x <= depth) & (item_size.z <= height)
        add = item.stop.bnot() & fits
        x = Float.Random(0, (depth - item_size.x).max(0), id=0, seed=item_seed + 2)
        chosen.translate(translation=(
            x - bounds.min.x, item.used + gap - bounds.min.y, -bounds.min.z,
        ))
        chosen.switch_false(add)
        item.decorations += chosen
        item.used.switch(add, end)
        item.stop = item.stop | fits.bnot()
        available.insts[add & delete_items & (nd.index == index)].delete()
        item.available = available

    margin = (width - item.used).max(0)
    jitter = Float.Random(-0.25, 0.25, id=0, seed=seed.hash_value(9187))
    placed = Instances(item.decorations)
    placed.translate(translation=location + Vector((0, margin / 2 + jitter * margin, 0)))
    Instances(item.available).out("Instances")
    Mesh(placed.realize()).out("Mesh")


@furniture.geo_modifier('Furniture Decoration')
def furniture_decoration():

    use_geometry = Boolean.MenuSwitch(
        {"Object": False, "Geometry": True},
        menu=Input("Source", optional_label=True, expanded=True),
    )
    obj = Object(None, "Furniture")
    source_geometry = Geometry()
    geo = Geometry.Switch(use_geometry, obj.info().geometry, source_geometry)

    show_deco = Boolean(True, "Show Decoration")
    show_ids = Boolean(False, "Show IDs")

    all_blocks = Boolean(True, "All")
    block_ids = String("", "Block IDs")
    tokens = block_ids.replace("\t", " ").replace("\n", " ").replace("\r", " ").split(" ")
    items_collection = Collection(None, "Items")
    compositions_collection = Collection(None, "Compositions")
    max_per_shelf = Integer(10, "Max per Shelf", 1, 20)
    delete_items = Boolean(True, "Delete Items")
    dist_min = Float.Distance(.01, "Min Distance", 0.0, 1.0)
    dist_max = Float.Distance(.05, "Distance", 0.0, 1.0)
    seed = Integer(0, "Seed")

    bundle = geo.get_bundle()
    blocks = get_blocks(bundle)
    items = items_collection.info(separate_children=True, reset_children=True)
    compositions = compositions_collection.info(separate_children=True, reset_children=True)

    for volume in repeat(
        blocks.list_length(), decorations=Geometry.Join(),
        available=compositions, available_items=items,
    ):
        block = blocks[volume.iteration]
        deco_id = volume.iteration
        mode = block.get_item("Decoration Mode", socket_type='INTEGER')
        active = block.get_item("Type", socket_type='INTEGER') == 1
        for selection in repeat(Integer.Switch(all_blocks, tokens.list_length(), 0), selected=all_blocks):
            selection.selected |= tokens[selection.iteration].to_integer() == deco_id
        active &= selection.selected
        use_items = active & (mode == 1)
        use_composition = active & (mode == 2)
        volume_seed = seed + deco_id * 104729

        with Layout("Items composition"):
            extracted_items = _extract_items(
                geo, block_id=deco_id, instances=volume.available_items,
                max_items=Integer.Switch(use_items, 0, max_per_shelf.max(1)),
                min_distance=dist_min, distance=dist_max,
                delete_items=delete_items, seed=volume_seed,
            ).node
            items_mesh = Mesh(extracted_items.mesh)
            placed = items_mesh.to_instance()
            placed.switch_false(items_mesh.points.count > 0)
            volume.available_items.switch(use_items, extracted_items.instances)

        with Layout("Composition without replacement"):
            extracted = _extract_composition(
                geo, block_id=deco_id, instances=volume.available, seed=volume_seed + 5,
            ).node
            extracted_mesh = Mesh(extracted.mesh)
            composition_instance = extracted_mesh.to_instance()
            composition_instance.switch_false(extracted_mesh.points.count > 0)
            placed = Instances(Instances.Switch(use_composition, placed, composition_instance))
            placed.switch_false(use_items | use_composition)
            volume.available.switch(use_composition, extracted.instances)

        placed.insts.set("Support Block ID", deco_id)
        placed.insts.set("Is Decoration", Boolean(True))
        volume.decorations += placed

    result = Geometry(volume.decorations)
    result.switch_false(show_deco)
    id_source = Geometry.Join()
    id_source.set_bundle(bundle)
    ids = show_decoration_ids(id_source, show=True).link_inputs()
    result.switch(show_ids, ids)
    result.set_bundle(bundle)
    result.out()



def demo(rebuild=False):
    furniture.build(rebuild=rebuild)
