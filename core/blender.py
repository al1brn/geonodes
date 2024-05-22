#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Wed Jun 29 17:03:43 2022

@author: alain.bernard
@email: alain@ligloo.net

-----

Blender utilities

Some functions to ease the access to standard bpy api
"""

import numpy as np
import bpy
import bmesh
import idprop
from mathutils import Vector

# ====================================================================================================
# Get Blender things from spec. The spec can be the name of the thing itself

# ----------------------------------------------------------------------------------------------------
# Get an existing collection

def get_collection(spec, halt=True):
    """ Get a collection by its name

    Args:
    - spec (str or Collection) : the collection to return
    - halt (bool=True) : raise an exception if not found

    Returns:
    - Collection
    """

    if isinstance(spec, str):
        coll = bpy.data.collections.get(spec)
        if coll is None:
            if halt:
                raise Exception(f"Collection '{spec}' not found")
        return coll

    elif isinstance(spec, bpy.types.Collection):
        return spec

    else:
        raise Exception(f"Collection name expected, not '{spec}'")

# ----------------------------------------------------------------------------------------------------
# Create a collection

def create_collection(spec, parent=None):
    """ Create an new collection by its name

    Args:
    - spec (str or Collection) : the collection to return
    - parent (str or Collection) : the parent collecton

    Returns:
    - Collection
    """
    if isinstance(spec, str):
        coll = bpy.data.collections.get(spec)
        if coll is None:
            coll = bpy.data.collections.new(spec)
            if parent is None:
                bpy.context.scene.collection.children.link(coll)
            else:
                get_collection(parent).children.link(coll)
        return coll

    elif isinstance(spec, bpy.types.Collection):
        return spec

    else:
        raise Exception(f"Collection name expected, not '{spec}'")

# ----------------------------------------------------------------------------------------------------
# Create a temporary collection

def get_temp_collection(name="GeoPy Temp"):
    coll = bpy.data.collections.get(name, None)
    if coll is None:
        coll = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(coll)
        coll.hide_render   = True
        coll.hide_viewport = True
        coll.hide_select   = True
    return coll

# ----------------------------------------------------------------------------------------------------
# An object

def get_object(spec, halt=True):
    """ Get an object by its name

    Args:
    - spec (str or Object) : the object to return
    - halt (bool=True) : raise an exception if not found

    Returns:
    - Object
    """

    obj = None
    if isinstance(spec, str):
        obj = bpy.data.objects.get(spec)
        if obj is None:
            if halt:
                raise Exception(f"Object '{spec}' not found")

    elif isinstance(spec, bpy.types.Object):
        obj = spec

    else:
        raise Exception(f"Object or object name expected, not '{spec}'")

    return obj

# ----------------------------------------------------------------------------------------------------
# Create an empty object

def get_empty(name, collection=None):
    """ Create an empty object in the specified collection

    If the object already exists, it is returned whaterver its type.

    Args:
    - name (str) : the name of the text object to create
    - collection (str or collection): the collection where to create the object

    Returns:
    - Empty object
    """

    obj = get_object(name, halt=False)
    if obj is not None:
        return obj

    empty = bpy.data.objects.new(name=name, object_data=None)
    if collection is None:
        coll = bpy.context.collection
    else:
        coll = get_collection(collection)

    coll.objects.link(empty)

    return empty


# ----------------------------------------------------------------------------------------------------
# Create a mesh object

def create_mesh_object(name, collection=None):
    """ Create a mesh in the specified collection

    If the object already exists, it is returned whaterver its type.

    Args:
    - name (str) : the name of the mesh object to create
    - collection (str or collection) : the collection where to create the object

    Returns:
    - Mesh object
    """

    obj = get_object(name, halt=False)
    new = False
    if obj is None:
        new = True
        mesh = bpy.data.meshes.new("Mesh")
        obj  = bpy.data.objects.new(name, mesh)

    if collection is None:
        if new:
            bpy.context.collection.objects.link(obj)
    else:
        try:
            get_collection(collection).objects.link(obj)
        except RuntimeError:
            pass

    return obj


# ----------------------------------------------------------------------------------------------------
# Create a curve object

def create_curve_object(name, collection=None):
    """ Create a curve in the specified collection

    If the object already exists, it is returned whaterver its type.

    Args:
    - name (str) : the name of the curve object to create
    - collection (str or collection) : the collection where to create the object

    Returns:
    - Curve object
    """

    obj = get_object(name, halt=False)
    new = False

    if obj is None:
        new = True
        curve = bpy.data.curves.new("Curve", type='CURVE')
        curve.dimensions = '3D'
        obj  = bpy.data.objects.new(name, curve)


    if collection is None:
        if new:
            bpy.context.collection.objects.link(obj)
    else:
        try:
            get_collection(collection).objects.link(obj)
        except RuntimeError:
            pass

    return obj

# ----------------------------------------------------------------------------------------------------
# Create a text object

def create_text_object(name, text="Text", collection=None):
    """ Create a text object in the specified collection

    If the object already exists, it is returned whaterver its type.

    Args:
    - name (str) : the name of the text object to create
    - text (str) : body of the object
    - collection (str or collection): the collection where to create the object

    Returns:
    - Text object
    """

    obj = get_object(name, halt=False)
    if obj is not None:
        obj.data.body = text
        return obj

    if obj is None:
        new   = True
        curve = bpy.data.curves.new("Curve", type='FONT')
        obj   = bpy.data.objects.new(name, curve)
        curve.body = text

    if collection is None:
        if new:
            bpy.context.collection.objects.link(obj)
    else:
        try:
            get_collection(collection).objects.link(obj)
        except RuntimeError:
            pass

    return obj

# ----------------------------------------------------------------------------------------------------
# Duplicate an object

def duplicate(spec, data=True, actions=True, collection=None):
    """ Duplicate an object.

    Depending on the data and actions arguments, a full copy is done or not.

    If a collection is given, the duplicate is placed in this collection.

    Args:
    - spec (str or Object) : the object to duplicate
    - data (bool=True) : duplicate the data
    - actions (bool=True) : duplicate the actions
    - collection (str or collection) : the collection where to duplicate the object

    Returns:
    - object
    """

    obj = get_object(spec)

    obj_copy = obj.copy()

    if data:
        obj_copy.data = obj_copy.data.copy()

    if actions and obj_copy.animation_data is not None and obj_copy.animation_data.action is not None:
        obj_copy.animation_data.action = obj_copy.animation_data.action.copy()

    if collection is None:
        for coll in bpy.data.collections:
            if obj.name in coll.objects:
                collection = coll

    if collection is not None:
        get_collection(collection, halt=True).objects.link(obj_copy)

    return obj_copy

# ----------------------------------------------------------------------------------------------------
# Object type: Empty of name to data type

def object_type(spec):
    """ Get the type of the specified object.

    Args:
    - spec (str or Object) : object

    Returns:
    - str : 'Empty' the name of the type of data
    """

    obj = get_object(spec)
    if obj.data is None:
        return 'Empty'
    else:
        return type(obj.data).__name__

# ====================================================================================================
# Access to typed data

# ----------------------------------------------------------------------------------------------------
# Mesh data

def get_mesh(spec, halt=True):
    """ Get the Mesh data of an object.

    Raise an exception if the mesh is not found and halt == True.

    Args:
    - spec (str, Object or Mesh) : data specifier
    - halt (boo:True) : raise exception if not found

    Returns:
    - Mesh instance
    """

    if isinstance(spec, bpy.types.Mesh):
        return spec

    obj = get_object(spec, halt=halt)
    if obj is None:
        return None

    if not isinstance(obj.data, bpy.types.Mesh):
        raise Exception(f"Object '{obj.name}' is not a Mesh")

    return obj.data

# ----------------------------------------------------------------------------------------------------
# Curve data

def get_curve(spec, halt=True):
    """ Get the Curve data of an object.

    Raise an exception if the curve is not found and halt == True.

    Args:
    - spec (str, Object or Curve) : data specifier
    - halt (boo:True) : raise exception if not found

    Returns:
    - Curve instance
    """

    if isinstance(spec, (bpy.types.Curve, bpy.types.SurfaceCurve)):
        return spec

    obj = get_object(spec, halt=halt)
    if obj is None:
        return None

    if not isinstance(obj.data, (bpy.types.Curve, bpy.types.SurfaceCurve)):
        raise Exception(f"Object '{obj.name}' is not a Curve")

    return obj.data


# ----------------------------------------------------------------------------------------------------
# Object data

def get_data(spec, halt=True):
    """ Get the data of an object.

    Raise an exception if the object is not found and halt == True.

    Args:
    - spec (str, Object or Data) : data specifier
    - halt (boo:True) : raise exception if not found

    Returns:
    - Curve instance
    """

    if isinstance(spec, (bpy.types.Mesh, bpy.types.Curve)):
        return spec

    else:
        return get_object(spec).data

    #data = get_mesh(spec, halt=False)
    #if data is None:
    #    data = get_curve(spec, halt=halt)
    #return data

# ====================================================================================================
# Clear Mesh or Curve geometry

def clear_geometry(spec):

    obj = get_object(spec, halt=False)
    if obj is None:
        return

    data = obj.data
    if isinstance(data, bpy.types.Mesh):
        data.clear_geometry()

    elif isinstance(data, bpy.types.Curve):
        data.splines.clear()

# ====================================================================================================
# set and get mesh vertices

# ----------------------------------------------------------------------------------------------------
# Get the vertices

def get_mesh_vertices(spec):
    """ Get the vertices of a Mesh.

    Args:
    - spec (str, Object or Mesh) : data specifier

    Returns:
    - numpy array (n, 3) where n is the number of vertices
    """

    mesh = get_mesh(spec)

    n = len(mesh.vertices)
    a = np.empty(n * 3, float)
    mesh.vertices.foreach_get('co', a)
    return np.reshape(a, (n, 3))

# ----------------------------------------------------------------------------------------------------
# Set the vertices

def set_mesh_vertices(spec, verts):
    """ Set the vertices of a Mesh.

    Use for updating a mesh, no change on the faces and edges.
    The size of the verts array must be n*3 where n is the number of vertices of the Mesh.

    Args:
    - spec (str, Object or Mesh) : data specifier
    - verts (array) : array of vectors.

    Returns:
    - None
    """

    mesh = get_mesh(spec)

    n = len(mesh.vertices)
    if n != np.size(verts)//3:
        raise Exception(f"set_mesh_vertices error: the number of vertices to write ({np.size(verts)//3}) is different" +
                         f" from the number of vertices in mesh '{spec}' which is ({n}).")

    a = np.reshape(verts, n*3)
    mesh.vertices.foreach_set('co', a)

    mesh.update()

# ====================================================================================================
# Temp object

def temp_mesh_object(name="Mesh"):
    return create_mesh_object(f"GeoPy Temp - {name}", collection=get_temp_collection())

# ====================================================================================================
# BMesh class

class BMesh:
    def __init__(self, obj):
        self.obj = get_object(obj, halt=True)

    def __enter__(self):
        self.bm = bmesh.new()
        self.bm.from_mesh(self.obj.data)

        return self.bm

    def __exit__(self, *args):
        self.bm.to_mesh(self.obj.data)
        self.bm.free()
        del self.bm

# ====================================================================================================
# Remove doubles

def remove_doubles(spec, threshold=0.0001):
    obj = get_object(spec, halt=True)
    with BMesh(obj) as bm:
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=threshold)
    return obj


# ====================================================================================================
# Faces

def shade_smooth(obj, smooth=True):
    obj = get_object(obj)
    a = [smooth] * len(obj.data.polygons)
    obj.data.polygons.foreach_set('use_smooth', a)

# ====================================================================================================
# ====================================================================================================
# Splines

SPLINE_TYPES = ['BEZIER', 'POLY', 'NURBS']

BEZIER = 0
POLY   = 1
NURBS  = 2

# ----------------------------------------------------------------------------------------------------
# One Blender spline to dict

def get_spline_points(bl_spline):

    def read(coll, attr, dtype, shape):
        a = np.empty(len(coll)*np.prod(shape, dtype=int), dtype)
        coll.foreach_get(attr, a)
        return np.reshape(a, (len(coll),) + shape)

    spline = {'type': SPLINE_TYPES.index(bl_spline.type)}

    if bl_spline.type == 'BEZIER':
        spline['points']            = read(bl_spline.bezier_points, 'co',                float, (3,))

        spline['handle_left']       = read(bl_spline.bezier_points, 'handle_left',       float, (3,))
        spline['handle_right']      = read(bl_spline.bezier_points, 'handle_right',      float, (3,))
        # Key name is the one of Geometry Nodes which is different from python name
        spline['handle_type_left']  = read(bl_spline.bezier_points, 'handle_left_type',  int,   ())
        spline['handle_type_right'] = read(bl_spline.bezier_points, 'handle_right_type', int,   ())

        spline['radius']      = read(bl_spline.bezier_points, 'radius',            float, ())
        spline['tilt']        = read(bl_spline.bezier_points, 'tilt',              float, ())

    else:
        spline['points']      = read(bl_spline.points, 'co',     float, (4,))

        spline['radius']      = read(bl_spline.points, 'radius', float, ())
        spline['tilt']        = read(bl_spline.points, 'tilt',   float, ())

    return spline

# ----------------------------------------------------------------------------------------------------
# Set the points of a Blender spline

def set_spline_points(bl_spline, spline):

    def write(coll, attr, a):
        if a is None:
            return
        coll.foreach_set(attr, np.reshape(a, np.size(a)))

    if spline is None:
        return

    if bl_spline.type == 'BEZIER':
        write(bl_spline.bezier_points, 'co',                spline['points'])
        write(bl_spline.bezier_points, 'handle_left',       spline.get('handle_left'))
        write(bl_spline.bezier_points, 'handle_right',      spline.get('handle_right'))
        # Key name is the one of Geometry Nodes which is different from python name
        write(bl_spline.bezier_points, 'handle_left_type',  spline.get('handle_type_left'))
        write(bl_spline.bezier_points, 'handle_right_type', spline.get('handle_type_right'))

        write(bl_spline.bezier_points, 'radius', spline.get('radius'))
        write(bl_spline.bezier_points, 'tilt',   spline.get('tilt'))

    else:
        write(bl_spline.points, 'co',     spline['points'])

        write(bl_spline.points, 'radius', spline.get('radius'))
        write(bl_spline.points, 'tilt',   spline.get('tilt'))


# ----------------------------------------------------------------------------------------------------
# Read all the splines

def get_splines(spec):
    """ Get the information on the splines from a curve object.

    Attribute names not starting with _ char are Blender spline attributes.

    Returns a dictionary with the following entries:
        - types array of ints) : the spline types
        - cyclic (array of bools) : splines are cyclic or not
        - resolution (array of ints) : spline resolutions
        - material_index (array of ints) : spline material indices
        - splines (array of dicts) : see below

    *'types'* is the only mandatory attribute. The length of this array gives the number of splines.
    If the object has no spline, the dictionary {'types': []} is returned.

    The spline dictionaries have the following entries:
        - points (array of 3-vectors or 4-vectors) : point positions
        - radius (array of floats) : point radius
        - tilt (array of floats) : point tilts
        - handle_left (array of 3-vectors or 4-vectors) : left handle positions
        - handle_right (array of 3-vectors or 4-vectors) : right handle positions
        - handle_type_left (array of ints) : left handle types
        - handle_type right (array of ints) : right handle types

    Arguments
    ---------
        - spec (str or Curve Object) : the Curve object

    Returns
    -------
        - A dictionary containing the splines data
    """

    bl_splines = get_curve(spec).splines
    nsplines   = len(bl_splines)
    if nsplines == 0:
        return {'types': []}

    # ----------------------------------------------------------------------------------------------------
    # Prepare the dictionary

    splines_dict = {'types' : [0]*nsplines, 'splines' : [None]*nsplines}

    # ----------------------------------------------------------------------------------------------------
    # Loop on the splines to read the types and the number of points

    for i, bl_spline in enumerate(bl_splines):
        splines_dict['types'  ][i] = SPLINE_TYPES.index(bl_spline.type)
        splines_dict['splines'][i] = get_spline_points(bl_spline)

    # ----------------------------------------------------------------------------------------------------
    # Read the splines attributes

    a = np.empty(nsplines, int)
    for name, key in [('material_index', 'material_index'), ('resolution_u', 'resolution'), ('use_cyclic_u', 'cyclic')]:
        bl_splines.foreach_get(name, a)
        splines_dict[key] = np.array(a)

    a = np.empty(nsplines, bool)
    for name, key in [('use_cyclic_u', 'cyclic')]:
        bl_splines.foreach_get(name, a)
        splines_dict[key] = np.array(a)

    return splines_dict

# ----------------------------------------------------------------------------------------------------
# Set splines

def set_splines(spec, splines_dict, update=True):
    """ Get the information on the splines from a curve object.

    Args:
    - spec (str or Curve Object) : the Curve object

    Returns:
    - Array (number of splines, 4) of ints : the splines info
    """

    bl_splines = get_curve(spec).splines
    if update:
        bl_splines.clear()

    nsplines = len(splines_dict['types'])
    if not nsplines:
        return

    # ----------------------------------------------------------------------------------------------------
    # Loop on the splines

    for i, (spline_type, spline) in enumerate(zip(splines_dict['types'], splines_dict['splines'])):

        # Create if update
        if update:
            count = len(spline['points'])
            bl_spline = bl_splines.new(SPLINE_TYPES[spline_type])
            if spline_type == BEZIER:
                bl_spline.bezier_points.add(count - len(bl_spline.bezier_points))
            else:
                bl_spline.points.add(count - len(bl_spline.points))

        # Transfer the points
        bl_spline = bl_splines[i]
        set_spline_points(bl_spline, spline)

    # ----------------------------------------------------------------------------------------------------
    # Write the splines attributes

    attr_names = {
        'resolution'     : 'resolution_u',
        'material_index' : 'material_index',
        'cyclic'         : 'use_cyclic_u',
        }

    for key, a in splines_dict.items():
        if key not in attr_names.keys():
            continue

        bl_splines.foreach_set(attr_names[key], np.reshape(a, np.size(a)))


# ====================================================================================================
# Create a new material

def create_material(name, reset=False, **kwargs):
    """ Create a material with parameters passed as keyword arguments.

    This simple method allows to specified the values of the input sockets of the Principled BSDF.
    The following example create a blue material.

    ``` python
    mat = create_material("Blue Material", color=mathutils.Color((0, 0, 1)))
    ```
    Args:
    - name (str) : name of the material to create
    - reset (bool=False) : reset the material if already exists (True) or let it unchanged (False).
    - **kwargs : key word arguments to specify the values of the entries in the BSDF Node

    Returns:
    - Material
    """

    if isinstance(name, bpy.types.Material):
        mat = name
        if not reset:
            return mat

    else:
        mat = bpy.data.materials.get(name)
        if mat is None:
            mat = bpy.data.materials.new(name)

        else:
            if not reset:
                return mat

    mat.use_nodes = True
    nodes = mat.node_tree.nodes

    bsdf = None
    for node in nodes:
        if isinstance(node, bpy.types.ShaderNodeBsdfPrincipled):
            bsdf = node
            break
    if bsdf is None:
        print(f"Warning: ShaderNodeBsdfPrincipled node not found for material '{name}'")
        return mat

    for sock_name, sock_value in kwargs.items():
        found = False
        for socket in bsdf.inputs:
            if sock_name.lower() in [socket.name.lower().replace(' ', '_'), socket.name.lower()]:
                if isinstance(socket.default_value, bpy.types.bpy_prop_array):
                    a = tuple(sock_value)
                    if len(socket.default_value) == 4 and len(a) == 3:
                        socket.default_value = a + (1,)
                    elif len(socket.default_value) == 3 and len(a) == 4:
                        socket.default_value = a[:-1]
                    elif len(socket.default_value) == len(a):
                        socket.default_value = a
                    else:
                        raise RuntimeError(f"create_material error: socket '{sock_name}' takes a vector of len {len(socket.default_value)}, but the parameter len is {len(a)}!")
                else:
                    socket.default_value = sock_value

                found = True
                break

        if not found:
            print([sock.name for sock in bsdf.inputs])
            raise RuntimeError(f"create_material error: Socket '{sock_name}' not found")

    return mat

# ----------------------------------------------------------------------------------------------------
# Create a series of materials

def create_materials(mat_specs, reset=False, return_names=True):
    """ Create new materials as specified.

    Call the function **create_material** as specified in the **mat_specs** argument.

    Args:
    - mat_specs (dict {mat_name: mat_spec}) where mat_spec is a dictionary passe to **create_material**
    - reset (bool=False) : reset the material if already exists (True) or let it unchanged (False).
    - return_names (bool=True) : return the material names (True) or the materials (False)

    Returns:
    - list of str or list of Materials : the created materials
    """

    materials = []
    for name, spec in mat_specs.items():
        materials.append(create_material(name, reset=reset, **spec))

    if return_names:
        return [mat.name for mat in materials]
    else:
        return materials

# ----------------------------------------------------------------------------------------------------
# Utility to get the materials prefixed

def choose_material_type(mat_type, rng, materials=None):
    """ Return the materials the name of which is prefixed by a given string.

    Args:
    - mat_type (str) : the prefix to use to filter the materials
    - rng (random generator) : use to shuffle the list
    - materials (list of Materials=None) : list to work. Use the whole Materials list if None.

    Returns:
    - list of Materials: the filtered materials randomly ordered
    """

    mats = []
    if materials is None:
        mats = [mat.name for mat in bpy.data.materials if mat.name[:len(mat_type)] == mat_type]
    else:
        mats = [name for name in materials if name[:len(mat_type)] == mat_type]

    if len(mats):
        return mats[rng.choice(np.arange(len(mats)))]
    else:
        return None

def set_material(spec, material, faces=None):

    if material is None:
        return

    obj = get_object(spec)
    mat = create_material(material, reset=False)
    mat_index = obj.data.materials.get(mat.name)
    if mat_index is None:
        mat_index = len(obj.data.materials)
        obj.data.materials.append(mat)

    if isinstance(obj.data, bpy.types.Mesh):
        if faces is None:
            a = [mat_index]*len(obj.data.polygons)
            obj.data.polygons.foreach_set('material_index', a)
        else:
            a = np.zeros(len(obj.data.polygons))
            obj.data.polygons.foreach_get('material_index', a)
            a[faces] = mat_index
            obj.data.polygons.foreach_set('material_index', a)

def change_material_image(model, new_name, image, image_nodes=None):

    # ----- Source material

    mat0 = bpy.data.materials[model] if isinstance(model, str) else model

    # ----- Target material

    mat1 = bpy.data.materials.get(new_name)
    if mat1 is not None:
        return mat1

    mat1 = mat0.copy()
    mat1.name = new_name

    assert(mat1.use_nodes)

    # ----- Change the image

    nodes = mat1.node_tree.nodes
    images = []
    for node in nodes:
        if isinstance(node, bpy.types.ShaderNodeTexImage):

            if image_nodes is None:
                images.append(node)

            elif isinstance(image_nodes, str):
                if node.name == image_nodes:
                    images.append(node)

            elif node.name in image_nodes:
                images.append(node)

    if len(images) == 0:
        raise Exception(f"The material '{mat0.name}' doesn't have a image texture node with name matching: {image_nodes}")

    for node in images:
        node.image = image

    return mat1

# =============================================================================================================================
# Mesh Attributes

# ----------------------------------------------------------------------------------------------------
# Attribute exists

def attribute_exists(spec, name):
    """ Test if an attribute exists.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name

    Returns
    -------
        - bool : True if exists, False otherwise
    """

    data = get_data(spec)
    return data.attributes.get(name) is not None

# ----------------------------------------------------------------------------------------------------
# Attribute info

def get_attribute_info(spec, name):
    """ Get the attribute info.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name

    Returns
    -------
        - dict with attribute informations, None if the attribute doesn't exist
    """

    data = get_data(spec)
    battr = data.attributes.get(name)
    if battr is None:
        return None

    return {
        'domain'    : battr.domain,
        'name'      : name,
        'data_type' : battr.data_type,
        'count'     : len(battr.data),
        'battr'     : battr,
        }

# ----------------------------------------------------------------------------------------------------
# List of attributes

def get_attribute_names(spec):
    """ Get the name of the attributes of an object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data

    Returns
    -------
        - list of strs : attribute names
    """

    data = get_data(spec)
    return list(data.attributes.keys())

# ----------------------------------------------------------------------------------------------------
# List of attributes

def get_attributes(spec):
    """ Get all the informations of the attributes of a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data

    Returns
    -------
        - dict of dicts : attribute informations.
    """

    data = get_data(spec)
    return {name: get_attribute_info(data, name) for name in get_attribute_names(data)}

# ----------------------------------------------------------------------------------------------------
# Delete an attribute

def delete_attribute(spec, name):
    """ Delete an attribute.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
    """

    data = get_data(spec)

    battr = data.attributes.get(name)
    if battr is not None:
        data.attributes.remove(battr)

# ----------------------------------------------------------------------------------------------------
# Create an attribute

def create_attribute(spec, name, data_type, domain='POINT', value=None):
    """ Create an attribute into a Blender object.

    Note that if the attribute already exists, it is deleted.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - data_type (str) : attribute data type
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """

    data = get_data(spec)

    battr = data.attributes.get(name)
    if battr is None:
        data.attributes.new(name, type=data_type, domain=domain)

    if value is not None:
        set_attribute(data, name, value)


def create_float_attribute(spec, name, domain='POINT', value=None):
    """ Create a float attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """

    create_attribute(spec, name, data_type='FLOAT', domain=domain, value=value)

def create_int_attribute(spec, name, domain='POINT', value=None):
    """ Create an int attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='INT', domain=domain, value=value)

def create_bool_attribute(spec, name, domain='POINT', value=None):
    """ Create a bool attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='BOOLEAN', domain=domain, value=value)

def create_vector_attribute(spec, name, domain='POINT', value=None):
    """ Create a vector attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='FLOAT_VECTOR', domain=domain, value=value)

def create_vector2_attribute(spec, name, domain='CORNER', value=None):
    """ Create a vector2 attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='FLOAT2', domain=domain, value=value)

def create_color_attribute(spec, name, domain='POINT', value=None):
    """ Create a float color attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='FLOAT_COLOR', domain=domain, value=value)

def create_rgb_color_attribute(spec, name, domain='POINT', value=None):
    """ Create a rgb color attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='BYTE_COLOR', domain=domain, value=value)

# ----------------------------------------------------------------------------------------------------
# Get the attribute value

TYPES = {
    'FLOAT'         : {'dtype': float,  'size': 1, 'shape': (),   'name': 'value'},
    'INT'           : {'dtype': int,    'size': 1, 'shape': (),   'name': 'value'},
    'FLOAT_VECTOR'  : {'dtype': float,  'size': 3, 'shape': (3,), 'name': 'vector'},
    'FLOAT_COLOR'   : {'dtype': float,  'size': 4, 'shape': (4,), 'name': 'color'},
    'BYTE_COLOR'    : {'dtype': 'u1',   'size': 4, 'shape': (4,), 'name': 'color_srgb'},
    'STRING'        : {'dtype': 'U128', 'size': 0, 'shape': (),   'name': 'value'},
    'BOOLEAN'       : {'dtype': bool,   'size': 1, 'shape': (),   'name': 'value'},
    'FLOAT2'        : {'dtype': float,  'size': 2, 'shape': (2,), 'name': 'vector'},
    'INT8'          : {'dtype': int,    'size': 1, 'shape': (),   'name': 'value'},
    'INT32_2D'      : {'dtype': int,    'size': 2, 'shape': (2,), 'name': 'value'},
    }

def get_attribute(spec, name):

    data  = get_data(spec)
    battr = data.attributes[name]
    n     = len(battr.data)

    value_size = TYPES[battr.data_type]['size']
    value_name = TYPES[battr.data_type]['name']
    value_type = TYPES[battr.data_type]['dtype']

    # ----- String

    if battr.data_type == 'STRING':
        return [str(item.value) for item in battr.data]

    # ----- Byte color = read a float ansd store u8

    elif battr.data_type == 'BYTE_COLOR':
        a = np.empty(n*4, dtype=float)
        battr.data.foreach_get('color_srgb', a)
        return np.reshape(np.clip(a*255, 0, 255).astype(value_type), (n, 4))

    # ------ Other toes

    else:
        a = np.empty(n*value_size, dtype=value_type)
        battr.data.foreach_get(value_name, a)

        return np.reshape(a, (n,) + TYPES[battr.data_type]['shape'])

# ----------------------------------------------------------------------------------------------------
# Set attribute value

def set_attribute(spec, name, value):

    data  = get_data(spec)
    battr = data.attributes[name]
    n     = len(battr.data)

    value_size = TYPES[battr.data_type]['size']
    value_name = TYPES[battr.data_type]['name']
    value_type = TYPES[battr.data_type]['dtype']

    # ----- String

    if battr.data_type == 'STRING':
        if isinstance(value, str):
            for i in range(n):
                battr.data[i].value = value

        elif len(value) == 1:
            for i in range(n):
                battr.data[i].value = value[0]

        else:
            for i in range(n):
                battr.data[i].value = value[i]

        return

    # ----- Byte color type : internal is u8 -> need conversion to float

    if battr.data_type == 'BYTE_COLOR':
        if isinstance(value, np.ndarray):
            value = value/255
        else:
            value = np.array(value)/255
        value_type = float

    # ----- Set the array to the layer

    if n*value_size == np.size(value):
        battr.data.foreach_set(value_name, np.reshape(value, np.size(value)).astype(value_type))

    else:
        nvalues = np.size(value)//value_size
        if n % nvalues != 0:
            raise Exception(f"Set Attribute Error: Object attribute '{name}' len is {n} (size={n*value_size}). Impossible to set with value of shape {np.shape(value)} (size={np.size(value)}).")

        item_size = n//nvalues
        a = np.empty((nvalues, item_size, value_size), dtype=value_type)
        a[:] = np.reshape(value, (nvalues, 1, value_size))

        battr.data.foreach_set(value_name, np.reshape(a, np.size(a)))



# ====================================================================================================
# Pillow image

# ----------------------------------------------------------------------------------------------------
# Convert a pillow image into a blender image

def pil_to_image(pil_image, name="Pillow"):
    """ Convert a Pillow image into a Blender Image.

    Args:
    - pil_image : image in the pillow format
    - name (str='Pillow') : named to give to the Blender new image.

    Returns:
    - Image : the converted image
    """

    image = bpy.data.images.new(name, pil_image.width, pil_image.height)
    a = np.insert(np.array(pil_image)/255, 3, 1, -1)
    image.pixels[:] = np.reshape(np.flip(a, axis=0), np.size(a))

    return image

# ----------------------------------------------------------------------------------------------------
# Convert a pillow array into a blender image

def pil_array_to_image(pil_array, name="Pillow"):
    """ Convert a Pillow arrayinto a Blender Image.

    Args:
    - pil_array : pillow array
    - name (str='Pillow') : named to give to the Blender new image.

    Returns:
    - Image : the converted image
    """

    image = bpy.data.images.new(name, np.shape(pil_array)[1], np.shape(pil_array)[0])
    a = np.insert(pil_array/255, 3, 1, -1)
    image.pixels[:] = np.reshape(np.flip(a, axis=0), np.size(a))

    return image

# ----------------------------------------------------------------------------------------------------
# Get the texture image node of a material

def get_image_node(mat, label='Generated'):
    """ Get the node image of a Material shader.

    The name of the node image is used in case several Image Nodes exist.

    Args:
    - mat (Material) : the material to get the node Image from
    - label (str='Generated') : named of the node image

    Returns:
    - None or Image Node
    """

    if isinstance(mat, str):
        mat = bpy.data.materials[mat]

    nodes = [node for node in mat.node_tree.nodes if node.bl_idname == "ShaderNodeTexImage" ]
    if len(nodes) == 1:
        return nodes[0]

    for node in nodes:
        if node.label == label:
            return node

    raise Exception(f"Material '{mat.name}' has several 'Image Texture' nodes. One must be labeled '{label}'")


# ====================================================================================================
# Markers

def markers(text, clear=True, start=0):
    """Create markers from a text made of lines.

    Each line contains a frame number and a name. These two tokens can be separated
    by a comma, a semi-column or a tab.

    Args:
    - text (string) : lines separated by \n.
    - clear (bool=True) : delete the existing markers if True
    - start (int=0) : frame number to start from
    """

    print('-'*10)
    print("Markers...")
    fails = 0
    total = 0

    scene = bpy.context.scene

    if clear:
        scene.timeline_markers.clear()

    frame_min = 1000000
    frame_max = 0

    # ----- Split the lines
    lines = text.split('\n')

    mks = []

    # ----- First pass to compute min an max
    for line in lines:

        total += 1

        # Split with possible separators
        ko = True
        for sep in [',', '\t', ';']:
            # Empty line !
            if (line == "") or (line.strip() == sep):
                total -= 1
                ko = False
                break

            # Not empty line
            else:
                fr_na = line.split(sep)
                if len(fr_na) == 2:
                    try:
                        frame = int(fr_na[0])
                        mks.append((frame, fr_na[1].strip()))
                        frame_min = min(frame_min, frame)
                        frame_max = max(frame_max, frame)

                        ko = False
                        break
                    except:
                        pass

        if ko:
            fails += 1
            print(f"Markers: unable to handle the line: '{line}'")

    # ----- Loop on the markers to set
    for fr_na in mks:
        scene.timeline_markers.new(fr_na[1], frame=start + fr_na[0] - frame_min)

    # ----- Start and end frames
    scene.frame_start = start
    scene.frame_end   = start + frame_max - frame_min

    # ----- Synthesis
    print(f"Markers from {start} to {start + frame_max - frame_min}: {total} line(s), {fails} fail(s)")


def fps():
    return bpy.context.scene.render.fps

def marker_frame(name):
    if isinstance(name, str):
        return bpy.context.scene.timeline_markers[name].frame
    else:
        return name

def frtime(frame):
    scene = bpy.context.scene
    return (marker_frame(frame) - scene.frame_start)/scene.render.fps

def frdur(frame0, frame1):
    return (marker_frame(frame1) - marker_frame(frame0))/bpy.context.scene.render.fps

def frame_at(t):
    return bpy.context.scene.frame_start + round(t*fps())

# ====================================================================================================
# Blender fcurves management

# ----------------------------------------------------------------------------------------------------
# Return the data_path and in the index of a name path

def data_path_index(data, name, index=-1):
    """Key frame utility: normalize the syntax name, index of a key frame.

    Used for instance for location. The syntax "location.x" can be used rather
    than the Blender syntax: "location", index=0.

    Transforms: location.y, -1 --> location, 1

    If index is not -1 and the dotted syntaxe is used, an error is raised.

    Args:
    - name (str) : the name of the attribute with possible the syntax attr.x.
    - index (int=-1) : for array attribute, the index of the entry. The default is -1.


    Returns:
    - couple (str, int) : The not dotted attribute name and in the index in the array
    """

    # ----- Custom property

    if '[' in name:
        return data, name, index

    # ----- Items

    attrs = name.split('.')
    if len(attrs) == 1:
        return data, name, index

    idx = index
    if idx == -1 and attrs[-1] in ["x", "y", "z", "w"]:
        idx = ["x", "y", "z", "w"].index(attrs[-1])
        del attrs[-1]

    if len(attrs) == 1:
        return data, attrs[0], idx

    for attr in attrs[:-1]:
        data = getattr(data, attr)

    return data, attrs[-1], idx


# ----------------------------------------------------------------------------------------------------
# Get a blender fcurve

def get_fcurve(spec, name, index=-1, create=True):
    """ Get a Blender fcurve.

    Args:
    - spec (str or Object) : the Object
    - name (str) : name of the attribute
    - index (int=-1) : index in the array
    - create (bool=True) : create the fcurve if it doesn't exist

    Returns:
    - fcurve or None
    """

    obj = get_object(spec)

    data, data_path, index = data_path_index(obj, name, index)


    # ----- animation

    animation = data.animation_data
    if animation is None:
        if create:
            animation = data.animation_data_create()
        else:
            return None

    # ----- action

    if animation.action is None:
        if create:
            animation.action = bpy.data.actions.new(name=f"{obj.name} action")
        else:
            return None

    # ----- Look in fcurves

    fcurves = animation.action.fcurves
    for fc in fcurves:
        if fc.data_path == data_path and (fc.array_index == index or index==-1):
            return fc

    if not create:
        return None

    # --- Create

    return fcurves.new(data_path=data_path, index=index)

# ----------------------------------------------------------------------------------------------------
# reset keyframes

def fc_clear(fc, frame0=None, frame1=None):
    """ Clear the points of a fcurve.

    Args:
    - fc (fcurve) : the fcurve to clear
    - frame0 (int=None) : clear from that frame
    - frame1 (int=None) : clear to that frame

    Returns:
    - None
    """

    kfs = []
    for i_kf, kf in enumerate(fc.keyframe_points):

        if frame0 is None:
            suppr = True
        else:
            suppr = kf.co[0] >= frame0

        if suppr and frame1 is not None:
            suppr = kf.co[0] <= frame1

        if suppr:
            kfs.append(i_kf)

    for i_kf in reversed(kfs):
        fc.keyframe_points.remove(fc.keyframe_points[i_kf])

# ----------------------------------------------------------------------------------------------------
# Set a list of keyframes

def fc_set_kfs(fc, kfs):

    from mathutils import Vector

    fc.keyframe_points.clear()
    fc.keyframe_points.add(len(kfs))

    for kf, in_kf in zip(fc.keyframe_points, kfs):
        kf.amplitude         = in_kf.amplitude
        kf.back              = in_kf.back
        kf.easing            = in_kf.easing
        kf.co                = Vector(in_kf.co)
        kf.handle_left       = Vector(in_kf.handle_left)
        kf.handle_right      = Vector(in_kf.handle_right)
        #kf.handle_left_type  = in_kf.handle_left_type
        #kf.handle_right_type = in_kf.handle_right_type
        kf.interpolation     = in_kf.interpolation
        kf.period            = in_kf.period
        #kf.type              = in_kf.type

    return fc


# ----------------------------------------------------------------------------------------------------
# Set a new keyframe in a fcurve

def fc_set_keyframe(fc, frame, value, interpolation=None):
    """ Set a new keyframe.

    Args:
    - fc (fcurve) : the fcurve to create a keyframe into
    - frame(int or float) : the frame
    - value (float) : the value at the frame
    - interpolation (str=None) : a valid interpolation mode

    Returns:
    - KeyFrame : the created keyframe
    """

    for kf in fc.keyframe_points:
        if abs(kf.co[0] - frame) < 0.1:
            kf.co[1] = value
            if interpolation is not None:
                kf.interpolation = interpolation
                return kf

    kf = fc.keyframe_points.insert(frame, value)
    if interpolation is None:
        kf.interpolation = 'BEZIER'
    else:
        kf.interpolation = interpolation

    fc.update()

    return kf

# ----------------------------------------------------------------------------------------------------
# Keyframe by path

def kf_clear(spec, name, frame0=None, frame1=None):
    """ Clear a keyframe.

    Args:
    - spec (str or Object) : the Object
    - name (str) : name of the fcurve
    - frame0 (int=None) : clear from that frame
    - frame1 (int=None) : clear to that frame

    Returns:
    - None
    """

    fc = get_fcurve(spec, name, create=None)
    if fc is not None:
        fc_clear(fc, frame0=frame0, frame1=frame1)

def set_key_frame(spec, name, frame, value, interpolation=None):
    """ Set a keyframe.

    Args:
    - spec (str or Object) : the Object
    - name (str) : name of the fcurve
    - frame(int or float) : the frame
    - value (float) : the value at the frame
    - interpolation (str=None) : a valid interpolation mode

    Returns:
    - KeyFrame : the created keyframe
    """

    return fc_set_keyframe(get_fcurve(spec, name), frame, value, interpolation=interpolation)


def get_value_at_frame(frame, spec, name, index=-1):
    """ Get the value of an attribute possibly keyed.

    Arguments
    ---------
        - frame (int) : frame at which the value is needed
        - spec (data spec) : data owning the property
        - name (str) : attribute name
        - index (int = -1) : index for vector attributes

    Returns
    -------
        - value
    """

    obj = get_object(spec)
    data, data_path, index = data_path_index(obj, name, index)

    # ----- Ref value

    if '[' in data_path:
        ref_value = eval(f"data{data_path}")
    else:
        ref_value = getattr(data, data_path)

    # ----- Target is a Vector or a list and we need all components

    if hasattr(ref_value, '__len__') and index == -1:
        v = []
        for i in range(len(ref_value)):
            v.append(get_value_at_frame(frame, data, data_path, index=i))

        if isinstance(ref_value, idprop.types.IDPropertyArray):
            return list(v)
        elif isinstance(ref_value, Vector):
            return Vector(v)
        else:
            return v

    # ----- Only a single value is required

    fcurve = get_fcurve(data, data_path, index, create=False)

    if fcurve is None:
        if index >= 0:
            return ref_value[index]
        else:
            return ref_value
    else:
        return fcurve.evaluate(frame)



# ====================================================================================================
# A Key frame

class KeyFrame:

    def __init__(self, frame, value):
        """ KeyFrame class takes same arguments as Blender KeyFrame.

        This class is used for operations on fcurves.

        Args:
        - frame (int or float) : the frame
        - value (float) : the keyframe value
        """

        self.amplitude         = 0.
        self.back              = 0.
        self.co                = Vector((frame, value))
        self.easing            = 'AUTO'
        self.handle_left       = Vector((0., 0.))
        self.handle_right      = Vector((0., 0.))
        self.handle_left_type  = 'FREE'
        self.handle_right_type = 'FREE'
        self.interpolation     = 'CONSTANT'
        self.period            = 0.
        self.type              = 'KEYFRAME'

    @classmethod
    def FromKeyFrame(cls, kf):
        """ Initialize from a Blender keyframe.

        Args:
        - kf (Blender KeyFrame) : the keyframe to copy
        """

        new_kf = cls(kf.co[0], kf.co[1])

        new_kf.amplitude         = kf.amplitude
        new_kf.back              = kf.back
        new_kf.easing            = kf.easing
        new_kf.handle_left       = Vector(kf.handle_left)
        new_kf.handle_right      = Vector(kf.handle_right)
        new_kf.handle_left_type  = kf.handle_left_type
        new_kf.handle_right_type = kf.handle_right_type
        new_kf.interpolation     = kf.interpolation
        new_kf.period            = kf.perdio
        new_kf.type              = kf.type

    def to_keyframe(self, kf):
        """ Copy attributes to a Blender KeyFrame

        Args:
        - kf (Blender KeyFrame) : the keyframe to setup
        """

        kf.amplitude         = self.amplitude
        kf.back              = self.back
        kf.easing            = self.easing
        kf.handle_left       = Vector(self.handle_left)
        kf.handle_right      = Vector(self.handle_right)
        kf.handle_left_type  = self.handle_left_type
        kf.handle_right_type = self.handle_right_type
        kf.interpolation     = self.interpolation
        kf.period            = self.perdio
        kf.type              = self.type


# ====================================================================================================
# A Function curve

class FCurve(list):

    def __init__(self, spec, name):

        self.fc = get_fcurve(spec, name)
        for kf in fc.keyframe_points:
            self.append(KeyFrame.FromKeyFrame(kf))

    def to_fcurve(self, fc):

        fc.keyframe_points.clear()
        fc.keyframe_points.add(len(self))

        for kf0, kf1 in zip(self, fc.keyframe_points):
            kf0.to_keyframe(kf1)


# ====================================================================================================
# Shape keys
#
# shape keys are organized
#
# object
#      shape_keys (Key)
#           key_blocks (Prop Collection of ShapeKey)
#                data (Prop Collection of
#                     ShapeKeyPoint
#                     ShapeKeyBezierPoint
#                     ShapeKeyCurvePoint
#
# cube.data.shape_keys.key_blocks[].data[].co
#
# A key is either a string (name of the shape) or an int (index in the array)
# Series are managed through a key name and a number of steps

def get_shape_keys_OLD(spec):

    obj = get_object(spec)

    if obj.data.shape_keys is None:
        return None

    n = len(obj.data.vertices)
    a = np.empty(n*3, float)

    verts = np.empty((len(obj.data.shape_keys.key_blocks), len(obj.data.vertices), 3), float)
    for index, key_block in enumerate(obj.data.shape_keys.key_blocks):
        key_block.data.foreach_get('co', a)
        verts[index] = np.reshape(a, (n, 3))

    return verts

# ====================================================================================================
# Shape Keys

def has_shape_keys(spec):

    obj = get_object(spec, halt=False)

    if obj is None:
        return False

    return obj.data.shape_keys is not None

def shape_keys_count(spec):

    obj = get_object(spec, halt=False)

    if obj is None or obj.data.shape_keys is None:
        return 0

    return len(obj.data.shape_keys.key_blocks)

def shape_keys_clear(spec):

    obj = get_object(spec, halt=False)

    if obj is None or obj.data.shape_keys is None:
        return

    for shapekey in obj.data.shape_keys.key_blocks:
        obj.shape_key_remove(shapekey)

def get_key_block(spec, index, create=False, name=None):

    obj = get_object(spec)

    if obj.data.shape_keys is None:
        obj.shape_key_add()

    kbs = obj.data.shape_keys.key_blocks

    if create:
        for _ in range(len(kbs)-1, index):
            obj.shape_key_add()

    if index >= len(kbs):
        return None
    else:
        if name is not None:
            kbs[index].name = name
        return kbs[index]

# ====================================================================================================
# Bake a frame

def bake_frame(collection, names=None, frame=None, reset=False):

    from geonodes.core.meshbuilder import MeshBuilder

    coll = create_collection(collection)

    # ----- Delete existing frames

    if reset:
        objs = [obj for obj in coll.objects]
        for obj in objs:
            mesh = obj.data
            bpy.data.objects.remove(obj)
            bpy.data.meshes.remove(mesh)

    # ----- Build the object

    if names is None or frame is None:
        return None

    mbs = MeshBuilder()

    for name in names:
        mb = MeshBuilder.FromObject(name)
        mbs.append(mb)

    obj = create_mesh_object(f"Frame {frame:03d}", collection=coll)
    mbs.to_object(obj)

    kf_set(obj, 'hide_render',   0,       True, 'CONSTANT')
    kf_set(obj, 'hide_render',   frame,   False)
    kf_set(obj, 'hide_render',   frame+1, True)

    kf_set(obj, 'hide_viewport', 0,       True, 'CONSTANT')
    kf_set(obj, 'hide_viewport', frame,   False)
    kf_set(obj, 'hide_viewport', frame+1, True)

    return obj

# ====================================================================================================
# Rendering

def is_viewport():
    return bpy.context.workspace is not None

def lock_interface(value):
    bpy.context.scene.render.use_lock_interface = value

def render_engine():
    return bpy.context.scene.render.engine
