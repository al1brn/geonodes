# Maths groups

``` python
import bpy
from geonodes import GeoNodes

print('-'*100)
print("Building the 4D engine: maths functions")
print()

CLEAR   = True
REBUILD = True

maths = GeoNodes.prefixed("M")

ZERO = 0.0001

# ----------------------------------------------------------------------------------------------------
# Select

def select(tree, selector, *values):
    
    count = len(values)
    if count == 0:
        return None
    
    with tree.layout("Selection"):
    
        res = values[0]
        for i in range(1, count):
            res = res.switch(selector.equal(i), values[i])
        
        return res

# ----------------------------------------------------------------------------------------------------
# dot

def gen_dot(tree, u0, w0, u1, w1, layout=False, label="Dot 4D"):
    
    if layout:
        with tree.layout(label):
            return u0.dot(u1) + w0*w1
        
    elif label is None:
        return u0.dot(u1) + w0*w1
    
    else:
        a = u0.dot(u1)
        a.node.node_label = label
        b = w0*w1
        b.node.node_label = label
        c = a + b
        c.node.node_label = label
        return c

# ----------------------------------------------------------------------------------------------------
# Projection matrix

def projection_matrix():
    
    with GeoNodes("Projection Matrix", is_group=True, fake_user=True, prefix=maths) as tree:
        
        abc = tree.ObjectInfo("Projection").rotation
        
        a = abc.x
        b = abc.y
        c = abc.z
        
        ca = tree.cos(a)
        sa = tree.sin(a)
        cb = tree.cos(b)
        sb = tree.sin(b)
        cc = tree.cos(c)
        sc = tree.sin(c)
        
        M = (
                (    ca, 0.,    -sa*sc,    -sa*cc),
                (-sa*sb, cb, -ca*sb*sc, -ca*sb*cc),
                (    0., 0.,        cc,       -sc),
                ( sa*cb, sb,  ca*cb*sc,  ca*cb*cc),
            )
            
        tree.vector(M[0][:3]).to_output("Row 0 xyz")
        M[0][ 3].to_output("Row 0 w")
        tree.vector(M[1][:3]).to_output("Row 1 xyz")
        M[1][ 3].to_output("Row 1 w")
        tree.vector(M[2][:3]).to_output("Row 2 xyz")
        M[2][ 3].to_output("Row 2 w")
        
        tree.vector(M[3][:3]).to_output("Dir xyz")
        M[3][ 3].to_output("Dir w")
        
        
# ----------------------------------------------------------------------------------------------------
# Perform a projection
#
# Takes the 4 parameters of a projection matrix plus
# - xyz : the xyz components
# - w   : the addition 4th component

def projection():
    
    with GeoNodes("Projection", is_group=True, fake_user=True, prefix=maths) as tree:

        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        mproj = maths.projection_matrix()
        
        mv0 = mproj.row_0_xyz
        mw0 = mproj.row_0_w
        mv1 = mproj.row_1_xyz
        mw1 = mproj.row_1_w
        mv2 = mproj.row_2_xyz
        mw2 = mproj.row_2_w

        x = mv0.dot(v) + mw0*w
        y = mv1.dot(v) + mw1*w
        z = mv2.dot(v) + mw2*w
        
        tree.vector((x, y, z)).to_output("Vector")
        
# ----------------------------------------------------------------------------------------------------
# length

def length():
    
    with GeoNodes("Length", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w", 1.)
        
        length = tree.sqrt(v.dot(v) + w*w)
        null   = length.less_than(ZERO)
        
        length.to_output("Length")
        null.to_output("Null")
        
# ----------------------------------------------------------------------------------------------------
# Normalize

def normalize():
    
    with GeoNodes("Normalize", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w", 1.)
        
        node = maths.length(xyz=v, w=w) 
        
        #n = maths.length(xyz=v, w=w).length
        #null = gn.Boolean(n.less_than(zero))
        
        rv = (v/node.length).switch(node.null, tree.vector(0))
        rw = (w/node.length).switch(node.null, tree.float(0))

        rv.to_output("xyz")
        rw.to_output("w")
        node.null.to_output("Null")
        
# ----------------------------------------------------------------------------------------------------
# Normal basis
#
# 3 vectors forming a normal basis to a 2D hyperplane defined by three independant vectors

def normal_basis():
    
    with GeoNodes("Normal basis", is_group=True, fake_user=True, prefix=maths) as tree:
        
        u0 = tree.vector_input("xyz 0", (1, 0, 0))
        w0 = tree.float_input( "w 0")
        u1 = tree.vector_input("xyz 1", (0, 1, 0))
        w1 = tree.float_input( "w 1")
        u2 = tree.vector_input("xyz 2", (0, 0, 1))
        w2 = tree.float_input( "w 2")
        
        # ----- Let's normalize the first input
        
        with tree.layout("Normalize entry"):
        
            node = maths.normalize(xyz=u0, w=w0)
            e0   = node.xyz
            t0   = node.w
            null = node.null
            
        # ----- (e0, t0) is the first vector
        # Let's suppress this dimension in the second one
        
        with tree.layout("Make the second vector perp to the first"):
        
            #d   = e0.dot(u1) + t0*w1
            d   = gen_dot(tree, e0, t0, u1, w1, layout=True)
            u1 -= e0*d
            w1 -= t0*d
            
            # ----- Let's normalize
            
            node = maths.normalize(xyz=u1, w=w1)
            e1   = node.xyz
            t1   = node.w
            null = null + node.null
            
        with tree.layout("Make the third vector perp to the two other ones"):
        
            # ----- (e0, t0) and (e1, t1) are two basis vectors
            # Let's suppress these dimensions in the third one

            #d = e0.dot(u2) + t0*w2
            d   = gen_dot(tree, e0, t0, u2, w2, layout=True)
            u2 -= e0*d
            w2 -= t0*d
            
            #d = e1.dot(u2) + t1*w2
            d   = gen_dot(tree, e1, t1, u2, w2, layout=True)
            u2 -= e1*d
            w2 -= t1*d
            
            # ----- Let's normalize
            
            node = maths.normalize(xyz=u2, w=w2)
            e2   = node.xyz
            t2   = node.w
            null = null + node.null
            
        # ----- We are done :-)
        
        e0.to_output("xyz 0")
        t0.to_output("w 0")
        e1.to_output("xyz 1")
        t1.to_output("w 1")
        e2.to_output("xyz 2")
        t2.to_output("w 2")
        
        null.to_output("Error")
        
# ----------------------------------------------------------------------------------------------------
# Cross
#
# A vector peprpendicular to three independant vectors

def cross():
    
    with GeoNodes("Cross", is_group=True, fake_user=True, prefix=maths) as tree:
        
        # ----- Convert the three input vectors in a normal basis
        
        u0 = tree.vector_input("xyz 0", (1, 0, 0))
        w0 = tree.float_input( "w 0")
        u1 = tree.vector_input("xyz 1", (0, 1, 0))
        w1 = tree.float_input( "w 1")
        u2 = tree.vector_input("xyz 2", (0, 0, 1))
        w2 = tree.float_input( "w 2")

        node = maths.normal_basis()
        tree.input_node.plug_to(node)
        
        u0 = node.xyz_0
        w0 = node.w_0
        u1 = node.xyz_1
        w1 = node.w_1
        u2 = node.xyz_2
        w2 = node.w_2
        
        error = node.error
        
        # ----- Test the fourth basis vectors
        
        n3 = tree.float(0)
        u3 = tree.vector(0)
        w3 = tree.float(0)
        for i in range(4):
            
            with tree.layout(f"Axis {i}"):
                
                v4 = [0] * 4
                v4[i] = 1
                
                u = tree.vector(v4[:3])
                w = tree.float(v4[3])
                
                d0 = u0.dot(u) + w*w0
                d1 = u1.dot(u) + w*w1
                d2 = u2.dot(u) + w*w2
                u -= d0*u0
                w -= d0*w0
                u -= d1*u1
                w -= d1*w1
                u -= d2*u2
                w -= d2*w2
                
                # Resulting norm
                
                n = maths.length(xyz=u, w=w).length
                
                greater = n.greater_than(n3)
                u3 = u3.switch(greater, u)
                w3 = w3.switch(greater, w)
                n3 = n3.switch(greater, n)
            
        # ----- Let's normalize the result
        
        u3 /= n3
        w3 /= n3
        
        u3.to_output("xyz")
        w3.to_output("w")
        error.to_output("Error")
        
# ----------------------------------------------------------------------------------------------------
# Get two vectors forming a basis for a plane
#
# BUGGED

def plane_basis():
    
    with GeoNodes("Plane basis", is_group=True, fake_user=True, prefix=maths) as tree:
        
        u0 = tree.vector_input("xyz 0", (1, 0, 0))
        w0 = tree.float_input( "w 0")
        u1 = tree.vector_input("xyz 1", (0, 1, 0))
        w1 = tree.float_input( "w 1")
        
        # ----- Let's try (0, 0, 1, 0) as third vector to form an hyperplane

        basis0 = maths.normal_basis(
            xyz_0 = u0,
            w_0   = w0,
            xyz_1 = u1,
            w_1   = w1,
            xyz_2 = (0, 0, 1),
            w_2   = 0)
        
        # ----- Let's try (0, 0, 0, 1) as third vector to form an hyperplane

        basis1 = maths.normal_basis(
            xyz_0 = u0,
            w_0   = w0,
            xyz_1 = u1,
            w_1   = w1,
            xyz_2 = (0, 0, 0),
            w_2   = 1)
            
        # ----- Return basis0 or basis1 depending upon the error
        
        basis0.xyz_0.switch(basis0.error, basis1.xyz_0).to_output("xyz 0")
        basis0.w_0.switch(  basis0.error, basis1.w_0  ).to_output("w 0")
        basis0.xyz_1.switch(basis0.error, basis1.xyz_1).to_output("xyz 1")
        basis0.w_1.switch(  basis0.error, basis1.w_1  ).to_output("w 1")
        
# ----------------------------------------------------------------------------------------------------
# Get three vectors perpendicular to a vector

def hyperplane():
    
    with GeoNodes("Hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w", 1.)
        
        # ----- Normalize the entry
        
        node = maths.normalize(xyz=v, w=w)
        v    = node.xyz
        w    = node.w
        
        # ----- Try to build a 3D-base with v and plane (k, l)
        
        node = maths.normal_basis(
            xyz_0 = v,
            w_0   = w,
            xyz_1 = (0, 0, 1),
            w_1   = 0,
            xyz_2 = (0, 0, 0),
            w_2   = 1)
            
        u0 = node.xyz_1
        w0 = node.w_1
        u1 = node.xyz_2
        w1 = node.w_2
        
        error = node.error
        
        # ---------------------------------------------------------------------------
        # If error, it does mean that v is in plane (k, l), hence (i, j) is perp to v
        
        node = maths.cross(
            xyz_0 = v,
            w_0   = w,
            xyz_1 = (1, 0, 0),
            w_1   = 0,
            xyz_2 = (0, 1, 0),
            w_2   = 0,
            )
            
        e_u2 = node.xyz
        e_w2 = node.w
        
        # ---------------------------------------------------------------------------
        # If no error, we have (u0, u1) perp to input vector
        # The third basis vector is perpendicular to these 3 vectors
        
        node = maths.cross(
            xyz_0 = v,
            w_0   = w,
            xyz_1 = u0,
            w_1   = w0,
            xyz_2 = u1,
            w_2   = w1,
            )

        u0 = u0.switch(error, (1, 0, 0))
        w0 = w0.switch(error, 0)
        u1 = u1.switch(error, (0, 1, 0))
        w1 = w1.switch(error, 0)
        u2 = node.xyz.switch(error, e_u2)
        w2 = node.w.switch(error, e_w2)
        
        # ----- Done
        
        u0.to_output("xyz 0")
        w0.to_output("w 0")

        u1.to_output("xyz 1")
        w1.to_output("w 1")
            
        u2.to_output("xyz 2")
        w2.to_output("w 2")
        
        v.to_output("xyz 3")
        w.to_output("w 3")
        
        
# ----------------------------------------------------------------------------------------------------
# Resolution system de deux équations à deux inconnues
# a0x + b0y = c0
# a1x + b1y = c1
#
# D = a0b1 - a1b0
# x = (b1c0 - b0c1)/D
# y = (a0c1 - a1c0)/D

def two_equations_solver():
    with GeoNodes("Two equations solver", is_group=True, prefix=maths) as tree:
        
        a0 = tree.float_input("a0")
        b0 = tree.float_input("b0")
        c0 = tree.float_input("c0")

        a1 = tree.float_input("a1")
        b1 = tree.float_input("b1")
        c1 = tree.float_input("c1")
        
        with tree.layout("Discriminant"):
         D = a0*b1 - a1*b0
         
        with tree.layout("x"):
            x = (b1*c0 - b0*c1)/D 
            x.to_output("x")
            
        with tree.layout("y"):
            y = (a0*c1 - b1*c0)/D 
            y.to_output("y")
        
        tree.abs(D).less_than(0.001).to_output("Error")
        tree.vector((x, y, 0)).length().to_output("Length")
        
# ----------------------------------------------------------------------------------------------------
# Rotate to an hyperplane 

def rotate_to_hyperplane():
    
    with GeoNodes("Rotate to hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:

        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        hv = tree.vector_input("Hyper xyz")
        hw = tree.float_input("Hyper w", 1)
        
        node = maths.hyperplane(xyz=hv, w=hw)
        
        x = node.xyz_0.dot(v) + node.w_0*w
        y = node.xyz_1.dot(v) + node.w_1*w
        z = node.xyz_2.dot(v) + node.w_2*w
        w = node.xyz_3.dot(v) + node.w_3*w
        
        tree.vector((x, y, z)).to_output("xyz")
        w.to_output("w")
        
# ----------------------------------------------------------------------------------------------------
# Rotate from an hyperplane 

def rotate_from_hyperplane():
    
    with GeoNodes("Rotate from hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        hv = tree.vector_input("Hyper xyz")
        hw = tree.float_input("Hyper w", 1)
        
        node = maths.hyperplane(xyz=hv, w=hw)
        
        rv = node.xyz_0*v.x + node.xyz_1*v.y + node.xyz_2*v.z + node.xyz_3*w
        rw = node.w_0*v.x   + node.w_1*v.y   + node.w_2*v.z   + node.w_3*w

        rv.to_output("xyz")
        rw.to_output("w")
        
        
# ----------------------------------------------------------------------------------------------------
# Rotation 3D in an hyperplane

def rotate_in_hyperplane():
    
    with GeoNodes("Rotate in hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        hv = tree.vector_input("Hyper xyz")
        hw = tree.float_input("Hyper w", 1)

        #euler = gn.Vector.Rotation((0, 0, 0), "Euler")
        euler = tree.rotation_input("Euler")
        axis  = tree.vector_input(  "Axis", (0, 0, 1))
        angle = tree.angle_input(   "Angle")
        
        to_hp = maths.rotate_to_hyperplane(
            xyz       = v,
            w         = w,
            hyper_xyz = hv,
            hyper_w   = hw,
        )
        
        v = to_hp.xyz
        w = to_hp.w
        
        v = v.vector_rotate(rotation=euler, rotation_type='EULER_XYZ')
        v = v.vector_rotate(axis=axis, angle=angle, rotation_type='AXIS_ANGLE')
        
        from_hp = maths.rotate_from_hyperplane(
            xyz       = v,
            w         = w,
            hyper_xyz = hv,
            hyper_w   = hw,
        )
        
        from_hp.xyz.to_output("xyz")
        from_hp.w.to_output("w")
        
        
# ----------------------------------------------------------------------------------------------------
# Follow a vector
#
# Rotate a vector such as the vector a rotates to vector b

def follow_vector():
    
    with GeoNodes("Follow vector", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")

        va = tree.vector_input("A xyz")
        wa = tree.float_input( "A w", 1)
        vb = tree.vector_input("B xyz")
        wb = tree.float_input( "B w", 1)
        
        # ----- Create a normalized basis in the plane (a, b)
        
        with tree.layout("e0 = Basis first vector aligned on A"):
            
            node = maths.length(xyz=va, w=wa)

            xa   = node.length
            null = node.null

            e0 = va / xa
            t0 = wa / xa
            
        with tree.layout("e1 = Basis second vector: B - (B.e0).e0"):
            
            xb = e0.dot(vb) + t0*wb
            e1 = vb - e0*xb
            t1 = wb - t0*xb
            
            node = maths.length(xyz=e1, w=t1)
            yb   = node.length

            null = null + node.null
            e1 /= yb
            t1 /= yb
            
            # If vector are colinear, they can be opposite
            
            opposite = xb.less_than(0) 
            
        # ----- Compute the angle, cosine and sine
        
        with tree.layout("Compute the rotation cosine and sine"):
        
            ag = tree.arctan2(yb, xb)
            ag.node.node_label = "Rotation angle"
            ca = tree.cos(ag)
            sa = tree.sin(ag)
            
        # ----- Component of v on (e0, e1)
        
        with tree.layout("Components (xv, yv) on (e0, e1)"):
        
            xv = e0.dot(v) + t0*w
            yv = e1.dot(v) + t1*w
            
            xv.node.node_label = "xv"
            yv.node.node_label = "yv"
            
        # ----- Part out of the rotation plane
        
        with tree.layout("Part out of the rotation plane"):
            
            v3 = v - xv*e0 - yv*e1
            w3 = w - xv*t0 - yv*t1
            
        # ----- Rotate in the plane

        with tree.layout("Rotated coordinates"):
            
            fac0 = xv*ca - yv*sa
            fac1 = xv*sa + yv*ca
            
        # ----- Build the rotated vector

        with tree.layout("Build the resulting vector"):
            
            rv = v3 + fac0*e0 + fac1*e1
            rw = w3 + fac0*t0 + fac1*t1
            
        with tree.layout("No rotation if null"):
            
            #print(" V", v)
            #print("-V", -v)
            
            #print("SWITCH", v.switch(opposite, -v))
            #print("BEF", v)
            #v = v.switch(opposite, -v)
            #print("AFT", v)
            
            print("BEF", rv)
            rv = rv.switch(null, v.switch(opposite, -v))
            rw = rw.switch(null, w.switch(opposite, -w))
            print("AFT", rv)
            
        rv.to_output("xyz")
        rw.to_output("w")
        

# ----------------------------------------------------------------------------------------------------
# Rotation in a plane (x|y|z, w)
        
def w_plane_rotation():
    
    with GeoNodes("W plane rotation", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        axis  = tree.integer_input("Axis", 0, min_value=0, max_value=2)
        angle = tree.angle_input(  "Angle")
        
        # w is mapped on x
        # select y based on axis value
        
        with tree.layout("Axis on y component"):
            
            y = v.y.switch(axis.equal(0), v.x).switch(axis.equal(2), v.z)
            
        with tree.layout("Rotation around z"): 
        
            # rotation around z axis
            
            #r = gn.Vector((w, y, 0)).rotate_axis_angle(axis=(0, 0, 1), angle=angle)
            r = tree.vector((w, y, 0)).vector_rotate(axis=(0, 0, 1), angle=angle, rotation_type='AXIS_ANGLE')
            
        with tree.layout("y result on axis, x result on w"):
            
            # Returns the result
            
            tree.vector((v.x.switch(axis.equal(0), r.y),
                         v.y.switch(axis.equal(1), r.y),
                         v.z.switch(axis.equal(2), r.y)) ).to_output("xyz")
                       
            r.x.to_output("w")
            
# ----------------------------------------------------------------------------------------------------
# Utility Rotation in a plane defined by two 4D vectors
        
def rotation_2D():
    
    with GeoNodes("Rotation 2D", is_group=True, fake_user=True, prefix=maths) as tree:

        v  = tree.vector_input("xyz")
        w  = tree.float_input( "w")
        
        v0 = tree.vector_input("xyz 0")
        w0 = tree.float_input( "w 0", 1)
        v1 = tree.vector_input("xyz 1", (1, 0, 0))
        w1 = tree.float_input( "w 1")
        a  = tree.angle_input( "Angle", description="Rotation angle in plane (V0, V1)")
        
        with tree.layout("Normalize vector 0"):

            n = tree.sqrt(v0.x*v0.x + v0.y*v0.y + v0.z*v0.z + w0*w0)
            v0 = v0/n
            w0 = w0/n
            
        with tree.layout("Build second vector orthogonally"):
            
            d = v0.dot(v1) + w0*w1
            
            v1 = v1 - v0*d
            w1 = w1 - w0*d
            
        with tree.layout("Normalize second vector"):
            
            n = tree.sqrt(v1.x*v1.x + v1.y*v1.y + v1.z*v1.z + w1*w1)
            v1 = v1/n
            w1 = w1/n
            
        with tree.layout("Rotation V0 towards V1"):
            
            # ----- Components in plane (V0, V1)
            
            x = v0.dot(v) + w0*w
            y = v1.dot(v) + w1*w
            
            # ----- Rotation

            c = tree.cos(a) - 1
            s = tree.sin(a)

            # ----- Rotated components
            
            xp =  c*x - s*y
            yp =  s*x + c*y
            
            # ----- Resulting vector
            # V = V - P01 components + P01 rotated components
            
            rv = v + xp*v0 + yp*v1
            rw = w + xp*w0 + yp*w1
            
        rv.to_output("xyz")
        rw.to_output("w")
        
# ----------------------------------------------------------------------------------------------------
# Mesh along a curve
        
def build_along_curve():
    
    with GeoNodes("Build along curve", is_group=True, fake_user=True, prefix=maths) as tree:
        
        geo        = tree.geometry_input("Geometry 4D")
        curve      = tree.geometry_input("Curve 4D")
        align_v    = tree.vector_input(  "Align xyz", (0, 0, 1))
        align_w    = tree.float_input(   "Align w")
        use_radius = tree.bool_input(    "Use Radius", False)
        
        # Instantiate along the curve
        
        instances = curve.instance_on_points(instance=geo)
        
        # Instances 4D coordinates
        
        with tree.layout("Instances curve w coordinate"):
            
            w  = curve.POINT.sample_index_float(value=tree.named_float("w"))
            instances.INSTANCE.store_named_float("curve w", w)
            
            # ----- Scale with radius
            
            scale = tree.float(1).switch(use_radius, curve.POINT.sample_index_float(curve.radius))
            instances.scale_instances(scale=scale)
            
        with tree.layout("Store curve tangent and point location for further rotation"):
            
            instances.INSTANCE.store_named_vector("pivot xyz", instances.position)
            instances.INSTANCE.store_named_float( "pivot w", w)
            
            Txyz = curve.POINT.sample_index_vector(value=tree.named_vector("Txyz"))
            Tw   = curve.POINT.sample_index_float(value=tree.named_float("Tw"))

            instances.INSTANCE.store_named_vector("curve Txyz", Txyz)
            instances.INSTANCE.store_named_float( "curve Tw", Tw)
            
        # ----- Realize instances
            
        geo = instances.realize_instances()
        
        with tree.layout("Set the vertices in 4D space"):
            
            # ----- w coordinate
        
            geo.POINT.store_named_float("w", tree.named_float("w") + tree.named_float("curve w"))
            geo.remove_named_attribute("curve w")
            
            # ----- Rotation
            
            v = geo.position
            w = tree.named_float("w")
            
            pv = tree.named_vector("pivot xyz")
            pw = tree.named_float("pivot w")
            
            rv = tree.named_vector("curve Txyz")
            rw = tree.named_float("curve Tw")
            
            # ----- Points location
            
            with tree.layout("Points location"):
            
                node = maths.follow_vector(
                    xyz   = v - pv,
                    w     = w - pw,
                    a_xyz = align_v,
                    a_w   = align_w,
                    b_xyz = rv,
                    b_w   = rw,
                    )
                    
                geo.POINT.position = pv + node.xyz
                geo.POINT.store_named_float("w", pw + node.w)
                
            comps = geo.separate_components()
                
            mesh  = comps.mesh
            curve = comps.curve
            cloud = comps.point_cloud
            inst  = comps.instances
            
            # ----- Normals
            
            with tree.layout("Normals"):
            
                node = maths.follow_vector(
                    xyz   = tree.named_vector("Nxyz"),
                    w     = tree.named_float("Nw"),
                    a_xyz = align_v,
                    a_w   = align_w,
                    b_xyz = rv,
                    b_w   = rw,
                    )
                    
                mesh.POINT.store_named_vector("Nxyz", node.xyz)
                mesh.POINT.store_named_float( "Nw",   node.w)
                
            # ----- Curves tangents
            
            with tree.layout("Curves tangents"):
            
                node = maths.follow_vector(
                    xyz   = tree.named_vector("Txyz"),
                    w     = tree.named_float("Tw"),
                    a_xyz = align_v,
                    a_w   = align_w,
                    b_xyz = rv,
                    b_w   = rw,
                    )
                    
                curve.POINT.store_named_vector("Txyz", node.xyz)
                curve.POINT.store_named_float( "Tw",   node.w)
                
            # ----- Remove the named attributes
            
            geo.remove_named_attribute("pivot xyz")
            geo.remove_named_attribute("pivot w")
            geo.remove_named_attribute("curve Txyz")
            geo.remove_named_attribute("curve Tw")
        
        (mesh + curve + cloud + inst).to_output("Geometry")
       

# ====================================================================================================
# Main

if CLEAR:
    maths.clear()        
  
if REBUILD:
    projection_matrix()
    projection()
    length()
    normalize()
    normal_basis()
    cross()
    hyperplane()
    
    two_equations_solver()
    plane_basis()    

    rotate_to_hyperplane()
    rotate_from_hyperplane()
    rotate_in_hyperplane()
    follow_vector()
    
    w_plane_rotation()
    rotation_2D()
    
    build_along_curve()
```
    
        
    
    
    

        


        

