from geonodes import *

# ====================================================================================================
# For a flat mesh in the plane XY, compute vertices coordinates relatively to
# the vectors computed from 3 points
# These coordinates can be then used to compyte sub shape in space with possible deformations
# ====================================================================================================

iter_signature = (
    {'Mesh'             : Mesh,
     'Model'            : Mesh,
     'Rotation'         : Float,
     'Hue Scale'        : Float,
    },
    {'Mesh'             : Mesh,
    },
)

def plane_triangle_coordinates(mesh, iO, iu, iv):
    
    with Layout("Plane tri coordinates"):
          
        O = mesh.points.sample_index(nd.position, index=iO)._lc("O")
        
        # The two vectors or the base
        u = (mesh.points.sample_index(nd.position, index=iu) - O)._lc("u")
        v = (mesh.points.sample_index(nd.position, index=iv) - O)._lc("v")
        w = u.cross(v)._lc("w")
        w = w.normalize().scale(w.length().sqrt())
        lw = w.length()
        
        ux, uy, _ = u.xyz
        vx, vy, _ = v.xyz
        
        delta = ux*vy - uy*vx
        
        p = (nd.position - O)._lc("p")
        x, y, z = p.xyz

        mesh.points.Rel_coords = Vector((
            (x*vy - y*vx)/delta,
            (ux*y - uy*x)/delta,
            (z/lw)*Float.Switch(p.dot(w) < 0, 1, -1)
        ))
        
        
    return mesh

def get_face_base(mesh, face_index=0):
    
    with Layout("Face local base"):
    
        c0 = mesh.faces.corner_index(face_index, sort_index=0)
        c1 = mesh.faces.corner_index(face_index, sort_index=1)
        c2 = mesh.faces.corner_index(face_index, sort_index=2)
        
        i0 = mesh.corners.vertex_index(c0)
        i1 = mesh.corners.vertex_index(c1)
        i2 = mesh.corners.vertex_index(c2)
        
        O = mesh.points.sample_index(nd.position, index=i1)._lc("O")
        
        u = (mesh.points.sample_index(nd.position, index=i0) - O)._lc("u")
        v = (mesh.points.sample_index(nd.position, index=i2) - O)._lc("v")
        w = u.cross(v)._lc("w")
        w = w.normalize().scale(w.length().sqrt())
        
        return O, u, v, w
    
def demo():

    from geonodes.demos import random, cam_culling
    random.demo()
    cam_culling.demo()

    # ====================================================================================================
    # Flat fractal closure
    # ====================================================================================================

    # The model is a face split into similary sub faces
    # The is preparaed 

    with GeoNodes("Flat Fractal Closure", is_group=True):
        
        with Closure() as cl:
            
            mesh = Mesh()

            model     = Mesh(None, "Model")
            rotation  = Float(0,   "Rotation")
            hue_scale = Float(0.5, "Hue Scale")
            
            O, u, v, w = get_face_base(mesh, face_index=nd.index)

            for feel in mesh.faces.for_each(O=O, u=u, v=v, w=w):
                
                face = Mesh(feel.element)
                
                depth    = face.faces.sample_index(Integer("Depth"), index=0) + 1
                face_id  = face.faces.sample_index(Integer("Uid"), index=0)
                face_hue = face.faces.sample_index(Float("Hue"), index=0)

                # New faces = transformed model
                new_faces = Mesh(model)
                cx, cy, cz = Vector("Rel coords").xyz
                new_faces.position = feel.O + feel.u.scale(cx) + feel.v.scale(cy) + feel.w.scale(cz)

                # Unique Id
                new_faces.faces.Uid = Integer.Random(0, 1_000_000_000, id=nd.index, seed=face_id)

                # Random rotation of child points
                face_rot = rotation*(0.5**depth)
                rot = G().random_normal_value(0, face_rot, seed=face_id.hash_value(1390887)).single
                new_faces[Boolean("Child")].position = Rotation.FromAxisAngle(nd.normal, rot) @ nd.position
                new_faces.remove_named_attribute(name="Child")

                # Depth & Hue
                new_faces.faces.Depth = depth
                new_faces.faces.Hue = (face_hue + G().random_normal_value(0.0, hue_scale**depth, seed=face_id.hash_value(7491998))) % 1.0

                # Done
                feel.geometry = new_faces
                
            res = Mesh(feel.generated)
            res.merge_by_distance()

            res.out("Mesh")
                
        
        cl.out()
        
    # ====================================================================================================
    # Fractal engine
    # ====================================================================================================

    with GeoNodes("Fractal From Model", is_group=True) as tree:
        
        mesh      = Mesh()
        count     = Integer(2, "Count", 1, 15)
        rotation  = Float.Angle(0, "Rotation")
        hue_scale = Float.Factor(0.5, "Hue Scale", 0, 1)
        mat       = Material(None, "Material")
        seed      = Integer(0, "Seed")
        
        with Panel("Model"):
            model = Mesh(None, "Model")
            iO    = Integer(1, "Origin Index", shape='Single')
            iu    = Integer(0, "U Index", shape='Single')
            iv    = Integer(2, "V Index", shape='Single')

        cam_culling = G().camera_face_culling().link_inputs(from_panel="Camera Culling", panel="Camera Culling").node

        with Layout("Prepare Model"):
            cl = G().flat_fractal_closure()
            
            model = plane_triangle_coordinates(model, iO, iu, iv)
            model.points[iO].Child = False
            model.points[iu].Child = False
            model.points[iv].Child = False

        # Initialize named attributes
        with Layout("Initialize Attributes"):
            mesh.faces.Uid   = Integer.Random(0, 1_000_000_000, seed=seed)
            mesh.faces.Hue   = Float.Random(0, 1, seed=seed + 1)
            mesh.faces.Depth = 0

        # Loop
        for rep in repeat(count, to_split=mesh, fractal=None):

            depth = rep.iteration + 1

            cam_culling.mesh = rep.to_split
            rep.fractal += cam_culling.deleted
            to_split = cam_culling.mesh

            new_mesh = cl.evaluate(
                mesh        = to_split,
                model       = model,
                rotation    = rotation,
                hue_scale   = hue_scale,
                signature   = iter_signature)

            # Candidate for further splitting
            rep.to_split = new_mesh

        # Merge all faces
        res = Mesh(rep.to_split + rep.fractal)  

        # Finalize  
        res.faces.Random = Float.Random(0, 1, id=Integer("Uid"), seed=0)
        res.faces.material = mat
            
        res.out()

    # ====================================================================================================
    # Fractal a Mesh with a model object
    # ====================================================================================================

    with GeoNodes("Fractal Mesh"):
        
        mesh = Mesh()

        with Panel("Model"):
            obj  = Object(None, "Model")
            model = Mesh(obj.info().geometry)

        G().fractal_from_model(mesh, model=model).link_inputs().out()

    # ====================================================================================================
    # Demo Shader
    # ====================================================================================================

    with ShaderNodes("Fractal Demo", replace_material=True):

        hue = snd.attribute("Hue").factor
        color = Color.CombineHSV(hue=hue, value=1, saturation=1)
        ped = Shader.Principled(
            base_color = color,
            roughness = 0.2,
            metallic = 0.7)
        ped.out()


    # ====================================================================================================
    # Sierpinski
    # ====================================================================================================

    with GeoNodes("Sierpinksi"):

        tri = Mesh.Circle(vertices=3, fill_type='N-Gon').transform(rotation=(0, 0, pi/6))

        with Layout("Build the model"):
            dims = tri.points.attribute_statistic(nd.position)
            size = dims.max_ - dims.min_
            sx, sy, _ = size.xyz

            model = tri + (Mesh(tri).transform(translation=(-sx/2, sy, 0)), Mesh(tri).transform(translation=(sx/2, sy, 0)))
            model.merge_by_distance()

            model.points.Child = True
            model.points[2].Child = False
            model.points[4].Child = False
            model.points[5].Child = False

        tri.faces.Hue = 0.5

        G().fractal_from_model(tri, origin_index=2, u_index=4, v_index=5, model=model).link_inputs().out()
            
    # ====================================================================================================
    # Cubes Pyramid
    # ====================================================================================================

    with GeoNodes("Cubes Pyramid"):

        with Layout("Build the model"):

            cube = Mesh.Cube()

            cube.faces[nd.index==0].delete_only_face().transform(translation=(0, 0, 0.5))

            face = Mesh.Grid(vertices_x=2, vertices_y=2).transform(translation=(-1, -1, 0))

            base = face + (Mesh(face).transform(translation=(1, 0, 0)), Mesh(face).transform(translation=(2, 0, 0)))
            base += Mesh(base).transform(translation=(0, 2, 0))
            base += (Mesh(face).transform(translation=(0, 1, 0)), Mesh(face).transform(translation=(2, 1, 0)))

            cube += base
            cube.merge_by_distance()

            cube.points.Child = False
            cube.points[nd.position.z > 0.5].Child = True
            cube.points[nd.index <= 4].Child = True

        square = Mesh.Grid(vertices_x=2, vertices_y=2)
        square.faces.Hue = 0.5

        frac = G().fractal_from_model(square, origin_index=8, u_index=15, v_index=12, model=cube).link_inputs()

        frac.out()
        cube.out("Model")

    # ====================================================================================================
    # Pyramid
    # ====================================================================================================

    with GeoNodes("Pyramid"):

        import math

        mesh = Mesh()

        with Layout("Build the model"):

            h = math.sqrt(2)

            cone = Mesh.Cone(vertices=3, depth=h)
            cone.faces[3].delete_only_face()

            tri = Mesh.Circle(vertices=3, fill_type='N-Gon')
            cone += Mesh(tri).transform(translation=(-1, 0, 0), rotation=(0, 0, pi))
            cone += Mesh(tri).transform(translation=(.5, math.sqrt(3)/2, 0), rotation=(0, 0, pi/3))
            cone += Mesh(tri).transform(translation=(.5, -math.sqrt(3)/2, 0), rotation=(0, 0, pi/3))

            cone.merge_by_distance()

            cone.faces.Child = True

        mesh.faces.Hue = 0.5

        tri.faces.Hue = 0.5
        frac = G().fractal_from_model(mesh, origin_index=4, u_index=5, v_index=6, model=cone).link_inputs()

        frac.out()
        cone.out("Model")        

            
        
        
        
        
        
        
        
        
        
        