#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:55:10 2024

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : node_explore
---------------------
- Generate source code from node analaysis

updates
-------
- creation : 2024/07/23
- update   : 2024/02/17
- update   : 2024/03/29
- update   : 2024/07/31
"""

from pprint import pprint
from pathlib import Path
import inspect

import bpy
import mathutils

from ..core import constants
from ..core import utils
from . import blendertree
from .mapping import Mapping

# ====================================================================================================
# Analyze a node

class NodeInfo:

    STD_ATTRS = None

    def __init__(self, btree, bnode):
        """ Tree node vrapper.

        Ued to analyze the behavior of a node:
            - List of input sockets
            - List of output sockets
            - List or parameters

        Arguments
        ---------
            - btree (Blender NodeTree) : the current node tree
            - bnode (Blender Node) : a node in the tree
        """

        if isinstance(bnode, str):
            bl_idname = constants.NODE_NAMES[btree.bl_idname].get(bnode.lower())
            if bl_idname is None:
                bl_idname = bnode
            bnode = btree.nodes.new(type=bl_idname)

        self.bnode = bnode
        self.btree = btree
        self.is_gnodes = self.btree.bl_idname == 'GeometryNodeTree'
        self.is_shader = self.btree.bl_idname == 'ShaderNodeTree'

        # ----------------------------------------------------------------------------------------------------
        # Make sure STD_ATTRS is initialized

        if NodeInfo.STD_ATTRS is None:
            ref_node = btree.nodes.new(type='ShaderNodeValue')
            NodeInfo.STD_ATTRS = dir(ref_node)
            btree.nodes.remove(ref_node)
            NodeInfo.STD_ATTRS.append('active_item')
            NodeInfo.STD_ATTRS.append('active_index')

        # ----------------------------------------------------------------------------------------------------
        # Analyze the parameters

        self.params = {}
        for name in dir(self.bnode):
            if name in NodeInfo.STD_ATTRS or name[-6:] == '_items':
                continue
            self.params[name] = getattr(self.bnode, name)

        #self.params = {name: getattr(self.bnode, name) for name in dir(self.bnode) if name not in NodeInfo.STD_ATTRS}

        # ----- Parameters in enum

        self.enum_params   = {}
        for param in self.params:
            enums = self.get_enum_list(param)
            if enums is None:
                continue
            self.enum_params[param] = enums

    def __str__(self):
        return f"<Node '{self.bnode.name}' ({self.bnode.bl_idname})>"

    def __repr__(self):
        s = f"#Node '{self.bnode.name}' ({self.bnode.bl_idname})"

        if len(self.bnode.inputs):
            s += "\nInput sockets"
            s += "\n-------------"
            for i, sock in enumerate(self.bnode.inputs):
                s += f"\n {i} - {sock.name} ({sock.type})"

        if len(self.bnode.outputs):
            s += "\n\nOutput sockets"
            s += "\n--------------"
            for i, sock in enumerate(self.bnode.outputs):
                s += f"\n {i} - {sock.name} ({sock.type})"

        if len(self.params):
            s += "\n\nParameters"
            s += "\n----------"
            for k, v in self.params.items():
                s += f"\n - {k:15s} : {v}"
                if k in self.enum_params:
                    s += f" in {self.enum_params[k]}"

        return s + "\n"

    # =============================================================================================================================
    # Loop

    @classmethod
    def Load(cls, name, tree_type='GeometryNodeTree'):

        btree = blendertree.get_tree("Temp", tree_type=tree_type, create=True)
        btree.nodes.clear()

        for type_name in dir(bpy.types):

            try:
                bnode = btree.nodes.new(type=type_name)
            except RuntimeError as e:
                continue

            if bnode.name != name:
                continue

            return NodeInfo(btree, bnode)

        return None

    # -----------------------------------------------------------------------------------------------------------------------------
    # Some properties

    @property
    def python_name(self):
        return utils.socket_name(self.bnode.name)

    @property
    def in_sockets_count(self):
        return len(self.bnode.inputs)

    @property
    def out_sockets_count(self):
        return len(self.bnode.outputs)

    @property
    def has_multi_input(self):
        for bsocket in self.bnode.inputs:
            if bsocket.is_multi_input:
                return True
        return False

    @property
    def global_is_prop(self):
        return self.in_sockets_count == 0 and len(self.params) == 0

    def out_socket_str(self, bsocket, suffix=''):
        return f"{utils.socket_name(bsocket.name)}{suffix} ({constants.CLASS_NAMES[bsocket.type]})"

    @property
    def has_items(self):
        return 'active_item' in dir(self.bnode)

    @property
    def items_prop(self):
        for name in dir(self.bnode):
            if name[-6:] == '_items':
                return name
        return None

    # ====================================================================================================
    # Get the valid values of an enum params

    def get_enum_list(self, param):
        """ Get the list of valid values of a node parameter.

        The list can vary when node parameters are changed.

        Arguments
        ---------
            - param (str) : Node parameter name

        Returns
        -------
            - tuple of valid values or None if the parameter is not a enum parameter
        """

        value = self.params[param]
        if not isinstance(value, str):
            return None

        try:
            setattr(self.bnode, param, 'ERROR')

        except TypeError as e:
            msg = str(e)
            i = msg.find('enum "ERROR" not found in')
            if i <= 0:
                return None

            vals = eval(msg[i+26:])
            # Only one possible value : ('VALUE') is evaluated as a str, not a singleton of a str
            if isinstance(vals, str):
                vals = (vals,)
            return vals

        return None

    # =============================================================================================================================
    # Get socket info

    def get_socket_info(self, name, halt=True):
        info = {}
        all = []

        inputs = self.bnode.inputs

        if isinstance(name, int) or (name.isnumeric() and not name in inputs):
            bsockets = [inputs[int(name)]]
        else:
            bsockets = []
            for bsocket in inputs:
                if bsocket.name.lower() == name.lower():
                    bsockets.append(bsocket)

        if len(bsockets) == 0:
            if halt:
                raise Exception(f"Socket {name} not found in node '{self.bnode.name}', inputs: {[bs.name for bs in inputs]}")
            return None

        elif len(bsockets) == 1:
            bsocket = bsockets[0]
            return {'name': bsocket.name, 'class': constants.CLASS_NAMES[bsocket.type]}

        else:
            classes = set()
            for bsocket in bsockets:
                classes.add(constants.CLASS_NAMES[bsocket.type])

            if len(classes) == 1:
                return {'name': bsockets[0].name, 'class': list(classes)[0]}
            else:
                return {'name': bsockets[0].name, 'class': 'variable', 'classes': list(classes)}

    # =============================================================================================================================
    # Source code generation

    # -----------------------------------------------------------------------------------------------------------------------------
    # Default self socket

    @property
    def default_self_socket(self):
        """ The default self socket

        if default socket for self if the first enabled input socket

        Returns
        -------
        - str : name of the first input socket
        """

        for bsock in self.bnode.inputs:
            if bsock.enabled:
                return bsock.name

        return None

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sockets

    def get_sockets(self, self_socket=None, expose_selection=True, ignore_sockets=[]):

        in_sockets = {}
        counter    = {}
        header     = []
        ok_self    = True
        arg_help   = []
        info_help  = []

        for sock_name in ignore_sockets:
            if not sock_name in self.bnode.inputs.keys():
                raise Exception(f"Socket '{sock_name}' doesn't exist in node '{self.bnode.name}': {list(self.bnode.inputs.keys())}")

        for bsocket in self.bnode.inputs:

            if not bsocket.enabled or bsocket.type == 'CUSTOM':
                continue

            if bsocket.name == self_socket and ok_self:
                if bsocket.type == 'GEOMETRY':
                    in_sockets[self_socket] = 'self._geo'
                else:
                    in_sockets[self_socket] = 'self'
                ok_self = False

                #arg_help.append(f"self : socket {bsocket.name} ({bsocket.identifier})")
                info_help.append(f"Socket '{bsocket.name}' : self")

            elif bsocket.name == 'Selection' and not expose_selection:
                in_sockets['Selection'] = 'self._sel'
                #arg_help.append(f"[...] : socket 'Selection' ({bsocket.identifier})")
                info_help.append("Socket 'Selection' : self[selection]")

            elif bsocket.name in ignore_sockets:
                info_help.append(f"Socket '{bsocket.name}' : ignored")

            else:
                pyname = utils.socket_name(bsocket.name)
                if pyname in counter:
                    counter[pyname] += 1
                    pyname += f"_{counter[pyname]}"

                elif pyname in self.params.keys():
                    if pyname in counter:
                        counter[pyname] += 1
                    else:
                        counter[pyname] = 1
                    pyname += f"_{counter[pyname]}"

                else:
                    counter[pyname] = 0

                in_sockets[bsocket.identifier] = pyname
                header.append(pyname)

                # Comment
                socket_type = constants.CLASS_NAMES[bsocket.type]
                #arg_help.append(f"{pyname} ({socket_type}) : socket '{bsocket.name}' ({bsocket.identifier})")
                arg_help.append(f"{pyname} ({socket_type}) : socket '{bsocket.name}' (id: '{bsocket.identifier}')")

        return {
            'has_items'  : len(in_sockets) > 0,
            'in_sockets' : in_sockets,
            'header'     : header,
            'header_str' : ", ".join([f"{pyname}=None" for pyname in header]),
            'call_str'   : "{" + ", ".join([f"'{socket_name}': {pyname}" for socket_name, pyname in in_sockets.items()]) + "}",
            'arg_help'   : arg_help,
            'info_help'  : info_help,
        }

    # -----------------------------------------------------------------------------------------------------------------------------
    # Parameters

    def get_parameters(self, **parameters):

        header    = []
        call      = []
        arg_help  = []
        info_help = []

        for param in parameters.keys():
            if param not in self.params.keys():
                raise Exception(f"Parameter '{param}' not found in node '{self.bnode.name}' parameters: {list(self.params.keys())}")

        for param, param_value in self.params.items():

            forced = param in parameters
            value = parameters[param] if forced else param_value

            str_value : str
            if isinstance(value, str):
                str_value = f"'{value}'"
            elif str(value)[0] == '<':
                str_value = "None"
            else:
                str_value = str(value)

            if forced:
                param_value = str_value
            else:
                header.append(f"{param}={str_value}")
                param_value = param

            if param == 'object' and self.btree.bl_idname == 'ShaderNodeTree':
                call.append(f"{param}=get_object({param_value})")
            else:
                call.append(f"{param}={param_value}")

            if forced:
                info_help.append(f"Parameter {param} : {str_value}")
            else:
                if param in self.enum_params:
                    arg_help.append(f"{param} (str): parameter '{param}' in {self.enum_params[param]}")
                else:
                    arg_help.append(f"{param} ({type(value).__name__}): parameter '{param}'")

        return {
            'has_items'  : len(header) > 0,
            'header_str' : ', '.join(header),
            'call_str'   : ', '.join(call),
            'arg_help'   : arg_help,
            'info_help'  : info_help,
        }

    # -----------------------------------------------------------------------------------------------------------------------------
    # Signature

    def signature(self, method_type='CLASS', self_socket=None, expose_selection=True, ignore_sockets=[], **parameters):
        """ Signature

        Arguments
        ---------
        - method_type (str = 'CLASS') : str in ('METHOD', 'PROPERTY_SET', 'PROPERTY_GET', 'CLASS', 'CLASS_PROPERTY', 'STATIC')
        - self_socket (str = None) : socket name for methods or 'AUTO' for the first input socket
        - expose_selection (bool = True) : expose the 'Selection' socket if exists
        - ignore_sockets (list of str = []) : list of sockets to ignore
        - parameters : parameter names and values to set

        Returns
        -------
        - str : the call function signature
        """

        if self_socket == 'AUTO':
            self_socket = self.default_self_socket

        sockets = self.get_sockets(self_socket=self_socket, expose_selection=expose_selection, ignore_sockets=ignore_sockets)
        params  = self.get_parameters(**parameters)

        items = []
        if method_type in ['METHOD', 'PROPERTY_SET', 'PROPERTY_GET']:
            items.append("self")
        elif method_type in ['CLASS', 'CLASS_PROPERTY']:
            items.append("cls")
        elif method_type == 'STATIC':
            pass
        else:
            raise Exception(f"Unknown method_type '{method_type}'")

        if self.has_items:
            items.append("_items={}")

        if sockets['has_items']:
            items.append(sockets['header_str'])

        if params['has_items']:
            items.append(params['header_str'])

        return "(" + ", ".join(items) + ")"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Node init

    def node_call(self, method_type='CLASS', self_socket=None, expose_selection=True, node_class='Node', ignore_sockets=[], **parameters):

        if self_socket == 'AUTO':
            self_socket = self.default_self_socket

        sockets = self.get_sockets(self_socket=self_socket, expose_selection=expose_selection, ignore_sockets=ignore_sockets)
        params  = self.get_parameters(**parameters)

        s = f"{node_class}('{self.bnode.name}'"

        if sockets['has_items']:
            s += ", " + sockets['call_str']

        if self.has_items:
            s += ", _items=_items"

        if params['has_items']:
            s += ", " + params['call_str']

        return s + ")"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Comment

    def comment(self, method_type='CLASS', self_socket=None, expose_selection=True, returns='NODE', ignore_sockets=[], **parameters):
        """ Generate method comment
        """

        if method_type == 'PROPERTY_SET':
            return "\n"

        if self_socket == 'AUTO':
            self_socket = self.default_self_socket

        _tab = " "*4
        c3 = '"""'

        sockets = self.get_sockets(self_socket=self_socket, expose_selection=expose_selection, ignore_sockets=ignore_sockets)
        params  = self.get_parameters(**parameters)

        snode = "ShaderNode" if self.is_shader else "Node"
        s = f"{_tab*2}{c3} > Node <&{snode} {self.bnode.name}>"

        if self.is_shader:
            s += f"\n\n{_tab*2}[&SHADER]"

        if returns == 'JUMP':
            s += f"\n\n{_tab*2}[&JUMP]"

        if sockets['info_help'] or params['info_help']:
            s += f"\n\n{_tab*2}Notes"
            s += f"\n{_tab*2}-----"
            for line in sockets['info_help']:
                s += f"\n{_tab*2}- {line}"
            for line in params['info_help']:
                s += f"\n{_tab*2}- {line}"

        if sockets['has_items'] or params['has_items'] or self.has_items:
            s += f"\n\n{_tab*2}Arguments"
            s += f"\n{_tab*2}---------"

            if self.has_items:
                s += f"\n{_tab*2}- items (dict) : items to create"

            for line in sockets['arg_help']:
                s += f"\n{_tab*2}- {line}"

            for line in params['arg_help']:
                s += f"\n{_tab*2}- {line}"

        if returns != 'NONE' or len(self.bnode.outputs):
            s += f"\n\n{_tab*2}Returns"
            s += f"\n{_tab*2}-------"

            s += f"\n{_tab*2}- "

            if returns == 'NODE':
                s += f"Node : '{self.bnode.name}'"

            else:
                bsocket = self.bnode.outputs[0]
                if bsocket.type != 'CUSTOM':
                    out_socket = constants.CLASS_NAMES[self.bnode.outputs[0].type]
                    s += out_socket
                    if returns == 'JUMP':
                        s += ": self"
                else:
                    s += "None"

        return s + f"\n{_tab*2}{c3}\n"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Source code

    def source_code(self, method_type='CLASS', self_socket=None, expose_selection=True, returns='NODE',
        func_name=None, node_class='Node', ignore_sockets=[], **parameters):
        """ Generate the source code

        Arguments
        ---------
        - method_type (str = 'CLASS') : str in ('METHOD', 'PROPERTY_SET', 'PROPERTY_GET', 'CLASS', 'CLASS_PROPERTY', 'STATIC')
        - self_socket (str = None) : socket name for methods or 'AUTO' for the first input socket
        - expose_selection (bool = True) : expose the 'Selection' socket if exists
        - returns (str = 'NODE') : str in ('NONE', 'NODE', 'OUT', 'JUMP')
        - func_name (str = None) : replace the default function name
        - node_class (str = 'Node') : Node or name of a sub class of Node
        - ignore_sockets (list of str = []) : list of sockets to ignore
        - parameters : parameter names and values to set
        """

        _tab = " "*4

        # ----- Adjust arguments

        if self_socket == 'AUTO':
            self_socket = self.default_self_socket

        if func_name is None:
            func_name = utils.socket_name(self.bnode.name)

        # ----- Main items

        signature = self.signature(method_type=method_type, self_socket=self_socket, expose_selection=expose_selection,
            ignore_sockets=ignore_sockets, **parameters)

        comment = self.comment(method_type=method_type, self_socket=self_socket, expose_selection=expose_selection, returns=returns,
            ignore_sockets=ignore_sockets, **parameters)

        node_call = self.node_call(method_type=method_type, self_socket=self_socket, expose_selection=expose_selection,
            node_class=node_class, ignore_sockets=ignore_sockets, **parameters)

        # ----- Prefix

        s = ""
        if method_type == 'METHOD':
            pass
        elif method_type == 'PROPERTY_GET':
            s = f"{_tab}@property\n"
        elif method_type == 'PROPERTY_SET':
            s = f"{_tab}@{func_name}.setter\n"
        elif method_type == 'CLASS':
            s = f"{_tab}@classmethod\n"
        elif method_type == 'CLASS_PROPERTY':
            s = f"{_tab}@classmethod\n"
            s += f"{_tab}@property\n"
        elif method_type == 'STATIC':
            s = f"{_tab}@staticmethod\n"
        else:
            raise Exception(f"Unknown method_type '{method_type}'")

        # ----- Function declaration

        s += f"{_tab}def {func_name}{signature}:\n"

        # ----- Comment

        s += comment

        # ----- Node call

        s += f"{_tab*2}node = {node_call}\n"

        # ----- Return

        s += f"{_tab*2}return "
        if returns == 'NODE':
            s += "node"
        elif returns == 'JUMP':
            s += "self._jump(node._out)"
        else:
            s += "node._out"

        # ----- Done

        return s + "\n\n"

    def class_method_code(self, returns='NODE', func_name=None, node_class='Node', ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         ='CLASS',
            returns             = returns,
            func_name           = func_name,
            node_class          = node_class,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def class_property_code(self, returns='OUT', func_name=None, node_class='Node', ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'CLASS_PROPERTY',
            returns             = returns,
            func_name           = func_name,
            node_class          = node_class,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def method_code(self, self_socket='AUTO', expose_selection=False, returns='OUT', func_name=None, node_class='Node',
        ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'METHOD',
            self_socket         = self_socket,
            expose_selection    = expose_selection,
            returns             = returns,
            func_name           = func_name,
            node_class          = node_class,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def property_get_code(self, self_socket='AUTO', expose_selection=False, returns='OUT', func_name=None, node_class='Node', ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'PROPERTY_GET',
            self_socket         = self_socket,
            expose_selection    = expose_selection,
            returns             = returns,
            func_name           = func_name,
            node_class          = node_class,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def property_set_code(self, self_socket='AUTO', expose_selection=False, returns='JUMP', func_name=None, node_class='Node', ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'PROPERTY_SET',
            self_socket         = self_socket,
            expose_selection    = expose_selection,
            returns             = returns,
            func_name           = func_name,
            node_class          = node_class,
            ignore_sockets      = ignore_sockets,
            **parameters)



    # -----------------------------------------------------------------------------------------------------------------------------
    # Comment

    def yield_comment(self):

        _tab = " "*4
        c3 = '"""'

        sockets = self.get_sockets()
        params  = self.get_parameters()

        snode = "ShaderNode" if self.is_shader else "Node"
        yield f"\n\n{_tab*2}{c3} > Node <&{snode} {self.bnode.name}>"

        if self.is_shader:
            yield f"\n\n{_tab*2}[&SHADER]"

        if sockets['has_items'] or params['has_items'] or self.has_items:
            yield f"\n\n{_tab*2}Arguments"
            yield f"\n{_tab*2}---------"

            if self.has_items:
                yield f"\n{_tab*2}- items (dict) : items to create"

            for line in sockets['arg_help']:
                yield f"\n{_tab*2}- {line}"

            for line in params['arg_help']:
                yield f"\n{_tab*2}- {line}"

        if len(self.bnode.outputs):
            yield f"\n\n{_tab*2}Returns"
            yield f"\n{_tab*2}-------"

            bsocket = self.bnode.outputs[0]
            if bsocket.type != 'CUSTOM':
                out_socket = constants.CLASS_NAMES[self.bnode.outputs[0].type]
                yield f"\n{_tab*2}- {out_socket}"
            else:
                yield f"\n{_tab*2}- None"

        yield f"\n{_tab*2}{c3}\n\n"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Static source

    def yield_static_source(self, func_name=None, as_class_method=True):
        _tab = " "*4

        if func_name is None:
            func_name = self.python_name

        sockets = self.get_sockets()
        params  = self.get_parameters()

        # ----------------------------------------------------------------------------------------------------
        # Decorators

        if as_class_method:
            yield f"{_tab}@classmethod\n"
            if self.global_is_prop:
                yield f"{_tab}@property\n"
        else:
            yield f"{_tab}@staticmethod\n"

        # ----------------------------------------------------------------------------------------------------
        # Header

        yield f"{_tab}def {func_name}("
        use_sepa = False
        if as_class_method:
            yield 'cls'
            use_sepa = True

        if self.has_items:
            if use_sepa:
                yield ", "
            yield "_items={}"
            use_sepa=True

        if sockets['has_items']:
            if use_sepa:
                yield ", "
            yield sockets['header_str']
            use_sepa = True

        if params['has_items']:
            if use_sepa:
                yield ", "
            yield params['header_str']
            use_sepa = True

        yield "):\n"

        # ----------------------------------------------------------------------------------------------------
        # Comment

        for line in self.yield_comment():
            yield line

        # ----------------------------------------------------------------------------------------------------
        # Node call

        yield f"{_tab*2}node = Node('{self.bnode.name}'"

        if sockets['has_items']:
            yield ", " + sockets['call_str']

        if self.has_items:
            yield ", _items=_items"

        if params['has_items']:
            yield ", " + params['call_str']

        yield ")\n"

        # ----------------------------------------------------------------------------------------------------
        # Return

        yield f"{_tab*2}return node._out\n\n"

    # ====================================================================================================
    # Method Source Code

    def gen_method_source(self, name=None, self_socket=None, return_node=False):
        _tab = " "*4

        if name is None:
            name = self.python_name

        # ----------------------------------------------------------------------------------------------------
        # Header

        if self_socket is None:
            yield f"{_tab}@classmethod\n"
            yield f"{_tab}def {name}(cls"
        else:
            yield f"{_tab}def {name}(self"

        insockets = {}
        for bsocket in self.bnode.inputs:
            if bsocket.enabled and bsocket.type != 'CUSTOM':
                if bsocket.name == self_socket:
                    if bsocket.type == 'GEOMETRY':
                        insockets[self_socket] = 'self._geo'
                    else:
                        insockets[self_socket] = 'self'
                elif bsocket.name == 'Selection':
                    insockets['Selection'] = 'self._sel'
                else:
                    pyname = utils.socket_name(bsocket.name)
                    insockets[bsocket.name] = pyname
                    yield f", {pyname}=None"

        for param, value in self.params.items():
            if isinstance(value, str):
                yield f", {param}='{value}'"
            else:
                yield f", {param}={value}"

        yield "):\n"

        # ----------------------------------------------------------------------------------------------------
        # Comments

        sockets = self.get_sockets()
        params  = self.get_parameters()

        if True:
            for line in self.yield_comment():
                yield line

        else:
            c3 = '"""'

            yield f"{_tab*2}{c3} Node '{self.bnode.name}' ({self.bnode.bl_idname})"

            yield f"\n\n{_tab*2}<&NODE {self.bnode.name}>"

            if sockets['has_items'] or params['has_items']:
                yield f"\n\n{_tab*2}Arguments"
                yield f"\n{_tab*2}---------"
                for line in sockets['arg_help']:
                    yield f"\n{_tab*2}- {line}"
                for line in params['arg_help']:
                    yield f"\n{_tab*2}- {line}"

            if len(self.bnode.outputs):
                yield f"\n\n{_tab*2}Returns"
                yield f"\n{_tab*2}-------"

                out_sockets = [f"{utils.socket_name(bsocket.name)} ({constants.CLASS_NAMES[bsocket.type]})" for bsocket in self.bnode.outputs if bsocket.type != 'CUSTOM']
                if return_node:
                    yield f"\n{_tab*2}- Node: [{', '.join(out_sockets)}]"
                elif len(out_sockets):
                    yield f"\n{_tab*2}- {out_sockets[0]}"

            yield f"\n{_tab*2}{c3}\n\n"

        # ----------------------------------------------------------------------------------------------------
        # Node call

        yield f"{_tab*2}node = Node('{self.bnode.name}'"

        if len(insockets):
            yield ", {" + ", ".join([f"'{socket_name}': {pyname}" for socket_name, pyname in insockets.items()]) + "}"

        for param in self.params.keys():
            yield f", {param}={param}"

        yield ")\n"
        if return_node:
            yield f"{_tab*2}return node\n\n"
        else:
            if True:
                yield f"{_tab*2}return node._out\n\n"
            else:
                count = 0
                out_name = None
                for bsocket in self.bnode.outputs:
                    if bsocket.enabled:
                        if count == 0:
                            count = 1
                            out_name = utils.socket_name(bsocket.name)
                        else:
                            if count == 1:
                                yield f"{_tab*2}{out_name} = node._out\n"
                            attr_name = utils.socket_name(bsocket.name)
                            yield f"{_tab*2}{out_name}.{attr_name}_ = node.{attr_name}\n"

                if count == 1:
                    yield f"{_tab*2}return node._out\n\n"
                else:
                    yield f"{_tab*2}return {out_name}\n\n"

    # ====================================================================================================
    # Sort the nodes

    @staticmethod
    def sort_nodes(tree_name="Temp"):

        node_infos = {
            'INPUT'             : [],
            'DOMAIN'            : [],
            'DATA_TYPE'         : [],
            'ENUMS'             : [],
            'PARAMS'            : [],
            'OTHER'             : [],
        }

        btree = blendertree.get_tree("Temp", create=True)
        btree.nodes.clear()

        for type_name in dir(bpy.types):

            try:
                bnode = btree.nodes.new(type=type_name)
            except RuntimeError as e:
                continue

            if 'legacy' in bnode.name.lower():
                continue

            node_info = NodeInfo(btree, bnode)

            if node_info.in_sockets_count == 0:
                node_infos['INPUT'].append(node_info)
            elif 'domain' in node_info.enum_params.keys():
                node_infos['DOMAIN'].append(node_info)
            elif 'data_type' in node_info.enum_params.keys():
                node_infos['DATA_TYPE'].append(node_info)
            elif len(node_info.enum_params):
                node_infos['ENUMS'].append(node_info)
            elif len(node_info.params):
                node_infos['PARAMS'].append(node_info)
            else:
                node_infos['OTHER'].append(node_info)

        for cat, nodes in node_infos.items():
            print("="*50)
            print(cat)
            for ni in nodes:
                print("   ", ni)

        blendertree.del_tree(btree)

# =============================================================================================================================
# Loop

def loop_on_nodes(func, *args, tree_type='GeometryNodeTree', **kwargs):

    btree = blendertree.get_tree("Temp", tree_type=tree_type, create=True)
    btree.nodes.clear()

    count = 0

    for type_name in dir(bpy.types):

        try:
            bnode = btree.nodes.new(type=type_name)
        except RuntimeError as e:
            continue

        if 'legacy' in bnode.name.lower():
            continue

        node_info = NodeInfo(btree, bnode)

        func(node_info, *args, **kwargs)

        count += 1

    blendertree.del_tree(btree)

    return count

# =============================================================================================================================
# Get the sockets types

def gen_socket_types(tree_type='GeometryNodeTree'):
    def get_types(node_info, types):
        for bsocket in node_info.bnode.inputs:
            types.add(bsocket.type)
        for bsocket in node_info.bnode.outputs:
            types.add(bsocket.type)

    types = set()
    count = loop_on_nodes(get_types, types, tree_type=tree_type)

    print("Socket types:")
    pprint(types)

# =============================================================================================================================
# Get the sockets types

def gen_nodes_with_items(tree_type='GeometryNodeTree'):

    # ---------------------------------------------------------------------------
    # Loop function

    def get_types(node_info, nodes):
        if node_info.has_items:
            name = node_info.items_prop
            items = getattr(node_info.bnode, name)
            try:
                sig = inspect.signature(items.new)
            except Exception as e:
                sig = str(e)
            nodes[node_info.bnode.name] = f"{name}: {sig}"

    nodes = {}
    loop_on_nodes(get_types, nodes, tree_type=tree_type)

    print("Dynamic nodes with items:")
    pprint(nodes)


# =============================================================================================================================
# Gen global functions

def gen_global_functions(tree_type='GeometryNodeTree', folder=''):

    # ----------------------------------------------------------------------------------------------------
    # The function called for each node

    def gen_node(node_info, f):
        for chars in node_info.yield_static_source():
            f.write(chars)
        f.write("\n")

    # ----------------------------------------------------------------------------------------------------
    # Main

    path = Path(folder) / Path('AUTO global functions.py')
    path.resolve()
    with open(path, 'w') as f:
        f.write("class StaticNodes:\n\n")
        count = loop_on_nodes(gen_node, f, tree_type=tree_type)
        f.write("\n\n")

    print(f"Global functions written ({count} methods or properties) in: '{path.absolute()}'")

# =============================================================================================================================
# Gen node

def gen_node_code(btree, node_name=None, self_socket=None, return_node=False):

    bl_idname = constants.NODE_NAMES[btree.bl_idname][node_name.lower()]

    bnode = None
    for nd in btree.nodes:
        if nd.bl_idname == bl_idname:
            bnode = nd
            break

    if bnode is None:
        bnode = btree.nodes.new(bl_idname)

    print("Node", node_name)
    print("-"*100)

    node_info = NodeInfo(btree, bnode)
    for line in node_info.gen_method_source(name=None, self_socket=self_socket, return_node=return_node):
        print(line, end='')

    print("-"*100)

# =============================================================================================================================
# Gen comment

def gen_node_comment(btree, node_name=None, self_socket=None, return_node=False):

    bl_idname = constants.NODE_NAMES[btree.bl_idname][node_name.lower()]

    bnode = None
    for nd in btree.nodes:
        if nd.bl_idname == bl_idname:
            bnode = nd
            break

    if bnode is None:
        bnode = btree.nodes.new(bl_idname)

    print("Node", node_name)
    print("-"*100)
    node_info = NodeInfo(btree, bnode)
    for line in node_info.yield_comment():
        print(line, end='')
    print("-"*100)









class OLD:

    def old(self):

        # ----------------------------------------------------------------------------------------------------
        # Sockets

        self.inputs      = Sockets(self, True)
        self.outputs     = Sockets(self, False)

        self.dynamic_in  = self.inputs.has_virtual  or self.bl_idname in constants.CUSTOM_INPUT_SOCKETS
        self.dynamic_out = self.outputs.has_virtual or self.bl_idname in constants.CUSTOM_OUTPUT_SOCKETS

        # Has a multi input socket

        self.has_multi_input = False
        for bsock in bnode.inputs:
            if bsock.is_multi_input:
                self.has_multi_input = True
                self.mi_bsocket = bsock
                self.mi_pyname = utils.socket_name(bsock.name)
                break

        # ----------------------------------------------------------------------------------------------------
        # DEBUG

        if False and self.class_name in ['Vector']:
            print("NodeInfo.__init__", self.tree_type, self.class_name)
            for bsocket in [bs for bs in self.inputs.bsockets] + [bs for bs in self.outputs.bsockets]:
                print(f"   - {bsocket.bl_idname}, {bsocket.type}, {bsocket.name}")

        # ----------------------------------------------------------------------------------------------------
        # Parameters

        self.analyze_parameters()

        # ====================================================================================================
        # Node attributes

        self.node_attrs = {} # For documentation
        self.node_args  = Arguments(is_static=False)
        if self.has_multi_input:
            self.node_args.add('*args', NO_VALUE)
            init_header  = "self, *args"
            sockets_init = "\n\tself._set_multi_input(*args)"
        else:
            init_header  = "self"
            sockets_init = ""

        # ----- Input sockets

        for root_name, count in self.in_counts.items():

            # ---- Socket name can collide with param name

            suffix = '_' if root_name in self.params else ''

            for rank in range(count):

                pyname = root_name + suffix if rank == 0 else f"{root_name}_{rank}"

                # ----- Socket argument

                sarg_name = pyname
                sarg_val  = pyname

                #if self.has_socket_method and root_name == self.sm_pyname:
                if False:
                    if rank == 0:
                        sarg_name = None
                        sarg_val  = "self"
                    else:
                        sarg_name = root_name if rank == 1 else f"{root_name}_{rank-1}"
                        sarg_val  = sarg_name

                # ----- Attribute info

                self.node_attrs[pyname] = {
                    'type'       : 'Input socket',
                    'sarg_name'  : sarg_name,
                    'sarg_val'   : sarg_val,
                    'argument'   : True,
                    'getter'     : None,
                    'setter'     : utils.setter(f"self._set_input_socket('{pyname}', value)", pyname),
                    'rank'       : rank,
                    'is_multi'   : self.has_multi_input and self.mi_pyname == pyname,
                    'descr'      : f"Input socket",
                    }
                if self.node_attrs[pyname]['is_multi']:
                    self.node_attrs[pyname]['descr'] += " (multi input)"

                # ----- Node argument and init code

                self.node_args.add(pyname, None, descr=self.node_attrs[pyname]['descr'])
                init_header  += f", {pyname}=None"
                sockets_init += f"\n\tself.{pyname:15s} = {pyname}"

        # ----- Output sockets

        params_init = ""

        for root_name, count in self.out_counts.items():
            for rank in range(count):

                pyname = root_name if rank == 0 else f"{root_name}_{rank}"

                getter = utils.getter(f"return self._get_output_socket('{pyname}')", pyname)

                if pyname in self.node_attrs:
                    self.node_attrs[pyname]['getter'] = getter
                    self.node_attrs[pyname]['descr'] = "Input / output socket"

                else:
                    self.node_attrs[pyname] = {
                        'type'       : 'Output socket',
                        'argument'   : False,
                        'getter'     : getter,
                        'setter'     : None,
                        'rank'       : rank,
                        'descr'      : "Output socket"
                        }

        # ----- Params

        for param in self.params:
            value = self.prm_defs[param]
            self.node_attrs[param] = {
                'type'      : 'Parameter',
                'argument'  : True,
                'default'   : utils.python_constant(value),
                'getter'    : utils.getter(f"return self._get_parameter('{param}')", param),
                'setter'    : utils.setter(f"self._set_parameter('{param}', value)", param),
                'descr'     : f"Node parameter, default {utils.python_constant(value)}"
                }

            # Node argument and init code

            self.node_args.add(param, value, descr=self.node_attrs[param]['descr'])
            init_header += f", {param}={utils.python_constant(value, keep_lower=False)}"
            params_init += f"\n\tself.{param:15s} = {param}"

        # ----- Source code
        # Sockets can change their name with some parameter
        # The new name can be set in **kwargs
        # All the init is done in root class Node but multi input initialization

        call_code = self.node_args.node_init_kwargs
        if call_code != "":
            call_code += ", "

        self.init_code  = f"def __init__({init_header}, node_label=None, node_color=None, **kwargs):\n"
        self.init_code += f"\n\tNode.__init__(self, '{self.bl_idname}', {call_code} node_label=node_label, node_color=node_color, **kwargs)\n"
        if self.has_multi_input:
            self.init_code += "\n\tself._set_multi_input(*args)\n"
        self.init_code += "\n"

        try:
            self.compiled_init = utils.compile_f(self.init_code, '__init__', {'Node': treestack.Node})
        except:
            raise NodeError(f"Node {self.class_name}: error in compiling '__init__', see code below.", self.init_code)

        # ----- DEBUG

        if False and self.class_name == "AxesToRotation":
            print("-"*100)
            print("NodeInfo.init", self.class_name, "__init__ source code\n")
            print(self.init_code)
            print("Arguments")
            print("---------")
            print(self.node_args)
            print()
            print("Arguments doc")
            print("-------------")
            print(self.node_args.docs)
            print()

            print("Individual arg doc")
            print("------------------")
            for arg in self.node_args.args:
                print(arg.doc)
            print()

            print("Arguments header and call")
            print("-------------------------")

            for arg in self.node_args.args:
                print("   arg", arg)
                print(arg.header)
                print(arg.call)
            print()

            #assert(False)


    # =============================================================================================================================
    # Check the used sockets types

    def check_socket_bl_idnames(self, unknwon):
        """ Check if new socket types have been added since the last Blender version.

        The passerd argument 'unknown' is a dictionary {bl_idname: type} of unknown sockets.

        Arguments
        ---------
            - unknown (dict)
        """

        bsockets = [bs for bs in self.bnode.inputs] + [bs for bs in self.bnode.outputs]
        for bsocket in bsockets:
            if bsocket.bl_idname in constants.BL_ID_SOCKET_TO_TYPE[self.tree_type]:
                continue
            if bsocket.bl_idname in unknwon:
                continue
            unknwon[bsocket.bl_idname] = bsocket.type

    # ====================================================================================================
    # Utility

    @property
    def is_geonodes(self):
        return self.tree_type == 'GeometryNodeTree'

    # ====================================================================================================
    # Detailed info

    def __repr__(self):
        tab = "   "
        s  = f"Node {self.name}, python name: {self.python_name}, class name: {self.class_name}\n"
        s += "\nParameters"
        s += "\n----------"
        if len(self.params) == 0:
            s += "\n{tab}None"
        else:
            for k, v  in self.prm_defs.items():
                s += f"\n{tab}{k:12s} = {v}"
        s += "\n"

        s += "\nInput sockets"
        s += "\n-------------"
        for sck in self.inputs:
            s += f"\n{tab}{sck[0]:12s} {'X' if sck[1] else '-'} {sck[2]}"
        s += "\n"

        s += "\nOutput sockets"
        s += "\n--------------"
        for sck in self.outputs:
            s += f"\n{tab}{sck[0]:12s} {'X' if sck[1] else '-'} {sck[2]}"
        s += "\n"

        return s



    def reset_params(self):
        """ Restore the node parameters to their default value.
        """

        for param, value in self.prm_defs.items():
            setattr(self.bnode, param, value)

    def analyze_parameters(self):
        """ Analyzes the parameters of the node.
        """

        # ----- Max number of sockets per name

        self.in_counts  = self.inputs.enabled_counts()
        self.out_counts = self.outputs.enabled_counts(ignore_disabled=self.bl_idname in constants.INCLUDE_HIDDEN_OUTPUT_SOCKETS)

        self.max_in  = sum(self.in_counts.values())
        self.max_out = sum(self.out_counts.values())

        # ----- Parameters and default value

        self.params   = [name for name in dir(self.bnode) if name not in constants.STANDARD_NODE_ATTRS]
        self.prm_defs = {name: getattr(self.bnode, name) for name in self.params}

        # ----- Parameters in enum

        self.enum_params   = {}
        self.domain_param  = None
        self.domain_values = None
        for param in self.params:
            enums = self.get_enum_list(param)
            if enums is not None:
                self.enum_params[param] = enums

                # ----- Do we have a domain parameter ?
                c = 0
                for dom in ['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE']:
                    for e in enums:
                        if dom in e:
                            c += 1
                            if c == 2:
                                self.domain_param  = param
                                self.domain_values = enums
                                break

                    if self.domain_param is not None:
                        #self.domain_values = enums
                        break

        # ----- DEBUG

        if False and self.class_name in ['ExtrudeMesh']:
            print('-'*30)
            print(self.class_name)
            print(self.domain_param, self.domain_values)
            #pprint(self.enum_params)

        # ----- Several enum params
        # Need to sort them

        self.driver_params = []
        for param, values in self.enum_params.items():
            for value in values:

                setattr(self.bnode, param, value)

                self.inputs.enabled_counts(self.in_counts)
                self.outputs.enabled_counts(self.out_counts)

                self.max_in  = max(self.max_in , sum(self.in_counts.values()))
                self.max_out = max(self.max_out, sum(self.out_counts.values()))

                changed = False
                for prm, vals in self.enum_params.items():
                    if prm == param:
                        continue
                    new_enums = self.get_enum_list(prm)
                    if new_enums != vals:
                        self.driver_params.append(param)
                        changed = True
                        break
                if changed:
                    break

            #print("PRM DEFS", self.prm_defs)
            #print(f"PARAM: '{param}': <{self.prm_defs.get(param, 'OUPS')}>")

            if self.prm_defs[param] != "":
                setattr(self.bnode, param, self.prm_defs[param])


        if len(self.driver_params):
            old_params = self.params
            self.params = list(self.driver_params)
            for param in old_params:
                if param not in self.driver_params:
                    self.params.append(param)

        # ----- data type special case

        if False and 'data_type' in self.params:
            count = len(self.get_enum_list('data_type'))
            counts = self.inputs.names_counts()

            print(self.class_name, "DATA_TYPE", count)
            pprint(counts)
            print()

    # =============================================================================================================================
    # Config the node

    def setup(self, **kwargs):
        """ Setup the parameters of the node with a number of values.

        Arguments
        ---------
            - kwargs : parameter name, value to apply to the node
        """

        mems = {}
        for param in self.params:
            if param in kwargs:
                mems[param] = getattr(self.bnode, param)
                setattr(self.bnode, param, kwargs[param])
        return mems

    # =============================================================================================================================
    # Get the args and call_args list

    def build_meth_args(self,
                  self_socket = None,  # Which socket to set with self
                  all_sockets = True,  # Use all the sockets (True) or the current node config (False)
                  node_label  = True,  # Add node_label and node_color
                  use_args    = False, # Use *args in header
                  **kwargs):           # Fixed node arguments

        """ Build the arguments list.

        if the argument 'self_socket' is None, the Arguments list is initialized as static

        Arguments
        ---------
            - self_socket (str = None) : Name of the socket to plug self (is excluded from argument list)
            - use_enabled (bool = False) : compute the current count per socket if True else get node.max_per_name
            - node_label (bool = True) : add node_label and node_color arguments
            - use_args (bool=False) : use *args
            - kwargs : Fixed arguments

        Returns
        -------
            - Arguments
        """

        # ----------------------------------------------------------------------------------------------------
        # Lists initialization

        args = Arguments(self_socket is None)

        if self_socket == 'ARG0':
            args.add('self', IGNORE, NO_VALUE)

        if self.has_multi_input or use_args:
            args.add("*args", NO_VALUE, NO_VALUE)

        # ----------------------------------------------------------------------------------------------------
        # Set up the node

        prm_defs  = {**self.prm_defs}
        prm_vals  = {}
        prm_enums = {}

        # ----- Change parameters

        if all_sockets:
            in_counts = {**self.in_counts}
        else:
            mems = self.setup(**kwargs)
            in_counts = self.inputs.enabled_counts()

        # Get node config
        prm_defs = {param: getattr(self.bnode, param) for param in self.params}

        # Param possible values
        for param in self.params:
            prm_enums[param] = self.get_enum_list(param)
            if param not in kwargs:
                prm_vals[param] = prm_enums[param]

        # ----- Restore parameters
        if not all_sockets:
            self.setup(**mems)

        # ----------------------------------------------------------------------------------------------------
        # Input sockets

        if len(in_counts) > 0:

            for sock_name in utils.input_sockets_order(in_counts):

                suffix = '_' if sock_name in self.params else ''

                descr = f"Socket"

                count = in_counts[sock_name]

                # ----- Socket where to plug self

                is_self_socket = sock_name == self_socket

                # ----- Loop on the sockets sharing the same name

                for i in range(count):

                    sock_i = sock_name + suffix if i == 0 else f"{sock_name}_{i}"

                    # ----- Socket name is for self
                    # Typical use
                    # def method(self, value, value_1, ...):
                    #     node = Node(value=self, value_1=value, value_2=value_1, ...)

                    if is_self_socket:
                        if i == 0:
                            if sock_name in kwargs:
                                args.add(sock_name, None, kwargs[sock_name], descr=descr)
                            elif count == 1:
                                args.add(sock_name, IGNORE, 'self', descr=descr)
                            else:
                                args.add(sock_name, None, 'self', descr=descr)

                        else:
                            sock_prev_i = sock_name if i == 1 else f"{sock_name}_{i-1}"
                            args.add(sock_i, None if i < count-1 else IGNORE, sock_prev_i, descr=descr)

                    # ----- Current socket is fixed in kwargs

                    elif sock_i in kwargs:
                        args.add(sock_i, None, kwargs[sock_i], descr=descr)

                    # ----- Nothing particular

                    else:
                        args.add(sock_i, None, descr=descr)

        # ----------------------------------------------------------------------------------------------------
        # Parameters

        for param in self.params:
            if param in kwargs:
                args.add(param, IGNORE, kwargs[param], enums=prm_enums[param])
            else:
                descr = f"Parameter"
                vals = prm_vals[param]
                if vals is not None:
                    descr += f" in {vals}"
                args.add(param, prm_defs[param], enums=prm_enums[param], descr=descr)

        # ----- Replace: domain = DEFAULT by domain = self._get_domain(DEFAULT)

        if self.domain_param is not None:
            arg = args[self.domain_param]
            if arg is not None:
                if arg.header == 'IGNORE':
                    pass
                elif arg.call is None:
                    arg.call = f"self._get_domain({arg.name}, {self.domain_values})"
                else:
                    arg.call = f"self._get_domain({arg.call}, {self.domain_values})"

        # ----------------------------------------------------------------------------------------------------
        # Node_label and node_color

        if node_label:
            args.add('node_label', None)
            args.add('node_color', None)

        # ----------------------------------------------------------------------------------------------------
        # Return the arguments

        return args

    # ====================================================================================================
    # Create the node class

    def create_node_class(self):
        """ Dynamically create the node class.

        To document the dynamic creation of Nodes, a Dynamic instance is created for the node.

        The Dynamic instance is store in the global list constants.NODES for further reference.

        The Dynamic instance contains:
            - a reference to self : dynamic.node_info
            - a reference to the Node class : dynamic.dyn_class

        Two attributes are created:
            - node_info.dynamic : the Dynamic instance
            - node_info.node_class : the Node class
        """

        root_class = treestack.Node
        gen_init   = True
        descr      = None

        if self.bl_idname == 'GeometryNodeIndexSwitch':
            root_class = treestack.IndexSwitchNode
            gen_init   = False
            descr      = root_class.__init__.__doc__
        elif  self.bl_idname == 'GeometryNodeMenuSwitch':
            root_class = treestack.MenuSwitchNode
            gen_init   = False
            descr      = root_class.__init__.__doc__

        self.dynamic = dynamic.Dynamic.NewNode(self, root_class, descr=documentation.left_translate(descr))
        descr = None

        # DEBUG

        if False and self.class_name == 'CombineColor':
            print(f"====== create_node_class {self.class_name}")
            print(self.init_code)
            print()

        if gen_init:
            self.dynamic.add_member('METHOD', '__init__', (self.init_code, self.compiled_init), None, args=self.node_args, descr=None)

        #self.dynamic.build_class()

        self.node_class = self.dynamic.dyn_class

        # ----- Some complementary attributes

        setattr(self.node_class, 'bl_idname',   self.bl_idname)
        setattr(self.node_class, 'params',      self.params)
        setattr(self.node_class, 'valid_inputs', self.node_args.key_names)
        setattr(self.node_class, 'dynamic_in',  self.dynamic_in)
        setattr(self.node_class, 'dynamic_out', self.dynamic_out)

        setattr(self.node_class, 'DOMAIN_PARAM',  self.domain_param)
        setattr(self.node_class, 'DOMAIN_VALUES', self.domain_values)

        # ----- Sockets and parameters properties

        for name, attr in self.node_attrs.items():
            fget = None if attr['getter'] is None else utils.compile_f(attr['getter'], name)
            fset = None if attr['setter'] is None else utils.compile_f(attr['setter'], name)
            setattr(self.node_class, name, property(fget, fset))

            #self.add_property(self.class_name, name, attr['getter'], attr['setter'], attr_type=attr['type'], descr=attr['descr'])

        # ----- Register the node class

        constants.NODES[self.tree_type][self.bl_idname] = self.dynamic


# ====================================================================================================
# Initialize a tree type

def tree_class_setup(tree_class):
    """ Set up the engine for a type of node tree.

    The structure of the engine is the following:
        - NodeClass
        - SocketClass
        - Global functions

    All of them are properties of the tree class, for instance:
        - Tree.Math : Node class 'Math'
        - Tree.GEOMETRY : Socket class 'GEOMETRY'
        - Tree.cos : function cos

    Tree, Node and Socket classes are generated and enriched thourgh Dynamic instances.
    Dynamic instances allow to managed the documentation of the generated objects.

    The setup is done with the following steps:
        - Initialization
            - create a Dynamic instance for the Tree class
            - create an instance of the require Blender tree
        - Loop on the nodes:
            - create an instance of NodeInfo for each possible Blender node in the tree
            - create the Dynamic instance for each Node
        - Loop on the existing sockets:
            - create the Dynamic instances for the sockets
        - Loop on the nodes:
            - Enrich the socket classes and the Tree class with Node implementations

    Arguments
    ---------
        - tree_class : a sub class of Tree with a valide TREE_TYPE attribute
    """

    # ====================================================================================================
    # Node and Socket classes

    tree_type = tree_class.TREE_TYPE
    sockets   = constants.SOCKETS[tree_type]

    # ----- Create the Tree Dynamic entry for documentation

    constants.TREES[tree_type] = dynamic.Dynamic.Tree(tree_class, descr=None)

    # ----------------------------------------------------------------------------------------------------
    # Create the node tree

    btree = treestack.get_tree("TREE - Temp", tree_type=tree_type, create=True, clear=True)

    # ----------------------------------------------------------------------------------------------------
    # Create all the possible nodes

    unknown_sockets = {}
    node_infos = []

    to_delete = []
    scene     = None

    for type_name in dir(bpy.types):

        # ----- Hack
        # CompositorNodeRLayers can't be set in a Group

        if type_name == 'CompositorNodeRLayers':
            if scene is None:
                scene = bpy.context.scene
                mem_un = scene.use_nodes
                scene.use_nodes = True

            bnode = None
            for bn in scene.node_tree.nodes:
                if bn.bl_idname == type_name:
                    bnode = bn
                    break

            if bnode is None:
                bnode = scene.node_tree.nodes.new(type=type_name)
                to_delete.append(bnode)

        # ----- Main loop

        else:
            try:
                bnode = btree.nodes.new(type=type_name)
            except RuntimeError as e:
                continue

        if 'legacy' in bnode.name.lower():
            continue

        # ----- Create the node info

        node_info = NodeInfo(btree, bnode)
        node_infos.append(node_info)

        # ----- Documented or not for version management

        if node_info.class_name not in custom.NODE_IMPLEMENTATIONS.keys():
            if type_name not in ['CompositorNodeRLayers']:
                constants.NON_DOCUMENTED_NODES[type_name] = f"{node_info.class_name} ({bnode.name})"

        # ----- Debug

        if False:
            print(f"tree_class_setup: {node_info.bl_idname:35s}: {node_info.class_name}")

        # ----- Check if there are no new sockets since last supported version

        node_info.check_socket_bl_idnames(unknown_sockets)

        # ----- Create the node class

        node_info.create_node_class()

        # Node class accessible as Tree attributes:
        # node = tree.NodeClass(...)

        setattr(tree_class, node_info.class_name, node_info.node_class)

    # ----------------------------------------------------------------------------------------------------
    # Create the socket classes

    if len(unknown_sockets):
        print(f"CAUTION ({tree_type}) : some sockets are new in this version:")
        pprint(unknown_sockets)
        print("Update the dict: constants.BL_ID_SOCKET_TO_TYPE")
        print()

    # Socket class name is equal to bsocket type
    socket_classes = constants.all_socket_classes(tree_type)
    for class_name in socket_classes:

        socket_type = class_name

        if class_name in dir(sockets_module):
            base_class = getattr(sockets_module, class_name)
        else:
            base_class = Socket

        sockets[class_name] = dynamic.Dynamic.NewSocket(class_name, base_class, socket_type, descr=None)

        # ----- The class as attribute of the Tree class

        setattr(tree_class, class_name, sockets[class_name].dyn_class)


    if False:
        print("SOCKETS")
        print(list(constants.SOCKETS[node_info.tree_type].keys()))

    # ----------------------------------------------------------------------------------------------------
    # Add members to the socket classes

    for node_info in node_infos:

        custs = custom.NODE_IMPLEMENTATIONS.get(node_info.class_name)

        if custs is None:
            continue

        if not isinstance(custs, (tuple, list)):
            custs = (custs,)

        # ----- c.code creates one or more methods, properties and global functions

        for cust in custs:
            cust.code(node_info)

    # ====================================================================================================
    # Done

    for node_info in node_infos:
        node_info.bnode   = None
        node_info.inputs  = None
        node_info.outputs = None

    treestack.del_tree(btree)

    if scene is not None:
        for bnode in to_delete:
            scene.node_tree.nodes.remove(bnode)
        scene.use_nodes = mem_un
