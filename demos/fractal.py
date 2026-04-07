from geonodes import *

# ====================================================================================================
# For a flat mesh in the pnae XY, compute vertices coordinates relatively to
# the vectors computed from 3 points
# These coordinates can be then used to compyte sub shape in space with possible deformations
# ====================================================================================================

iter_signature = (
    {'Mesh'             : Mesh,
     'Selection'        : Boolean,
     'Model'            : Mesh,
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
        #w = w.scale(lw.sqrt())
        
        ux, uy, _ = u.xyz
        vx, vy, _ = v.xyz
        
        delta = ux*vy - uy*vx
        
        p = (nd.position - O)._lc("p")
        x, y, z = p.xyz
        
        mesh.points.Cx = (x*vy - y*vx)/delta
        mesh.points.Cy = (ux*y - uy*x)/delta
        mesh.points.Cz = (z/lw)*Float.Switch(p.dot(w) < 0, 1, -1)
        
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


with GeoNodes("Test"):
    
    mesh = Mesh()
    mesh = plane_triangle_coordinates(mesh, 0, 1, 2)
    mesh.out()


# ====================================================================================================
# Flat fractal closure
# Each face is replaced by the model
# ====================================================================================================

with GeoNodes("Flat Fractal Closure", is_group=True):
    
    with Closure() as cl:
        
        mesh    = Mesh()
        sel     = Boolean(True, "Selection")

        model   = Mesh(None, "Model")        
        seed    = Integer(0, "Seed")
        
        O, u, v, w = get_face_base(mesh, face_index=nd.index)
        
        for feel in mesh.faces.for_each(sel=sel, O=O, u=u, v=v, w=w):
            
            face = Mesh(feel.element)
            
            new_faces = Mesh(model)
            new_faces.position = feel.O + Float("Cx")*feel.u + Float("Cy")*feel.v + Float("Cz")*feel.w
            
            
            feel.geometry = face.switch(feel.sel, new_faces)
            
        splitted = Mesh(feel.generated)
        splitted.merge_by_distance()
            
        splitted.out("Mesh")
            
    
    cl.out()
    
# ====================================================================================================
# Fractal engine
# ====================================================================================================

with GeoNodes("Fractal Mesh"):
    
    mesh    = Mesh()
    count   = Integer(2, "Count", 1)
    
    with Panel("Model"):
        obj  = Object(None, "Model")
        iO   = Integer(1, "Origin Index", shape='Single')
        iu   = Integer(0, "U Index", shape='Single')
        iv   = Integer(2, "V Index", shape='Single')
    
    cl = G().flat_fractal_closure()
    
    model = Mesh(obj.info().geometry)
    
    model = plane_triangle_coordinates(model, iO, iu, iv)
    
    for rep in repeat(count, mesh=mesh):
        rep.mesh = cl.evaluate(mesh=rep.mesh, selection=True, model=model, signature=iter_signature)
        
    rep.mesh.out()
        
        
    
    
    
    
    
    
    
    
     
    