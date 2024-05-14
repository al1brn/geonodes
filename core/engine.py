#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:33:23 2022

@author: alain.bernard
"""

import bpy
from bpy.types import Depsgraph

# ====================================================================================================
# Wrap a scene to offer additional features:
# - first call flag
# - time calculation
# - continuous time
# - sub frames
#
# Order of events is:
#
# Render PRE  None
# Change PRE  None
# Change POST depsgraph
# rendering and saving image ...
# Render POST None


class Engine:
    """ Simplify the use of frame_change_pre and offer additional features.

    The class is not supposed to be instantied. It has only class attributes and methods.
    """

    scene       = None
    #setup       = None

    first_call  = True
    last_frame  = None

    subframes   = 0
    subframe    = 0

    rendering   = False
    depsgraph   = None

    # ----- List of functions to call: couple of (func, setup)

    functions   = []

    # ----------------------------------------------------------------------------------------------------
    # Has setup

    @classmethod
    @property
    def has_setup(cls):

        for _, setup in cls.functions:
            if setup is not None:
                return True
        return False

    # ----------------------------------------------------------------------------------------------------
    # Frame

    @classmethod
    @property
    def is_frame(cls):
        return cls.subframe == 0

    # ----------------------------------------------------------------------------------------------------
    # Time

    @classmethod
    @property
    def time(cls):
        return (cls.frame - cls.scene.frame_start)/cls.scene.render.fps
        #return cls.time_offset + (cls.frame - cls.scene.frame_start)/cls.scene.render.fps

    @classmethod
    @property
    def duration(cls):
        return (cls.scene.frame_end - cls.scene.frame_start)/cls.scene.render.fps

    @classmethod
    @property
    def dt(cls):
        return 1/cls.scene.render.fps/(cls.subframes + 1)

    # ----------------------------------------------------------------------------------------------------
    # Motion blur class update several times

    @classmethod
    @property
    def use_motion_blur(cls):
        return cls.scene.render.use_motion_blur

    # ----------------------------------------------------------------------------------------------------
    # depsgraph helper

    @staticmethod
    def get_evaluated(spec):
        obj = bpy.data.objects[spec] if isinstance(spec, str) else spec
        if Engine.depsgraph is None:
            depsgraph = bpy.context.evaluated_depsgraph_get()
            return obj.evaluated_get(depsgraph)
        else:
            return obj.evaluated_get(Engine.depsgraph)

def is_viewport():
    return not Engine.rendering

def rendering():
    return Engine.rendering

def lock_interface(value):
    bpy.context.scene.render.use_lock_interface = value

# ====================================================================================================
# Add a function

def add(f, setup=None):
    Engine.functions.append((f, setup))

# ====================================================================================================
# Animation is:
# - one reset
# - one call of step at each frame change

# ----------------------------------------------------------------------------------------------------
# Reset
# Called at start rendering or when frame is before last frame

def reset():
    Engine.first_call  = True
    Engine.last_frame  = None

    display = "Engine> User setup"

    for _, setup in Engine.functions:
        if setup is None:
            continue

        if display is not None:
            print(display)
            display = None

        setup(Engine)

# ----------------------------------------------------------------------------------------------------
# One step

def step():

    # ----- Call for current frame

    for f, _ in Engine.functions:
        f(Engine)

    Engine.first_call = False

    # ----- If sub frame, call till 1 sub frame before next one

    if Engine.subframes > 0:
        for i in range(Engine.subframes - 1):
            Engine.subframe = i+1
            for f, _ in Engine.functions:
                f(Engine)

        Engine.subframe = 0

    # ----- Store last frame

    Engine.last_frame = Engine.frame

# ====================================================================================================
# Viewport animation
# Frame change - handler: frame_change_pre

def update(scene, depsgraph):

    # ----- Rendering : update is done by the function

    if Engine.rendering:
        Engine.depsgraph = depsgraph
        before_render_image(scene, depsgraph)
        Engine.depsgraph = None
        return

    Engine.scene = scene

    # ----- If update, need to simulate lost frames

    if Engine.has_setup:
        if Engine.last_frame is None:
            Engine.last_frame = scene.frame_start - 1
        else:
            if Engine.last_frame >= scene.frame_current:
                reset()
                Engine.last_frame = scene.frame_start - 1

        for frame in range(Engine.last_frame, scene.frame_current - 1):
            Engine.frame = frame
            step()

    # ----- Points to the right scene

    Engine.scene = scene
    Engine.frame = scene.frame_current

    # ----- One step

    step()

# ====================================================================================================
# Render animation
# - Capture start and end rendering
# - When rendering starts, call reset
# - Call step at each new frame

# ----------------------------------------------------------------------------------------------------
# Render init - handler: render_init

def before_render(scene):

    print("Engine> Start rendering")

    # To be sure
    lock_interface(True)

    Engine.rendering = True
    reset()

# ----------------------------------------------------------------------------------------------------
# Render done - handler: render_complete and render_cancel

def after_render(scene):
    print("Engine> Render finished")
    Engine.rendering = False
    Engine.depsgraph = None


# ----------------------------------------------------------------------------------------------------
# Render image - handler: render_pre

def before_render_image(scene, depsgraph):

    # ----- Points to the right scene
    # depsgraph has been set by update

    Engine.scene = scene
    Engine.frame = scene.frame_current
    print(f"Engine> Frame {Engine.frame}")
    step()

    return


    # ----- Compute all the frame up to the current one

    frame0 = Engine.last_frame
    if frame0 is None:
        frame0 = scene.frame_start - 1

    for frame in range(frame0 + 1, scene.frame_current + 1):
        Engine.frame = frame
        print(f"Engine> Frame {Engine.frame}")
        step()

# ====================================================================================================
# Module initialization

def init(subframes=0):

    Engine.subframes    = subframes
    Engine.subframe     = 0

    Engine.functions.clear()

    if True:
        # Handle on change post to get the depsgraph

        # ----- Frame change
        bpy.app.handlers.frame_change_post.clear()
        bpy.app.handlers.frame_change_post.append(update)

        # ----- Render init
        bpy.app.handlers.render_init.clear()
        bpy.app.handlers.render_init.append(before_render)

        # ----- Render done
        bpy.app.handlers.render_complete.clear()
        bpy.app.handlers.render_complete.append(after_render)

        bpy.app.handlers.render_cancel.clear()
        bpy.app.handlers.render_cancel.append(after_render)

        # ----- Before render image
        #bpy.app.handlers.render_post.clear()
        #bpy.app.handlers.render_post.append(before_render_image)

    else:
        # ----- Frame change
        bpy.app.handlers.frame_change_pre.clear()
        bpy.app.handlers.frame_change_pre.append(update)

        # ----- Render init
        bpy.app.handlers.render_init.clear()
        bpy.app.handlers.render_init.append(before_render)

        # ----- Render done
        bpy.app.handlers.render_complete.clear()
        bpy.app.handlers.render_complete.append(after_render)

        bpy.app.handlers.render_cancel.clear()
        bpy.app.handlers.render_cancel.append(after_render)

        # ----- Before render image
        bpy.app.handlers.render_pre.clear()
        bpy.app.handlers.render_pre.append(before_render_image)

# ====================================================================================================
# Quick launch

def go(f, setup=None, subframes=0):

    # Clear the module
    init(subframes=subframes)

    # Add the function and its setup
    add(f, setup)

    # Reset
    reset()
