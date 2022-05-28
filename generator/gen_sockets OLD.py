{}#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:49:27 2022

@author: alain
"""

import inspect

_0_ = ""
_1_ = "    "
_2_ = _1_*2
_3_ = _1_*3
_4_ = _1_*4


GEN_NODES = []


# =============================================================================================================================
# Node calling

class NodeCall:
    
    FAMILIES = {
        'CONSTRUCTOR' : ('Constructor',     'Constructors'    , False),
        'STATIC'      : ('Static method',   'Static methods'  , False),
        'CLASS'       : ('Class method',    'Class methods'   , False),
        
        'PROPERTY'    : ('Property',        'Properties'      , True ),   
        'NODE_PROP'   : ('Node property',   'Node properties' , True ),
        'ATTRIBUTE'   : ('Attribute',       'Attributes'      , True ),
        'METHOD'      : ('Method',          'Methods'         , True ),        
        'STACK'       : ('Stacked method',  'Stacked methods' , True ),
        
        'FUNCTION'    : ('Function',        'Functions'       , False),
        }
    
    def __init__(self, family, node, class_name, meth_name, self_name=None, out_name=None, ret_class=None, args_hooks={}, **variation):
        
        self.family     = family

        self.node       = node
        self.class_name = class_name
        self.meth_name  = meth_name
        
        self.variation  = dict(variation)
        self.configure_node()
        
        # ----- The self name
        
        self.self_name = None
        if self.use_self and self.node.inputs:
            
            self.self_name = self_name
        
            if self.self_name is None and self.node.inputs:
                first = None
                for sock in node.inputs:
                    if sock.enabled:
                        if first is None:
                            first = sock.uname
                            
                        if sock.class_name == self.class_name:
                            self.self_name = sock.uname
                            break
                        
                if self.self_name is None:
                    self.self_name = first
                    
            if self.self_name is None:
                raise RuntimeError(f"Impossible to find a valid input socket name for method '{self.meth_name}' in class {self.class_name}.")
            
        # ----- Build the arguments
        
        
        attr_args = {'attribute': False}
        """
        if self.family == 'ATTRIBUTE':
            if self.capture:
                sdomain = "domain"
            else:
                sdomain = f"'{self.domain}'"
            attr_args = {'attribute': True, 'domain': 'TOTO', 'data_type': 'TITI'}
        """
            
            
        
        self.args = self.node.build_arguments(only_enabled=True, variation=variation, self_name=self.self_name, **attr_args, hooks=args_hooks)
        
        # ----- All the possible returned sockets
        
        self.returned_sockets = []
        for socket in self.node.outputs:
            if socket.bsocket.enabled:
                self.returned_sockets.append(socket)
                
        # ----- Output socket
        
        self.out_name = out_name
        if self.out_name is None:
            if len(self.returned_sockets) == 1:
                self.out_name = self.returned_sockets[0].uname
                
        self.output_socket = None
        if self.out_name is not None:
            for socket in self.returned_sockets:
                if socket.uname == self.out_name:
                    self.output_socket = socket
                    break
                
            if self.output_socket is None:
                raise RuntimeError(f"Impossible to find the output socket named '{self.out_name}' in node '{self.node.node_name}' for method '{self.meth_name}' in class {self.class_name}.")
                
        self.return_sockets = len(self.returned_sockets) > 1 and self.output_socket is None

        # ----- The returned class
        
        self.ret_class = 'cls' if self.family in ['CLASS', 'CONSTRUCTOR'] else ret_class
        if self.output_socket is not None:
            if self.ret_class is None:
                self.ret_class = self.returned_sockets[0].class_name
            elif ret_class == 'SAME':
                self.ret_class = self.class_name
            
    # ----------------------------------------------------------------------------------------------------
    # Prepate the node
    
    def configure_node(self):
        self.node.set_parameters(self.variation)

    # ----------------------------------------------------------------------------------------------------
    # A property
    
    @classmethod
    def Property(cls, node, class_name, meth_name, settable=False, **variation):
        nc = cls('PROPERTY', node, class_name, meth_name, **variation)
        
        count = 0
        for arg in nc.args:
            if not arg.is_variation:
                count += 1
        if count > 1:
            raise RuntimeError(f"Internal error: impossible to build the property '{nc.meth_name}' of class '{nc.class_name}' wih arguments {nc.args.header}.")
        
        nc.settable = settable
        return nc

    # ----------------------------------------------------------------------------------------------------
    # A node property
    
    @classmethod
    def NodeProperty(cls, node, class_name, meth_name, sockets_name, out_name, settable=False, **variation):
        nc = cls('NODE_PROP', node, class_name, meth_name, out_name=out_name, **variation)
        nc.sockets_name = sockets_name
        nc.settable  = settable
        
        return nc
    
    # ----------------------------------------------------------------------------------------------------
    # Implement node properties
    
    @staticmethod
    def NodeProperties(node, class_name, meth_name, prop_names=[], settables=False, **variation):
        
        sockets = NodeCall.Property(node, class_name, meth_name, **variation) 
        if not sockets.return_sockets:
            raise RuntimeError(f"Internal error: the node {sockets.node.node_name} has not several output sockets to build several node properties {sockets.class_name}.{sockets.meth_name}.")

        calls = [sockets]
        
        if not prop_names:
            prop_names = [socket.uname for socket in node.outputs]
            
        if not isinstance(settables, (list, tuple)):
            settables = [settables] * len(node.outputs)
        
        for socket, prop_name, settable in zip(node.outputs, prop_names, settables):
            calls.append(NodeCall.NodeProperty(node, class_name, prop_name, meth_name, socket.uname, settable=settable, **variation))
            
        return calls
    
    # ----------------------------------------------------------------------------------------------------
    # Attributes
    # build attributes names and params
    
    @classmethod
    def Attribute(cls, node, class_name, meth_name, capture=False, domain='POINT', data_type='FLOAT'):
        nc = cls('ATTRIBUTE', node, class_name, meth_name)

        nc.capture   = capture
        nc.domain    = domain
        nc.data_type = data_type
        
        return nc
    
    @staticmethod
    def Attributes(node, class_name, base_name, domains='POINT', prop_names=None):

        def data_type(dtype):
            data_types = {'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'COLOR': 'FLOAT_COLOR'}
            if dtype in data_types:
                return data_types[dtype]
            else:
                return dtype
            
        attrs = []
    
        for socket_index, socket in enumerate(node.outputs):
            
            if prop_names is None:
                socket_name = f"_{socket.name}" if len(node.outputs) > 1 else ""
                meth_name   = f"{base_name}{socket_name}"
            else:
                meth_name = prop_names[socket_index]
            
            # ---------------------------------------------------------------------------
            # The domains can be:
            # 1. a single string
            # 2. a list of strings
            # 3. a set of strings
            #
            # In case 1. and 2., the capture_{name} method is implement with defaut domain
            # set to the first item in the list
            # Otherwise (case 2.), the capture_{name} is not implemented
            #
            # This allow to implement capture_{name} once and to implement further
            # domains in class children
            
            domains = [domains] if isinstance(domains, str) else domains
            
            # ----- Implement the general capture_.... method
            
            if isinstance(domains, list):
                attrs.append(NodeCall.Attribute(node, class_name, f"capture_{meth_name}", capture=True, domain=domains[0], data_type=data_type(socket.bsocket.type)))

            # ----- Implement one metod per domain
            
            domain_prefix = len(domains) > 1 or isinstance(domains, set)
            for domain in domains:
                sdomain = f"{domain.lower()}_" if domain_prefix else ""
                attrs.append(NodeCall.Attribute(node, class_name, f"{sdomain}{meth_name}", capture=False, domain=domain, data_type=data_type(socket.bsocket.type)))
                
        return attrs        

    # ----------------------------------------------------------------------------------------------------
    # The call is a method using self
    
    @property
    def use_self(self):
        return self.FAMILIES[self.family][2]
        
    # ----------------------------------------------------------------------------------------------------
    # Returned sockets str
    
    @property
    def returned_sockets_string(self):
        socks = self.returned_sockets
        s = "["
        sep = ""
        for sock in socks:
            s += f"{sep}{sock.uname} ({sock.class_name})"
            sep = ", "
        return s + "]"
    
    # ----------------------------------------------------------------------------------------------------
    # Node creation
    
    @property
    def node_creation(self):
        
        if self.family == 'ATTRIBUTE':
            node_name = "Attribute"
        else:
            node_name = f"Node{self.node.node_name}"
        
        if self.family == 'ATTRIBUTE_OLD':

            if self.capture:
                sdomain = "domain"
            else:
                sdomain = f"'{self.domain}'"
            snode = f"nodes.Attribute(bl_idname='{self.node.bl_idname}', name='{self.meth_name}', owner_socket=self, data_type='{self.data_type}', domain={sdomain})"
            
        else:
            snode = f"nodes.{node_name}({self.args.node_call})"
        
        if self.family == 'STACK':
            return f"self.stack({snode})"
        
        else:
            return f"{snode}.output"
        
        """
        elif len(self.returned_sockets) == 0:
            return snode
        
        elif len(self.returned_sockets) == 1:
            ret_class = self.ret_class if self.ret_class in ['cls', self.class_name] else "gn." + self.ret_class
            return f"{ret_class}({snode}.{self.out_name})"
        
        else:
            return snode
        """
        
    """
    @property
    def sockets_creation(self):
        s = ""
        for socket in self.returned_sockets:
            s += f", {socket.uname}={socket.class_name}(node.{socket.uname})"
        return f"Sockets({s[2:]})"
    """
    
    # ----------------------------------------------------------------------------------------------------
    # The string for what is returned (used in comments)
    
    @property
    def return_str(self):
        socks = self.returned_sockets
        if self.family == 'STACK':
            return self.class_name
            
        elif len(socks) == 0:
            return "None"
            
        elif self.return_sockets:
            return f"Sockets {self.returned_sockets_string}"
            
        else:
            return self.class_name if self.ret_class == 'cls' else self.ret_class
    

    # ----------------------------------------------------------------------------------------------------
    # Class comment: line generated at class level
    
    @property
    def class_comment(self):
        return f"{self.meth_name:20s} : {self.return_str}"
        
    # ----------------------------------------------------------------------------------------------------
    # Method comment: generated within the method
    
    def gen_comment(self):
        
        if self.class_name == 'GLOBAL':
            _1_ = ""
            _2_ = "    "
            _3_ = _2_ * 2
        else:
            _1_ = "    "
            _2_ = _1_ * 2
            _3_ = _1_ * 3
            
        yield _2_ + '"""' + f" {self.FAMILIES[self.family][0]} {self.meth_name} using node Node{self.node.node_name}"
        
        if self.family == 'NODE_PROP':
            yield f" on output socket {self.out_name}"
            
        yield "\n\n"
        
        # ----------------------------------------------------------------------------------------------------
        # Arguments
        
        yield _2_ + "Arguments\n"
        yield _2_ + "---------\n"
        
        has_variations = False
        first_param = True
        for arg in self.args:
            if arg.is_variation:
                has_variations = True
            else:
                if not arg.is_input and first_param:
                    yield "\n"
                    first_param = False
                yield _3_ + arg.comment
        yield "\n"
        
        # ----------------------------------------------------------------------------------------------------
        # Variations

        if has_variations:
            yield _2_ + "Node parameters settings\n"
            yield _2_ + "------------------------\n"
            for arg in self.args:
                if arg.is_variation:
                    yield _3_ + arg.comment
            yield "\n"
            
        # ----------------------------------------------------------------------------------------------------
        # Return
        
        yield _2_ + "Returns\n"
        yield _2_ + "-------\n"
        yield _3_ + f"{self.return_str}\n"

        yield _2_ + '"""' + "\n\n"
        
    # ----------------------------------------------------------------------------------------------------
    # Generates the method
    
    def gen_method(self):
        
        if self.class_name == 'GLOBAL':
            _1_ = ""
            _2_ = "    "
            _3_ = _2_ * 2
        else:
            _1_ = "    "
            _2_ = _1_ * 2
            _3_ = _1_ * 3
        
        # ----------------------------------------------------------------------------------------------------
        # Prepare the node
        
        self.configure_node()
        
        # ----------------------------------------------------------------------------------------------------
        # Decorator and method name
        
        sep = ""
        if self.family in ['CONSTRUCTOR', 'CLASS']:
            yield _1_ + "@classmethod\n"
            yield _1_ + f"def {self.meth_name}(cls"
            sep = ", "
            
        elif self.family == 'STATIC':
            yield _1_ + "@staticmethod\n"
            yield _1_ + f"def {self.meth_name}("
            
        elif self.family in ['PROPERTY', 'NODE_PROP']:
            yield _1_ + "@property\n"
            yield _1_ + f"def {self.meth_name}("
            
        elif self.family == 'ATTRIBUTE':
            if not self.capture and not self.return_sockets:
                yield _1_ + "@property\n"
            yield _1_ + f"def {self.meth_name}(self"
            sepa = ", "

        else:
            yield _1_ + f"def {self.meth_name}("

        # ----------------------------------------------------------------------------------------------------
        # Arguments 
        
        s = self.args.header
        if s != "":
            yield sep + s
            
        if self.family == 'ATTRIBUTE':
            if self.capture:
                yield f", domain='{self.domain}'"
                #yield f", data_type='{self.data_type}'"
            
        yield "):\n"
        
        # ----------------------------------------------------------------------------------------------------
        # Doc
        
        for line in self.gen_comment():
            yield line
            
        # ----------------------------------------------------------------------------------------------------
        # A property
        
        if self.family == 'PROPERTY':
            yield _2_ + f"if not hasattr(self.top, '{self.meth_name}_'):\n"
            yield _3_ + f"self.top.{self.meth_name}_ = {self.node_creation}\n"
            
            """
            if self.return_sockets:
                yield _3_ + f"node = {self.node_creation}\n"
                yield _3_ + f"self.top.{self.meth_name}_ = {self.sockets_creation}\n"
            else:
                yield _3_ + f"self.top.{self.meth_name}_ = {self.node_creation}\n"
            """
            yield _2_ + f"return self.top.{self.meth_name}_\n\n"
            
        # ----------------------------------------------------------------------------------------------------
        # A node property
        
        elif self.family == 'NODE_PROP':
            yield _2_ + f"return self.{self.sockets_name}.{self.out_name}\n\n"
            
            if self.settable:
                yield _1_ + f"@{self.meth_name}.setter\n"
                yield _1_ + f"def {self.meth_name}(self, value):\n"
                yield _2_ + f"self.top.{self.sockets_name}.{self.out_name} = value\n\n"
                    
        # ----------------------------------------------------------------------------------------------------
        # Other
        
        else:
            yield _2_ + f"return {self.node_creation}\n\n"
            """
            if self.return_sockets:
                yield _2_ + f"node = {self.node_creation}\n"
                yield _2_ + f"return {self.sockets_creation}\n\n"
            else:
                yield _2_ + f"return {self.node_creation}\n\n"
            """
                

# =============================================================================================================================
# Parameters to call a Node

class NodeCall_OLD:
    
    def __init__(self, bl_idname, meth_name, family='METHOD', self_name=None, out_name=None, ret_class=None, variation={}, domains=None, prop_names=None, arg_hooks={}):

        self.bl_idname  = bl_idname
        self.meth_name  = meth_name
        self.family     = family
        self.self_name  = self_name
        self.out_name   = out_name
        self.ret_class  = ret_class
        self.variation  = variation
        self.domains    = domains
        self.prop_names = prop_names
        self.arg_hooks  = arg_hooks
        
    def __repr__(self):
        s = f"<Method '{self.meth_name}' with node '{self.bl_idname}'"
        if self.variation:
            s += f", {self.variation}"
        return s + ">"
    
    # ----------------------------------------------------------------------------------------------------
    # Attributes
    # build attributes names and params
    
    def attributes(self, node):
        
        class Attr:
            pass

        def data_type(dtype):
            data_types = {'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'COLOR': 'FLOAT_COLOR'}
            if dtype in data_types:
                return data_types[dtype]
            else:
                return dtype
        
        attrs = []
    
        for socket_index, socket in enumerate(node.outputs):
            
            if self.prop_names is  None:
                socket_name = f"_{socket.name}" if len(node.outputs) > 1 else ""
                meth_name = f"{self.meth_name}{socket_name}"
            else:
                meth_name = self.prop_names[socket_index]
            
            # ---------------------------------------------------------------------------
            # The domains can be:
            # 1. a single string
            # 2. a list of strings
            # 3. a set of strings
            #
            # In case 1. and 2., the capture_{name} method is implement with defaut domain
            # set to the first item in the list
            # Otherwise (case 2.), the capture_{name} is not implemented
            #
            # This allow to implement capture_{name} once and to implement further
            # domains in class children
            
            domains = [self.domains] if isinstance(self.domains, str) else self.domains
            if isinstance(domains, list):
                
                attr = Attr()
                attr.capture   = True
                attr.domain    = domains[0]
                attr.meth_name = f"capture_{meth_name}"
                attr.data_type = data_type(socket.bsocket.type)
                attr.ret_class = socket.class_name
                attr.index     = socket_index
                
                attrs.append(attr)
                
            domain_prefix = len(domains) > 1 or isinstance(domains, set)
            
            for domain in domains:
                
                sdomain = f"{domain.lower()}_" if domain_prefix else ""

                attr = Attr()
                attr.capture   = False
                attr.domain    = domain
                attr.meth_name = f"{sdomain}{meth_name}"
                attr.data_type = data_type(socket.bsocket.type)
                attr.ret_class = socket.class_name
                attr.index     = socket_index
                
                attrs.append(attr)
                
        return attrs    
    
    # ----------------------------------------------------------------------------------------------------
    # Generate the comment
    
    def comment(self, class_name, node=None):
        
        s = f"{self.meth_name:20s} :"
        
        if self.ret_class == 'NODE':

            s += f" node {self.bl_idname}"

        else:
            cname = self.ret_class
            if cname == 'SAME':
                cname = class_name

            if cname is not None:
                s += f" ({cname})"
                
            s += f" {self.bl_idname:25s}"
                
            if self.out_name is not None:
                s += f".{self.out_name}"
            
        if self.variation:
            s += "("
            for k, v in self.variation.items():
                s += f"{k} = {v}"
            s += ")"
            
        # ----- Properties linked to the node output sockets

        if self.family == 'NODE_PROP':
            s += "\n"
            
            names = [socket.uname for socket in node.outputs]
            if self.prop_names is None:
                pnames = names
            else:
                pnames = self.prop_names
                
            for pname, name in zip(pnames, names):
                s += _2_ + f"{pname:20s} : {self.meth_name}.{name}\n"

        # ----- Attributes
        
        if self.family == 'ATTRIBUTE':
            attrs = self.attributes(node)
            s += "\n"
            for attr in attrs:
                s += _2_ + f"{attr.meth_name:20s} : {attr.ret_class} on domain {attr.domain}\n"
            
        return s

# =============================================================================================================================
# A variation is a a value set to a parameter
#
# For a defined parameter, one function / method can be generated for each possible variation
#
# The variations can give birth to different methods within a same class:
# - operation for a math node
#
# Or they can give birth to the same method among several classes:
# - random generator

class Variations:
    
    def __init__(self, param_name, class_name=None, family='METHOD', values={}, comment=None):

        self.param_name = param_name
        self.class_name = class_name
        self.family     = family
        self.values     = values
        self.comment    = comment

    # ---------------------------------------------------------------------------
    # Get the functions implementations
    
    def functions(self, bl_idname):
        
        funcs = []
        
        for value, spec in self.values.items():
            
            fname = spec[0]
            if fname != '':
                funcs.append(NodeCall(
                    bl_idname  = bl_idname,
                    meth_name  = fname,
                    family     = 'FUNCTION',
                    ret_class  = spec[2],
                    variation  = {self.param_name: value},
                    ))
        
        return funcs
    
    # ---------------------------------------------------------------------------
    # Get the methods implementations
    
    def methods(self, bl_idname, class_name):
        
        meths = []
        
        # ---------------------------------------------------------------------------
        # If self.class_name is defined, it must match the argument
        
        if self.class_name is not None:
            if isinstance(self.class_name, (tuple, list)):
                if class_name not in self.class_name:
                    return meths
            else:
                if self.class_name != class_name:
                    return meths
                
        # ---------------------------------------------------------------------------
        # class name is item # 3
        
        for value, spec in self.values.items():
            
            # ---------------------------------------------------------------------------
            # The class name must be specified in the spec
            # Let's check this line is for the requested class
            
            cname = spec[2]
            
            if self.class_name is None:
                if cname is None:
                    raise RuntimeError(f"Variation of parameter '{self.param_name}' must give the class name for the method '{spec[1]}'.")
                
                if isinstance(cname, (tuple, list)):
                    if class_name not in cname:
                        continue
                else:
                    if class_name != cname:
                        continue
                    
            # ---------------------------------------------------------------------------
            # Let's add the node call
            
            meths.append(NodeCall(
                bl_idname  = bl_idname,
                meth_name  = spec[0] if class_name == 'GLOBAL' else spec[1],
                family     = self.family,
                self_name  = None,
                out_name   = None,
                ret_class  = spec[3],
                variation  = {self.param_name: value},
                ))
            
        return meths
    
    

# -----------------------------------------------------------------------------------------------------------------------------
# The variations
#
# 0: Function name
# 1: mehod name
# 2: class name to which the method applies (methods only)
# 3: output socket class name
#    - None: use default
#    - NODE: return the Node 
#    - SAME: use class name
#    - str : class name 

VARIATIONS = {
    
    'FunctionNodeBooleanMath': Variations(param_name = 'operation', class_name = ('GLOBAL', 'Boolean'), values = {
         'AND'                : ('b_and'               , 'b_and'        , None, None),
         'OR'                 : ('b_or'                , 'b_or'         , None, None),
         'NOT'                : ('b_not'               , 'b_not'        , None, None),
         'NAND'               : ('nand'                , 'nand'         , None, None),
         'NOR'                : ('nor'                 , 'nor'          , None, None),
         'XNOR'               : ('xnor'                , 'xnor'         , None, None),
         'XOR'                : ('xor'                 , 'xor'          , None, None),
         'IMPLY'              : ('imply'               , 'imply'        , None, None),
         'NIMPLY'             : ('nimply'              , 'nimply'       , None, None),
         }, comment = "Boolean math"),


    'ShaderNodeMath' : Variations(param_name = 'operation', class_name = ('GLOBAL', 'Integer', 'Float'), values = {
         'ADD'                : ('add'                 , 'add'          , None, 'SAME'      ),
         'SUBTRACT'           : ('substract'           , 'substract'    , None, 'SAME'      ),
         'MULTIPLY'           : ('multiply'            , 'multiply'     , None, 'SAME'      ),
         'DIVIDE'             : ('divide'              , 'divide'       , None, 'Float'     ),
         'MULTIPLY_ADD'       : ('multiply_add'        , 'multiply_add' , None, 'SAME'      ),
         'POWER'              : ('pow'                 , 'pow'          , None, 'SAME'      ),
         'LOGARITHM'          : ('log'                 , 'log'          , None, 'Float'     ),
         'SQRT'               : ('sqrt'                , 'sqrt'         , None, 'Float'     ),
         'INVERSE_SQRT'       : ('inverse_sqrt'        , 'inverse_sqrt' , None, 'Float'     ),
         'ABSOLUTE'           : ('abs'                 , 'abs'          , None, 'SAME'      ),
         'EXPONENT'           : ('exp'                 , 'exp'          , None, 'Float'     ),
         'MINIMUM'            : ('min'                 , 'min'          , None, 'SAME'      ),
         'MAXIMUM'            : ('max'                 , 'max'          , None, 'SAME'      ),
         'LESS_THAN'          : ('less_than'           , 'less_than'    , None, 'Boolean'   ),
         'GREATER_THAN'       : ('greater_than'        , 'greater_than' , None, 'Boolean'   ),
         'SIGN'               : ('sign'                , 'sign'         , None, 'Integer'   ),
         'COMPARE'            : ('compare'             , 'compare'      , None,  None       ),
         'SMOOTH_MIN'         : ('smooth_min'          , 'smooth_min'   , None, 'SAME'      ),
         'SMOOTH_MAX'         : ('smooth_max'          , 'smooth_max'   , None, 'SAME'      ),
         'ROUND'              : ('round'               , 'round'        , None, 'Integer'   ),
         'FLOOR'              : ('floor'               , 'floor'        , None, 'Integer'   ), 
         'CEIL'               : ('ceil'                , 'ceil'         , None, 'Integer'   ),
         'TRUNC'              : ('trunc'               , 'trunc'        , None, 'Integer'   ), 
         'FRACT'              : ('fract'               , 'fract'        , None, 'Float'     ),
         'MODULO'             : ('modulo'              , 'modulo'       , None, 'SAME'      ),
         'WRAP'               : ('wrap'                , 'wrap'         , None,  None       ),
         'SNAP'               : ('snap'                , 'snap'         , None,  None       ),
         'PINGPONG'           : ('pingpong'            , 'pingpong'     , None, 'SAME'      ),
         'SINE'               : ('sin'                 , 'sin'          , None, 'Float'     ),
         'COSINE'             : ('cos'                 , 'cos'          , None, 'Float'     ),
         'TANGENT'            : ('tan'                 , 'tan'          , None, 'Float'     ),
         'ARCSINE'            : ('arcsin'              , 'arcsin'       , None, 'Float'     ),
         'ARCCOSINE'          : ('arccos'              , 'arccos'       , None, 'Float'     ),
         'ARCTANGENT'         : ('arctan'              , 'arctan'       , None, 'Float'     ),
         'ARCTAN2'            : ('arctan2'             , 'arctan2'      , None, 'Float'     ),
         'SINH'               : ('sinh'                , 'sinh'         , None, 'Float'     ),
         'COSH'               : ('cosh'                , 'cosh'         , None, 'Float'     ),
         'TANH'               : ('tanh'                , 'tanh'         , None, 'Float'     ),
         'RADIANS'            : ('radians'             , 'radians'      , None, 'Float'     ),
         'DEGREES'            : ('degrees'             , 'degrees'      , None, 'Float'     ),    
         },comment = "Float maths"),
                                 
    'ShaderNodeVectorMath' : Variations(param_name = 'operation', class_name=('GLOBAL', 'Vector'), values = {
         'ADD'                : ('vector_add'          , 'add'          , None, None),
         'SUBTRACT'           : ('vector_subtract'     , 'substract'    , None, None),
         'MULTIPLY'           : ('vector_multiply'     , 'multiply'     , None, None),
         'DIVIDE'             : ('vector_divide'       , 'divide'       , None, None),
         'MULTIPLY_ADD'       : ('vector_multiply_add' , 'multiply_add' , None, None),
         'CROSS_PRODUCT'      : ('cross'               , 'cross'        , None, None),
         'PROJECT'            : ('project'             , 'project'      , None, None),
         'REFLECT'            : ('reflect'             , 'reflect'      , None, None),
         'REFRACT'            : ('refract'             , 'refract'      , None, None),
         'FACEFORWARD'        : ('faceforward'         , 'faceforward'  , None, None),
         'DOT_PRODUCT'        : ('dot'                 , 'dot'          , None, None),
         'DISTANCE'           : ('distance'            , 'distance'     , None, None),
         'LENGTH'             : ('length'              , 'length'       , None, None),
         'SCALE'              : ('scale'               , 'scale'        , None, None),
         'NORMALIZE'          : ('normalize'           , 'normalize'    , None, None),
         'ABSOLUTE'           : ('absolute'            , 'absolute'     , None, None),
         'MINIMUM'            : ('vector_min'          , 'min'          , None, None),
         'MAXIMUM'            : ('vector_max'          , 'max'          , None, None),
         'FLOOR'              : ('vector_floor'        , 'floor'        , None, None),
         'CEIL'               : ('vector_ceil'         , 'ceil'         , None, None),
         'FRACTION'           : ('vector_fraction'     , 'fraction'     , None, None),
         'MODULO'             : ('vector_modulo'       , 'modulo'       , None, None),
         'WRAP'               : ('wrap'                , 'wrap'         , None, None),
         'SNAP'               : ('snap'                , 'snap'         , None, None),
         'SINE'               : ('vector_sin'          , 'sin'          , None, None),
         'COSINE'             : ('vector_cos'          , 'cos'          , None, None),
         'TANGENT'            : ('vector_tan'          , 'tan'          , None, None),

        }, comment = "Vector maths"),

    'GeometryNodeMeshBoolean' : Variations(param_name = 'operation', class_name = 'Mesh', values = {
         'INTERSECT'          : ('intersect'           , 'intersect'    , None, None),
         'UNION'              : ('union'               , 'union'        , None, None),
         'DIFFERENCE'         : ('difference'          , 'difference'   , None, None),
         },comment = "Mesh boolean operation"),


    'FunctionNodeRandomValue' : Variations(param_name = 'data_type', family='CONSTRUCTOR', values = {
         'FLOAT'              : ('random_float'        , 'Random'       , 'Float'         , None),
         'INT'                : ('random_integer'      , 'Random'       , 'Integer'       , None),
         'FLOAT_VECTOR'       : ('random_vector'       , 'Random'       , 'Vector'        , None),
         'BOOLEAN'            : ('random_boolean'      , 'Random'       , 'Boolean'       , None),
         },comment = "Random value"),

    'GeometryNodeSwitch' : Variations(param_name = 'input_type', values = {
         'FLOAT'              : ('switch_float'        , 'switch'       , 'Float'         , None),
         'INT'                : ('switch_integer'      , 'switch'       , 'Integer'       , None),
         'BOOLEAN'            : ('switch_boolean'      , 'switch'       , 'Boolean'       , None),
         'VECTOR'             : ('switch_vector'       , 'switch'       , 'Vector'        , None),
         'STRING'             : ('switch_string'       , 'switch'       , 'String'        , None),
         'RGBA'               : ('switch_color'        , 'switch'       , 'Color'         , None),
         'OBJECT'             : ('switch_object'       , 'switch'       , 'Object'        , None),
         'IMAGE'              : ('switch_image'        , 'switch'       , 'Image'         , None),
         'GEOMETRY'           : ('switch_geometry'     , 'switch'       , 'Geometry'      , None),
         'COLLECTION'         : ('switch_collection'   , 'switch'       , 'Collection'    , None),
         'TEXTURE'            : ('switch_texture'      , 'switch'       , 'Texture'       , None),
         'MATERIAL'           : ('switch_material'     , 'switch'       , 'Material'      , None),
         },comment = "Swicth between two data"),
    
    'FunctionNodeCompare' : Variations(param_name='data_type', values = {
        'FLOAT'               : ('compare_float'       , 'compare'      , 'Float'         , None),
        'INT'                 : ('compare_integer'     , 'compare'      , 'Integer'       , None),
        'VECTOR'              : ('compare_vector'      , 'compare'      , 'Vector'        , None),
        'STRING'              : ('compare_string'      , 'compare'      , 'String'        , None),
        'RGBA'                : ('compare_color'       , 'compare'      , 'Color'         , None),
        }),

    'GeometryNodeViewer' : Variations(param_name = 'data_type', values = {
         'FLOAT'              : ('float_viewer'        , 'to_viewer'    , 'Float'         ,'NODE'),
         'INT'                : ('integer_viewer'      , 'to_viewer'    , 'Integer'       ,'NODE'),
         'FLOAT_VECTOR'       : ('vector_viewer'       , 'to_viewer'    , 'Vector'        ,'NODE'),
         'FLOAT_COLOR'        : ('color_viewer'        , 'to_viewer'    , 'Color'         ,'NODE'),
         'BOOLEAN'            : ('boolean_viewer'      , 'to_viewer'    , 'Boolean'       ,'NODE'),
    },comment = "To viewer node"),
}


MATH = {
    'ADD'                : ('add'                 , 'SAME'      ),
    'SUBTRACT'           : ('subtract'            , 'SAME'      ),
    'MULTIPLY'           : ('multiply'            , 'SAME'      ),
    'DIVIDE'             : ('divide'              , 'Float'     ),
    'MULTIPLY_ADD'       : ('multiply_add'        , 'SAME'      ),
    'POWER'              : ('pow'                 , 'SAME'      ),
    'LOGARITHM'          : ('log'                 , 'Float'     ),
    'SQRT'               : ('sqrt'                , 'Float'     ),
    'INVERSE_SQRT'       : ('inverse_sqrt'        , 'Float'     ),
    'ABSOLUTE'           : ('abs'                 , 'SAME'      ),
    'EXPONENT'           : ('exp'                 , 'Float'     ),
    'MINIMUM'            : ('min'                 , 'SAME'      ),
    'MAXIMUM'            : ('max'                 , 'SAME'      ),
    'LESS_THAN'          : ('less_than'           , 'Boolean'   ),
    'GREATER_THAN'       : ('greater_than'        , 'Boolean'   ),
    'SIGN'               : ('sign'                , 'Integer'   ),
    'COMPARE'            : ('compare'             , 'Boolean'   ),
    'SMOOTH_MIN'         : ('smooth_min'          , 'SAME'      ),
    'SMOOTH_MAX'         : ('smooth_max'          , 'SAME'      ),
    'ROUND'              : ('round'               , 'Integer'   ),
    'FLOOR'              : ('floor'               , 'Integer'   ), 
    'CEIL'               : ('ceil'                , 'Integer'   ),
    'TRUNC'              : ('trunc'               , 'Integer'   ), 
    'FRACT'              : ('fract'               , 'Float'     ),
    'MODULO'             : ('modulo'              , 'SAME'      ),
    'WRAP'               : ('wrap'                , 'SAME'      ),
    'SNAP'               : ('snap'                , 'SAME'      ),
    'PINGPONG'           : ('pingpong'            , 'SAME'      ),
    'SINE'               : ('sin'                 , 'Float'     ),
    'COSINE'             : ('cos'                 , 'Float'     ),
    'TANGENT'            : ('tan'                 , 'Float'     ),
    'ARCSINE'            : ('arcsin'              , 'Float'     ),
    'ARCCOSINE'          : ('arccos'              , 'Float'     ),
    'ARCTANGENT'         : ('arctan'              , 'Float'     ),
    'ARCTAN2'            : ('arctan2'             , 'Float'     ),
    'SINH'               : ('sinh'                , 'Float'     ),
    'COSH'               : ('cosh'                , 'Float'     ),
    'TANH'               : ('tanh'                , 'Float'     ),
    'RADIANS'            : ('radians'             , 'Float'     ),
    'DEGREES'            : ('degrees'             , 'Float'     ),   
 }

VECTOR_MATH = {
    'ADD'                : 'add',
    'SUBTRACT'           : 'subtract',
    'MULTIPLY'           : 'multiply',
    'DIVIDE'             : 'divide',
    'MULTIPLY_ADD'       : 'multiply_add',
    'CROSS_PRODUCT'      : 'cross',
    'PROJECT'            : 'project',
    'REFLECT'            : 'reflect',
    'REFRACT'            : 'refract',
    'FACEFORWARD'        : 'faceforward',
    'DOT_PRODUCT'        : 'dot',
    'DISTANCE'           : 'distance',
    'LENGTH'             : 'length',
    'SCALE'              : 'scale',
    'NORMALIZE'          : 'normalize',
    'ABSOLUTE'           : 'absolute',
    'MINIMUM'            : 'min',
    'MAXIMUM'            : 'max',
    'FLOOR'              : 'floor',
    'CEIL'               : 'ceil',
    'FRACTION'           : 'fraction',
    'MODULO'             : 'modulo',
    'WRAP'               : 'wrap',
    'SNAP'               : 'snap',
    'SINE'               : 'sin',
    'COSINE'             : 'cos',
    'TANGENT'            : 'tan',
}



# ========================================================================================================================
# The data class generator                
        
class DataClass:
    
    def __init__(self, nodes, class_name, super_class):
        
        self.nodes       = nodes
        self.class_name  = class_name
        self.super_class = super_class
        
        self.methods_     = []
        
        return
        
        # Add the methods coming for parameter variations
        
        for blid, vs in VARIATIONS.items():
            self.methods_.extend(vs.methods(blid, self.class_name))
            
        blid = 'FunctionNodeBooleanMath'
        self.add_call('METHOD', blid, 'b_and', operaton='AND')
            
            
    # ----------------------------------------------------------------------------------------------------
    # Methods per family
    
    def methods(self, family=None):
        meths = []
        for meth in self.methods_:
            if family is None or family == meth.family:
                meths.append(meth)
        return meths
    
    # ----------------------------------------------------------------------------------------------------
    # Add a method
    
    def add_call(self, family, bl_idname, meth_name, **kwargs):
        self.methods_.append(NodeCall(family, self.nodes[bl_idname], class_name=self.class_name, meth_name=meth_name, **kwargs))
        
    # ----------------------------------------------------------------------------------------------------
    # Add node properties
    
    def add_node_properties(self, bl_idname, meth_name, **kwargs):
        ncs = NodeCall.NodeProperties(self.nodes[bl_idname], self.class_name, meth_name, **kwargs)
        self.methods_.extend(ncs)
        
    # ----------------------------------------------------------------------------------------------------
    # Add attributes
    
    def add_attribute(self, bl_idname, meth_name, domains=None, **kwargs):
        if domains is None:
            domains = ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
            
        ncs = NodeCall.Attributes(self.nodes[bl_idname], self.class_name, meth_name, domains=domains, **kwargs)
        self.methods_.extend(ncs)
    
    # ----------------------------------------------------------------------------------------------------
    # Add node creations instructions
    
    def add_constructor(self, bl_idname, meth_name, variation={}):
        self.methods_.append(NodeCall(bl_idname, meth_name, family='CONSTRUCTOR', ret_class='cls', variation=variation))
        
    def add_static(self, bl_idname, meth_name, ret_class=None, variation={}):
        self.methods_.append(NodeCall(bl_idname, meth_name, family='STATIC', ret_class=ret_class, variation=variation))
        
    def add_class_method(self, bl_idname, meth_name):
        self.methods_.append(NodeCall(bl_idname, meth_name, family='CLASS'))

    def add_property(self, bl_idname, meth_name, ret_class=None):
        self.methods_.append(NodeCall(bl_idname, meth_name, family='PROPERTY', ret_class=ret_class))
        
    def add_node_prop(self, bl_idname, meth_name, prop_names=None):
        self.methods_.append(NodeCall(bl_idname, meth_name, family='NODE_PROP', ret_class='NODE', prop_names=prop_names))

    def add_attribute_OLD(self, bl_idname, meth_name, domains=None, prop_names=None):
        if domains is None:
            domains = ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
            
        self.methods_.append(NodeCall(bl_idname, meth_name, family='ATTRIBUTE', domains=domains, prop_names=prop_names))
            
    def add_method(self, bl_idname, meth_name, self_name=None, variation={}, ret_class=None, arg_hooks={}, stack=False):
        if stack:
            self.methods_.append(NodeCall(bl_idname, meth_name, self_name=self_name, variation=variation, family='STACK', ret_class='NODE', arg_hooks=arg_hooks))
        else:
            self.methods_.append(NodeCall(bl_idname, meth_name, self_name=self_name, variation=variation, family='METHOD', ret_class=ret_class, arg_hooks=arg_hooks))
            
    # ----------------------------------------------------------------------------------------------------
    # Template
    
    @staticmethod
    def get_template(template, replace={}):
        #s = inspect.getsource(method)
        s = template
        for templ, repl in replace.items():
            s = s.replace(templ, repl)
        return s
    
    # ----------------------------------------------------------------------------------------------------
    # Gen the comments
        
    def gen_comments(self):
        
        yield _1_ + '"""' + f" Socket data class {self.class_name}\n\n"
        
        for family, label in NodeCall.FAMILIES.items():
            meths = self.methods(family)
            if meths:
                meths.sort(key=lambda nc: nc.meth_name)
                yield _1_ + f"{label[1]}\n"
                yield _1_ + "-" * len(label[1]) + "\n"
                for nc in meths:
                    yield _2_ + f"{nc.class_comment}\n"
                yield "\n"
            
        yield _1_ + '"""' + "\n\n"
        
    # ----------------------------------------------------------------------------------------------------
    # Get the default out name and return class
    
    def get_ret_class(self, node_call, node):
        
        count = 0
        for socket in node.outputs:
            if socket.enabled:
                count += 1

        # ----- Output socket name and return class
        
        if node_call.ret_class == 'NODE' or count > 1:
            out_name  = None
            ret_class = None
            
        else:
            out_name  = node_call.out_name
            ret_class = self.class_name if node_call.ret_class == 'SAME' else node_call.ret_class
            
            if out_name is None and node.outputs:
                out_name = node.out_name
                
                if ret_class is None:
                    for sock in node.outputs:
                        if sock.enabled and sock.uname == out_name:
                            ret_class = sock.class_name
                            break
                        
        return out_name, ret_class
        
    # ----------------------------------------------------------------------------------------------------
    # Node creation
    
    def node_creation(self, node_call, node, args):
        return f"nodes.Node{node.node_name}({args.node_call})"
    
    # ----------------------------------------------------------------------------------------------------
    # Return one typed socket or a class made of typed sockets
    
    def sockets_return(self, node_call, node, node_creation):
        
        # ------ Depending on enabled sockets
        
        socks = []
        for socket in node.outputs:
            if socket.bsocket.enabled:
                socks.append(socket)

        # ------ Stack if no error
        
        if node_call.family == 'STACK':
            if len(socks) != 1:
                raise RuntimeError(f"Impossible to stack node {node.bnode.bl_idname} with output sockets {[sock.name for sock in socks]}")
                
            yield f"return self.stack({node_creation})\n"

        # ------ Depending on enabled sockets
        
        elif len(socks) == 0:
            yield f"return {node_creation}\n"
        
        elif len(socks) == 1:
            sock = socks[0]
            out_name, ret_class = self.get_ret_class(node_call, node)
            if ret_class != self.class_name:
                ret_class = "gn." + ret_class
            yield f"return {ret_class}({node_creation}.{sock.uname})\n"
            #yield f"return {sock.class_name}({node_creation}.{sock.uname})\n"
            
        else:
            s = ""
            for sock in socks:
                s += f", {sock.uname}={sock.class_name}(node.{sock.uname})"
            
            yield f"node = {node_creation}\n"
            yield f"return Sockets({s[2:]})\n"

    # ---------------------------------------------------------------------------
    # Generate the class source code
        
    def gen_class(self):
        
        # ----------------------------------------------------------------------------------------------------
        # Generates module header
        
        yield "import geonodes as gn\n"
        yield "from geonodes.core import socket as bcls\n"
        yield "from geonodes.nodes import nodes\n"
        #if self.super_class.find('.') < 0:
        #    yield f"from geonodes import {self.super_class}\n"
        yield "import logging\n"
        yield "logger = logging.Logger('geonodes')\n"
        yield "\n"
        
        # ----------------------------------------------------------------------------------------------------
        # Utility: argument is a vector
        
        yield f"# {'-'*100}\n# Argument is a vector\n\n"
        yield "def is_vector(arg):\n"
        yield _1_ + "return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)\n\n"
        
        # ----------------------------------------------------------------------------------------------------
        # Sockets
        
        yield f"# {'-'*100}\n# Sockets outputs\n\n"
        yield "class Sockets(bcls.Sockets):\n"
        yield _1_ + "pass\n\n"

        # ---------------------------------------------------------------------------
        # Header
        
        yield  "\n# " + '='*110 + "\n"
        yield f"# Data class {self.class_name}\n\n"
        
        yield _0_ + f"class {self.class_name}({self.super_class}):\n"
        
        # ---------------------------------------------------------------------------
        # Documentation
            
        for line in self.gen_comments():
            yield line
            
        # ---------------------------------------------------------------------------
        # Methods
        
        for family, label in NodeCall.FAMILIES.items():
            
            meths = self.methods(family)
            if not meths:
                continue
            
            yield f"\n{_1_}# {'-'*100}\n{_1_}# {label[1]}\n\n"
            
            for nc in meths:
                
                for line in nc.gen_method():
                    yield line
                    
                continue
                
                
                
                # ----------------------------------------------------------------------------------------------------
                # Prepare the node
                
                node = nodes[nc.bl_idname]
                GEN_NODES.append(nc.bl_idname)
                node.set_parameters(nc.variation)

                # ----------------------------------------------------------------------------------------------------
                # Arguments
                
                if family in ['CONSTRUCTOR', 'STATIC', 'CLASS', 'ATTRIBUTE']:
                    
                    self_name = None

                else:
                    self_name = nc.self_name
                    if self_name is None and node.inputs:
                        first = None
                        for sock in node.inputs:
                            if sock.enabled:
                                if first is None:
                                    first = sock.uname
                                    
                                if sock.class_name == self.class_name: # or sock.is_multi_input:
                                    self_name = sock.uname
                                    break
                                
                        if self_name is None:
                            self_name = first
                            
                    if self_name is None:
                        raise RuntimeError(f"Impossible to find a valid input socket name for method '{nc.meth_name}' in class {self.class_name}.")
                
                
                args = node.build_arguments(only_enabled=True, variation=nc.variation, self_name=self_name, hooks=nc.arg_hooks)
                
                # ----------------------------------------------------------------------------------------------------
                # Node properties
                
                if family == 'NODE_PROP':
                    snode = self.node_creation(nc, node, args)
                    
                    yield _1_ + f"# {'-'*10} Node {node.node_name}\n\n"
                    
                    yield _1_ +  "@property\n"
                    yield _1_ + f"def {nc.meth_name}(self):\n"
                    yield _2_ + f"if not hasattr(self.top, '{nc.meth_name}_'):\n"
                    yield _3_ + f"self.top.{nc.meth_name}_ = nodes.Node{node.node_name}(self)\n"
                    yield _3_ + f"self.top.{nc.meth_name}_.prop_of = self.node\n"
                    yield _2_ + f"return self.top.{nc.meth_name}_\n\n"
                    
                    # ----- Note that it doesn't work if some output sockets are disabled
            
                    names = [socket.uname for socket in node.outputs]
                    if nc.prop_names is None:
                        pnames = names
                    else:
                        pnames = nc.prop_names
                    cnames = [socket.class_name for socket in node.outputs]
                    
                    for pname, name, cname in zip(pnames, names, cnames):
                        yield _1_ +  "@property\n"
                        yield _1_ + f"def {pname}(self):\n"
                        yield _2_ + f"if not hasattr(self.top, '{pname}_'):\n"
                        yield _3_ + f"self.top.{pname}_ = {cname}(self.top.{nc.meth_name}.{name})\n"
                        yield _2_ + f"return self.top.{pname}_\n\n"
                        
                        if True:
                            yield _1_ + f"@{pname}.setter\n"
                            yield _1_ + f"def {pname}(self, value):\n"
                            yield _2_ + f"_ = self.{nc.meth_name}\n"
                            yield _2_ + f"self.top.{pname}_ = value\n\n"
                    
                    continue
                
                # ----------------------------------------------------------------------------------------------------
                # Attribute
                    
                if family == 'ATTRIBUTE':
                    
                    yield _1_ + f"# {'-'*10} Attribute {node.bnode.bl_idname}\n\n"
                    
                    for attr in nc.attributes(node):
                        
                        if not args and not attr.capture:
                            yield _1_ +  "@property\n"
                            
                        yield _1_ + f"def {attr.meth_name}(self"

                        if args:
                            for arg in args:
                                yield arg.header

                        sdomain = f"'{attr.domain}'"
                        if attr.capture:
                            yield f", domain='{attr.domain}'"
                            sdomain = "domain"
                            
                        yield "):\n"

                        yield _2_ + f"return {attr.ret_class}(nodes.Node{node.node_name}("
                        sepa = ""
                        
                        for arg in args:
                            yield f"{sepa}{arg.name}={arg.name}"
                            sepa = ", "
                            
                        yield f"{sepa}owner_socket=self.socket, data_type='{attr.data_type}', domain={sdomain}).outputs[{attr.index}])\n\n"
                            
                    continue
                
                
                # ----------------------------------------------------------------------------------------------------
                # Decorator and method name
                
                sep = ""
                if family in ['CONSTRUCTOR', 'CLASS']:
                    yield _1_ + "@classmethod\n"
                    yield _1_ + f"def {nc.meth_name}(cls"
                    sep = ", "
                    
                elif family == 'STATIC':
                    yield _1_ + "@staticmethod\n"
                    yield _1_ + f"def {nc.meth_name}("
                    
                elif family in ['PROPERTY', 'ATTRIBUTE']:
                    yield _1_ + "@property\n"
                    yield _1_ + f"def {nc.meth_name}(self"
                else:
                    yield _1_ + f"def {nc.meth_name}("

                # ----------------------------------------------------------------------------------------------------
                # Function header
                
                if family != 'PROPERTY':
                    s = args.header
                    if s != "":
                        yield sep + s
                        
                yield "):\n"
                
                # ----------------------------------------------------------------------------------------------------
                # Doc
                
                yield _2_ + '""" ' + f"Method {nc.meth_name} on node Node{node.node_name}\n\n"
                
                yield _2_ + "Arguments\n"
                yield _2_ + "---------\n"
                
                has_variations = False
                for arg in args:
                    if arg.is_variation:
                        has_variations = True
                    else:
                        yield _3_ + arg.comment
                yield "\n"

                if has_variations:
                    yield _2_ + "Node parameters settings\n"
                    yield _2_ + "------------------------\n"
                    for arg in args:
                        if arg.is_variation:
                            yield _3_ + arg.comment
                    yield "\n"
                    
                yield _2_ + "Returns\n"
                yield _2_ + "-------\n"
                    
                yield _2_ + '"""' + "\n\n"
                
                # ----------------------------------------------------------------------------------------------------
                # Return

                for line in self.sockets_return(nc, node, self.node_creation(nc, node, args)):
                    yield _2_ + line
                yield "\n"
                
                if False:
                    if family == 'STACK':
                        yield _2_ + f"return self.stack({self.node_creation(nc, node, args)})\n\n"
                    
                    else:
                        for line in self.sockets_return(nc, node, self.node_creation(nc, node, args)):
                            yield _2_ + line
                        yield "\n"


# -----------------------------------------------------------------------------------------------------------------------------
# Global functions
                    
class GlobalGen(DataClass):
    
    def __init__(self, nodes):
        super().__init__(nodes, 'GLOBAL', '')
        
        self.add_call('METHOD', 'FunctionNodeCompare',          meth_name="compare"             )
        self.add_call('METHOD', 'GeometryNodeStringJoin',       meth_name="join_strings"        )
        self.add_call('METHOD', 'GeometryNodeAccumulateField',  meth_name="accumulate_field"    )
        self.add_call('METHOD', 'GeometryNodeFieldAtIndex',     meth_name="field_at_index"      )
        self.add_call('METHOD', 'GeometryNodeCollectionInfo',   meth_name="collection_info", arg_hooks={'collection': 'Collection.blender_collection'})
        self.add_call('METHOD', 'GeometryNodeObjectInfo',       meth_name="object_info",     arg_hooks={'object':     'Object.blender_object'})
        
        self.add_call('METHOD', 'GeometryNodeInputSceneTime', 'scene')
        
    def gen_class(self):
        
        # ---------------------------------------------------------------------------
        # Header
        
        yield  "\n# " + '='*110 + "\n"
        yield f"# Global functions\n\n"
        
        # ---------------------------------------------------------------------------
        # Loop on functions
        
        meths = self.methods('METHOD')
        
        for nc in meths:
            
            for line in nc.gen_method():
                yield line
                
            continue
            
            
            # ----------------------------------------------------------------------------------------------------
            # Prepare the node
            
            node = nodes[nc.bl_idname]
            GEN_NODES.append(nc.bl_idname)
            node.set_parameters(nc.variation)

            # ----------------------------------------------------------------------------------------------------
            # Arguments
            
            args = node.build_arguments(only_enabled=True, variation=nc.variation, hooks=nc.arg_hooks)
            
            # ----------------------------------------------------------------------------------------------------
            # Function header
            
            yield _0_ + f"def {nc.meth_name}({args.header}):\n"
            
            # ----------------------------------------------------------------------------------------------------
            # Return
            
            for line in self.sockets_return(nc, node, self.node_creation(nc, node, args)):
                yield _1_ + line
            yield "\n"
                    

# -----------------------------------------------------------------------------------------------------------------------------
# Boolean

class BooleanGen(DataClass):
    def __init__(self, nodes):
        
        super().__init__(nodes, 'Boolean', 'bcls.Boolean')
        
        # ----------------------------------------------------------------------------------------------------
        # Boolean math
        
        blid = 'FunctionNodeBooleanMath'
        self.add_call('METHOD', blid, 'b_and',  operation='AND'     )
        self.add_call('METHOD', blid, 'b_or',   operation='OR'      )
        self.add_call('METHOD', blid, 'b_not',  operation='NOT'     )
        self.add_call('METHOD', blid, 'nand',   operation='NAND'    )
        self.add_call('METHOD', blid, 'nor',    operation='NOR'     )
        self.add_call('METHOD', blid, 'xnor',   operation='XNOR'    )
        self.add_call('METHOD', blid, 'xor',    operation='XOR'     )
        self.add_call('METHOD', blid, 'imply',  operation='IMPLY'   )
        self.add_call('METHOD', blid, 'nimply', operation='NIMPLY'  )
        
        # ----------------------------------------------------------------------------------------------------
        # Constructors

        self.add_call('CONSTRUCTOR', 'FunctionNodeRandomValue', 'Random', data_type='BOOLEAN')

        # ----------------------------------------------------------------------------------------------------
        # Other methods
        
        self.add_call('METHOD', 'GeometryNodeFieldAtIndex', "field_at_index", self_name='value', ret_class='Boolean', data_type='BOOLEAN')
        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Boolean',     input_type='BOOLEAN')
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Integer
        
class IntegerGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Integer', 'bcls.Integer')
        
        # ----------------------------------------------------------------------------------------------------
        # Constructors

        self.add_call('CONSTRUCTOR', 'FunctionNodeRandomValue', 'Random', data_type='INT')

        # ----------------------------------------------------------------------------------------------------
        # Operations
        
        blid = 'ShaderNodeMath'
        for op, spec in MATH.items():
            ret_class = 'Integer' if spec[1] == 'SAME' else spec[1]
            self.add_call('METHOD', blid, spec[0], ret_class=ret_class, operation=op)

        # ----------------------------------------------------------------------------------------------------
        # Methods

        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Integer',     input_type='INT'    )

        self.add_call('METHOD', 'GeometryNodeAccumulateField',  "accumulate_field", data_type = 'INT')
        self.add_call('METHOD', 'GeometryNodeFieldAtIndex',     "field_at_index", self_name='value', ret_class='Integer', data_type = 'INT')
        

# -----------------------------------------------------------------------------------------------------------------------------
# Float

class FloatGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Float', 'bcls.Float')
        
        # ----------------------------------------------------------------------------------------------------
        # Constructors

        self.add_call('CONSTRUCTOR', 'FunctionNodeRandomValue', 'Random', data_type='FLOAT')

        # ----------------------------------------------------------------------------------------------------
        # Operations
        
        blid = 'ShaderNodeMath'
        for op, spec in MATH.items():
            ret_class = 'Float' if spec[1] == 'SAME' else spec[1]
            self.add_call('METHOD', blid, spec[0], ret_class=ret_class, operation=op)

        # ----------------------------------------------------------------------------------------------------
        # Methods

        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Float',       input_type='FLOAT'  )
        
        self.add_call('METHOD', 'FunctionNodeFloatToInt',     'to_integer',   ret_class='Integer')
        self.add_call('METHOD', 'FunctionNodeValueToString',  'to_string',    ret_class='String' )

        self.add_call('METHOD', 'GeometryNodeAccumulateField',  meth_name="accumulate_field", data_type='FLOAT')
        self.add_call('METHOD', 'GeometryNodeFieldAtIndex',     meth_name="field_at_index",   self_name='value', ret_class='Float', data_type='FLOAT')
        self.add_call('METHOD', 'ShaderNodeValToRGB',        'color_ramp'       )
        

        self.add_call('STACK', 'ShaderNodeFloatCurve',       'curve'            )
        self.add_call('STACK', 'ShaderNodeClamp',            'clamp'            )
        
        self.add_call('STACK', 'ShaderNodeMapRange',         'map_range',    data_type = 'FLOAT')
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Vector
        
class VectorGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Vector', 'bcls.Vector')
        
        # ----------------------------------------------------------------------------------------------------
        # Constructors

        self.add_call('CONSTRUCTOR', 'FunctionNodeRandomValue',         'Random', data_type='FLOAT_VECTOR')
        self.add_call('CONSTRUCTOR', 'ShaderNodeCombineXYZ',            'Combine')
        self.add_call('CONSTRUCTOR', 'FunctionNodeAlignEulerToVector',  'AlignToVector')
        
        # ----------------------------------------------------------------------------------------------------
        # Operations
        
        blid = 'ShaderNodeVectorMath'
        for op, meth_name in VECTOR_MATH.items():
            self.add_call('METHOD', blid, meth_name, operation=op)

        # ----------------------------------------------------------------------------------------------------
        # x, y, z properties
        
        self.add_node_properties('ShaderNodeSeparateXYZ', 'separate')

        # ----------------------------------------------------------------------------------------------------
        # Methods
    
        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Vector',      input_type='VECTOR' )
        
        self.add_call('STACK', 'ShaderNodeVectorCurve',           'curves'          )
        self.add_call('STACK', 'FunctionNodeAlignEulerToVector',  'align_to_vector' )
        self.add_call('STACK', 'FunctionNodeRotateEuler',         'rotate_euler'    )
        self.add_call('STACK', 'ShaderNodeMapRange',              'map_range',      data_type = 'FLOAT_VECTOR')
        
        self.add_call('METHOD', 'ShaderNodeVectorRotate',         'rotate'          )
        self.add_call('METHOD', 'GeometryNodeAccumulateField',    'accumulate_field', data_type = 'FLOAT_VECTOR')
        self.add_call('METHOD', 'GeometryNodeFieldAtIndex',       'field_at_index',   self_name='value', ret_class='Vector', data_type = 'FLOAT_VECTOR')
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# String

class ColorGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Color', 'bcls.Color')
        
        # ----------------------------------------------------------------------------------------------------
        # Constructor
        
        self.add_call('CONSTRUCTOR', 'ShaderNodeCombineRGB', 'Combine')
        
        # ----------------------------------------------------------------------------------------------------
        # r, g, b properties
        
        self.add_node_properties('ShaderNodeSeparateRGB', 'separate')

        # ----------------------------------------------------------------------------------------------------
        # Methods

        self.add_call('STACK', 'ShaderNodeRGBCurve',         'curves')

        self.add_call('METHOD', 'ShaderNodeMixRGB',          'mix')
        self.add_call('METHOD', 'GeometryNodeFieldAtIndex',  'field_at_index', self_name='value', ret_class='Color', data_type = 'FLOAT_COLOR')
        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Color',       input_type='RGBA'   )
        

# -----------------------------------------------------------------------------------------------------------------------------
# String

class StringGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'String', 'bcls.String')
        
        # ----------------------------------------------------------------------------------------------------
        # Property
        
        self.add_call('PROPERTY', 'FunctionNodeStringLength', 'length')
        
        # ----------------------------------------------------------------------------------------------------
        # Operation

        self.add_call('METHOD', 'GeometryNodeStringJoin', meth_name="join", self_name="strings")        
        
        # ----------------------------------------------------------------------------------------------------
        # Methods
        
        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='String',      input_type='STRING' )
        
        
        self.add_call('STACK', 'FunctionNodeReplaceString',      'replace')
        
        self.add_call('METHOD', 'FunctionNodeSliceString',       'slice')        
        self.add_call('METHOD', 'GeometryNodeStringToCurves',    'to_curves',  ret_class = 'Curve')        
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Geometry
        
class GeometryGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Geometry', 'bcls.Geometry')
        
        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Geometry',    input_type='GEOMETRY')

        self.add_attribute('GeometryNodeInputNormal',       'normal',           domains=None  )
        self.add_attribute('GeometryNodeInputTangent',      'tangent',          domains=None  )
        
        # ----- ID and Index
        
        self.add_attribute('GeometryNodeInputID',           'ID',               domains=['POINT']  )
        self.add_attribute('GeometryNodeInputIndex',        'index',            domains=['POINT']  )        
        self.add_attribute('GeometryNodeInputPosition',     'position',         domains=['POINT']  )
        self.add_attribute('GeometryNodeIsViewport',        'is_viewport',      domains=['POINT']  )
        
        
        self.add_node_properties('GeometryNodeBoundBox',           'bound_box',  prop_names=('box', 'box_min', 'box_max'))
        self.add_node_properties('GeometryNodeSeparateComponents', 'components', 
                          prop_names=('mesh_component', 'points_component', 'curve_component', 'volume_component', 'instances_component'))
        
        
        self.add_call('METHOD', 'GeometryNodeAttributeTransfer',    'transfer_boolean', data_type = 'BOOLEAN'      )
        self.add_call('METHOD', 'GeometryNodeAttributeTransfer',    'transfer_integer', data_type = 'INT'          )
        self.add_call('METHOD', 'GeometryNodeAttributeTransfer',    'transfer_float',   data_type = 'FLOAT'        )
        self.add_call('METHOD', 'GeometryNodeAttributeTransfer',    'transfer_vector',  data_type = 'FLOAT_VECTOR' )
        self.add_call('METHOD', 'GeometryNodeAttributeTransfer',    'transfer_color',   data_type = 'FLOAT_COLOR'  )

        self.add_call('STACK', 'GeometryNodeDeleteGeometry',       'delete_geometry'    )
        self.add_call('STACK', 'GeometryNodeMergeByDistance',      'merge_by_distance'  )
        self.add_call('STACK', 'GeometryNodeRealizeInstances',     'realize_instances'  )
        self.add_call('STACK', 'GeometryNodeReplaceMaterial',      'replace_material'   )
        self.add_call('STACK', 'GeometryNodeScaleElements',        'scale_elements'     )
        self.add_call('STACK', 'GeometryNodeSetID',                'set_ID'             )
        self.add_call('STACK', 'GeometryNodeSetMaterial',          'set_material'       )
        self.add_call('STACK', 'GeometryNodeSetMaterialIndex',     'set_material_index' )
        self.add_call('STACK', 'GeometryNodeSetPosition',          'set_position'       )
        self.add_call('STACK', 'GeometryNodeSetShadeSmooth',       'set_shade_smooth'   )
        self.add_call('STACK', 'GeometryNodeTransform',            'transform'          )
        
        self.add_call('METHOD', 'GeometryNodeAttributeDomainSize',  'attribute_domain_size' )
        self.add_call('METHOD', 'GeometryNodeAttributeRemove',      'attribute_remove'      )
        self.add_call('METHOD', 'GeometryNodeAttributeStatistic',   'attribute_statistic'   )
        self.add_call('METHOD', 'GeometryNodeSeparateGeometry',     'components'            )
        self.add_call('METHOD', 'GeometryNodeCaptureAttribute',     'capture_attribute'     )
        self.add_call('METHOD', 'GeometryNodeConvexHull',           'convex_hull'           )
        self.add_call('METHOD', 'GeometryNodeGeometryToInstance',   'to_instance'           )
        self.add_call('METHOD', 'GeometryNodeJoinGeometry',         'join'                  )
        self.add_call('METHOD', 'GeometryNodeProximity',            'proximity'             )
        self.add_call('METHOD', 'GeometryNodeRaycast',              'raycast'               )
        
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Mesh  
        
class MeshGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Mesh', 'gn.Geometry')
        
        # ----------------------------------------------------------------------------------------------------
        # Constructors
        
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshCircle'        ,'Circle'     )
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshCone'          ,'Cone'       )
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshCube'          ,'Cube'       )
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshCylinder'      ,'Cylinder'   )
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshGrid'          ,'Grid'       )
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshIcoSphere'     ,'IcoSphere'  )
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshLine'          ,'Line'       )
        self.add_call('CONSTRUCTOR', 'GeometryNodeMeshUVSphere'      ,'UVSphere'   )
        
        # ----------------------------------------------------------------------------------------------------
        # Boolean operation

        self.add_call('METHOD', 'GeometryNodeMeshBoolean', 'intersect',  operation='INTERSECT'  )
        self.add_call('METHOD', 'GeometryNodeMeshBoolean', 'union',      operation='UNION'      )
        self.add_call('METHOD', 'GeometryNodeMeshBoolean', 'difference', self_name='mesh_1',    operation='DIFFERENCE')
        
        # ----------------------------------------------------------------------------------------------------
        # Attributes

        self.add_attribute('GeometryNodeInputID',                   'ID',              domains={'FACE', 'EDGE', 'CORNER'})
        self.add_attribute('GeometryNodeInputIndex',                'index',           domains={'FACE', 'EDGE', 'CORNER'})
        
        self.add_attribute('GeometryNodeInputMeshEdgeNeighbors',   'edge_neighbors',   domains=['EDGE']  )
        self.add_attribute('GeometryNodeInputMeshFaceArea',        'face_area',        domains=['FACE']  )
        self.add_attribute('GeometryNodeInputMeshEdgeAngle',       'edge_angle',       domains=['EDGE']  )
        self.add_attribute('GeometryNodeInputMeshEdgeVertices',    'edge_vertices',    domains=['EDGE']  )
        self.add_attribute('GeometryNodeInputMeshFaceNeighbors',   'face_neighbors',   domains=['FACE']  )
        self.add_attribute('GeometryNodeInputMeshIsland',          'island',           domains=['FACE'],  prop_names=('island_index', 'island_count'))
        self.add_attribute('GeometryNodeInputMeshVertexNeighbors', 'vertex_neighbors', domains=['POINT'] )
        
        self.add_attribute('GeometryNodeInputMaterialIndex',       'material_index',   domains=['FACE']  )
        self.add_attribute('GeometryNodeInputShadeSmooth',         'shade_smooth',     domains=['FACE']  )
        
        
        # ----------------------------------------------------------------------------------------------------
        # Attributes

        self.add_call('STACK', 'GeometryNodeSplitEdges',         'split_edges'          )
        self.add_call('STACK', 'GeometryNodeSubdivideMesh',      'subdivide'            )
        self.add_call('STACK', 'GeometryNodeSubdivisionSurface', 'subdivision_surface'  )
        self.add_call('STACK', 'GeometryNodeTriangulate',        'triangulate'          )
        self.add_call('STACK', 'GeometryNodeDualMesh',           'dual'                 )
        self.add_call('STACK', 'GeometryNodeFlipFaces',          'flip_faces'           )
        
        self.add_call('METHOD', 'GeometryNodeExtrudeMesh',              'extrude',                       )
        self.add_call('METHOD', 'GeometryNodeMeshToCurve',              'to_curve',                     ret_class='Curve')
        self.add_call('METHOD', 'GeometryNodeMeshToPoints',             'to_points',                    ret_class='Points')
        self.add_call('METHOD', 'GeometryNodeDistributePointsOnFaces',  'distribute_points_on_faces',   ret_class='Points')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Points
        
class PointsGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Points', 'gn.Mesh')
        
        self.add_call('STACK',  'GeometryNodeSetPointRadius',    'set_radius'          )
        
        self.add_call('METHOD', 'GeometryNodeInstanceOnPoints',  'instance_on_points', ret_class='Instances')
        self.add_call('METHOD', 'GeometryNodePointsToVertices',  'to_vertices',        ret_class='Mesh'     )
        self.add_call('METHOD', 'GeometryNodePointsToVolume',    'to_volume',          ret_class='Volume'   )

# -----------------------------------------------------------------------------------------------------------------------------
# Instances
        
class InstancesGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Instances', 'gn.Mesh')
        
        self.add_attribute('GeometryNodeInputIndex',      'index',     domains=['INSTANCE']  )
        
        self.add_call('STACK', 'GeometryNodeRotateInstances',    'rotate'    )
        self.add_call('STACK', 'GeometryNodeScaleInstances',     'scale'     )
        self.add_call('STACK', 'GeometryNodeTranslateInstances', 'translate' )
        
        self.add_call('METHOD', 'GeometryNodeInstancesToPoints',  'to_points', ret_class='Points')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Volume
        
class VolumeGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Volume', 'gn.Mesh')
        
        self.add_call('METHOD', 'GeometryNodeVolumeToMesh', 'to_mesh' , ret_class='Mesh')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Spline

class SplineGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Spline', 'gn.Geometry')
        
        self.add_attribute('GeometryNodeInputSplineCyclic',         'cyclic',       domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputSplineResolution',     'resolution',   domains=['CURVE']  )
        self.add_attribute('GeometryNodeSplineLength',              'length',       domains=['CURVE']  , prop_names = ['length', 'point_count'])
        self.add_attribute('GeometryNodeSplineParameter',           'parameter',    domains=['CURVE']  )
        
        self.add_call('STACK', 'GeometryNodeSetSplineCyclic',              'set_cyclic'     )
        self.add_call('STACK', 'GeometryNodeSetSplineResolution',          'set_resolution' )

# -----------------------------------------------------------------------------------------------------------------------------
# Curve 
        
class CurveGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Curve', 'gn.Spline')
        
        self.add_call('CONSTRUCTOR', 'GeometryNodeCurvePrimitiveBezierSegment', 'BezierSegment'     )
        self.add_call('CONSTRUCTOR', 'GeometryNodeCurvePrimitiveCircle',        'Circle'            )
        self.add_call('CONSTRUCTOR', 'GeometryNodeCurvePrimitiveLine',          'Line'              )
        self.add_call('CONSTRUCTOR', 'GeometryNodeCurvePrimitiveQuadrilateral', 'Quadrilateral'     )
        self.add_call('CONSTRUCTOR', 'GeometryNodeCurveQuadraticBezier',        'QuadraticBezier'   )
        self.add_call('CONSTRUCTOR', 'GeometryNodeCurveStar',                   'Star'              )
        self.add_call('CONSTRUCTOR', 'GeometryNodeCurveSpiral',                 'Spiral'            )
        
        # Depending upon the way it is initialized, the node GeometryNodeCurveArc has
        # only one output socket or several

        self.add_call('CONSTRUCTOR', 'GeometryNodeCurveArc',            'ArcFromRadius', mode = 'RADIUS')
        self.add_call('STATIC',      'GeometryNodeCurveArc',            'ArcFromPoints', mode = 'POINTS')
        
        
        self.add_attribute('GeometryNodeInputID',           'ID',               domains={'SPLINE'})
        self.add_attribute('GeometryNodeInputIndex',        'index',            domains={'SPLINE'})
        
        
        self.add_attribute('GeometryNodeCurveEndpointSelection',        'endpoint_selection',       domains=['CURVE']  )
        self.add_attribute('GeometryNodeCurveHandleTypeSelection',      'handle_type_selection',    domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputCurveTilt',                'tilt',                     domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputRadius',                   'radius',                   domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputCurveHandlePositions',     'handle_positions',         domains=['CURVE']  )
        
        self.add_call('STACK', 'GeometryNodeCurveSetHandles',          'set_handles'              )
        self.add_call('STACK', 'GeometryNodeCurveSplineType',          'set_spline_type'          )
        self.add_call('STACK', 'GeometryNodeFillCurve',                'fill'                     )
        self.add_call('STACK', 'GeometryNodeFilletCurve',              'fillet'                   )
        self.add_call('STACK', 'GeometryNodeResampleCurve',            'resample'                 )
        self.add_call('STACK', 'GeometryNodeReverseCurve',             'reverse'                  )
        self.add_call('STACK', 'GeometryNodeSetCurveHandlePositions',  'set_handle_positions'     )
        self.add_call('STACK', 'GeometryNodeSetCurveRadius',           'set_radius'               )
        self.add_call('STACK', 'GeometryNodeSetCurveTilt',             'set_tilt'                 )
        self.add_call('STACK', 'GeometryNodeSubdivideCurve',           'subdivide'                )
        self.add_call('STACK', 'GeometryNodeTrimCurve',                'trim'                     )
        
        self.add_call('METHOD', 'GeometryNodeCurveToMesh',             'to_mesh',     ret_class='Mesh')
        self.add_call('METHOD', 'GeometryNodeCurveToPoints',           'to_points',   ret_class='Points')
        self.add_call('METHOD', 'GeometryNodeSampleCurve',             'sample',      ret_class='NODE')
        self.add_call('METHOD', 'GeometryNodeCurveLength',             'length',      ret_class='Float')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Texture

class TextureGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Texture', 'bcls.Texture')
        
        self.add_call('STATIC', 'ShaderNodeTexBrick'          ,'Brick'     )
        self.add_call('STATIC', 'ShaderNodeTexChecker'        ,'Checker'   )
        self.add_call('STATIC', 'ShaderNodeTexGradient'       ,'Gradient'  )
        self.add_call('STATIC', 'ShaderNodeTexMagic'          ,'Magic'     )
        self.add_call('STATIC', 'ShaderNodeTexMusgrave'       ,'Musgrave'  )
        self.add_call('STATIC', 'ShaderNodeTexNoise'          ,'Noise'     )
        self.add_call('STATIC', 'ShaderNodeTexVoronoi'        ,'Voronoi'   )
        self.add_call('STATIC', 'ShaderNodeTexWave'           ,'Wave'      )
        self.add_call('STATIC', 'ShaderNodeTexWhiteNoise'     ,'WhiteNoise')
        self.add_call('STATIC', 'GeometryNodeImageTexture'    ,'Image'     )
        
        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Texture',     input_type='TEXTURE' )

# -----------------------------------------------------------------------------------------------------------------------------
# Material
        
class MaterialGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Material', 'bcls.Material')

        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Material', input_type='MATERIAL')
        self.add_call('METHOD', 'GeometryNodeMaterialSelection', 'selection', ret_class='Boolean')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Image 
        
class ImageGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Image', 'bcls.Image')
        
        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Image',    input_type='IMAGE'  )
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Collection
        
class CollectionGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Collection', 'bcls.Collection')

        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Collection',  input_type='COLLECTION')

        self.add_call('METHOD', 'GeometryNodeCollectionInfo', 'info')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Object
        
class ObjectGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Object', 'bcls.Object')

        self.add_call('METHOD', 'GeometryNodeSwitch', 'switch', self_name='false', ret_class='Object',      input_type='OBJECT' )

        self.add_call('PROPERTY', 'GeometryNodeObjectInfo', 'info')


# =============================================================================================================================
# The classes generators
        

DATA_CLASSES = [GlobalGen, BooleanGen, IntegerGen, FloatGen, VectorGen, ColorGen, StringGen,
                GeometryGen, SplineGen, CurveGen, MeshGen, PointsGen, InstancesGen, VolumeGen,
                CollectionGen, ObjectGen, TextureGen, MaterialGen, ImageGen]


#DATA_CLASSES = [MeshGen]

     

