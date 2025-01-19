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

module : demo topology
----------------------

Playing with topology

updates
-------
- creation :   2024/09/04

$ DOC START

[Source Code](../demos/topology.py)

This demo provides two modifiers:
- Topology Indices :
  The modifier allows to select a domain in 'Vertices', 'Edges', ...
  It displays the index of each element iof the selected domain
- Mesh Topology :
  The modifier selects a domain in 'Vertices', 'Edges',... and a index which
  must be valid in the selected domain.
  The modifiers displays the linked domain elements, for instance the edges, faces and corners
  linked to a selected vertex.

> [!NOTE]
> Modifiers:
> - Topology Indices
> - Mesh Topology

``` python
from geonodes.demos import topology

topology.demo()
```
"""


from geonodes import *
import numpy as np

def demo():

    COL_UNSELECTED = (.8, .8, .8, 1)
    COL_POINT      = (.8,  0,  0, 1)
    COL_FACE       = (.8,  0, .8, 1)
    COL_EDGE       = ( 0, .8,  0, 1)
    COL_CORNER     = ( 0,  0, .8, 1)

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
    # Create a label based on the attribute "Label Value"
    # Link the selected domain to the label with a line
    # Returns: labels and lines (Curve)

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
    # Show mesh domains
    # Transform the mesh in order to show selected domains:
    # - vertices : place a sphere at each selected points
    # - edges : build a cylinder around selected edges
    # - faces : change the face color of selected faces
    # - corners : place a cube at each selected corner, slightly displaced toward the center of its face

    with GeoNodes("Mesh Selection", is_group=True):

        mesh = Mesh()
        size = Float(.1, "Size", 0)

        mesh.faces.material = "Topology"
        mesh.faces._Color = COL_UNSELECTED

        with Layout("Selected Vertices"):

            cloud = mesh.points[Boolean("Select V")].to_points()
            v_vis = Mesh(cloud.instance_on(instance=Mesh.UVSphere(radius=size)).realize())
            v_vis.faces.material = "Topology"
            v_vis.faces.smooth = True
            v_vis.faces._Color = COL_POINT

        with Layout("Selected Edges"):

            curve = mesh[Boolean("Select E")].to_curve()
            e_vis = curve.to_mesh(profile_curve=Curve.Circle(radius=size/2))
            e_vis.faces.material = "Topology"
            e_vis.faces.smooth = True
            e_vis.faces._Color = COL_EDGE

        with Layout("Selected Faces"):

            mesh.faces[Boolean("Select F")]._Color = COL_FACE

        with Layout("Selected Corners"):

            cube_size = size*2

            with mesh.corners[Boolean("Select C")].for_each(position=nd.position, face_index=nd.face_of_corner()) as feel:

                face_pos = mesh.faces.sample_index(nd.position, index=feel.face_index)
                v = (face_pos - feel.position).normalize()
                c_point = Cloud.Points(1, position=feel.position + cube_size*v)

                feel.generated.geometry = c_point

            cloud = Cloud(feel.generated.geometry)
            c_vis = Mesh(cloud.instance_on(instance=Mesh.Cube(size=cube_size)).realize())
            c_vis.faces.material = "Topology"
            c_vis.faces.smooth = False
            c_vis.faces._Color = COL_CORNER

        mesh += (v_vis, e_vis, c_vis)
        mesh.out()

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
            selection = Boolean(True, "Selection")
            use_indices = Boolean(False, "Use Indices")
            ind0 = Integer(0,    "First Index", 0, single_value=True)
            ind1 = Integer(1000, "Last Index", 0, single_value=True)

        with Layout("Mesh domains"):
            pt_cloud = mesh.points.to_points()
            pt_cloud.points._Selection = mesh.points.sample_index(selection, nd.index)

            pt_cloud.points._Normal = mesh.points.sample_index(nd.normal, nd.index)
            pt_cloud.points._Value  = mesh.points.sample_index(nd.index,  nd.index)
            pt_cloud.points._Color  = COL_POINT

            face_cloud = mesh.faces.to_points()
            face_cloud.points._Selection = mesh.faces.sample_index(selection, nd.index)

            face_cloud.points._Normal = mesh.faces.sample_index(nd.normal, nd.index)
            face_cloud.points._Value  = mesh.faces.sample_index(nd.index,  nd.index)
            face_cloud.points._Color  = COL_FACE

            edge_cloud = mesh.edges.to_points()
            edge_cloud.points._Selection = mesh.edges.sample_index(selection, nd.index)

            edge_cloud.points._Normal = mesh.edges.sample_index(nd.normal, nd.index)
            edge_cloud.points._Value  = mesh.edges.sample_index(nd.index,  nd.index)
            edge_cloud.points._Color  = COL_EDGE

            crn_cloud = mesh.corners.to_points()
            crn_cloud.points._Selection = mesh.corners.sample_index(selection, nd.index)

            crn_cloud.points._Normal = mesh.corners.sample_index(nd.normal, nd.index)
            crn_cloud.points._Value  = mesh.corners.sample_index(nd.index,  nd.index)
            crn_cloud.points._Color  = COL_CORNER

        with Layout("Curve domains"):

            spt_cloud = Cloud.Points(count=curve.points.count)
            spt_cloud.points._Selection = curve.points.sample_index(selection, nd.index)

            spt_cloud.position = curve.points.sample_index(nd.position, nd.index)
            spt_cloud.points._Normal = curve.points.sample_index(curve.tangent, nd.index).cross((0, 0, 1)).normalize()

            spt_cloud.points._Value = curve.points.sample_index(nd.index, nd.index)
            spt_cloud.points._Color  = COL_POINT

            spline_cloud = Cloud(spt_cloud)

            spline_cloud.points._Value  = curve.points.sample_index(curve.points.curve_index(nd.index), nd.index)
            delete = curve.points.sample_index(curve.points.index_in_curve(nd.index), nd.index).not_equal(0)
            spline_cloud.points._Color  = COL_EDGE
            spline_cloud.points[delete].delete()

            spline_cloud.points._Selection = curve.splines.sample_index(selection, nd.index)


        with Layout("Cloud"):

            cl_cloud = Cloud(cloud)
            cl_cloud.points._Selection = cloud.points.sample_index(selection, nd.index)

            cl_cloud.points._Normal = (1, 0, 0)
            cl_cloud.points._Value = nd.index
            cl_cloud.points._Color  = COL_POINT

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
            show = Boolean("Selection") & ((nd.index >= ind0) & (nd.index <= ind1) | (-use_indices))

        labels = G().show_labels(cloud=cloud, label_value=cloud._Value, show=show, direction=cloud._Normal, label_color=cloud._Color, link_from='TREE')

        labels.switch(merge, geo + labels).out()

    # ====================================================================================================
    # Mesh Topology

    with GeoNodes("Mesh Topology"):

        mesh = Mesh()
        mesh.material = "Topology"
        mesh.faces._Color = COL_UNSELECTED

        index = Integer(0, "Domain Index")

        topo_link = {'exclude': 'Domain'}

        with If(Geometry, "Vertices", name="Domain") as geo:

            vert_mesh = Mesh(mesh)
            vert_mesh.points._Select_V = nd.index.equal(index)
            vrt_vis = G().topology_indices(geometry=vert_mesh, merge_input_geometry=False, domain='Vertices', selection=Boolean("Select V"), link_from=topo_link)

            with Layout("Corners & Faces of Vertex"):

                vert_mesh.faces._Select_F = False
                vert_mesh.corners._Select_C = False

                total = vert_mesh.points.sample_index(Vertex.corners_total(), index)
                with Repeat(mesh=vert_mesh, iterations=total) as rep:
                    corner_index = Vertex.corner_index(index, sort_index=rep.iteration)
                    rep.mesh.corners[corner_index]._Select_C = True
                    rep.mesh.faces._Select_F |= nd.index.equal(Corner.face_index(corner_index))

                vert_mesh = rep.mesh

                vrt_vis += G().topology_indices(geometry=vert_mesh, merge_input_geometry=False, domain='Corners', selection=Boolean("Select C"), link_from=topo_link)
                vrt_vis += G().topology_indices(geometry=vert_mesh, merge_input_geometry=False, domain='Faces', selection=Boolean("Select F"), link_from=topo_link)

            with Layout("Edges of Vertex"):
                sel = Edge.vertex_index_1.equal(index) | Edge.vertex_index_2.equal(index)
                vert_mesh.edges._Select_E = sel
                vrt_vis += G().topology_indices(geometry=vert_mesh, merge_input_geometry=False, domain='Edges', selection=Boolean("Select E"), link_from=topo_link)

            vrt_vis += Group("Mesh Selection", mesh=vert_mesh, link_from='TREE').geometry

            geo.option = vert_vis


        #with Layout("Edge Domain"):
        with Elif(geo, "Edges"):

            edge_mesh = Mesh(mesh)
            edge_mesh.edges._Select_E = nd.index.equal(index)
            edge_vis = G().topology_indices(geometry=edge_mesh, merge_input_geometry=False, domain='Edges', selection=Boolean("Select E"), link_from=topo_link)

            with Layout("Vertices of Edge"):
                v1 = mesh.edges.sample_index(Edge.vertex_index_1, index)
                v2 = mesh.edges.sample_index(Edge.vertex_index_2, index)
                edge_mesh.points._Select_V = nd.index.equal(v1) | nd.index.equal(v2)

                edge_vis += G().topology_indices(geometry=edge_mesh, merge_input_geometry=False, domain='Vertices', selection=Boolean("Select V"), link_from=topo_link)

            with Layout("Corners & Faces of Edge"):

                edge_mesh.faces._Select_F = False
                total = edge_mesh.corners.sample_index(Edge.corners_total(index), index)

                with Layout("Repeat Zone"):
                    with Repeat(mesh=edge_mesh, iterations=total) as rep:
                        corner_index = Edge.corner_index(index, sort_index=rep.iteration)
                        rep.mesh.corners[corner_index]._Select_C = True
                        rep.mesh.faces[Corner.face_index(corner_index)]._Select_F = True

                edge_mesh = rep.mesh
                edge_vis += G().topology_indices(geometry=edge_mesh, merge_input_geometry=False, domain='Corners', selection=Boolean("Select C"), link_from=topo_link)
                edge_vis += G().topology_indices(geometry=edge_mesh, merge_input_geometry=False, domain='Faces', selection=Boolean("Select F"), link_from=topo_link)

            edge_vis += Group("Mesh Selection", mesh=edge_mesh, link_from='TREE').geometry

            geo.edge_vis.option = edge_vis

        #with Layout("Face Domain"):
        with Elif(geo, "Faces"):

            face_mesh = Mesh(mesh)
            face_mesh.faces._Select_F = nd.index.equal(index)
            face_vis = G().topology_indices(geometry=face_mesh, merge_input_geometry=False, domain='Faces', selection=Boolean("Select F"), link_from=topo_link)

            with Layout("Corners and Vertices of Face"):
                face_mesh.corners._Select_C = False
                face_mesh.points._Select_V = False
                face_mesh.edges._Select_E = False

                total = face_mesh.faces.sample_index(Face.corners_total(index), index=index)

                with Repeat(mesh=face_mesh, iterations=total) as rep:

                    corner_index = rep.mesh.faces.sample_index(Face.corner_index(index, sort_index=rep.iteration))
                    vertex_index = rep.mesh.corners.sample_index(Corner.vertex_index(), corner_index)
                    edge_index = rep.mesh.corners.sample_index(Corner.next_edge_index(), corner_index)
                    rep.mesh.corners[corner_index]._Select_C = True
                    rep.mesh.points[vertex_index]._Select_V = True
                    rep.mesh.edges[edge_index]._Select_E = True

                face_mesh = rep.mesh
                face_vis += G().topology_indices(geometry=face_mesh, merge_input_geometry=False, domain='Corners', selection=Boolean("Select C"), link_from=topo_link)
                face_vis += G().topology_indices(geometry=face_mesh, merge_input_geometry=False, domain='Vertices', selection=Boolean("Select V"), link_from=topo_link)
                face_vis += G().topology_indices(geometry=face_mesh, merge_input_geometry=False, domain='Edges', selection=Boolean("Select E"), link_from=topo_link)

            face_vis += Group("Mesh Selection", mesh=face_mesh, link_from='TREE').geometry

            geo.option = face_vis

        #with Layout("Corner Domain"):
        with Elif(geo, "Corners"):

            crn_mesh = Mesh(mesh)
            crn_mesh.corners._Select_C = nd.index.equal(index)
            crn_vis = G().topology_indices(geometry=crn_mesh, merge_input_geometry=False, domain='Corners', selection=Boolean("Select C"), link_from=topo_link)

            crn_mesh.points._Select_V = nd.index.equal(crn_mesh.corners.sample_index(Corner.vertex_index(), index))
            edge0 = crn_mesh.corners.sample_index(Corner.next_edge_index(), index)
            edge1 = crn_mesh.corners.sample_index(Corner.previous_edge_index(), index)
            crn_mesh.edges._Select_E = nd.index.equal(edge0) | nd.index.equal(edge1)
            crn_mesh.faces._Select_F = nd.index.equal(crn_mesh.corners.sample_index(Corner.face_index(), index))

            crn_vis += G().topology_indices(geometry=crn_mesh, merge_input_geometry=False, domain='Vertices', selection=Boolean("Select V"), link_from=topo_link)
            crn_vis += G().topology_indices(geometry=crn_mesh, merge_input_geometry=False, domain='Faces', selection=Boolean("Select F"), link_from=topo_link)
            crn_vis += G().topology_indices(geometry=crn_mesh, merge_input_geometry=False, domain='Edges', selection=Boolean("Select E"), link_from=topo_link)

            crn_vis += Group("Mesh Selection", mesh=crn_mesh, link_from='TREE').geometry

            geo.option = crn_vis

        geo.out()

        """
        vis = Geometry.MenuSwitch({
            "Vertices": vrt_vis,
            "Edges"   : edge_vis,
            "Faces"   : face_vis,
            "Corners" : crn_vis,
            }, menu="Vertices", name="Domain")

        vis.out()
        """
