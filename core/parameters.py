#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Sat Dec  9 09:24:40 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Custom properties used as parameters.

Operations performed with GeoPy can require parameters from user. Moreover, these parameters can be keyed in
order to perform animations.

User can use existing properties of a control object, such as the location of an empty.

A more userfriendly way is to create parameters which can be set and keyed in the object property panel.

This panel is named "GeoPy Parameters" and is displayed in the object property panel.

When a property is needed, it is created as a Custom Property of the object.
The name of this Custom Property is prefixed by a group prefix in order to allow several groups of
parameters to coexist.

For instance, a transformation need as 'scale' parameter and another transformation needs also a 'scale' parameter.
These two differents parameters can be defined in two groups when the two transformations are performed on
the same object.

Here after is the pseudo code to create and use user parameters

``` python
import parameters

# ----- Create a group of parameters which will be accessible in the Object properties UI panel

group = parameters.new_param_group("My Parameters")

# ----- Create the parameters

group.new("Count", 10, min=1, max=10, description="Number of items")

# ----- Transfer to an existing object
# This operation creates the custom properties into the object
# After this operation, the Object properties UI panel will display the required properties
# for this object

group.to_object("My Object")

# If other group are needed, they can also be transferred

other_group.to_object("My Object")

# ----- The parameter can be read from the object

param_value = group.get_value("My Object", "Count")

# ----- The parameter can be keyed and accessed in a loop

def update(eng):

    # ----- Group can be read if it has been defined out of the function scope

    group = parameters.param_group("My Parameters")

    # ----- Read the parameter value which can keyed

    count = group.get_value(obj, "Count")

    # ----- It can be used to whatever purpose

    # ...


# ----- Launch the animation

gp.engine.go(update)
```

"""

import bpy
import idprop
from geonodes.core import blender, engine

GROUPS = {}

def get_group_by_name(name):
    return GROUPS.get(name)

def get_group_by_prefix(prefix):
    for item in GROUPS.values():
        if item.prefix == prefix:
            return item
    return None


OBJ_GROUP_LIST = "gp Groups"

PROP_SUBTYPES = ['NONE', 'FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'PIXEL',
                 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE',
                 'DISTANCE_CAMERA', 'POWER', 'TEMPERATURE', 'COLOR', 'TRANSLATION', 'DIRECTION',
                 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ',
                 'XYZ_LENGTH', 'COLOR_GAMMA', 'COORDINATES', 'LAYER', 'LAYER_MEMBER']

# ====================================================================================================
# One custom property

class CustomProp:
    def __init__(self, prefix, name, value, description="", panel=None, **attrs):
        """ A Custom property.

        Arguments
        ---------
            - prefix (str) : group prefix, common to all properties of the same group
            - name (str) : property name
            - value (any) : property value
            - description (str = "") : pop over help text
            - **attrs : keywords valid in layout.prop method
        """

        self.prefix      = prefix
        self.name        = name
        self.gp_name     = f"{self.prefix} {self.name}"
        self.value       = value
        self.description = description
        self.panel       = panel
        self.attrs       = attrs

    def to_object(self, spec, override=False):
        """ Create the custom properties in an object.

        Arguments
        ---------
            - spec (str of obj) : the object
        """

        obj = blender.get_object(spec)

        cur = obj.get(self.gp_name)

        if cur is None or override:
            obj[self.gp_name] = self.value

        if len(self.attrs):
            id_prop = obj.id_properties_ui(self.gp_name)
            id_prop.update(description=self.description, **self.attrs)

    def to_panel(self, layout, obj):
        """ Write the property into a layout.

        Arguments
        ---------
            - layout (bpy.types.UILayout) : the layout
            - obj (bpy.types.Object) : the object
        """

        row = layout.row()
        row.use_property_split = True
        row.use_property_decorate = True
        row.prop(obj, f'["{self.gp_name}"]', text=self.name, text_ctxt=self.description)

    def get_value(self, obj, frame=None):
        """ Read the value from the object.

        Arguments
        ---------
            - spec (str of obj) : the object
            - frame (int = None) : frame where the evaluation is required

        Returns
        -------
            - value
        """

        # ----- If frame is None, default is to get from Engine if rendering in progress

        if frame is None and engine.Engine.rendering:
            frame = engine.Engine.frame

        if frame is None:
            v = obj.get(self.gp_name)

            if v is None:
                self.to_object(obj)
                v = obj[self.gp_name]

        else:
            v = blender.get_value_at_frame(frame, obj, f'["{self.gp_name}"]')

        if isinstance(v, idprop.types.IDPropertyArray):
            return list(v)
        else:
            return v


# ====================================================================================================
# A group of custom properties

class CustomProps(dict):

    def __init__(self, prefix, name):
        """ A consistent group of custom properties.

        Arguments
        ---------
            - prefix (str) : group prefix, used as unique key
            - name (str) : group name
        """

        super().__init__()
        self.prefix = prefix
        self.name   = name
        self.panels = []

    def __str__(self):
        return f"<Parameters group '{self.name}' : {list(self.keys())}>"

    def add_panel(self, *name):
        self.panels.extend(name)

    def new(self, name, value, description="", panel=None, **attrs):
        """ Create a new property in the group.

        Arguments
        ---------
            - name (str) : property name
            - value (any) : property value
            - description (str = "") : pop over help text
            - **attrs : keywords valid in layout.prop method

        Returns
        -------
            - CustomProp
        """

        self[name] = CustomProp(self.prefix, name, value, description=description, panel=panel, **attrs)
        if panel is not None and panel not in self.panels:
            self.panels.append(panel)

        return self.name

    def get_value(self, spec, name, frame=None):
        """ Read the value from the object.

        Arguments
        ---------
            - spec (str of obj) : the object
            - name (str) : the property name
            - frame (int = None) : the frame at which the evaluation is required

        Returns
        -------
            - value
        """

        return self[name].get_value(blender.get_object(spec), frame=frame)

    def to_object(self, spec, override=False):
        """ Write the properties into an object.

        Arguments
        ---------
            - spec (str of obj) : the object
        """

        obj = blender.get_object(spec)

        cur = obj.get(OBJ_GROUP_LIST)
        if cur is None:
            obj[OBJ_GROUP_LIST] = self.prefix
            override = True
        else:
            if not self.prefix in cur.split('|'):
                obj[OBJ_GROUP_LIST] = f"{cur}|{self.prefix}"
                override = True

        for cprop in self.values():
            cprop.to_object(obj, override=override)


    def to_panel(self, layout, obj):
        """ Write the property into a layout.

        Arguments
        ---------
            - layout (bpy.types.UILayout) : the layout
            - obj (bpy.types.Object) : the object
        """

        # ----- Properties without panel

        for cprop in self.values():
            if cprop.panel is None:
                cprop.to_panel(layout, obj)

        # ----- Properties within panel

        for panel_name in self.panels:
            if True:
                header, panel = layout.panel(self.prefix + panel_name, default_closed=False)
                header.label(text=panel_name)
            else:
                box = layout.box()
                box.label(text=panel_name)
                panel = box

            for cprop in self.values():
                if panel is None:
                    continue
                if cprop.panel == panel_name:
                    cprop.to_panel(panel, obj)


# ====================================================================================================
# Create a property group

def new_param_group(name):
    """ Create a new group of properties

    ``` python
    obj = gp.blender.create_mesh_object("Cube")

    group = parameters.new_param_group("Possible types")

    group.new("Float", .5, min=0, max=1, description="Float test between 0 and 1")
    group.new("Factor", 50, min=0, max=100, subtype='PERCENTAGE', description="Factor between 0 and 100%")
    group.new("Int",   1, min=0, max=20, soft_max=10, description="Int between 0 and 20 with softmax at 10")
    group.new("Speed", 1.1234, min=0, subtype='VELOCITY', description="The speed of the cube...")
    group.new("Bool",  False, description="Boolean flag")
    group.new("Vector", (1.1234, 5, 7), subtype='VELOCITY', description="Vector")
    group.to_object(obj)


    group = parameters.new_param_group("Another Group")

    group.new("Float", 1.1234, min=0, max=2, description="Same name as in previous group")
    group.new("Vector 2", (1., 2), description="Vector 2D")
    group.new("Vector 3", (1., 2, 3), description="Vector 3D")
    group.new("Vector 4", (1., 2, 3, 4), description="Vector 4D")
    group.new("Vector 5", (1., 2, 3, 4, 5), description="Vector 5D")
    group.to_object(obj)

    group = parameters.new_param_group("Control")
    group.new("Top scale", .5, min=0, max=1, description="Same name as in previous group")

    group.to_object(obj)

    def update(eng):
        props = parameters.param_group("Control")

        mesh = gp.Mesh.Cube()
        scale = props.get_value("Cube", "Top scale")
        print("SCALE", scale)

        mesh.points[[1, 3, 5, 7]].scale((scale, scale, 1.))
        mesh.to_object("Cube")

    gp.engine.go(update)
    ```

    Arguments
    ---------
        - name (str) : group name

    Returns
    -------
        - CustomProps
    """

    cprops = GROUPS.get(name)
    if cprops is not None:
        cprops.clear()
        return cprops

    prefix = f"gp{len(GROUPS)}"
    GROUPS[name] = CustomProps(prefix, name)
    return GROUPS[name]

# ====================================================================================================
# Get a Group by its name

def param_group(name):
    """ Get the group by its name.

    Arguments
    ---------
        - name (str) : group name

    Returns
    -------
        - CustomProps
    """

    try:
        return GROUPS[name]
    except:
        raise Exception(f"Group named {name} nor found in {list(GROUPS.keys())}")


    names = []
    for group in GROUPS.values():
        if group.name == name:
            return group
        names.append(name)

    raise Exception(f"Group named {name} nor found in {names}")

# ====================================================================================================
# ObjectParams

class ObjectParams:
    def __init__(self, obj, name):
        self.obj    = blender.get_object(obj)
        self.cprops = param_group(name)
        self.cprops.to_object(self.obj, override=False)

    def get_value(self, name, frame=None):
        return cprops.get_value(self.obj, name, frame=frame)

    def __getattr__(self, name):
        for key, cprop in self.cprops.items():
            if key.lower().replace(' ', '_') == name:
                return cprop.get_value(self.obj, frame=None)


# ====================================================================================================
# Layout

class GeoNodesPanel(bpy.types.Panel):
    """GeoNodes parameters"""
    bl_label = "GeoNodes Parameters"
    bl_idname = "OBJECT_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        if len(GROUPS) == 0:
            layout.label(text='No parameter group defined')
            layout.label(text="Use: group = geonodes.new_param_group(name)")
            layout.label(text="   to create a group")
            layout.label(text="Use: group.to_object(object)")
            layout.label(text="   to set parameter to the object")
            return

        # ----- Get the active object

        obj = bpy.context.view_layer.objects.active

        # Does it have GeoPy properties ?

        groups = obj.get(OBJ_GROUP_LIST)
        if groups is None:
            layout.label(text='No group defined for this object')
            layout.label(text="Use geonodes.param_group(name).to_object(object)")
            layout.label(text="   to set parameters to the object")
            return

        # ----- Loop on the groups

        for prefix in groups.split("|"):
            if True:
                header, panel = layout.panel(prefix, default_closed=False)
            else:
                box = layout.box()
                panel = box

            cprops = get_group_by_prefix(prefix)
            if cprops is None:
                if True:
                    header.row().label(text=f"Prefix {prefix} not initialized...")
                else:
                    panel.row().label(text=f"Prefix {prefix} not initialized...")
            else:
                if True:
                    header.row().label(text=cprops.name)
                else:
                    panel.row().label(text=cprops.name)
                cprops.to_panel(panel, obj)



def register():
    bpy.utils.register_class(GeoNodesPanel)


def unregister():
    bpy.utils.unregister_class(GeoNodesPanel)

try:
    unregister()
except:
    pass

register()
