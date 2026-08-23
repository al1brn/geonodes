from geonodes import *


def demo():

    with ShaderNodes("Golf Ball", replace_material=False):

        # -------------------------------------------------------------------------
        # Coordonnées objet

        with Layout("Coordinates"):

            coord = snd.texture_coordinate().object

        # -------------------------------------------------------------------------
        # Microtexture du revêtement

        with Layout("Surface Texture"):

            grain = Texture.Noise(
                vector=coord,
                scale=180.0,
                detail=3.0,
                roughness=0.65,
                lacunarity=2.0,
                distortion=0.05,
            )

            micro_grain = Texture.Noise(
                vector=coord,
                scale=650.0,
                detail=2.0,
                roughness=0.5,
                lacunarity=2.0,
                distortion=0.0,
            )

            surface_height = grain * 0.7 + micro_grain * 0.3

        # -------------------------------------------------------------------------
        # Couleur blanche légèrement irrégulière

        with Layout("Color"):

            white = Color("#F4F4F0FF")
            off_white = Color("#D8D9D5FF")

            color_factor = grain.map_range(
                from_min=0.25,
                from_max=0.75,
                to_min=0.0,
                to_max=1.0,
                clamp=True,
                interpolation_type="SMOOTHSTEP",
            )

            base_color = off_white.mix(
                white,
                factor=color_factor,
            )

        # -------------------------------------------------------------------------
        # Rugosité

        with Layout("Roughness"):

            roughness = grain.map_range(
                from_min=0.2,
                from_max=0.8,
                to_min=0.32,
                to_max=0.46,
                clamp=True,
                interpolation_type="SMOOTHSTEP",
            )

        # -------------------------------------------------------------------------
        # Microrelief

        with Layout("Micro Bump"):

            normal = snd.bump(
                height=surface_height,
                strength=0.16,
                distance=0.0025,
            )

        # -------------------------------------------------------------------------
        # BSDF

        with Layout("BSDF"):

            shader = Shader.Principled(
                base_color=base_color,
                roughness=roughness,
                normal=normal,
            )

            shader.out()    


    with GeoNodes("Golf Ball"):

        radius = 1.0

        # -------------------------------------------------------------------------
        # Centres des alvéoles

        with Layout("Dimple Centers"):

            centers_mesh = Mesh.IcoSphere(
                radius=radius,
                subdivisions=4,
            )

            centers = centers_mesh.points.to_points()

        # -------------------------------------------------------------------------
        # Surface dense

        with Layout("Dense Surface"):

            ball = Mesh.IcoSphere(
                radius=radius,
                subdivisions=7,
            )

        # -------------------------------------------------------------------------
        # Distance au centre d’alvéole le plus proche

        with Layout("Dimple Distance"):

            proximity = centers.proximity_points(
                sample_position=nd.position,
            )

            distance = proximity.distance_

        # -------------------------------------------------------------------------
        # Profil des alvéoles

        with Layout("Dimple Profile"):

            dimple_radius = 0.1#0.055
            dimple_depth = 0.012

            # Profil compris entre 1 au centre et 0 au bord.
            profile = distance.map_range(
                from_min=0.0,
                from_max=dimple_radius,
                to_min=1.0,
                to_max=0.0,
                clamp=True,
                interpolation_type="SMOOTHERSTEP",
            )

        # -------------------------------------------------------------------------
        # Creusement radial

        with Layout("Displacement"):

            radial_normal = nd.position.normalize()

            offset = radial_normal.scale(
                -dimple_depth * profile
            )

            ball.points.position += offset

        # -------------------------------------------------------------------------
        # Lissage

        ball.faces.smooth = True
        ball.faces.material = "Golf Ball"
        ball.out()
        


