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

module : demo shaders
---------------------

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/02/01 # Wood and planks

$ DOC START

[Source Code](../demos/shaders.py)

WORK IN PROGRESS

"""

from geonodes import *

# ====================================================================================================
# Attribute-based coloration
# ====================================================================================================

def coloration_group(rebuild=False):
    """Expose the geometry attributes Color and Transparency."""

    with ShaderNodes("Coloration", is_group=True, rebuild=rebuild):
        Color(snd.attribute(
            attribute_type='GEOMETRY', attribute_name="Color",
        ).vector).out("Color")
        snd.attribute(
            attribute_type='GEOMETRY', attribute_name="Transparency",
        ).factor.out("Transparency")


def colored_shaders(rebuild=False):
    """Create shiny, satin and matte materials using the Coloration group."""

    coloration_group(rebuild=rebuild)

    for name, roughness in (("Colored Shiny", 0.0), ("Colored", 0.5), ("Colored Mat", 1.0)):
        with ShaderNodes(name, replace_material=rebuild):
            coloration = G().coloration()
            shader = Shader.Principled(
                base_color=coloration,
                roughness=roughness,
            )
            shader.mix(
                shader=Shader.Transparent(), factor=coloration.transparency_,
            ).out()


# ====================================================================================================
# Default Shader for Arrow
# ====================================================================================================

def arrow_shader(rebuild=False):

    with ShaderNodes("Arrow", replace_material=rebuild):

        pos_color = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        negative  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Negative").factor
        transp    = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        neg_color = pos_color.hue_saturation_value(hue=.5, saturation=.9, value=.9)
        color = pos_color.mix(negative, neg_color)

        ped = Shader.Principled(
            base_color = color,
            roughness  = negative.map_range(to_min=.1, to_max=.9),
        )

        shader = ped.mix(shader=Shader.Transparent(), factor=transp)

        shader.out()

# ====================================================================================================
# Default Shader for Atoms
# ====================================================================================================

def atom_shader(rebuild=False):

    with ShaderNodes("Atom", replace_material=rebuild):

        color = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        transp    = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        ped = Shader.Principled(
            base_color = color,
            roughness  = 0.1,
        )

        shader = ped.mix(shader=Shader.Transparent(), factor=transp)

        shader.out() 

# ====================================================================================================
# Default Shader for Formulas
# ====================================================================================================

def formula_shader(rebuild=False):

    with ShaderNodes("Formula", replace_material=rebuild):

        color  = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="face_color").vector)
        transp = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        ped = Shader.Principled(
            base_color = color,
            roughness  = 1.0,
        )
        shader = ped.mix(shader=Shader.Transparent(), factor=transp)

        shader.out()        


# ====================================================================================================
# Glass
# ====================================================================================================

def glass_shader(color=(1.0, 1.0, 1.0, 1.0), roughness=0.0, ior=1.45,
                 rebuild=False):
    """Create Glass using the geometry float attribute 'IOR' for refraction.

    A zero or missing attribute falls back to ior (1.45 by default).
    """

    with ShaderNodes("Glass", replace_material=rebuild):

        geometry_ior = snd.attribute(
            attribute_type='GEOMETRY', attribute_name="IOR",
        ).factor
        effective_ior = geometry_ior + geometry_ior.equal(0.0, epsilon=0.0) * ior

        transp_fac = snd.attribute(
            attribute_type='GEOMETRY', attribute_name="Transparency",
        ).factor

        glass = Shader.Glass(
            color=color,
            roughness=roughness,
            ior=effective_ior,
        )
        transp = Shader.Transparent()

        glass.mix(transp, factor=transp_fac).out()


# ====================================================================================================
# Chrome
# ====================================================================================================

def chrome_shader(color=(0.55, 0.55, 0.55, 1.0), roughness=0.08, rebuild=False):
    """Create the Chrome material with adjustable tint and roughness."""

    with ShaderNodes("Chrome", replace_material=rebuild):

        Shader.Principled(
            base_color=color,
            metallic=1.0,
            roughness=roughness,
        ).out()


# ====================================================================================================
# Wood Handle
# ====================================================================================================

def wood_handle_shader(color1="#301407", color2="#965025", roughness=0.22,
                       coat_roughness=0.08, rotation=(0, 0, 0), rebuild=False):
    """Create varnished brown wood with fine grain along the local Z axis.

    Rotation (Euler angles in radians) adjusts the grain direction.
    Generated coordinates keep the grain independent of object dimensions.
    """

    with ShaderNodes("Wood Handle", replace_material=rebuild):

        with Layout("Wood Grain"):
            coord = snd.texture_coordinate().generated
            coord = snd.mapping(vector=coord, rotation=rotation)
            coord = snd.mapping(vector=coord, scale=(6, 6, 0.35))

            grain = Texture.Noise(
                vector=coord, scale=5, detail=3, roughness=0.65,
                distortion=0.3,
            )
            fine_grain = Texture.Noise(
                vector=coord, scale=35, detail=2, roughness=0.5,
            )
            factor = (grain.factor * 0.85 + fine_grain.factor * 0.15)
            factor = factor.map_range(
                from_min=0.25, from_max=0.75,
                interpolation_type="SMOOTHSTEP",
            )
            color = Color(color1).mix(Color(color2), factor=factor)

        with Layout("Polished Wood"):
            normal = snd.bump(
                strength=0.12, distance=0.015, height=fine_grain.factor,
            )
            Shader.Principled(
                base_color=color,
                roughness=roughness,
                normal=normal,
                coat_weight=1.0,
                coat_roughness=coat_roughness,
                coat_ior=1.5,
            ).out()


def demo(rebuild=False):

    colored_shaders(rebuild=rebuild)
    arrow_shader(rebuild=rebuild)
    atom_shader(rebuild=rebuild)
    glass_shader(rebuild=rebuild)
    chrome_shader(rebuild=rebuild)
    wood_handle_shader(rebuild=rebuild)


    # ====================================================================================================
    # Planks

    with ShaderNodes("Planks Splitter", is_group=True, rebuild=rebuild):

        vector = Vector(None, "Vector")

        with Panel("Planks"):
            scale      = Float(.6, "Scale")
            length     = Float(1, "Length")
            width      = Float(.2, "Width")
            gap        = Float(.002, "Gap")
            gap_smooth = Float.Factor(.73, "Gap Smooth", 0, 1)

        bricks = Texture.Brick(vector=vector, color1=.05, color2=1, mortar=0, bias=0,
                scale=scale, mortar_size=gap, mortar_smooth=gap_smooth, brick_width=length, row_height=width)

        bricks_offset = Texture.Brick(vector=vector, color1=.05, color2=1, mortar=0, bias=0,
                scale=scale, mortar_size=0, mortar_smooth=0, brick_width=length, row_height=width)

        is_mortar = bricks.value.mless_than(.01)
        offset = Vector(bricks_offset).scale(10)

        is_mortar.out("Mortar")
        (vector + offset).out("Vector")
        bricks.out("Color")
        offset.out("Offset")


    # ====================================================================================================
    # Wood base

    with ShaderNodes("Wood Group", is_group=True, rebuild=rebuild):

        vector = Vector(None, "Vector")

        with Panel("Colors"):
            col1 = Color("#181007FF", "Color 1")
            col2 = Color("#BD8B35FF", "Color 2")
            col1_fac = Float.Factor(.32, "Factor 1", 0, .5)
            col2_fac = Float.Factor(.45, "Factor 2", 0, .5)
            detail   = Float(5, "Detail", 0)

        with Panel("Coordinates"):
            scale      = Float(1.5, "Scale")
            stretch    = Float.Factor(.25, "Stretch", 0, 10)
            dist       = Float(2, "Distorsion")
            rot        = Float.Angle(0, "Rotation")

        with Panel("Appearance"):
            rough1 = Float.Factor(.23, "Roughness Min", 0, 1)
            rough2 = Float.Factor(.72, "Roughness Max", 0, 1)
            bump_fac = Float.Factor(.17, "Bump", 0, 1)
            bump_inv = Boolean(True, "Invert Bump")

        with Layout("Base"):
            sx = stretch
            sy = 1/stretch

            coord = snd.mapping(vector=vector, rotation=(0, 0, rot), scale=(sx, sy, sy))

            noise1 = Texture.Noise(vector=coord, scale=scale, detail=detail, distortion=dist)
            noise2 = Texture.Noise(vector=noise1, scale=3, detail=11, roughness=.7, lacunarity=2, distortion=0)

        with Layout("Color"):
            fac = noise2.map_range_linear(col1_fac, 1 - col2_fac)
            col = col1.mix(col2, factor=fac)

        with Layout("Roughness"):
            roughness = noise2.map_range_linear(to_min=rough1, to_max=rough2)

        with Layout("Bump"):
            bump = snd.bump(strength=bump_fac, height=noise2)
            bumpi = snd.bump(strength=bump_fac, height=noise2, invert=True)

            bump = bump.mix(bumpi, factor=bump_inv)

        ped = Shader.Principled(
            base_color = col,
            roughness  = roughness,
            normal     = bump,
            )

        ped.out()

    # ====================================================================================================
    # Planks

    with ShaderNodes("Wood Planks Group", is_group=True, rebuild=rebuild):

        splitter = G().planks_splitter().link_inputs()

        wood = G().wood_group(vector=splitter.vector_).link_inputs()

        m_color = Color("#2E150AFF", "Gap Color", panel="Colors")

        mortar = Shader.Principled(
            base_color = m_color,
            normal = snd.bump(strength=1, height=is_mortar, invert=True),
            )

        shader = wood.mix(mortar, factor=splitter)

        shader.out()

    # ====================================================================================================
    # Wood

    with ShaderNodes("Wood", replace_material=rebuild):

        coord = snd.texture_coordinate().object

        G().wood_group(vector=coord).out()

    with ShaderNodes("Wood Planks", replace_material=rebuild):

        coord = snd.texture_coordinate().object

        G().wood_planks_group(vector=coord).out()


    # ====================================================================================================
    # Basket Ball
    # ====================================================================================================

    with ShaderNodes("Basket Ball", replace_material=rebuild):
        
        
        with Layout("UV Map"):
            uv = snd.uv_map(uv_map="UVMap").uv
            
            u, v, _ = uv.xyz
            lat = gnmath.cos((v - 0.5)*pi)
            
        with Layout("Skin"):
            size = 500
            
            fac = gnmath.sin(u*size)*gnmath.sin(v*size)
            fac = fac.map_range(.1, .9, interpolation_type="Smooth Step")
            
            orange1 = Color("#D65F0EFF") #D65F0EFF
            orange2 = Color("#7B381CFF")

            color = orange2.mix(orange1, factor=fac)
            
        with Layout("Black Lines"):

            black_color = Color("Black")

            line_width = 0.003
            softness = 0.5

            lat_safe = lat.max(0.01)
            outer_width = line_width / lat_safe
            inner_width = outer_width * (1 - softness)

            def meridian(center):

                delta = abs(u - center)

                # Distance circulaire dans l'intervalle UV [0, 1].
                # Par exemple, 0.99 est à une distance 0.01 de 0.
                distance = delta.min(1.0 - delta)

                return distance.map_range(
                    from_min=inner_width,
                    from_max=outer_width,
                    to_min=1.0,
                    to_max=0.0,
                    interpolation_type="SMOOTHSTEP",
                )

            black = meridian(0.00)
            black = black.max(meridian(0.25))
            black = black.max(meridian(0.50))
            black = black.max(meridian(0.75))
        
        with Layout("Ellipses"):

            line_width = 0.003
            softness = 0.5

            def ellipse(center_u):

                radius = 0.125
                half_height = 0.40
                roundness = 3 #2.7

                du = abs(u - center_u)
                du = du.min(1.0 - du)

                du_normalized = du / radius
                dv_normalized = abs(v - 0.5) / half_height

                distance = radius * (
                    du_normalized**roundness
                    + dv_normalized**roundness
                ) ** (1.0 / roundness)

                outline_distance = abs(distance - radius)

                inner_width = line_width * (1.0 - softness)
                outer_width = line_width

                return outline_distance.map_range(
                    from_min=inner_width,
                    from_max=outer_width,
                    to_min=1.0,
                    to_max=0.0,
                    interpolation_type="SMOOTHERSTEP",
                )

            ellipse_1 = ellipse(0.0)
            ellipse_2 = ellipse(0.5)

            black = black.max(ellipse_1)
            black = black.max(ellipse_2)
            
        with Layout("BSDF"):
            color = color.mix(
                black_color,
                factor=black,
            ) 

            
            ped = Shader.Principled(
                base_color = color,
            )
            
            ped.out()
            

        with Layout("Displacement"):

            # Relief des points orange
            skin_height = 0.0015

            # Profondeur des rainures noires
            groove_depth = 0.01

            # Les points orange ressortent.
            # (1 - black) évite d’ajouter des bosses dans les rainures.
            skin_displacement = fac * (1.0 - black) * skin_height

            # Les lignes noires sont creusées.
            groove_displacement = black * groove_depth

            height = skin_displacement - groove_displacement

            disp = snd.displacement(
                height=height,
                midlevel=0.0,
                scale=1.0,
            )

            disp.out()        
            
            
