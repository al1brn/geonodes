#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:42:54 2024

@author: alain
"""

from importlib import reload
import requests
import re

from docgen import pydoc, documentation
import docgen

reload(documentation)
reload(pydoc)
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
    if tree == 'Node':
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
# Methods tags

# [$COMMAND]
# Accepted commands are
# - SHADER : method is specific to shaders
# - MIX : method behaves differently in shader / geonodes
# - RETURN_NODE : returns a node, not as socket

# [!Node] node name, node name
expr1 = r"\[!(?P<cmd>\w*)\] *(?P<names>.*)"

# <&Node node name> : cross reference
# <*Node node name> : no cross reference
expr1b = r"<(?P<cross>(&|\*))(?P<cmd>\w*) *(?P<names>[^>]*)>"

# Node 'node name' (bl_idname)
expr2 = r"^(?P<tree>(Node)|(ShaderNode)) *'(?P<name>[^']*)' \((?P<blid>\w*)\)"

cexpr1  = re.compile(expr1,  flags = re.MULTILINE)
cexpr1b = re.compile(expr1b, flags = re.MULTILINE)
cexpr2  = re.compile(expr2,  flags = re.MULTILINE)

g_nodes = {}
s_nodes = {}

def cross_ref(tree, name, section):
    
    nodes = g_nodes if tree == 'Node' else s_nodes
    
    class_ = section
    while class_ is not None and class_.tag != 'Classes':
        class_ = class_.parent
        
    cref = g_nodes.get(name)
    if cref is None:
        cref = []
        nodes[name] = cref
        
    cref.append((class_, section))
    
def replace1(m, section):

    cross = m.group('cross')
    cmd   = m.group('cmd').strip()
    names = m.group('names')
    
    # [!SHADER] : only in ShaderNodes
    # [!MIX] : two behaviors
    
    if cmd.upper() == 'SHADER':
        return ":sunrise: **ShaderNodes** only\n"
    
    elif cmd.upper() == 'MIX':
        #return f"> [!IMPORTANT]\n> Behaves differently in GeoNodes and ShaderNodes\n"
        return ":hotsprings: Behaves differently in **GeoNodes** and **ShaderNodes**\n"
    
    elif cmd.upper() == 'RETURN_NODE':
        return ":warning: returns the **node**, not a socket"
    
    # Not for us!
    
    if cmd.upper() not in ['NODE', 'SHADERNODE']:
        return m.group(0)
    
    # [!Node] or [!ShaderNode]
    
    if cmd.upper() == 'NODE':
        cmd = 'Node'
    else:
        cmd = 'ShaderNode'
        
    s = ""
    for a_name in names.split(','):
        name = a_name.strip()
        
        if s != "":
            s += ', '
            
        if cross:
            cross_ref(cmd, name, section)
        
        s += get_node_link(cmd, name)
        
    return s

# OLD VERSION

def replace2(m, section):
    
    tree = m.group('tree')
    name = m.group('name').strip()
    
    cross_ref(tree, name, section)
    
    return "> **node** : " + get_node_link(tree, name)
    

# =============================================================================================================================
# geonodes module documentation

def geonodes_documentation(write_files=True):
    
    from importlib import reload
    from pathlib import Path
    
    print('-'*100)
    print("Generates documentation of geonodes")
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
    # Hooks to replace references to nodes and build cross references
    
    print("Replacements...")
    child_iter = doc.top_section.all_values()
    for section in child_iter:
        if section.is_hidden:
            child_iter.no_child()
            continue
        
        if section.is_transparent:
            continue
        
        if section.comment is None:
            continue
        
        #section.comment = cexpr1.sub(lambda m: replace1(m, section), section.comment)
        section.comment = cexpr1b.sub(lambda m: replace1(m, section), section.comment)
        section.comment = cexpr2.sub(lambda m: replace2(m, section), section.comment)
        
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
                node_section.write(f"- <!{class_.title}> :white_small_square: <!{class_.title}#{member_.title}>\n")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Finally create documentation
    
    print("Create documentation files...")
    doc.create_documentation(folder)
    





    
    

