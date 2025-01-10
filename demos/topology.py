from geonodes import *
import numpy as np

def demo():

    # ====================================================================================================
    # Shader

    with ShaderNodes("Topology"):

        ped = Shader.Principled(
            base_color = snd.attribute("Color").color,
            roughness  = .8,
            metallic   = .3,
        )
        ped.out()

    with ShaderNodes("Label"):

        ped = Shader.Principled(
            base_color = snd.attribute("Color").color,
            roughness  = 1,
            metallic   = 0,
        )
        ped.out()


    # ====================================================================================================
    # Show the labels

    with GeoNodes("Show Labels"):

        cloud = Cloud()
        with Panel("Labels"):
            value     = Integer(0, "Label Value")
            show      = Boolean(True, "Show")
            direction = Vector((0, 0, 1), "Direction")
            dist      = Float(.3, "Distance")
            color     = Color((.1, .1, .8), "Label Color")

        with Panel("Options"):
            font_size = Float(.3, "Font Size")
            face_cam  = Boolean(False, "Orient to Camera")

        with cloud.points[show].for_each(value=value, position=nd.position + dist*direction) as feel:

            cam_vec = Object.ActiveCamera().info().location - feel.position
            rot = Rotation((np.pi/2, 0, 0)).align_z_to_vector(cam_vec, factor=face_cam, pivot_axis='Y')

            label = Curve(feel.value.to_string().to_curves(size=font_size, align_x='CENTER'))
            label.transform(translation=feel.position, rotation=rot)
            label = label.fill()

            feel.generated.geometry = label

        curves = feel.generated.geometry
        curves = Mesh(Instances(curves).realize())

        curves.faces._Color = color
        curves.material = "Label"

        with Layout("Lines"):
            line = Curve.Line()
            lines = cloud[show].instance_on(instance=line, scale=dist, rotation=Rotation.AlignZToVector(direction))
            lines = Curve(lines.realize())
            lines = lines.to_mesh(profile_curve=Curve.Circle(resolution=12, radius=.01))

            lines.faces._Color = color
            lines.material = "Label"

        (curves + lines).out()

    # ====================================================================================================
    # Indices

    with GeoNodes("Topology Indices"):

        geo = Geometry()

        with Panel("Options"):
            merge = Boolean(True, "Merge input Geometry")

        mesh  = geo.mesh
        curve = geo.curve
        cloud = geo.point_cloud

        with Panel("Domain"):
            ind0 = Integer(0,    "First Index", 0, single_value=True)
            ind1 = Integer(1000, "Last Index", 0, single_value=True)

        with Layout("Mesh domains"):
            pt_cloud = mesh.points.to_points()
            pt_cloud.points._Normal = mesh.points.sample_index(nd.normal, nd.index)
            pt_cloud.points._Value  = mesh.points.sample_index(nd.index,  nd.index)
            pt_cloud.points._Color  = (.9, 0, 0)

            face_cloud = mesh.faces.to_points()
            face_cloud.points._Normal = mesh.faces.sample_index(nd.normal, nd.index)
            face_cloud.points._Value  = mesh.faces.sample_index(nd.index,  nd.index)
            face_cloud.points._Color  = (0, .9, 0)

            edge_cloud = mesh.edges.to_points()
            edge_cloud.points._Normal = mesh.edges.sample_index(nd.normal, nd.index)
            edge_cloud.points._Value  = mesh.edges.sample_index(nd.index,  nd.index)
            edge_cloud.points._Color  = (0, 0, .9)

            crn_cloud = mesh.corners.to_points()
            crn_cloud.points._Normal = mesh.corners.sample_index(nd.normal, nd.index)
            crn_cloud.points._Value  = mesh.corners.sample_index(nd.index,  nd.index)
            crn_cloud.points._Color  = (.1, .9, .9)

        with Layout("Curve domains"):

            spt_cloud = Cloud.Points(count=curve.points.count)
            spt_cloud.position = curve.points.sample_index(nd.position, nd.index)
            spt_cloud.points._Normal = curve.points.sample_index(curve.tangent, nd.index).cross((0, 0, 1)).normalize()

            spt_cloud.points._Value = curve.points.sample_index(nd.index, nd.index)
            spt_cloud.points._Color  = (.9, 0, 0)

            spline_cloud = Cloud(spt_cloud)
            spline_cloud.points._Value  = curve.points.sample_index(curve.points.curve_index(nd.index), nd.index)
            delete = curve.points.sample_index(curve.points.index_in_curve(nd.index), nd.index).not_equal(0)
            spline_cloud.points._Color  = (0, .9, 0)
            spline_cloud.points[delete].delete()

        with Layout("Cloud"):

            cl_cloud = Cloud(cloud)
            cl_cloud.points._Normal = (1, 0, 0)
            cl_cloud.points._Value = nd.index
            cl_cloud.points._Color  = (1, 0, 0)

        with Panel("Domain"):
            cloud = Cloud.MenuSwitch(items={
                "Vertices" : pt_cloud,
                "Faces"    : face_cloud,
                "Edges"    : edge_cloud,
                "Corners"  : crn_cloud,
                "Spline Points" : spt_cloud,
                "Splines" : spline_cloud,
                "Cloud Points" : cl_cloud,
            }, menu=0, name="Domain")

        with Layout("Selection"):
            show = (nd.index >= ind0) & (nd.index <= ind1)
            selected = Boolean("Selected")
            show = show.switch(selected.exists_, selected & show)

        labels = G.show_labels(cloud=cloud, label_value=cloud._Value, show=show, direction=cloud._Normal, label_color=cloud._Color, link_from='TREE')

        labels.switch(merge, geo + labels).out()

    # ====================================================================================================
    # Mesh Topology

    with GeoNodes("Mesh Topology"):

        in_mesh = Mesh()
        in_mesh.material = "Topology"
        in_mesh.faces._Color = (.8, .8, .8, 1)

        index = Integer(0, "Domain Index")

        with Layout("Vertex Domain"):

            with Layout("Corners of Vertex"):
                mesh = Mesh(in_mesh)
                mesh.corners._Selected = mesh.corners.vertex_index(nd.index).equal(index)

                vrt_vis = G.topology_indices(geometry=mesh, merge_input_geometry=False, domain='Corners', first_index=0, last_index=1000, link_from='TREE')

            with Layout("Edges of Vertex"):
                mesh = Mesh(in_mesh)
                mesh.edges._Selected = mesh.edges.vertex_index_1.equal(index)
                mesh.edges._Selected |= mesh.edges.vertex_index_2.equal(index)

                vrt_vis += G.topology_indices(geometry=mesh, merge_input_geometry=False, domain='Edges', first_index=0, last_index=1000, link_from='TREE')

            with Layout("Faces of Vertex"):
                mesh = Mesh(in_mesh)
                total = mesh.points.sample_index(mesh.points.corners_total(), index)
                mesh.faces._Selected = False
                with Repeat(mesh=mesh, iterations=total) as rep:
                    corner_index = mesh.points.corner_index(index, sort_index=rep.iteration)
                    rep.mesh.faces._Selected |= nd.index.equal(rep.mesh.corners.face_index(corner_index))

                mesh = rep.mesh
                in_mesh.faces[mesh.faces.sample_index(mesh._Selected, nd.index)]._Color = (0, .5, 0, 1)

                vrt_vis += G.topology_indices(geometry=mesh, merge_input_geometry=False, domain='Faces', first_index=0, last_index=1000, link_from='TREE')

        with Layout("Edge Domain"):

            with Layout("Vertices of Edge"):
                mesh = Mesh(in_mesh)
                v1 = mesh.edges.sample_index(mesh.edges.vertex_index_1, index)
                v2 = mesh.edges.sample_index(mesh.edges.vertex_index_2, index)
                mesh.points._Selected = nd.index.equal(v1) | nd.index.equal(v2)

                edge_vis = G.topology_indices(geometry=mesh, merge_input_geometry=False, domain='Vertices', first_index=0, last_index=1000, link_from='TREE')

            # IN PROGRESS
            with Layout("Faces of Edge"):
                mesh = Mesh(in_mesh)
                c1 = mesh.edges.sample_index(mesh.edges.corner_index(1), index)
                c2 = mesh.edges.sample_index(mesh.edges.corner_index(2), index)
                mesh.faces._Selected = nd.index.equal(nd.vertex_of_corner(v1)) | nd.index.equal(nd.vertex_of_corner(v1))

                edge_vis += G.topology_indices(geometry=mesh, merge_input_geometry=False, domain='Faces', first_index=0, last_index=1000, link_from='TREE')


        #(edge_vis + in_mesh).out()
        (vrt_vis + in_mesh).out()
