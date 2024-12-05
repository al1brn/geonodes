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
- update   : 2024/12/03
"""

from pprint import pprint
from pathlib import Path
import inspect

import bpy

from ..core import constants
from ..core import utils
from . import blendertree


IGNORE_PARAMS = ['color_ramp']

DEPRECATED_NODES = [
    'Align Euler to Vector',
    'Rotate Euler',
]

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
            if name in IGNORE_PARAMS:
                continue
            self.params[name] = getattr(self.bnode, name)

        # ----- Parameters in enum

        self.enum_params   = {}
        for param in self.params:
            enums = self.get_enum_list(param)
            if enums is None:
                continue
            self.enum_params[param] = enums

        # ----------------------------------------------------------------------------------------------------
        # Build the input sockets list plus the data driven socket list

        homonyms  = {}
        enableds  = {}
        disableds = {}
        for bsock in self.bnode.inputs:
            if bsock.type == 'CUSTOM':
                continue

            if bsock.name in homonyms:
                homonyms[bsock.name] += 1
            else:
                homonyms[bsock.name] = 1

            d = enableds if bsock.enabled else disableds
            if bsock.name in d:
                d[bsock.name] += 1
            else:
                d[bsock.name] = 1

        self.input_sockets  = {} # key: (socket name, order), value: identifier to use
        self.driven_sockets = []
        drived_count = None
        for name, count in homonyms.items():

            # ----- No homonym: very simple
            if count == 1:
                self.input_sockets[(name, 0)] = name

            # ----- Only one enabled -> data driven
            # NOTE
            # This algo could not work
            # Mix node has two driving parameter:
            # - data_type
            # - factor_mode for vectors (driving Factor socket)
            # Since data_type is the default driving parameter, there is not need to hack this algo

            elif name in enableds and enableds[name] == 1:
                self.input_sockets[(name, None)] = name
                self.driven_sockets.append(name)
                if drived_count is None:
                    drived_count = count

            # ----- We need to use identifier
            else:
                num = 0
                for bsock in self.bnode.inputs:
                    if bsock.name != name:
                        continue
                    self.input_sockets[(name, num)] = bsock.identifier
                    num += 1

        self.driver_param = None
        if len(self.driven_sockets):
            if hasattr(self.bnode, 'data_type'):
                self.driver_param = 'data_type'

            elif len(self.enum_params) == 1:
                self.driver_param = list(self.enum_params.keys())[0]
                assert(drived_count == len(self.enum_params[self.driver_param]))

            else:
                for name, enum in self.enum_params.items():
                    if len(enum) == drived_count:
                        self.driver_param = name

                if self.driver_param is not None:
                    print(self.bnode.name)
                    pprint(self.driven_sockets)
                    print("Homonyms")
                    pprint(homonyms)
                    print("Enableds")
                    pprint(enableds)
                    print("Disableds")
                    pprint(disableds)
                    print("Enum params")
                    pprint(self.enum_params)
                    assert(False)

        # -----------------------------------------------------------------------------------------------------------------------------
        # Some nodes hacking

        self.node_class = None
        self._signature = None
        self._node_call = None

        if self.bnode.name == 'Color Ramp':
            self.params['stops'] = []
            self.node_class = 'ColorRamp'
            self._signature = "(cls, fac=None, stops=[])"
            self._node_call = "ColorRamp(fac=fac, stops=stops)"


    # =============================================================================================================================
    # Utilities

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
    # Load a specific node

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

    def get_input_socket(self, name, num=None):

        # No num : first enabled
        if num is None:
            for bsock in self.bnode.inputs:
                if bsock.enabled and bsock.name == name:
                    return bsock

        # num : names only
        else:
            for bsock in self.bnode.inputs:
                if bsock.name == name:
                    if num == 0:
                        return bsock
                    num -= 1

        print(f"get_input_socket error on node {self.bnode.name}: socket = '{name}', num = {num}")
        pprint(self.input_sockets)
        assert(False)

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

        # ----- Check consistency

        for sock_name in ignore_sockets:
            if not sock_name in self.input_sockets:
                raise Exception(f"Socket '{sock_name}' doesn't exist in node '{self.bnode.name}': {list(self.input_sockets.keys())}")

        # ----- Multi input

        multi_input_socket = None
        for bsock in self.bnode.inputs:
            if bsock.is_multi_input:
                multi_input_socket = bsock.name

                arg_name = utils.socket_name(bsock.name)
                if self_socket == bsock.name:
                    in_sockets[bsock.name] = f"[self] + list({arg_name})"
                else:
                    in_sockets[bsock.name] = f"list({arg_name})"
                arg_help.append(f"{arg_name} ({constants.CLASS_NAMES[bsock.type]}) : multi input socket '{bsock.name}'")

                header.append(f"*{arg_name}")

                break

        # ----- Loop on the sockets

        for (sock_name, sock_num), sock_id in self.input_sockets.items():

            # Already done
            if sock_name == multi_input_socket:
                continue

            bsocket = self.get_input_socket(sock_name, sock_num)
            arg_name = utils.socket_name(sock_name)
            if sock_num is not None and sock_num != 0:
                arg_name = f"{arg_name}_{sock_num:d}"

            # HACK
            if self.bnode.name == 'Axes to Rotation':
                if arg_name == 'primary_axis':
                    arg_name = 'primary_axis_1'
                if arg_name == 'secondary_axis':
                    arg_name = 'secondary_axis_1'

            if sock_name == self_socket and ok_self:
                if bsocket.type == 'GEOMETRY':
                    in_sockets[sock_id] = 'self._geo'
                else:
                    in_sockets[sock_id] = 'self'
                ok_self = False

                info_help.append(f"Socket '{sock_name}' : self")

            elif sock_name == 'Selection' and not expose_selection:
                in_sockets[sock_id] = 'self._sel'
                info_help.append("Socket 'Selection' : self[selection]")

            elif sock_name in ignore_sockets:
                info_help.append(f"Socket '{sock_name}' : ignored")

            else:
                in_sockets[sock_id] = arg_name
                header.append(arg_name)

                # Comment
                socket_type = constants.CLASS_NAMES[bsocket.type]
                sid = "" if sock_name == sock_id else f" (id: '{sock_id}')"
                arg_help.append(f"{arg_name} ({socket_type}) : socket '{sock_name}'{sid}")

        return {
            'has_items'  : len(in_sockets) > 0,
            'in_sockets' : in_sockets,
            'header'     : header,
            'header_str' : ", ".join([pyname if pyname.startswith('*') else f"{pyname}=None" for pyname in header]),
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

        if method_type == 'CLASS' and self._signature is not None:
            return self._signature

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

    def node_call(self, method_type='CLASS', self_socket=None, expose_selection=True, ignore_sockets=[], **parameters):

        if method_type == 'CLASS' and self._node_call is not None:
            return self._node_call

        if self_socket == 'AUTO':
            self_socket = self.default_self_socket

        sockets = self.get_sockets(self_socket=self_socket, expose_selection=expose_selection, ignore_sockets=ignore_sockets)
        params  = self.get_parameters(**parameters)

        s : str
        if self.node_class is None:
            s = f"Node('{self.bnode.name}'"
        else:
            s = f"{self.node_class}("

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
        func_name=None, ignore_sockets=[], **parameters):
        """ Generate the source code

        Arguments
        ---------
        - method_type (str = 'CLASS') : str in ('METHOD', 'PROPERTY_SET', 'PROPERTY_GET', 'CLASS', 'CLASS_PROPERTY', 'STATIC')
        - self_socket (str = None) : socket name for methods or 'AUTO' for the first input socket
        - expose_selection (bool = True) : expose the 'Selection' socket if exists
        - returns (str = 'NODE') : str in ('NONE', 'NODE', 'OUT', 'JUMP')
        - func_name (str = None) : replace the default function name
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
            ignore_sockets=ignore_sockets, **parameters)

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

    def class_method_code(self, returns='NODE', func_name=None, ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         ='CLASS',
            returns             = returns,
            func_name           = func_name,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def class_property_code(self, returns='OUT', func_name=None, ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'CLASS_PROPERTY',
            returns             = returns,
            func_name           = func_name,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def method_code(self, self_socket='AUTO', expose_selection=False, returns='OUT', func_name=None,
        ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'METHOD',
            self_socket         = self_socket,
            expose_selection    = expose_selection,
            returns             = returns,
            func_name           = func_name,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def property_get_code(self, self_socket='AUTO', expose_selection=False, returns='OUT', func_name=None, ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'PROPERTY_GET',
            self_socket         = self_socket,
            expose_selection    = expose_selection,
            returns             = returns,
            func_name           = func_name,
            ignore_sockets      = ignore_sockets,
            **parameters)

    def property_set_code(self, self_socket='AUTO', expose_selection=False, returns='JUMP', func_name=None, ignore_sockets=[], **parameters):
        return self.source_code(
            method_type         = 'PROPERTY_SET',
            self_socket         = self_socket,
            expose_selection    = expose_selection,
            returns             = returns,
            func_name           = func_name,
            ignore_sockets      = ignore_sockets,
            **parameters)

    # ====================================================================================================
    # Default static implementation

    def default_class_code(self, return_test=False):

        test = f"{utils.socket_name(self.bnode.name)}"

        method_type = 'CLASS'
        if len(self.bnode.inputs) == 0 and len(self.params) == 0:
            method_type = 'CLASS_PROPERTY'
        else:
            test += "()"

        returns = 'OUT' if len(self.bnode.outputs) == 1 else 'NODE'
        node_name = self.bnode.name

        source_code = self.source_code(method_type=method_type, returns=returns)

        if return_test:
            return source_code, test
        else:
            return source_code

    # ====================================================================================================
    # Default implementation

    def default_implementation(self):

        tags = ['METHOD', 'SET', 'GET', 'CONSTRUCTOR']


        has_data_type = 'data_type' in self.params
        has_domain    = 'domain' in self.params
        has_selection = 'Selection' in [bsock.name for bsock in self.bnode.inputs]
        func_name     = utils.socket_name(self.bnode.name)

        # ----- Input class

        input_class = None
        for bsock in self.bnode.inputs:
            if bsock.type == 'CUSTOM':
                continue
            input_class = constants.CLASS_NAMES[bsock.type]
            break

        # ----- Output class

        output_class = None
        for bsock in self.bnode.outputs:
            if bsock.type == 'CUSTOM':
                continue
            output_class = constants.CLASS_NAMES[bsock.type]
            break

        # ----- Number of "free" sockets or parameters

        free_params = []
        for bsock in self.bnode.inputs:
            if bsock.name == input_class or bsock.name == 'Selection':
                continue
            free_params.append(bsock.name)

        for param in self.params:
            if param in ['data_type', 'domain']:
                continue
            free_params.append(param)

        print("Implementation of:", self.bnode.name)
        print("   Default implementation name:", func_name)

        # ----- No input : constructor

        if input_class is None:
            print("   Constructor or", output_class)

        else:
            jump = False
            if input_class == 'Geometry' and output_class == 'Geometry' and not self.has_multi_input:
                jump = True

            if jump:
                if len(free_params) == 1:
                    name = func_name[4:] if func_name.startswith('set_') else func_name
                    print(f"   {name}: SET property of", input_class, ':', free_params[0])
                else:
                    print("   Jump method of", input_class)
            else:
                print("   Method of", input_class)

            if has_domain:
                print("   Domain method: ", self.enum_params['domain'])

    # ====================================================================================================
    # Utilities

    @classmethod
    def loop(cls, func, *args, tree_type='GeometryNodeTree', **kwargs):

        btree = blendertree.get_tree("Temp", tree_type=tree_type, create=True)
        btree.nodes.clear()

        count = 0

        for type_name in dir(bpy.types):

            try:
                bnode = btree.nodes.new(type=type_name)
            except RuntimeError as e:
                continue

            if ('legacy' in bnode.name.lower()) or (bnode.name in DEPRECATED_NODES):
                continue

            node_info = cls(btree, bnode)

            func(node_info, *args, **kwargs)

            count += 1

        blendertree.del_tree(btree)

        return count

    # ====================================================================================================
    # List of nodes

    @classmethod
    def get_nodes(cls, tree_type='GeometryNodeTree'):

        nodes = {}

        def func(node_info):
            nodes[node_info.bnode.bl_idname] = node_info.bnode.name

        cls.loop(func, tree_type=tree_type)

        return nodes

    # ====================================================================================================
    # Auto generation

    # ----------------------------------------------------------------------------------------------------
    # Get the dictionnaries

    @classmethod
    def get_node_dicts(cls):
        s_nodes = cls.get_nodes('ShaderNodeTree')
        g_nodes = cls.get_nodes('GeometryNodeTree')
        common_nodes   = {blid: name for blid, name in s_nodes.items() if blid in g_nodes}

        return {
            'Common'          : common_nodes,
            'ShaderNodeTree'  : {blid: name for blid, name in s_nodes.items() if blid not in common_nodes},
            'GeometryNodeTree': {blid: name for blid, name in g_nodes.items() if blid not in common_nodes},
        }

    # ----------------------------------------------------------------------------------------------------
    # Implementation

    @classmethod
    def name_interpretation(cls):
        dicts = cls.get_node_dicts()

        setters    = []
        getters    = []
        converters = []
        others     = []

        for d in dicts.values():
            for blid, name in d.items():
                if name.startswith("Set "):
                    setters.append(name)
                elif name.find(" to ") >= 0:
                    converters.append(name)
                else:
                    others.append(name)

        for name in others:
            if f"Set {name}" in setters:
                getters.append(name)

        for name in getters:
            others.remove(name)

        print('-'*60)
        print("Others")
        print('-'*60)
        pprint(others)
        print()

        print('-'*60)
        print("Setters")
        print('-'*60)
        pprint(setters)
        print()

        print('-'*60)
        print("Getters")
        print('-'*60)
        pprint(getters)
        print()

        print('-'*60)
        print("Converters")
        print('-'*60)
        pprint(converters)
        print()

        print('-'*60)
        print("Others")
        print('-'*60)
        pprint(len(others))
        print()








    # ----------------------------------------------------------------------------------------------------
    # Static class

    @classmethod
    def gen_static_classes(cls):

        codes = []
        tests = {}

        def func(node_info, nodes):
            if node_info.bnode.bl_idname not in nodes:
                return
            code, test = node_info.default_class_code(return_test=True)
            codes.append(code)
            tests[node_info.bnode.name] = test

        def gen_receipt(name, class_name, exclude=[]):
            _tab = " "*4
            nd = "snd" if class_name == 'ShaderNodes' else "nd"

            codes.append(f"{_tab}@classmethod")
            codes.append(f"{_tab}def _{name}(cls):")
            codes.append(f"{_tab*2}from geonodes import GeoNodes, ShaderNodes, nd, snd")
            codes.append(f"{_tab*2}with {class_name}('{name}'):")
            for node_name, test in tests.items():
                if node_name in exclude:
                    continue
                codes.append(f"{_tab*3}{nd}.{test}")
            codes.append("")

        s_nodes = cls.get_nodes('ShaderNodeTree')
        g_nodes = cls.get_nodes('GeometryNodeTree')

        common_nodes   = {blid: name for blid, name in s_nodes.items() if blid in g_nodes}
        shader_nodes   = {blid: name for blid, name in s_nodes.items() if blid not in common_nodes}
        geometry_nodes = {blid: name for blid, name in g_nodes.items() if blid not in common_nodes}

        # Header
        codes.append("# Static classes exposing all nodes")
        codes.append("#")
        codes.append("# Auto generated by NodeInfo.gen_static_classes")
        codes.append(f"# Blender version: {bpy.app.version}")
        codes.append("")
        codes.append("import numpy as np")
        codes.append("import bpy")
        codes.append("from .treeclass import Node, ColorRamp")
        codes.append("from .utils import get_object")
        codes.append("")

        # --- Common class

        print(f"Generating CommonStatic: {len(common_nodes)} nodes")
        codes.append("class CommonStatic:")
        cls.loop(func, common_nodes, tree_type='ShaderNodeTree')

        #gen_receipt('_receipt_common', "ShaderNodes")
        #tests.clear()

        # ----- Shader class

        print(f"Generating ShaderStatic: {len(shader_nodes)} nodes")
        codes.append("class snd(CommonStatic):")
        cls.loop(func, shader_nodes, tree_type='ShaderNodeTree')

        # Receipt for common and shader

        gen_receipt('receipt_shader', "ShaderNodes")
        tests.clear()

        # ----- Geometry nodes class

        print(f"Generating GeonodesStatic: {len(geometry_nodes)} nodes")
        codes.append("class nd(CommonStatic):")
        cls.loop(func, geometry_nodes, tree_type='GeometryNodeTree')

        # Modifier and tool receipt

        gen_receipt('receipt_modifier', "GeoNodes", exclude=constants.TOOL_ONLY)
        gen_receipt('receipt_tool', "GeoNodes.Tool", exclude=constants.MODIFIER_ONLY)
        tests.clear()

        # Done

        return "\n".join(codes)
