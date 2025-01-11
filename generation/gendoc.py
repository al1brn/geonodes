#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:42:54 2024

@author: alain
"""

from importlib import reload
import requests
import re

from docgen import packagedoc, documentation
import docgen

reload(documentation)
reload(packagedoc)
reload(docgen)

from docgen import PackageDoc

# =============================================================================================================================
# Get the url of nodes documentation on blender site

gnodes_url  = "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/"
shader_url  = "https://docs.blender.org/manual/en/latest/render/shader_nodes/"

# ----- Load list of geometry nodes from blender doc website

x = requests.get(gnodes_url + "index.html")
if x.status_code != 200:
    raise Exception("Impossible to download index from Blender site")
gnodes_ref = str(x.content)

# ----- Load list of shader nodes from blender doc website

x = requests.get(shader_url + "index.html")
if x.status_code != 200:
    raise Exception("Impossible to download index from Blender site")
shader_ref = str(x.content)

# ----- Regular expression to search by name

ref_search = r'<a class="reference internal" href="(?P<url>[^"]*)">(NODE_NAME) Node</a>'

# ----- Return the url of the node

def get_node_link(tree, name):
    if tree == 'NODE':
        ref  = gnodes_ref
        base = gnodes_url
    else:
        ref  = shader_ref
        base = shader_url

    m = re.search(ref_search.replace('NODE_NAME', name), ref, flags=re.MULTILINE | re.IGNORECASE)
    if m is None:
        return f"ERROR: Node '{name}' not found"
    return f"[{name}]({base + m.group('url')})"

# =============================================================================================================================
# Cross references

g_nodes = {}
s_nodes = {}

def cross_ref(tree, name, section):

    nodes = g_nodes if tree == 'NODE' else s_nodes

    class_ = section
    while class_ is not None and class_.tag != 'Classes':
        class_ = class_.parent

    if class_ is not None and class_.hidden:
        return

    cref = nodes.get(name)
    if cref is None:
        cref = []
        nodes[name] = cref

    if class_ is None:
        for a, b in cref:
            if a is None and b.title == section.title:
                return
    else:
        for a, b in cref:
            if a is None:
                continue
            if a.title == class_.title and b.title == section.title:
                return

    cref.append((class_, section))


# =============================================================================================================================
# Regular expressions

# -----------------------------------------------------------------------------------------------------------------------------
# [&COMMAND]
#
# Accepted commands are
# - SHADER : method is specific to shaders
# - MIX : method behaves differently in shader / geonodes
# - RETURN_NODE : returns a node, not as socket

tag_expr = r"\[&(?P<tag>\w*)\]"
ctag     = re.compile(tag_expr,  flags = re.MULTILINE)

def tag_replace(m, section):

    tag = m.group('tag').strip().upper()

    if tag == 'SHADER':
        return ":sunrise: **ShaderNodes** only\n"

    elif tag == 'MIX':
        return ":hotsprings: Behaves differently in **GeoNodes** and **ShaderNodes**\n"

    elif tag == 'RETURN_NODE':
        return ":warning: returns the **node**, not a socket"

    elif tag == 'JUMP':
        return ""

    elif tag == 'NO_JUMP':
        return ""

    else:
        print(f"UNKNOWN Method tag: '{tag}' in '{m.group(0)}'")
        return m.group(0)

# -----------------------------------------------------------------------------------------------------------------------------
# <&Node node name> or <*Node node name>
#
# Reference to blender documentation
# - & : add a cross reference
# - * : don't add a crosse reference

bnode_expr = r"<(?P<cross>(&|\*))(?P<tree>\w*) *(?P<name>[^>]*)>"
cbnode = re.compile(bnode_expr, flags = re.MULTILINE)

def bnode_replace(m, section):

    cross = m.group('cross')
    tree  = m.group('tree').upper()
    name  = m.group('name').strip()

    if cross == '&':
        cross_ref(tree, name, section)

    return get_node_link(tree, name)


# =============================================================================================================================
# geonodes module documentation

def geonodes_documentation(write_files=True):

    from importlib import reload
    from pathlib import Path

    print('-'*100)
    print("Generate documentation of geonodes")
    print()

    import geonodes
    reload(geonodes)

    folder = Path(geonodes.__file__).parents[0] / 'doc'
    if not write_files:
        folder = None

    # -----------------------------------------------------------------------------------------------------------------------------
    # Load the package

    print("Load package...")
    doc = PackageDoc(geonodes)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Socket class is hidden as a sub class of generated classes
    # Let's hunhide it

    doc.top_section.find("Socket").hidden = False

    # -----------------------------------------------------------------------------------------------------------------------------
    # DEBUG

    if False:
        return

    # -----------------------------------------------------------------------------------------------------------------------------
    # Hooks to replace references to nodes and build cross references

    print("Replacements...")
    if True:
        child_iter = doc.top_section.all_values()
        for section in child_iter:

            if section.is_hidden:
                child_iter.no_child()
                continue

            if section.is_transparent:
                continue

            if section.comment is None:
                continue

            section.comment = ctag.sub(  lambda m: tag_replace(  m, section), section.comment)
            section.comment = cbnode.sub(lambda m: bnode_replace(m, section), section.comment)
    else:
        doc.set_hook(tag_expr, tag_replace)
        doc.set_hook(bnode_expr, bnode_replace)

        doc.cook()


    # -----------------------------------------------------------------------------------------------------------------------------
    # Add the cross reference page

    print("Cross references...")

    cross_page = doc.top_section.new_page("Cross Reference",
            in_toc=True, parent_toc_depth=0,
            toc=True, sort_sections=True, toc_flat=True, toc_sort=True)
    cross_page.write("You will find here how nodes are implemented")

    for node_name, refs in g_nodes.items():
        node_section = cross_page.new(node_name.replace('/', ' '), in_toc=True, depth_shift=2)
        for class_, member_ in refs:
            if class_ is None:
                node_section.write(f"- <!{member_.title}>\n")
            else:
                if class_.hidden:
                    continue

                node_section.write(f"- <!{class_.title}> :white_small_square: <!{class_.title}#{member_.title}>\n")

    cross_page = doc.top_section.new_page("Shader Cross Reference",
            in_toc=True, parent_toc_depth=0,
            toc=True, sort_sections=True, toc_flat=True, toc_sort=True)
    cross_page.write("You will find here how nodes are implemented")


    for node_name, refs in s_nodes.items():
        node_section = cross_page.new(node_name.replace('/', ' '), in_toc=True, depth_shift=2)
        for class_, member_ in refs:
            if class_ is None:
                node_section.write(f"- <!{member_.title}>\n")
            else:
                if class_.hidden:
                    continue

                node_section.write(f"- <!{class_.title}> :white_small_square: <!{class_.title}#{member_.title}>\n")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Finally create documentation

    print("Create documentation files...")
    doc.create_documentation(folder)

    print("Done")
