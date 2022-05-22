#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 10:56:43 2022

@author: alain
"""

from pprint import pprint, pformat
import bpy

_0_ = " "*0
_1_ = " "*4
_2_ = " "*8
_3_ = " "*12

NODE_ATTRS = ['__doc__', '__module__', '__slots__',
    'bl_description', 'bl_height_default', 'bl_height_max', 'bl_height_min', 'bl_icon',
    'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type', 'bl_width_default',
    'bl_width_max', 'bl_width_min',
    'color', 'dimensions', 'draw_buttons', 'draw_buttons_ext', 'height', 'hide',
    'input_template', 'inputs', 'internal_links', 'is_registered_node_type',
    'label', 'location', 'mute', 'name', 'output_template',
    'outputs', 'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options',
    'show_preview', 'show_texture', 'socket_value_update', 'type', 'update',
    'use_custom_color', 'width', 'width_hidden',
    'color_mapping', 'texture_mapping',
    ]
    
SOCKET_TYPES = {
    'NodeSocketVectorEuler'       : 'Vector',
    'NodeSocketFloatFactor'       : 'Float',
    'NodeSocketVector'            : 'Vector',
    'NodeSocketBool'              : 'Boolean',
    'NodeSocketFloat'             : 'Float',
    'NodeSocketInt'               : 'Integer',
    'NodeSocketColor'             : 'Color',
    'NodeSocketString'            : 'String',
    'NodeSocketFloatAngle'        : 'Float',
    'NodeSocketVectorXYZ'         : 'Vector',
    'NodeSocketGeometry'          : 'Geometry',
    'NodeSocketIntUnsigned'       : 'Integer',
    'NodeSocketVectorTranslation' : 'Vector',
    'NodeSocketFloatDistance'     : 'Float',
    'NodeSocketObject'            : 'Object',
    'NodeSocketCollection'        : 'Collection',
    'NodeSocketTexture'           : 'Texture',
    'NodeSocketMaterial'          : 'Material',
    'NodeSocketImage'             : 'Image',
    'NodeSocketVirtual'           : 'Virtual',
}

# ====================================================================================================
# Socket

class Socket:
    def __init__(self, bsocket, index):
        
        self.bsocket = bsocket
        self.index   = index

        # ----- Name and unique name
        
        self.name  = self.user_name(self.bsocket.name)
        self.uname = self.name
        
        # ----- Class name
        
        self.class_name = SOCKET_TYPES[self.bsocket.bl_idname]
        if self.bsocket.name in ['Mesh', 'Points', 'Instances', 'Volume', 'Curve', 'Spline']:
            self.class_name = self.bsocket.name
            
        # ----- Parameters which enable or not this socket (see enabling_params)

        self.param_0 = {}
        self.param_1 = {}

        # ----- Default enablement
        
        self.def_enabled = self.enabled
        
    # ----------------------------------------------------------------------------------------------------
    # User friendly name
        
    @staticmethod
    def user_name(name):
        if name == 'ID':
            return name
        return name.lower().replace(' ', '_')
        
    # ----------------------------------------------------------------------------------------------------
    # Properties read from Blender socket
        
    @property
    def bl_idname(self):
        return self.bsocket.bl_idname
    
    @property
    def enabled(self):
        return self.bsocket.enabled
    
    @property
    def is_output(self):
        return self.bsocket.is_output

    @property
    def is_multi_input(self):
        return self.bsocket.is_multi_input
    
    # ----------------------------------------------------------------------------------------------------
    # Initalization source code
    #
    # Input socket sample:
    # SocketIn(self, 'NodeSocketVectorEuler', 'rotation')
    #
    # Output socket sample:
    # Socket(self, 'NodeSocketGeometry', 'geometry')

    @property
    def gen_init(self):
        sblid   = f"'{self.bl_idname}'"
        sname   = f"'{self.uname}'"
        scommon = f"self, {sblid:25s}, {sname:15s}"
        
        if self.bsocket.is_output:
            return f"Socket ({scommon})"
        else:
            has_default = hasattr(self.bsocket, 'default_value')
            s = f"SocketIn({scommon}"
            if self.is_multi_input:
                s += ", is_multi_input=True"
            return s + ")"
    
    # ----------------------------------------------------------------------------------------------------
    # When an enum parameter is read from a Node, all its possibles values are tried
    # At each try, the enablement of the socket is stored:
    # - param_1 if enabled
    # - param_0 otherwise
    # If one of these two lists is empty, it does mean that the parametert doesn't drive the enablement
    # This properpty return the enabling params if any
    
    @property
    def enabling_params(self):
        ch = None
        for param_name in self.param_0:
            if len(self.param_0[param_name]) != 0 and len(self.param_1[param_name]) != 0:
                if ch is None:
                    ch = {}
                ch[param_name] = self.param_1[param_name]
        return ch
       
# ----------------------------------------------------------------------------------------------------
# A list of sockets
# Initialized either from inputs or from outputs

class Sockets(list):
   
    @classmethod
    def Inputs(cls, bnode):
        inputs = cls()
        for index, bsocket in enumerate(bnode.inputs):
            inputs.append(Socket(bsocket, index))
        inputs.check_uniques()
        return inputs
           
    @classmethod
    def Outputs(cls, bnode):
        outputs = cls()
        for index, bsocket in enumerate(bnode.outputs):
            outputs.append(Socket(bsocket, index))
        outputs.check_uniques()
        return outputs
    
    @property
    def build_unames(self):
        
        def count_name(name):
            count = 0
            for socket in self:
                if socket.enabled and socket.name == name:
                    count += 1
            return count
        
        def uname(name, socket_index):
            count = 0
            for i, socket in enumerate(self):
                if socket.enabled and socket.name == name:
                    if i == socket_index:
                        return f"{name}{count}"
                    else:
                        count += 1
        
        unames = [None] * len(self)
        for i, socket in enumerate(self):
            if socket.enabled:
                count = count_name(socket.name)
                if count == 1:
                    unames[i] = socket.name
                else:
                    unames[i] = uname(socket.name, i)
                    
        return unames
    
    def set_unames(self, unames):
        for socket, uname in zip(self, unames):
            if uname is not None:
                if uname != socket.name:
                    if socket.uname != socket.name:
                        if socket.uname != uname:
                            raise RuntimeError("Algorithm error with unnames. Two possible unames for socket '{socket.name}' ({socket.index}) in node '{self.bnode.bl_idname}': '{socket.uname}' or '{uname}'!")
                    socket.uname = uname
                    
    def update_unames(self):
        self.set_unames(self.build_unames)
        
    def get_unames(self, enabled=True):
        if enabled:
            unames = []
            for socket in self:
                if socket.enabled:
                    unames.append(socket.uname)
            return unames
        else:
            return [socket.uname for socket in self]

    
    """
                
    # ----------------------------------------------------------------------------------------------------
    # Get the socket index using the uname as a key
                
    def socket_from_uname(self, uname):
        socks   = []
        enabled = []
        for sock in self:
            if sock.uname == uname:
                socks.append(sock)
                if sock.enabled:
                    enabled.append(sock)
                    
        if len(socks) == 0:
            for sock in self:
                print(f"{sock.index}: name: {sock.name}, uname: {sock.uname}")
            raise RuntimeError(f"Input socket '{uname}' not found.")
            
        elif len(socks) == 1:
            return socks[0]
        
        elif len(enabled) == 0:
            return None
        
        elif len(enabled) != 1:            
            for sock in self:
                print(f"{sock.index}: name: {sock.name}, uname: {sock.uname}, enabled={sock.enabled}")
            raise RuntimeError(f"Severable input sockets with uname '{uname}' are enabled: {len(enabled)} found!")

        else:
            return enabled[0]
        
    """
        
    # ----------------------------------------------------------------------------------------------------
    # Get the multi input socket if exists
    
    @property
    def multi_input_index(self):
        for i, socket in enumerate(self):
            if socket.is_multi_input:
                return i
        return None
    
    # ----------------------------------------------------------------------------------------------------
    # Has a geometry input socket
    
    @property
    def geometry_socket_index(self):
        for i, socket in enumerate(self):
            if socket.bsocket.type == 'GEOMETRY':
                if hasattr(socket, 'is_multi_input'):
                    if socket.is_multi_input:
                        continue
                return i
        return None

    @property
    def has_geometry_socket(self):
        return self.geometry_socket_index is not None
        
    # ----------------------------------------------------------------------------------------------------
    # Manage the enablement when a parameter varies
    
    def new_param(self, param_name):
        for sock in self:
            sock.param_0[param_name] = []
            sock.param_1[param_name] = []
            
    def new_param_value(self, param_name, value):
        for sock in self:
            if sock.enabled:
                sock.param_1[param_name].append(value)
            else:
                sock.param_0[param_name].append(value)
                
    # Some sockets can share the same unique name
    # 'uniques' property return a dictionary of the unique names
    # Each value of the dictionary contains:
    # - None : the unique name is always valid and point on only one socket
    # - dict : a dict keyed by the socket indices with the {param: [values]} driving the enablement
    #
    # 'value' : {0: {'data_type': ['FLOAT']},
    #            1: {'data_type': ['INT']},
    #           }
                
    @property
    def uniques(self):
        uns = {}
        for i, sock in enumerate(self):
            uname = sock.uname
            ch    = sock.enabling_params
            
            if uname in uns:
                cur = uns[uname]
                if cur is None:
                    for sock in self:
                        print(f"   {sock.name} (uname: {sock.uname}) -> enabling :  {self.enabling_params}")
                    raise RuntimeError(f"Algorithm error: uname '{uname}' should vary for each of its sockets.")
                uns[uname][i] = ch
            else:
                uns[uname] = {i: ch}
                
        uniques = {}
        for uname, spec in uns.items():
            if len(spec) == 1:
                uniques[uname] = list(spec.keys())[0]
            else:
                uniques[uname] = spec
                
        return uniques
    
    # ----------------------------------------------------------------------------------------------------
    # Some properties as list
    
    @property
    def unames(self):
        return [socket.uname for socket in self]
   
    @unames.setter
    def unames(self, values):
        for sock, value in zip(self, values):
            sock.uname = value

    @property
    def enablement(self):
        return [1 if socket.enabled else 0 for socket in self]

    @property
    def enabled_indices(self):
        indices = []
        for index, socket in enumerate(self):
            if socket.enabled:
                indices.append(index)
        return indices
           
    @property
    def enabled_sockets(self):
        return [self[i] for i in self.enabled_indices]
           
    @property
    def names(self):
        return [socket.name for socket in self]
   
    @property
    def enabled_names(self):
        return [socket.name for socket in self.enabled_sockets]
   
    @staticmethod
    def unique_names(names):
        total = {}
        for name in names:
            if name in total:
                total[name] += 1
            else:
                total[name] = 1
               
        counts = {}
        for name in total:
            counts[name] = 0
        uniques = []
        for name in names:
            if total[name] == 1:
                uniques.append(name)
            else:
                uniques.append(name + str(counts[name]))
                counts[name] += 1
        return uniques
   
    @property
    def enabled_unique_names(self):
        return self.unique_names(self.enabled_names)
    
    # ----------------------------------------------------------------------------------------------------
    # Check if sockets have a unique name or not
    
    def check_uniques(self):
        
        # Current unique names
        
        indices = []
        names   = []
        for i, sock in enumerate(self):
            if sock.enabled:
                indices.append(i)
                names.append(sock.uname)
                
        # Ensure unicicity
        
        unames = Sockets.unique_names(names)
        
        # Back to the sockets
        
        for i, uname in zip(indices, unames):
            self[i].uname = uname
            

    # ----------------------------------------------------------------------------------------------------
    # Which input socket is for self
    
    def self_index(self, default=None):
        if default is not None:
            return default
        
        first_enabled = None
        for i, sock in enumerate(self):
            if sock.is_multi_input:
                return i
            
            if sock.enabled and first_enabled is None:
                first_enabled = i
                
        return first_enabled
   
# ====================================================================================================
# A parameter

class Parameter:
    def __init__(self, node, name):
        
        self.node  = node
        self.name  = name
        self.uname = name
        
        # ---------------------------------------------------------------------------
        # Set the default value
        
        self.default = getattr(node.bnode, self.name)
        if isinstance(self.default, bpy.types.bpy_struct):
            #print(f"{node.bnode.bl_idname:30s}.{self.name:15s}:", self.default)
            self.default = None

        # ---------------------------------------------------------------------------
        # Get the enum values of the parameters
       
        self.values   = self.get_values()
        self.is_enum  = self.values is not None
       
        if not self.is_enum:
            return
        
        # ----- Initialize capture the enablement changes for this parameter
        
        node.inputs.new_param(name)
        node.outputs.new_param(name)

        for val in self.values:
            
            setattr(self.node.bnode, self.name, val)
            
            node.inputs.new_param_value(name, val)
            node.outputs.new_param_value(name, val)
           
        setattr(self.node.bnode, self.name, self.default)

    # ---------------------------------------------------------------------------
    # Get the enum values
    # When type is str, try to set a wrong attribute et interpret the error
    # message which contains to authorized values
   
    def get_values(self):
       
        if type(self.default) is not str:
            return None
       
        serror = "Param error"
        try:
            setattr(self.node.bnode, self.name, serror)
            setattr(self.node.bnode, self.name, self.default)
            return None
        except TypeError as e:
            msg = f"{e}"
            i = msg.find(serror)
            return eval(msg[i+26:])
        except AttributeError as e: # Read only
            return None
       
    # ---------------------------------------------------------------------------
    # Set the parameter value
    # if argument is None, reset to the default value
   
    def set_value(self, value=None):
        if value is None:
            value = self.default
        try:
            setattr(self.node.bnode, self.name, value)
        except AttributeError as e: # Read only
            pass
       
    # ---------------------------------------------------------------------------
    # Pretty pres

    def __repr__(self):
        s = f"{self.name:15s}: {self.default}"
        if self.is_enum:
            s += " enum"
            if self.change_inputs or self.change_outputs:
                s += " (CH)"
            s += f" in {self.values}"
        if hasattr(self, "arguments"):
            s += "\n"
            for k, v in self.arguments.items():
                 s += "   " + f"{k:20s}" + f"{v}" + "\n"
        return s
    
# ====================================================================================================
# Node argument
#
# Argument is either a node or a parameter
#
# arg_type : 'SOCKET', 'PARAMETER', 'VARIATION'
#
# is_self  : this argument is used for self in metod implementation

class Argument:
    
        def __init__(self, name, default, class_name, arg_type, is_multi=False, is_self=False, hooks={}):
            
            self.name = name
            self.hook = hooks.get(name)
            self.class_name = class_name
            
            self.default_type = type(default).__name__ # USed for comment
            
            if type(default) is str:
                self.default = f"'{default}'"
            elif type(default).__name__ == 'Vector':
                self.default = tuple(default)
            else:
                self.default = default
                
            self.arg_type = arg_type
            self.is_multi = is_multi
            self.is_self  = is_self
            
            
        @property
        def is_input(self):
            return self.arg_type == 'SOCKET'
        
        @property
        def is_parameter(self):
            return self.arg_type == 'PARAMETER'
                
        @property
        def is_variation(self):
            return self.arg_type == 'VARIATION'
        
        @property
        def comment(self):
            s = f"{self.name:15s} : "
            if self.is_variation:
                s += f"node parameter set to {self.default}"
                
            elif self.is_parameter:
                s += self.default_type

            else:
                s += self.class_name
                if self.is_multi:
                    s += " (multi input)"
                if self.is_self:
                    s += ": self socket"
            return s + "\n"
        
            
        @property
        def header(self):
            
            if self.is_self:
                if self.is_multi:
                    return f", self, *{self.name}"
                else:
                    return ", self"
                
            elif self.is_variation:
                return ""
            
            else:
                if self.is_multi:
                    return f", *{self.name}"
                else:
                    return f", {self.name}={self.default}"
                
        @property
        def node_call(self):
            if self.is_self:
                if self.is_multi:
                    return f", self, *{self.name}"
                else:
                    return f", {self.name}=self"
            else:
                if self.is_multi:
                    return f", *{self.name}"
                elif self.is_variation:
                    return f", {self.name}={self.default}"
                elif self.hook is not None:
                    return f", {self.name}={self.hook}({self.name})"
                else:
                    return f", {self.name}={self.name}"
                
# ----------------------------------------------------------------------------------------------------
# The list of arguments
                
class Arguments(list):
    
    @property
    def header(self):
        s = ""
        for arg in self:
            s += arg.header
        return s[2:]
            
    @property
    def node_call(self):
        s = ""
        
        for arg in self:
            if arg.is_multi:
                s += arg.node_call
                
        for arg in self:
            if not arg.is_multi:
                s += arg.node_call

        return s[2:]
    
    def node_creation(self, node_name, ret='NODE', socket_name=None):
        
        # ----- Node creation

        snode = f"Node{node_name}({self.node_call})"
        
        # ----- No socket
        
        if ret == 'NODE':
            return f"{snode}"
        
        elif ret == 'STACK':
            return f"self.stack({snode})"
        
        # ----- If not NODE or STACK, ret is the class name (or cls)
        # We need the output socket
        
        #if socket_name is None:
        #    if self.out_name is not None:
        #        socket_name = self.out_name
        #    else:
        #        for socket in self.outputs:
        #            if socket.enabled:
        #                if socket.class_name == ret:
        #                    socket_name = socket.uname
        #                    break
                        
        if socket_name is None:
            raise RuntimeError(f"Impossible to get a valid output socket name when creating the node '{node_name}' with ouput class '{ret}'.")
        
        return f"{ret}({snode}.{socket_name})"    
    

    
# ====================================================================================================
# A node Generator

class Node:
    
    # ----------------------------------------------------------------------------------------------------
    # Constructor
    
    def __init__(self, bnode):
       
        self.bnode   = bnode
        
        # ---------------------------------------------------------------------------
        # The inputs and outputs sockets
        
        self.inputs     = Sockets.Inputs(bnode)
        self.outputs    = Sockets.Outputs(bnode)
        self.self_index = None
        self.out_index_ = None
        
        # ---------------------------------------------------------------------------
        # Some hacks
        
        if bnode.bl_idname == 'GeometryNodeAttributeRemove':
            self.self_index = 0

        # ---------------------------------------------------------------------------
        # Read the parameters
       
        self.parameters = {}
        for param_name in dir(self.bnode):
            
            if param_name in NODE_ATTRS:
                continue
            
            val = getattr(self.bnode, param_name)
            if isinstance(val, bpy.types.bpy_struct):
                continue
            
            param = Parameter(self, param_name)
            
            for sock in self.outputs:
                if param.name == sock.name:
                    param.uname = param.name + "_"
                    
            self.parameters[param_name] = param
                
        # ---------------------------------------------------------------------------
        # Compute the unique names by setting all the possible combinations
        
        def explore_params(config={}):
            
            # ---- What are the free parameters
            
            frees = []
            for param_name, param in self.parameters.items():
                if param.is_enum and not param_name in config:
                    frees.append(param_name)

            # ---- Let's make vary the free parameters

            for param_name in frees:
                param = Parameter(self, param_name)
                for value in param.values:
                    
                    param.set_value(value)
                    
                    self.inputs.update_unames()
                    self.outputs.update_unames()
                            
                    # ---- Deeper....
                    
                    explore_params({**config, param_name: value})
                    
                param.set_value()
                
        explore_params()
            
    # ----------------------------------------------------------------------------------------------------
    # bl_idname
    
    @property
    def bl_idname(self):
        return self.bnode.bl_idname
    
    # ----------------------------------------------------------------------------------------------------
    # When a node is created, a parameter can be passed as argument or not
    # When passed as an argument, the use can change it
    # A change in parameter value can change the enablement of input sockets
    # The arguments must include all the possible input sockets
    
    def get_variation_input_unames(self, variation={}):

        unames = self.inputs.get_unames(True)
        
        # ----- No variation : return all the unames
        
        if len(variation) == 0:
            for socket in self.inputs:
                if socket.uname not in unames:
                    unames.append(socket.uname)
            return unames
        
        # ---- Recursive
        
        def search(config):
        
            # ---- What are the free parameters
            
            frees = []
            for param_name, param in self.parameters.items():
                if param.is_enum:
                    if param_name in config:
                        param.set_value(config[param_name])
                    else:
                        frees.append(param_name)

            # ---- Let's make vary the free parameters

            for param_name in frees:
                param = Parameter(self, param_name)
                for value in param.values:
                    param.set_value(value)
                    uns = self.inputs.get_unames(True)
                    for uname in uns:
                        if uname not in unames:
                            unames.append(uname)
                            
                    # ---- Deeper....
                    
                    search({**config, param_name: value})
                    
                param.set_value()
                
        search(variation)
        
        # ----- Make sure the order is right
        
        res = []
        for socket in self.inputs:
            if socket.uname in unames:
                res.append(socket.uname)
            
        return res
    
    # ----------------------------------------------------------------------------------------------------
    # Output unames
    
    def get_output_unames(self):
        unames = []
        for socket in self.outputs:
            if socket.uname not in unames:
                unames.append(socket.uname)
        return unmes
            
    # ----------------------------------------------------------------------------------------------------
    # Output index
    
    @property
    def out_index(self):
        if self.out_index_ is not None:
            return self.out_index_
        outputs = Sockets.Outputs(self.bnode)
        for i, sock in enumerate(outputs):
            if sock.enabled:
                return i
            
    @property
    def class_out(self):
        index = self.out_index
        if index is None:
            return None
        else:
            return SOCKET_TYPES[self.outputs[index].bl_idname]
        
    @property
    def out_name(self):
        index = self.out_index
        if index is None:
            return None
        else:
            return self.outputs[index].uname
        
    
    # ----------------------------------------------------------------------------------------------------
    # Name of the generated node class
    
    @property
    def node_name(self):
        s = ""
        for word in self.bnode.name.split(' '):
            s += word
        return s
    
    # ----------------------------------------------------------------------------------------------------
    # Default name for the method
    
    def function_name(self, func_type='METHOD'):
        s = self.bnode.name
        if s == 'ID':
            pass
        else:
            if func_type == 'CONSTRUCTOR':
                return self.node_name
            else:
                return s.lower().replace(' ', '_')
        
    # ----------------------------------------------------------------------------------------------------
    # Read the input arguments
    # - Only the enabled sockets
    # - Unique names
    # - With their indices
   
    def read_arguments(self):
        inputs  = self.inputs
        return [(name, index) for name, index in zip(inputs.enabled_unique_names, inputs.enabled_indices)]
    
    # ----------------------------------------------------------------------------------------------------
    # Split a generated line into several lines
    
    @staticmethod
    def split(word, left=""):

        sep0  = " "
        ws0   = word.split(sep0)

        sep1  = " "
        ws1   = word.split(sep1)
        if len(ws0) > len(ws1):
            sep = sep0
            ws  = ws0
        else:
            sep = sep1
            ws  = ws1
            
        line = left
        s = ""
        for i, w in enumerate(ws):
            line += w + sep
            if len(line) > 110 and i < len(ws)-1:
                s += line + "\n"
                line = " " * len(left)
        
        return s + line

    # ----------------------------------------------------------------------------------------------------
    # Generate the source code of an input socket
    
    def gen_socket_property(self):
        
        # ---------------------------------------------------------------------------
        # The set / get line
        
        def line(index, is_get=True):
            if is_get:
                return f"return self.inputs[{index}]\n" #".link\n"
            else:
                #return f"self.inputs[{index}].link = value\n"
                return f"self.inputs[{index}].plug(value)\n"
            
        # ---------------------------------------------------------------------------
        # Loop on the unique sockets
        
        uniques = self.inputs.uniques
        
        for uname, spec in uniques.items():
            for is_get in [True, False]:
                
                if is_get:
                    yield _1_ +  "@property\n"
                    yield _1_ + f"def i{uname}(self):\n"
                else:
                    yield _1_ + f"@i{uname}.setter\n"
                    yield _1_ + f"def i{uname}(self, value):\n"
                    
                # No condition: spec = {index: None}
                    
                if type(spec) is int:
                    
                    yield _2_ + line(spec, is_get)
                    
                # Conditions: spec = {0: {param: values}, 1: {param: values}, ...}
                
                else:
                    sif = "if"
                    for index, conditions in spec.items():
                        if conditions is None:
                            continue
                        
                        sep = _2_ + f"{sif} "
                        sif = "elif"
                        for param_name, values in conditions.items():
                            if len(values) == 1:
                                yield f"{sep}(self.{param_name} == '{values[0]}')"
                            else:
                                yield f"{sep}(self.{param_name} in {values})"
                            sep = " and "
                        yield ":\n"
                        yield _3_ + line(index, is_get)
                
                yield "\n"
                
    # ----------------------------------------------------------------------------------------------------
    # Prepare the node
    
    def set_parameters(self, variation):
            
        for param_name, param in self.parameters.items():
            if param_name in variation:
                param.set_value(variation[param_name])
            else:
                param.set_value()
            
    # ----------------------------------------------------------------------------------------------------
    # Build the list of arguments
    
    def build_arguments(self, only_enabled=False, variation={}, self_name=None, hooks={}):
        
        # ---------------------------------------------------------------------------
        # An empty arguments list
        
        args = Arguments()
        self_arg = None
        
        # ---------------------------------------------------------------------------
        # Only enabled nodes
        
        if only_enabled:
            
            unames = set(self.get_variation_input_unames(variation))
            for sock in self.inputs:
                
                if sock.uname in unames:
                    
                    # ----- Remove the entry to avoid two inclusions
                    
                    unames.remove(sock.uname)
                    
                    is_multi = sock.is_multi_input
                    is_self  = sock.uname == self_name
                    
                    arg = Argument(sock.uname, None, sock.class_name, arg_type = 'SOCKET', is_multi=is_multi, is_self=is_self, hooks=hooks)
                    
                    if is_self:
                        self_arg = arg
                    elif is_multi:
                        args.insert(0, arg)
                    else:
                        args.append(arg)
                    
        # ---------------------------------------------------------------------------
        # All nodes

        else:
            uniques = self.inputs.uniques
            for uname, spec in uniques.items():
                
                is_self = uname == self_name
                
                # Multi is necessarily allways enabled
                is_multi = False
                if type(spec) is int:
                    index    = spec
                    sock     = self.inputs[index]
                    is_multi = sock.is_multi_input
                        
                arg = Argument(uname, None, class_name = 'Undef', arg_type = 'SOCKET', is_multi=is_multi, is_self=is_self, hooks=hooks)
                
                if is_self:
                    self_arg = arg
                elif is_multi:
                    args.insert(0, arg)
                else:
                    args.append(arg)
                    
        if self_arg is not None:
            args.insert(0, self_arg)
            
        # ---------------------------------------------------------------------------
        # Parameters
            
        for param in self.parameters.values():
            arg_type = 'VARIATION' if param.name in variation else 'PARAMETER'
            default = variation[param.name] if arg_type == 'VARIATION' else param.default
            
            args.append(Argument(param.name, default, class_name='Param', arg_type=arg_type, hooks=hooks))
            
        return args
    
    # ----------------------------------------------------------------------------------------------------
    # Generate the source code for comments
    
    def gen_comments(self):
        
        def stitle(title):
            yield _1_ + title + "\n"
            yield _1_ + '-'*len(title) + "\n\n"
            
        yield _1_ + '""" ' + f"Node class {self.bnode.bl_idname}\n\n"
        
        if self.inputs:
            for line in stitle("Input sockets"):
                yield line
            for sock in self.inputs:
                yield _2_ + f"{sock.index}: {sock.uname:20s} {SOCKET_TYPES[sock.bl_idname]}\n"
            yield "\n"
            
        if self.parameters:
            for line in stitle("Parameters"):
                yield line
                
            for param in self.parameters.values():
                if type(param.default) is str: 
                    s =  _2_ + f"{param.uname:12s}: '{param.default}'"
                else:
                    s =  _2_ + f"{param.uname:12s}: {param.default}"
                if param.is_enum:
                    s = self.split(str(param.values), s + " in ")
                yield s + "\n"
                
                #yield _2_ + f"{param.uname:12s}: {param.default}\n"
            yield "\n"
        
        if self.outputs:
            for line in stitle("Output sockets"):
                yield line
            for sock in self.outputs:
                yield _2_ + f"{sock.index}: {sock.uname:20s} {SOCKET_TYPES[sock.bl_idname]}\n"
            yield "\n"
        
        yield _1_ + '"""\n\n'
        
    # ----------------------------------------------------------------------------------------------------
    # Generate the source code for the node class
    
    def gen_node_class(self, is_attribute=False):
        
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Header and class constants
        
        node_class = 'Attribute' if is_attribute else 'Node'
        
        yield  "# " + '-'*120 + "\n"
        yield f"# {node_class} class {self.bnode.bl_idname}\n\n" 
        
        yield f"class Node{self.node_name}({node_class}):\n\n"

        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Documentation
        
        for line in self.gen_comments():
            yield line

        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Parameter list
        
        yield _1_ + f"PARAMETERS = {[param.uname for param in self.parameters.values()]}\n\n"
    
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Constructor __init__
    
        yield _1_ + "def __init__(self"
        
        args = self.build_arguments(only_enabled=False)
        s = args.header
        if s != "":
            yield ", " + s

        # ---------------------------------------------------------------------------
        # Attribute specific arguments
                
        if is_attribute:
            yield f", owner_socket=None, data_type='FLOAT', domain='POINT'"

        # ---------------------------------------------------------------------------
        # Hack for NodeValue which doesn't behave as other values
        
        if self.bnode.bl_idname == 'ShaderNodeValue':
            yield ", value=0."
            
        yield "):\n\n"

        # ---------------------------------------------------------------------------
        # Super
        
        yield _2_ + f"super().__init__('{self.bnode.bl_idname}', name='{self.bnode.name}'"
        
        if is_attribute:
            yield ", owner_socket=owner_socket, data_type=data_type, domain=domain"
        
        yield ")\n\n"
    
        # ---------------------------------------------------------------------------
        # Input sockets
        
        if len(self.inputs):
            for sock in self.inputs:
                yield _2_ + f"self.inputs.add({sock.gen_init})\n"
            yield "\n"
    
        # ---------------------------------------------------------------------------
        # Output sockets
        
        if len(self.outputs):
            for sock in self.outputs:
                yield _2_ + f"self.outputs.add({sock.gen_init})\n"
            yield "\n"
            
        cr = False
        if self.inputs.has_geometry_socket:
            yield _2_ + f"self.input_geometry_socket = self.inputs[{self.inputs.geometry_socket_index}]\n"
            cr = True
        if self.outputs.has_geometry_socket:
            yield _2_ + f"self.output_geometry_socket = self.outputs[{self.outputs.geometry_socket_index}]\n"
            cr = True
        if cr:
            yield "\n"
            
        yield _2_ + f"self.socket_out_name = "
        if self.out_name is None:
            yield "None\n\n"
        else:
            yield f"'{self.out_name}'\n\n"
            
        # ---------------------------------------------------------------------------
        # Hack for NodeValue which doesn't behave as other values
        
        if self.bnode.bl_idname == 'ShaderNodeValue':
            yield _2_ +"self.outputs[0].default_value = value\n\n"
    
        # ---------------------------------------------------------------------------
        # Parameters
        
        if len(self.parameters):
            yield _2_ + "# ----- Parameters\n\n"
            
            for param in self.parameters.values():
                yield _2_ + f"self.{param.uname:15s} = {param.name}\n"
            
            yield _2_ + "self.check_parameters()\n\n"
            
        # ---------------------------------------------------------------------------
        # Input sockets
        
        in_uniques = self.inputs.uniques
        if in_uniques:
            yield _2_ + "# ----- Input sockets\n\n"
            
            for uname in in_uniques:
                yield _2_ + f"self.i{uname:14s} = {uname}\n"

            yield "\n"
            
        yield _2_ + f"self.socket_in_name = "
        index = self.inputs.self_index(self.self_index)
        if index is None:
            yield "None\n\n"
        else:
            yield f"'i{self.inputs[index].uname}'\n\n"
            
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Str
        
        if False:
            yield _1_ + f"def __str__(self):\n"
            yield _2_ + "return f" + '"' + f"<Node '{self.node_name}'" + "({self.unique_id})"
    
            if len(self.inputs.uniques) > 0:
                sep = " ("
                for uname in self.inputs.uniques:
                    yield f"{sep}{uname}"
                    sep = ", "
                yield ")"
                    
            if len(self.parameters) > 0:
                sep = " ["
                for name in self.parameters:
                    yield f"{sep}{name}"
                    sep = ", "
                yield "]"
                #yield f" {list(self.parameters.keys())}"
                
            if len(self.outputs.uniques) > 0:
                sep = " -> "
                for uname in self.outputs.uniques:
                    yield f"{sep}{uname}"
                    sep = ", "
                    
            yield '>"\n\n'
        
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Rep
        
        CR = "\\n"
        QU = '\"'
        OPEN = '{'
        CLOSE = '}'
        
        yield _1_ +  "def __repr__(self):\n"
        yield _2_ + f"s = f{QU}Node '{self.node_name}' ({OPEN}self.unique_id{CLOSE}){QU}\n"

        if len(self.inputs.uniques) > 0:
            yield _2_ + f"s += '{CR}Input sockets'\n"
            for uname in self.inputs.uniques:
                yield _2_ + f"s += f{QU}{CR}   {uname:15s} : {OPEN}self.i{uname}{CLOSE}{QU}\n"

        if len(self.parameters) > 0:
            yield _2_ + f"s += '{CR}Parameters'\n"
            for name in self.parameters:
                yield _2_ + f"s += f{QU}{CR}   {name:15s} : {OPEN}self.{name}{CLOSE}{QU}\n"

        if len(self.outputs.uniques) > 0:
            yield _2_ + f"s += '{CR}Output sockets'\n"
            for uname, spec in self.outputs.uniques.items():
                yield _2_ + f"s +=  {QU}{CR}   {uname:15s} : "
                if type(spec) is int:
                    yield SOCKET_TYPES[self.outputs[spec].bl_idname]
                else:
                    yield "variable"
                yield f"{QU}\n"

                
        yield _2_ + f"return s + {QU}{CR}{QU}\n\n"
        
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Check the parameters
        
        enums = []
        for param in self.parameters.values():
            if param.is_enum:
                enums.append(param)
                
        if enums:
            yield _1_ + "def check_parameters(self):\n"
            for param in enums:
                
                yield self.split(str(param.values), _2_ + "valids = ") + "\n"
                yield _2_ + f"if self.{param.name} not in valids:\n"
                serror  = f"\\nAttribute error for Node 'Node{self.node_name}'.\\n '{param.name}' is "
                serror += "'{" + f"self.{param.uname}" + "}'" + f".\\n Authorized values are " + "{valids}."
                yield _3_ + f"raise AttributeError(f\"" + serror + "\")\n"
                
                continue
                
                
                
                yield _2_ + f"if self.{param.name} not in {param.values}:\n"
                serror  = f"\\nAttribute error for Node 'Node{self.node_name}'.\\n '{param.name}' is "
                serror += "'{" + f"self.{param.uname}" + "}'" + f".\\n Authorized values are {param.values}."
                
                yield _3_ + f"raise AttributeError(f\"" + serror + "\")\n"
                
            yield "\n"
        
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Output sockets
        
        if self.outputs:
            yield _1_ + f"# {'-'*80}\n{_1_}# Output sockets\n\n"
            
            uniques = self.outputs.uniques
            for uname, spec in uniques.items():
                yield _1_ +  "@property\n"
                yield _1_ + f"def {uname}(self):\n"

                if type(spec) is int:
                    
                    yield _2_ + f"return self.outputs[{spec}]\n\n"
                    
                else:
                    
                    sif = "if"
                    for index, conditions in spec.items():
                        sep = _2_ + f"{sif} "
                        sif = "elif"
                        for param_name, values in conditions.items():
                            if len(values) == 1:
                                yield f"{sep}(self.{param_name} == '{values[0]}')"
                            else:
                                yield f"{sep}(self.{param_name} in {values})"
                            sep = " and "
                        yield ":\n"
                        sock = self.outputs[index]
                        
                        yield _3_  + f"return self.outputs[{index}]\n"
                        
                    yield _2_ + "self.check_parameters()\n\n"
        
            
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Input sockets
        
        ok_com = True
        for line in self.gen_socket_property():
            if ok_com:
                yield _1_ + f"# {'-'*80}\n{_1_}# Input sockets\n\n"
                ok_com = False
                
            yield line
            
    # ----------------------------------------------------------------------------------------------------
    # Node are created with variations in parameters either through a function or a method
    
    def gen_function(self, func_name, variation={}, ret='NODE', socket_name=None):
        
        args = self.build_arguments(only_enabled=True, variation=variation, self_name=None)
        
        yield _0_ + f"def {func_name}({args.header}):\n"
        
        # ---------------------------------------------------------------------------
        # Hack for math function
        # functions like sin must be implemented by check if the arguments
        # are vectors or values
        
        alt_math = self.bnode.bl_idname == 'ShaderNodeMath'
        if func_name in ['add', 'substract', 'multiply', 'divide', 'multiply_add', 'min', 'max', 'fraction', 'modulo']:
            alt_math_args_count = 2
        elif func_name in ['floor', 'ceil', 'sin', 'cos', 'tan']:
            alt_math_args_count = 1
        else:
            alt_math = False
        
        if alt_math:
            yield _1_ + "if is_vector(value0)"
            if alt_math_args_count == 2:
                yield " or is_vector(value1)"
            yield ":\n"
            yield _1_ + f"return vector_{func_name}(value0"
            if alt_math_args_count == 2:
                yield ", value1"
            yield ")\n"

            
        # ---------------------------------------------------------------------------
        # The node creation
        
        yield _1_ + "return " + args.node_creation(self.node_name, ret=ret, socket_name=socket_name) + "\n\n"
        
    # ----------------------------------------------------------------------------------------------------
    # Node are created with variations in parameters either through a function or a method
    
    def gen_method(self, meth_name, decorator=None, self_name=None, variation={}, ret='NODE', socket_name=None):
        
        # ---------------------------------------------------------------------------
        # Input socket for self
        
        if decorator in ['staticmethod', 'classmethod']:
            self_name = None
        else:
            if self_name is None:
                for sock in self.inputs:
                    if sock.enabled:
                        self_name = sock.uname
                        break
            #if self_name is None:
            #    raise RuntimeError(f"Impossible to find an input socket to implement the method '{meth_name}' with node '{self.node_name}'.")

        args = self.build_arguments(only_enabled=True, variation=variation, self_name=self_name)

        # ---------------------------------------------------------------------------
        # Method header
        
        if decorator is not None:
            yield _1_ + f"@{decorator}\n"
        
        yield _1_ + f"def {meth_name}({args.header}):\n"
        

        # ---------------------------------------------------------------------------
        # Socket out name
        
        if socket_name is None:
            socket_name = self.out_name
            
        # ---------------------------------------------------------------------------
        # The node creation
        
        yield _2_ + "return " + args.node_creation(self.node_name, ret=ret, socket_name=socket_name) + "\n\n"
        
    # ----------------------------------------------------------------------------------------------------
    # Generate an attribute
    #
    # class_name is either the str for the actual class_name
    # or a dictionnary keyed by the node output sockets and the class_name as a value
    
    def gen_attribute(self, base_name, domains=None):
        
        args = self.build_arguments()
        
        if domains is None:
            domains = ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
        
        for socket_index, socket in enumerate(self.outputs):
            
            socket_name = f"_{socket.name}" if len(self.outputs) > 1 else ""
            
            for domain in domains:
                sdomain = f"{domain.lower()}_" if len(domains) > 1 else ""
                
                if not args:
                    yield _1_ +  "@property\n"
                yield _1_ + f"def {sdomain}{base_name}{socket_name}(self"
                if args:
                    for arg in args:
                        yield f", {arg.header}"
                yield "):\n"
                
                yield _2_ + f"return {socket.class_name}(nodes.Node{self.node_name}("
                sepa = ""
                
                for arg in args:
                    yield f"{sepa}{arg.name}={arg.name}"
                    sepa = ", "
                    
                yield f"{sepa}owner_socket=self.socket, data_type='{socket.bsocket.type}', domain='{domain}').outputs[{socket_index}])\n\n"
        
    # ----------------------------------------------------------------------------------------------------
    # Generate the source code for a class method
    
    def gen_function_OLD(self, func_type='METHOD', func_name=None, variation={}, return_class=None):
    
        # ---------------------------------------------------------------------------
        # Method name
        
        if func_name is None:
            func_name = self.function_name(func_type)
            
        if func_type == 'METHOD' and func_name[0].upper() == func_name[0] and func_name[0] != '_':
            func_type = 'CONSTRUCTOR'
            
        # A method can either return another class be stacked and return self
            
        as_stack = False
        if func_type == 'STACK':
            func_type = 'METHOD'
            as_stack  = True
            
        # Static method
        
        as_static = False
        if func_type == 'STATIC':
            func_type = 'METHOD'
            as_static = True
            
        # ---------------------------------------------------------------------------
        # Hack for math function
        # functions like sin must be implemented by check if the arguments
        # are vectors or values
        
        alt_math = (func_type == 'FUNCTION') and (self.bnode.bl_idname == 'ShaderNodeMath')
        if func_name in ['add', 'substract', 'multiply', 'divide', 'multiply_add', 'min', 'max', 'fraction', 'modulo']:
            alt_math_args_count = 2
        elif func_name in ['floor', 'ceil', 'sin', 'cos', 'tan']:
            alt_math_args_count = 1
        else:
            alt_math = False
            
        # ---------------------------------------------------------------------------
        # Indentation

        _i_ = "" if func_type == 'FUNCTION' else _1_

        # ---------------------------------------------------------------------------
        # Set the bnodes parameters which the enablement
            
        for param_name, param in self.parameters.items():
            if param_name in variation:
                param.set_value(variation[param_name])
            else:
                param.set_value()
                    
        # ---------------------------------------------------------------------------
        # Now that enablement is updated, let's get the return class
        # The return class is Node for stackable methods
        
        if return_class is None:
            return_class = self.class_out
            
        if as_stack:
            return_class = None
            
        # ---------------------------------------------------------------------------
        # Counter order : the return class is the node itself if more than
        # one output socket exists
        
        if len(self.outputs.uniques) > 1:
            return_class = None
                    
        # ---------------------------------------------------------------------------
        # Get the enabled arguments excluding the variation

        args = self.build_arguments(only_enabled=True, variation=variation)
        
        # ---------------------------------------------------------------------------
        # Hack for reversed operator
        
        rev_self = func_name in ['__radd__', '__rsub__', '__rmul__', '__rtruediv__', '__rpow__']
        if rev_self:
            args[0].self_arg = False
            args[1].self_arg = True
        
        # ---------------------------------------------------------------------------
        # Mehod header
        
        use_self = False
        use_cls  = False
        sep      = ""
        
        # ----- Decorator
        
        if func_type == 'CONSTRUCTOR':
            yield _1_ + "@classmethod\n"
            
        if as_static:
            yield _1_ + "@staticmethod\n"

        # ----- Function name
        
        yield _i_ + f"def {func_name}("

        # ----- First parameter
    
        if func_type == 'METHOD':
            if not as_static:
                yield "self"
                sep = ", "
                use_self = True
                
        elif func_type == 'CONSTRUCTOR':
            yield "cls"
            sep = ", "
            use_cls = True
    
        for i, arg in enumerate(args):
            # drop the argument associated to self if:
            # - self is used :-)
            # - it is the argument associated to self
            # - it is not a multi input socket
            if use_self and arg.self_arg and not arg.is_multi:
                continue
            yield f"{sep}{arg.header}"
            sep = ", "
        yield "):\n"
        
        # ---------------------------------------------------------------------------
        # Call the vector function in case of alternative math
        
        if alt_math:
            yield _1_ + "if is_vector(value0)"
            if alt_math_args_count == 2:
                yield " or is_vector(value1)"
            yield ":\n"
            yield _2_ + f"return vector_{func_name}(value0"
            if alt_math_args_count == 2:
                yield ", value1"
            yield ")\n"
        
    
        # ---------------------------------------------------------------------------
        # ---------------------------------------------------------------------------
        # Build the Node initialization
        # Possible templates are:
        #
        # The node when it has more than one output sockets:
        #   return Node(....)
        #
        # The node and the output socket when only one output socket.
        # Use cls for class methods
        #
        #   return cls(Node(...), socket)
        #   return class(Node(...), socket)
        #
        # If the method is stackable, stack it and return self 
        #   self.stack(...)
        #   return self
        
        # ---------------------------------------------------------------------------
        # Return or stack
        
        if as_stack:
            yield _i_ + _1_ + "self.stack("

        else:
            yield _i_ + _1_ + "return "
            
        # ---------------------------------------------------------------------------
        # Insert the return class
        
        if return_class is not None:
            if use_cls:
                yield "cls("
            else:
                yield f"{return_class}("
                
        # ---------------------------------------------------------------------------
        # Node name
        
        yield f"nodes.Node{self.node_name}("
        
        # ---------------------------------------------------------------------------
        # __init__ arguments
            
        sep = ""

        for i, arg in enumerate(args):

            if arg.is_multi: # i == 0 necessarily
                if use_self and arg.self_arg:
                    yield f"self, *{arg.name}"
                else:
                    yield f"*{arg.name}"
                
            elif use_self and arg.self_arg:
                yield f"{sep}{arg.name}=self"
                if as_stack:
                    yield ".connector"
            else:
                yield f"{sep}{arg.name}={arg.name}"
            
            sep = ", "
                
        # ---------------------------------------------------------------------------
        # Node arguments coming from the variation
        
        for name, val in variation.items():
            if type(val) is str:
                val = f"'{val}'"
            yield f", {name}={val}"

        # ---------------------------------------------------------------------------
        # Done

        yield ")"
        
        if return_class is not None:
            yield f".outputs[{self.out_index}])"
            
        if as_stack:
            yield ")\n"
            yield _2_ + "return self"
            
        yield "\n\n"
        
    # ----------------------------------------------------------------------------------------------------
    # Generate the source code for a field
    
    def gen_field(self, func_name=None, return_class=None):
        
        has_args = False
        
        if not has_args:
            yield _1_ +  "@property\n"
        yield _1_ + f"def {func_name}(self):\n"
        yield _2_ +  "ns = "
        
        if return_class is not None:
            yield f"{return_class}("
            
        yield f"nodes.Node{self.node_name}("
        
        # other arguments here
        
        yield ")"
        
        if return_class is not None:
            yield ")"
        
        yield "\n"

        yield _2_ + "ns.field_of = self\n"
        yield _2_ + "return ns\n\n"
        
        
    # ----------------------------------------------------------------------------------------------------
    # A node can be considered as a property of a node socket:
    # NodeSeparateRGG is a property of Color
    # It is implemented in the following way
    # 
    #   @property
    #   def separate(self):
    #       if not hasattr(self, 'separate_'):
    #           self.separate_ = NodeSeparateRGB(self)
    #       return self.separate_
    #
    #   @property
    #   def r(self):
    #       if not hasattr(self, 'r_'):
    #           self.r_ = self.separate.r
    #       return self.r_
    #
    #   @r.setter
    #   def r(self, value):
    #       _ = self.separate
    #       self.r_ = value
    # 
    #   ...
    
    def gen_node_as_property(self, prop_name, names=None, settable = False):

        yield _1_ +  "@property\n"
        yield _1_ + f"def {prop_name}(self):\n"
        yield _2_ + f"if not hasattr(self.top, '{prop_name}_'):\n"
        yield _3_ + f"self.top.{prop_name}_ = nodes.Node{self.node_name}(self.connector)\n"
        yield _3_ + f"self.top.{prop_name}_.prop_of = self.node\n"
        yield _2_ + f"return self.top.{prop_name}_\n\n"
        
        # ----- Note hat it doesn't work if some output sockets are disabled

        unames = self.outputs.uniques
        unames = [sock.name for sock in self.outputs]
        cnames = [SOCKET_TYPES[sock.bl_idname] for sock in self.outputs]
        if names is None:
            names = unames
        
        for uname, name, cname in zip(unames, names, cnames):
            yield _1_ +  "@property\n"
            yield _1_ + f"def {name}(self):\n"
            yield _2_ + f"if not hasattr(self.top, '{name}_'):\n"
            yield _3_ + f"self.top.{name}_ = {cname}(self.top.{prop_name}.{uname})\n"
            yield _2_ + f"return self.top.{name}_\n\n"
            
            if settable:
                yield _1_ + f"@{name}.setter\n"
                yield _1_ + f"def {name}(self, value):\n"
                yield _2_ + f"_ = self.{prop_name}\n"
                yield _2_ + f"self.top.{name}_ = value\n\n"
                
               
            
         
    


