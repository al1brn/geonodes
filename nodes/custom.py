#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:19:44 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : custom
---------------
Depending on their sockets, nodes can be automaticalley implemented as class socket methods.
The custom functions defined more accurate ways to implement nodes using add_function function:

update : 2024/02/17
update : 2024/03/29
"""

from pprint import pprint

from geonodes.nodes import documentation
from geonodes.nodes import constants
from geonodes.nodes import utils
from geonodes.nodes import dynamic

CUSTOM = {bl_id: {} for bl_id in constants.TREE_BL_IDS.values()}

CUST_PROPS = {bl_id: [] for bl_id in constants.TREE_BL_IDS.values()}

TEST_PROPS = {bl_id: {} for bl_id in constants.TREE_BL_IDS.values()}

class C:

    GLOBAL = 'GLOBAL'
    METHOD = 'METHOD'
    GETTER = 'GETTER'
    SETTER = 'SETTER'

    def __init__(self,
                 impl_type,            # Implementation type
                 target,               # Target class
                 self_socket  = None,  # Socket to plug self into
                 name         = "@",   # Name template
                 jump         = None,  # Name of the socket to jump on
                 ret_socket   = None,  # Socket to return
                 loops        = [],    # Loop on node parameter
                 value_socket = None,  # For property setter
                 descr        = None,  # Documentation
                 tree_type    = None,  # Tree type filter (some nodes share the same name)
                 **kwargs):            # Node parameters

        self.impl_type  = impl_type

        self.target       = target
        self.name         = name
        self.self_socket  = self_socket
        self.jump         = jump
        self.ret_socket   = ret_socket
        self.value_socket = value_socket
        self.loops        = loops
        self.descr        = descr
        self.tree_type    = tree_type
        self.kwargs       = kwargs

    def __str__(self):
        return f"[C: {self.impl_type=}, {self.target=}, {self.name=}, {self.self_socket=}, {self.ret_socket=}"

    @classmethod
    def Glob(cls, name="@", ret_socket=None, loops=[], descr=None, tree_type=None, **kwargs):
        return cls(C.GLOBAL, None,
                   name       = name,
                   ret_socket = ret_socket,
                   loops      = loops,
                   descr      = descr,
                   tree_type  = tree_type,
                   **kwargs)

    @classmethod
    def Meth(cls, target, self_socket="@", name="@", jump=None, ret_socket=None, loops=[], descr=None, tree_type=None, **kwargs):
        return cls(C.METHOD, target,
                 self_socket  = self_socket,
                 name         = name,
                 jump         = jump,
                 ret_socket   = ret_socket,
                 loops        = loops,
                 tree_type    = tree_type,
                 descr        = descr,
                 **kwargs)

    @classmethod
    def Get(cls, target, name, self_socket, ret_socket, loops=[], descr=None, tree_type=None, **kwargs):
        return cls(C.GETTER, target,
                 self_socket  = self_socket,
                 name         = name,
                 ret_socket   = ret_socket,
                 loops        = loops,
                 tree_type    = tree_type,
                 descr        = descr,
                 **kwargs)

    @classmethod
    def Set(cls, target, name, self_socket, value_socket, jump=None, loops=[], descr=None, tree_type=None, **kwargs):
        return cls(C.SETTER, target,
                 name         = name,
                 self_socket  = self_socket,
                 value_socket = value_socket,
                 jump         = jump,
                 loops        = loops,
                 tree_type    = tree_type,
                 descr        = descr,
                 **kwargs)

    # ====================================================================================================
    # Build code

    def code(self, node_info):

        # ----- Check tree type is ok

        tree_type = node_info.tree_type

        if self.tree_type is not None:
            if isinstance(self.tree_type, tuple):
                if tree_type not in self.tree_type:
                    return
            else:
                if tree_type != self.tree_type:
                    return

        # ----- Debug

        if False and node_info.class_name in ['Math']:
            print("="*100)
            print("C.Code", tree_type, self)
            print("")
            print("bl_idname", node_info.bl_idname)
            print(node_info.class_name, node_info.params)
            print()

        # ---------------------------------------------------------------------------
        # Loop on targets
        # - Can be a tuple (several targets), e.g.: ('Float', 'Int')
        # - Or a dict : param_name = tuple of data type values, e.g.: {'data_type': ('FLOAT', 'INT)}

        targets = self.target
        data_type_socket = None
        if isinstance(targets, dict):
            data_type_socket = list(targets.keys())[0]
            targets = targets[data_type_socket]
            # Targets is an empty tuple : the values must be read from the parameter
            if isinstance(targets, tuple) and len(targets) == 0:
                targets = tuple(node_info.enum_params[data_type_socket])

        if isinstance(targets, tuple):

            for target in targets:

                if data_type_socket is None:
                    kwargs = self.kwargs
                else:
                    kwargs = {**self.kwargs}
                    kwargs[data_type_socket] = target
                    target = constants.DATA_TYPE_TO_SOCKET_CLASS_NAME[target]

                C(impl_type    = self.impl_type,
                  target       = target,
                  self_socket  = self.self_socket,
                  name         = self.name,
                  jump         = self.jump,
                  ret_socket   = self.ret_socket,
                  value_socket = self.value_socket,
                  loops        = self.loops,
                  descr        = self.descr,
                  **kwargs).code(node_info)
            return

        # ---------------------------------------------------------------------------
        # Loops on parameters

        if len(self.loops) > 0:

            param  = self.loops[0]

            # ----- Store the current value of the parameter

            mem_value = getattr(node_info.bnode, param)
            mems      = node_info.setup(**self.kwargs)

            # ----- Loop on the possible values

            values = node_info.get_enum_list(param)

            for value in values:

                setattr(node_info.bnode, param, value)
                self.kwargs[param] = value

                new_loops = self.loops[1:]
                if param == 'operation':
                    new_name  = self.name.replace(param.upper(), utils.operation_name(value))
                else:
                    new_name  = self.name.replace(param.upper(), utils.data_type_name(value, values))

                new_descr = f"{param}={value}" if self.descr is None else self.descr + f", {param}={value}"

                if False and node_info.class_name in ['Math']:
                    print("CUSTOM code", value, new_name)

                C(self.impl_type, self.target,
                    name         = new_name,
                    self_socket  = self.self_socket,
                    jump         = self.jump,
                    ret_socket   = self.ret_socket,
                    value_socket = self.value_socket,
                    loops        = new_loops,
                    descr        = new_descr,
                    **self.kwargs).code(node_info)

            # ----- Restore the previous value

            del self.kwargs[param]

            node_info.setup(**mems)
            setattr(node_info.bnode, param, mem_value)

            return

        # ---------------------------------------------------------------------------
        # Main

        # ----- Target class name short cut
        # Int --> INTEGER for instance

        if self.target is not None and self.target in constants.SOCKET_CLASS_NAME_SHORTCUTS:
            self.target = constants.SOCKET_CLASS_NAME_SHORTCUTS[self.target]

        # ----- Target not implemented in this Tree
        # For instance Int doesn't exist in Shaders

        if self.target is not None and self.target not in constants.SOCKETS[tree_type]:
            return

        # ----- Replace @ tokens

        if False and node_info.class_name == 'MapRange':
            print("C.code:", node_info.class_name, str(self))

        # Name : replace by the node python name
        name = self.name.replace('@', node_info.python_name)

        # sockets : replace by the lower of the target name

        self_socket  = self.self_socket
        ret_socket   = self.ret_socket
        value_socket = self.value_socket

        if self.impl_type != C.GLOBAL:
            if self_socket is not None:
                self_socket = self_socket.replace('@', constants.SOCKET_CLASS_DEFAULT_SOCKET_NAME[self.target])

            if ret_socket is not None:
                ret_socket = ret_socket.replace('@', constants.SOCKET_CLASS_DEFAULT_SOCKET_NAME[self.target])

            if value_socket is not None:
                value_socket = value_socket.replace('@', constants.SOCKET_CLASS_DEFAULT_SOCKET_NAME[self.target])

        # ----- All sockets if no param is set

        all_sockets = True
        for param in node_info.params:
            if param in self.kwargs:
                all_sockets = False
                break

        # ----- If ret_socket is None:
        # - returns node if no jump
        # - else returns self

        if ret_socket is None and self.jump is not None:
            ret_socket = 'self'

        # ----- For documentation

        doc_kwargs = {
            'self_socket' : self_socket,
            'jump'        : 'No' if self.jump is None else self.jump,
            'return'      : 'node' if ret_socket is None else ret_socket,
            }

        use_args = node_info.bl_idname in constants.USE_ARGS_NODES

        # ---------------------------------------------------------------------------
        # Global method (= method of Tree)

        if self.impl_type == C.GLOBAL:

            args = node_info.build_meth_args(all_sockets=all_sockets, node_label=False, use_args=use_args, **self.kwargs)

            if False and self.name == 'sin':
                print("CUSTOM C.code", args)

            if True:
                # Property if not arg
                # If more than on output socket, returns the node
                is_prop = len(args) == 0
                if is_prop and ret_socket is None and len(node_info.outputs) == 1:
                    ret_socket = node_info.outputs.socket_names[0]
            else:
                is_prop = ret_socket is not None and len(args) == 0
            if not is_prop:
                args.add('node_label', None)
                args.add('node_color', None)

            # As method of Tree
            args.is_static = False

            # Header
            if args.header_code == "":
                s = f"def {name}(**kwargs):\n"
            else:
                s = f"def {name}({args.header_code}, **kwargs):\n"

            # Create the node
            if args.call_code == "":
                s += f"\tnode = self.{node_info.class_name}(**kwargs)\n"
            else:
                s += f"\tnode = self.{node_info.class_name}({args.call_code}, **kwargs)\n"

            # Return node or socket
            if ret_socket is None:
                s += "\treturn node\n"

            else:
                s += f"\treturn node.{ret_socket}\n"

            if False and self.name == 'sin':
                print("CUSTOM C.code\n", s)


            #print("CUSTOM GLOBAL", name, "\n", s)

            # ----- Add to dynamic class of the Tree

            del doc_kwargs['jump'], doc_kwargs['self_socket']

            dyn = constants.TREES[node_info.tree_type]
            if is_prop:
                dyn.add_member('GETTER', name, s, node_info.class_name, args=args, descr=None, **doc_kwargs)
            else:
                dyn.add_member('METHOD', name, s, node_info.class_name, args=args, descr=None, **doc_kwargs)

        # ---------------------------------------------------------------------------
        # Socket method

        elif self.impl_type == C.METHOD:

            # Little hack to exclude redundant methods

            if tree_type == 'GeometryNodeTree':
                if node_info.class_name == 'Math':
                    if name in ['less_than', 'greater_than', 'round', 'floor']:
                        name = 'math_' + name

            try:
                args = node_info.build_meth_args(self_socket=self_socket, all_sockets=all_sockets, use_args=use_args, **self.kwargs)

            except Exception as e:
                # Implementatio not valid for this tree_type !
                if False:
                    print('='*100)
                    print(f"Custom C.Code error ({tree_type})): node {node_info.class_name} ({node_info.bl_idname})), target: {self.target}, kwargs:", self.kwargs)
                    print()
                return
                #raise Exception(e)

            # To access self.tree
            args.is_static = False

            # Header
            if args.header_code == "":
                s = f"def {name}(**kwargs):\n"
            else:
                s = f"def {name}({args.header_code}, **kwargs):\n"

            # Create the node
            if args.call_code == "":
                s += f"\tnode = self.tree.{node_info.class_name}(**kwargs)\n"
            else:
                s += f"\tnode = self.tree.{node_info.class_name}({args.call_code}, **kwargs)\n"

            # Self jump
            if self.jump is not None:
                s += f"\tself.jump(node.{self.jump})\n"

            # Return node or socket
            if ret_socket is None:
                s += "\treturn node\n"

            elif ret_socket == 'self':
                s += "\treturn self\n"

            else:
                s += f"\treturn node.{ret_socket}\n"

            # ----- Add to dynamic class

            dyn = constants.SOCKETS[node_info.tree_type][self.target]
            dyn.add_member('METHOD', name, s, node_info.class_name, args=args, descr=None, **doc_kwargs)

        # ---------------------------------------------------------------------------
        # Property getter

        elif self.impl_type == C.GETTER:

            args = node_info.build_meth_args(self_socket=self_socket, all_sockets=all_sockets, node_label=False, **self.kwargs)
            #args.add("node_color", call=str(constants.NODE_COLORS['property']))
            args.add("node_color", call=constants.NODE_COLORS['property'])

            # To access self.tree
            args.is_static = False

            # Header
            s = f"def {name}(self):\n"

            # Create the node
            s += f"\tnode = self.tree.{node_info.class_name}({args.call_code})\n"

            # Self jump
            if self.jump is not None:
                s += f"\tself.jump(node.{self.jump})\n"

            # Return node or socket
            if ret_socket is None:
                s += "\treturn node\n"

            elif ret_socket == 'self':
                s += "\treturn self\n"

            else:
                s += f"\treturn node.{ret_socket}\n"

            # ----- Add to dynamic class

            dyn = constants.SOCKETS[node_info.tree_type][self.target]
            dyn.add_member('GETTER', name, s, node_info.class_name, args=args, descr=None, **doc_kwargs)


        # ---------------------------------------------------------------------------
        # Property setter

        elif self.impl_type == C.SETTER:

            args = node_info.build_meth_args(self_socket=self_socket, all_sockets=all_sockets, node_label=False, **{value_socket: 'value'}, **self.kwargs)

            # To access self.tree
            args.is_static = False

            # Header
            s = f"def {name}(self, value):\n"

            # Create the node
            if False:
                s += f"\tnode = self.tree.{node_info.class_name}({args.call_code}"
            else:
                s += f"\tnode = self.tree.{node_info.class_name}({self_socket}=self, {value_socket}=value"

            # Selection socket
            if args['selection'] is not None and 'selection' not in self.kwargs:
                s +=  ", selection=self._get_selection(None)"

            # kwargs
            for k, v in self.kwargs.items():
                s += f", {k}={v}"

            # Color
            s += f", node_color={constants.NODE_COLORS['property']}"

            # Done
            s += ")\n"

            # Self jump
            if self.jump is not None:
                s += f"\tself.jump(node.{self.jump})\n"

            # ----- Add to dynamic class

            dyn = constants.SOCKETS[node_info.tree_type][self.target]
            dyn.add_member('SETTER', name, s, node_info.class_name, args=args, descr=None, **doc_kwargs)


        # ----- Register cross reference

        constants.cross_ref(node_info.tree_type, node_info.class_name, None if self.impl_type == C.GLOBAL else self.target, name)

        # ----- Debug

        if False and node_info.class_name == 'Math' and name not in ['']:
            print('='*100)
            print("C.CODE", node_info.tree_name, node_info.class_name, '->', self.target, self.name)
            print(s)
            print()

# =============================================================================================================================
# DEFAULT NODE IMPLEMENTATIONS

NODE_IMPLEMENTATIONS = {
    'AccumulateField'    : None,
    'AlignEulerToVector' : C.Meth(('Rot', 'Vect'), self_socket='rotation', ret_socket='rotation'),
    'Arc'                : C.Glob(ret_socket='curve'),
    'AttributeStatistic' : [C.Meth('Geometry'),
                            C.Meth('Geometry', name='@_DATA_TYPE', loops=['data_type'])],
    'AxisAngleToRotation': C.Meth('Vect', 'axis', ret_socket='rotation'),
    'Bake'               : [C.Glob(ret_socket='geometry'),
                            C.Meth('Geometry', self_socket='geometry', ret_socket='geometry')],
    'BezierSegment'      : C.Glob(ret_socket='curve'),
    'BlurAttribute'      : [C.Meth('Geometry', self_socket=None, ret_socket='value'),
                            C.Meth('Int',   'value', ret_socket='value', data_type='INT'),
                            C.Meth('Float', 'value', ret_socket='value', data_type='FLOAT'),
                            C.Meth('Col',   'value', ret_socket='value', data_type='FLOAT_COLOR'),
                            C.Meth('Vect',  'value', ret_socket='value', data_type='FLOAT_VECTOR')],
    'Boolean'            : None,
    'BooleanMath'        : [C.Glob('OPERATION', ret_socket='boolean', loops=['operation']),
                            C.Meth('Bool', 'boolean', 'OPERATION', ret_socket='boolean', loops=['operation'])],
    'BoundingBox'        :  C.Meth('Geometry'),
    'BrickTexture'       : C.Glob(ret_socket='color'),
    'CaptureAttribute'   : [C.Meth('Geometry', jump='geometry', ret_socket='attribute'),
                            C.Meth('Geometry', jump='geometry', ret_socket='attribute', name='capture_DATA_TYPE', loops=['data_type'])],
    'CheckerTexture'     : C.Glob(ret_socket='curve'),
    'Clamp'              : C.Meth(('Int', 'Float'), self_socket='value', ret_socket='result'),
    'CollectionInfo'     : C.Meth('Collection', ret_socket='instances'),
    'Color'              : None,
    'ColorRamp'          : C.Meth(('Float', 'Int'), 'fac', ret_socket='value'),
    'CombineColor'       : [C.Glob(ret_socket='color'),
                            C.Glob('MODE', ret_socket='color', loops=["mode"])],
    'CombineXYZ'         : [C.Glob(ret_socket='vector'),
                            C.Glob('xyz', ret_socket='vector')],
    'Compare'            : C.Meth({'data_type': ()}, 'a', ret_socket='result', name='OPERATION', loops=['operation']),
    'Cone'               : C.Glob(ret_socket='mesh'),
    'ConvexHull'         : C.Meth('Geometry', ret_socket='convex_hull'),
    'CornersOfEdge'      : [C.Meth('Geometry', None), C.Glob()],
    'CornersOfFace'      : [C.Meth('Geometry', None), C.Glob()],
    'CornersOfVertex'    : [C.Meth('Geometry', None), C.Glob()],
    'Cube'               : C.Glob(ret_socket='mesh'),
    'CurveCircle'        : C.Glob(ret_socket='curve'),
    'CurveHandlePositions' : [C.Meth('Geometry', None), C.Glob()],
    'CurveLength'        : C.Get('Geometry', '@', 'curve', 'length'),
    'CurveLine'          : C.Glob(ret_socket='curve'),
    'CurveOfPoint'       : [C.Meth('Geometry', None), C.Glob()],
    'CurveTangent'       : C.Get('Geometry', '@', None, 'tangent'),
    'CurveTilt'          : C.Get('Geometry', '@', None, 'tilt'),
    'CurveToMesh'        : C.Meth('Geometry', self_socket='curve', ret_socket='mesh'),
    'CurveToPoints'      : C.Meth('Geometry', self_socket='curve'),
    'Cylinder'           : C.Glob(ret_socket='mesh'),
    'DeformCurvesOnSurface' : C.Meth('Geometry', 'curves', jump='curves'),
    'DeleteGeometry'     : C.Meth('Geometry', jump='geometry'),
    'DistributePointsInVolume' : C.Meth('Geometry', 'volume',  ret_socket='points'),
    'DistributePointsOnFaces'  : C.Meth('Geometry', 'mesh'),
    'DomainSize'         : C.Meth('Geometry'),
    'DualMesh'           : C.Meth('Geometry', 'mesh', ret_socket='mesh'),
    'DuplicateElements'  : C.Meth('Geometry'),
    'EdgeAngle'          : [C.Meth('Geometry', None), C.Glob(),],
    'EdgeNeighbors'      : [C.Get('Geometry', '@', None, 'face_count'), C.Glob(),],
    'EdgePathsToCurves'  : C.Meth('Geometry', 'mesh', ret_socket='curves'),
    'EdgePathsToSelection' : [C.Meth('Geometry', None, ret_socket='selection'), C.Glob()],
    'EdgeVertices'       : [C.Meth('Geometry', None), C.Glob()],
    'EdgesOfCorner'      : [C.Meth('Geometry', None), C.Glob()],
    'EdgesOfVertex'      : [C.Meth('Geometry', None), C.Glob()],
    'EdgesToFaceGroups'  : [C.Meth('Geometry', None, ret_socket='face_group_id'), C.Glob()],
    'EndpointSelection'  : [C.Meth('Geometry', None, ret_socket='selection'), C.Glob()],
    'EulerToRotation'    : C.Meth('Vect', 'euler', ret_socket='rotation'),
    'EvaluateAtIndex'    : [C.Meth('Geometry', None, ret_socket='value'),
                            C.Meth('Geometry', None, ret_socket='value', name='evaluate_at_index_DATA_TYPE', loops=['data_type'])],
    'EvaluateOnDomain'   : [C.Meth('Geometry', None, ret_socket='value'),
                            C.Meth('Geometry', None, ret_socket='value', name='evaluate_on_domain_DATA_TYPE', loops=['data_type'])],
    'ExtrudeMesh'        : C.Meth('Geometry', 'mesh', jump='mesh'),
    'FaceArea'           : [C.Get('Geometry', '@', None, 'area'), C.Glob()],
    'FaceGroupBoundaries': [C.Meth('Geometry', None, ret_socket='boundaries_edges'), C.Glob()],
    'FaceNeighbors'      : [C.Meth('Geometry', None), C.Glob()],
    'FaceOfCorner'       : [C.Meth('Geometry', None), C.Glob()],
    'FaceSet'            : None, # ??????
    'FillCurve'          : C.Meth('Geometry', 'curve', ret_socket='mesh'),
    'FilletCurve'        : [C.Meth('Geometry', 'curve', jump='curve'),
                            C.Meth('Geometry', 'curve', jump='curve', name='@_MODE', loops=['mode'])],
    'FlipFaces'          : C.Meth('Geometry',  'mesh',  jump='mesh'),
    'FloatCurve'         : C.Meth(('Float', 'Int'), 'value', jump='value'),
    'FloatToInteger'     : [C.Meth('Float', 'float', ret_socket='integer'),
                            C.Meth('Float', 'float', ret_socket='integer', name='@_ROUNDING_MODE', loops=['rounding_mode']),
                            C.Meth('Float', 'float', ret_socket='integer', name='ROUNDING_MODE', loops=['rounding_mode'])], #('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')
    'Frame'              : None,
    'GeometryProximity'  : C.Meth('Geometry', 'target'),
    'GeometryToInstance' : C.Meth('Geometry', ret_socket='instances'),
    'GradientTexture'    : C.Glob(ret_socket='color'),
    'Grid'               : C.Glob(ret_socket='mesh'),
    'Group'              : None,
    'GroupInput'         : None,
    'GroupOutput'        : None,
    'HandleTypeSelection': [C.Meth('Geometry', None, ret_socket='selection'),
                            C.Glob(),
                            C.Meth('Geometry', None, ret_socket='selection', name='left_@',  mode = {'LEFT'}),
                            C.Meth('Geometry', None, ret_socket='selection', name='right_@', mode = {'RIGHT'})],
    'ID'                 : [C.Get('Geometry', '@', None, 'id'), C.Glob()],
    'IcoSphere'          : C.Glob(ret_socket='mesh'),
    'Image'              : None,
    'ImageInfo'          : C.Meth('Img'),
    'ImageTexture'       : C.Meth('Img'),
    'Index'              : [C.Get('Geometry', '@', None, 'index'), C.Glob()],
    'IndexOfNearest'     : [C.Meth('Geometry', None), C.Glob()],
    'IndexSwitch'        : C.Meth({'data_type': ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')}, 'ARG0', ret_socket='output'),

    'InstanceOnPoints'   : C.Meth('Geometry', 'points', ret_socket='instances'),
    'InstanceRotation'   : [C.Get('Geometry', '@', None, 'rotation'), C.Glob()],
    'InstanceScale'      : [C.Get('Geometry', '@', None, 'scale'), C.Glob()],
    'InstancesToPoints'  : C.Meth('Geometry', 'instances', ret_socket='points'),
    'Integer'            : None,
    'InterpolateCurves'  : C.Meth('Geometry', 'guide_curves'),
    'InvertRotation'     : C.Meth(('Rot', 'Vect'), 'rotation', jump='rotation'),
    'IsEdgeSmooth'       : [C.Get( 'Geometry', 'edge_smooth',   None, 'smooth'), C.Glob()],
    'IsFacePlanar'       : [C.Meth('Geometry', None, ret_socket='planar'), C.Glob()],
    'IsFaceSmooth'       : [C.Get( 'Geometry', 'face_smooth',   None, 'smooth'), C.Glob()],
    'IsSplineCyclic'     : [C.Get( 'Geometry', 'spline_cyclic', None, 'cyclic'), C.Glob()],
    'IsViewport'         : C.Glob(),
    'JoinGeometry'       : [C.Meth('Geometry', 'geometry', jump='geometry'),
                            C.Glob(ret_socket='geometry')],
    'JoinStrings'        : [C.Meth('Str', 'strings', jump='string'),
                            C.Glob(ret_socket='string')],
    'MagicTexture'       : C.Glob(ret_socket='color'),
    'MapRange'           : [C.Meth(('Float', 'Int'), 'value', ret_socket='result'),
                            C.Meth('Vect',           'value', ret_socket='result')],
    'Material'           : None,
    'MaterialIndex'      : [C.Get('Geometry', '@', None, 'material_index'), C.Glob()],
    'MaterialSelection'  : C.Meth('Mat', None, ret_socket='selection'),
    'Math'               : [C.Glob(name='OPERATION',  ret_socket='value', loops=['operation']),
                            C.Meth(('Float', 'Int'), 'value', ret_socket='value', name='OPERATION', loops=['operation'])],
    'MeanFilterSDFVolume': None,
    'MenuSwitch'         : C.Glob(ret_socket='output'),
    'MergeByDistance'    : C.Meth('Geometry', jump='geometry'),
    'MeshBoolean'        : [C.Meth('Geometry', 'mesh_2', name='mesh_intersect',  ret_socket='mesh', operation='INTERSECT'),
                            C.Meth('Geometry', 'mesh_2', name='mesh_union',      ret_socket='mesh', operation='UNION'),
                            C.Meth('Geometry', 'mesh_1', name='mesh_difference', ret_socket='mesh', operation='DIFFERENCE')],
    'MeshCircle'         : C.Glob(ret_socket='mesh'),
    'MeshIsland'         : [C.Meth('Geometry', None), C.Glob()],
    'MeshLine'           : C.Glob(ret_socket='mesh'),
    'MeshToCurve'        : C.Meth('Geometry', 'mesh', ret_socket='curve'),
    'MeshToPoints'       : C.Meth('Geometry', 'mesh', ret_socket='points'),
    'MeshToSDFVolume'    : None,
    'MeshToVolume'       : C.Meth('Geometry', 'mesh', ret_socket='volume'),
    #'Mix'                : [C.Meth(('Float', 'Int'), 'a', jump='result', ret_socket='self', data_type='FLOAT', blend_type='MIX', factor_mode='UNIFORM'),
    #                        C.Meth('Vect', 'a', jump='result', data_type='VECTOR',   blend_type='MIX'),
    #                        C.Meth('Rot',  'a', jump='result', data_type='ROTATION', blend_type='MIX', factor_mode='UNIFORM'),
    #                        C.Meth('Col',  'a', jump='result', data_type='RGBA',     factor_mode='UNIFORM'),
    #                        C.Meth('Col',  'a', jump='result', data_type='RGBA',     name='mix_BLEND_TYPE', loops=['blend_type'], factor_mode='UNIFORM'),
    #                        ],
    'Mix'                : [C.Meth(('Float', 'Int'), 'a', data_type='FLOAT', blend_type='MIX', factor_mode='UNIFORM'),
                            C.Meth('Vect', 'a', data_type='VECTOR',   blend_type='MIX'),
                            C.Meth('Rot',  'a', data_type='ROTATION', blend_type='MIX', factor_mode='UNIFORM'),
                            C.Meth('Col',  'a', data_type='RGBA',     factor_mode='UNIFORM'),
                            C.Meth('Col',  'a', data_type='RGBA',     name='mix_BLEND_TYPE', loops=['blend_type'], factor_mode='UNIFORM'),
                            ],
    'MusgraveTexture'    : C.Glob(ret_socket='height'),
    'NamedAttribute'     : [C.Glob(name='named_DATA_TYPE', ret_socket='attribute', loops=['data_type']),
                            C.Meth('Geometry', None, ret_socket='attribute'),
                            C.Meth('Geometry', None, ret_socket='attribute', name='named_DATA_TYPE', loops=['data_type'])],
    'NoiseTexture'       : C.Glob(ret_socket='fac'),
    'Normal'             : [C.Get('Geometry', 'normal', None, ret_socket='normal'), C.Glob()],
    'ObjectInfo'         : C.Meth('Object'),
    'OffsetCornerInFace' : [C.Meth('Geometry', None, ret_socket='corner_index'), C.Glob()],
    'OffsetPointInCurve' : [C.Meth('Geometry', None), C.Glob()],
    'OffsetSDFVolume'    : None,
    'PackUVIslands'      : C.Meth('Vect', 'uv', jump='uv'),
    'Points'             : C.Glob(ret_socket='points'),
    'PointsOfCurve'      : [C.Meth('Geometry', None), C.Glob()],
    'PointsToCurves'     : C.Meth('Geometry', 'points', ret_socket='curves'),
    'PointsToSDFVolume'  : None,
    'PointsToVertices'   : C.Meth('Geometry', 'points', ret_socket='mesh'),
    'PointsToVolume'     : C.Meth('Geometry', 'points', ret_socket='volume'),
    'Position'           : [C.Get('Geometry', '@', None, 'position'), C.Glob()],
    'QuadraticBezier'    : C.Glob(ret_socket='curve'),
    'Quadrilateral'      : C.Glob(ret_socket='curve'),
    'QuaternionToRotation' : C.Glob(ret_socket='rotation'),
    'RGBCurves'          : C.Meth('Col', jump='color'),
    'Radius'             : [C.Get('Geometry', '@', None, 'radius'), C.Glob()],
    'RandomValue'        : [C.Glob(ret_socket='value'), # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
                            C.Glob('random_DATA_TYPE', ret_socket='value', loops=['data_type'])],
    'Raycast'            : [C.Meth('Geometry', 'target_geometry'),
                            C.Meth('Geometry', 'target_geometry', name='raycast_DATA_TYPE', loops=['data_type'])], # ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
    'RealizeInstances'   : C.Meth('Geometry', jump='geometry'),
    'RemoveNamedAttribute' : C.Meth('Geometry', jump='geometry'),
    'RepeatInput'        : None,
    'RepeatOutput'       : None,
    'ReplaceMaterial'    : C.Meth('Geometry', jump='geometry'),
    'ReplaceString'      : C.Meth('Str', jump='string'),
    'Reroute'            : None,
    'ResampleCurve'      : C.Meth('Geometry', 'curve', jump='curve', ret_socket='self'),
    'ReverseCurve'       : C.Meth('Geometry', 'curve', jump='curve', ret_socket='self'),
    'RotateEuler'        : [C.Meth(('Vect', 'Rot'), 'rotation', jump='rotation'), # ('AXIS_ANGLE', 'EULER')
                            C.Meth(('Vect', 'Rot'), 'rotation', jump='rotation', name= '@_axis_angle', type='AXIS_ANGLE'),
                            C.Meth(('Vect', 'Rot'), 'rotation', jump='rotation', name= '@_euler', type='EULER')],
    'RotateInstances'    : C.Meth('Geometry', 'instances', jump='instances'),
    'RotateRotation'     : C.Meth('Rot', 'rotation', jump='rotation'),
    'RotateVector'       : C.Meth('Vect', jump='vector'),
    'RotationToAxisAngle' : C.Meth(('Rot', 'Vect'), 'rotation'),
    'RotationToEuler'     : C.Meth(('Rot', 'Vect'), 'rotation', rot_socket='euler'),
    'RotationToQuaternion': C.Meth(('Rot', 'Vect'), 'rotation'),
    'SDFVolumeSphere'    : None,
    'SampleCurve'        : [C.Meth('Geometry', 'curves'),
                            C.Meth('Geometry', 'curves', name='@_DATA_TYPE', loops=['data_type']),
                            C.Meth('Geometry', 'curves', name='@_DATA_TYPE_MODE', loops=['data_type', 'mode'])],
    'SampleIndex'        : [C.Meth('Geometry', ret_socket='value'),
                            C.Meth('Geometry', ret_socket='value', name='@_DATA_TYPE', loops=['data_type'])],
    'SampleNearest'      : C.Meth('Geometry', ret_socket='index'),
    'SampleNearestSurface' : [C.Meth('Geometry', 'mesh', ret_socket='value'),
                              C.Meth('Geometry', 'mesh', ret_socket='value', name='@_DATA_TYPE', loops=['data_type'])],
    'SampleUVSurface'    : [C.Meth('Geometry', 'mesh'),
                            C.Meth('Geometry', 'mesh', name='@_DATA_TYPE', loops=['data_type'])],
    'SampleVolume'       : None,
    'ScaleElements'      : C.Meth('Geometry', jump='geometry'),
    'ScaleInstances'     : C.Meth('Geometry', 'instances', jump='instances'),
    'SceneTime'          : [C.Glob(),
                            C.Glob(name='seconds', ret_socket='seconds'),
                            C.Glob(name='frame',   ret_socket='frame')
                            ],
    'Selection'          : None,
    'SelfObject'         : C.Glob(),
    'SeparateColor'      : [C.Meth('Col'),
                            #C.Get('Col', 'MODE', 'color', None, loops=['mode'])
                            ],
    'SeparateComponents' : C.Meth('Geometry'),
    'SeparateGeometry'   : C.Meth('Geometry'),
    'SeparateXYZ'        : [C.Meth('Vect'),
                            #C.Get('Vect', 'xyz', 'vector', None)
                            ],
    'SetCurveNormal'     : [C.Meth('Geometry', 'curve', jump='curve'),
                            C.Set( 'Geometry', 'normal', 'curve', 'mode', jump='curve')],
    'SetCurveRadius'     : [C.Meth('Geometry', 'curve', jump='curve'),
                            C.Set( 'Geometry', 'radius', 'curve', 'radius', jump='curve')],
    'SetCurveTilt'       : [C.Meth('Geometry', 'curve', jump='curve'),
                            C.Set( 'Geometry', 'tilt', 'curve', 'tilt', jump='curve')],
    'SetFaceSet'         : None,
    'SetHandlePositions' : C.Meth('Geometry', 'curve', jump='curve'),
    'SetHandleType'      : C.Meth('Geometry', 'curve', jump='curve'),
    'SetID'              : [C.Meth('Geometry', jump='geometry'),
                            C.Set( 'Geometry', 'id', '@', 'id', jump='geometry')],
    'SetMaterial'        : [C.Meth('Geometry', jump='geometry'),
                            C.Set( 'Geometry', 'material', '@', 'material', jump='geometry')],
    'SetMaterialIndex'   : [C.Meth('Geometry', jump='geometry'),
                            C.Set( 'Geometry', 'material_index', '@', 'material_index', jump='geometry')],
    'SetPointRadius'     : [C.Meth('Geometry', 'points', jump='points'),
                            C.Set( 'Geometry', 'point_radius', 'points', 'radius', jump='points')],
    'SetPosition'        : [C.Meth('Geometry', jump='geometry'),
                            C.Set( 'Geometry', 'position', '@', 'position', jump='geometry'),
                            C.Set( 'Geometry', 'offset',   '@', 'offset',   jump='geometry')],
    'SetSelection'       : None,
    'SetShadeSmooth'     : [C.Meth('Geometry', jump='geometry'),
                            C.Set('Geometry', 'shade_smooth', '@', 'shade_smooth', jump='geometry')],
    'SetSplineCyclic'    : [C.Meth('Geometry', jump='geometry'),
                            C.Set( 'Geometry', 'cyclic', '@', 'cyclic', jump='geometry')],
    'SetSplineResolution' : [C.Meth('Geometry', jump='geometry'),
                            C.Set( 'Geometry', 'spline_resolution', '@', 'resolution', jump='geometry')],
    'SetSplineType'      : [C.Meth('Geometry', 'curve', jump='curve'),
                            C.Set( 'Geometry', 'spline_type', 'curve', 'spline_type', jump='geometry')],
    'ShortestEdgePaths'  : [C.Meth('Geometry', None), C.Glob()],
    'SignedDistance'     : None,
    'SimulationInput'    : None,
    'SimulationOutput'   : None,
    'SliceString'        : C.Meth('Str', jump='string'),
    'SortElements'       : C.Meth('Geometry', 'geometry', jump='geometry'),
    'SpecialCharacters'  : [C.Glob(),
                            C.Meth('Str', None),
                            C.Get('Str', 'line_break', None, 'line_break'),
                            C.Get('Str', 'tab',        None, 'tab')],
    'Spiral'             : C.Glob(ret_socket='curve'),
    'SplineLength'       : [C.Meth('Geometry', None), C.Glob()],
    'SplineParameter'    : [C.Meth('Geometry', None), C.Glob()],
    'SplineResolution'   : [C.Get( 'Geometry', '@', None, 'resolution'), C.Glob()],
    'SplitEdges'         : C.Meth('Geometry', 'mesh', jump='mesh'),
    'SplitToInstances'   : C.Meth('Geometry', 'geometry', ret_socket='instances'),
    'Star'               : C.Glob(ret_socket='curve'),
    'StoreNamedAttribute': [C.Meth('Geometry', jump='geometry'),
                            C.Meth('Geometry', jump='geometry', name='store_named_DATA_TYPE', loops=['data_type']),],
    'String'             : None,
    'StringLength'       : C.Get('Str', 'length', 'string', 'length'),
    'StringToCurves'     : C.Meth('Str'),
    'SubdivideCurve'     : C.Meth('Geometry', 'curve',  jump='curve'),
    'SubdivideMesh'      : C.Meth('Geometry', 'mesh',   jump='mesh'),
    'SubdivisionSurface' : C.Meth('Geometry', 'mesh',   jump='mesh'),
    'Switch'             : [C.Meth({'input_type': ()}, 'false', ret_socket='output', tree_type='GeometryNodeTree'),
                            C.Meth('Rgba', 'off', ret_socket='image', tree_type='CompositorNodeTree')],

    'TransformGeometry'  : C.Meth('Geometry',              jump='geometry'),
    'TranslateInstances' : C.Meth('Geometry', 'instances', jump='instances'),
    'Triangulate'        : C.Meth('Geometry', 'mesh',      jump='mesh'),
    'TrimCurve'          : C.Meth('Geometry', 'curve',     jump='curve'),
    'UVSphere'           : C.Glob(ret_socket='mesh'),
    'UVUnwrap'           : C.Meth('Geometry', None, ret_socket='uv'),
    'Value'              : None,
    'ValueToString'      : C.Meth(('Float', 'Int'), 'value', ret_socket='string'),
    'Vector'             : None,
    'VectorCurves'       : C.Meth(('Vect', 'Rot'), 'vector', jump='vector'),
    'VectorMath'         : [C.Glob(name='vOPERATION',  ret_socket='output_socket', loops=['operation']),
                            C.Meth(('Vect', 'Rot'), 'vector', ret_socket='output_socket', name='OPERATION', loops=['operation'])],
    'VectorRotate'       : C.Meth('Vect', jump='vector'), #C.Meth('Vect', ret_socket='vector'),
    'VertexNeighbors'    : [C.Meth('Geometry', None), C.Glob()],
    'VertexOfCorner'     : [C.Meth('Geometry', None), C.Glob()],
    'Viewer'             : [C.Glob(name='viewer', tree_type='GeometryNodeTree'),
                            C.Meth('Geometry', tree_type='GeometryNodeTree'),
                            C.Meth('Geometry', name='viewer_DATA_TYPE', loops=['data_type'], tree_type='GeometryNodeTree'),
                            ],
    'VolumeCube'         : C.Glob(ret_socket='volume'),
    'VolumeToMesh'       : C.Meth('Geometry', 'volume', ret_socket='mesh'),
    'VoronoiTexture'     : C.Glob(ret_socket='distance'),
    'WaveTexture'        : C.Glob(ret_socket='curve'),
    'WhiteNoiseTexture'  : C.Glob(ret_socket='value'),
    '_3DCursor'          : None,
    }

# GeometryNodeViewer
# CompositorNodeViewer


# =============================================================================================================================
# Get the custom functions declared for a node class name

def get_custom(tree_type, class_name, create=False):
    """ Get the custome functions defined for a Node.

    Arguments
    ---------
        - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree')
        - class_name : a node class name
        - create (bool = True) : create the dictionaty entry if if doesn't exist

    Returns
    -------
        - dict
    """

    cm = CUSTOM[tree_type]
    d = cm.get(class_name)
    if d is None and create:
        d = {}
        cm[class_name] = d
    return d

# =============================================================================================================================
# Get the custom properties

def get_cust_props(tree_type):
    return CUST_PROPS[tree_type]

# =============================================================================================================================
# Declare a custom function for a node class name

def add_function(class_name, name,
                 target       = None,  # tuple of / or : None (Global), str or 'SOCKET'
                 self_socket  = None,  # Static if None
                 use_enabled  = False,
                 node_label   = True,
                 node_return  = "node",
                 loops        = None,
                 debug        = None,
                 descr        = None,
                 tree_classes = None,
                 **kwargs):

    """ Declare a custom function for a node class name.

    Can be used to create as many functions as they are possible values for a node parameter.
    For instance, the node Math can give birth to one global function and one method per possible value of the operation parameter:
        - operation = 'SINE' -> sin global function, Float.sin method
        - operation = 'COSINE' -> cos global function, Float.sin method

    When the name of the function depends upon the value of a parameter, use the capitalized named of the parameter in the name.
    For instance:
        - node Math : name = 'OPERATION'
        - node StoreNamedAttribute : name = 'store_named_DATA_TYPE'

    The parameters to loop on are given in the loops argument.

    The following example create the Geometry methods: store_named_float, store_named, vector, store_named_color,...

    ```python
    add_function("StoreNamedAttribute", "store_named_DATA_TYPE", "Geometry",
                 self_socket = 'geometry',
                 use_enabled = True,
                 node_return = "self.jump(node.geometry)",
                 loops       = ['data_type'],
             )
    ```


    Arguments
    ---------
        - class_name  : Node class name
        - name : name of the function to create. Can contain name temps such as func_DATA_TYPE -->  func_float, func_vector, ...
        - target (str = None) : socket class. Global function if None
        - self_socket (str = None) : Node socket to plug self to
        - use_enabled (bool = False) : Get the enabled sockets rather than all the possible sockets
        - node_label (bool = True) : add node_label and node_color arguments
        - node_return (str = "node") : return statement. By default, returns the node. Use node_return = node.output_socket to return the socket
        - loops (list = None) : list of parameters to loop on. One function is created per parameter possible values
        - debug (str = None) : python source code to insert for debug
        - descr (str = None) : description string
        - tree_type (str = "GeoNodes") : str in 'GeoNodes', 'Shader', 'Compositor', 'Texture'
        - kwargs : keys, values for parameter to set

    """

    return

    if tree_classes is None:
        tree_classes = ("GeoNodes", "Shader")
    elif isinstance(tree_classes, str):
        tree_classes = (tree_classes,)

    for tree_class in tree_classes:

        methods = get_custom(constants.TREE_BL_IDS[tree_class], class_name, create=True)

        if name in methods:
            print(f"CAUTION: method {name} added twice for class {class_name}, target: {target}.")

        if loops is not None and target != 'SOCKET':
            for key in loops:
                if key.upper() not in name:
                    raise AttributeError(f"Custom function error: the function name template {name} should contain {key.upper()} for distinct function names with loops {loops}.")

        methods[name] = {
            'target'      : target,
            'self_socket' : self_socket,
            'use_enabled' : use_enabled,
            'node_label'  : node_label,
            'node_return' : node_return,
            'loops'       : [] if loops is None else list(loops),
            'debug'       : debug,
            'descr'       : descr,
            'kwargs'      : {**kwargs},
            'descr'       : descr,
            }

# =============================================================================================================================
# Register a custom property

def add_property(target, name,
                 getter_class = None,
                 setter_class = None,
                 getter       = None,
                 setter       = None,
                 descr        = None,
                 tree_class   = "GeoNodes"):

    return

    cust_props = get_cust_props(constants.TREE_BL_IDS[tree_class])
    cust_props.append({
        'target'       : target,
        'name'         : name,
        'getter_class' : getter_class,
        'setter_class' : setter_class,
        'getter'       : getter,
        'setter'       : setter,
        'descr'        : descr,
        })

    test_prop = TEST_PROPS[constants.TREE_BL_IDS[tree_class]]
    if setter_class is None:
        test_prop[name] = f"a = geo.{name}\n"
    else:
        if getter_class is None:
            test_prop[name] = f"geo.{name} = geo\n"
        else:
            test_prop[name] = f"geo.{name} = geo.{name}\n"



# =============================================================================================================================
# Test the properties

def test_properties(tree_class):
    test_props = TEST_PROPS[constants.TREE_BL_IDS[tree_class]]

    s = f"with {tree_class}('Test properties') as tree:\n"
    s += "    geo = tree.ig\n"
    for prop, line in test_props.items():
        s += f"    {line}\n"

    print(s)

# =============================================================================================================================
# Create the properties

def create_properties(tree_type):

    return

    cust_props = get_cust_props(tree_type)
    tree_dict = constants.tree_dict(tree_type)
    doc = documentation.doc_dict(tree_type)

    set_color = f"node_color=constants.NODE_COLORS['property']"

    for prop in cust_props:
        getter_class = prop['getter_class']
        setter_class = prop['setter_class']

        fget = None
        fset = None

        getter_code = None
        setter_code = None

        name = prop['name']

        if getter_class is not None:
            getter = prop['getter']
            if getter is None:
                getter = f"return self.tree.{getter_class}({set_color}).output_socket"
            getter_code = f"def {name}(self):\n\t{getter}\n"
            fget = utils.compile_f(getter_code, name)

        if setter_class is not None:
            setter = prop['setter']
            if setter is None:
                pyname = doc[setter_class]['pyname']
                setter = f"self.{pyname}(value, {set_color})"
            setter_code = f"def {name}(self, value):\n\t{setter}\n"

            fset = utils.compile_f(setter_code, name)

        the_class = tree_dict[prop['target']]
        setattr(the_class, name, property(fget, fset))

        # ----- Documentation

        documentation.add_property_doc(tree_type, prop['target'], name,
                             attr_type     = 'Properties',
                             getter        = getter_code,
                             setter        = setter_code,
                             getter_node   = getter_class,
                             setter_node   = setter_class,
                             descr         = prop['descr'],
                             )


        if False:
            print("Property", name)
            print("   Getter:\n", f"def {name}(self):\n\t{getter}\n")
            print("   Getter:\n", f"def {name}(self, value):\n\t{setter}\n")
            print()

# =============================================================================================================================
# Maths

for tree_classes in ['GeoNodes', ('Shader', 'Compositor', 'Texture')]:
    if tree_classes == 'GeoNodes':
        targets = ('Float', 'Int', None)
    else:
        targets = ('Float', None)

    add_function("Math", "OPERATION", targets,
                 self_socket  = 'value',
                 use_enabled  = True,
                 node_return  = "node.output_socket",
                 loops        = ['operation'],
                 descr        = "value=self",
                 tree_classes = tree_classes,
                 )

    add_function("MapRange", "map_range", targets,
                     self_socket = None,
                     use_enabled = True,
                     node_return = "node.output_socket",
                     descr       = None,
                     data_type   = 'FLOAT',
                 )

add_function("MapRange", "map_range", 'Vect',
                 self_socket = None,
                 use_enabled = True,
                 node_return = "node.output_socket",
                 descr       = None,
                 data_type   = 'FLOAT_VECTOR',
             )



add_function("VectorMath", "OPERATION", 'Vect',
             self_socket = 'vector',
             use_enabled = True,
             node_return = "node.output_socket",
             loops       = ['operation'],
             descr       = "vector=self",
             )

add_function("BooleanMath", "OPERATION", ('Bool', None),
             self_socket = 'boolean',
             use_enabled = True,
             node_return = "node.boolean",
             loops       = ['operation'],
             descr       = "boolean=self",
             )

add_function("Mix", "mix_BLEND_TYPE", 'Col',
                 self_socket = 'a',
                 use_enabled = True,
                 node_return = "node.result",
                 loops       = ['blend_type'],
                 data_type   = 'RGBA',
                 descr       = "a=self",
                 )

add_function("Mix", "mix", 'SOCKET',
                 self_socket = 'a',
                 use_enabled = True,
                 node_return = "node.result",
                 loops       = ['data_type'],
                 descr       = "a=self",
                 )

add_function("Compare", "OPERATION", 'SOCKET',
                 self_socket = 'a',
                 use_enabled = True,
                 node_return = "node.result",
                 loops       = ['data_type', 'operation'],
                 descr       = "a=self",
                 )

add_function("Switch", "switch", 'SOCKET',
                 self_socket = 'false',
                 use_enabled = True,
                 node_return = "node.output",
                 loops       = ['input_type'],
                 descr       = "false=self",
             )

add_function("RandomValue", "random_DATA_TYPE", None,
                 self_socket = None,
                 use_enabled = True,
                 node_return = "node.value",
                 loops       = ['data_type'],
                 descr       = None,
             )

# =============================================================================================================================
# Named attributes

add_function("StoreNamedAttribute", "store_named_DATA_TYPE", "Geometry",
             self_socket = 'geometry',
             use_enabled = True,
             node_return = "self.jump(node.geometry)",
             loops       = ['data_type'],
             )

add_function("NamedAttribute", "named_DATA_TYPE", None,
             self_socket = None,
             node_return = "node.attribute",
             loops       = ['data_type'],
             )

add_function("CaptureAttribute", "capture_DATA_TYPE", "Geometry",
             self_socket = 'geometry',
             use_enabled = True,
             node_return = "self.jump(node.geometry).node.attribute",
             loops       = ['data_type'],
             )


# =============================================================================================================================
# Mesh Boolean

add_function("MeshBoolean", "difference", "Geometry",
             self_socket = 'mesh_1',
             use_enabled = True,
             node_return = "node.mesh",
             operation   = 'DIFFERENCE',
             descr       = "mesh_1=self, mesh_2=args",
             )

add_function("MeshBoolean", "intersect", "Geometry",
             self_socket = 'mesh_2',
             use_enabled = True,
             node_return = "node.mesh",
             operation   = 'INTERSECT',
             descr       = "mesh=geometry + args",
             )

add_function("MeshBoolean", "union", "Geometry",
             self_socket = 'mesh_2',
             use_enabled = True,
             node_return = "node.mesh",
             operation   = 'UNION',
             descr       = "mesh=geometry + args",
             )


# =============================================================================================================================
# Geometry methods

add_function("SampleIndex", "sample_index_DATA_TYPE", "Geometry",
             self_socket = 'geometry',
             use_enabled = True,
             node_return = "node.output_socket",
             loops       = ['data_type'],
             )

# =============================================================================================================================
# Shader nodes

add_function("CombineColor", "combine_MODE", None,
             self_socket = None,
             use_enabled = True,
             node_return = "node.output_socket",
             loops       = ['mode'],
             )

add_function("SeparateColor", "separate_MODE", None,
             self_socket = None,
             use_enabled = True,
             node_return = "node",
             loops       = ['mode'],
             descr       = None,
             )


# =============================================================================================================================
# Properties

prop_color = f"node_color={constants.NODE_COLORS['property']}"


# -----------------------------------------------------------------------------------------------------------------------------
# Base types

add_property('Vect', 'xyz',
             getter_class = 'SeparateXYZ',
             setter_class = 'CombineXYZ',
             getter       = f"return self.separate_xyz({prop_color})",
             setter       = f"self.jump(self.tree.CombineXYZ(*value, {prop_color}).vector if hasattr(value, '__len__') else self.tree.CombineXYZ(value, value, value, {prop_color}).vector)"
             )

add_property('Col', 'rgb',
             getter_class = 'SeparateColor',
             setter_class = 'CombineColor',
             getter       = f"return self.tree.separate_rgb()",
             setter       = f"self.jump(self.tree.combine_rgb(*value))",
             )

add_property('Col', 'hsv',
             getter_class = 'SeparateColor',
             setter_class = 'CombineColor',
             getter       = f"return self.tree.separate_hsv()",
             setter       = f"self.jump(self.tree.combine_hsv(*value))",
             )

add_property('Col', 'hsl',
             getter_class = 'SeparateColor',
             setter_class = 'CombineColor',
             getter       = f"return self.tree.separate_hsl()",
             setter       = f"self.jump(self.tree.combine_hsl(*value))",
             )

# -----------------------------------------------------------------------------------------------------------------------------
# Geometry

add_property('Geometry', 'ID',
             getter_class = 'ID',
             setter_class = 'SetID',
             )

add_property('Geometry', 'index',
             getter_class = 'Index',
             )

add_property('Geometry', 'position',
             getter_class = 'Position',
             setter_class = 'SetPosition',
             descr        = f"SetPosition(position=value, {prop_color})",
             )

add_property('Geometry', 'offset',
             setter_class = 'SetPosition',
             setter       = f"self.set_position(offset=value, {prop_color})",
             descr        = "SetPosition(offset=value)",
             )

add_property('Geometry', 'material',
             getter_class = 'Material',
             setter_class = 'SetMaterial',
             )

add_property('Geometry', 'radius',
             getter_class = 'Radius',
             setter_class = 'SetPointRadius',
             getter       = None,
             setter       = f"if self._domain == 'CURVE':\n\t\tself.curve_radius=value\n\telse:\t\tself.point_radius=value\n",
             descr        = "Point radius property",
             )


# -----------------------------------------------------------------------------------------------------------------------------
# Curve

add_property('Geometry', 'spline_cyclic',
             getter_class = 'IsSplineCyclic',
             setter_class = 'SetSplineCyclic',
             )

add_property('Geometry', 'curve_radius',
             getter_class = 'Radius',
             setter_class = 'SetCurveRadius',
             getter       = None,
             setter       = None,
             descr        = "Curve radius property",
             )

add_property('Geometry', 'tangent',
             getter_class = 'CurveTangent',
             )

add_property('Geometry', 'curve_tilt',
             getter_class = 'CurveTilt',
             setter_class = 'SetCurveTilt',
             )

add_property('Geometry', 'spline_resolution',
             getter_class = 'SplineResolution',
             setter_class = 'SetSplineResolution',
             )

# -----------------------------------------------------------------------------------------------------------------------------
# Mesh

add_property('Geometry', 'shade_smooth',
             getter_class = 'IsFaceSmooth',
             setter_class = 'SetSmooth',
             getter       = f"return self.tree.is_edge_smooth({prop_color}) if self._domain == 'EDGE' else self.tree.is_face_smooth({prop_color})",
             #setter       = "self.set_shade_smooth(value, domain=self._get_domain('FACE'))",
             setter       = f"self.set_shade_smooth(value, domain='EDGE' if self._domain == 'EDGE' else 'FACE', {prop_color})",
             descr        = "SetShadeSmooth()",
             )

add_property('Geometry', 'face_area',
             getter_class = 'FaceArea',
             )

add_property('Geometry', 'edge_neighbors',
             getter_class = 'EdgeNeighbors',
             )

add_property('Geometry', 'normal',
             getter_class = 'Normal',
             )

# -----------------------------------------------------------------------------------------------------------------------------
# Points

add_property('Geometry', 'point_radius',
             getter_class = 'Radius',
             setter_class = 'SetPointRadius',
             getter       = None,
             setter       = None,
             descr        = "Point radius property",
             )
