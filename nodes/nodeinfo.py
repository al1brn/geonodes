#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:55:10 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : nodeinfo
-----------------
- Dynamically build the node clases and the socket classes
- NodeInfo.__init__:
    - analyze the nodes
    - create the associated class
    - create the socket classes
    - create some sockets methods
    - implement the custom functions declared with custom.add_function
The dynamic biulding is triggered by the instanciation of a Tree class by calling nodeinfo.tree_class_setup.

update : 2024/02/17
"""

from pprint import pprint

import bpy
from geonodes.nodes import documentation
from geonodes.nodes import constants
from geonodes.nodes import custom
from geonodes.nodes import utils
from geonodes.nodes import treestack
from geonodes.nodes.treestack import StackedTree, StackedNode
from geonodes.nodes.sockets import Socket, Sockets

from geonodes.nodes import sockets

# ====================================================================================================
# A node argument

NO_VALUE = 'ARG_NO_VALUE'
IGNORE   = 'ARG_IGNORE'


class Argument:
    
    def __init__(self, name, header=NO_VALUE, call=None, descr=None):
        self.name   = name
        self.header = header
        self.call   = call
        self.descr  = descr
        
    def __str__(self):
        return f"<Argument {self.name}, header={self.header} -> ({self.header_code}), call={self.call} -> ({self.call_code})>"
        
    @property
    def header_code(self):
        if self.header == IGNORE:
            return None

        elif self.header == NO_VALUE:
            return self.name

        else:
            return self.name + "=" + utils.python_constant(self.header)
    
    @property
    def call_code(self):
        # Ignore in call
        if self.call == IGNORE:
            return None

        # Ignored in header and no value specified
        elif self.header == IGNORE and self.call is None:
            print(f"CAUTION: Argument call_code is stange: {self.name=}, {self.header=}, {self.call=}")
            return None
        
        # No value specified
        elif self.call == NO_VALUE:
            return self.name
        
        # selection socket
        elif self.name == 'selection' and self.call is None:
            return f"selection=self._get_selection(selection)"
        
        # name = value
        else:
            return self.name + "=" + (self.name if self.call is None else utils.python_constant(self.call))
    
    @property
    def init(self):
        return f"self.{self.name:15s} = {self.name}"
    
    @property
    def doc(self):
        return f"- {self.name} : {self.descr}\n"
    
class Arguments:
    
    def __init__(self, is_static):
        self.is_static = is_static
        self.args = []
        
    def __str__(self):
        s = f"[Arguments static: {self.is_static}, {len(self.args)}:"
        for arg in self.args:
            s += "\n   " + str(arg)
        return s + "\n]"
        
    def __len__(self):
        return len(self.args)
    
    def __getitem__(self, name):
        for arg in self.args:
            if arg.name == name:
                return arg
        return None
    
    def add(self, name, header=NO_VALUE, call=None, descr=None):
        a = Argument(name, header=header, call=call, descr=descr)
        self.args.append(a)
        return a
    
    @property
    def header_code(self):
        args = ", ".join([arg.header_code for arg in self.args if arg.header != IGNORE])
        if self.is_static:
            return args
        elif args == "":
            return "self"
        else:
            return "self, " + args
    
    @property
    def call_code(self):
        return ", ".join([arg.call_code for arg in self.args if arg.call != IGNORE])
    
    @property
    def init_code(self):
        return "\n\t".join([arg.init for arg in self.args]) + "\n"
    
    @property
    def doc(self):
        return "".join([arg.doc for arg in self.args]) + "\n"
    
    


# ====================================================================================================
# Analyze a node

class NodeInfo:

    def __init__(self, btree, bnode):
        
        # ----- Initialization
        
        self.tree_type   = type(btree).__name__
        
        self.bnode       = bnode
        self.bl_idname   = bnode.bl_idname
        self.name        = bnode.bl_idname if bnode.name == "" else bnode.name
        
        self.class_name  = utils.node_class_name(self.name)
        if self.class_name == 'Color':
            self.python_name = 'color'
        else:
            self.python_name = utils.node_method(self.name)
        
        # ----- Sockets

        self.inputs      = Sockets(self, True)
        self.outputs     = Sockets(self, False)
        
        self.dynamic_in  = self.inputs.has_virtual  or self.bl_idname in constants.CUSTOM_INPUT_SOCKETS
        self.dynamic_out = self.outputs.has_virtual or self.bl_idname in constants.CUSTOM_OUTPUT_SOCKETS
        
        # ----- Parameters
        
        self.analyze_parameters()
        
        # ----- Has a multi input socket
        
        self.has_multi_input = False
        for bsock in bnode.inputs:
            if bsock.is_multi_input:
                self.has_multi_input = True
                self.mi_bsocket = bsock
                self.mi_pyname = utils.socket_name(bsock.name)
                break
        
        # ====================================================================================================
        # When muting a node, internal links are built
        # The first socket with an internal link is used to build a method
        #
        # Example
        # SetMaterial(geometry, material)
        # geometry.set_material(material) implemented as SetMaterial(self, material)
        
        # ----- Force internal links by connecting output sockets to the input sockets
        
        to_delete = []
        for out_socket in bnode.outputs:
            for in_socket in bnode.inputs:
                if in_socket.type == out_socket.type:
                    link = btree.links.new(in_socket, out_socket, verify_limits=True)
                    to_delete.append(link)
                    
        # ----- Capture the internal links which are set when muting the node
        
        int_links = []
        if self.class_name not in ['SeparateComponents']:
            bnode.mute = True
            for link in bnode.internal_links:
                int_links.append((link.from_socket, link.to_socket))
            bnode.mute = False
        
        # ----- Remove the external links
        for link in to_delete:
            if link.from_socket is not None:
                btree.links.remove(link)
            
        self.has_socket_method = len(int_links) > 0
        if self.has_socket_method:
            self.sm_in_bsock   = int_links[0][0]
            self.sm_out_bsock  = int_links[0][1]
            self.sm_pyname     = utils.socket_name(self.sm_in_bsock.name)
            self.sm_out_pyname = utils.socket_name(self.sm_out_bsock.name)
            self.sm_is_multi   = self.sm_in_bsock.is_multi_input
            
        if self.class_name == 'StoreNamedAttribute':
            self.has_socket_method = True
            self.sm_in_bsock   = self.bnode.inputs[0]
            self.sm_out_bsock  = self.bnode.outputs[0]
            self.sm_pyname     = utils.socket_name(self.sm_in_bsock.name)
            self.sm_out_pyname = utils.socket_name(self.sm_out_bsock.name)
            self.sm_is_multi   = False
            
                
        # ====================================================================================================
        # Node attributes

        self.node_attrs = {}
        self.node_args  = []
        
        # ----- Input sockets
        
        for root_name, count in self.in_counts.items():
            for rank in range(count):
                
                pyname = root_name if rank == 0 else f"{root_name}_{rank}"
                
                # ----- Socket argument
                
                sarg_name = pyname
                sarg_val  = pyname
                
                if self.has_socket_method and root_name == self.sm_pyname:
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
                    
                
                # ----- Node argument
                
                self.node_args.append(pyname)
                
        # ----- Output sockets
                
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
            
            self.node_args.append(param)
            
    # =============================================================================================================================
    # Generate the methods
            
    def generate_dynamic_classes(self):
        
        # ====================================================================================================
        # Create the socket classes
        
        nodesocket_classes = constants.nodesocket_classes(self.tree_type)
        socket_classes = constants.socket_classes(self.tree_type)
        node_classes = constants.node_classes(self.tree_type)
        tree_dict = constants.tree_dict(self.tree_type)
        
        bsocks = [bsock for bsock in self.bnode.inputs] + [bsock for bsock in self.bnode.outputs]
        
        for bsock in bsocks:
            if bsock.type not in socket_classes:
                self.add_socket_class(bsock)
            
            if bsock.bl_idname not in nodesocket_classes:
                nodesocket_classes[bsock.bl_idname] = socket_classes[bsock.type]
            
        # ====================================================================================================
        # Node class
        
        # ----- __init__ method

        init_code = self.method_code(self.class_name)
        
        if False and self.class_name in ['SimulationOutput', 'SimulationOutput']:
            print('='*100)
            print("INIT", self.class_name, self.bl_idname)
            print()
            print(init_code)
            print()
        
        # ----- Add the class
        
        self.add_node_class(init_code=init_code, descr=None)
        
        # ----- Domain param and values
        
        setattr(node_classes[self.bl_idname], 'DOMAIN_PARAM',  self.domain_param)
        setattr(node_classes[self.bl_idname], 'DOMAIN_VALUES', self.domain_values)
        
        # ----- Attributes
        
        self.add_attribute(self.class_name, 'bl_idname',   self.bl_idname)
        self.add_attribute(self.class_name, 'params',      self.params)
        self.add_attribute(self.class_name, 'dynamic_in',  self.dynamic_in)
        self.add_attribute(self.class_name, 'dynamic_out', self.dynamic_out)
        
        for name, attr in self.node_attrs.items():
            self.add_property(self.class_name, name, attr['getter'], attr['setter'], attr_type=attr['type'], descr=attr['descr'])
        
        # ====================================================================================================
        # Socket method
        
        ok_method = True
        
        # ----- Standard
        
        if self.has_socket_method and self.class_name not in ['Switch', 'Mix']:
            
            jump = False
            if self.max_out == 1 and self.sm_out_bsock.bl_idname == 'NodeSocketGeometry':
                jump = True
                
            types = [self.sm_in_bsock.type]
            if types[0] == 'INT':
                types.append('VALUE')
            if types[0] == 'VALUE' and self.is_geonodes:
                types.append('INT')
                
            for vtype in types:
                socket_class = socket_classes[vtype]
                
                meth_code, meth_args, node_args = self.method_code(self.python_name,
                            method_type   = 'METHOD', 
                            self_socket   = self.sm_pyname,
                            use_enabled   = False,
                            node_return   = f"self.jump(node.{self.sm_out_pyname})" if jump else f"node.{self.sm_out_pyname}",
                            return_args   = True,
                            )
                
                self.add_method(socket_class.__name__, self.python_name, meth_code, 
                                meth_args = meth_args, node_args = node_args,
                                descr=f"{self.class_name}, {self.sm_pyname}=self")
                
            ok_method = False
            
        # ====================================================================================================
        # One single input socket
        
        if ok_method and self.max_in == 1:
            
            target = constants.SOCKET_CLASS_NAMES[self.bnode.inputs[0].type]
            self_socket = list(self.in_counts.keys())[0]

            return_socket = self.max_out == 1
            
            meth_code, meth_args, node_args = self.method_code(self.python_name,
                        method_type   = 'METHOD', 
                        self_socket   = self_socket,
                        use_enabled   = False,
                        node_return   = "node.output_socket" if return_socket else "node",
                        return_args   = True,
                        )
            
            self.add_method(target, self.python_name, meth_code, is_static=False, 
                            meth_args=meth_args, node_args=node_args,
                            descr=f"{self.class_name}, {self_socket}=self, return {'socket' if return_socket else 'node'}")
            
            ok_method = False
            
        # ====================================================================================================
        # Input nodes
        
        if self.max_in == 0 and self.class_name not in constants.NO_INPUT_NODES:
            
            return_socket = self.max_out == 1
            
            meth_code, meth_args, node_args = self.method_code(self.python_name,
                        method_type   = 'STATIC', 
                        self_socket   = None,
                        use_enabled   = False,
                        node_return   = "node.output_socket" if return_socket else "node",
                        return_args   = True,
                        )
            self.add_function(self.python_name, meth_code, 
                            meth_args=meth_args, node_args=node_args,
                            descr=f"{self.class_name}, return {'socket' if return_socket else 'node'}")

        # ====================================================================================================
        # Single output socket
        
        if self.max_out == 1:
            
            # ----- Already done
            
            if self.python_name not in tree_dict and self.class_name not in constants.CONSTANT_NODES.keys():
                
                meth_code, meth_args, node_args = self.method_code(self.python_name,
                            method_type   = 'STATIC', 
                            self_socket   = None,
                            use_enabled   = False,
                            node_return   = "node.output_socket",
                            return_args   = True,
                            )
                self.add_function(self.python_name, meth_code, 
                            meth_args=meth_args, node_args=node_args,
                            descr=f"{self.class_name}, return single output socket")
                
        # ====================================================================================================
        # Custom methods
        
        self.add_customs()
                

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
        for sck in self.in_socks:
            s += f"\n{tab}{sck[0]:12s} {'X' if sck[1] else '-'} {sck[2]}"
        s += "\n"
        
        s += "\nOutput sockets"
        s += "\n--------------"
        for sck in self.out_socks:
            s += f"\n{tab}{sck[0]:12s} {'X' if sck[1] else '-'} {sck[2]}"
        s += "\n"
        
        return s
    
    # ====================================================================================================
    # Analyze the effect of changing a parameter
    
    def get_enum_list(self, param):
        
        value = self.prm_defs[param]
        if not isinstance(value, str):
            return None
        
        try:
            setattr(self.bnode, param, 'ERROR')
        except TypeError as e:
            msg = str(e)
            i = msg.find('enum "ERROR" not found in')
            if i <= 0:
                return None
            
            return eval(msg[i+26:])
        
        return None
    
    def reset_params(self):
        for param, value in self.prm_defs.items():
            setattr(self.bnode, param, value)
    
    def analyze_parameters(self):
        
        # ----- Max number of sockets per name
        
        self.in_counts  = self.inputs.enabled_counts()
        self.out_counts = self.outputs.enabled_counts()

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
                        self.domain_values = enums
                        break
                
        # ----- DEBUG

        if False and self.class_name in ['Math', 'BooleanMath', 'VectorMath', 'Mix']:
            print('-'*30)
            print(self.class_name)
            pprint(self.enum_params)
        
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
                  **kwargs):           # Fixed node arguments
        
        """ Build the arguments list.
        
        if the argument 'self_socket' is None, the Arguments list is initialized as static
        
        Arguments
        ---------
            - self_socket (str = None) : Name of the socket to plug self (is excluded from argument list)
            - use_enabled (bool = False) : compute the current count per socket if True else get node.max_per_name
            - node_label (bool = True) : add node_label and node_color arguments
            - kwargs : Fixed arguments
            
        Returns
        -------
            - Arguments
        """

        # ----------------------------------------------------------------------------------------------------
        # Lists initialization
        
        args = Arguments(self_socket is None)

        if self.has_multi_input:
            args.add("*args", NO_VALUE, NO_VALUE)
            
        # ----------------------------------------------------------------------------------------------------
        # Set up the node

        prm_defs = {**self.prm_defs}
        prm_vals = {}
        
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
            if param not in kwargs:
                prm_vals[param] = self.get_enum_list(param)
                
        # ----- Restore parameters
        if not all_sockets:
            self.setup(**mems)

        #else:
        #    in_counts = {**self.in_counts}
            
        #    # Param possible values
        #    for param in self.params:
        #        if param not in kwargs:
        #            prm_vals[param] = self.get_enum_list(param)
            
            
        if self_socket is not None:
            in_counts[self_socket] -= 1
            
        # ----------------------------------------------------------------------------------------------------
        # Input sockets
        
        if len(in_counts) > 0:

            for sock_name in utils.input_sockets_order(in_counts):
                
                descr = f"Socket"
                
                count = in_counts[sock_name]
                
                # ----- Socket where to plug self
                
                if sock_name == self_socket:
                    if sock_name in kwargs:
                        args.add(sock_name, None, kwargs[sock_name], descr=descr)
                    else:
                        args.add(sock_name, IGNORE, 'self', descr=descr)

                # ----- Loop on the sockets sharing the same name

                for i in range(count):
                    sock_i = sock_name if i == 0 else f"{sock_name}_{i}"
                    
                    if self_socket == sock_name:
                        if i == 0:
                            args.add(f"{sock_name}_1", None, sock_name, descr=descr)
                        else:
                            args.add(f"{sock_name}_{i+1}", None, sock_i, descr=descr)
                            
                    elif sock_i in kwargs:
                        args.add(sock_i, None, kwargs[sock_i], descr=descr)
                        
                    #elif sock_i == 'selection':
                    #    args.add('selection', None, 'self._get_selection(selection)', descr=descr)
                        
                    else:
                        args.add(sock_i, None, descr=descr)
                            
        # ----------------------------------------------------------------------------------------------------
        # Parameters

        for param in self.params:
            if param in kwargs:
                args.add(param, IGNORE, kwargs[param])
            else:
                descr = f"Parameter"
                vals = prm_vals[param]
                if vals is not None:
                    descr += f" in {vals}"
                args.add(param, prm_defs[param], descr=descr)
                    
        # ----- Replace: domain = DEFAULT by domain = self._get_domain(DEFAULT)
        
        if self.domain_param is not None:
            arg = args[self.domain_param]
            if arg is not None:
                if arg.call is None:
                    arg.call = f"self._get_domain({utils.python_constant(prm_defs[self.domain_param])})"
                else:
                    arg.call = f"self._get_domain({arg.call})"
                
        # ----------------------------------------------------------------------------------------------------
        # Node_label and node_color
        
        if node_label:
            args.add('node_label', None)
            args.add('node_color', None)
                
        # ----------------------------------------------------------------------------------------------------
        # Return the arguments
        
        return args
    
    # ====================================================================================================
    # Create the node
    
    def node_class_init_code(self):
        
        args = self.build_meth_args()
        args.is_static = False
        
        return f"def __init__({args.header_code}):\n\t{args.init_code}\n"
    
    def class_method_code(self, name, self_socket, jump=None, ret_socket=None, **kwargs):
        
        args = self.build_meth_args(self_socket=self_socket, **kwargs)
        
        # Header
        s = f"def {name}({args.header_code}):\n"
        
        # Create the node
        s += f"\tnode = self.tree.{self.class_name}({args.call_code})\n"
        
        # Self jump
        if jump is not None:
            s += f"\tself.jump(node.{jump})\n"
            
        # Return node or socket
        if ret_socket is None:
            s += "\treturn node\n"
            
        elif ret_socket == 'self':
            s += "\treturn self\n"

        else:
            s += f"\treturn node.{ret_socket}\n"
            
        return s
    
    def class_getter_code(self, name, self_socket=None, jump=None, ret_socket=None, **kwargs):

        args = self.build_meth_args(self_socket=self_socket, node_label=False, **kwargs)
        args.is_static = False
        
        # Header
        s = f"def {name}(self):\n"
        
        # Create the node
        s += f"\tnode = self.tree.{self.class_name}({args.call_code})\n"
        
        # Self jump
        if jump is not None:
            s += f"\tself.jump(node.{jump})\n"
            
        # Return node or socket
        if ret_socket is None:
            s += "\treturn node"
        else:
            s += f"\treturn node.{ret_socket}"
            
        return s

    def class_setter_code(self, name, self_socket, value_socket, jump=None, **kwargs):

        args = self.build_meth_args(self_socket=self_socket, node_label=False, **{value_socket: 'value'}, **kwargs)
        
        # Header
        s = f"def {name}(self, value):\n"
        
        # Create the node
        s += f"\tnode = self.tree.{self.class_name}({self_socket}=self, {value_socket}=value"
        
        # Selection socket
        if args['selection'] is not None and 'selection' not in kwargs:
            s +=  ", selection=self._get_selection(None)"
            
        # kwargs
        for k, v in kwargs.items():
            s += f", {k}={v}"
            
        # Done
        s += ")\n"
        
        # Self jump
        if jump is not None:
            s += f"\tself.jump(node.{jump})\n"
            
        return s
        
        
            
        
    

    
    # ====================================================================================================
    # Create a node class
    
    def method_code(self, name,
                    method_type   = 'INIT',
                    self_socket   = None, 
                    use_enabled   = False,
                    node_label    = True, 
                    node_return   = "node", 
                    debug         = None, 
                    return_args   = False,
                    **kwargs):
        
        """ Build the arguments string for the header of a function.
        
        The 'method_type' argument can be:
            - INIT : (self, all sockets, all params)
            - METHOD : (self, sockets, params)
            - STATIC : (sockets, params)
            
        For none static methods, self_socket indicates the socket to exclude from the list.
        
        The list of sockets can be:
            - The maximum possible sockets given by self.in_counts
            - The currently enabled sockets given by self.inputs.enabled_counts()
        
        Arguments
        ---------
            - name (str) : method name
            - method_type (str  = 'INIT') : method type in 'INIT', 'STATIC', 'METHOD' 
            - self_socket (str = None) : Name of the socket to plug self (is excluded from argument list)
            - use_enabled (bool = False) : compute the current count per socket if True else get node.max_per_name
            - node_label (bool = True) : add node_label and node_color arguments
            - node_return (str = 'node') : can be replaced by 'self.jump(node)' or 'node.output_socket' for instance
            - debug (str = None) : additional lines to insert
            - return_args (bool = False) : return tuple (code, args, call_args) if True
            - kwargs : param, value to exclude
            
        Returns
        -------
            - str : function source code
        """

        # ----------------------------------------------------------------------------------------------------
        # Variables
        
        args = []
        is_init = method_type == 'INIT'
        call_args = []
        
        if is_init:
            sock_setter  = ""
            param_setter = ""

        # ----------------------------------------------------------------------------------------------------
        # Multi
        
        if method_type != 'STATIC':
            args.append("self")

        if self.has_multi_input:
            args.append("*args")
            if not is_init:
                call_args.append("*args")

        # ----------------------------------------------------------------------------------------------------
        # Input sockets
            
        if use_enabled:
            in_counts = self.inputs.enabled_counts()
        else:
            in_counts = {**self.in_counts}
            
        if self_socket is not None:
            in_counts[self_socket] -= 1
            
        # ----- Loop on the sockets with selection as last argument
        
        if len(in_counts) > 0:

            if is_init:
                sock_setter = f"\t# Input sockets\n"
                if self.has_multi_input:
                    sock_setter += f"\tself._set_multi_input(*args)\n"

            for sock_name in utils.input_sockets_order(in_counts): #, count in in_counts.items():
                
                count = in_counts[sock_name]
                
                if not is_init and sock_name == self_socket:
                    if sock_name in kwargs:
                        call_args.append((sock_name, kwargs[sock_name]))
                    else:
                        call_args.append((sock_name, "self"))

                for i in range(count):
                    sock_i = sock_name if i == 0 else f"{sock_name}_{i}"
                    args.append((sock_i, "None"))
                    
                    if is_init:
                        sock_setter += f"\tself.{sock_i:12s} = {sock_i}\n"
                    else:
                        if self_socket == sock_name:
                            if i == 0:
                                call_args.append((f"{sock_name}_1", sock_name))
                            else:
                                call_args.append((f"{sock_name}_{i+1}", sock_i))
                                
                        elif sock_i in kwargs:
                            call_args.append((sock_i, kwargs[sock_i]))
                            
                        elif sock_i == 'selection':
                            call_args.append(('selection', 'self._get_selection(selection)'))
                            
                        else:
                            call_args.append((sock_i, sock_i))
                            
        # ----------------------------------------------------------------------------------------------------
        # Parameters
        
        if is_init or len(kwargs) == 0:
            args.extend([(param, utils.python_constant(self.prm_defs[param])) for param in self.params])
            
        if is_init:
            if len(self.params):
                param_setter = "\t# Node parameters\n" + "".join([f"\tself.{param:12s} = {param}\n" for param in self.params]) + "\n"
            
        else:
            # ----- Build the call_args list
            
            if len(kwargs) == 0:
                call_args.extend([(param, param) for param in self.params])
                
            else:
                for param in self.params:
                    if param in kwargs:
                        call_args.append((param, kwargs[param]))
                    else:
                        args.append((param, utils.python_constant(self.prm_defs[param])))
                        call_args.append((param, param))
                        
            # ----- Replace: domain = DEFAULT by domain = self._get_domain(DEFAULT)
            
            if self.domain_param is not None:
                for i, item in enumerate(call_args):
                    if not isinstance(item, tuple):
                        continue
                    if item[0] == self.domain_param:
                        call_args[i] = (self.domain_param, f"self._get_domain({item[1]})")
                        break
                        
        # ----------------------------------------------------------------------------------------------------
        # Node label
        
        if node_label:
            args.append(("node_label", "None"))
            args.append(("node_color", "None"))
            
            if not is_init:
                call_args.append(("node_label", "node_label"))
                call_args.append(("node_color", "node_color"))
                
        # ----------------------------------------------------------------------------------------------------
        # Debug
        
        if debug is not None:
            lines = "\n".split(debug)
            debug_lines = "\n\t" + "\n\t".join(lines) + "\n\n"
                
        # ----------------------------------------------------------------------------------------------------
        # Let's build all of that
        
        all_args = ", ".join([f"{item[0]}={item[1]}" if isinstance(item, tuple) else item for item in args])
        
        if is_init:
            #s = f"def {name}(" + ", ".join(args) + "):\n"
            s = f"def {name}(" + all_args + "):\n"
            s += constants.IMPORT_BASE_NODE
            if debug is not None:
                s += debug_lines
            s += f"\t{constants.BASE_NODE}.__init__(self, '{self.bl_idname}', node_label=node_label, node_color=node_color)\n\n"
            s += param_setter
            s += sock_setter
            
        else:
            all_call = ", ".join([f"{item[0]}={item[1]}" if isinstance(item, tuple) else item for item in call_args])

            s = f"def {name}(" + all_args + "):\n"
            s += constants.IMPORT_TREE
            if debug is not None:
                s += debug_lines
            #s += f"\tnode = {constants.CUR_TREE}().{self.class_name}(" + ", ".join(call_args) + ")\n"
            s += f"\tnode = {constants.CUR_TREE}().{self.class_name}(" + all_call + ")\n"
            s += f"\treturn {node_return}\n\n"
            
            
        if return_args:
            return s, args, call_args
        else:
            return s
    
    # =============================================================================================================================
    # Custom methods
        
    def add_customs(self):
        
        def add_from_dict(name, cust):
            
            # ----- Loop on loops
            
            loops = cust['loops']
            if len(loops):
                key = loops[0]
                values = utils.get_enum_list(self.bnode, key)
                
                
                if False and self.class_name == 'SeparateColor':
                    print(f"CUSTOM {self.class_name}, {key} = {values}")
                
                loops2 = list(loops[1:])
                mem_key = getattr(self.bnode, key)
                for value in values:
                    
                    if key == 'operation':
                        rep = utils.operation_name(value)
                        if self.class_name == 'Math' and rep in ['compare', 'less_than', 'greater_than'] and self.is_geonodes:
                            rep = 'math_' + rep
                    elif key == 'data_type':
                        rep = utils.data_type_name(value, all_names=values)
                    else:
                        rep = value.lower()
                    name2 = name.replace(key.upper(), rep)

                    cust2 = {**cust}
                    cust2['loops']       = loops2
                    cust2['use_enabled'] = True
                    cust2['kwargs'][key] = value
                    cust2['descr'] += f", {key}='{value}'"
                    
                    setattr(self.bnode, key, value)
                    add_from_dict(name2, cust2)

                setattr(self.bnode, key, mem_key)
                return

            # ----- Save the modified params and set the required value
            
            kwargs = {**cust['kwargs']}
            mems = {}
            
            for k in self.params:
                if k in kwargs.keys():
                    # Raise Type Error if the value is not a valid value
                    # For instance domain=self.domain_name rather that domain='FACE'
                    try:
                        mems[k] = getattr(self.bnode, k)
                        setattr(self.bnode, k, kwargs[k])
                        kwargs[k] = utils.python_constant(kwargs[k])
                    except TypeError as e:
                        pass

            # ----- Source code

            is_static = cust['self_socket'] is None or cust['target'] is None
            meth_code, meth_args, node_args = self.method_code(name,
                    method_type     = 'STATIC' if is_static else 'METHOD', 
                    self_socket     = None if cust['target'] is None else cust['self_socket'], 
                    use_enabled     = cust['use_enabled'],
                    node_label      = cust['node_label'], 
                    node_return     = cust['node_return'], 
                    debug           = cust['debug'],
                    return_args     = True,
                    **kwargs,
                    )

            # ----- Restore the params
            
            for k in reversed(mems.keys()):
                setattr(self.bnode, k, mems[k])
                
            # ----- Compile the function
            
            descr = cust['descr']
            target_class_name = cust['target']
            if target_class_name == 'SOCKET':
                self_socket = cust['self_socket']
                if self_socket is None:
                    raise AttributeError(f"Custom function error: class {self.class_name}. 'self_socket' can't be None but a valid input socket.")
                bl_id = self.inputs.enabled_homonyms(self_socket)[0].bl_idname
                target_class_name = constants.nodesocket_classes(self.tree_type)[bl_id].__name__
                descr = descr.replace('SOCKET', target_class_name)
                
            # ----- Debug

            if False and self.class_name == 'StoreNamedAttribute':
                print("=====", self.class_name, '-->', target_class_name, "//",  descr)
                print(meth_code)
                
            # ----- Set the function globally or to the target class
                    
            if is_static:
                if target_class_name is None:
                    self.add_function(name, meth_code, descr=descr, meth_args=meth_args, node_args=node_args)
                else:
                    self.add_method(target_class_name, name, meth_code, is_static=True, descr=descr, meth_args=meth_args, node_args=node_args)
            else:
                self.add_method(target_class_name, name, meth_code, descr=descr, meth_args=meth_args, node_args=node_args)
                
        # ----------------------------------------------------------------------------------------------------
        # Main

        custs = custom.get_custom(self.tree_type, self.class_name)
        if custs is None:
            return
        
        for name, cust in custs.items():
            targets = cust['target']
            if not isinstance(targets, tuple):
                targets = (targets,)
                
            for target in targets:
                cust2 = {**cust}
                cust2['target'] = target
                descr = f"{self.class_name}"
                if cust2['descr'] is None:
                    cust2['descr'] = descr
                else:
                    cust2['descr'] = descr + ", " + cust2['descr']
                    
                add_from_dict(name, cust2)
    
    # ====================================================================================================
    # Add code
    
    # ----------------------------------------------------------------------------------------------------
    # Register a class
    
    def register_class(self, the_class, category, descr=None):

        tree_dict = constants.tree_dict(self.tree_type)
        class_name = the_class.__name__
        the_class._tree_type = self.tree_type

        if class_name in tree_dict:
            return Exception(f"Class {class_name} already registered.")
        
        # ----- Register globally

        tree_dict[class_name] = the_class
        
        # ----- Documentation
        
        doc = documentation.doc_dict(self.tree_type, class_name)
        doc['category'] = category
        doc['descr']    = descr
    
    # ----------------------------------------------------------------------------------------------------
    # Add a new node class
    
    def add_node_class(self, init_code=None, descr=None):
        
        node_classes = constants.node_classes(self.tree_type)
        tree_dict    = constants.tree_dict(self.tree_type)
        
        class_name = self.class_name
        if class_name in tree_dict:
            print(f"CAUTION node class {class_name} registered twice! (Class {self.class_name})")
            
        # ----- Create the class
        
        methods = {'_tree_type': self.tree_type}
        if init_code is not None:
            methods['__init__'] = utils.compile_f(init_code, self.class_name) #, treestack.__dict__)
        node_classes[self.bl_idname] = type(class_name, (StackedNode,), methods)
        
        tree_dict[class_name] = node_classes[self.bl_idname]
        
        # ----- Documentation
        
        doc = documentation.doc_dict(self.tree_type, class_name)
        doc['category']  = 'Node'
        doc['bl_idname'] = self.bl_idname
        doc['pyname']    = self.python_name
        doc['node name'] = self.name
        doc['descr']     = descr
        doc['code']      = init_code
        
        doc['params']         = {param: utils.python_constant(value) for param, value in self.prm_defs.items()}
        doc['input_sockets']  = self.inputs.sockets_doc(enabled_only=False)
        doc['output_sockets'] = self.outputs.sockets_doc(enabled_only=False)
        
        # Create entry for cross reference
        
        documentation.new_cross_ref(self.tree_type, self.class_name)
        
    # ----------------------------------------------------------------------------------------------------
    # Add a new socket class
    
    def add_socket_class(self, bsocket, descr=None):
        
        socket_classes     = constants.socket_classes(self.tree_type)
        nodesocket_classes = constants.socket_classes(self.tree_type)
        tree_dict          = constants.tree_dict(self.tree_type)
        
        if bsocket.type in socket_classes:
            return socket_classes[bsocket.type]
        
        class_name = constants.SOCKET_CLASS_NAMES[bsocket.type]

        if class_name in tree_dict:
            print(f"CAUTION socket class {class_name} registered twice! (Class {self.class_name})")
            
        # ----- Create the class
        
        base_class = sockets.Geometry if class_name == 'Geometry' else sockets.Socket
        socket_classes[bsocket.type] = type(class_name, (base_class,), {'_tree_type': self.tree_type})
        tree_dict[class_name] = socket_classes[bsocket.type]
            
        if bsocket.bl_idname not in nodesocket_classes:
            nodesocket_classes[bsocket.bl_idname] = socket_classes[bsocket.type]
            
        # ----- Documentation
        
        doc = documentation.doc_dict(self.tree_type, class_name)
        doc['category']    = 'Socket'
        doc['socket type'] = bsocket.type
        doc['bl_idname']   = utils.nodesocket_main_class(bsocket.bl_idname)
        doc['descr']       = descr
        
        # ----- Register Domain class if Geometry
        
        if False and class_name == 'Geometry':
            self.register_class(sockets.Domain, 'Other', descr="Geometry domain")
        
        return socket_classes[bsocket.type]
    
    # ----------------------------------------------------------------------------------------------------
    # Add a new attribute to a class
    
    def add_attribute(self, class_name, name, value, attr_type='Attributes', descr=None):
        
        tree_dict = constants.tree_dict(self.tree_type)
        the_class = tree_dict[class_name]
        
        # ----- Add the attribute

        if name in the_class.__dict__:
            print(f"CAUTION {class_name}: member {name} (attribute) already registered! (Class {self.class_name})")
        
        setattr(the_class, name, value)
        
        # ----- Documentation
        
        doc = documentation.doc_dict(self.tree_type, class_name)['members']
        
        doc[name] = {'name'  : name,
                     'type'  : attr_type, 
                     'value' : value, 
                     'descr' : value if descr is None else descr}
        
    # ----------------------------------------------------------------------------------------------------
    # Add a new node class method
    
    def add_property(self, class_name, name, getter=None, setter=None, attr_type='Properties', descr=None):
        
        tree_dict = constants.tree_dict(self.tree_type)
        the_class = tree_dict[class_name]
        
        # ----- Add the property
        
        if name in the_class.__dict__:
            print(f"CAUTION {class_name}: member {name} (property) already registered! (Class {self.class_name})")
        
        fget = None if getter is None else utils.compile_f(getter, name)
        fset = None if setter is None else utils.compile_f(setter, name)
        setattr(the_class, name, property(fget, fset))
        
        # ----- Documentation
        
        documentation.add_property_doc(self.tree_type, class_name, name,
                 attr_type     = attr_type,
                 getter_node   = None,
                 setter_node   = None,
                 getter        = getter,
                 setter        = setter,
                 descr         = descr,
                 )

    # ----------------------------------------------------------------------------------------------------
    # Add a new node class method
    
    def add_method(self, class_name, name, code, is_static=False, descr=None, meth_args=None, node_args=None):
        
        tree_dict = constants.tree_dict(self.tree_type)
        the_class = tree_dict[class_name]
        
        # ----- Add the method / function

        if name in the_class.__dict__:
            print(f"CAUTION {class_name}: member {name} (method) already registered! (Class {self.class_name})")
        
        f = utils.compile_f(code, name)
        f._tree_type  = self.tree_type
        f._class_name = class_name
        if is_static:
            if name in tree_dict:
                print(f"CAUTION {class_name}: global function {name} (static method) already registered! (Class {self.class_name})")
                
            f = staticmethod(f)
            tree_dict[name] = f
            
        setattr(the_class, name, f)
        
        # ----- Documentation
        
        documentation.add_method_doc(self.tree_type, class_name, name,
                        attr_type  = 'Methods',
                        static     = is_static,
                        bl_idname  = self.bl_idname,
                        node_class = self.class_name,
                        code       = code,
                        meth_args  = meth_args,
                        node_args  = node_args,
                        descr      = descr,
                        )
        
    # ----------------------------------------------------------------------------------------------------
    # Add a global function
    
    def add_function(self, name, code, descr=None, meth_args=None, node_args=None):
        
        if name == 'vector':
            print("OUPS "*100)
            print(self.class_name)
            print(code)
            aa
        
        tree_dict = constants.tree_dict(self.tree_type)
        
        # ----- Add the function

        if name in tree_dict:
            print(f"CAUTION function {name} registered twice! (Class {self.class_name})")
            
        f = staticmethod(utils.compile_f(code, name))
        f._tree_type  = self.tree_type
        f._class_name = 'GLOBAL'
        tree_dict[name] = f
        
        # ----- Documentation
        
        documentation.add_method_doc(self.tree_type, None, name,
                        attr_type  = 'Functions',
                        bl_idname  = self.bl_idname,
                        node_class = self.class_name,
                        code       = code,
                        meth_args  = meth_args,
                        node_args  = node_args,
                        descr      = descr,
                        )
        
        
# ====================================================================================================
# Nodes list

def list_nodes(tree_type='GeometryNodeTree'):
    
    print("="*100)
    print("List of nodes")
    print()
    
    btree = treestack.get_tree("TREE - Temp", tree_type=tree_type, create=True, clear=True)
    
    for type_name in dir(bpy.types):
        
        try:
            bnode = btree.nodes.new(type=type_name)
        except RuntimeError as e:
            continue
        
        if 'legacy' in bnode.name.lower():
            continue
        
        class_name = utils.node_class_name(bnode.name)
        
        has_geo = False
        for bsock in bnode.inputs:
            if bsock.type == 'GEOMETRY':
                has_geo = True
        for bsock in bnode.outputs:
            if bsock.type == 'GEOMETRY':
                has_geo = True
                
        if has_geo:
            print(f"{class_name:20s} {has_geo=}")
        
    print()
    treestack.del_tree(btree.name)
    
# ====================================================================================================
# Loop on the nodes

def loop_on_nodes(tree_type='GeometryNodeTree', func=lambda node_info: None):
    
    # ====================================================================================================
    # Node and Socket classes
    
    btree = treestack.get_tree("TREE - Temp", tree_type=tree_type, create=True, clear=True)
    
    for type_name in dir(bpy.types):
        try:
            bnode = btree.nodes.new(type=type_name)
        except RuntimeError as e:
            continue
        
        if 'legacy' in bnode.name.lower():
            continue
        
        node_info = NodeInfo(btree, bnode)
        
        func(node_info)

    treestack.del_tree(btree.name)
    
    
# ====================================================================================================
# Initialize a tree type

def tree_class_setup(tree_type):
    
    # ====================================================================================================
    # Node and Socket classes
    
    btree = treestack.get_tree("TREE - Temp", tree_type=tree_type, create=True, clear=True)
    
    for type_name in dir(bpy.types):
        try:
            bnode = btree.nodes.new(type=type_name)
        except RuntimeError as e:
            continue
        
        if 'legacy' in bnode.name.lower():
            continue
        
        node_info = NodeInfo(btree, bnode)
        
        node_info.generate_dynamic_classes()
        
    # ----- Custom properties
    
    custom.create_properties(tree_type)
        
    # ====================================================================================================
    # Documentation
    # Very slooowwww
    
    if False:
        for the_class in tree_dict.values():
            doc = documentation.Doc(tree_type)
            
            for name, the_class in tree_dict.items():
                if type(the_class).__name__ != 'type':
                    continue
                
                doc.class_doc(name)
                the_class.__doc__ = doc.text
                doc.clear()
            

    # ====================================================================================================
    # Done

    treestack.del_tree(btree.name)
    
# ====================================================================================================
# Imort tree dictionaty into locals
    
def tree_import(tree_type, names):
    for name, obj in constants.tree_dict(tree_type).items():
        names[name] = obj



    
                
            
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    

