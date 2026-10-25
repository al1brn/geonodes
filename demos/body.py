from geonodes import *

from geonodes.demos import common, meshutil, shaders

import bpy
import math
from math import radians

# ====================================================================================================
# Constants
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Hand constants
# ----------------------------------------------------------------------------------------------------

HAND_POSE_SIG = {
    "Thumb Lateral": Float, "Thumb Twist": Float, "Thumb": Vector,
    "Lat 1": Float, "Rot 1": Vector,
    "Lat 2": Float, "Rot 2": Vector,
    "Lat 3": Float, "Rot 3": Vector,
    "Lat 4": Float, "Rot 4": Vector,
}
HAND_POSE_FUNC = ({"Factor": Float, "Seed": Integer}, {"Hand Pose": Bundle})

HAND_POSES = {
    "Rest"      : ((0, 30, (10,)),          (0, (5, 10))),
    "None"      : ((0, 0, (0,)),            (0, (0,))),
    "Ok"        : ((0, 0, (-30, 10)),       (0, (50, 90))),
    "V"         : ((80, 10, (2, 40)),       (-15, (0,)), (15, (0,)), (0, (60, 90,))),
    "2"         : ((0, 0, (0, )),           (0, (0,)), (0, (60, 90,))),
    "3"         : ((80, 10, (2, 40)),       (-10, (0,)), (0, (0,)), (10, (0, )), (0, (60, 90,))),
    "4"         : ((80, 10, (2, 40)),       (-10, (0,)), (0, (0,)), (5, (0, )), (10, (0, ))),
    "5"         : ((0, 0, (10, 0)),         (-10, (0,)), (0, (0,)), (5, (0, )), (10, (0, ))),
    "Fist"      : ((25, 30, (-30, 60, 45)), (0, (30, 90))),
    "Handle"    : ((25, 30, (-30, 50, 40)), (0, (20, 80))),
    "Nickel"    : ((45, 80, (-25, -7, 50)), (0, (15, 55)), (0, (10, 20)), (0, (7, 25)), (0, (10, 30,))),
    "3 Thumb"   : ((0, 0, (0,)),            (-15, (0,)), (15, (15,)), (0, (60, 90,)), ),
    "4 Thumb"   : ((0, 0, (0,)),            (-15, (0,)), (0, (7,)), (15, (15,)), (0, (60, 90,))),
    "Show"      : ((80, 10, (2, 40)),       (0, (0,)), (0, (60, 90,)), ),
    "Rock"      : ((0, 0, (10, 0)),         (-10, (0,)), (0, (60, 90)), (0, (60, 90)), (10, (0, ))),
    "Cup"       : ((30, 30, (20, 20, 20)),  (0, (10, 30)),),
    "Hook"      : ((0, 0, (10, 10, 10)),    (0, (0, 90, 90)),),
    "Mouse Up"  : ((30, 30, (20, 15)),      (0, (5,)), (0, (10, 20, 30)), (0, (10, 30)), (0, (40, 20, 10))),
    "Mouse Down": ((30, 30, (20, 15)),      (0, (7, 15, 20)), (0, (10, 20, 30)), (0, (10, 30)), (0, (40, 20, 10))),
    "Keyboard"  : ((30, 30, (20, 15)),      (-7, (10,)), (-3, (10, )), (3, (10, )), (7, (10,))),
    #"Keyboard 1": ((30, 30, (20, 15)),      (-7, (30, 10, 20)), (-3, (10, )), (3, (10, )), (7, (10,))),
    #"Keyboard 2": ((30, 30, (20, 15)),      (-7, (10, )), (-3, (30, 10, 20)), (3, (10, )), (7, (10,))),
    #"Keyboard 3": ((30, 30, (20, 15)),      (-7, (10, )), (-3, (10, )), (3, (30, 10, 20)), (7, (10,))),
    #"Keyboard 4": ((30, 30, (20, 15)),      (-7, (10, )), (-3, (10, )), (3, (10, )), (7, (30, 10, 20))),
}

# ----------------------------------------------------------------------------------------------------
# Hand constants
# ----------------------------------------------------------------------------------------------------

HEAD_POSE_SIG = {
    "Head"     : Vector,
    "Left Eye" : Vector,
    "Right Eye": Vector,
    "Left Lid" : Vector,
    "Right Lid": Vector,
    "Mouth"    : Vector,
}

# ====================================================================================================
# ====================================================================================================
# Create Hair curves
# ====================================================================================================
# ====================================================================================================

def create_hair_curves(object_name, hair_name="Hair", scalp_name="Scalp"):
    """Create the Hair object and return the hair generation node.

    The object starts empty; the node belongs to the current Geometry Nodes tree.
    Reuse an existing CURVES object with the requested name.
    """

    CAPTURE_NAME = "Capture Scalp"

    capture_scalp_group = bpy.data.node_groups.get(CAPTURE_NAME)
    if capture_scalp_group is None:
        demo_hair()
        capture_scalp_group = bpy.data.node_groups[CAPTURE_NAME]
    
    obj = bpy.data.objects.get(object_name)
    if obj is None:
        raise AttributeError(f"Object {object_name!r} not found")
        
    hair_obj_name = f"{object_name} {hair_name}"

    hair = bpy.data.objects.get(hair_obj_name)
    if hair is not None and hair.type != 'CURVES':
        raise ValueError(f"Object {hair_obj_name!r} already exists and is not a CURVES object")
        
    if hair is None:
        curves = bpy.data.hair_curves.new(hair_obj_name)
        hair = bpy.data.objects.new(hair_obj_name, curves)
        obj.users_collection[0].objects.link(hair)
        hair.parent = obj
        
    modifier = None
    for mod in hair.modifiers:
        if mod.type == 'NODES' and getattr(mod.node_group, "name", None) == CAPTURE_NAME:
            modifier = mod
            break
        
    if modifier is None:
        modifier = hair.modifiers.new(name=CAPTURE_NAME, type='NODES')
        modifier.node_group = capture_scalp_group

    modifier.properties.inputs.Socket_1.value = obj
    modifier.properties.inputs.Socket_2.value = scalp_name
    



# ====================================================================================================
# ====================================================================================================
# Hand builders
# ====================================================================================================
# ====================================================================================================

def demo_hand(rebuild=False):

    # ----------------------------------------------------------------------------------------------------
    # Required groups
    # ----------------------------------------------------------------------------------------------------

    from geonodes.demos import meshutil
    meshutil.demo()

    # ----------------------------------------------------------------------------------------------------
    # Helpers
    # ----------------------------------------------------------------------------------------------------
    
    OSel = G("OSel")
    CBone = G("CBone")
    GBody = G("Body")
    
    # ====================================================================================================
    # Hand Animation
    # ====================================================================================================
    
    # ----------------------------------------------------------------------------------------------------
    # Preset Hand Poses
    # Return a "Hand Pose" Bundle
    # ----------------------------------------------------------------------------------------------------
    
    # CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD 
    # CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD 
    # CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD 
    # CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD 
    # CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD 
    # CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD 
    # CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD CAUTION REBUILD 

    with GeoNodes("Body Hand Pose Preset", is_group=True, rebuild=False):
        
        # ----------------------------------------------------------------------------------------------------
        # Expand HAND POSES
        # ----------------------------------------------------------------------------------------------------
        
        def get_values(angles, i):
            if i == 0:
                a, b = radians(angles[0][0]), radians(angles[0][1])
                v = angles[0][2]
            else:
                if len(angles) < i+1:
                    a = radians(angles[-1][0])
                    v = angles[-1][1]
                else:
                    a = radians(angles[i][0])
                    v = angles[i][1]
                    
            if len(v) == 0:
                v = (0, 0, 0)
            elif len(v) == 1:
                v = (radians(v[0]), radians(v[0]), radians(v[0]))
            elif len(v) == 2:
                v = (radians(v[0]), radians(v[1]), radians(v[1]))
            else:
                v = (radians(v[0]), radians(v[1]), radians(v[2])) 
                
            if i == 0:
                return a, b, v
            else:
                return a, v

        # ----------------------------------------------------------------------------------------------------
        # Hand pose dict
        # ----------------------------------------------------------------------------------------------------

        def get_hand_pose(name):
            
            angles = HAND_POSES[name]
            
            hand_pose = {}
            hand_pose["Thumb Lateral"], hand_pose["Thumb Twist"], hand_pose["Thumb"] = get_values(angles, 0)
            
            for i in range(1, 5):
                hand_pose[f"Lat {i}"], hand_pose[f"Rot {i}"] = get_values(angles, i)
                
            return hand_pose

        # ----------------------------------------------------------------------------------------------------
        # Interpolation curve between several poses
        # ----------------------------------------------------------------------------------------------------
        
        def get_interpolation_curve(poses):
            
            line = Curve.Line().resample(count=len(poses))
            for name, vtype in HAND_POSE_SIG.items():
                
                with Layout(f"Curve {name}"): 
                    for i in range(len(poses)):
                        line.points[nd.index == i].set(name, poses[i][name])
                            
            return line

        # ----------------------------------------------------------------------------------------------------
        # Interpolation closure between a liste of poses
        # ----------------------------------------------------------------------------------------------------
        
        def get_interpolation_closure(curve):
            with Closure() as closure:
                factor = Float(1.0, "Factor")
                seed = Integer(0, "Seed")
                
                #curve = get_interpolation_curve(pose_names)
                with Bundle() as bundle: 
                    for name, vtype in HAND_POSE_SIG.items():
                        value = curve.sample_factor(vtype(name), factor=factor)
                        value.out(name)
                                
                bundle.out("Hand Pose")
                factor.out("Factor")
                seed.out("Seed")
                
            return closure
            
        # ----------------------------------------------------------------------------------------------------
        # "Static" functions
        # ----------------------------------------------------------------------------------------------------
            
        closures = {}
        for pose_name in HAND_POSES.keys():
            
            with Closure() as closure:
                factor = Float(1.0, "Factor")
                seed = Integer(0, "Seed")
                
                hand_pose = get_hand_pose(pose_name)
                
                with Bundle() as bundle:
                    for name, value in hand_pose.items():
                        vtype = HAND_POSE_SIG[name]
                        vtype.Out(value, name)
                                
                bundle.out("Hand Pose")
                factor.out("Factor")
                seed.out("Seed")
                            
            closures[pose_name] = closure

        # ----------------------------------------------------------------------------------------------------
        # Count
        # ----------------------------------------------------------------------------------------------------
            
        poses = [get_hand_pose(pose_name) for pose_name in ("Ok", "2", "3 Thumb", "4 Thumb", "5")]
        curve = get_interpolation_curve(poses)
        closures["Count Thumb"] = get_interpolation_closure(curve)

        poses = [get_hand_pose(pose_name) for pose_name in ("Ok", "2", "3", "4", "5")]
        curve = get_interpolation_curve(poses)
        closures["Count"] = get_interpolation_closure(curve)
            
        # ----------------------------------------------------------------------------------------------------
        # Keyboard
        # ----------------------------------------------------------------------------------------------------

        with Layout("Typing"):
        
            n = 15
            poses = [get_hand_pose("Keyboard") for i in range(15)]
            curve = get_interpolation_curve(poses)

            vdown = (radians(30), radians(10), radians(20))

            curve.points[nd.index ==  1].set("Rot 1", vdown)
            curve.points[nd.index ==  2].set("Rot 3", vdown)
            curve.points[nd.index ==  3].set("Rot 2", vdown)
            curve.points[nd.index ==  4].set("Rot 1", vdown)
            curve.points[nd.index ==  5].set("Rot 4", vdown)
            curve.points[nd.index ==  6].set("Rot 3", vdown)
            curve.points[nd.index ==  7].set("Rot 2", vdown)
            curve.points[nd.index ==  8].set("Rot 4", vdown)
            curve.points[nd.index ==  9].set("Rot 2", vdown)
            curve.points[nd.index == 10].set("Rot 1", vdown)
            curve.points[nd.index == 11].set("Rot 3", vdown)
            curve.points[nd.index == 12].set("Rot 1", vdown)
            curve.points[nd.index == 13].set("Rot 2", vdown)

            closures["Typing"] = get_interpolation_closure(curve)


        # ----------------------------------------------------------------------------------------------------
        # Menu Selection
        # ----------------------------------------------------------------------------------------------------
                    
        closure = Closure.MenuSwitch(closures, menu=Input("Pose"))
        closure.out("Hand Pose Func")          
    
    # ----------------------------------------------------------------------------------------------------
    # Hand Pose UI Definition
    # ----------------------------------------------------------------------------------------------------
    
    with GeoNodes("Body Hand Anim", is_group=False, rebuild=rebuild):
        
        mesh = Mesh()
        is_right = Boolean(False, "Right")

        factor = Float.Factor(1, "Factor", 0, 1)
        
        with Panel("Base"):
            base_pose_func = GBody.hand_pose_preset(pose=Input("Base"))
            base_factor = Float.Factor(1.0, "Factor", 0, 1)
            
        with Panel("Offset"):
            inputs = {}
            
            inputs["Thumb Lateral"] = Float.Angle(0, "Thumb Lateral")
            inputs["Thumb Twist"] = Float.Angle(0, "Thumb Twist")
            inputs["Thumb"] = Vector.Euler(None, "Thumb")

            for i in range(1, 5):
                name = f"Lat {i}"
                inputs[name] = Float.Angle(0, name)
                name = f"Rot {i}"
                inputs[name] = Vector.Euler(None, name)
                
        # ----------------------------------------------------------------------------------------------------
        # Get The Curreent Hand Pose
        # ----------------------------------------------------------------------------------------------------
                
        with Layout("Get Current Hand Pose"):
            
            mesh_bundle = mesh.get_bundle()
            
            left_pose = mesh_bundle.get_item("Left Hand", socket_type='BUNDLE')
            left_exists = left_pose.exists
            right_pose = mesh_bundle.get_item("Right Hand", socket_type='BUNDLE')
            right_exists = right_pose.exists
            
            cur_pose = Bundle.Switch(is_right, left_pose, right_pose)
            exists = Boolean.Switch(is_right, left_exists, right_exists)
            
            def_pose = GBody.hand_pose_preset(pose="Rest").evaluate(factor=1.0, signature=HAND_POSE_FUNC)
            
            cur_pose.switch_false(exists, def_pose)
            
            cur = cur_pose.separate(signature=HAND_POSE_SIG)
            
        # ----------------------------------------------------------------------------------------------------
        # Target Base
        # ----------------------------------------------------------------------------------------------------
            
        with Layout("Base for Target"):
            base_pos = base_pose_func.evaluate(factor=base_factor, seed=0, signature=HAND_POSE_FUNC)
            base = base_pos.separate(signature=HAND_POSE_SIG)
            
        with Bundle() as bundle:
            for name, val_type in HAND_POSE_SIG.items():
                a = cur[name]
                b = base[name]
                val_type(factor).map_range(to_min=cur[name], to_max=base[name] + inputs[name]).out(name)
                
        left_mesh_bundle = Bundle(mesh_bundle)
        left_mesh_bundle.set_item("Left Hand", bundle)
        
        right_mesh_bundle = Bundle(mesh_bundle)
        right_mesh_bundle.set_item("Right Hand", bundle)
        
        mesh.set_bundle(Bundle.Switch(is_right, left_mesh_bundle, right_mesh_bundle))
        
        mesh.out()
        bundle.out("Hand Pose")
    
    
    # ====================================================================================================
    # Hand
    # ====================================================================================================
    
    with GeoNodes("Body Hand", is_group=False, rebuild=rebuild):
        
        # ----------------------------------------------------------------------------------------------------
        # Input
        # ----------------------------------------------------------------------------------------------------
        
        mesh = Mesh()
        
        is_right = Boolean(False, "Right")
        size = Float(1.0, "Size")
        mat = Material(None, "Material")
        
        mesh = GBody.hand_anim(mesh, right=is_right).link_inputs(from_panel="Pose")
        hand_pose = mesh.hand_pose
        
        # ----------------------------------------------------------------------------------------------------
        # Constants
        # ----------------------------------------------------------------------------------------------------
        
        N_PROF = 44 - 9 + 1
        N_RINGS = 10
        
        RESOL = 3
        N_POINTS = 4*(RESOL-1) + 7*4
        N4 = N_POINTS // 4
        N2 = N_POINTS // 2
        
        N_PROF = N_POINTS
        
        H_FINGER = 1.0

        finger_radius=0.16
        
        
        # ----------------------------------------------------------------------------------------------------
        # Palm Profile
        # ----------------------------------------------------------------------------------------------------
        
        with Layout("Palm Profile"):
            
            profile = Curve.Circle().resample(count=N_POINTS)
            ag=nd.index*(pi/2/RESOL)
            
            l = 0.45
            
            profile[nd.index < RESOL].position = (l + finger_radius*ag.cos(), finger_radius*ag.sin(), 0)
            profile[nd.index >= RESOL].position = ((N4 - nd.index)/(N4 - RESOL)*l, finger_radius, 0)
            
            with Layout("Symmetry"):
                x, y, _ = profile.points.sample_index(nd.position, index=N2 - nd.index).xyz
                profile[nd.index >= N4].position = (-x, y, 0)
                
                x, y, _ = profile.points.sample_index(nd.position, index=N_POINTS - nd.index).xyz
                profile[nd.index >= N2].position = (x, -y, 0)
                
        # ----------------------------------------------------------------------------------------------------
        # Extrude Profile
        # ----------------------------------------------------------------------------------------------------
                
        with Layout("Base Palm"):
        
            bb = Curve.Line().resample(count=10)
            bb.points.radius=1.0
            
            with Layout("Close Bottom"):
                d = finger_radius
                
                for i in range(4):
                    f = nd.index/4
                    f = f**2
                    sel = nd.index == i
                    z = (f-1)*d
                    bb.points[sel].radius = math.sqrt(i/4) #1.0 - Float((1 - (i/4))**2).sqrt()
                    bb.points[sel].position = (0, 0, z)
                    
                    
            with Layout("Palm Height"):
                sel = nd.index >= 4
                bb.points[sel].position = (0, 0, (nd.index - 4)*(1/6))
                bb.points[sel].radius = 0.9 + ((nd.index - 4)/6).sqrt()*0.2
                
                palm = bb.to_mesh(profile_curve = profile, scale=nd.radius)
                palm.points.set("Bone", -1)
                    
                palm = OSel.add_selection(palm, (nd.index // N_PROF) == N_RINGS-1, name="Loop")
                
        # ----------------------------------------------------------------------------------------------------
        # Create the hole for the Thumb
        # ----------------------------------------------------------------------------------------------------
                
        with Layout("Thumb Selections (Delete and Loop)"):
            sels = [None]*8
            for i in range(5):
                idx0 = (N2-1, N2-2, N2-2, N2-2, N2-1)[i]
                nidx = (3, 5, 5, 5, 3)[i]

                sel = (nd.index // N_POINTS) == 3 + i
                
                if i > 0 and i < 4:
                    
                    # ----- Deletion
                    
                    del_sel = sel
                    del_sel &= (nd.index % N_POINTS) > idx0
                    del_sel &= (nd.index % N_POINTS) < idx0 + nidx - 1
                    
                    palm = OSel.add_selection(palm, del_sel, invert=i==4, name="tmp Delete")
                    
                    # ----- Selection
                    
                    sels[i]     = sel & ((nd.index % N_POINTS) == idx0)
                    sels[8 - i] = sel & ((nd.index % N_POINTS) == idx0 + nidx - 1)
                    
                elif i in [0, 4]:
                    
                    sel &= (nd.index % N_POINTS) >= idx0-1
                    sel &= (nd.index % N_POINTS) <= idx0 + nidx
                    
                    if i == 0:
                        sels[0] = sel
                    else:
                        sels[4] = sel
                        
            for i, sel in enumerate(sels):
                palm = OSel.add_selection(palm, sel, invert=i==0, name="Thumb")
                
        # ----------------------------------------------------------------------------------------------------
        # Finger Holes
        # ----------------------------------------------------------------------------------------------------
                
        with Layout("Finger Holes"):
            
            palm = OSel.split_hole(palm, "Loop",     count=3, index_0 = RESOL+2, index_1=N_POINTS - 1*(RESOL+1) - 1, resolution=RESOL)
            palm = OSel.split_hole(palm, "Loop B",   count=3, index_0 = 7,       index_1=N_POINTS - 2*(RESOL+2) - 1, resolution=RESOL)
            palm = OSel.split_hole(palm, "Loop B B", count=3, index_0 = 7,       index_1=N_POINTS - 3*(RESOL+3) - 1, resolution=RESOL)

            palm = OSel.rename(palm, "Loop A",      "Finger 4")
            palm = OSel.rename(palm, "Loop B A",    "Finger 3")
            palm = OSel.rename(palm, "Loop B B A",  "Finger 2")
            palm = OSel.rename(palm, "Loop B B B",  "Finger 1")
            
            palm = OSel.to_circle(palm, "Finger 1", radius=finger_radius, default_center=True)
            palm = OSel.to_circle(palm, "Finger 2", radius=finger_radius, default_center=True)
            palm = OSel.to_circle(palm, "Finger 3", radius=finger_radius, default_center=True)
            palm = OSel.to_circle(palm, "Finger 4", radius=finger_radius, default_center=True)
            
            for i in range(4):
                palm.points[Integer(f"Finger {i+1}") > 0].set("Bone", i)
                
        # ----------------------------------------------------------------------------------------------------
        # Weld the four fingers
        # ----------------------------------------------------------------------------------------------------
            
        with Layout("Base Finger"):
            cyl = G().new_cylinder(rings=12, segments=12, caps=False, radius=finger_radius, depth=H_FINGER)
            cyl = G().close_cylinder(cyl, height=finger_radius, bottom=False, top=True)
            
        for i_finger in range(4):

            # ----------------------------------------------------------------------------------------------------
            # Weld the finger
            # ----------------------------------------------------------------------------------------------------
            
            with Layout(f"Finger {i_finger + 1}"):
            
                sel_name = f"Finger {i_finger + 1}"
                
                scale = (1.0, 1.1, 1.0, 0.90)[i_finger]
                offset = (1.5, 2.5, 1.5, 1.0)[i_finger]
                
                finger = Mesh(cyl)
                finger.points.set("Bone", i_finger)
                
                finger.transform(scale=(1.0, 1.0, scale))
                center = OSel.get_disk(palm, sel_name).center
                finger.offset = center + (0, 0, finger_radius*offset/3)

                finger = OSel.add_selection(finger, G().cylinder_selection(cyl, ring_index=0), invert=True, name="tmp Base")
                finger = OSel.shift(finger, "tmp Base", 9 if i_finger == 0 else 3)

                palm += finger
                palm = OSel.merge(palm, sel_name, "tmp Base")
                
            # ----------------------------------------------------------------------------------------------------
            # Finger Bone
            # ----------------------------------------------------------------------------------------------------
                
            with Layout(f"Bone {i_finger + 1}"):
                bone = Curve.Line().resample(count=5)

                base_finger = (0.9, 0.98, 0.9, 0.88)[i_finger]
                h_finger    = (0.92, 0.98, 0.92, 0.82)[i_finger]
                
                x = Float(i_finger).map_range(0, 3, -finger_radius*2.5, finger_radius*2.5)
                bone.offset = (x, 0, finger_radius*(-1.1))
                
                x = Float(i_finger).map_range(0, 3, -finger_radius*3.2, finger_radius*3.2)
                
                bone[nd.index == 1].position = (x, 0, 0.7*base_finger)
                
                bone[nd.index == 2].position = (x, 0, base_finger)
                bone[nd.index == 3].position = (x, 0, base_finger + h_finger/2)
                bone[nd.index == 4].position = (x, 0, base_finger + h_finger)
                
                if i_finger == 0:
                    bones = bone
                else:
                    bones += bone
                    
        # ----------------------------------------------------------------------------------------------------
        # Thumb and Thumb Bone
        # ----------------------------------------------------------------------------------------------------
                
        with Layout("Thumb"):
            
            with Layout("Delete Inside Loop"):
                palm.points[Integer("tmp Delete")>0].delete()
                palm.remove_named_attribute(name="tmp Delete")
                
            with Layout("Thumb Mesh"):
                thumb = G().new_cylinder(rings=12, segments=16, caps=False, radius=finger_radius*1.1, depth=H_FINGER*0.9)
                thumb = G().close_cylinder(thumb, height=finger_radius, bottom=False, top=True)
                thumb.transform(rotation=(0, -pi/3, 0), translation=(-0.75, 0, 0.3))
                thumb.points.set("Bone", 4)
                
            with Layout("Weld Thumb"):
                
                sel = nd.index < 16
                thumb = OSel.add_selection(thumb, sel, name="Base")
                
                palm = OSel.shift(palm, name="Thumb", shift=-2)
                palm += thumb
                
                palm = OSel.bridge(palm, name="Thumb", closed=True, to_name="Base", resolution=5, bridge_name="Thumb Bridge")
                palm.points[Integer("Thumb Bridge") > 0].set("Bone", 4)
                
            with Layout("Thumb Bone"):
                tbone = Curve.Line(end=(0, 0, 1.3)).resample(count=4)
                tbone[nd.index == 2].offset = 0, 0, -0.2
                tbone[nd.index == 1].offset = 0, 0, -0.1
                tbone.transform(translation=(-0.4, 0, 0.1), rotation=(0, -pi/3, 0))
                bones += tbone
                
        # ----------------------------------------------------------------------------------------------------
        # Link Bones
        # ----------------------------------------------------------------------------------------------------
                
        with Layout("Link Bones"):
            bones = CBone.new(bones)
            # Make sure perpendicular along X for fingers 0 to 3 (overrides default)
            bones.points[nd.index < 20].set("Perp", (1, 0, 0))
            
            # Link to Mesh
            #palm.points[nd.position.z < 0.4].set("Bone", 4)
            palm = CBone.link(palm, curve=bones, distance=finger_radius*2, fall_off=0.5)
            
        with Layout("Adjust Thumb Bridge"):
            ib = Integer("Thumb Bridge")
            ring = (ib-1) // 16 
            fac = (ring+1)/4
            palm.points[Integer("Thumb Bridge")>0].set("Bone Weight", fac)
            palm.remove_named_attribute(name="Thumb Bridge")
            
        # ----------------------------------------------------------------------------------------------------
        # Pose
        # ----------------------------------------------------------------------------------------------------
        
        with Layout("Hand Pose"):
        
            node = hand_pose.separate(signature=HAND_POSE_SIG)

            with Layout("Thumb"):
                r0, r1, r2 = node.thumb.xyz
                bones = CBone.rotate(bones, 4, 0, rotation=(0, 0, node.thumb_lateral), local=False)
                bones = CBone.rotate(bones, 4, 0, rotation=(0, 0, node.thumb_twist))
                bones = CBone.rotate(bones, 4, 0, rotation=(r0, 0, 0), local=True)
                bones = CBone.rotate(bones, 4, 1, rotation=(0, -r1, 0))
                bones = CBone.rotate(bones, 4, 2, rotation=(0, -r2, 0))
                
            for i in range(1, 5):
                with Layout(f"Finger {i}"):
                    lat = node[f"Lat {i}"]
                    r0, r1, r2 = node[f"Rot {i}"].xyz
                    bones = CBone.rotate(bones, i-1, 1, rotation=(0, lat, 0))
                    bones = CBone.rotate(bones, i-1, 1, rotation=(r0, 0, 0))
                    bones = CBone.rotate(bones, i-1, 2, rotation=(r1, 0, 0))
                    bones = CBone.rotate(bones, i-1, 3, rotation=(r2, 0, 0))
            
            palm = CBone.deform(palm, bones)      
            
        # ----------------------------------------------------------------------------------------------------
        #  Finalize
        # ----------------------------------------------------------------------------------------------------
        
        with Layout("Finalize"):
            palm.position = nd.position.scale(size)

            right_hand = Mesh(palm)
            right_hand.position = nd.position*(1, -1, 1)
            right_hand.flip_faces()
            palm.switch(is_right, right_hand)

            palm.transform(rotation=(0, 0, pi/2))
            
            palm.faces.shade_smooth=True
            palm.faces.material = mat
            palm.out()

# ====================================================================================================
# ====================================================================================================
# Hair
# ====================================================================================================
# ====================================================================================================

def demo_hair(rebuild=False):

    shaders.transparent_shader()

    # ====================================================================================================
    # Capure Scalp from a Mesh
    # ====================================================================================================

    with GeoNodes("Capture Scalp", rebuild=rebuild):
        
        object = Object(name="Object")
        name = String("Scalp", "Scalp Name")
        
        mesh = Mesh(object.info().geometry)
        bundle = mesh.get_bundle()
        pear_shape = bundle.get_item("Pear Shape", socket_type="CLOSURE")
        
        scalp = Mesh(mesh.faces[Boolean(name)].separate())

        scalp = G().capture_rest_geometry(scalp)
        scalp.set_bundle(
            scalp.get_bundle() + Bundle.Combine({"Pear Shape": pear_shape})
        )
        
        scalp.out()

    # ====================================================================================================
    # Depracated
    # ====================================================================================================

    if False:
        with GeoNodes("Body Hair To Mesh"):
            
            curves = Curve(name="Curves")
            lod_factor = Float(1.0, "LoD", 0, 1)
            
            with Panel("Profile", create_layout=True):
                resol = Integer(12, "Resolution", 3)
                radius = Float(0.01, "Radius", 0)
                radius = lod_factor.interpolate(radius*5, radius)
                curves = G().set_hair_curve_profile(curves, replace_radius=True, radius=radius).link_inputs()
                curves = Curve(curves)

            with Panel("Color", create_layout=True):
                col0 = Color(None, "Start Color")
                col1 = Color(None, "End Color")
                cfac0 = Float(0, "Start Factor", 0, 1)
                cfac1 = Float(1, "End Factor", 0, 1)
                
                prm = nd.spline_parameter().factor
                curves.points.set("Color", col0.mix(col1, factor=prm.map_range(cfac0, cfac1)))
                
            with Layout("To Mesh"):
                resol = gnmath.max(3, (resol*lod_factor).to_integer())
                mesh = curves.to_mesh(profile_curve=Curve.Circle(), scale=nd.radius, fill_caps=True)
                
                mesh.faces.shade_smooth=True
                
            mesh.out()

    with GeoNodes("Body Hair", rebuild=rebuild):

        HAIR_DEBUG = False

        # ----------------------------------------------------------------------------------------------------
        # Parameters
        # ----------------------------------------------------------------------------------------------------

        # Global parameters

        scalp = Mesh()
        pear_shape = scalp.get_bundle().get_item("Pear Shape", socket_type="CLOSURE")
        hair_resol = Integer(12, "Hair Resolution", 3)
        lod_factor = Float(1.0, "LoD", 0, 1)
        hair_length = Float(1.0, "Length", 0)
        seed = Integer(0, "Seed")

        hair_resol = gnmath.max(3, hair_resol*lod_factor).to_integer()._lc("Hair Resol")

        if HAIR_DEBUG:
            with Panel("DEBUG", create_layout=True):
                single_hair = Boolean(False, "Single", shape="Single")
                to_mesh = Boolean(False, "To Mesh")

                theta = Float.Angle(pi/2, "Theta")
                phi = Float.Angle(0, "Phi")
                pos = G().combine_spherical(theta=theta, phi=phi, r=1.0)
                single_pt = Cloud.Points(position=pos)

                line = Curve.Line().resample(count=hair_resol)
                single_curve = Curve(single_pt.instance_on_points(instance=line).realize())

        with Panel("Baldness", create_layout=True):
            bald_angle = Float.Factor(0.5, "Position", 0, 1).interpolate(pi/4, -pi/4)
            bald_aspect = Float.Factor(0.5, "Aspect", 0, 1)
            bald_size = Float.Factor(0, "Size", 0, 1).interpolate(0, pi/2)
            bald_falloff = Float.Factor(0.5, "Falloff", 0, 1)

        with Layout("Baldness Density"):
            rpos = Rotation((0, bald_angle, 0)) @ nd.position.normalize()
            spherical = G().separate_spherical(rpos).node
            bald_max = pi/2 - bald_size
            cs = spherical.phi.cos()*(bald_aspect + 0.25).pingpong(1.0)*bald_max*2
            sn = spherical.phi.sin()*(bald_aspect + 0.75).pingpong(1.0)*bald_max*2
            boundary = gnmath.sqrt(cs**2 + sn**2)
            fade = bald_size*(1 - bald_falloff)
            # Remaining density: 0 in the bald area, 1 outside it.
            bald_density = spherical.theta.map_range(
                boundary - fade.max(0.000001), boundary, 1.0, 0.0)
            bald_density.switch(bald_falloff >= 1.0, Float(spherical.theta < boundary))

        # Scalp to put hair onto

        with Panel("Scalp", create_layout=True):

            curves = G().generate_hair_curves(
                hair_surface=scalp,
                surface_source='Input',
                resting_surface=True,
                attach_to_surface=True,
                density_mask=bald_density,
                hair_length=hair_length,
                control_points=hair_resol,
                seed=seed.hash_value(72998588),
                ).link_inputs(exclude=["Surface", "Surface UV Map", "Mask Texture", "Hair Material"]).curves

            if HAIR_DEBUG:
                curves.switch(single_hair, single_curve)

            blur_size = Float.Factor(0, "Blur", 0, 1).interpolate(0, 0.1)

            point_index  = (nd.index % hair_resol)._lc("Point Index")
            spline_index  = (nd.index // hair_resol)._lc("Spline Index")

            spline_root_position = curves.points.sample_index(nd.position, index=nd.index*hair_resol)

        with Panel("Hair properties", create_layout=True):
            stiffness = Float.Factor(0.5, "Stiffness", 0, 1)
            flatness = Float.Factor(0.5, "Flatness", 0, 1)
            
        with Panel("Fringe", create_layout=True):
            x, y, z = spline_root_position.xyz
            fringe_min = curves.splines[(x > 0) & (y.abs() <= 0.1)].attribute_statistic(z).min_
            theta_max = gnmath.asin(fringe_min)
            fringe_theta = Float(0.5, "Fringe", 0, 1).interpolate(pi/2, theta_max)
            fringe_width = Float(1.0, "Fringe Width", 0, 1).interpolate(0, pi/2)

        with Panel("Comb", create_layout=True):
            comb_factor = Float.Factor(0, "Factor", 0, 1)
            comb_direction = Float.Factor(0, "Direction", 0, 1)

            use_node = Boolean(False, "Node")
            node_theta = Float.Factor(0.5, "Position", 0, 1).interpolate(pi/2, -0.4*pi)
            node_phi = Float.Factor(0, "Lateral", 0, 1).interpolate(0, pi/2)
            node_dist = Float.Factor(0.5, "Distance", 0, 1).interpolate(1.05, 1.5)
            
        with Panel("Hair Cut"):
            use_hair_cut = Boolean(True, "Hair Cut")
            fringe_z = Float(0.5, "Fringe Cut", 0, 1).interpolate(fringe_min - 0.01, 0)
            fringe_cut_width = Float.Factor(0.5, "Fringe Width", 0, 1).interpolate(0, pi*0.49)
            back_z = Float(-1, "Back Cut", -10, 1)
            back_width = Float.Factor(0.5, "Back Width", 0, 1).interpolate(0, pi*0.49)
        
        with Layout("Generate Curves"):
            pos0 = curves.splines.sample_index(spline_root_position, index=nd.index // hair_resol)
            
            node = G().separate_spherical(pos0).node
            phi0,  theta0, r0 = node.phi, node.theta, node.r
            
            tan0 = G().combine_spherical(phi=phi0, theta=theta0 - pi/2, r=r0)._lc("Tangent 0")
            
            with Layout("Blur Direction & Boundaries"):
                # One rotation per hair, shared by its direction and zone
                # tests. The actual root and surface attachment stay fixed.
                blur_angles = Vector.Random(-blur_size, blur_size, id=spline_index,
                                            seed=seed.hash_value(927220))
                blur_rotation = Rotation(blur_angles)
                zone_position = blur_rotation @ pos0
                zone = G().separate_spherical(zone_position).node
                is_fringe = ((zone_position.x > 0) & (zone.theta < fringe_theta)
                             & (zone.phi.abs() < fringe_width))

            hair_dist = Float.Random(1.0, flatness.interpolate(1.05, 1.0), id=spline_index, seed=seed.hash_value(86927856))
        
        with Layout("Hair Curves"):
            
            zdot = pos0.z
            hrz_dir = (pos0 - Vector((0, 0, zdot))).normalize()
            
            direction = Vector(flatness).map_range(to_min=pos0, to_max=tan0)
            direction = blur_rotation @ direction

            with Layout("Comb Direction & Intensity"):
                comb_phi = G().separate_spherical(direction).phi
                side = Float.Switch(comb_phi < 0, 1.0, -1.0)
                target_phi = side * comb_direction.interpolate(pi/2, pi)
                # Intensity depends on the root's front/back position,
                # independently of the selected comb direction.
                front_weight = phi0.cos().map_range(-1.0, 1.0, 0.0, 1.0)
                influence = comb_factor * front_weight
                influence = Float.Switch(is_fringe, influence, 0.0)
                angle = (target_phi - comb_phi) * influence
                direction = Rotation((0, 0, angle)) @ direction

            with Layout("Hair Node Target"):
                node_active = use_node & ~is_fringe
                root_side = Float.Switch(zone_position.y < 0, 1.0, -1.0)
                node_r = Float.Switch(node_theta < 0, node_dist,
                                      node_dist / node_theta.cos().max(0.000001))
                node_target = Vector(G().combine_spherical(
                    phi=root_side * (pi - node_phi), theta=node_theta, r=node_r))
                node_start_distance = (node_target - pos0).length()
                node_radius = hair_dist.min(node_r)

            with Layout("Hair Node Route"):
                root_normal = pos0.normalize()
                route_axis = root_normal.cross(node_target)
                # Opposite roots have no unique great circle. Choose an
                # upward route, slightly toward the root's own side.
                preferred = Vector((0, root_side * 0.25, 1))
                preferred -= root_normal.scale(preferred.dot(root_normal))
                preferred.switch(preferred.length() < 0.000001, Vector((0, root_side, 0)))
                route_axis.switch(route_axis.length() < 0.000001,
                                  root_normal.cross(preferred))
                route_axis = route_axis.normalize()
                initial_tangent = route_axis.cross(root_normal)
                # Reverse only a route that descends farther in front of
                # the face. A downward route toward a lateral node is valid.
                crosses_face = ((pos0.x > 0) & (initial_tangent.z < 0)
                                & (initial_tangent.x > 0.000001))
                route_axis = Vector.Switch(crosses_face, route_axis, -route_axis)

            with Layout("Cut z"):
                
                node = G().separate_spherical(direction).node
                dir_phi,  dir_theta = node.phi, node.theta
                
                cut_z = dir_phi.abs().map_range(fringe_cut_width, pi-back_width, fringe_z, back_z)
            
            dl_fac = 1.0 + 1/(hair_resol-1)
            dl_sum = (1 - dl_fac**hair_resol)/(1 - dl_fac)
            dl = hair_length/dl_sum
            
            for rep in repeat(hair_resol-1, curves=curves, pos=pos0, direction=direction,
                              dl=dl, is_cut=False, node_reached=False):

                with Layout("Guide Hair To Node"):
                    to_node = node_target - rep.pos
                    node_distance = to_node.length()
                    direct = to_node.normalize()
                    normal = rep.pos.normalize()

                    # Test the whole segment to the target, not only its ends.
                    closest_factor = (-rep.pos.dot(to_node)
                                      / to_node.dot(to_node).max(0.000001)).clamp(0, 1)
                    closest = rep.pos + to_node.scale(closest_factor)
                    direct_clear = closest.length() >= node_radius - 0.000001

                    # The plane and traversal sense are fixed at the root.
                    tangent = route_axis.cross(normal).normalize()
                    guide = direct

                    # Slack peaks between root and target and vanishes at
                    # both ends. Close to the target, guidance takes over.
                    remaining = (node_distance / node_start_distance.max(0.000001)).clamp(0, 1)
                    sag = (1 - stiffness) * 2 * remaining * (1 - remaining)
                    guide += Vector((0, 0, -sag))
                    # While the skull hides the target, stay on the chosen
                    # route. Gravity can bend the free span after departure.
                    guide.switch(~direct_clear, tangent)
                    guide = guide.normalize()
                    step_direction = Vector.Switch(node_active, rep.direction, guide)
                    reached_now = node_active & direct_clear & (node_distance <= rep.dl)
                
                delta = step_direction.scale(rep.dl)
                new_pos = rep.pos + delta
                
                d = new_pos.length()
                new_pos.switch(d < hair_dist, new_pos.normalize().scale(hair_dist))
                new_pos.switch(reached_now, node_target)
                new_pos.switch(rep.node_reached, rep.pos)
                
                z = new_pos.z
                prev_z = rep.pos.z
                to_cut = use_hair_cut & ~node_active & (z < cut_z) & (cut_z <= prev_z)
                
                diff = z - prev_z
                ratio = Float.Switch(diff > -0.0001, (cut_z - prev_z)/diff, 0.0)
                
                new_pos.switch(to_cut, rep.pos + (new_pos - rep.pos).scale(ratio))
                new_pos.switch(rep.is_cut, rep.pos)
                
                rep.curves[point_index==rep.iteration+1].position = new_pos
                
                new_dir = (rep.direction + (0, 0, stiffness.interpolate(-10/(hair_resol-1), 0))).normalize()

                with Layout("Comb During Growth"):
                    current_theta = G().separate_spherical(new_pos).theta
                    comb_fade = current_theta.map_range(
                        -radians(10), radians(10), 0.0, 1.0,
                        interpolation_type='SMOOTHSTEP')

                    # Guide along the local scalp tangent, rather than adding
                    # a horizontal force at every step.
                    normal = new_pos.normalize()
                    comb_target = Vector((target_phi.cos(), target_phi.sin(), 0))
                    comb_target = comb_target - normal.scale(comb_target.dot(normal))
                    comb_target.switch(comb_target.length() < 0.000001, new_dir)
                    comb_target = comb_target.normalize()

                    # Scale the blend by segment length, so subdivision does
                    # not multiply the amount of combing.
                    comb_rate = influence * comb_fade * (1 - stiffness) * 4
                    comb_blend = 1 - (-comb_rate * rep.dl/hair_length.max(0.000001)).exp()
                    guided = new_dir.mix(comb_target, factor=comb_blend)
                    guided.switch(guided.length() < 0.000001, new_dir)
                    new_dir = guided.normalize()
                
                rep.pos = new_pos
                rep.direction = new_dir
                rep.dl *= dl_fac
                rep.is_cut |= to_cut
                rep.node_reached |= reached_now
                
            curves = rep.curves.resample(count=hair_resol)

            curves.position = pear_shape.evaluate(
                position=nd.position,
                signature=({"Position": Vector}, {"Position": Vector}),
            )

            if HAIR_DEBUG:
                with Layout("To Mesh"):
                    curves.points.set("Color", Color("red").mix(Color("blue"), factor=is_fringe))
                    mesh = curves.to_mesh(profile_curve=Curve.Circle(radius=0.01))
                    mesh.faces.material = "Colored Mat"
                    curves.switch(to_mesh, mesh)

        curves.out("Curves")
        scalp.out("Mesh")
          

    # ====================================================================================================
    # Body Head Scalp
    # ====================================================================================================

    with GeoNodes("Body Head Scalp", is_group = True, rebuild=rebuild):

        # Hair convention: front +X, lateral Y, up +Z.
        
        inv_normals = Boolean(False, "Invert Normals")
        resolution = Integer(32, "Resolution")
        lod_factor = Float(1.0, "LoD", 0, 1)

        resolution = gnmath.max(32, (resolution*lod_factor)).to_integer()
        with Panel("Hair Scalp"):
            z_scalp = Float.Factor(0.5, "Forehead", 0, 1, shape="Single").interpolate(0.3, 0.95)
            z_slope = Float.Factor(0.5, "Rear", 0, 1, shape="Single").interpolate(-0.9, 0)
            
        with Panel("Moustache Scalp"):
            h_moust = Float.Factor(0.5, "Moustache Height", 0, 1, shape="Single").interpolate(0, 0.2)
            z_moust = Float.Factor(0.5, "Moustache Position", 0, 1, shape="Single").interpolate(0.0, -0.4)
            w_moust = Float.Factor(0.5, "Moustache Width", 0, 1, shape="Single").interpolate(0.99, 0.93)
            
        with Layout("Hair Scalp"):

            with Layout("Base Sphere"):
                scalp = Mesh.UVSphere(segments=resolution, rings=resolution//2)
                uv = scalp.uv_map
                scalp.corners.store_uv("UV Map", uv)
                
            cube = Mesh.Cube(size=4.0)
            cube.offset = (2, 0, -2.0 + z_scalp)
            
            nx = nd.normal.x
            
            cube.faces[nx < -0.9].extrude(offset=(-2, 0, z_slope*4))
            
            scalp -= cube
            
            scalp.faces[nd.face_area > 0.1].delete(mode = "Only Edges & Faces")
            
            inverted = Mesh(scalp)
            
            inverted.set_normal_free(custom_normal=nd.normal.scale(-1), domain='POINT')
            scalp.switch(inv_normals, inverted)
            
        with Layout("Moustache Scalp"):
            
            with Layout("Base Sphere"):
                moustache = Mesh.UVSphere(segments=resolution*4, rings=resolution*2)
                uv = moustache.uv_map
                moustache.corners.store_uv("UV Map", uv)
            
            cube = Mesh.Cube(size=4)
            top = Mesh(cube)
            top.offset = 0, 0, 2 + z_moust + h_moust/2
            
            moustache -= top
            
            bot = Mesh(cube)
            bot.offset = 0, 0, -2 + z_moust - h_moust/2 
            
            moustache -= bot
            
            cube.offset = -2 + w_moust, 0, 0
            ag = gnmath.atan2(z_moust, 1)
            cube.transform(rotation=(0, -ag, 0))
            moustache -= cube
            
            nz = nd.normal.z
            moustache.faces[(nd.face_area > 0.01) | (nz.abs() > 0.8)].delete(mode = "Only Edges & Faces")

            inverted = Mesh(moustache)
            
            inverted.set_normal_free(custom_normal=nd.normal.scale(-1), domain='POINT')
            moustache.switch(inv_normals, inverted)
            
            
            moustache.switch(h_moust<=0.02)

        with Layout("Finalize"):
            scalp.faces.material = "Transparent"
            moustache.faces.material = "Transparent"
            scalp.faces.set("Scalp", True)
            moustache.faces.set("Moustache", True)
            G().capture_rest_geometry(scalp).out("Hair Scalp")
            G().capture_rest_geometry(moustache).out("Moustache Scalp")

# ====================================================================================================
# ====================================================================================================
# Head
# ====================================================================================================
# ====================================================================================================

def demo_head(rebuild=False):

    # ----------------------------------------------------------------------------------------------------
    # Helpers
    # ----------------------------------------------------------------------------------------------------
    
    OSel = G("OSel")
    #CBone = G("CBone")
    #GBody = G("Body")

    with GeoNodes(".Body Mouth"):
        
        # ----------------------------------------------------------------------------------------------------
        # Utilities
        # ----------------------------------------------------------------------------------------------------
        
        def sphere_point(theta, phi):
            
            z = phi.sin()
            r = phi.cos()
            # Front +X; keep the mouth's point and selection order.
            return r*theta.cos(), -r*theta.sin(), z
            
        def arc(count, theta_ampl, phi_corner, phi_max, rev=False):
            with Layout("Half Circle"):
                line = Mesh.Line(count=count)
                
                idx = Integer.Switch(rev, nd.index, count - 1 - nd.index)# if rev else nd.index
                fac = idx/(count-1)
                
                ta2 = theta_ampl/2
                theta = fac.interpolate(-ta2, ta2)
                phi = (fac*pi).sin().interpolate(phi_corner, phi_max)
                    
                line.position = sphere_point(theta, phi)
                return line

        # ----------------------------------------------------------------------------------------------------
        # Input
        # ----------------------------------------------------------------------------------------------------
        
        with Panel("Frame"):
            hrz_count = Integer(12, "Horizontal Count", 2)
            vrt_count = Integer(2, "Vertical Count", 0)
                    
            theta_ampl = Float.Angle(pi/3, "Horizontal Angle", 0.0, 0.9*pi)
            phi0 = Float.Angle(-pi/3, "Vertical Min", -pi/20, -pi/10)
            phi1 = Float.Angle(-pi/6, "Vertical Max", -pi/20, -pi/10).max(phi0)
            
        with Panel("Expression"):
            smile = Float.Factor(0.5, "Smile", 0, 1)
            open = Float.Factor(0.5, "Open", 0, 1)
            width_fac = Float.Factor(0.5, "Width", 0, 1)
        
        with Layout("Surrounding Rectangle"):
            
            count = 2*(hrz_count + vrt_count)
            
            phi_ampl = phi1 - phi0
            dphi = phi_ampl/(vrt_count + 1)
            
            theta1 = theta_ampl/2
            theta0 = -theta1
            dtheta = theta_ampl/(hrz_count - 1)
            
            rect = Mesh.Circle(vertices=count)
            
            # Left Side
            rect.position = sphere_point(theta0, phi0 + nd.index*dphi)
            
            # Top Side
            idx = nd.index - vrt_count - 1
            rect[nd.index >= vrt_count + 1].position = sphere_point(theta0 + idx*dtheta, phi1)
            
            # Right Side
            idx = nd.index - vrt_count - hrz_count
            rect[nd.index >= vrt_count + hrz_count + 1].position = sphere_point(theta1, phi1 - idx*dphi)
            
            # Bot Side
            idx = nd.index - 2*vrt_count - hrz_count - 1
            rect[nd.index >= 2*vrt_count + hrz_count + 1].position = sphere_point(theta1 - idx*dtheta, phi0)
            
            rect.points.set("Weld", nd.index + 1)

        with Layout("Dimensions"):
            
            # Theta Angle
            mouth_angle = width_fac*theta_ampl
            
            # Phi Angle
            phi_center = (phi0 + phi1)/2
            
            mphi_ampl2 = phi_ampl*0.45
            mphi_min = phi_center - mphi_ampl2
            mphi_max = phi_center + mphi_ampl2
            
            phi_corner = smile.interpolate(mphi_min, mphi_max)
            phi_opp = 2*phi_center - phi_corner

            # -------------------------
            # Continuous lip opening for every smile value
            # -------------------------

            mphi0 = open.interpolate(phi_opp, mphi_min)
            mphi1 = open.interpolate(phi_opp, mphi_max)
            
            # -------------------------
            # Vertices
            # -------------------------
            
            c_fac = (phi_corner - phi0)/phi_ampl
            nside = gnmath.round(c_fac*(vrt_count + 2)).to_integer().min(vrt_count+2)
            ntop = hrz_count - 2 + 2*(vrt_count + 2 - nside)
            nbot = count - ntop + 2
            
        for i_line in range(2):
            
            with Layout("Lips" if i_line == 0 else "Bevel"):
                
                if i_line == 0:
                    line0 = arc(nbot, mouth_angle, phi_corner, mphi0, True)
                    line1 = arc(ntop, mouth_angle, phi_corner, mphi1, False)
                else:
                    f = 0.995
                    dp = phi_ampl*0.01
                    line0 = arc(nbot, mouth_angle*f, phi_corner, mphi0 + dp, True)
                    line1 = arc(ntop, mouth_angle*f, phi_corner, mphi1 - dp, False)
                    
                circle = Mesh.Circle(vertices=count, fill_type="None")
                
                # Upper
                circle.position = line1.points.sample_index(nd.position, index=nd.index)
                
                # Lower
                circle[nd.index >= ntop].position = line0.points.sample_index(nd.position, index=nd.index - ntop + 1)
                
                circle.points[nd.index < ntop].set("tmp Upper", nd.index + 1)

                n_from = ntop - 1
                circle.points[nd.index >= n_from].set("tmp Lower", nd.index - n_from + 1)
                circle.points[nd.index == 0].set("tmp Lower", nbot)
                
                circle.points.set("Mouth" if i_line == 0 else "Bevel", nd.index + 1)
                if i_line == 0:
                    circle.points.set("tmp Weld" , nd.index + 1)
                
                if i_line == 0:
                    mouth = circle
                else:
                    bevel = circle

        with Layout("Lips Bevel"):
            sel = mouth.points.evaluate_on_domain(Integer("Mouth")>0)
            offset = bevel.points.sample_index(nd.position, index=nd.index).scale(0.99) - nd.position
            mouth = mouth.edges[sel].extrude(offset=offset)
            #mouth = mouth.faces.extrude(offset=offset)

            side = mouth.side
            edge_top = mouth.top
            top = mouth.edges.evaluate_on_domain(edge_top)
            mouth.points[top].set("Mouth", 0)
            mouth.points[top].set("tmp Upper", 0)
            mouth.points[top].set("tmp Lower", 0)
            mouth.points[top].set("tmp Weld", 0)

            mouth[side].flip_faces()

            mouth.edges[edge_top].extrude(offset = -nd.position, offset_scale=0.3)
            mouth = meshutil.fill_selection(mouth, mouth.top, center=(0, 0, 0))

        with Layout("Fill Concave Side"):
            
            fill_up = phi_corner > mphi1
            fill_dn = phi_corner < mphi0
            
            nfill = Integer.Switch(fill_up, nbot, ntop)
            fill_line = arc(nfill, mouth_angle, phi_corner, phi_corner, fill_up.bnot())
            fill_line.points.set("tmp Fill", nd.index + 1)
            
            filled = mouth + fill_line
            sel_name = String.Switch(fill_up, "tmp Lower", "tmp Upper")
            filled = OSel.bridge(filled, "tmp Fill", to_name=sel_name, resolution=3, flip=True, remove=False, side_name="tmp Side")
            filled = OSel.rename(filled, "tmp Fill", sel_name)

            filled.points.set("tmp Weld", 0)
            
            sidea = (Integer(String.Switch(smile > 0.5, "tmp Side B", "tmp Side A")) > 0)
            sideb = (Integer(String.Switch(smile > 0.5, "tmp Side A", "tmp Side B")) > 0)
            
            filled.points[sidea].set("tmp Lower", nbot)
            filled.points[sideb].set("tmp Lower", 1)
            filled.points[sidea].set("tmp Upper", 1)
            filled.points[sideb].set("tmp Upper", ntop)
            
            filled.points[sidea].merge(merge_id=1)
            filled.points[sideb].merge(merge_id=1)
            
            filled.points[Integer("tmp Lower")>0].set("tmp Weld", Integer("tmp Lower") + ntop - 1)
            filled.points[Integer("tmp Upper")>0].set("tmp Weld", Integer("tmp Upper"))
            
            mouth.switch(fill_up | fill_dn, filled)

        with Layout("Weld Mouth and rect"):
            rect.points.set("tmp Rect", nd.index + 1)
            rect = OSel.Shift(rect, "tmp Rect", shift=-nside+1)
            
            mouth += rect
            mouth = OSel.bridge(
                mouth, 
                "tmp Rect", 
                to_name="tmp Weld", 
                resolution=3, 
                closed=True, 
                flip=True, 
                bridge_name="tmp Bridge", 
                remove=False)
            
            # Stick on the sphere
            _, y, z = nd.position.xyz
            mouth[Integer("tmp Bridge")>0].position = gnmath.sqrt(1 - y**2 - z**2), y, z
            
        mouth.remove_named_attribute("Wildcard", "tmp*")

        mouth.out()

    # ====================================================================================================
    # Head with mouth
    # ====================================================================================================

    with GeoNodes("Body Head With Mouth"):
        
        # ----------------------------------------------------------------------------------------------------
        # Inputs
        # ----------------------------------------------------------------------------------------------------
        
        with Panel("Resolution", create_layout=True):
            resol = ((Integer(32, "Resolution", 12) // 2)*2)._lc("Segments")
            segments = resol
            rings = (resol//2 + 1)._lc("Base Rings")
            
            phi_center = Float(0.5, "Mouth Position", 0, 1)
            phi_ampl  = Float(0.5, "Mouth Height", 0, 1).interpolate(pi*0.05, pi*0.42)
            shade_smooth = Boolean(True, "Shade Smooth")
            mat = Material(None, "Material")
            
            phi_ampl2 = phi_ampl/2
            
            min_phi0 = pi/20            
            phi_center = phi_center.interpolate(-pi/2 + min_phi0 + phi_ampl2, -phi_ampl2)

            phi0 = phi_center - phi_ampl2
            phi1 = phi_center + phi_ampl2
            
            dphi = pi/(rings - 1)
            
            # below : number of rings below including lower mouth ring
            # mouth : inner rings, excluding lower and upper rings
            # above : number of rings above includine upper mouth ring
            #
            # 0 - - - - - - -  r0 - - - - - - - r1 - - - - - - - n-1
            # <mouth_below_count>               <mouth_above_count>
            #                     <mouth_rings>

            mouth_below_count = ((pi/2+phi0)/dphi).trunc().to_integer().max(4)
            mouth_ring0 = mouth_below_count - 1
            
            mouth_rings = (((phi1 - phi0)/dphi).trunc().to_integer()*4).max(4)
            mouth_ring1 = mouth_ring0 + mouth_rings + 1
            mouth_above_count = ((pi/2 - phi1)/dphi).trunc().to_integer() + 1
            
            nrings = mouth_below_count + mouth_rings + mouth_above_count
            
            #Boolean(True).info("Rings: " + mouth_below_count.to_string() + " " + mouth_rings.to_string() + " "+ mouth_above_count.to_string())
            
            
        with Panel("Expression"):
            smile = Float(0.5, "Smile", 0, 1)
            mouth_open = Float.Factor(0.5, "Open", 0, 1)
            width_fac = Float(0.5, "Width", 0, 1)
            
            no_mouth = (mouth_open == 0) | (width_fac == 0)
            
        # ----------------------------------------------------------------------------------------------------
        # Dimensions
        # ----------------------------------------------------------------------------------------------------
        
        with Layout("Dimensions"):
            
            width_dag = tau/segments
            
            seg_count = segments//4 - 1
            hole_max_angle = 2*seg_count*width_dag
            
            seg_count = (seg_count*width_fac).trunc().to_integer() + 1
            hole_angle = 2*seg_count*width_dag
            
            mouth_angle_fac = width_fac*hole_max_angle/hole_angle
            
        # ----------------------------------------------------------------------------------------------------
        # Starts from a Cylinder shaped in as multires Sphere
        # ----------------------------------------------------------------------------------------------------
        
        with Layout("Sphere From Cylinder"):
            
            head = Mesh.Cylinder(vertices=segments, side_segments=nrings - 1, fill_type='None')
            
            iring = (nd.index // segments)._lc("i ring")
            isegm = (nd.index % segments)._lc("i segm")
            
            # Below rings
            phi = (iring/(mouth_below_count-1)).interpolate(-pi/2, phi0)
            
            # mouth rings
            phi.switch(iring > mouth_ring0, phi0 + phi_ampl*(iring-mouth_ring0)/(mouth_rings+1))
            
            # Above Rings
            phi.switch(iring > mouth_ring1, phi1 + (pi/2 - phi1)*(iring-mouth_ring1)/(mouth_above_count-1))
            
            theta = -(tau/segments)*isegm
            
            z = phi.sin()
            r = phi.cos()
            
            # The middle segment remains the front of each ring.
            head.position = -theta.cos()*r, -theta.sin()*r, z
            
            head.points.set("tmp Pole 0", iring==0)
            head.points.set("tmp Pole 1", iring==nrings-1)
            
        # ----------------------------------------------------------------------------------------------------
        # Dig a hole for the mouth mesh
        # ----------------------------------------------------------------------------------------------------

        with Layout("Mouth Segments Cut Selection"):
            
            mid_seg = segments//2
            
            segm_cut0 = mid_seg - seg_count
            segm_cut1 = mid_seg + seg_count
            
            inner_seg = (isegm > segm_cut0) & (isegm < segm_cut1)
            outer_seg = (isegm >= segm_cut0) & (isegm <= segm_cut1)
            
        with Layout("Mouth Rings Cut Selection"):

            ring_cut0 = mouth_ring0 + 1
            ring_cut1 = mouth_ring1 - 1
            
            rings_sel = (iring >= ring_cut0) & (iring <= ring_cut1)
            
        with Layout("Mark Hole for Mouth"):
            
            cut_sel = rings_sel & inner_seg
            
            head = OSel.add_selection(head, selection=rings_sel & (isegm==segm_cut0), name="Weld")
            head = OSel.add_selection(head, selection=(iring==ring_cut1+1) & outer_seg, name="Weld")
            head = OSel.add_selection(head, selection=rings_sel & (isegm==segm_cut1), invert=True, name="Weld") 
            head = OSel.add_selection(head, selection=(iring==ring_cut0-1) & outer_seg, invert=True, name="Weld")

            head = OSel.shift(head, name="Weld",  shift = 1)
            
        # ----------------------------------------------------------------------------------------------------
        # Create the Mouth to Patch
        # ----------------------------------------------------------------------------------------------------
            
        with Layout("Mouth Dimensions"):
            idx0 = ring_cut0*segments + mid_seg
            
            hole_z0 = head.points.sample_index(nd.position.z, index=(ring_cut0-1)*segments + 1)
            hole_z1 = head.points.sample_index(nd.position.z, index=(ring_cut1+1)*segments + 1)
            hole_h = (hole_z1 - hole_z0)/2
            
            hole_w = -1.5*head.points.sample_index(nd.position.y, index=(ring_cut1+1)*segments - seg_count + 2)
            
        with Layout("Mouth expression"):
            
            mw = width_fac.interpolate(0.01, hole_w)
            mouth = G()._body_mouth(
                horizontal_count = 2*seg_count+1,
                vertical_count = mouth_rings,
                horizontal_angle = hole_angle,
                vertical_min = phi0,
                vertical_max = phi1,
                
                smile=smile, 
                open = mouth_open,
                width=mouth_angle_fac, #mw,
                )

        with Layout("Cut the mouth and bridge Circle"):
            no_mouth_head = Mesh(head)
            
            # Cut the mouth for patch
            head.points[cut_sel].delete()

            # Patch the mouth
            head += mouth
            head.points[Integer("Weld")>0].merge(merge_id=Integer("Weld"))
            head.remove_named_attribute(name="Weld")

        # ----------------------------------------------------------------------------------------------------
        # Finalize
        # ----------------------------------------------------------------------------------------------------
            
        with Layout("Finalize"):
            head.switch(no_mouth, no_mouth_head)
            head.points[Boolean("tmp Pole 0")].merge(merge_id=1)
            head.points[Boolean("tmp Pole 1")].merge(merge_id=1)
            
            head.remove_named_attribute("Wildcard", "tmp *")
            
            head.faces.shade_smooth=shade_smooth
            head.faces.material = mat

            head.out()

    # ====================================================================================================
    # Head parameters
    # ====================================================================================================
    
    with GeoNodes("Body Head Anim", is_group=False, rebuild=rebuild):

        mesh = Mesh()
        
        factor = Float.Factor(1.0, "Factor", 0, 1)
        
        head_rot = Vector.Euler(0, "Head Rotation")
        
        with Panel("Eyes"):
            
            same_eyes = Boolean(True, "Same Direction")
            
            left_eye_rot = G()._direction_input(location=0).link_inputs(from_panel="Left")
            right_eye_rot = G()._direction_input(location=0).link_inputs(from_panel="Right")
            right_eye_rot.switch(same_eyes, left_eye_rot)
            
            same_lids = Boolean(True, "Same Lids")
            with Panel("Left"):
                left_lid_open = Float.Factor(0.5, "Open Lid", 0, 1)
                left_lid_severe = Float.Factor(0.5, "Severe", 0, 1)
                
                left_lid = Vector((left_lid_open, left_lid_severe, 0))
                
            with Panel("Right"):
                right_lid_open = Float.Factor(0.5, "Open Lid", 0, 1)
                right_lid_severe = Float.Factor(0.5, "Severe", 0, 1)
                
                right_lid = Vector((right_lid_open, right_lid_severe, 0))
                
                right_lid.switch(same_lids, left_lid)
                
        with Panel("Mouth"):
            mouth_smile = Float.Factor(0.5, "Smile", 0, 1)
            mouth_open = Float.Factor(0.5, "Open", 0, 1)
            mouth_width = Float.Factor(0.5, "Width", 0, 1)
            
            mouth = Vector((mouth_smile, mouth_open, mouth_width))

        mesh_bundle = mesh.get_bundle()
        bundle = mesh_bundle.get_item("Head", socket_type='BUNDLE')
        
        with Bundle() as def_bundle:
            Vector.Out(0, "Head")
            
            Vector.Out(0, "Left Eye")
            Vector.Out(0, "Right Eye")
            
            Vector.Out((0.6, 0.5, 0), "Left Lid")
            Vector.Out((0.6, 0.5, 0), "Right Lid")

            Vector.Out((0.5, 0.0, 0.5), "Mouth")
            
        bundle.switch_false(bundle.exists, def_bundle)
        
        head_pose = bundle.separate(signature=HEAD_POSE_SIG)
        
        with Bundle() as new_bundle:
            
            head_pose.head.mix(head_rot, factor=factor).out("Head")
            
            head_pose.left_eye.mix(left_eye_rot, factor=factor).out("Left Eye")
            head_pose.right_eye.mix(right_eye_rot, factor=factor).out("Right Eye")
            
            head_pose.left_lid.mix(left_lid, factor=factor).out("Left Lid")
            head_pose.right_lid.mix(right_lid, factor=factor).out("Right Lid")

            head_pose.mouth.mix(mouth, factor=factor).out("Mouth")
        
        mesh_bundle.set_item("Head", new_bundle)
        mesh.set_bundle(mesh_bundle)
        
        mesh.out()
        new_bundle.out("Head Pose")

    # ====================================================================================================
    # Body Head
    # ====================================================================================================

    with GeoNodes("Body Head", is_group=False, rebuild=rebuild):

        mesh = Mesh()
        
        # ----------------------------------------------------------------------------------------------------
        # Animation parameters
        # ----------------------------------------------------------------------------------------------------
        
        bundle = G().body_head_anim(mesh, factor=0).head_pose
        
        head_pose = bundle.separate(signature=HEAD_POSE_SIG)
        
        # ----------------------------------------------------------------------------------------------------
        # Inputs
        # ----------------------------------------------------------------------------------------------------
        
        blink_delay = Float.TimeAbsolute(3, "Blink", 0, shape="Single")
        head_height = Float(1.0, "Size", 0.1, 1, shape="Single")
        resol  = Integer(8, "Resolution", 1, 8, shape="Single")
        mat = Material("Obs Skin", "Material") 
        
        with Panel("Shape", create_layout=True):
            width = Float.Factor(0.6, "Width", 0, 1, shape='Single').interpolate(0.4, 1.3)
            depth = Float.Factor(0.6, "Depth", 0, 1, shape='Single').interpolate(0.4, 1.4)
            pear_shape = Float.Factor(0.0, "Pear Factor", 0, 1, shape='Single').interpolate(-1, 1)
            shape_signature = ({"Position": Vector}, {"Position": Vector})
            head_shape = G()._body_pear_shape(
                width=width, depth=depth, height=1.0, pear_factor=pear_shape)
            
            # ----------------------------------------------------------------------------------------------------
            # Transform location at the head surface
            # ----------------------------------------------------------------------------------------------------

            # Shared hair/head convention: front +X, lateral Y, up +Z.
            def x_coord(y, z):
                return gnmath.sqrt(gnmath.max(1 - y**2 - z**2, 0))
            
            def transform_head_location(x, y, z):
                return head_shape.evaluate(
                    position=(x, y, z), signature=shape_signature).xyz

            # ----------------------------------------------------------------------------------------------------
            # Head
            # ----------------------------------------------------------------------------------------------------
            
            segments = resol*8
            rings = resol*4
            
            if True:
                mouth_smile, mouth_open, mouth_width = head_pose.mouth.xyz
                head = G().body_head_with_mouth(
                    resolution = segments,
                    mouth_position = 0.5,
                    mouth_height = 0.5,
                    smile = mouth_smile,
                    open = mouth_open,
                    width = mouth_width,
                    shade_smooth = True,
                    material = mat,
                )
                
                nose = Mesh.UVSphere(segments=segments, rings=rings, radius=1.0)
                nose.faces.material = mat
                nose.faces.shade_smooth = True
                
            else:
                head = Mesh.UVSphere(segments=segments, rings=rings, radius=1.0)
                head.faces.shade_smooth = True
                head.faces.material = mat
                
                nose = Mesh(head)
                
            head.position = head_shape.evaluate(position=nd.position, signature=shape_signature)
                
        # ----------------------------------------------------------------------------------------------------
        # Nose
        # ----------------------------------------------------------------------------------------------------
        
        with Panel("Nose", create_layout=True):
            nose_length = Float.Factor(0.5, "Length", 0, 1, shape='Single').interpolate(0.01, 0.8)
            nose_width = Float.Factor(0.5, "Width", 0, 1, shape='Single').interpolate(0.2, 0.7)
            nose_height = Float.Factor(0.5, "Height", 0, 1, shape='Single').interpolate(0.2, 0.7)
            nose_z = Float.Factor(0.5, "Position", 0, 1, shape='Single').interpolate(0.0, 0.5)
            nose_pear = Float.Factor(0.5, "Pear Factor", 0, 1, shape='Single').interpolate(-1, 1)
            nose_x = Float.Factor(0.5, "Inside", 0, 1, shape='Single').interpolate(-0.1, 0.7)
            
            nose_shape = G()._body_pear_shape(
                width=width, depth=depth, height=1.0, pear_factor=nose_pear)
            nose.position = nose_shape.evaluate(position=nd.position, signature=shape_signature)
            
            nose_width  *= nose_length
            nose_height *= nose_length
            
            x, y, z = transform_head_location(x_coord(0, nose_z), 0, nose_z)
            nose.transform(rotation=(0, -pi/2, 0), translation=(x + nose_x*nose_length, y, z), scale=(nose_height, nose_width, nose_length))
            
            mouth_z_max = nose_z - 2*nose_height
            
            node = head.points[nd.position.z < mouth_z_max].attribute_statistic(nd.position.y).node
            y_max = node.max
            
            mouth_y_max = 0.9*y_max
            
        # ----------------------------------------------------------------------------------------------------
        # Eyes
        # ----------------------------------------------------------------------------------------------------
            
        with Panel("Eyes", create_layout=True):
            eye_radius = Float.Factor(0.1, "Size", 0, 1, shape='Single').interpolate(0.05, 0.3)
            eye_z = Float.Factor(0.5, "Position", 0, 1, shape='Single')#.interpolate(0.0, 0.8)
            eye_y = Float.Factor(0.6, "Distance", 0, 1, shape='Single').interpolate(0.0, 0.8)
            eye_x = Float.Factor(0, "Inside", 0, 1, shape='Single').interpolate(-1, 1)
            
            eye_z = eye_z.interpolate(nose_z+0.8*nose_height, 0.9)
            
            eye = Mesh.UVSphere(segments=segments//2, rings=rings//2, radius=eye_radius)
            eye.faces.set('White', nd.position.z < .9*eye_radius)
            eye.transform(rotation=(0, pi/2, 0))
            eye.points.set("Head", 1)

            eye.faces.shade_smooth = True
            eye.faces.material = "Obs Eye"
            
            eye_y = eye_y.max(eye_radius+nose_width)
            eye_y = eye_y.min(x_coord(0, eye_z))
            
            x, y, z = transform_head_location(x_coord(eye_y, eye_z), eye_y, eye_z)
            x += eye_x*eye_radius
            left_loc = (x, y, z)
            right_loc = (x, -y, z)
            
            left_eye = Mesh(eye)
            left_eye.transform(rotation=head_pose.left_eye)
            left_eye.offset = left_loc
            
            right_eye = Mesh(eye)
            right_eye.transform(rotation=head_pose.right_eye)
            right_eye.offset = right_loc
            
        # ----------------------------------------------------------------------------------------------------
        # Eye Lids
        # ----------------------------------------------------------------------------------------------------
        
        with Layout("Eye Lids"):
            lid_radius = eye_radius*1.2

            nsegms = segments // 2
            eyelid = Mesh.UVSphere(segments=nsegms, rings=rings//2, radius=1.0)
            eyelid.points[nd.position.z < -0.01].delete()
            eyelid.faces.shade_smooth = True
            disk = Mesh.Circle(vertices=nsegms, radius=1.0, fill_type='NGON').flip_faces()

            eyelid += disk
            eyelid.merge_by_distance()

            eyelid.position = nd.position.scale(lid_radius)

            eyelid.faces.material = "Obs Skin"
            
            with Layout("Blink"):
                blink = blink_delay >= 1.0
                time = nd.scene_time().seconds
                blink_animation = (((time/blink_delay) % 1.0) - 0.5).abs().map_range(0, 0.05, 0, 1)
                blink_animation.switch_false(blink)
            
            with Layout("Left Lid"):            
                left_eyelid = Mesh(eyelid)
                
                fx, fy, _ = head_pose.left_lid.xyz
                fx = fx.min(blink_animation)
                opening_angle = fx.interpolate(-pi/2, pi/2)
                tilt_angle = fy.interpolate(-0.5*pi/2, 0.5*pi/2)
                lid_rotation = Rotation((0, -opening_angle, 0)).rotate_local((tilt_angle, 0, 0))
                left_eyelid.transform(rotation=lid_rotation)
                
                left_eyelid.offset = left_loc
                
            with Layout("Right Lid"):
                right_eyelid = Mesh(eyelid)

                fx, fy, _ = head_pose.right_lid.xyz
                fx = fx.min(blink_animation)
                opening_angle = fx.interpolate(-pi/2, pi/2)
                tilt_angle = fy.interpolate(-0.5*pi/2, 0.5*pi/2)
                lid_rotation = Rotation((0, -opening_angle, 0)).rotate_local((-tilt_angle, 0, 0))
                right_eyelid.transform(rotation=lid_rotation)
                
                right_eyelid.offset = right_loc
            
        with Panel("Hair", create_layout=True):
            hair_obj  = Object(None, "Hair Object")
            hair_mat  = Material("Obs Hair", "Hair Material")
            use_hair  = Boolean(True,    "Hair")
            hair_col  = Color([0.061606, 0.008269, 0.002920, 1.000000], "Hair Color")
            use_moust = Boolean(True,    "Moustache")
            moust_col = Color([0.061606, 0.008269, 0.002920, 1.000000], "Moustache Color")

        # ----------------------------------------------------------------------------------------------------
        # Hair
        # ----------------------------------------------------------------------------------------------------

        with Panel("Scalp", create_layout=True):
            scalp_resol = Integer(32, "Scalp Resolution", 12)
            scalp_lod = Float(1.0, "Scalp LoD", 0, 1)
            scalp = Mesh(G().body_head_scalp(
                invert_normals=False,
                resolution=scalp_resol,
                lod=scalp_lod,
            ).link_inputs(exclude=["Moustache Scalp"]))

        # ----------------------------------------------------------------------------------------------------
        # Finalize
        # ----------------------------------------------------------------------------------------------------
        
        with Layout("Finalize"):
            head += nose, left_eye, right_eye, left_eyelid, right_eyelid
            
            head.transform(translation=(0, 0, head_height), scale=head_height)
            head.transform(rotation=head_pose.head)

            # Hair generation uses the scalp in its normalized coordinates.
            head += scalp

        with Closure() as hair_shape:
            position = Vector(name="Position")
            position = head_shape.evaluate(
                position=position,
                signature=shape_signature,
            )
            position = position.scale(head_height) + Vector((0, 0, head_height))
            position = Rotation(head_pose.head) @ position
            position.out("Position")

        hair_shape.out("Pear Shape")
        head.out()

          

def demo(rebuild=False):

    common.demo()

    # ----------------------------------------------------------------------------------------------------
    # Common
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Body Pear Shape", is_group=True, rebuild=rebuild):
        # Front +X (depth), lateral Y (width), up +Z (height).
        height = Float(1.0, "Height", 0)
        width = Float(1.0, "Width", 0)
        depth = Float(1.0, "Depth", 0)
        pear_factor = Float(0.0, "Pear Factor", -1, 1)

        with Closure() as cl:
            position = Vector(name="Position")

            x, y, z = position.xyz
            radial_scale = 1 - 0.7 * pear_factor * z
            shaped_position = Vector((x * radial_scale * depth,
                                    y * radial_scale * width,
                                    z * height))
            shaped_position.out("Position")

        cl.out("Shape")

    # ----------------------------------------------------------------------------------------------------
    # Body Parts
    # ----------------------------------------------------------------------------------------------------

    demo_hand(rebuild=rebuild)
    demo_hair(rebuild=rebuild)
    demo_head(rebuild=rebuild)

    # ----------------------------------------------------------------------------------------------------
    # Body Test
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Body Test", rebuild=rebuild):
        geo = Mesh()
        head = G().body_head(geo).link_inputs()
        pear_shape = head.node.pear_shape
        head.set_bundle(Bundle.Combine({"Pear Shape": pear_shape}))
        head.out()



