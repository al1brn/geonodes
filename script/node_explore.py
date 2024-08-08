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

import bpy
import mathutils

from . import constants
from . import utils
from . import blendertree

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

        # ----------------------------------------------------------------------------------------------------
        # Make sure STD_ATTRS is initialized

        if NodeInfo.STD_ATTRS is None:
            ref_node = btree.nodes.new(type='ShaderNodeValue')
            NodeInfo.STD_ATTRS = dir(ref_node)
            btree.nodes.remove(ref_node)

        # ----------------------------------------------------------------------------------------------------
        # Analyze the parameters

        self.params   = {name: getattr(self.bnode, name) for name in dir(self.bnode) if name not in NodeInfo.STD_ATTRS}

        # ----- Parameters in enum

        self.enum_params   = {}
        for param in self.params:
            enums = self.get_enum_list(param)
            if enums is None:
                continue
            self.enum_params[param] = enums

    def __str__(self):
        return f"<Node '{self.bnode.name}' ({self.bnode.bl_idname})>"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Some properties
    #
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
    # Source code generation

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sockets

    def get_sockets(self, self_socket=None, expose_selection=True):

        in_sockets = {}
        counter = {}
        header = []
        ok_self = True
        for bsocket in self.bnode.inputs:

            if not bsocket.enabled or bsocket.type == 'CUSTOM':
                continue

            if bsocket.name == self_socket and ok_self:
                if bsocket.type == 'GEOMETRY':
                    in_sockets[self_socket] = 'self._geo'
                else:
                    in_sockets[self_socket] = 'self'
                ok_self = False

            elif bsocket.name == 'Selection' and not expose_selection:
                in_sockets['Selection'] = 'self._sel'

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

        return {
            'has_items'  : len(in_sockets) > 0,
            'in_sockets' : in_sockets,
            'header'     : header,
            'header_str' : ", ".join([f"{pyname}=None" for pyname in header]),
            'call_str'   : "{" + ", ".join([f"'{socket_name}': {pyname}" for socket_name, pyname in in_sockets.items()]) + "}"
        }

    # -----------------------------------------------------------------------------------------------------------------------------
    # Parameters

    def get_parameters(self):

        header = []
        call   = []

        for param, value in self.params.items():
            if isinstance(value, str):
                header.append(f"{param}='{value}'")
            #elif isinstance(value, (bpy.types.bpy_struct, bpy.types.ID)):
            elif str(value)[0] == '<':
                header.append(f"{param}=None")
            else:
                header.append(f"{param}={value}")

            if param == 'object' and self.btree.bl_idname == 'ShaderNodeTree':
                call.append(f"{param}=get_object({param})")
            else:
                call.append(f"{param}={param}")

        return {
            'has_items'  : len(header) > 0,
            'header_str' : ', '.join(header),
            'call_str'   : ', '.join(call)
        }

    # -----------------------------------------------------------------------------------------------------------------------------
    # Static source

    def yield_static_source(self, func_name=None, as_class_method=True):
        _tab = " "*4

        if func_name is None:
            func_name = self.python_name

        is_prop     = self.in_sockets_count == 0 and len(self.params) == 0
        return_node = self.out_sockets_count > 1

        sockets = self.get_sockets()
        params  = self.get_parameters()

        # ----------------------------------------------------------------------------------------------------
        # Decorators

        if as_class_method:
            yield f"{_tab}@classmethod\n"
            if is_prop:
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

        c3 = '"""'

        yield f"{_tab*2}{c3} Node '{self.bnode.name}' ({self.bnode.bl_idname})\n"
        for param, valids in self.enum_params.items():
            yield f"{_tab*2}- {param} in {valids}\n"
        yield f"{_tab*2}{c3}\n\n"

        # ----------------------------------------------------------------------------------------------------
        # Node call

        yield f"{_tab*2}node = Node('{self.bnode.name}'"
        if sockets['has_items']:
            yield ", " + sockets['call_str']
        if params['has_items']:
            yield ", " + params['call_str']

        yield ")\n"

        # ----------------------------------------------------------------------------------------------------
        # Return

        if return_node:
            yield f"{_tab*2}return node\n\n"
        else:
            yield f"{_tab*2}return node._out\n\n"

    # ====================================================================================================
    # Method Source Code

    def gen_method_source(self, name=None, self_socket=None):
        _tab = " "*4

        if name is None:
            name = self.python_name

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
        yield f"{_tab*2}node = Node('{self.bnode.name}'"

        if len(insockets):
            yield ", {" + ", ".join([f"'{socket_name}': {pyname}" for socket_name, pyname in insockets.items()]) + "}"

        for param in self.params.keys():
            yield f", {param}={param}"

        yield ")\n"
        yield f"{_tab*2}return node._out\n\n"

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
# Gen static functions

def gen_static_class(tree_type='GeometryNodeTree', folder=''):

    def gen_node(node_info, f):
        for chars in node_info.yield_static_source():
            f.write(chars)
        f.write("\n")

    path = Path(folder) / Path('AUTO static_classes.py')
    path.resolve()
    with open(path, 'w') as f:
        f.write("class StaticNodes:\n\n")
        count = loop_on_nodes(gen_node, f, tree_type=tree_type)
        f.write("\n\n")

    print(f"StaticNodes class written ({count} methods or properties) in: '{path.absolute()}'")





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
