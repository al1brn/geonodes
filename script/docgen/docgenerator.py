#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:10:09 2024

@author: alain
"""

import bpy

from pprint import pprint
import inspect
from ..geonodes import *
from .. import constants
from ..node_explore import NodeInfo
from .pyparser import Parser, Tokenizer

classes = [Integer, Float, Boolean, String, Vector, Rotation, Matrix, Image, Object, Collection, Geometry, Mesh, Curve, Instances, Cloud, Volume]

# =============================================================================================================================
# Node create

def get_geotree():
    tree_name = 'TEMP_GEO'
    tree = bpy.data.node_groups.get(tree_name)
    if tree is None:
        return bpy.data.node_groups.new(tree_name, type='GeometryNodeTree')
    else:
        return tree

def get_shadertree():
    tree_name = 'TEMP_SHADER'
    tree = bpy.data.node_groups.get(tree_name)
    if tree is None:
        return bpy.data.node_groups.new(tree_name, type='ShaderNodeTree')
    else:
        return tree

def get_node(node_name, tree=None):
    bl0 = constants.NODE_NAMES['GeometryNodeTree'].get(node_name.lower())
    bl1 = constants.NODE_NAMES['ShaderNodeTree'].get(node_name.lower())

    tree = None
    if bl0 is None:
        tree = get_shadertree()
        bl_idname = bl1
    elif bl1 is None or bl0 == bl1:
        tree = get_geotree()
        bl_idname = bl0
    else:
        raise Exception(f"Node name '{node_name}' is implementedd diffrently in both trees")

    if bl_idname is None:
        return None

    for node in tree.nodes:
        if node.bl_idname == bl_idname:
            return node

    node = tree.nodes.new(type=bl_idname)
    return node



# =============================================================================================================================
# Node call parser

def node_call_parser(code, print_code=False):
    """ Parse source code to find Node(node_name, sockets, **params)

    Arguments
    ---------
    - code (str) : source code text

    Returns
    -------
    - tuple (str, dict, dict) : node_name, sockets initialization, params initialisation
    """

    # ----------------------------------------------------------------------------------------------------
    # Look for the initialization of a Node class

    def get_node_calls(tokens, index0=0):
        """ Capture the syntax Node(node_name, sockets={}, **params)

        Compare each token to ('NAME', 'Node') and next as ('(', tokens)
        If the current token in ('(', tokens), explore the sub tokens list

        Arguments
        ---------
        - tokens : list of tokens
        - index0 : first index to read

        Returns
        -------
        - list : all the node calls found
        """

        # ----- Resulting list

        node_calls = []

        # ----- No exploration is possible

        if index0 >= len(tokens):
            return node_calls

        # ----- Loop on the tokens

        for index in range(index0, len(tokens)):

            # ----- Current token

            token = tokens[index]

            # -----  tokens : ('NAME', 'Node') followed by ('(', tokens)

            if token[1] == 'Node' and index < len(tokens) - 1:

                args_token = tokens[index + 1]
                if args_token[0] != '(':
                    continue

                sockets = None
                params  = {}

                # ----- token[1] is a list of lists of tokens
                # The first list could be
                # - sockets = {} | name
                # - {} | name
                # If not, no socket is provided

                tokens_list = args_token[1]

                # ----- Node name

                name_tokens = tokens_list[0]
                assert(len(name_tokens) == 1 and name_tokens[0][0] in ['STRING','NAME'])
                node_name = name_tokens[0][1]
                tokens_list = tokens_list[1:]

                # ----- No argument at all

                if len(tokens_list) == 0:
                    node_calls.append({'name': node_name, 'sockets': None, 'params': {}})
                    continue

                # ----- First argument

                first_tokens = tokens_list[0]

                # ----- A single token : this is the socket dict

                if len(first_tokens) == 1:
                    sockets = first_tokens[0][1]
                    tokens_list = tokens_list[1:]

                # ----- More than one token

                else:
                    if first_tokens[0][1] == 'sockets':
                        assert(first_tokens[1][1] == '=')
                        if len(first_tokens) == 3:
                            sockets = first_tokens[2][1]
                        else:
                            # Complex, for instance (sockets = obj.sockets())
                            sockets = None
                        tokens_list = tokens_list[1:]

                # ----- Other arguments are parameters

                for param_tokens in tokens_list:
                    params[param_tokens[0][1]] = param_tokens[2:]

                call_args = {'name': node_name, 'sockets': sockets, 'params': params}
                node_calls.append(call_args)

            # ----- We have a list, let's explore its items
            # The token[1] list is a list for lists of tokens

            elif token[0] in ['(', '[']:
                for tk in token[1]:
                    node_calls.extend(get_node_calls(tk))

            elif token[0] == '{':
                for val in token[1].values():
                    node_calls.extend(get_node_calls(val))


        return node_calls

    # -----------------------------------------------------------------------------------------------------------------------------
    # Main
    # -----------------------------------------------------------------------------------------------------------------------------

    if code is None:
        return None

    # ----- Tokenizes the source code

    source = Parser(code).source_code_only(True)
    if print_code:
        print('='*100)
        print(code)
        print('-'*100)
        print(source)
        print()

    tokens = Tokenizer(source).tokens()
    if False:
        pprint(tokens)

    # ----------------------------------------------------------------------------------------------------
    # Header

    method = {'staticmethod': False, 'classmethod': False, 'getter': False, 'setter': False}

    args   = None
    i_body = None
    for i, token in enumerate(tokens):
        if token[1] == '@':
            next_token = tokens[i + 1]
            if next_token[1] in ['staticmethod', 'classmethod']:
                method[next_token[1]] = True
            elif next_token[1] == 'property':
                method['setter'] = True
            else:
                method['getter'] = True
                assert(tokens[i + 2][1] == '.')
                assert(tokens[i + 3][1] == 'setter')

        elif token[1] == 'def':
            next_token = tokens[i + 1]
            assert(next_token[0] == 'NAME')
            method['name'] = next_token[1]

            args = tokens[i + 2]

            assert(args[0] == '(')
            assert(tokens[i + 3][1] == ':')
            i_body = i + 3
            break

    # ----------------------------------------------------------------------------------------------------
    # Node creation

    node_calls = get_node_calls(tokens, i_body)
    method['node_calls'] = node_calls

    return method

# =============================================================================================================================
# Take a method into account

implementations = {}

def register_method(class_name, method):
    if len(method['node_calls']) == 0:
        return

    nodes = implementations.get(class_name)
    if nodes is None:
        nodes = []
        implementations[class_name] = nodes

# =============================================================================================================================
# Merge info

def merge_info(class_name, node_call, argspec):

    node_name = node_call['name']
    bnode = get_node(node_name)
    if bnode is None:
        return None

    node_info = NodeInfo(get_geotree(), bnode)

    # node_call :  {'name': node_name, 'sockets': tokens, 'params': tokens})

    info = {'class_name': class_name, 'node_name': node_call['name']}

    sockets = node_call['sockets']
    params  = node_call['params']

    plug_sockets = []
    param_init = {}

    if sockets is not None:
        if isinstance(sockets, dict):

            for key, tokens in sockets.items():
                socket_info = node_info.get_socket_info(key, halt=False)

                """"
                if key.isnumeric():
                    bsocket = bnode.inputs[int(key)]
                else:
                    bsocket = None
                    for bsock in bnode.inputs:
                        if bsock.name == key:
                            bsocket = bsock
                            break
                """

                # -----------------------------------------------------------------------------------------------------------------------------
                # bsocket not found : there is an error in the source code

                if socket_info is None:
                    print('-'*100)
                    print("Class", class_name)
                    print("Node", bnode.name)
                    print("Node inputs:", [bs.name for bs in bnode.inputs])
                    print("Node identifiers:", [bs.identifier for bs in bnode.inputs])
                    print("Node call arguments")
                    print(sockets)
                    raise Exception(f"Socket '{key}' not found in node '{bnode.name}'. Certainly an error in the source code!")

                if len(tokens) == 1:
                    value = tokens[0][1]
                else:
                    value = "<computed>"

                plug_sockets.append({'name': socket_info['name'], 'class': socket_info['class'], 'value': value})

    for name, tokens in params.items():
        if len(tokens) == 1:
            value = tokens[0][1]
        else:
            value = "<computed>"
        param_init[name] = value

    info['plug_sockets'] = plug_sockets
    info['param_init']   = param_init

    return info

# =============================================================================================================================
# Md doc

def yield_doc(class_name, method, argspec):

    # node_call :  {'name': node_name, 'sockets': tokens, 'params': tokens})

    for node_call in method['node_calls']:

        info = merge_info(class_name, node_call, argspec)
        if info is None:
            continue

        yield f"\n# Node '{node_call['name']}'"

        plug_sockets = info['plug_sockets']
        if len(plug_sockets):
            yield "\n\nSockets"
            yield "\n-------"
            for ps in plug_sockets:
                yield f"\n- {ps['name']} ({ps['class']}) : {ps['value']}"

        param_init = info['param_init']
        if len(param_init):
            yield "\n\nParameters"
            yield "\n----------"
            for name, value in param_init.items():
                yield f"\n- {name} : {value}"

        yield "\n"

# ========================================================================================================================
# Generate documentation from source code parsing

def document_script(include=None):

    for cls in classes:

        with GeoNodes("Test"):
            print('-'*30)
            print("Class", cls.__name__)
            print(inspect.getdoc(cls))
            print('-'*30)

            #for m in inspect.getmembers_static(cls):
            for m in inspect.getmembers(cls):

                if include is not None and (m[0] in include):
                    continue

                if m[0][:2] == '__':
                    continue

                is_prop = isinstance(m[1], property)
                if is_prop:
                    funcs = []
                    if m[1].fget is not None:
                        funcs.append(m[1].fget)
                    if m[1].fset is not None:
                        funcs.append(m[1].fset)
                else:
                    funcs = [m[1]]

                for func in funcs:
                    comments = inspect.getdoc(func)

                    if comments is not None:
                        print(" -", m[0], 'EMBEDDED')
                        pprint(comments)
                        continue

                    try:
                        code = inspect.getsource(func)
                    except Exception as e:
                        print(" -", m[0], is_prop, str(e))
                        continue

                    method = node_call_parser(code, False)
                    if not len(method['node_calls']):
                        print(" -", m[0], 'NO CALL')
                        continue

                    try:
                        argspec = inspect.getfullargspec(func)
                    except Exception as e:
                        print(" -", m[0], str(e))
                        continue

                    print(" -", m[0], "OK")

                    if False:
                        pprint(argspec)
                        pprint(method)

                    print('   """')
                    for line in yield_doc(cls.__name__, method=method, argspec=argspec):
                        print(line, end='')
                    print('   """')
                    print()
