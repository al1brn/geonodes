from geonodes import Tree
from .gentestmodifiers import demo
from geonodes.demos import arrows, counters, curly, explosion, fields, fourd, gravity, helloworld, rain, relativity, shaders

def receipt(demos = True):
    print('='*100)
    print("GeoNodes Receipt")
    print('='*100)
    print()

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

    print()
    print("Receipt done")
    print()
