from ..shadernodes import *

def demo():

    # ====================================================================================================
    # Default Shader for Arrow

    with ShaderNodes("Arrow"):

        pos_color = Color(nd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        negative  = nd.attribute(attribute_type='GEOMETRY', attribute_name="Negative").fac
        transp    = nd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

        neg_color = pos_color.hue_saturation_value(hue=.5, saturation=.9, value=.9)
        color = pos_color.mix(negative, neg_color)

        ped = Shader.Principled(
            base_color = color,
            roughness  = negative.map_range(to_min=.1, to_max=.9),
        )

        shader = ped.mix(transp, Shader.Transparent())

        shader.out()
