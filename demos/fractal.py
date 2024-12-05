from random import Random
from geonodes import *

# =============================================================================================================================
# Split segments

def split_segments():

    with GeoNodes("Split Segments"):

        sides       = Integer(3, "Sides", min=3, max=10)
        iterations  = Integer(5, "Iterations", min=0, max=10)
        external    = Boolean(True, "External")
        noise_scale = Float(0, "Noise Scale")
        seed        = Integer(0, "Seed")

        triangle = Mesh.Circle(vertices=sides)
        angle = Float(pi/3).switch(external, -pi/3)

        with Repeat(triangle=triangle, seed=seed, iterations=iterations) as rep:

            rep.seed = rep.seed.hash_value(rep.iteration)

            node = nd.edge_vertices
            with rep.triangle.edges.for_each(p1=node.position_1, p2=node.position_2) as feel:

                new_edges = Mesh.Line(start_location=feel.p1, end_location=feel.p2, count=5)
                v = (feel.p2 - feel.p1)/3

                ns = noise_scale * v.length
                noise_vector = Vector((ns, ns, 0))

                new_edges.points[1].position = feel.p1 + v + Float.Random(-noise_vector, noise_vector, rep.seed)
                new_edges.points[3].position = feel.p2 - v  + Float.Random(-noise_vector, noise_vector, rep.seed + 1)

                w = Rotation((0, 0, angle)) @ v
                new_edges.points[2].position = feel.p1 + v + w  + Float.Random(-noise_vector, noise_vector, rep.seed + 2)

                feel.generated.geometry = new_edges

            rep.triangle = feel.generated.geometry

        rep.triangle.out()

# =============================================================================================================================
# Sierpinski triangle

def sierpinski():

    with GeoNodes("Sierpinski"):

        iterations  = Integer(5, "Iterations", min=0, max=10)
        rotation    = Float.Factor(0, "Rotation", min=-1, max=1)
        noise_scale = Float(0, "Noise Scale")
        seed        = Integer(0, "Seed")

        triangle = Mesh.Circle(vertices=3, fill_type='NGON')

        with Repeat(triangle=triangle, seed=seed, iterations=iterations) as rep:

            rep.seed = rep.seed.hash_value(rep.iteration)

            i0 = nd.offset_corner_in_face(nd.corners_of_face().corner_index, offset=0)
            i1 = nd.offset_corner_in_face(nd.corners_of_face().corner_index, offset=1)
            i2 = nd.offset_corner_in_face(nd.corners_of_face().corner_index, offset=2)

            p0 = rep.triangle.points.sample_index(nd.position, nd.vertex_of_corner(i0))
            p1 = rep.triangle.points.sample_index(nd.position, nd.vertex_of_corner(i1))
            p2 = rep.triangle.points.sample_index(nd.position, nd.vertex_of_corner(i2))

            with rep.triangle.faces.for_each(p0=p0, p1=p1, p2=p2, seed=rep.seed) as feel:

                sn = (p1 - p0).length*noise_scale
                nv1 = Vector((sn, sn, 0))
                nv0 = -nv1

                #p0 = feel.p0 + Vector.Random(nv0, nv1, feel.seed)
                #p1 = feel.p1 + Vector.Random(nv0, nv1, feel.seed + 1)
                #p2 = feel.p2 + Vector.Random(nv0, nv1, feel.seed + 2)

                p0, p1, p2 = feel.p0, feel.p1, feel.p2

                f = .5 + rotation/2
                f_ = 1 - f

                q0 = (f*p0 + f_*p1)._lc("q0")
                q1 = (f*p1 + f_*p2)._lc("q1")
                q2 = (f*p2 + f_*p0)._lc("q2")

                q0 += Vector.Random(nv0, nv1, feel.seed)
                q1 += Vector.Random(nv0, nv1, feel.seed + 1)
                q2 += Vector.Random(nv0, nv1, feel.seed + 2)

                tri0 = Mesh.Circle(vertices=3, fill_type='NGON')
                tri0.points[0].position = p0
                tri0.points[1].position = q0
                tri0.points[2].position = q2

                tri1 = Mesh(tri0)
                tri1.points[0].position = q0
                tri1.points[1].position = p1
                tri1.points[2].position = q1

                tri2 = Mesh(tri0)
                tri2.points[0].position = q1
                tri2.points[1].position = p2
                tri2.points[2].position = q2


                feel.generated.geometry = tri0.join(tri1, tri2)


            rep.triangle = feel.generated.geometry


        rep.triangle.out()

# =============================================================================================================================
# Fern

def fern():

    with GeoNodes("Fern"):

        iterations   = Integer(5, "Iterations", min=0, max=10)
        angle        = Float.Angle(pi/20, "Grow Angle")
        grow_factor  = Float.Factor(.9, "Grow Factor", min=.01, max=.99)
        sub_angle    = Float.Angle(pi/5, "Sub Angle")
        sub_factor   = Float.Factor(.3, "Sub Factor", min=.01, max=.99)
        angle_noise  = Float(0, "Angle Noise")
        factor_noise = Float(0, "Factor Noise")
        seed         = Integer(0, "Seed")

        leaf = Mesh.Line(start_location=0, end_location=(1, 0, 0), count=2)
        leaf.edges.store("Use", True)

        with Repeat(leaf=leaf, seed=seed, iterations=iterations) as rep:

            rep.seed = rep.seed.hash_value(rep.iteration)

            node = nd.edge_vertices
            with rep.leaf.edges.for_each(p1=node.position_1, p2=node.position_2, seed=rep.seed) as feel:

                hv = rep.seed.hash_value(feel.index)

                v = feel.p2 - feel.p1
                l = v.length

                edge = Mesh(feel.element)
                extrude = edge.edges.sample_index(Boolean.Named("Use"), 0)

                loop_angle  = angle       + Float.Random(-angle*angle_noise, angle*angle_noise, hv)
                loop_ag     = sub_angle   + Float.Random(-sub_angle*angle_noise, sub_angle*angle_noise, hv + 1)
                loop_factor = grow_factor + Float.Random(-factor_noise, factor_noise, hv + 2)
                loop_fac    = sub_factor  + Float.Random(-factor_noise, factor_noise, hv + 3)

                edge.points[1].extrude(Rotation((0, 0, loop_angle)) @ (v*loop_factor))
                edge.points[1].extrude(Rotation((0, 0, -loop_angle - loop_ag)) @ (v*loop_fac))
                edge.points[1].extrude(Rotation((0, 0,  loop_angle + loop_ag)) @ (v*loop_fac))

                edge.edges.store("Use", True)
                edge.edges[0].store("Use", False)
                feel.generated.geometry  = feel.element.switch(extrude, edge)

            leaf = feel.generated.geometry #.merge_by_distance()
            rep.leaf = leaf

        rep.leaf.out()











def demo():

    # ----- Growing Mesh

    with GeoNodes("Branch"):

        iterations = Integer(10, "Iterations", min=2, max=10)
        extr_scale = Float.Factor(.3, "Extrude Scale", min=.1, max=2)
        branches   = Integer(2, "Branches", min=2, max=6)

        seed       = Integer(0, "Seed")

        line = Mesh.Line(end_location=(0, 0, 1), count=2)

        with Repeat(tree=line, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.tree.edges.for_each() as feel:

                edge = Mesh(feel.element)

                with Layout("Edge direction and length"):
                    p0 = edge.points.sample_index(nd.position, index=0)._lc("P0")
                    p1 = edge.points.sample_index(nd.position, index=1)._lc("P1")
                    direction = (p1 - p0)._lc("Direction")
                    length = direction.length._lc("Length")
                    direction = direction.normalize()

                with Repeat(edge=edge, iterations=branches) as br_rep:

                    br_seed = rep_seed.hash_value(br_rep.iteration)

                    br_length = length*extr_scale*Float.Random(.8, 1.2, id=feel.index, seed=br_seed)
                    br_dir = direction + Vector.Random(-.4, .4, id=feel.index, seed=br_seed + 1)

                    br_rep.edge.points[1].extrude(br_dir*br_length)

                feel.generated.geometry = br_rep.edge

            rep.tree = feel.generated.geometry

        rep.tree.out()

    # ----- Mesh 1

    with GeoNodes("Branch 1"):

        iterations = Integer(10, "Iterations")
        trunk_fac  = Float.Factor(.3, "Trunk Factor", min=0, max=1)
        seed       = Integer(0, "Seed")

        line = Mesh.Line(end_location=(0, 0, 1), count=2)
        line.edges.store_named_attribute("Split", True)

        with Repeat(tree=line, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.tree.edges.for_each() as feel:

                edge = Mesh(feel.element)

                with Layout("Edge direction and length"):
                    p0 = edge.points.sample_index(nd.position, index=0)._lc("P0")
                    p1 = edge.points.sample_index(nd.position, index=1)._lc("P1")
                    direction = (p1 - p0)._lc("Direction")
                    length = direction.length._lc("Length")

                with Layout("First edge: from start to point located around trunk factor"):
                    c  = (p0 + p1)*trunk_fac
                    c += Vector.Random(-.1*length, .1*length, id=feel.index, seed=rep_seed)._lc("Center")

                    new_edges = Mesh.Line(start_location=p0, end_location=c, count=2)
                    new_edges.edges.store_named_attribute("Split", False)

                with Layout("Extrude till end point"):
                    new_edges.points[1].extrude(p1 - c)
                    new_edges.edges[1].store_named_attribute("Split", True)

                with Layout("Extrude in another direction"):
                    direction += Vector.Random(-.4*length, .4*length, id=feel.index, seed=rep_seed + 1)
                    length *= (1 - trunk_fac)*Float.Random(.8, 1.2, id=feel.index, seed=rep_seed + 2)

                    new_edges.points[1].extrude(direction.normalize()*length)
                    new_edges.edges[2].store_named_attribute("Split", True)

                with Layout("Keep element if not split"):
                    feel.generated.geometry = edge.switch(edge.edges.sample_index(Boolean.Named("Split"), 0), new_edges)

            rep.tree = feel.generated.geometry

        rep.tree.out()


    # ----- Curve

    with GeoNodes("Branch Curve"):

        iterations = Integer(10, "Iterations")
        seed       = Integer(0, "Seed")

        fr = Curve.Line(end=(0, 0, 1))

        with Repeat(curve=fr, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.curve.splines.for_each() as feel:

                segment = Curve(feel.element)
                p0 = segment.points.sample_index(nd.position, index=0)
                p1 = segment.points.sample_index(nd.position, index=1)

                segment.resample(3)

                segment.points[1].offset = Vector.Random(-.1, .1, id=feel.index, seed=rep_seed)

                direction = p1 - p0
                length = direction.length

                direction += Vector.Random(-.3, .3, id=feel.index, seed=rep_seed + 1)
                length *= Float.Random(.8, 1.2, id=feel.index, seed=rep_seed + 2)


                new_segment = Curve.Line(start=segment.points.sample_index(nd.position, index=1), direction=direction.normalize(), length=length)

                feel.generated.geometry = segment + new_segment


            rep.curve = feel.generated.geometry

        rep.curve.out()
