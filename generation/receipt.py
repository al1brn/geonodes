import inspect

from geonodes import Tree
from .gentestmodifiers import demo
from geonodes.demos import arrows, counters, curly, explosion, fields, fourd, gravity, helloworld, rain, relativity, shaders
from geonodes.demos import forest, gizmo

from geonodes import *

# =============================================================================================================================
# Test the static nodes

def test_statics():
    print('-'*60)
    print("Test static classes")
    print()

    print("Shader...")
    snd._receipt_shader()
    print("Modifier...")
    nd._receipt_modifier()
    print("Tool...")
    nd._receipt_tool()

    print("Done")
    print()


def run_tests():

    String._run_tests()
    #Menu._run_tests()
    Material._run_tests()
    Image._run_tests()
    Object._run_tests()
    Collection._run_tests()

    Boolean._run_tests()
    Color._run_tests()
    Integer._run_tests()
    Float._run_tests()
    Texture._run_tests()
    Vector._run_tests()
    Rotation._run_tests()
    Matrix._run_tests()

    Geometry._run_tests()
    Mesh._run_tests()
    Curve._run_tests()
    Cloud._run_tests()
    Instances._run_tests()
    Volume._run_tests()

#from .geonodes.geometryclass import Domain, Vertex, Edge, Face, Corner, SplinePoint, Spline, CloudPoint, Instance


# ----------------------------------------------------------------------------------------------------
# Shader

#from .shadernodes.shadernodes import ShaderNodes, snd
#from .shadernodes.shaderclass import Shader, VolumeShader


def receipt(demos = True):
    print('='*100)
    print("GeoNodes Receipt")
    print('='*100)
    print()

    test_statics()

    print("Base receipt...")
    Tree._reset_counters()
    print("All nodes receipts")
    demo()
    print()
    print(f"Base receipt done : {Tree._total_nodes} nodes, {Tree._total_links} links")
    print()

    if demos:
        print("="*100)
        print("Demos...")
        print()

        arrows.demo()
        counters.demo()
        curly.demo()
        explosion.demo()
        fields.demo()
        fourd.demo()
        gravity.demo()
        helloworld.demo()
        rain.demo()
        relativity.demo()
        shaders.demo()
        forest.demo()
        gizmo.demo()

    print()
    print("Receipt done")
    print()
