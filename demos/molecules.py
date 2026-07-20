"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demo molecules
-----------------------

Simulate molecules

updates
-------
- creation :   2026/07/17
"""

from geonodes import *
from geonodes.demos.shaders import atom_shader, arrow_shader, formula_shader



# ====================================================================================================
# Utilities
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Single value
# ----------------------------------------------------------------------------------------------------

def get_single_value(value, count=1):
    
    with Layout("Single Value"):
        values = []
        pts = Cloud.Points(count)
        captured = pts.points.capture_attribute(value)
        for i in range(count):
            values.append(pts.points.sample_index(captured, index=i))
        
    if count == 1:
        return values[0]
    else:
        return tuple(values)

# ----------------------------------------------------------------------------------------------------
# Create a ball
# ----------------------------------------------------------------------------------------------------

def get_ball(position, radius, color, material="Atom", show=1.0):
    
    with Layout("Sphere"):
        sphere = Mesh.UVSphere(radius=radius)
        sphere.offset = position
        sphere.faces.Color = color
        sphere.faces.material = material
        sphere.faces.Transparency = 1.0 - show
        sphere.faces.shade_smooth = True
        
        sphere.switch(show.equal(0.0))
        
    return sphere

# ----------------------------------------------------------------------------------------------------
# Create an arrow
# ----------------------------------------------------------------------------------------------------

def get_arrow(panel_name, position, vector=None, section=0.05, color="Black", show=0.0, use_scale=True):
    
    with Panel(panel_name, create_layout=True):
        Fshow = Float.Factor(show, "Show", 0, 1)
        if vector is None:
            vector = Vector((1, 0, 0), "Vector")
        Ccolor = Color(color, "Color") 
        Fsection = Float(section, "Section")
        
        if use_scale:
            scale = Float(1.0, "Scale")
        else:
            scale = 1.0
            
        size = Float(1.0, "Size")
        
        vector = vector.scale(scale)
        
        arrow = G().arrow(
            show = Fshow,
            position = position,
            color = Ccolor,
            vector = vector.scale(size),
            shaft_radius = Fsection*size,
            head = "Cone",
        )
        arrow.faces.Transparency = 1.0 - Fshow
        
        arrow.switch(Fshow.equal(0.0))
        
    return arrow, vector

# ----------------------------------------------------------------------------------------------------
# Vibration around a position
# ----------------------------------------------------------------------------------------------------

def get_vibration(position, scale, seed):
    
    with Layout("Vibration"):
        
        t = nd.scene_time().seconds
        h = t.hash_value(seed=seed)
        seed += 1
        scale /= 100
        scale_ = -scale
        deltas = Vector.Random((scale_, scale_, 0.0), (scale, scale, 0), seed=h)

        delta = get_single_value(deltas)
        
        return (position + delta)._lc("Vibration"), seed
    
# ====================================================================================================
# Nodes
# ====================================================================================================

def demo():

    # ====================================================================================================
    # Shaders
    # ====================================================================================================

    atom_shader()
    arrow_shader()
    formula_shader()

    # ====================================================================================================
    # Display Value
    # ====================================================================================================

    with GeoNodes("Value Display", is_group=True):
        
        show = Float.Factor(1.0, "Show", 0, 1)
        use_string = Boolean(False, "Use String")
        value = Float(0.0, "Value")
        decimals = Integer(2, "Decimals", 0, 5)
        string_value = String("", "String")
        size = Float(1.0, "Size")
        mat = Material("Formula", "Material")
        color = Color("Black", "Color")
        
        s = value.to_string(decimals=decimals)
        s.switch(use_string, string_value)

        try:
            curves = G().string_to_curves(
                s,
                size = size,
                align_x = Input("X Align"),
                align_y = Input("Y Align"),
            )
        except AttributeError:
            curves = s.to_curves(
                size = size,
                align_x = Input("X Align"),
                align_y = Input("Y Align"),
            )

        text = Curve(curves.realize()).fill()
            
        text.faces.material = mat
        text.faces.store_named_attribute("face_color", color)
        text.faces.Transparency = 1.0 - show

        rot = Rotation.MenuSwitch({
                'XY' : (0.0, 0.0, 0.0),
                'XZ' : (pi/2, 0.0, 0.0),
                'YZ' : (pi/2, 0.0, pi/2),
            }, menu=Input("Plane"),
        )
        text.transform(rotation=rot)
        
        text.out()

    # ====================================================================================================
    # A vibrating atom
    # ====================================================================================================

    with GeoNodes("Atom"):
        
        show = Float.Factor(1.0, "Show", 0, 1)
        position = Vector(name="Position")
        
        element = Integer.MenuSwitch({
            "Free"      : 0,
            "Hydrogen"  : 1,
            "Oxygen"    : 2,
            "Carbon"    : 3,
            },
            menu = Input("Element"),
            )
        
        radius = Float(0.1, "Radius")
        scale = Float(1.0, "Scale")
        vibration = Float(0.0, "Vibration")
        color = Color(name="Color")
        seed = Integer(0, "Seed")
        
        with Float.IndexSwitch(index=element) as element_radius:
            radius.out()
            Float(0.1).out()
            Float(0.3).out()
            Float(0.4).out()
            
        element_radius *= scale
            
        with Color.IndexSwitch(index=element) as element_color:
            color.out()
            Color("Blue").out()
            Color("Orange").out()
            Color("Purple").out()
        
        pos, seed = get_vibration(position, vibration, seed)
        
        sphere = get_ball(pos, radius=element_radius, color=element_color, show=show)
        
        sphere.out("Mesh")
        element_radius.out("Radius")
        seed.out("Seed")
        
    # ====================================================================================================
    # A molecule
    # ====================================================================================================
        
    with GeoNodes("Molecule"):
        
        show = Float.Factor(1.0, "Show", 0, 1)
        molecule = Mesh.MenuSwitch(menu=Input("Molecule"))
        position = Vector(name="Position")
        scale = Float(1.0, "Scale")
        vibration = Float(0.0, "Vibration")
        omega = Float(0.0, "Omega")    
        seed = Integer(0, "Seed")
        
        with Layout("Orientation"):
            t = nd.scene_time().seconds
            t *= omega
            t += Float.Random(0, tau, seed=seed)
            seed += 1
            
            rotation = get_single_value(Vector.Random(0, omega, seed=seed).scale(t))
            seed += 1
        
        with Layout("Build the atoms"):
            
            O = []
            for i in range(2):
                atom = G().atom(
                    show = show,
                    element = "Oxygen",
                    scale = scale,
                    vibration = vibration,
                    seed = seed,
                    )
                seed = atom.seed
                O.append(atom)
                if i == 0:
                    O_radius = atom.radius
                    
            H = []
            for i in range(4):
                atom = G().atom(
                    show = show,
                    element = "Hydrogen",
                    scale = scale,
                    vibration = vibration,
                    seed = seed,
                    )
                seed = atom.seed
                H.append(atom)
                if i == 0:
                    H_radius = atom.radius
                    
            C = []
            for i in range(1):
                atom = G().atom(
                    show = show,
                    scale = scale,
                    element = "Carbon",
                    vibration = vibration,
                    seed = seed,
                    )
                seed = atom.seed
                C.append(atom)
                if i == 0:
                    C_radius = atom.radius

        # ---------------------------------------------------------------------------
        # H2O
        # ---------------------------------------------------------------------------
        
        with molecule:
            
            r = O_radius*1.1
            
            H2O = Mesh(O[0])
            
            a = Mesh(H[0])
            a.offset =  (0, 0, r),
            H2O += a
            
            a = Mesh(H[1])
            a.offset =  (0, r*0.866, -r*0.5),
            H2O += a
            
            H2O.out("H2O")
            
        # ---------------------------------------------------------------------------
        # CO2
        # ---------------------------------------------------------------------------
        
        with molecule:
            
            r = C_radius*0.9
            
            CO2 = Mesh(C[0])
            
            a = Mesh(O[0])
            a.offset =  (0, 0, r),
            CO2 += a
            
            a = Mesh(O[1])
            a.offset =  (0, 0, -r),
            CO2 += a
            
            CO2.out("CO2")
            
        # ---------------------------------------------------------------------------
        # O2
        # ---------------------------------------------------------------------------
        
        with molecule:
            
            r = O_radius*0.4
            
            O2 = Mesh(O[0])
            O2.offset = (-r, 0, 0)
            
            a = Mesh(O[1])
            a.offset = (r, 0, 0)
            O2 += a
            
            O2.out("O2")
            
            
        # ---------------------------------------------------------------------------
        # H2
        # ---------------------------------------------------------------------------
        
        with molecule:
            
            delta = H_radius*0.4
            H2 = Mesh(H[0])
            H2.offset = (-delta, 0, 0)
            
            a = Mesh(H[1])
            a.offset = (delta, 0, 0)
            H2 += a
            
            H2.out("H2")
            
        # ---------------------------------------------------------------------------
        # CH4
        # ---------------------------------------------------------------------------
        
        with molecule:
            
            r = C_radius*1.05
            
            CH4 = Mesh(C[0])
            
            a = Mesh(H[0])
            a.offset = (0, 0, r)
            CH4 += a
            
            a = Mesh(H[1])
            a.offset = (r*0.866, 0, -r*0.5)
            CH4 += a
            
            a = Mesh(H[2])
            a.offset = (r*(-0.5*0.866), r*(0.866*0.866), -r*0.5)
            CH4 += a
            
            a = Mesh(H[3])
            a.offset = (r*(-0.5*0.866), r*(-0.866*0.866), -r*0.5)
            CH4 += a
            
            CH4.out("CH4")
            
        molecule.transform(translation=position, rotation=rotation)
        
        molecule.out()
        seed.out("Seed")
        
    # ====================================================================================================
    # Add Dynamic
    # ====================================================================================================

    with GeoNodes("Add Dynamic"):
        
        geo = Geometry()
        position = Vector(name="At Position")
        mass = Float(1.0, "Mass")
        
        speed_arrow, speed = get_arrow("Speed", position=position, color="Green")
        acc_arrow, acc = get_arrow("Acceleration", position=position, color="Red")
        
        with Panel("Kinetic Energy"):
            T_show = Float.Factor(0.0, "Show", 0, 1)
            T_use_speed = Boolean(True, "Compute")
            T_value = Float(1.0, "Value")
            T_size = Float(1.0, "Size")
            T_pos = Vector((0, 0, 0.3), "Position")
            T_col = Color("Red", "Color")
        
        with Layout("Acceleration components"):
            speed_dir = speed.normalize()
            tg_acc = speed_dir.scale(acc.dot(speed_dir))
            rad_acc = acc - tg_acc
            
            tg_arrow, _ = get_arrow("Tangent Acceleration", section=0.07, position=position, vector=tg_acc, color="#BC8441FF", use_scale=False)
            rad_arrow, _ = get_arrow("Radial Acceleration", section=0.07, position=position, vector=rad_acc, color="#5952BCFF", use_scale=False)
            
        with Layout("Kinetic Energy"):
            T_value.switch(T_use_speed, (speed.length()**2)*(mass/2))
            T_label = G().value_display(
                show = T_show,
                value = T_value,
                decimals = 0,
                size = T_size,
                color = T_col,
            )
            T_label.offset = T_pos
            T_label.switch(T_show.equal(0.0))
            
        geo += speed_arrow, acc_arrow, tg_arrow, rad_arrow, T_label
        geo.out()
        
