#!/usr/bin/env python3
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
# Parameters to call a Node

class NodeCall:
    
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


# ========================================================================================================================
# The data class generator                
        
class DataClass:
    
    FAMILIES = {
        'CONSTRUCTOR' : 'Constructors',
        'STATIC'      : 'Static methods',
        'CLASS'       : 'Class methods',
        'PROPERTY'    : 'Properties',   
        'NODE_PROP'   : 'Node properties',
        'ATTRIBUTE'   : 'Attributes',
        'METHOD'      : 'Methods',        
        'STACK'       : 'Stacked methods',
        }
    
    def __init__(self, class_name, super_class):
        
        self.class_name  = class_name
        self.super_class = super_class
        
        self.methods_     = []
        
        # Add the methods coming for parameter variations
        
        for blid, vs in VARIATIONS.items():
            self.methods_.extend(vs.methods(blid, self.class_name))
            
    # ----------------------------------------------------------------------------------------------------
    # Methods per family
    
    def methods(self, family=None):
        meths = []
        for meth in self.methods_:
            if family is None or family == meth.family:
                meths.append(meth)
        return meths
    
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

    def add_attribute(self, bl_idname, meth_name, domains=None, prop_names=None):
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
        
    def gen_comments(self, nodes):
        
        yield _1_ + '"""' + f" Socket data class {self.class_name}\n\n"
        
        for family, label in self.FAMILIES.items():
            meths = self.methods(family)
            if meths:
                meths.sort(key=lambda nc: nc.meth_name)
                yield _1_ + f"{label}\n"
                yield _1_ + "-" * len(label) + "\n"
                for nc in meths:
                    yield _2_ + f"{nc.comment(self.class_name, nodes[nc.bl_idname])}\n"
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
        
    def gen_class(self, nodes):

        # ---------------------------------------------------------------------------
        # Header
        
        yield  "\n# " + '='*110 + "\n"
        yield f"# Data class {self.class_name}\n\n"
        
        yield _0_ + f"class {self.class_name}({self.super_class}):\n"
        
        # ---------------------------------------------------------------------------
        # Documentation
            
        for line in self.gen_comments(nodes):
            yield line
            
        # ---------------------------------------------------------------------------
        # Methods
        
        for family, label in self.FAMILIES.items():
            
            meths = self.methods(family)
            if not meths:
                continue
            
            yield f"\n{_1_}# {'-'*100}\n{_1_}# {label}\n\n"
            
            for nc in meths:
                
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
                
                yield _2_ + '""" ' + f"Method {nc.meth_name}\n\n"
                yield _2_ + "Arguments\n"
                yield _2_ + "---------\n"
                
                for arg in args:
                    yield _3_ + arg.comment
                    
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
    
    def __init__(self):
        super().__init__('GLOBAL', '')
        
        self.add_method('FunctionNodeCompare',          meth_name="compare"             )
        self.add_method('GeometryNodeStringJoin',       meth_name="join_strings"        )
        self.add_method('GeometryNodeAccumulateField',  meth_name="accumulate_field"    )
        self.add_method('GeometryNodeFieldAtIndex',     meth_name="field_at_index"      )
        self.add_method('GeometryNodeCollectionInfo',   meth_name="collection_info", arg_hooks={'collection': 'Collection.blender_collection'})
        self.add_method('GeometryNodeObjectInfo',       meth_name="object_info",     arg_hooks={'object':     'Object.blender_object'})
        
        self.add_method('GeometryNodeInputSceneTime', 'scene')
        

        
    def gen_class(self, nodes):
        
        # ---------------------------------------------------------------------------
        # Header
        
        yield  "\n# " + '='*110 + "\n"
        yield f"# Global functions\n\n"
        
        # ---------------------------------------------------------------------------
        # Loop on functions
        
        meths = self.methods('METHOD')
        
        for nc in meths:
            
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
    def __init__(self):
        super().__init__('Boolean', 'bcls.Boolean')
        
        self.add_method('GeometryNodeFieldAtIndex', meth_name="field_at_index", self_name='value', variation={'data_type': 'BOOLEAN'}, ret_class='Boolean')
        
            
        
# -----------------------------------------------------------------------------------------------------------------------------
# Integer
        
class IntegerGen(DataClass):
    def __init__(self):
        super().__init__('Integer', 'bcls.Integer')

        self.add_method('GeometryNodeAccumulateField',  meth_name="accumulate_field", variation={'data_type': 'INT'})
        self.add_method('GeometryNodeFieldAtIndex',     meth_name="field_at_index",   variation={'data_type': 'INT'}, self_name='value', ret_class='Integer')
        

# -----------------------------------------------------------------------------------------------------------------------------
# Float

class FloatGen(DataClass):
    def __init__(self):
        super().__init__('Float', 'bcls.Float')
        
        self.add_method('FunctionNodeFloatToInt',     'to_integer',   ret_class='Integer')
        self.add_method('FunctionNodeValueToString',  'to_string',    ret_class='String' )

        self.add_method('GeometryNodeAccumulateField',  meth_name="accumulate_field", variation={'data_type': 'FLOAT'})
        self.add_method('GeometryNodeFieldAtIndex',     meth_name="field_at_index",   variation={'data_type': 'FLOAT'}, self_name='value', ret_class='Float')
        

        self.add_method('ShaderNodeFloatCurve',       'curve',        stack=True         )
        self.add_method('ShaderNodeValToRGB',         'color_ramp',                      )
        self.add_method('ShaderNodeClamp',            'clamp',        stack=True         )
        self.add_method('ShaderNodeMapRange',         'map_range',    stack=True, variation={'data_type': 'FLOAT'})
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Vector
        
class VectorGen(DataClass):
    def __init__(self):
        super().__init__('Vector', 'bcls.Vector')
        
        self.add_constructor('ShaderNodeCombineXYZ', 'Combine')
        self.add_constructor('FunctionNodeAlignEulerToVector',  'AlignToVector')
        
        self.add_node_prop('ShaderNodeSeparateXYZ',     'separate')
        self.add_method('ShaderNodeVectorCurve',        'curves',    stack=True)
        
        self.add_method('ShaderNodeVectorRotate',       'rotate',    ret_class='Vector')
        self.add_method('GeometryNodeAccumulateField',  meth_name="accumulate_field", variation={'data_type': 'FLOAT_VECTOR'})
        self.add_method('GeometryNodeFieldAtIndex',     meth_name="field_at_index",   variation={'data_type': 'FLOAT_VECTOR'}, self_name='value', ret_class='Vector')

        # ----- Rotation

        self.add_method('FunctionNodeAlignEulerToVector',  'align_to_vector',    stack=True)
        self.add_method('FunctionNodeRotateEuler',         'rotate_euler',       stack=True)
        
        self.add_method('ShaderNodeMapRange',              'map_range',          stack=True, variation={'data_type': 'FLOAT_VECTOR'})
        
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# String

class ColorGen(DataClass):
    def __init__(self):
        super().__init__('Color', 'bcls.Color')
        
        self.add_constructor('ShaderNodeCombineRGB', 'Combine')        
        
        self.add_node_prop('ShaderNodeSeparateRGB',     'separate')

        self.add_method('ShaderNodeRGBCurve',           'curves',    stack=True)

        self.add_method('ShaderNodeMixRGB',             'mix')
        
        self.add_method('GeometryNodeFieldAtIndex',     meth_name="field_at_index",   variation={'data_type': 'FLOAT_COLOR'}, self_name='value', ret_class='Color')
        
        

# -----------------------------------------------------------------------------------------------------------------------------
# String

class StringGen(DataClass):
    def __init__(self):
        super().__init__('String', 'bcls.String')
        
        self.add_method('FunctionNodeReplaceString',     'replace',       stack=True)
        self.add_method('FunctionNodeSliceString',       'slice',         stack=True)
        
        self.add_property('FunctionNodeStringLength', 'length',    ret_class ='Integer')
        self.add_method('GeometryNodeStringToCurves', 'to_curves', ret_class = 'Curve')
        
        self.add_method('GeometryNodeStringJoin', meth_name="join", self_name="strings")
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Geometry
        
class GeometryGen(DataClass):
    def __init__(self):
        super().__init__('Geometry', 'bcls.Geometry')
        
        

        self.add_attribute('GeometryNodeInputNormal',       'normal',           domains=None  )
        self.add_attribute('GeometryNodeInputTangent',      'tangent',          domains=None  )
        
        # ----- ID and Index
        
        self.add_attribute('GeometryNodeInputID',           'ID',               domains=['POINT'])
        self.add_attribute('GeometryNodeInputIndex',        'index',            domains=['POINT']  )
        
        self.add_attribute('GeometryNodeInputPosition',     'position',         domains=['POINT'])

        self.add_attribute('GeometryNodeIsViewport',        'is_viewport',      domains=['POINT']  )
        
        
        self.add_node_prop('GeometryNodeBoundBox',           'bound_box',        prop_names=('box', 'box_min', 'box_max'))
        self.add_node_prop('GeometryNodeSeparateComponents', 'components',       
                          prop_names=('mesh_component', 'points_component', 'curve_component', 'volume_component', 'instances_component'))
        
        #self.add_method('GeometryNodeAttributeTransfer',    'transfer_attribute')
        self.add_method('GeometryNodeAttributeTransfer',    'transfer_boolean', variation={'data_type': 'BOOLEAN'}      )
        self.add_method('GeometryNodeAttributeTransfer',    'transfer_integer', variation={'data_type': 'INT'}          )
        self.add_method('GeometryNodeAttributeTransfer',    'transfer_float',   variation={'data_type': 'FLOAT'}        )
        self.add_method('GeometryNodeAttributeTransfer',    'transfer_vector',  variation={'data_type': 'FLOAT_VECTOR'} )
        self.add_method('GeometryNodeAttributeTransfer',    'transfer_color',   variation={'data_type': 'FLOAT_COLOR'}  )

        self.add_method('GeometryNodeDeleteGeometry',       'delete_geometry',         stack=True)
        self.add_method('GeometryNodeMergeByDistance',      'merge_by_distance',       stack=True)
        self.add_method('GeometryNodeRealizeInstances',     'realize_instances',       stack=True)
        self.add_method('GeometryNodeReplaceMaterial',      'replace_material',        stack=True)
        self.add_method('GeometryNodeScaleElements',        'scale_elements',          stack=True)
        self.add_method('GeometryNodeSetID',                'set_ID',                  stack=True)
        self.add_method('GeometryNodeSetMaterial',          'set_material',            stack=True)
        self.add_method('GeometryNodeSetMaterialIndex',     'set_material_index',      stack=True)
        self.add_method('GeometryNodeSetPosition',          'set_position',            stack=True)
        self.add_method('GeometryNodeSetShadeSmooth',       'set_shade_smooth',        stack=True)
        self.add_method('GeometryNodeTransform',            'transform',               stack=True)
        
        self.add_method('GeometryNodeAttributeDomainSize',  'attribute_domain_size',    ret_class='Integer')
        self.add_method('GeometryNodeAttributeRemove',      'attribute_remove',         ret_class= None)
        self.add_method('GeometryNodeAttributeStatistic',   'attribute_statistic',      ret_class='Float')
        self.add_method('GeometryNodeSeparateGeometry',     'components',               ret_class= None)
        self.add_method('GeometryNodeCaptureAttribute',     'capture_attribute',        ret_class= None)
        self.add_method('GeometryNodeConvexHull',           'convex_hull',              ret_class='Mesh')
        self.add_method('GeometryNodeGeometryToInstance',   'to_instance',              ret_class='Instances')
        self.add_method('GeometryNodeJoinGeometry',         'join',                     ret_class='Geometry')

        self.add_method('GeometryNodeProximity',            'proximity')
        self.add_method('GeometryNodeRaycast',              'raycast')
        
        
        
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Mesh  
        
class MeshGen(DataClass):
    def __init__(self):
        super().__init__('Mesh', 'Geometry')
        
        self.add_constructor('GeometryNodeMeshCircle'        ,'Circle'     )
        self.add_constructor('GeometryNodeMeshCone'          ,'Cone'       )
        self.add_constructor('GeometryNodeMeshCube'          ,'Cube'       )
        self.add_constructor('GeometryNodeMeshCylinder'      ,'Cylinder'   )
        self.add_constructor('GeometryNodeMeshGrid'          ,'Grid'       )
        self.add_constructor('GeometryNodeMeshIcoSphere'     ,'IcoSphere'  )
        self.add_constructor('GeometryNodeMeshLine'          ,'Line'       )
        self.add_constructor('GeometryNodeMeshUVSphere'      ,'UVSphere'   )
        
        self.add_attribute('GeometryNodeInputID',           'ID',               domains={'FACE', 'EDGE', 'CORNER'})
        self.add_attribute('GeometryNodeInputIndex',        'index',            domains={'FACE', 'EDGE', 'CORNER'})
        
        self.add_attribute('GeometryNodeInputMeshEdgeNeighbors',   'edge_neighbors',   domains=['EDGE']  )
        self.add_attribute('GeometryNodeInputMeshFaceArea',        'face_area',        domains=['FACE']  )
        self.add_attribute('GeometryNodeInputMeshEdgeAngle',       'edge_angle',       domains=['EDGE']  )
        self.add_attribute('GeometryNodeInputMeshEdgeVertices',    'edge_vertices',    domains=['EDGE']  )
        self.add_attribute('GeometryNodeInputMeshFaceNeighbors',   'face_neighbors',   domains=['FACE']  )
        self.add_attribute('GeometryNodeInputMeshIsland',          'island',           domains=['FACE']  )
        self.add_attribute('GeometryNodeInputMeshVertexNeighbors', 'vertex_neighbors', domains=['POINT'] )
        
        self.add_attribute('GeometryNodeInputMaterialIndex',       'material_index',   domains=['FACE'] )
        self.add_attribute('GeometryNodeInputShadeSmooth',         'shade_smooth',     domains=['FACE'] )
        
        
        self.add_method('GeometryNodeSplitEdges',         'split_edges',         stack=True)
        self.add_method('GeometryNodeSubdivideMesh',      'subdivide',           stack=True)
        self.add_method('GeometryNodeSubdivisionSurface', 'subdivision_surface', stack=True)
        self.add_method('GeometryNodeTriangulate',        'triangulate',         stack=True)
        self.add_method('GeometryNodeDualMesh',           'dual',                stack=True)
        self.add_method('GeometryNodeExtrudeMesh',        'extrude',                       )
        self.add_method('GeometryNodeFlipFaces',          'flip_faces',          stack=True)
        
        self.add_method('GeometryNodeMeshToCurve',              'to_curve',                     ret_class='Curve')
        self.add_method('GeometryNodeMeshToPoints',             'to_points',                    ret_class='Points')
        self.add_method('GeometryNodeDistributePointsOnFaces',  'distribute_points_on_faces',   ret_class='Points')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Points
        
class PointsGen(DataClass):
    def __init__(self):
        super().__init__('Points', 'Mesh')
        
        self.add_method('GeometryNodeSetPointRadius',    'set_radius', stack=True)
        
        self.add_method('GeometryNodeInstanceOnPoints',  'instance_on_points', ret_class='Instances')
        self.add_method('GeometryNodePointsToVertices',  'to_vertices',        ret_class='Mesh'     )
        self.add_method('GeometryNodePointsToVolume',    'to_volume',          ret_class='Volume'   )

# -----------------------------------------------------------------------------------------------------------------------------
# Instances
        
class InstancesGen(DataClass):
    def __init__(self):
        super().__init__('Instances', 'Mesh')
        
        self.add_attribute('GeometryNodeInputIndex',      'index',     domains=['INSTANCE']  )
        
        self.add_method('GeometryNodeRotateInstances',    'rotate',    stack=True)
        self.add_method('GeometryNodeScaleInstances',     'scale',     stack=True)
        self.add_method('GeometryNodeTranslateInstances', 'translate', stack=True)
        
        self.add_method('GeometryNodeInstancesToPoints',  'to_points', ret_class='Points')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Volume
        
class VolumeGen(DataClass):
    def __init__(self):
        super().__init__('Volume', 'Mesh')
        
        self.add_method('GeometryNodeVolumeToMesh', 'to_mesh' , ret_class='Mesh')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Spline

class SplineGen(DataClass):
    def __init__(self):
        super().__init__('Spline', 'Geometry')
        
        self.add_attribute('GeometryNodeInputSplineCyclic',         'cyclic',       domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputSplineResolution',     'resolution',   domains=['CURVE']  )
        self.add_attribute('GeometryNodeSplineLength',              'length',       domains=['CURVE']  , prop_names = ['length', 'point_count'])
        self.add_attribute('GeometryNodeSplineParameter',           'parameter',    domains=['CURVE']  )
        
        self.add_method('GeometryNodeSetSplineCyclic',              'set_cyclic',     stack=True)
        self.add_method('GeometryNodeSetSplineResolution',          'set_resolution', stack=True)

# -----------------------------------------------------------------------------------------------------------------------------
# Curve 
        
class CurveGen(DataClass):
    def __init__(self):
        super().__init__('Curve', 'Spline')
        
        self.add_constructor('GeometryNodeCurvePrimitiveBezierSegment', 'BezierSegment'     )
        self.add_constructor('GeometryNodeCurvePrimitiveCircle',        'Circle'            )
        self.add_constructor('GeometryNodeCurvePrimitiveLine',          'Line'              )
        self.add_constructor('GeometryNodeCurvePrimitiveQuadrilateral', 'Quadrilateral'     )
        self.add_constructor('GeometryNodeCurveQuadraticBezier',        'QuadraticBezier'   )
        self.add_constructor('GeometryNodeCurveStar',                   'Star'              )
        self.add_constructor('GeometryNodeCurveSpiral',                 'Spiral'            )
        
        # Depending upon the way it is initialized, the node GeometryNodeCurveArc has
        # only one output socket or several

        self.add_constructor('GeometryNodeCurveArc',                    'ArcFromRadius', variation={'mode':'RADIUS'})
        self.add_static(     'GeometryNodeCurveArc',                    'ArcFromPoints', variation={'mode':'POINTS'})
        
        
        self.add_attribute('GeometryNodeInputID',           'ID',               domains={'SPLINE'})
        self.add_attribute('GeometryNodeInputIndex',        'index',            domains={'SPLINE'})
        
        
        self.add_attribute('GeometryNodeCurveEndpointSelection',        'endpoint_selection',       domains=['CURVE']  )
        self.add_attribute('GeometryNodeCurveHandleTypeSelection',      'handle_type_selection',    domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputCurveTilt',                'tilt',                     domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputRadius',                   'radius',                   domains=['CURVE']  )
        self.add_attribute('GeometryNodeInputCurveHandlePositions',     'handle_positions',         domains=['CURVE']  )
        
        self.add_method('GeometryNodeCurveSetHandles',          'set_handles',              stack=True)
        self.add_method('GeometryNodeCurveSplineType',          'set_spline_type',          stack=True)
        self.add_method('GeometryNodeFillCurve',                'fill',                     stack=True)
        self.add_method('GeometryNodeFilletCurve',              'fillet',                   stack=True)
        self.add_method('GeometryNodeResampleCurve',            'resample',                 stack=True)
        self.add_method('GeometryNodeReverseCurve',             'reverse',                  stack=True)
        self.add_method('GeometryNodeSetCurveHandlePositions',  'set_handle_positions',     stack=True)
        self.add_method('GeometryNodeSetCurveRadius',           'set_radius',               stack=True)
        self.add_method('GeometryNodeSetCurveTilt',             'set_tilt',                 stack=True)
        self.add_method('GeometryNodeSubdivideCurve',           'subdivide',                stack=True)
        self.add_method('GeometryNodeTrimCurve',                'trim',                     stack=True)
        
        self.add_method('GeometryNodeCurveToMesh',              'to_mesh',     ret_class='Mesh')
        self.add_method('GeometryNodeCurveToPoints',            'to_points',   ret_class='Points')
        self.add_method('GeometryNodeSampleCurve',              'sample',      ret_class='NODE')
        self.add_method('GeometryNodeCurveLength',              'length',      ret_class='Float')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Texture

class TextureGen(DataClass):
    def __init__(self):
        super().__init__('Texture', 'bcls.Texture')
        
        self.add_constructor('ShaderNodeTexBrick'          ,'Brick'     )
        self.add_constructor('ShaderNodeTexChecker'        ,'Checker'   )
        self.add_constructor('ShaderNodeTexGradient'       ,'Gradient'  )
        self.add_constructor('ShaderNodeTexMagic'          ,'Magic'     )
        self.add_constructor('ShaderNodeTexMusgrave'       ,'Musgrave'  )
        self.add_constructor('ShaderNodeTexNoise'          ,'Noise'     )
        self.add_constructor('ShaderNodeTexVoronoi'        ,'Voronoi'   )
        self.add_constructor('ShaderNodeTexWave'           ,'Wave'      )
        self.add_constructor('ShaderNodeTexWhiteNoise'     ,'WhiteNoise')
        self.add_constructor('GeometryNodeImageTexture'    ,'Image'     )
        

# -----------------------------------------------------------------------------------------------------------------------------
# Material
        
class MaterialGen(DataClass):
    def __init__(self):
        super().__init__('Material', 'bcls.Material')
        
        self.add_method('GeometryNodeMaterialSelection', 'selection', ret_class='Boolean')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Image 
        
class ImageGen(DataClass):
    def __init__(self):
        super().__init__('Image', 'bcls.Image')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Collection
        
class CollectionGen(DataClass):
    def __init__(self):
        super().__init__('Collection', 'bcls.Collection')
        
        self.add_method('GeometryNodeCollectionInfo', 'info')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Object
        
class ObjectGen(DataClass):
    def __init__(self):
        super().__init__('Object', 'bcls.Object')

        self.add_node_prop('GeometryNodeObjectInfo', 'info')


# =============================================================================================================================
# The classes generators
        

DATA_CLASSES = [GlobalGen, BooleanGen, IntegerGen, FloatGen, VectorGen, ColorGen, StringGen,
                GeometryGen, SplineGen, CurveGen, MeshGen, PointsGen, InstancesGen, VolumeGen,
                CollectionGen, ObjectGen, TextureGen, MaterialGen, ImageGen]


     




















"""

# =============================================================================================================================
# Class implementation

class Impl:
    
    def __init__(self, implementation, class_name, name, **kwargs):
        
        self.implementation = implementation
        self.class_name     = class_name
        self.name           = name
        for k, v in kwargs.items():
            setattr(self, k, v)
        
        self.user_name = self.Implementation
        if self.implementation == 'Node':
            self.user_name = 'Node'
            
        if self.implementation == 'NodeProps':
            self.user_name = 'Node output sockets implemented as data properties'
        
    @classmethod
    def Function(cls, name, variations=[]):
        return cls('Function', None, name, variations=variations)
    
    @classmethod
    def Constructor(cls, class_name, name, out_name=None, variation={}):
        return cls('Constructor', class_name, name, out_name=out_name, variation=variation)
    
    @classmethod
    def Static(cls, class_name, name, out_name=None, out_class=None):
        return cls('Static', class_name, name, out_name=out_name, out_class=out_class)
    
    @classmethod
    def Stack(cls, class_name, name, in_name=None):
        return cls('Stack', class_name, name, in_name=in_name)
    
    @classmethod
    def Node(cls, class_name, name, in_name=None):
        return cls('Node', class_name, name, in_name=in_name)
    
    @classmethod
    def NodeProps(cls, class_name, name, in_name=None, prop_names=None):
        return cls('NodeProps', class_name, name, in_name=in_name, prop_names=prop_names)
    
    @classmethod
    def Method(cls, class_name, name, in_name=None, out_name=None, out_class=None):
        return cls('Method', class_name, name, in_name=in_name, out_name=out_name, out_class=out_class)
    
    @classmethod
    def Property(cls, class_name, name, in_name=None, out_name=None, out_class=None):
        return cls('Property', class_name, name, in_name=in_name, out_name=out_name, out_class=out_class)
    
    @classmethod
    def Attribute(cls, class_name, name, domains=None):
        return cls('Property', class_name, name, domains=domains)

        

NODES_IMPLEMENTATION = {
    
    # ----- Special nodes which are not implemented through functions or methods
    
    'NodeGroupInput'                          : None,
    'NodeGroupOutput'                         : None,
    'NodeFrame'                               : None,
    'NodeReroute'                             : None,
    'GeometryNodeInputSceneTime'              : None,
    'GeometryNodeViewer'                      : None,
    
    # ----- Data creation are manually implemented with Input
    
    'FunctionNodeInputBool'                   : None,
    'FunctionNodeInputInt'                    : None,
    'ShaderNodeValue'                         : None,
    'FunctionNodeInputVector'                 : None,
    'FunctionNodeInputColor'                  : None,
    'FunctionNodeInputString'                 : None,
    'FunctionNodeInputSpecialCharacters'      : None,
    'GeometryNodeCollectionInfo'              : None,
    'GeometryNodeInputMaterial'               : None,

    # -----------------------------------------------------------------------------------------------------------------------------
    # ------------------------- Objects
    
    'GeometryNodeObjectInfo'                  : Impl.Property('Object', "info"),
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # ------------------------- Functions
    
    'ShaderNodeMixRGB'                        : Impl.Function('mixRGB'                 out_name = 'Color'     ),
    'FunctionNodeBooleanMath'                 : Impl.Function('boolean_math',          out_name = 'Boolean'   ),
    'FunctionNodeCompare'                     : Impl.Function('compare'                out_name = None        ),
    'FunctionNodeRandomValue'                 : Impl.Function('random_value'           out_name = 'Value'     ),
    'FunctionNodeRotateEuler'                 : Impl.Function('rotate_euler'           out_name = 'Vector'    ),
    'GeometryNodeAttributeTransfer'           : Impl.Function('attribute_transfer'     out_name = 'NODE'      ),
    'GeometryNodeMeshBoolean'                 : Impl.Function('mesh_boolean'           out_name = 'Mesh'      ),
    'GeometryNodeCurveArc'                    : Impl.Function('curve_arc'              out_name = 'Curve'     ),
    'GeometryNodeProximity'                   : Impl.Function('proximity'              out_name = 'Float'     ),
    'ShaderNodeVectorMath'                    : Impl.Function('vector_math'            out_name = None        ),
    'GeometryNodeRaycast'                     : Impl.Function('raycast'                out_name = None        ),
    'GeometryNodeStringJoin'                  : Impl.Function('join_strings'           out_name = 'String'    ),
    'GeometryNodeSwitch'                      : Impl.Function('switch'                 out_name = 'Geometry'  ),
    'ShaderNodeClamp'                         : Impl.Function('clamp'                  out_name = 'Float'     ),
    'ShaderNodeCombineRGB'                    : Impl.Function('combine_rgb'            out_name = 'Color'     ),
    'ShaderNodeCombineXYZ'                    : Impl.Function('combine_xyz'            out_name = 'Vector'    ),
    'ShaderNodeMapRange'                      : Impl.Function('map_range'              out_name = None        ),
    'ShaderNodeMath'                          : Impl.Function('math'                   out_name = 'Float'     ),
    'ShaderNodeValToRGB'                      : Impl.Function('color_ramp'             out_name = 'Color'     ),
    'GeometryNodeAccumulateField'             : Impl.Function('accumulate_field'       out_name = None        ),
    'GeometryNodeFieldAtIndex'                : Impl.Function('field_at_index'         out_name = None        ),

    # -----------------------------------------------------------------------------------------------------------------------------
    # ------------------------- Multy types

    # ----- Random value
    
    'FunctionNodeRandomValue'                 :(Impl.Constructor('Boolean',    'Random', variation={'data_type': 'INT'}         ),
                                                Impl.Constructor('Integer',    'Random', variation={'data_type': 'BOOLEAN'}     ),
                                                Impl.Constructor('Float',      'Random', variation={'data_type': 'FLOAT'}       ),
                                                Impl.Constructor('Vector',     'Random', variation={'data_type': 'FLOAT_VECTOR'}),
                                                ),

    # ----- Switch

    'GeometryNodeSwitch'                      :(Impl.Constructor('Boolean',    'switch', variation={'data_type': 'BOOLEAN'}     ),
                                                Impl.Constructor('Integer',    'switch', variation={'data_type': 'INT'}         ),
                                                Impl.Constructor('Float',      'switch', variation={'data_type': 'FLOAT'}       ),
                                                Impl.Constructor('Vector',     'switch', variation={'data_type': 'VECTOR'}      ),
                                                Impl.Constructor('String',     'switch', variation={'data_type': 'STRING'}      ),
                                                Impl.Constructor('Color',      'switch', variation={'data_type': 'RGBA'}        ),
                                                Impl.Constructor('Object',     'switch', variation={'data_type': 'OBJECT'}      ),
                                                Impl.Constructor('Image',      'switch', variation={'data_type': 'IMAGE'}       ),
                                                Impl.Constructor('Geometry',   'switch', variation={'data_type': 'GEOMETRY'}    ),
                                                Impl.Constructor('Collection', 'switch', variation={'data_type': 'COLLECTION'}  ),
                                                Impl.Constructor('Texture',    'switch', variation={'data_type': 'TEXTURE'}     ),
                                                Impl.Constructor('Material',   'switch', variation={'data_type': 'MATERIAL'}    ),
                                                ),
    
}

"""
