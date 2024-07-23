import bpy

def get_image(name):
    image = bpy.data.images.get(name)
    if image is None:
        image = bpy.data.images.new(name, width=1024, height=1024)
    return image

def get_material(name):
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name)
    return material

def get_object(name):
    return bpy.data.objects.get(name)

def test_geonodes_inputs(tree):
    a = tree.boolean(True)
    b = tree.color((.1, .2, .3, .4))
    c = tree.image(get_image("Test image"))
    d = tree.integer(123)
    e = tree.material(get_material("Test material"))
    f = tree.rotation((.4, .5, .6))
    g = tree.string("My String")
    h = tree.value(789)
    i = tree.vector((7, 8, 9))

    j = tree.active_camera
    k = tree.is_viewport
    l = tree.scene_time
    m = tree.self_object

    n = tree.object_info(object="Cube", as_instance=True, transform_space='RELATIVE')
    o = tree.self_object.info(as_instance=False, transform_space='ORIGINAL')
    p = tree.collection_info(collection=None, separate_children=True, reset_children=True, transform_space='RELATIVE')
    q = tree.image_info(image=get_image("Test image"), frame=123)

def test_geometry(tree):

    a = tree.ID
    b = tree.index
    d = tree.normal
    e = tree.position
    f = tree.radius

    n = tree.named_float("float")
    for bsock in n._bnode.outputs:
        print(bsock.name, bsock)
    print(n, n.attribute)
    n = tree.named_int("int")
    print(n, n.attribute)
    n = tree.named_vector("vector")
    print(n, n.attribute)
    n = tree.named_color("color")
    print(n, n.attribute)
    n = tree.named_bool("bool")
    print(n, n.attribute)
    n = tree.named_quaternion("quaternion")
    print(n, n.attribute)
    n = tree.named_matrix("matrix")
    print(n, n.attribute)
