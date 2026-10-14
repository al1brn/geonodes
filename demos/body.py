from geonodes import *

import math
from math import radians

# ====================================================================================================
# Hand constants
# ====================================================================================================

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

# ====================================================================================================
# Body Demo
# ====================================================================================================

def demo(rebuild=False):

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
    
    with GeoNodes("Body Hand Pose Preset", is_group=True, rebuild=rebuild):
        
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
            
            palm.faces.shade_smooth=True
            palm.faces.material = mat
            palm.out()
    
demo()

