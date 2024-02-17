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

A more userfriendly way is to create parameters which can be set anc keyed in the object property panel.

This panel is named "GeoPy Parameters" and is displayed in the object property panel.

When a property is needed, it is created as a Custom Property of the object.
The name of this Custom Property is prefixed by a group prefix in order to allow several groups of
parameters to coexist.

for instance, a transformation need as 'scale' parameter and another transformation needs also a 'scale' parameter.
These two differents parameters can defined in to groups when the two transformations are performed on the same  object.

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
from geopy.core import blender

GROUPS = {}

OBJ_GROUP_LIST = "gp Groups"

PROP_SUBTYPES = ['NONE', 'FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'PIXEL', 
                 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE', 
                 'DISTANCE_CAMERA', 'POWER', 'TEMPERATURE', 'COLOR', 'TRANSLATION', 'DIRECTION',
                 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 
                 'XYZ_LENGTH', 'COLOR_GAMMA', 'COORDINATES', 'LAYER', 'LAYER_MEMBER']

# ====================================================================================================
# One custom property

class CustomProp:
    def __init__(self, prefix, name, value, description="", **attrs):
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
            id_prop.update(**self.attrs)
            
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
        
        if frame is None:
            v = obj.get(self.gp_name)
            if v is None:
                self.to_object(obj)
                return obj[self.gp_name]
            else:
                return v
        else:
            return blender.get_value_at_frame(frame, obj, f'["{self.gp_name}"]')
        
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
        
    def __str__(self):
        return f"<Parameters group '{self.name}' : {list(self.keys())}>"
        
    def new(self, name, value, description="", **attrs):
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
        
        self[name] = CustomProp(self.prefix, name, value, description=description, **attrs)
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
       
        for cprop in self.values():
            cprop.to_panel(layout, obj)
            
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
    
    prefix = f"gp{len(GROUPS)}"
    cprops = CustomProps(prefix, name)
    GROUPS[prefix] = cprops
    return cprops

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
    
    names = []
    for group in GROUPS.values():
        if group.name == name:
            return group
        names.append(name)
        
    raise Exception(f"Group named {name} nor found in {names}")
            
# ====================================================================================================
# Layout
            
class GeoPyPanel(bpy.types.Panel):
    """GeoPy parameters"""
    bl_label = "GeoPy Parameters"
    bl_idname = "OBJECT_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        
        if len(GROUPS) == 0:
            layout.label(text='No parameter group defined')
            layout.label(text="Use: group = geopy.new_param_group(name)")
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
            layout.label(text="Use geopy.param_group(name).to_object(object)")
            layout.label(text="   to set parameters to the object")
            return
        
        # ----- Loop on the groups
        
        for prefix in groups.split("|"):
            #if not first:
            #    layout.split()
            #first = False
            box = layout.box()
            cprops = GROUPS.get(prefix)
            if cprops is None:
                box.row().label(text=f"Prefix {prefix} not initialized...")
            else:
                box.row().label(text=cprops.name)
                cprops.to_panel(box, obj)



def register():
    bpy.utils.register_class(GeoPyPanel)


def unregister():
    bpy.utils.unregister_class(GeoPyPanel)

try:
    unregister()
except:
    pass

register()



            
            
            