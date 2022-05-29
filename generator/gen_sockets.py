{}#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:49:27 2022

@author: alain
"""

def indent_set(depth=0):
    _indent_ = "    "
    _0_ = "\n" + _indent_ * max(0, 0 + depth)
    _1_ = "\n" + _indent_ * max(0, 1 + depth)
    _2_ = "\n" + _indent_ * max(0, 2 + depth)
    _3_ = "\n" + _indent_ * max(0, 3 + depth)
    _4_ = "\n" + _indent_ * max(0, 4 + depth)
    
    return _indent_, _0_, _1_, _2_, _3_, _4_

_indent_, _0_, _1_, _2_, _3_, _4_ = indent_set(0)


FAMILIES = {
    'CONSTRUCTOR' : ('Constructor',      'Constructors'          , False),
    'STATIC'      : ('Static method',    'Static methods'        , False),
    'CLASS'       : ('Class method',     'Class methods'         , False),    
    'PROPERTY'    : ('Property',         'Properties'            , True ),
    'CAPT_ATTR'   : ('Capture attribute','Attribute captures'    , True ),
    'ATTRIBUTE'   : ('Attribute',        'Attributes'            , True ),
    'METHOD'      : ('Method',           'Methods'               , True ),        
    'STACK'       : ('Stacked method',   'Stacked methods'       , True ),
    
    'FUNCTION'    : ('Function',         'Functions'             , False),
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

COLOR_MIX = {
    'MIX'           : 'mix',
    'DARKEN'        : 'darken',
    'MULTIPLY'      : 'multiply',
    'BURN'          : 'burn',
    'LIGHTEN'       : 'lighten',
    'SCREEN'        : 'screen',
    'DODGE'         : 'dodge',
    'ADD'           : 'add',
    'OVERLAY'       : 'overlay',
    'SOFT_LIGHT'    : 'soft_light',
    'LINEAR_LIGHT'  : 'linear_light',
    'DIFFERENCE'    : 'difference',
    'SUBTRACT'      : 'subtract',
    'DIVIDE'        : 'divide',
    'HUE'           : 'hue',
    'SATURATION'    : 'saturation',
    'COLOR'         : 'mix_color',
    'VALUE'         : 'value',
}

MULTI_CLASSES_NODES = { # Function name and is an attribute. If it is an attribute, use the geometry as geometry socket
    'FunctionNodeRandomValue'        : ('Random',              False ), # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
    'GeometryNodeAccumulateField'    : ('accumulate_field',    False ), # ('FLOAT', 'INT', 'FLOAT_VECTOR')
    'GeometryNodeAttributeStatistic' : ('attribute_statistic', True  ), # ('FLOAT', 'FLOAT_VECTOR')
    'GeometryNodeAttributeTransfer'  : ('transfer_attribute',  True  ), # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
    'GeometryNodeCaptureAttribute'   : ('capture_attribute',   True  ), # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
    'GeometryNodeFieldAtIndex'       : ('field_at_index',      False ), # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
    'GeometryNodeRaycast'            : ('raycast',             True  ), # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
    'GeometryNodeSwitch'             : ('switch',              False ), # ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
    'ShaderNodeMapRange'             : ('map_range',           False ), # ('FLOAT', 'FLOAT_VECTOR')
    
#   'FunctionNodeCompare'            : ('compare',             False ), # ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
#   'GeometryNodeViewer'             : ('viewer',              False ), # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
    
}

DATA_TYPES = {
    'Integer'     : 'INT',
    'Color'       : 'RGBA',
    'Vector'      : 'FLOAT_VECTOR',
    'Color'       : 'FLOAT_COLOR',
}

# =============================================================================================================================
# Node calling

class NodeCall:
    
    def __init__(self, family, wnode, class_name, meth_name, self_name=None, out_name=None, ret_class=None, args_hooks={}, **fixed):
        
        self.family     = family

        self.wnode      = wnode
        self.class_name = class_name
        self.meth_name  = meth_name
        
        self.self_name  = self_name
        self.out_name   = out_name
        self.ret_class  = ret_class
        self.hooks      = args_hooks

        self.fixed      = dict(fixed)
        
        self.properties = None
        self.attribute  = {}

    # ----------------------------------------------------------------------------------------------------
    # A property
    
    @classmethod
    def Property(cls, wnode, class_name, meth_name, settable=False, prop_names=None, **fixed):
        nc = cls('PROPERTY', wnode, class_name, meth_name, **fixed)
        nc.properties = {
            'settable' : settable,
            'names'    : prop_names,
            }
        return nc

    # ----------------------------------------------------------------------------------------------------
    # An attribute
    
    @classmethod
    def Attribute(cls, wnode, class_name, meth_name, capture_meth=None, domain='POINT', output_index=0):
        
        capture = capture_meth is None

        nc = cls('CAPT_ATTR' if capture else 'ATTRIBUTE', wnode, class_name, meth_name)

        nc.attribute = {
            'capture'      : capture,
            'capture_meth' : capture_meth,
            'domain'       : domain,
            'output_index' : output_index,
            }
        
        return nc

    # ----------------------------------------------------------------------------------------------------
    # The call is a method using self
    
    @property
    def use_self(self):
        return FAMILIES[self.family][2]
    
    # ----------------------------------------------------------------------------------------------------
    # Class comment: line generated at class level
    
    @property
    def class_comment(self):
        
        unames = self.wnode.output_unames(self.fixed)
        
        if self.family == 'STACK':
            ret_str = self.class_name
            
        elif self.family == 'ATTRIBUTE':
            
            index = self.attribute['output_index']
            
            ret_str = f"{unames[list(unames)[index]]:9s} = {self.attribute['capture_meth']}(domain='{self.attribute['domain']}')"
            if len(unames) > 1:
                ret_str += f".{list(unames)[index]}"
            
        elif len(unames) == 0:
            ret_str = "None"
            
        elif len(unames) == 1:
            uname = list(unames)[0]
            ret_str = f"{uname:12s} ({unames[uname]})"
            
        else:
            ret_str = "Sockets      ["
            sep = ""
            for uname, class_name in unames.items():
                ret_str += f"{sep}{uname} ({class_name})"
                sep = ", "
            ret_str += "]"
        
        return f"{self.meth_name:25s} : {ret_str}"
    

# ========================================================================================================================
# The data class generator                
        
class DataClass:
    
    def __init__(self, wnodes, class_name, super_class):
        
        self.wnodes      = wnodes
        self.class_name  = class_name
        self.super_class = super_class
        
        self.methods_    = []
        
        self.is_global   = False
        
        # ----------------------------------------------------------------------------------------------------
        # Add the multi classes methods
        
        for blid, spec in MULTI_CLASSES_NODES.items():
            wn = self.wnodes[blid]
            if not self.data_type in wn.parameters[wn.driving_param].values:
                continue
            
            meth_name = spec[0]
            
            fixed = {wn.driving_param: self.data_type}
            
            family = 'CONSTRUCTOR' if meth_name[0].upper() == meth_name[0] else 'METHOD'
            
            self.add_call(family, blid, meth_name, **fixed)
            
        # ----------------------------------------------------------------------------------------------------
        # FunctionNodeCompare is a little bit complex !
        
        blid    = 'FunctionNodeCompare'
        val_ops = ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')
        str_ops = ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
        col_ops = ('EQUAL', 'NOT_EQUAL', 'BRIGHTER', 'DARKER')
        
        if self.class_name == 'Integer':
            for op in val_ops:
                self.add_call('METHOD', blid, op.lower(), data_type='INT', operation=op, mode='ELEMENT')
                
        elif self.class_name == 'Float':
            for op in val_ops:
                self.add_call('METHOD', blid, op.lower(), data_type='FLOAT', operation=op, mode='ELEMENT')
                
        elif self.class_name == 'Vector':
            modes = ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
            for op in val_ops:
                self.add_call('METHOD', blid, op.lower(), data_type='VECTOR', operation=op)
                
        elif self.class_name == 'String':
            for op in str_ops:
                self.add_call('METHOD', blid, op.lower(), data_type='STRING', operation=op, mode='ELEMENT')
                
        elif self.class_name == 'Color':
            for op in col_ops:
                self.add_call('METHOD', blid, op.lower(), data_type='RGBA', operation=op, mode='ELEMENT')
        
        
    # ----------------------------------------------------------------------------------------------------
    # Data type for multi classes nodes (random for instance)

    @property
    def data_type(self):
        if self.class_name in DATA_TYPES:
            return DATA_TYPES[self.class_name]
        else:
            return self.class_name.upper()
        
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
        self.methods_.append(NodeCall(family, self.wnodes[bl_idname], class_name=self.class_name, meth_name=meth_name, **kwargs))
        
    # ----------------------------------------------------------------------------------------------------
    # Add node properties
    
    def add_property(self, bl_idname, meth_name, settable=False, prop_names=None, **kwargs):
        self.methods_.append(NodeCall.Property(self.wnodes[bl_idname], self.class_name, meth_name, settable=settable, prop_names=prop_names, **kwargs))
        
    # ----------------------------------------------------------------------------------------------------
    # Add attributes
    
    def add_attribute(self, bl_idname, meth_name, capture=False, domains=None, no_prefix='NONE', prop_names=None):

        if domains is None:
            domains = ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
            
        capture_meth = f"capture_{meth_name}"
            
        if capture:
            self.methods_.append(NodeCall.Attribute(self.wnodes[bl_idname], self.class_name, capture_meth, capture_meth=None, domain=domains[0]))
            
        for domain in domains:
            if prop_names is None:
                m_name = meth_name if domain == no_prefix else f"{domain.lower()}_{meth_name}"
                self.methods_.append(NodeCall.Attribute(
                    self.wnodes[bl_idname], self.class_name, m_name, capture_meth=capture_meth, domain=domain))
                
            else:
                for i, m_name in enumerate(prop_names):
                    self.methods_.append(NodeCall.Attribute(
                        self.wnodes[bl_idname], self.class_name, m_name, capture_meth=capture_meth, domain=domain, output_index=i))
                    

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
    # Generate the class source code
        
    def gen_class(self):
        
        _indent_, _0_, _1_, _2_, _3_, _4_ = indent_set(-1 if self.is_global else 0)
        
        # ----------------------------------------------------------------------------------------------------
        # Generates module header
        
        yield "import geonodes as gn\n"
        yield "from geonodes.core import datasockets as dsock\n"
        yield "from geonodes.nodes import nodes\n\n"
        yield "import logging\n"
        yield "logger = logging.Logger('geonodes')\n"
        yield "\n"

        # ----------------------------------------------------------------------------------------------------
        # Class header or list of function to import
        
        if self.is_global:
            meths = [nc.meth_name for nc in self.methods_]
            meths.sort()
            
            simport = "from geonodes.sockets.functions import " 
            s = ""
            sep = simport
            
            yield '"""' + " Function to declare in file __init__.py\n"
            
            wmax = 100
            for i, meth_name in enumerate(meths):
                s += sep + meth_name
                sep = ", "
                if len(s) > wmax or i == len(meths)-1:
                    yield s + "\n"
                    s = ""
                    sep = simport
                    
            yield '"""' + "\n"
            
        else:
            yield  "# " + '='*110 + "\n"
            yield f"# Data class {self.class_name}\n"
            
            yield _0_ + f"class {self.class_name}({self.super_class}):"

        # ----------------------------------------------------------------------------------------------------
        # Comments
        
        yield _1_ + '"""' + f" Data socket {self.class_name}"
        
        for family, label in FAMILIES.items():
            meths = self.methods(family)
            if meths:
                meths.sort(key=lambda nc: nc.meth_name)
                yield _0_
                yield _1_ + f"{label[1]}"
                yield _1_ + "-" * len(label[1])
                for nc in meths:
                    yield _2_ + f"{nc.class_comment}"
            
        yield _1_ + '"""'
        
        # ----------------------------------------------------------------------------------------------------
        # Properties attributes
        
        meths = self.methods('PROPERTY')
        if meths:
            yield _0_ + _1_ + "def reset_properties(self):"
            for nc in meths:
                yield _2_ + f"self.{nc.meth_name}_ = None"

        # ----------------------------------------------------------------------------------------------------
        # Methods
        
        for family, label in FAMILIES.items():
            
            meths = self.methods(family)
            if not meths:
                continue
            
            yield f"\n{_1_}# {'-'*100}{_1_}# {label[1]}\n"
            
            for nc in meths:
                for line in nc.wnode.gen_call(family, nc.class_name, nc.meth_name, self_name=nc.self_name, properties=nc.properties, attribute=nc.attribute, **nc.fixed):
                    yield line
                    

# -----------------------------------------------------------------------------------------------------------------------------
# Global functions
                    
class GlobalGen(DataClass):
    
    def __init__(self, nodes):
        super().__init__(nodes, 'functions', '')

        self.is_global = True

        self.add_call('FUNCTION', 'FunctionNodeCompare',          meth_name="compare"             )
        self.add_call('FUNCTION', 'GeometryNodeStringJoin',       meth_name="join_strings"        )
        
        self.add_call('FUNCTION', 'GeometryNodeInputSceneTime', 'scene')

        
        blid = 'ShaderNodeMath'
        for op, spec in MATH.items():
            self.add_call('FUNCTION', blid, spec[0], operation=op)
            
        blid = 'ShaderNodeVectorMath'
        for op, meth_name in VECTOR_MATH.items():
            f_name = f"vector_{meth_name}" if op in MATH else meth_name
            self.add_call('FUNCTION', blid, f_name, operation=op)
            
        blid = 'ShaderNodeMixRGB'
        for op, meth_name in COLOR_MIX.items():
            self.add_call('FUNCTION', blid, f"color_{meth_name}", blend_type=op)
            

# -----------------------------------------------------------------------------------------------------------------------------
# Boolean

class BooleanGen(DataClass):
    def __init__(self, nodes):
        
        super().__init__(nodes, 'Boolean', 'dsock.Boolean')
        
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
        
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Integer
        
class IntegerGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Integer', 'dsock.Integer')
        

        # ----------------------------------------------------------------------------------------------------
        # Operations
        
        blid = 'ShaderNodeMath'
        for op, spec in MATH.items():
            ret_class = 'Integer' if spec[1] == 'SAME' else spec[1]
            self.add_call('METHOD', blid, spec[0], self_name="value0", ret_class=ret_class, operation=op)


# -----------------------------------------------------------------------------------------------------------------------------
# Float

class FloatGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Float', 'dsock.Float')
        
        # ----------------------------------------------------------------------------------------------------
        # Operations
        
        blid = 'ShaderNodeMath'
        for op, spec in MATH.items():
            ret_class = 'Float' if spec[1] == 'SAME' else spec[1]
            self.add_call('METHOD', blid, spec[0], ret_class=ret_class, operation=op)

        # ----------------------------------------------------------------------------------------------------
        # Methods

        self.add_call('METHOD', 'FunctionNodeFloatToInt',     'to_integer',   ret_class='Integer')
        self.add_call('METHOD', 'FunctionNodeValueToString',  'to_string',    ret_class='String' )

        self.add_call('METHOD', 'ShaderNodeValToRGB',        'color_ramp'       )
        

        self.add_call('STACK', 'ShaderNodeFloatCurve',       'curve'            )
        self.add_call('STACK', 'ShaderNodeClamp',            'clamp'            )
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Vector
        
class VectorGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Vector', 'dsock.Vector')
        
        # ----------------------------------------------------------------------------------------------------
        # Constructors

        self.add_call('CONSTRUCTOR', 'ShaderNodeCombineXYZ',            'Combine')
        self.add_call('CONSTRUCTOR', 'FunctionNodeAlignEulerToVector',  'AlignToVector')
        
        # ----------------------------------------------------------------------------------------------------
        # Operations
        
        blid = 'ShaderNodeVectorMath'
        for op, meth_name in VECTOR_MATH.items():
            self.add_call('METHOD', blid, meth_name, operation=op)

        # ----------------------------------------------------------------------------------------------------
        # x, y, z properties
        
        self.add_property('ShaderNodeSeparateXYZ', 'separate', settable=True)

        # ----------------------------------------------------------------------------------------------------
        # Methods
    
        self.add_call('STACK', 'ShaderNodeVectorCurve',           'curves'          )
        self.add_call('STACK', 'FunctionNodeAlignEulerToVector',  'align_to_vector' )
        self.add_call('STACK', 'FunctionNodeRotateEuler',         'rotate_euler'    )
        self.add_call('METHOD', 'ShaderNodeVectorRotate',         'rotate'          )
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# String

class ColorGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Color', 'dsock.Color')
        
        # ----------------------------------------------------------------------------------------------------
        # Constructor
        
        self.add_call('CONSTRUCTOR', 'ShaderNodeCombineRGB', 'Combine')
        
        # ----------------------------------------------------------------------------------------------------
        # Operations
        
        blid = 'ShaderNodeMixRGB'
        for op, meth_name in COLOR_MIX.items():
            self.add_call('METHOD', blid, meth_name, self_name="color1", blend_type=op)
        
        # ----------------------------------------------------------------------------------------------------
        # r, g, b properties
        
        self.add_property('ShaderNodeSeparateRGB', 'separate', settable=True)

        # ----------------------------------------------------------------------------------------------------
        # Methods

        self.add_call('STACK', 'ShaderNodeRGBCurve',         'curves')
        self.add_call('METHOD', 'ShaderNodeMixRGB',          'mix')
        

# -----------------------------------------------------------------------------------------------------------------------------
# String

class StringGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'String', 'dsock.String')
        
        # ----------------------------------------------------------------------------------------------------
        # Property
        
        self.add_property('FunctionNodeStringLength', 'length')
        
        # ----------------------------------------------------------------------------------------------------
        # Operation

        self.add_call('METHOD', 'GeometryNodeStringJoin', meth_name="join", self_name="strings")        
        
        # ----------------------------------------------------------------------------------------------------
        # Methods
        
        
        self.add_call('STACK', 'FunctionNodeReplaceString',      'replace')
        
        self.add_call('METHOD', 'FunctionNodeSliceString',       'slice')        
        self.add_call('METHOD', 'GeometryNodeStringToCurves',    'to_curves',  ret_class = 'Curve')        
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Geometry
        
class GeometryGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Geometry', 'dsock.Geometry')
        
        self.add_attribute('GeometryNodeInputNormal',       'normal',           domains=None  , capture=True)
        self.add_attribute('GeometryNodeInputTangent',      'tangent',          domains=None  , capture=True)
        
        # ----- ID and Index
        
        self.add_attribute('GeometryNodeInputID',           'ID',               capture=True, domains=['POINT']  )
        self.add_attribute('GeometryNodeInputIndex',        'index',            capture=True, domains=['POINT']  )        
        self.add_attribute('GeometryNodeInputPosition',     'position',         capture=True, domains=['POINT']  , no_prefix='POINT')
        self.add_attribute('GeometryNodeIsViewport',        'is_viewport',      capture=True, domains=['POINT']  )
        
        
        self.add_property('GeometryNodeBoundBox',           'bound_box',  prop_names=['box', 'box_min', 'box_max'])
        self.add_property('GeometryNodeSeparateComponents', 'components', 
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
        self.add_call('METHOD', 'GeometryNodeSeparateGeometry',     'components'            )
        self.add_call('METHOD', 'GeometryNodeConvexHull',           'convex_hull'           )
        self.add_call('METHOD', 'GeometryNodeGeometryToInstance',   'to_instance'           )
        self.add_call('METHOD', 'GeometryNodeJoinGeometry',         'join'                  )
        self.add_call('METHOD', 'GeometryNodeProximity',            'proximity'             )
        
        
        
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
        self.add_attribute('GeometryNodeInputIndex',                'position',        domains={'FACE', 'EDGE', 'CORNER'})
        
        self.add_attribute('GeometryNodeInputMeshEdgeNeighbors',   'edge_neighbors',   capture=True, domains=['EDGE']  , no_prefix='EDGE')
        self.add_attribute('GeometryNodeInputMeshFaceArea',        'face_area',        capture=True, domains=['FACE']  , no_prefix='FACE')
        self.add_attribute('GeometryNodeInputMeshEdgeAngle',       'edge_angle',       capture=True, domains=['EDGE']  , prop_names=('edge_unsigned_angle', 'edge_angle'))
        self.add_attribute('GeometryNodeInputMeshEdgeVertices',    'edge_vertices',    capture=True, domains=['EDGE']  , 
                           prop_names=('edge_vertices_index1', 'edge_vertices_index2', 'edge_vertices_position1', 'edge_vertices_position2'))
        self.add_attribute('GeometryNodeInputMeshFaceNeighbors',   'face_neighbors',   capture=True, domains=['FACE']  ,
                           prop_names=('face_neighbors_vertex_count', 'face_neighbors_face_count'))
        self.add_attribute('GeometryNodeInputMeshIsland',          'island',           capture=True, domains=['FACE']  , prop_names=('island_index', 'island_count'))
        self.add_attribute('GeometryNodeInputMeshVertexNeighbors', 'vertex_neighbors', capture=True, domains=['POINT'] ,
                           prop_names=('vertex_neighbors_vertex_count', 'vertex_neighbors_face_count'))
        
        
        self.add_attribute('GeometryNodeInputMaterialIndex',       'material_index',   capture=True, domains=['FACE']  , no_prefix='FACE')
        self.add_attribute('GeometryNodeInputShadeSmooth',         'shade_smooth',     capture=True, domains=['FACE']  , no_prefix='FACE')
        
        
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
        
        self.add_attribute('GeometryNodeInputSplineCyclic',         'cyclic',       capture=True, domains=['CURVE']  , no_prefix='CURVE')
        self.add_attribute('GeometryNodeInputSplineResolution',     'resolution',   capture=True, domains=['CURVE']  , no_prefix='CURVE')
        self.add_attribute('GeometryNodeSplineLength',              'length',       capture=True, domains=['CURVE']  ,
                           prop_names = ['length', 'point_count'])
        self.add_attribute('GeometryNodeSplineParameter',           'parameter',    capture=True, domains=['CURVE']  ,
                           prop_names = ['factor', 'parameter_length', 'parameter_index'])
        
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
        
        
        self.add_attribute('GeometryNodeCurveEndpointSelection',        'endpoint_selection',       capture=True, domains=['CURVE']  , no_prefix='CURVE')
        self.add_attribute('GeometryNodeCurveHandleTypeSelection',      'handle_type_selection',    capture=True, domains=['CURVE']  , no_prefix='CURVE')
        self.add_attribute('GeometryNodeInputCurveTilt',                'tilt',                     capture=True, domains=['CURVE']  , no_prefix='CURVE')
        self.add_attribute('GeometryNodeInputRadius',                   'radius',                   capture=True, domains=['CURVE']  , no_prefix='CURVE')
        self.add_attribute('GeometryNodeInputCurveHandlePositions',     'handle_positions',         capture=True, domains=['CURVE']  , 
                           prop_names=('left_handle_position', 'right_handle_position'))
        
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
        super().__init__(nodes, 'Texture', 'dsock.Texture')
        
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
        
# -----------------------------------------------------------------------------------------------------------------------------
# Material
        
class MaterialGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Material', 'dsock.Material')

        self.add_call('METHOD', 'GeometryNodeMaterialSelection', 'selection', ret_class='Boolean')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Image 
        
class ImageGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Image', 'dsock.Image')
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Collection
        
class CollectionGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Collection', 'dsock.Collection')

        self.add_call('METHOD', 'GeometryNodeCollectionInfo', 'info')
        
# -----------------------------------------------------------------------------------------------------------------------------
# Object
        
class ObjectGen(DataClass):
    def __init__(self, nodes):
        super().__init__(nodes, 'Object', 'dsock.Object')

        self.add_property('GeometryNodeObjectInfo', 'info')


# =============================================================================================================================
# The classes generators
        

DATA_CLASSES = [GlobalGen, BooleanGen, IntegerGen, FloatGen, VectorGen, ColorGen, StringGen,
                GeometryGen, SplineGen, CurveGen, MeshGen, PointsGen, InstancesGen, VolumeGen,
                CollectionGen, ObjectGen, TextureGen, MaterialGen, ImageGen]


#DATA_CLASSES = [BooleanGen]

     

