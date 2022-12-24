# class Geometry

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

# Geometry

**Geometry** is the root class for:
- [Mesh](Mesh.md)
- [Curve](Curve.md)
- [Points](Points.md)
- [Instances](Instances.md)
- [Volume](Volume.md)

## Initialization

Geometry is not initialized directly.

## Input / Output

The default input geometry is read from the current Tree with property `input_geometry` (or with its short version `ig`).

The resulting geometry to output set with the current Tree property 'output_geometry` (or with is short version `og`).

The *do nothing* default tree is the following:

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    tree.og = tree.ig
```

## Examples

### Joining geometry

Three syntaxes are possible to join geometries:
- using the global function `join_geometry`
- using the Geometry method `join` (the geometry instance is part of the joining)
- using the operator `+`

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    in_geo = tree.ig
    
    # ----- Let's create some geometries
    
    circle1 = gn.Curve.Circle().set_position(offset=(0, 0, -2))
    circle2 = gn.Curve.Circle().set_position(offset=(0, 0, -3))
    cube1   = gn.Mesh.Cube().set_position(offset=(0, 0, 2))
    cube2   = gn.Mesh.Cube().set_position(offset=(0, 0, 4))
    volume  = gn.Volume.Cube()
    
    # Global function
    geo = gn.join_geometry(in_geo, circle1, circle2)
    
    # Geometry method
    geo.join(cube1, cube2)
    
    # + operator
    geo = geo + volume
    
    # As a result
    tree.og = geo
```







## Properties

- [ID](#ID)
- [bounding_box](#bounding_box)
- [bounding_box_min](#bounding_box_min)
- [bounding_box_min](#bounding_box_min)
- [convex_hull](#convex_hull)
- [curve_component](#curve_component)
- [domain_size](#domain_size)
- [index](#index)
- [instances_component](#instances_component)
- [is_viewport](#is_viewport)
- [material_index](#material_index)
- [mesh_component](#mesh_component)
- [normal](#normal)
- [points_component](#points_component)
- [position](#position)
- [radius](#radius)
- [separate_components](#separate_components)
- [volume_component](#volume_component)

## Class methods

- [Collection](#Collection)


## Methods

- [attribute_statistic](#attribute_statistic)
- [capture_attribute](#capture_attribute)
- [capture_attribute_node](#capture_attribute_node)
- [delete](#delete)
- [duplicate](#duplicate)
- [field_at_index](#field_at_index)
- [get_named_boolean](#get_named_boolean)
- [get_named_color](#get_named_color)
- [get_named_float](#get_named_float)
- [get_named_integer](#get_named_integer)
- [get_named_vector](#get_named_vector)
- [interpolate_domain](#interpolate_domain)
- [join](#join)
- [material_selection](#material_selection)
- [merge_by_distance](#merge_by_distance)
- [named_attribute](#named_attribute)
- [proximity](#proximity)
- [proximity_edges](#proximity_edges)
- [proximity_faces](#proximity_faces)
- [proximity_points](#proximity_points)
- [random_boolean](#random_boolean)
- [random_float](#random_float)
- [random_integer](#random_integer)
- [random_vector](#random_vector)
- [raycast](#raycast)
- [raycast_interpolated](#raycast_interpolated)
- [raycast_nearest](#raycast_nearest)
- [remove_named_attribute](#remove_named_attribute)
- [replace_material](#replace_material)
- [sample_index](#sample_index)
- [sample_nearest](#sample_nearest)
- [separate](#separate)
- [set_ID](#set_ID)
- [set_material](#set_material)
- [set_material_index](#set_material_index)
- [set_named_boolean](#set_named_boolean)
- [set_named_color](#set_named_color)
- [set_named_float](#set_named_float)
- [set_named_integer](#set_named_integer)
- [set_named_vector](#set_named_vector)
- [set_position](#set_position)
- [store_named_attribute](#store_named_attribute)
- [switch](#switch)
- [to_instance](#to_instance)
- [transform](#transform)

