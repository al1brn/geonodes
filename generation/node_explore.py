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

from pprint import pprint, pformat
from pathlib import Path
import inspect

import bpy

from ..core import constants
from ..core import utils
from . import blendertree


IGNORE_PARAMS = ['color_ramp', 'paired_output']

DEPRECATED_NODES = [
    'Align Euler to Vector',
    'Rotate Euler',
]

# Specific Nodes

SPEC_NODES = {
    'Float Curve'   : 'NodeCurves',
    'RGB Curves'    : 'NodeCurves',
    'Vector Curves' : 'NodeCurves',
}

# Tabulation
_1, _2, _3, _4 = " "*4, " "*8, " "*12, " "*16

# ====================================================================================================
# Node wrapper

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
            #bl_idname = constants.NODE_NAMES[btree.bl_idname].get(bnode.lower())
            #if bl_idname is None:
            #    bl_idname = bnode
            bl_idname = utils.get_node_bl_idname(bnode, btree.bl_idname)
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
            s = str(getattr(self.bnode, name))
            if not s.startswith('<'):
                self.params[name] = getattr(self.bnode, name)

        # ----- Parameters in enum

        self.enum_params   = {}
        self.user_params   = {}
        for param in self.params:
            enums = self.get_enum_list(param)
            if enums is None:
                continue
            self.enum_params[param] = enums
            if param in ['domain', 'data_type', 'input_type']:
                self.user_params[param] = enums
            else:
                self.user_params[param] = utils.get_enum_param_users(enums, self.bnode.name, param, user_case=True)

        self.data_type_sockets = self.get_data_type_sockets()

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

    @classmethod
    def geometry_class(cls, name):
        if name in ['Mesh', 'Meshes', 'Mesh 1', 'Mesh 2', 'Bounding Box', 'Convex Hull', 'Dual Mesh']:
            return 'Mesh'
        elif name in ['Curve', 'Curves', 'Spline', 'Splines', 'Guide Curves']:
            return 'Curve'
        elif name in ['Instance', 'Instances', 'Curve Instances']:
            return 'Instances'
        elif name in ['Cloud', 'Points', 'Point Cloud']:
            return 'Cloud'
        elif name in ['Volume']:
            return 'Volume'
        elif name in ['Grease Pencil']:
            return 'GreasePencil'
        elif name in ['Geometry', 'Geometries', 'Transform', 'Target Geometry', 'Selection', 'Inverted', 'Output']:
            return 'Geometry'
        else:
            raise Exception(f"Unkown Geometry socket name: '{name}'")

    @classmethod
    def get_socket_class_name(cls, socket):
        class_name = constants.CLASS_NAMES[socket.type]
        if class_name == 'Geometry':
            class_name = cls.geometry_class(socket.name)
        elif class_name == 'Shader':
            if socket.name in ['Volume']:
                return 'VolumeShader'
            else:
                return 'Shader'
        return class_name

    def get_domain_class(self, domain):

        if domain in ['POINT', 'POINTS']:
            return 'Point'
        elif domain in ['FACE', 'FACES']:
            return 'Face'
        elif domain in ['EDGE', 'EDGES']:
            return 'Edge'
        elif domain in ['CORNER', 'CORNERS']:
            return 'Corner'
        elif domain in ['SPLINE', 'SPLINES', 'CURVE']:
            return 'Spline'
        elif domain in ['INSTANCE', 'INSTANCES']:
            return 'Instance'
        elif domain in ['LAYER', 'LAYERS']:
            return 'Layer'
        elif domain == 'AUTO':
            return 'Geometry'
        else:
            raise Exception(f"Unknown domain: '{domain}' in node '{self.bnode.name}'")

    # =============================================================================================================================
    # Dump

    @classmethod
    def dump_nodes(cls, btree, nodes, target='CONSOLE'):

        tree_name = "GeoNodes" if btree.bl_idname == 'GeometryNodeTree' else 'ShaderNodes'

        txt = ""
        for node in nodes:
            node_info = NodeInfo(btree, node)
            txt += node_info.dump_node()

        if target == 'CONSOLE':
            print(txt)

        elif target is not None:
            bl_text = bpy.data.texts.get(target)
            if bl_text is None:
                bl_text = bpy.data.texts.new(target)
            bl_text.clear()

            bl_text.write("\nfrom geonodes import *\n\n")
            bl_text.write(f"with {tree_name}('{target}'):\n\n")

            lines = txt.split("\n")
            txt = "\n    ".join([""] + lines)
            bl_text.write(txt)

        return txt

    def dump_node(self):

        from geonodes.core.generated.cross_reference import CROSS_REF

        DOMAINS = {
            'Point': 'Mesh(Geometry()).points',
            'Vertex': 'Mesh().points',
            'Face' : 'Mesh().faces',
            'Edge' : 'Mesh().edges',
            'Corner' : 'Mesh().corners',
            'CloudPoint' : 'Cloud().points',
            'SplinePoint' : 'Curve().points',
            'Spline' : 'Curve().splines',
            'Instance' : 'Instances().insts',
            'Layer' : 'GreasePencil().layers',
        }

        # ---------------------------------------------------------------------------
        # An list of values to string

        def a_str(a):
            return "(" + ", ".join([f"{v:.3f}" for v in a]) + ")"

        # ---------------------------------------------------------------------------
        # Name and bl_idname

        bnode = self.bnode
        bl_idname = bnode.bl_idname
        node_name = bnode.name.split('.')[0] if bnode.label == "" else bnode.label

        # ---------------------------------------------------------------------------
        # Specific dump for nodes such as "Float Curve" or "Color Ramp"

        content = ""
        if bl_idname == 'FunctionNodeInputColor':
            c = bnode.value
            content = f"color = Color({a_str(c)})"
        elif bl_idname == 'ShaderNodeFloatCurve':
            content =  f"value = Float().curve(factor=None, curve={utils.curve_to_list(bnode.mapping.curves[0], as_str=True)})"
        elif bl_idname == 'ShaderNodeVectorCurve':
            content = f"vector = Vector().curves(fac=None, curves={utils.curves_to_list(bnode.mapping.curves, as_str=True)})"
        elif bl_idname == 'ShaderNodeRGBCurve':
            content = f"col = Color().curves(fac=None, curves={utils.curves_to_list(bnode.mapping.curves, as_str=True)})"
        elif bl_idname == 'ShaderNodeValToRGB':
            content = f"col = Float().color_ramp(stops={utils.color_ramp_get_stops(self.bnode, as_str=True)}, interpolation='{self.bnode.color_ramp.interpolation}')"

        # ---------------------------------------------------------------------------
        # Node name and parameters

        txt = f"# " + '-'*80 + f"\n# Node '{node_name}' ({bnode.bl_idname})\n"
        add_line = False
        for param in self.params:
            add_line = True
            if param in self.enum_params:
                txt += f"# - {param:15s}: in {self.enum_params[param]}\n"
            else:
                txt += f"# - {param:15s}: {type(getattr(bnode, param)).__name__}\n"
        if add_line:
            txt += "\n"

        if content != "":
            txt += "# Content\n"
            txt += content + "\n"

        # ---------------------------------------------------------------------------
        # Implementations

        d = CROSS_REF.get(bl_idname, {})
        nd_impl = ""
        cl_impl = ""
        for class_name, impls in d.items():

            is_nd = class_name in ['nd', 'snd']
            is_module = class_name in ['gnmath']

            if is_nd:
                line = f"{class_name}:"
                s_impl = nd_impl
            elif is_module:
                line = f"Module {class_name}:"
                s_impl = cl_impl
            else:
                line = f"Class {class_name}:"
                s_impl = cl_impl

            s_impl += f"\n# {line}\n# {'-'*len(line)}\n"

            for impl in impls:
                help_str = impl.get('help')
                if help_str is not None:
                    s_impl += "\n" + help_str + "\n"
                    continue

                line = ""
                sample_class = impl.get('sample_class', None)
                if sample_class is None:
                    klass = class_name
                    comment = "#"
                else:
                    klass = sample_class
                    comment = f"# Sample with {class_name} = {sample_class}\n#"

                if impl.get('is_classmethod', False):
                    comment += " class"
                    line += f"{klass}."

                else:
                    if klass in DOMAINS:
                        comment += f" domain {klass}"
                        line = f"{DOMAINS[klass]}."

                    elif is_module:
                        line = f"{klass}."

                    else:
                        line = f"{klass}()."

                signature = impl.get('signature', "")
                signature = signature.replace("self, ", "")
                signature = signature.replace("self", "")
                signature = signature.replace("cls, ", "")
                signature = signature.replace("cls", "")

                if impl.get('is_get', False):
                    signature = ""

                line += impl['func_name'] + signature

                returns = impl.get('returns')
                outs = [utils.snake_case(bsock.name) for bsock in self.bnode.outputs]

                if impl.get('is_jump', False):
                    comment += " jump method"
                    if len(outs) > 1:
                        comment += ", peer sockets: " + str([f"{sout}_" for sout in outs[1:]])

                elif impl.get('is_get', False):
                    comment += " property"
                    line = "value = " + line

                elif impl.get('is_set', False):
                    comment += " property set"
                    line += " = value"

                else:
                    if is_module:
                        comment += ' function'
                    else:
                        comment += ' method'
                    comment += ", returns: "
                    if returns is None:
                        comment += "None"

                    elif returns == 'NODE':
                        line = "node = " + line
                        comment += f"Node {outs}"

                    elif returns == 'OUT':
                        if len(outs) == 0:
                            comment += "None"
                        elif len(outs) == 1:
                            line = "value = " + line
                            comment += f"node.{outs[0]}"
                        else:
                            line = "value = " + line
                            comment += f"node.{outs[0]} " + str([f"{sout}_" for sout in outs[1:]])

                    elif returns == 'TUPLE':
                        line = "my_tuple = " + line
                        comment += f"{len(bnode.outputs)}-tuple of output sockets {outs}"

                    else:
                        line = "value = " + line
                        comment += returns

                s_impl += "\n" + comment + "\n" + line + "\n"
                if is_nd:
                    nd_impl = s_impl
                else:
                    cl_impl = s_impl


            cl_impl += "\n\n"
            nd_impl += "\n\n"

        # ---------------------------------------------------------------------------
        # Concat

        txt = txt + cl_impl + nd_impl
        for i in range(5):
            txt = txt.replace('\n\n\n', '\n\n')

        return txt

    # =============================================================================================================================
    # Socket exploration

    @property
    def enabled_input_sockets(self):
        return {socket.name: socket for socket in self.bnode.inputs if socket.enabled}

    @property
    def enabled_output_sockets(self):
        return {socket.name: socket for socket in self.bnode.outputs if socket.enabled}

    # ----------------------------------------------------------------------------------------------------
    # Get the sockets driven by data_type, input_type or selection_type parameter

    def get_data_type_sockets(self):
        """ Get the dict describing the sockets driven by data_type

        > [!NOTE]
        > Return None if the node has not, data_type, input_type or selection_type parameter

        The returned dict has the following structure:
        - param_name : str in ('data_type', 'input_type', 'selection_type')
        - in_sockets : list of driven input sockets
        - out_sockets : list of driven output sockets
        - value_to_type : dict param value -> socket type
        - type_to_value : dict socket type -> param value

        > [!NOTE]
        > type_to_value is not always the transposition of value_to_type sinc different parameter values
        > can use the same socket type such as in 'Store Named Value'

        Returns
        -------
        - dict : sockets driven by data_type
        """

        driver_name = None
        for name in ['data_type', 'input_type', 'selection_type']:
            if name in self.enum_params:
                driver_name = name
                break
        if driver_name is None:
            return None

        # ----- Snapshot of current enabled sockets

        in_sockets  = {socket.name: [socket.type] for socket in self.enabled_input_sockets.values()}
        out_sockets = {socket.name: [socket.type] for socket in self.enabled_output_sockets.values()}

        # ----- Loop on the possible param values

        # Parame values

        param_values = self.enum_params[driver_name]

        # Save init Value

        driver_value = getattr(self.bnode, driver_name)

        # Loop

        in_sockets  = {}
        out_sockets = {}

        for value in param_values:

            setattr(self.bnode, driver_name, value)

            # ----- Input sockets

            for socket_name, socket in self.enabled_input_sockets.items():
                if socket_name in in_sockets.keys():
                    in_sockets[socket_name].append(socket.type)
                else:
                    in_sockets[socket_name] = [socket.type]

            # ----- Output sockets

            for socket_name, socket in self.enabled_output_sockets.items():
                if socket_name in out_sockets.keys():
                    out_sockets[socket_name].append(socket.type)
                else:
                    out_sockets[socket_name] = [socket.type]

        # Restore initial value

        setattr(self.bnode, driver_name, driver_value)

        # ----- Get the driven socket names
        # The length of the types set must be the length of the number of driving values

        value_to_type    = None
        in_socket_names  = []
        out_socket_names = []

        # ----- Input sockets

        for socket_name, socket_types in in_sockets.items():
            n = len(set(socket_types))
            # Heuristic
            if n != len(param_values):
                if n == 1:
                    continue
                if len(param_values) > 5 and n <= 3:
                    continue

            if value_to_type is None or len(socket_types) > len(value_to_type):
                value_to_type = {value: socket_type for value, socket_type in zip(param_values, socket_types)}

            in_socket_names.append(socket_name)

        # ----- Output sockets

        for socket_name, socket_types in out_sockets.items():
            if len(set(socket_types)) != len(param_values):
                continue

            if value_to_type is None or len(socket_types) > len(value_to_type):
                value_to_type = {value: socket_type for value, socket_type in zip(param_values, socket_types)}

            out_socket_names.append(socket_name)

        # -----Build type to value
        # For some nodes (e.g. Set Named Attribute) several values can need the same socket_type
        # socket_type -> value would loose info

        type_to_value = {}
        for value, socket_type in value_to_type.items():
            if not socket_type in type_to_value:
                type_to_value[socket_type] = value

        return {
            'param_name'    : driver_name,
            'in_sockets'    : in_socket_names,
            'out_sockets'   : out_socket_names,
            'value_to_type' : value_to_type,
            'type_to_value' : type_to_value,
        }

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
    def has_multi_input(self):
        for bsocket in self.bnode.inputs:
            if bsocket.is_multi_input:
                return True
        return False

    @property
    def global_is_prop(self):
        return len(self.bnode.inputs) == 0 and len(self.params) == 0

    def out_socket_str(self, bsocket, suffix=''):
        return f"{utils.snake_case(bsocket.name)}{suffix} ({constants.CLASS_NAMES[bsocket.type]})"

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

    def get_enum_list(self, param, user_version=False):
        """ Get the list of valid values of a node parameter.

        The list can vary when node parameters are changed.

        Arguments
        ---------
        - param (str) : Node parameter name
        - user_version (bool = False) user version

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

            if user_version:
                return utils.get_enum_param_users(vals, self.bnode.name, param)
            else:
                return vals

        return None

    # =============================================================================================================================
    # Loop on nodes

    @classmethod
    def loop(cls, func, *args, tree_type='GeometryNodeTree', is_tool=False, **kwargs):

        btree = blendertree.get_tree("Temp", tree_type=tree_type, create=True)
        if tree_type == 'GeometryNodeTree' and is_tool:
            btree.is_tool     = True
            btree.is_modifier = False
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

    # =============================================================================================================================
    # List of nodes

    @classmethod
    def get_nodes(cls, tree_type='GeometryNodeTree'):

        def func(node_info, nodes):
            nodes[node_info.bnode.bl_idname] = node_info.bnode.name

        nodes = {}
        cls.loop(func, nodes, tree_type=tree_type)

        return nodes

    # ----------------------------------------------------------------------------------------------------
    # Get the dictionnaries

    @classmethod
    def get_node_dicts(cls):
        s_nodes = cls.get_nodes('ShaderNodeTree')
        g_nodes = cls.get_nodes('GeometryNodeTree')
        common_nodes = {blid: name for blid, name in s_nodes.items() if blid in g_nodes}

        return {
            'Common'          : common_nodes,
            'ShaderNodeTree'  : {blid: name for blid, name in s_nodes.items() if blid not in common_nodes},
            'GeometryNodeTree': {blid: name for blid, name in g_nodes.items() if blid not in common_nodes},
        }

    # =============================================================================================================================
    # Source code generation

    # -----------------------------------------------------------------------------------------------------------------------------
    # Input sockets

    def get_in_sockets(self, only_enabled=True):

        in_sockets = []
        factor_socket = None
        for socket in self.bnode.inputs:
            if only_enabled and not socket.enabled:
                continue
            if socket.name in ['Fac', 'Factor']:
                factor_socket = socket
            else:
                in_sockets.append(socket)
        if factor_socket is not None:
            in_sockets.append(factor_socket)

        return in_sockets

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
        in_sockets = self.get_in_sockets(True)
        if len(in_sockets):
            return in_sockets[0].name
        else:
            return None

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sockets

    def get_arguments(self, self_socket: str | None = None, expose_selection: bool = True,
            only_enabled: bool = True, ignore_sockets: list[str] = [], **parameters):
        """ Build arguments list

        One dictionary is returned for each socket:
        - 'is_socket'    : is a socket (True) or a parameter (False)
        - 'identifier'   : socket identifier
        - 'socket_name'  : socket name
        - 'socket_type'  : socket type
        - 'is_argument'  : is included in the argument list
        - 'is_self'      : is the self socket
        - 'is_multi'     : is a multi argument
        - 'arg_name'     : argument name
        - 'socket_value' : argument value
        - 'comment'      : comment
        - 'info'         : information for non argument sockets

        Arguments
        ---------
        - self_socket : socket name to use to plug self
        - expose_selection : put 'Selection' socket (if exists) in the list of arguments or set to 'self._sel'
        - only_enabled : sue only enabled sockets
        - ignore_sockets : list of sockets to ignore
        - parameters : forced node parameters

        Returns
        -------
        - list of dicts
        """

        args = []

        # ====================================================================================================
        # Parameters

        # ----- Set the parameters to the required value

        param_values = {param_name: getattr(self.bnode, param_name) for param_name in self.params}

        data_type = None
        for param_name, param_value in parameters.items():
            if param_name not in self.params.keys():
                raise Exception(f"Parameter '{param_name}' not found in node '{self.bnode.name}' parameters: {list(self.params.keys())}")
            if param_value == 'DATA_TYPE':
                data_type = param_name
            else:
                setattr(self.bnode, param_name, param_value)

        # ----- Loop on the node parameters

        for param, param_value in self.params.items():

            if param == data_type:
                driving_arg_name = utils.snake_case(self.data_type_sockets['in_sockets'][0])

                args.append({
                    'is_socket'    : False,
                    'arg_name'     : param,
                    'is_argument'  : False,
                    'comment'      : None,
                    'info'         : f"Parameter '{param}' : depending on '{driving_arg_name}' type",
                    'node_value'   : param,
                    #'source_code'  : f"{param} = utils.get_argument_data_type({driving_arg_name}, {self.data_type_sockets['type_to_value']}, '{self.bnode.name}', '{driving_arg_name}')"
                })
                continue

            # ----- Forced, vs free

            forced = param in parameters
            value = parameters[param] if forced else param_value

            # ----- Parameter value to source code string

            str_value : str
            if isinstance(value, str):
                str_value = f"'{value}'"
            elif str(value)[0] == '<':
                str_value = "None"
            else:
                str_value = str(value)

            # ----- Add the parameter

            d = {
                'is_socket'    : False,
                'arg_name'     : param,
                'is_argument'  : not forced,
                'comment'      : None,
                'info'         : None,
            }

            if forced:
                d['node_value'] = str_value
                d['info'] = f"Parameter '{param}' : {str_value}"

            else:
                d['arg_value']  = str_value
                d['node_value'] = param

                if param in self.enum_params:
                    d['comment'] = f"{param} (str): parameter '{param}' in {self.get_enum_list(param, user_version=True)}"
                    d['check'] = f"utils.check_enum_arg('{self.bnode.name}', '{param}', {param}, 'METH_NAME', {self.get_enum_list(param)})"
                else:
                    d['comment'] = f"{param} ({type(value).__name__}): parameter '{param}'"

            if False: # A REPRENDRE
                if param == 'object' and self.btree.bl_idname == 'ShaderNodeTree':
                    call.append(f"{param}=get_object({param_value})")
                else:
                    call.append(f"{param}={param_value}")

            args.append(d)

        # ====================================================================================================
        # Sockets

        # ----- Check consistency

        for sock_name in ignore_sockets:
            all = [socket.name for socket in self.bnode.inputs]
            if not sock_name in all:
                raise Exception(f"Socket '{sock_name}' doesn't exist in node '{self.bnode.name}': {all}")

        # ----- Base input sockets

        in_sockets = self.get_in_sockets(only_enabled)

        # ----- Loop on the sockets

        # Socket can have the name of a node parameter
        counters = {d['arg_name']: 0 for d in args if d['is_argument']}

        ok_self  = self_socket is None

        for socket in in_sockets:

            if socket.type == 'CUSTOM':
                continue

            socket_name = socket.name if socket.label == ""  else socket.label

            if (socket_name in ignore_sockets) or (socket.name in ignore_sockets):
                args.append({
                    'is_socket'   : True,
                    'is_argument' : False,
                    'is_self'     : False,
                    'identifier'  : socket.identifier,
                    'node_value'  : None,
                    'info'        : f"Socket '{socket_name}' : ignored",
                })
                continue

            is_self     = False
            arg_name    = utils.snake_case(socket_name)
            node_value  = None
            is_multi    = socket.is_multi_input
            is_argument = True
            comment     = None
            info        = None

            # ----- Self socket

            if (self_socket == 'FIRST' or (socket_name == self_socket) or (socket.name == self_socket)) and not ok_self:
                ok_self = True
                is_self = True
                if is_multi:
                    node_value = f"[self] + list({arg_name})"
                    is_argument = True
                else:
                    node_value  = 'self'
                    is_argument = False
                    info        = f"Socket '{socket_name}' : self"

            # ----- Not self socket

            else:
                if arg_name in counters:
                    counters[arg_name] += 1
                    arg_name = f"{arg_name}_{counters[arg_name]}"
                else:
                    counters[arg_name] = 0

                # Selection socket
                if socket_name == 'Selection' and not expose_selection:
                    is_argument = False
                    node_value = "self._sel"
                    info       = "Socket 'Selection' : self[selection]"

                # Any other socket
                else:
                    if is_multi:
                        node_value = f"list({arg_name})"
                    else:
                        node_value = arg_name

            # ----- Store the socket usage

            args.append({
                'is_socket'   : True,
                'identifier'  : socket.identifier,
                'socket_name' : socket.name,
                'socket_type' : socket.type,
                'is_argument' : is_argument,
                'is_self'     : is_self,
                'is_multi'    : is_multi,
                'arg_name'    : arg_name,
                'arg_value'   : "None",
                'node_value'  : node_value,
                'comment'     : f"{arg_name} ({constants.CLASS_NAMES[socket.type]}) : socket '{socket_name}' (id: {socket.identifier})",
                'info'        : info,
            })

        # ----- Restore the parameters

        for param_name, param_value in param_values.items():
            setattr(self.bnode, param_name, param_value)

        return args

    # -----------------------------------------------------------------------------------------------------------------------------
    # Signature

    @staticmethod
    def signature(method, args):

        a = []
        for is_socket in [True, False]:
            for arg in args:
                if not arg['is_argument']:
                    continue
                if arg['is_socket'] != is_socket:
                    continue

                if arg['is_socket'] and arg['is_multi']:
                    a.insert(0, f"*{arg['arg_name']}")
                else:
                    a.append(f"{arg['arg_name']}={arg['arg_value']}")

        if method == 'CLASS':
            a.insert(0, "cls")
        elif method == 'METHOD':
            a.insert(0, "self")

        return "(" + ", ".join(a) + ")"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Node call

    def node_call(self, args):

        sockets = []
        params  = []

        for arg in args:
            if arg['is_socket']:
                sockets.append(f"'{arg['identifier']}': {arg['node_value']}")
            else:
                params.append(f"{arg['arg_name']}={arg['node_value']}")

        s = "sockets={" + ", ".join(sockets) + "}"
        params.insert(0, s)

        return f"('{self.bnode.name}', " + ", ".join(params) + ")"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Output sockets

    def node_output(self):
        out = {}
        for socket_name, socket in self.enabled_output_sockets.items():
            if socket.type == 'CUSTOM':
                continue
            if socket.label is not None and socket.label != "":
                name = socket.label
            else:
                name = socket_name
            out[utils.snake_case(name)] = self.get_socket_class_name(socket)
        return out

    # -----------------------------------------------------------------------------------------------------------------------------
    # Documentation

    def documentation(self, implementation, args, is_jump=False, returns='OUT'):

        IMPLEMENTATIONS = {
            'CONSTRUCTOR': 'Constructor',
            'GET': 'Property Get',
            'SET': 'Property Set',
            'METHOD': 'Method',
            'CLASS' : 'Class Method',
            'FUNCTION': 'Function',
            'STATIC' : 'Node',
        }

        if implementation == 'FUNCTION':
            _1, _2 = "", " "*4
        else:
            _1, _2 = " "*4, " "*8


        snode = "ShaderNode" if self.is_shader else "Node"

        if True:
            doc = _2 + '""" > ' + f"Node <&{snode} {self.bnode.name}>\n\n"
            if is_jump:
                doc += f"{_2}> ***Jump*** : Socket refers to node output socket after the call\n\n"
        else:
            doc += f"{'Jump ' if is_jump else ''}{IMPLEMENTATIONS[implementation]} <&{snode} {self.bnode.name}>\n\n"

        # Arguments

        arg_doc = []
        inf_doc = []
        for is_socket in [True, False]:
            for arg in args:
                if arg['is_socket'] != is_socket:
                    continue
                if arg['is_argument']:
                    arg_doc.append(arg['comment'])
                if arg['info'] is not None:
                    inf_doc.append(arg['info'])

        if len(inf_doc):
            doc += f"{_2}Information\n"
            doc += f"{_2}-----------\n{_2}- "
            doc += f"\n{_2}- ".join(inf_doc) + "\n\n"

        if len(arg_doc):
            doc += f"{_2}Arguments\n"
            doc += f"{_2}---------\n{_2}- "
            doc += f"\n{_2}- ".join(arg_doc) + "\n\n"

        # Returns

        if returns is not None:
            doc += f"{_2}Returns\n"
            doc += f"{_2}-------\n"

            out = self.node_output()

            if returns == 'NODE':
                a = [f"{socket_name} ({class_name})" for socket_name, class_name in out.items()]
                doc += f"{_2}- node [{', '.join(a)}]\n"

            elif returns == 'OUT':
                if implementation == 'JUMP':
                    doc += f"{_2}- self"
                    if len(out) > 1:
                        doc += f" [{list(out.values())[1]}_]\n"
                    doc += "\n"

                else:
                    if len(out):
                        doc += f"{_2}- {list(out.values())[0]}"
                        a = [f"{socket_name}_ ({class_name})" for socket_name, class_name in out.items()]
                        if len(a) > 1:
                            doc += f" [{', '.join(a[1:])}]"
                        doc += "\n"
                    else:
                        doc += f"{_2}- None\n"


            elif returns == 'TUPLE':
                a = [class_name for class_name in out.values()]
                doc += f"{_2}- tuple ({', '.join(a)})\n"

            else:
                doc += f"{_2}- {returns}\n"

        doc += _2 + '"""\n'

        return doc

    # ====================================================================================================
    # Enum argument checks

    def gen_arg_check(self, tab, args, meth_name):

        s = ""
        for arg in args:
            check = arg.get('check')
            if check is not None:
                check = check.replace('METH_NAME', meth_name)
                s += f"{tab}{check}\n"

        return s

    # ====================================================================================================
    # Auto generation

    # ====================================================================================================
    # Add an entry to auto gen dict

    def add_func(self, gen, class_name, func_name, code, node_name=None, halt=True, **params):

        # ----------------------------------------------------------------------------------------------------
        # Source code in gen['source']

        if class_name not in gen['source']:
            gen['source'][class_name] = {}

        if func_name in gen['source'][class_name] and halt:
            print('-'*100)
            print("Class name:", class_name)
            print("Function name:", func_name)
            print()
            print(">>>>> Existing code:")
            print(gen[class_name][func_name])

            print()
            print(">>>>> New code:")
            print(code)
            print('-'*100)

            raise Exception(f"Function name '{func_name}' already exists in class '{class_name}'")

        gen['source'][class_name][func_name] = code

        # ----------------------------------------------------------------------------------------------------
        # Cross reference in gen['cross']

        # ----- No node_name : it's the wrapped node

        if node_name is None:
            node_name = self.bnode.name

        # ----- Two nodes : it's property getter and setter

        is_prop = isinstance(node_name, (tuple, list))
        if not is_prop:
            node_name = [node_name]

        for i_name, name in enumerate(node_name):
            if name is None:
                continue

            bl_idname = constants.NODE_NAMES[self.btree.bl_idname][name]

            if bl_idname not in gen['cross']:
                gen['cross'][bl_idname] = {}
            if class_name not in gen['cross'][bl_idname]:
                gen['cross'][bl_idname][class_name] = []

            prms = {'func_name': func_name, 'node_name': name, **params}
            if is_prop:
                prms = {**prms, 'is_get': i_name==0, 'is_set': i_name==1}

            gen['cross'][bl_idname][class_name].append(prms)

        return gen

    # =============================================================================================================================
    # Merge generated source code

    @staticmethod
    def merge_implementation(source, target):
        if source is None:
            return target

        for class_name, funcs in source.items():
            if class_name not in target:
                target[class_name] = {}
            for name, code in funcs.items():
                target[class_name][name] = code

        return target

    # =============================================================================================================================
    # Node or subclass of Node

    @classmethod
    def get_node_class(cls, node_name):
        return SPEC_NODES.get(node_name, 'Node')

    # =============================================================================================================================
    # Static implementation

    # -----------------------------------------------------------------------------------------------------------------------------
    # Static Color Ramp implementation

    @classmethod
    def color_ramp(cls, fac=None, stops=None, interpolation='LINEAR'):
        """ Node <&Node Color Ramp>

        Exposes utilities to manage the color ramp

        ``` python
        ramp1 = Float(.5).color_ramp(stops=[.1, .9])
        ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
        ```

        Arguments
        ---------
        - fac (Float = None)
        - stops (list of tuple(float, tuple)) : stops made of (float, color as tuple of floats)
        - interpolation in ('EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT')
        """
        node = ColorRamp(fac=fac, stops=stops, interpolation=interpolation)
        return node._out

    # -----------------------------------------------------------------------------------------------------------------------------
    # Standard static codes

    def static_code(self, gen: dict, module: str, name: str | None = None):
        """
        Arguments
        ---------
        - gen : key = class name -> : dict of function name -> source code
        - module : module name
        - name : function name
        """
        node_name = self.bnode.name
        bl_idname = self.bnode.bl_idname

        # ----------------------------------------------------------------------------------------------------
        # Hacks

        if bl_idname == 'ShaderNodeValToRGB':
            code = inspect.getsource(NodeInfo.color_ramp)
            if name is None:
                name = 'color_ramp'
            else:
                code = code.replace('color_ramp', name)
            signature = str(inspect.signature(NodeInfo.color_ramp))
            self.add_func(gen, module, name, code, node_name='Color Ramp', halt=True, is_classmethod=True, returns='OUT', signature=signature)
            return

        # ----------------------------------------------------------------------------------------------------
        # Function name

        if name is None:
            name = utils.snake_case(node_name)

        # ----------------------------------------------------------------------------------------------------
        # Get the arguments

        args = self.get_arguments(self_socket=None, expose_selection=True, only_enabled=False)

        # ----------------------------------------------------------------------------------------------------
        # Implemented as property if
        # - no input sockets
        # - only one output sockets

        is_prop = True
        socks_count = 0
        for arg in args:
            if arg['is_argument']:
                is_prop = False
                if arg['is_socket']:
                    socks_count += 1
        ret_node = (socks_count == 0) and len(self.node_output()) > 1
        if ret_node:
            is_prop = False

        # ----------------------------------------------------------------------------------------------------
        # Source code

        s  = f"{_1}@classmethod\n"
        if is_prop:
            s += f"{_1}@property\n"
        signature = self.signature('CLASS', args)
        s += f"{_1}def {name}{signature}:\n"
        s += self.documentation('STATIC', args, returns='OUT')

        # Argument check
        s += self.gen_arg_check(_2, args, name)

        s += f"{_2}node = {self.get_node_class(node_name)}{self.node_call(args)}\n"
        if ret_node:
            s += f"{_2}return node\n"
        else:
            s += f"{_2}return node._out\n"

        # ----------------------------------------------------------------------------------------------------
        # Done

        return self.add_func(gen, module, name, s, is_classmethod=True, is_get=is_prop, returns='NODE' if ret_node else 'OUT', signature=signature)

    # =============================================================================================================================
    # Implement all static methods

    @classmethod
    def gen_static_nodes(cls, gen, tree_type='GeometryNodeTree', verbose=False):

        module = 'nd' if tree_type == 'GeometryNodeTree' else 'snd'

        def f(node_info, gen):
            if verbose:
                print("gen_static_nodes:", node_info.bnode.name)
            node_info.static_code(gen, module)

        cls.loop(f, gen, tree_type=tree_type)

        return gen

    # =============================================================================================================================
    # Set user parameters

    def set_user_parameters(self, **parameters):
        mem_params = {param_name: getattr(self.bnode, param_name) for param_name in parameters}
        for param_name, param_value in parameters.items():
            setattr(self.bnode, param_name, param_value)
        return mem_params

    # =============================================================================================================================
    # Constructor implementation

    def constructor_code(self, gen: dict, func_name: str | None = None, class_name: str | None = None, ignore_sockets: dict = {}, **parameters):
        """ Class constructor code

        Arguments
        ---------
        - gen : dict [class name -> dict[method name -> source code]]
        - func_name : function name, from node name if None
        - class_name : class name, deduced from output socket type if None
        - ignore_sockets : sockets to ignore
        - parameters : node parameters
        """
        # ----------------------------------------------------------------------------------------------------
        # Set user parameters

        mem_params = self.set_user_parameters(**parameters)

        # ----------------------------------------------------------------------------------------------------
        # Has a data_type parameter

        data_type_param: str = None
        data_type_sockets = self.data_type_sockets
        if data_type_sockets is not None:
            data_type_param = data_type_sockets['param_name']
            # Ignored if set in parameters
            if data_type_param in parameters:
                data_type_param = None

        if data_type_param is not None:
            for data_type_value in data_type_sockets['type_to_value'].values():
                self.constructor_code(gen, func_name=func_name, **{data_type_param: data_type_value}, **parameters)

            return gen

        # ----------------------------------------------------------------------------------------------------
        # Class name and function name

        if class_name is None:
            class_name = list(self.node_output().values())[0]

        if func_name is None:
            func_name = utils.CamelCase(self.bnode.name)

        # ----------------------------------------------------------------------------------------------------
        # Arguments

        args = self.get_arguments(self_socket=None, expose_selection=True, only_enabled=True, ignore_sockets=ignore_sockets, **parameters)

        is_prop = True
        for arg in args:
            if arg['is_argument']:
                is_prop = False
        if is_prop:
            is_prop = len(self.node_output()) == 1

        # ===========================================================================
        # NO Property constructor
        is_prop = False
        # ===========================================================================

        # ----------------------------------------------------------------------------------------------------
        # Source code

        s  = f"{_1}@classmethod\n"
        if is_prop:
            s += f"{_1}@property\n"

        signature = self.signature('CLASS', args)
        s += f"{_1}def {func_name}{signature}:\n"
        s += self.documentation('CONSTRUCTOR', args, returns=class_name)

        # Argument check
        s += self.gen_arg_check(_2, args, func_name)

        s += f"{_2}node = {self.get_node_class(self.bnode.name)}{self.node_call(args)}\n"
        s += f"{_2}return cls(node._out)\n"

        self.add_func(gen, class_name, func_name, s, is_classmethod=True, is_get=is_prop, returns='OUT', signature=signature)

        # ----------------------------------------------------------------------------------------------------
        # Done

        self.set_user_parameters(**mem_params)

        return gen


    # =============================================================================================================================
    # Method implementation

    def method_code(self, gen, func: str = 'method', func_name: str | None = None,
        class_name: str | None = None, self_: str | None = None, is_class_method: bool = False, jump_method: bool | None = None, only_enabled: bool = True,
        domain_loop: bool = True, domain_param: str | None = None, domain_value : str | None = None,
        data_type_loop: bool = True, set_in_socket: str | None = None, ret: str | None = 'OUT', cache: bool = False,
        check_existing: bool = True,
        **parameters):
        """ Method code

        Arguments
        ---------
        - gen : dict [class name -> dict[method name -> source code]]
        - func : type of implementation
        - func_name : function name, from node name if None
        - class_name : class name, deduced from output socket type if None
        - self_ : name of the socket to use as self value
        - is_class_method : implement as class method
        - jump_method : force or disable is_jump automatic flag
        - only_enabled : use only enabled input sockets
        - domain_loop : loop on domain values
        - domain_param : name of domain node parameter if any
        - domain_value : implement the method on the specifid domain
        - data_type_loop : loop on data_type parameter if any
        - set_in_socket : name of the input socket to use for set
        - ret : type of return
        - cache : use cache when creating the node
        - check_existing : raises en error if the method already exists
        - parameters : node parameters
        """
        # ----------------------------------------------------------------------------------------------------
        # Set user parameters

        mem_params = self.set_user_parameters(**parameters)

        # ----------------------------------------------------------------------------------------------------
        # Shader Node
        #
        # The name ends with BSDF : this is a Constructor

        if self.btree.bl_idname == 'ShaderNodeTree':
            if self.bnode.name.endswith('BSDF'):
                if class_name is None:
                    class_name = 'Shader'
                if func_name is None:
                    func_name = utils.CamelCase(self.bnode.name[:-5])

                return self.constructor_code(gen=gen, func_name=None, class_name=class_name, **parameters)

        # ----------------------------------------------------------------------------------------------------
        # Has a domain parameter
        #
        # If the node has a domain parameter, the method is implemented on each domain
        # By default, the parameter name is 'domain', but it can be different
        # When it is the case, the parameter name is given by 'domain_param' key in spec dict
        #
        # The loop is performed by calling recursively this method for each parameter value
        # - parameters is enriched with domain_param: value
        # - the entry 'domain' is added to spec to specify that the method must be implemented on a domain class
        #
        # The auto loop on domain param can be disabled with 'domain_loop': False

        # default domain param name is 'domain'
        if domain_param is None and 'domain' in self.enum_params:
            domain_param = 'domain'

        if (domain_value is None) and domain_loop:

            # We have a domain param, we loop on the possible values
            if (domain_param is not None) and (domain_param not in parameters):

                for domain_value in self.enum_params[domain_param]:
                    self.method_code(gen, func=func, func_name=func_name,
                        class_name=class_name, self_=self_, is_class_method=is_class_method, jump_method=jump_method,
                        only_enabled=only_enabled, domain_value=domain_value,
                        data_type_loop=data_type_loop, domain_param=domain_value, ret=ret, cache=cache,
                        **{domain_param: domain_value}, check_existing=check_existing, **parameters)

                self.set_user_parameters(**mem_params)

                return gen

        # ----------------------------------------------------------------------------------------------------
        # The node has a data_type parameter
        #
        # If the node has a data_type parameter, there are 3 possibilities:
        # - data_type drives the first input socket : the method is implemented for each class
        # - data_type drives at least one input socket but not the first one :
        #   data_type is dynamically computed from the argument type
        # - data_type drives only output sockets : no loop is performed on the parameter,
        #   it is up to the user to implement various data types with various method names

        data_type = None
        data_type_sockets = self.data_type_sockets
        if (data_type_sockets is not None) and len(data_type_sockets['in_sockets']):

            data_type = data_type_sockets['param_name']

            # data_type is in parameters: no loop
            if data_type in parameters:
                data_type = None

            else:
                # By default, self is not supposed to depend upon data_type value
                # It will be checkes afterwards
                self_is_driven = False

        # ----------------------------------------------------------------------------------------------------
        # What is the self socket ?
        #
        # It can be specified with the 'self_' argument
        # If it is not the case, the first enabled input socket is taken
        # If the node as no enabled input socket, self socket is undefined,
        # the caller must specify the class name with 'class' key.

        if (not is_class_method) and (self_ is None):
            self_ = self.default_self_socket
            is_class_method = self_ is None

        # ----------------------------------------------------------------------------------------------------
        # Self socket is driven
        #
        # We loop on all the data_type possible values.
        # This will change the self socket type and generate one implementation per class

        if data_type_loop and (data_type is not None) and (self_ in data_type_sockets['in_sockets']):
            for value in self.enum_params[data_type]:
                self.method_code(gen, func=func, func_name=func_name,
                    class_name=class_name, self_=self_, is_class_method=is_class_method, jump_method=jump_method,
                    only_enabled=only_enabled,
                    domain_loop=False, domain_value=domain_value, ret=ret, cache=cache, **{data_type: value}, check_existing=check_existing, **parameters)

            self.set_user_parameters(**mem_params)

            return gen

        # ----------------------------------------------------------------------------------------------------
        # What is the class name ?
        #
        # If it is not the case, the classe name is deduced from the first enabled input socket type
        #
        # If the class name is a geometry class, the implementation is performed on the domain with
        # the 'domain_value' key is set in spec.

        if class_name is None:

            if domain_value is None and domain_param is not None:
                domain_value = parameters.get(domain_param)

            # If domain is specified, overrides Geometry class
            if domain_value is None:
                if self_ is None:
                    raise Exception(f"Node '{self.bnode.name}': impossible to know the class name.")

                class_name = self.get_socket_class_name(self.bnode.inputs[self_])

            else:
                # If the first socket is not geometry, this is a class method
                if self_ is None or self.bnode.inputs[self_].type != 'GEOMETRY':
                    self_ = None
                    is_class_method = True

                # Let's get the class name
                class_name = self.get_domain_class(domain_value)

        else:
            # ----- Class name is specified
            # If it doesn't correspond to the class of the self socket
            # it is a class method and there is not self socket
            if self_ is not None:
                self_class_name = self.get_socket_class_name(self.bnode.inputs[self_])

                # ----- Geometry
                if self.bnode.inputs[self_].type == 'GEOMETRY':
                    if (self_class_name not in constants.GEOMETRY_CLASSES) and (self_class_name not in constants.GEOMETRY_CLASSES):
                        is_class_method = True

                # ----- Other than geometry
                else:
                    if self_class_name != class_name:
                        is_class_method = True

                if is_class_method:
                    self_ = None

        # ----------------------------------------------------------------------------------------------------
        # Output nodes

        out = self.node_output()

        # ----------------------------------------------------------------------------------------------------
        # Get the arguments
        #
        # The arguments return as dict per argument used to generate:
        # - the method signature
        # - the method documentation
        # - the node call

        # DATA_TYPE value for data_type parameter tells to get_arguments that data_type is dynamically computed:
        # - it is not included in the method arguments
        # - it is included in the node call with the same name allegedly previously computed:
        # def method(no data_type):
        #    data_type = ...
        #    node = Node(..., data_type=data_type)

        # dict copy
        parameters = {**parameters}
        if data_type is not None:
            parameters[data_type] = 'DATA_TYPE'

        ignore = []
        in_socket = None
        if func == 'set':
            for socket in self.bnode.inputs:
                if socket.type == 'CUSTOM' or not socket.enabled:
                    continue
                if socket.name in [self_, 'Selection']:
                    continue
                if set_in_socket is None:
                   if in_socket is None:
                       in_socket = socket.name
                   else:
                       ignore.append(socket.name)
                elif set_in_socket != socket.name:
                    ignore.append(socket.name)


        args = self.get_arguments(self_socket=self_, expose_selection=False, only_enabled=only_enabled, ignore_sockets=ignore, **parameters)

        # ----------------------------------------------------------------------------------------------------
        # If self is not used, this is as class method

        is_geometry  = False
        in_geo_class = 'NOPE'
        self_is_used = False
        free_args_count = 0
        for arg in args:
            if arg['is_socket'] and arg['is_self']:
                self_is_used = True
                is_geometry = arg['socket_type'] == 'GEOMETRY'
                if is_geometry:
                    in_geo_class = self.geometry_class(arg['socket_name'])
            elif arg['is_argument']:
                free_args_count += 1

        if not self_is_used:
            is_class_method = True

        # ----------------------------------------------------------------------------------------------------
        # Jump and get
        #
        # If self socket is a geometry and the node returns a geometry
        # - Jump if the geometries are the same
        # - Get if it returns a specific output socket and no free input arguments
        # Else
        # - get if one single output and no argument other than self

        is_jump = False
        is_get  = (func == 'get') and (free_args_count == 0)
        if is_geometry:
            if len(self.bnode.outputs):
                if self.bnode.outputs[0].type == 'GEOMETRY':
                    out_geo_class = self.geometry_class(self.bnode.outputs[0].name)
                    if in_geo_class == out_geo_class:
                        is_jump = True
                    if (free_args_count == 0) and (ret not in [None, 'OUT', 'NODE', 'TUPLE']) and (len(out) == 2):
                        is_get = True
                else:
                    if (free_args_count == 0) and (ret is not None) and (len(out) == 1):
                        is_get = True
            else:
                ret = None

        else:
            if (free_args_count == 0) and (ret is not None) and (len(out) == 1):
                is_get = True

        if jump_method is not None:
            is_jump = jump_method

        # ----- Adjust is_get

        if is_get:
            is_get = (is_class_method and ret != 'NODE') or (ret not in ['NODE', 'OUT'])
            #print("METHOD", "GET " if new_get else "METH", "CLASS" if is_class_method else "     ", func_name, '->', ret)

        # ----------------------------------------------------------------------------------------------------
        # Function name

        if func_name is None:
            func_name = utils.snake_case(self.bnode.name)

        # ----------------------------------------------------------------------------------------------------
        # Let's generated the source code

        # ----- Decorators

        s = f"{_1}@classmethod\n" if is_class_method else ""
        if is_get:
            s += f"{_1}@property\n"
        if func == 'set':
            s += f"{_1}@{func_name}.setter\n"

        # ----- header

        method = 'METHOD'
        if is_class_method:
            method = 'CLASS'

        signature = self.signature(method, args)
        s += f"{_1}def {func_name}{signature}:\n"

        # ----- Documentation

        if is_get:
            method = 'GET'

        s += self.documentation(method, args, is_jump=is_jump, returns=ret)

        # ----- Argument check

        s += self.gen_arg_check(_2, args, func_name)

        # ----- Data type dynamic computation

        if data_type is not None:
            driving_arg_name = utils.snake_case(data_type_sockets['in_sockets'][0])
            s += f"{_2}{data_type} = utils.get_argument_data_type({driving_arg_name}, {data_type_sockets['type_to_value']}, '{class_name}.{func_name}', '{driving_arg_name}')\n"

        # ----- Node call

        if is_class_method:
            cache = False

        snode = 'self._cache' if cache else self.get_node_class(self.bnode.name)
        s += f"{_2}node = {snode}{self.node_call(args)}\n"

        # ----- Jump

        if is_jump:
            s += f"{_2}self._jump(node._out)\n"

        # ----- Return

        if ret is None:
            s += f"{_2}return\n"

        elif ret == 'OUT':
            if is_jump:
                s += f"{_2}return self._domain_to_geometry\n"
            else:
                s += f"{_2}return node._out\n"

        elif ret == 'NODE':
            s += f"{_2}return node\n"

        elif ret == 'TUPLE':
            a = [f"node.{socket_name}" for socket_name in out.keys()]
            s += f"{_2}return ({', '.join(a)})\n"

        else:
            s += f"{_2}return node.{ret}\n"

        self.add_func(gen, class_name, func_name, s, halt=check_existing, is_classmethod=is_class_method, is_get=is_get, is_set=func=='set', returns=ret, signature=signature, is_jump=is_jump)

        # ----------------------------------------------------------------------------------------------------
        # Done

        self.set_user_parameters(**mem_params)

        return gen

    # =============================================================================================================================
    # Method implementation

    def global_code(self, gen, module: str, func_name: str | None = None, ret: str = 'OUT', **parameters):
        """ Method code

        Arguments
        ---------
        - gen : dict [class name -> dict[method name -> source code]]
        - func_name : function name, from node name if None
        - module : module name
        - ret : type of return
        - parameters : node parameters
        """
        # ----------------------------------------------------------------------------------------------------
        # Set user parameters

        mem_params = self.set_user_parameters(**parameters)

        # ----------------------------------------------------------------------------------------------------
        # Function name

        if func_name is None:
            func_name = utils.snake_case(self.bnode.name)

        # ----------------------------------------------------------------------------------------------------
        # Output nodes

        out = self.node_output()

        # ----------------------------------------------------------------------------------------------------
        # Get the arguments
        #
        # The arguments return as dict per argument used to generate:
        # - the method signature
        # - the method documentation
        # - the node call

        args = self.get_arguments(self_socket=None, expose_selection=True, only_enabled=True, **parameters)

        # ----------------------------------------------------------------------------------------------------
        # Let's generate the source code

        # ----- Method header

        signature = self.signature('FUNCTION', args)
        s = f"def {func_name}{signature}:\n"

        # ----- Documentation

        s += self.documentation('FUNCTION', args, returns=ret)

        # ----- Argument check

        s += self.gen_arg_check(_1, args, func_name)

        # ----- Node call

        s += f"{_1}node = {self.get_node_class(self.bnode.name)}{self.node_call(args)}\n"

        # ----- Return

        if ret is None:
            s += f"{_1}return\n"

        elif ret == 'OUT':
            s += f"{_1}return node._out\n"

        elif ret == 'NODE':
            s += f"{_1}return node\n"

        elif ret == 'TUPLE':
            a = [f"node.{socket_name}" for socket_name in out.keys()]
            s += f"{_1}return ({', '.join(a)})\n"

        self.add_func(gen, module, func_name, s, returns=ret, signature=signature)

        # ----------------------------------------------------------------------------------------------------
        # Done

        self.set_user_parameters(**mem_params)

        return gen

    # =============================================================================================================================
    # Implement according spec

    def source_code(self, gen, func: str = 'method', func_name: str | None = None,
        param_loop: str | None = None, mode_loop: bool = True, prefix: str = "", suffix: str = "",
        operation_param: str = 'operation', rename: dict = {},
        **kwargs):
        """ Source code from user spec

        Arguments
        ---------
        - gen : dict [class name -> dict[method name -> source code]]
        - func : type of implementation
        - func_name : function name, from node name if None
        - param_loop : one implementation per parameter value, using param value as method name
        - mode_loop : if the node an enum parameter equal to 'mode', performs a param_loop on it
        - prefix : prefix for method name in parameter loop
        - suffix : suffix for method name in parameter loop
        - operation_param : name of operation parameter for param_loop
        - rename : method rename dictionary for param loop
        - ret : type of return
        - parameters : node parameters
        """

        # DEBUG
        DEBUG = self.bnode.name in ['Trim Curve']

        if self.bnode.name not in ['Random Value']:
            pass
            #return

        # ----------------------------------------------------------------------------------------------------
        # Extract parameters from kwargs dict

        parameters = {}
        if 'parameters' in kwargs:
            parameters = kwargs['parameters']
            del kwargs['parameters']

        # ----------------------------------------------------------------------------------------------------
        # A loop on a parameter is required
        #
        # mode is often a parameter on which a loop is done

        mode_loop_performed = False
        mem_func_name = func_name

        if mode_loop and (param_loop is None) and ('mode' in self.enum_params) and ('mode' not in parameters):

            param_loop = 'mode'
            mode_loop_performed = True

            if prefix == '':
                if func_name is None:
                    if func == 'C':
                        prefix = utils.CamelCase(self.bnode.name)
                    else:
                        prefix = utils.snake_case(self.bnode.name) + '_'
                else:
                    if func == 'C':
                        prefix = func_name.title().replace('_', '')
                    else:
                        prefix = utils.snake_case(func_name) + '_'

            func_name = None

        if param_loop is not None:

            for value in self.get_enum_list(param_loop):
                fname = func_name
                if fname is None:
                    if value in ['RGB', 'HSV', 'HSL']:
                        fname = value
                    else:
                        if func in ['C', 'Constructor']:
                            fname = utils.CamelCase(value)
                        else:
                            fname = utils.snake_case(value)

                if fname in rename:
                    fname = rename[fname]

                fname = prefix + fname + suffix
                self.source_code(gen, func=func, func_name=fname, parameters={**parameters, param_loop: value}, **kwargs)

            if not mode_loop_performed:
                return gen

            func_name = mem_func_name

        # ----------------------------------------------------------------------------------------------------
        # Let's dispatch according the type of implementation

        # ----- Loop on output sockets

        if func == 'get_out_loop':

            # Return the node
            self.method_code(gen, func='get', func_name=func_name, cache=True, ret='NODE', **kwargs, **parameters)

            mem_params = self.set_user_parameters(**parameters)

            for socket_name in self.node_output():
                ret = utils.snake_case(socket_name)
                fname = rename.get(ret, ret)
                fname = prefix + fname + suffix
                self.method_code(gen, func='get', func_name=fname, cache=True, ret=ret, **kwargs, **parameters)

            self.set_user_parameters(**mem_params)

        # ----- Constructor

        elif func in ('C', 'Constructor'):
            self.constructor_code(gen, func_name=func_name, **kwargs, **parameters)

        # ----- Method

        elif func in ('m', 'method', 'Method', 'get'):
            self.method_code(gen, func=func, func_name=func_name, **kwargs, **parameters)

        # ----- Operation

        elif func in ['op', 'operation']:

            mem_params = self.set_user_parameters(**parameters)

            for op_value in self.get_enum_list(operation_param):
                fname = op_value.lower()
                if fname in rename:
                    fname = rename[fname]

                self.method_code(gen, func='m', func_name=fname, **kwargs, **{operation_param: op_value}, **parameters)

            self.set_user_parameters(**mem_params)

        # ----- Global math

        elif func in ['math']:

            for op_value in self.get_enum_list(operation_param):
                fname = op_value.lower()
                if fname in rename:
                    fname = rename[fname]

                self.global_code(gen, 'gnmath', func_name=fname, **kwargs, **{operation_param: op_value}, **parameters)

        return gen

    # =============================================================================================================================
    # Implement a property

    @classmethod
    def property_code(cls, tree, gen, func_name: str, setter: str, getter: str | dict | None = None,
        class_name: str | None = None, in_socket: str | None = None, out_socket: str | None = None,
        setter_params: dict = {}, getter_params: dict = {}, setter_sockets: dict = {}, getter_sockets: dict = {}):
        """
        Arguments
        ---------
        - gen : dict [class name -> dict[method name -> source code]]
        - func_name : property name
        - setter : node name for setter
        - getter : node name for getter, write only property if None
        - in_socket: name of the socket to use to set the value
        - out_socket: name of the socket to use to g the value
        """

        # ----------------------------------------------------------------------------------------------------
        # Setter

        set_node = cls(tree, setter)
        g = set_node.method_code({'source': {}, 'cross': {}}, func='set', func_name=func_name, set_in_socket=in_socket, **setter_params)

        # ----------------------------------------------------------------------------------------------------
        # Merge for all the class names

        for cname, code in g['source'].items():

            if class_name is None:
                klass = cname
            else:
                klass = class_name

            set_code = code[func_name]

            # ----------------------------------------------------------------------------------------------------
            # Getter

            if getter is None:
                getter_node_name = None
            elif isinstance(getter, dict):
                getter_node_name = getter[klass]
            else:
                getter_node_name = getter

            get_code  = f"{_1}@property\n"
            get_code += f"{_1}def {func_name}(self):\n"

            if getter_node_name is None:
                get_code += _2 + '"""' + f" Write only property for node <Node {set_node.bnode.name}>\n"
                get_code += _2 + '"""\n'
                get_code += f"{_2}raise NodeError('Property {klass}.{func_name} is write only.')\n\n"

            else:
                get_node = cls(tree, getter_node_name)
                get_code += _2 + '"""' + f" Property get node <Node {set_node.bnode.name}>\n"
                get_code += _2 + '"""\n'
                get_code += f"{_2}return Node('{getter_node_name}'"
                get_code += f", sockets={getter_sockets}"
                for k, v in getter_params.items():
                    get_code += f", {k}={v}"
                get_code += ")."
                if out_socket is None:
                    get_code += "_out\n\n"
                else:
                    get_code += f"{out_socket}\n\n"

            # ----- Merge the two methods in the dict

            set_node.add_func(gen, klass, func_name, get_code + set_code, node_name=(getter_node_name, setter))

        return gen


# =============================================================================================================================
# Generates the reference dictionaries

# -----------------------------------------------------------------------------------------------------------------------------
# enum_params values
#
# IN PROGRESS

def build_user_enum_params():
    """ Build the dictionary: user name -> enum param value
    """

    def f(ni, transco):

        node_name = ni.bnode.name
        for param_name, values in ni.enum_params.items():
            if param_name in ['data_type', 'domain', 'input_type']:
                continue

            for value in values:
                user = value.title()

                if user in transco:
                    transco[user]['nodes'].append(node_name)
                else:
                    transco[user] = {'value': value, 'nodes': [node_name]}


    geo_transco = {}
    utils.BUILD = True
    NodeInfo.loop(f, geo_transco)

    shader_transco = {}
    NodeInfo.loop(f, shader_transco, tree_type="ShaderNodeTree")
    utils.BUILD = False


    transco = {}
    for k, v in shader_transco.items():
        if k in geo_transco:
            for n in v['nodes']:
                if n not in geo_transco[k]['nodes']:
                    transco[k] = v




    print("# " + "="*100)
    print("# Nodes enum params transco")
    print("#")
    print("# Generated by node_explore.build_user_enum_params")
    print(f"# Blender version: {bpy.app.version}")
    print()

    print("ENUM_PARAMS = {")
    for user, info in transco.items():
        suser = f"'{user}'"
        sval  = f"'{info['value']}',"
        print(f"    {suser:25s} : {sval:25s} # {info['nodes']}")
    print("}")

    # ----- DEBUG

    if False:
        def check(ni):
            node_name = ni.bnode.name
            for param_name, values in ni.enum_params.items():
                if param_name in ['data_type', 'domain', 'input_type']:
                    continue

                print(f"# {node_name}, {param_name}")
                print(utils.get_enum_param_users(values, node_name, param_name, False))
                print(utils.get_enum_param_users(values, node_name, param_name, True))
                print()

        NodeInfo.loop(check)






# -----------------------------------------------------------------------------------------------------------------------------
# Information on classes

def build_sockets_dict():

    sockets = {}

    for tree_type in ['GeometryNodeTree', 'ShaderNodeTree']:

        # ===== Create temporaty tree

        tree = bpy.data.node_groups.get(f"Temp {tree_type}")
        if tree is None:
            tree = bpy.data.node_groups.new(f"Temp {tree_type}", tree_type)
        tree.nodes.clear()
        if tree_type == 'GeometryNodeTree':
            tree.is_modifier = True
        tree.interface.clear()
        tree.nodes.clear()

        # ===== List of acceptable input sockets

        try:
            tree.interface.new_socket(name="Socket", socket_type='ERROR')

        except Exception as e:
            s = str(e)
            p = s.find("ERROR")
            nodesockets = eval(s[p+20:])

        # ===== Group input node for the sockets

        in_node = tree.nodes.new('NodeGroupInput')

        for nodesocket in nodesockets:

            short = nodesocket[len('NodeSocket'):]
            class_name = CLASS_NAMES[short]

            # ----- Create a input socket

            item = tree.interface.new_socket(name=nodesocket, socket_type=nodesocket)

            # ----- Get the socket type

            socket_type = ""
            for socket in in_node.outputs:
                if socket.identifier == item.identifier:
                    socket_type = socket.type
                    ok = True
                    break
            assert(socket_type != "")

            # ----- The entry already exists

            if socket_type in sockets.keys():
                sockets[socket_type][tree_type] = True
                continue

            # ----- Create the entry

            sockets[socket_type] = {
                'class_name'        : class_name,
                'short'             : short,
                'nodesocket'        : nodesocket,
                'GeometryNodeTree'  : False,
                'ShaderNodeTree'    : False,
                'subtypes'          : [],
            }
            sockets[socket_type][tree_type] = True

            # ----- Get the subtypes if any

            if hasattr(item, 'subtype'):

                try:
                    item.subtype = "ERROR"

                except Exception as e:
                    s = str(e)
                    p = s.find("ERROR")
                    subtypes = eval(s[p+20:])

                for subtype in subtypes:
                    if subtype == 'NONE':
                        continue

                    sockets[socket_type]['subtypes'].append(subtype)

                    sub_item = tree.interface.new_socket(name=nodesocket + " " + subtype, socket_type=nodesocket)
                    sub_item.subtype = subtype

    # ----------------------------------------------------------------------------------------------------
    # Print the result in the console to copy / paste

    print("#", "="*125)
    print("# Sockets dictionary")
    print("#")
    print("# Generated by node_explore.build_sockets_dict")
    print("#")
    print(f"# Blender version: {bpy.app.version_string}")
    print(f"# Sockets: {list(sockets.keys())}")
    print()
    print("SOCKETS_DICT = " + pformat(sockets))
    print()

    return sockets


# -----------------------------------------------------------------------------------------------------------------------------
# data type node parameter from class

def build_data_types_dict():

    def f(node_info, nodes):

        # ----- Already done

        if node_info.bnode.bl_idname in nodes.keys():
            return

        for name, values in node_info.enum_params.items():

            if name not in ['data_type', 'input_type', 'selection_type']:
                continue

            # Get the driven sockets
            sockets = node_info.get_driven_socket_names(name)

            if node_info.bnode.name == "Random Value":
                print(node_info.bnode.name)
                pprint(sockets)
                print(node_info.enum_params[name])
                aaa

            # Initialize the entry
            nodes[node_info.bnode.bl_idname] = {
                'param_name'    : name,                     # node parameter name
                'value_to_type' : sockets['value_to_type'], # socket_type -> param value
                'type_to_value' : {},                       # socket_type -> param value
                'in_sockets'    : sockets['in_sockets'],    # names of driven input sockets
                'out_sockets'   : sockets['out_sockets'],   # names of driven output sockets
            }

            # Build the transco dictionary
            for value, socket_type in sockets["value_to_type"].items():
                # Different values of data_type parameter can need the same socket type
                # Store Named Attribute for instance
                if not socket_type in nodes[node_info.bnode.bl_idname]['type_to_value']:
                    nodes[node_info.bnode.bl_idname]['type_to_value'][socket_type] = value

    nodes = {}
    NodeInfo.loop(f, nodes, tree_type='GeometryNodeTree')
    NodeInfo.loop(f, nodes, tree_type='ShaderNodeTree')

    # ----------------------------------------------------------------------------------------------------
    # Print the result in the console to copy / paste

    print("#", "="*125)
    print("# Node data type parameter value from class name")
    print("#")
    print("# Generated by node_explore.build_data_types_dict")
    print("#")
    print(f"# Blender version: {bpy.app.version_string}")
    print(f"# Nodes: {list(nodes.keys())}")
    print()

    print("NODE_DATA_TYPES = {")
    for bl_idname, param in nodes.items():
        sblid = f"'{bl_idname}'"

        print(f"\t{sblid} :")
        pprint(param)
        print()

        if False:
            print(f"\t{sblid} :", "{")
            for param_name, transco in param.items():
                sparam = f"'{param_name}'"
                print(f"\t\t{sparam} :", "{")
                for k, v in transco.items():
                    sk = f"'{k}'"
                    print(f"\t\t\t{sk:12s} : '{v}',")
                print("\t\t},")

            print("\t},")

    print("}\n")

    return nodes

# =============================================================================================================================
# Build the dictionnary of node name -> bl_idname

def build_node_names_dict(tree_type='GeometryNodeTree'):
    """ Build the NODE_NAMES dictionary: tree type -> node name -> bl_idname

    To be copied in constants
    """

    def f(node_info, nodes):
        nodes[node_info.bnode.name] = node_info.bnode.bl_idname

    nodes = {}
    for tree_type in ['GeometryNodeTree', 'ShaderNodeTree']:
        nodes[tree_type] = {}
        NodeInfo.loop(f, nodes[tree_type], tree_type=tree_type)
        #if tree_type == 'GeometryNodeTree':
        #    NodeInfo.loop(f, nodes[tree_type], tree_type=tree_type, is_tool=True)


    print("#", "="*125)
    print("# Node bl_idname from node name")
    print("#")
    print("# Generated by node_explore.build_node_names_dict")
    print("#")
    print(f"# Blender version: {bpy.app.version_string}")
    print(f"# Total: GeometryNodeTree: {len(nodes['GeometryNodeTree'])}, ShaderNodeTree: {len(nodes['ShaderNodeTree'])}")
    print()

    print("NODE_NAMES = {")
    for tree_type, d in nodes.items():
        print(f"\t'{tree_type}' :", "{")
        for node_name, blid in d.items():
            sname = f"'{node_name}'"
            print(f"\t\t{sname:30s} : '{blid}',")
        print("\t},")
    print("}\n")
