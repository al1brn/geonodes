from geonodes import *

# ====================================================================================================
# For a flat mesh in the plane XY, compute vertices coordinates relatively to
# the vectors computed from 3 points
# These coordinates can be then used to compyte sub shape in space with possible deformations
# ====================================================================================================

iter_signature = (
    {'Mesh'             : Mesh,
     'Selection'        : Boolean,
     'Model'            : Mesh,
     'Depth'            : Integer,
     'Seed'             : Integer,
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
            
            mesh    = Mesh()
            sel     = Boolean(True, "Selection")

            model   = Mesh(None, "Model")
            depth   = Integer(1, "Depth")     
            seed    = Integer(0, "Seed")
            
            O, u, v, w = get_face_base(mesh, face_index=nd.index)
            for feel in mesh.faces.for_each(sel=sel, O=O, u=u, v=v, w=w):
                
                face = Mesh(feel.element)
                
                new_faces = Mesh(model)
                cx, cy, cz = Vector("Rel coords").xyz
                new_faces.position = feel.O + feel.u.scale(cx) + feel.v.scale(cy) + feel.w.scale(cz)

                new_faces.faces.Depth = depth
                new_faces.faces.Hue = face.faces.sample_index(Float("Hue"), index=0)
                # Face UID is based only on the hierarchy
                new_faces.faces.Uid = face.faces.sample_index(Integer("Uid"), index=0).hash_value(seed=971647)
                
                feel.geometry = face.switch(feel.sel, new_faces)
                
            res = Mesh(feel.generated)
            res.merge_by_distance()

            res.out("Mesh")
                
        
        cl.out()
        
    # ====================================================================================================
    # Fractal engine
    # ====================================================================================================

    with GeoNodes("Fractal From Model", is_group=True) as tree:
        
        mesh    = Mesh()
        count   = Integer(2, "Count", 1)
        mat     = Material(None, "Material")
        seed    = Integer(0, "Seed")
        
        with Panel("Model"):
            model = Mesh(None, "Model")
            iO    = Integer(1, "Origin Index", shape='Single')
            iu    = Integer(0, "U Index", shape='Single')
            iv    = Integer(2, "V Index", shape='Single')

        cl = G().flat_fractal_closure()
        
        model = plane_triangle_coordinates(model, iO, iu, iv)

        mesh.faces.Seed = seed
        
        for rep in repeat(count, mesh=mesh):

            depth = rep.iteration + 1

            with Layout("Camera Culling"):
                node = G().camera_face_culling(rep.mesh).link_inputs(from_node=tree.input_node, from_panel="Culling").node

            new_mesh = cl.evaluate(
                mesh        = rep.mesh, 
                selection   = True, 
                model       = model,
                depth       = depth,
                seed        = seed.hash_value(rep.iteration),
                signature   = iter_signature)
            
            sel_new = Integer("Depth") == depth

            hue_scale = 0.5**(rep.iteration + 1)
            new_mesh.faces[sel_new].Hue = (Float("Hue") + G().random_normal_value(Float("Hue"), hue_scale, seed=seed + 1)) % 1.0

            rep.mesh = new_mesh

        res = rep.mesh
        res.faces.Random = Float.Random(0, 1, seed=Integer("Uid"))

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

        tri.faces.Hue = 0.5

        G().fractal_from_model(tri, origin_index=2, u_index=4, v_index=5, model=model).link_inputs().out()

            
            
        
        
        
        
        
        
        
        
        
        