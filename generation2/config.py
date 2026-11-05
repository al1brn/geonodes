"""Explicit exceptions to the generation rules.

All dictionaries use Blender bl_idname keys so homonymous UI node names stay
distinct. Each key line includes the UI name as a comment for manual editing.
Shared nodes are declared only once, without branches by tree type.
Keep general inference rules in NodeInfo and document individual exceptions
here. Deprecated nodes are excluded before introspection; nodes without a
default implementation remain available for introspection and nd access.
"""


DEPRECATED_NODES = {
    'FunctionNodeAlignEulerToVector': 'Use Align Rotation to Vector',  # Align Euler to Vector
    'FunctionNodeRotateEuler': 'Use Rotate Rotation',  # Rotate Euler
}


NO_DEFAULT_IMPLEMENTATION_DEPRECATED = {
    'GeometryNodeMenuSwitch': 'Use the handwritten Socket.MenuSwitch and menu_switch methods',  # Menu Switch
    'FunctionNodeCompare': 'Typed comparisons and environment-specific Float.compare provide the implementations',  # Compare
    'NodeGroupInput': 'Group interface input',  # Group Input
    'NodeGroupOutput': 'Group interface output',  # Group Output
    'GeometryNodeBake': 'Bake with dynamic items; requires a dedicated implementation',  # Bake
    'GeometryNodeViewer': 'Viewer with dynamic items; requires a dedicated implementation',  # Viewer
    'GeometryNodeRepeatInput': 'Repeat zone input',  # Repeat Input
    'GeometryNodeRepeatOutput': 'Repeat zone output',  # Repeat Output
    'GeometryNodeSimulationInput': 'Simulation zone input',  # Simulation Input
    'GeometryNodeSimulationOutput': 'Simulation zone output',  # Simulation Output
    'GeometryNodeForeachGeometryElementInput': 'For Each Geometry Element zone input',  # For Each Geometry Element Input
    'GeometryNodeForeachGeometryElementOutput': 'For Each Geometry Element zone output',  # For Each Geometry Element Output
    'NodeClosureInput': 'Closure zone input',  # Closure Input
    'NodeClosureOutput': 'Closure zone output',  # Closure Output
}


# Handwritten APIs registered for documentation without emitting their source.
HANDWRITTEN_IMPLEMENTATIONS = {
    'GeometryNodeIndexSwitch': {'Socket': ('index_switch',)},
    'GeometryNodeMenuSwitch': {'Socket': ('MenuSwitch', 'menu_switch')},
}


# Per-node replacements for default-implementation descriptors. Individual
# cases will be specified here rather than hard-coded in the inference rules.
# param_loop expands a proposal for each valid enum value. The constructor's
# class is inferred from the first output in that configuration.
# self_socket chooses an input by identifier or UI name instead of the first
# input; a METHOD override keeps the proposal as a method even without free args.
REPLACE_DEFAULT_IMPLEMENTATIONS = {
    # Rotate Vector: the Rotation is the receiver, leaving Vector.rotate to Vector Rotate.
    'FunctionNodeRotateVector': {
        'kind': 'METHOD',
        'name': 'rotate_vector',
        'self_socket': 'Rotation',
    },
    # Find in String
    'FunctionNodeFindInString': {  
        'name': 'find',
    },
    # Combine List
    'GeometryNodeCombineList': {  
        'kind': 'CONSTRUCTOR',
        'name': 'CombineList',
        'param_loop': 'data_type',
    },
    # Closure to List
    'GeometryNodeClosureToList': {  
        'kind': 'METHOD',
        'name': 'to_list',
        'self_socket': 'Closure',
    },
    # Collection Info
    'GeometryNodeCollectionInfo': {  
        'kind': 'CONSTRUCTOR',
    },
}


# Exceptions to the input/output data-type rule. Ordinary nodes use their
# first input: Geometry -> instance method; typed first input/output -> typed
# instance methods; otherwise one class method per type.
# Random's Min/Max inputs are absent for Boolean, so its output selects the class.
DATA_TYPE_IMPLEMENTATIONS = {
    'NodeEnableOutput': {  # Enable Output: Value is self; Enable stays an argument.
        'kind': 'METHOD',
        'self_socket': 'Value',
        'param_loop': 'data_type',
    },
    'FunctionNodeRandomValue': {  # Random Value
        'kind': 'CONSTRUCTOR',
        'name': 'Random',
        'class_from': 'OUTPUT',
    },
    'GeometryNodeSwitch': {'kind': 'DEFAULT'},  # Legacy generation only.
}


# Extra proposals, without replacing the inferred/default implementation.
# Each node may have several additions, using the same keys as replacements.
ADDITIONAL_IMPLEMENTATIONS = {
    # Collection Info
    'GeometryNodeCollectionInfo': [  
        {
            'kind': 'METHOD',
            'name': 'info',
            'self_socket': 'Collection',
        },
    ],
}


# Overrides/additions to NodeInfo.input_implementation's domain/name rules.
# Unmatched INPUTs need an explicit class_name. name=None disables the Node
# method; otherwise name creates a class
# method returning the Node. create_properties defaults to True: each output
# becomes a snake_case class property only if there are no active inputs or free
# parameters. False disables properties. parameters fixes node parameters.
# property_names optionally renames generated Python names, e.g.
# {'unsigned_angle': 'unsigned_edge_angle'}; None excludes a property.
# Other properties keep their names.
INPUT_IMPLEMENTATIONS = {
    # Spline Parameter: Spline.length is provided by Spline Length.
    'GeometryNodeSplineParameter': {
        'property_names': {'length': None},
    },
    # Edge Angle
    'GeometryNodeInputMeshEdgeAngle': {
        'class_name': 'Edge',
        'name': 'angle',
        'create_properties': True,
        'property_names': {},
    },
}


# Implements __getitem__ __setitem__
ITEM_IMPLEMENTATION = {
    #'Get Bundle Item': {'kind': 'get'},
    'Store Bundle Item': {'kind': 'set'},
}

# Instance properties: target class -> property name -> getter/setter node descriptions.
# Missing getter means write-only. Each part accepts parameters and fixed sockets.
PROPERTIES = {
    'ShaderNodeTree': {},
    
    'GeometryNodeTree': {

    'Geometry': {'position': {'setter': {'node': 'Set Position', 'socket': 'Position'},
                        'getter': {'node': 'Position'}},
            'bundle': {'getter': {'node': 'Get Geometry Bundle', 'output': 'Bundle',
                                    'sockets': {'Remove': False}},
                        'setter': {'node': 'Set Geometry Bundle', 'socket': 'Bundle'}},
            'offset': {'setter': {'node': 'Set Position', 'socket': 'Offset'}},
            'id': {'setter': {'node': 'Set ID', 'socket': 'ID'}, 'getter': {'node': 'ID'}},
            'material': {'setter': {'node': 'Set Material', 'socket': 'Material'}},
            'name': {'setter': {'node': 'Set Geometry Name', 'socket': 'Name'}}},

    'Point': {'position': {'setter': {'node': 'Set Position', 'socket': 'Position'},
                            'getter': {'node': 'Position'}},
            'offset': {'setter': {'node': 'Set Position', 'socket': 'Offset'}},
            'normal': {'setter': {'node': 'Set Mesh Normal',
                                    'socket': 'Custom Normal',
                                    'parameters': {'mode': 'FREE', 'domain': 'POINT'}}}},
    'Face': {'material': {'setter': {'node': 'Set Material', 'socket': 'Material'}},
             
            'material_index': {'setter': {'node': 'Set Material Index', 'socket': 'Material Index'},
                                'getter': {'node': 'Material Index'}},
            'shade_smooth': {'setter': {'node': 'Set Shade Smooth',
                                        'socket': 'Shade Smooth',
                                        'parameters': {'domain': 'FACE'}},
                            'getter': {'node': 'Is Face Smooth'}},
            'smooth': {'setter': {'node': 'Set Shade Smooth',
                                    'socket': 'Shade Smooth',
                                    'parameters': {'domain': 'FACE'}},
                        'getter': {'node': 'Is Face Smooth'}},
            'normal': {'setter': {'node': 'Set Mesh Normal',
                                    'socket': 'Custom Normal',
                                    'parameters': {'mode': 'FREE', 'domain': 'FACE'}}}},

    'Edge': {'material': {'setter': {'node': 'Set Material', 'socket': 'Material'}},
            'shade_smooth': {'setter': {'node': 'Set Shade Smooth',
                                        'socket': 'Shade Smooth',
                                        'parameters': {'domain': 'EDGE'}},
                            'getter': {'node': 'Is Edge Smooth'}},
            'smooth': {'setter': {'node': 'Set Shade Smooth',
                                    'socket': 'Shade Smooth',
                                    'parameters': {'domain': 'EDGE'}},
                        'getter': {'node': 'Is Edge Smooth'}}},

    'Mesh': {'material_index': {'setter': {'node': 'Set Material Index', 'socket': 'Material Index'},
                                'getter': {'node': 'Material Index'}},
            'normal': {'setter': {'node': 'Set Mesh Normal',
                                    'socket': 'Custom Normal',
                                    'parameters': {'mode': 'FREE', 'domain': 'POINT'}}}},

    'Spline': {'material_index': {'setter': {'node': 'Set Material Index', 'socket': 'Material Index'},
                                'getter': {'node': 'Material Index'}},
                'tilt': {'setter': {'node': 'Set Curve Tilt', 'socket': 'Tilt'},
                        'getter': {'node': 'Curve Tilt'}},
                'normal': {'setter': {'node': 'Set Curve Normal',
                                    'socket': 'Normal',
                                    'sockets': {'Mode': 'Free'}}},
                'is_cyclic': {'setter': {'node': 'Set Spline Cyclic', 'socket': 'Cyclic'},
                            'getter': {'node': 'Is Spline Cyclic'}},
                'resolution': {'setter': {'node': 'Set Spline Resolution', 'socket': 'Resolution'},
                            'getter': {'node': 'Spline Resolution'}},
                'type': {'setter': {'node': 'Set Spline Type', 'parameter': 'spline_type'}}},

    'Cloud': {'radius': {'setter': {'node': 'Set Point Radius', 'socket': 'Radius'},
                        'getter': {'node': 'Radius'}}},

    'CloudPoint': {'radius': {'setter': {'node': 'Set Point Radius', 'socket': 'Radius'},
                            'getter': {'node': 'Radius'}}},

    'Curve': {'radius': {'setter': {'node': 'Set Curve Radius', 'socket': 'Radius'},
                        'getter': {'node': 'Radius'}},
            'left_handle_position': {'setter': {'node': 'Set Handle Positions',
                                                'socket': 'Position',
                                                'parameters': {'mode': 'LEFT'}},
                                        'getter': {'node': 'Curve Handle Positions',
                                                'output': 'Left',
                                                'sockets': {'Relative': False}}},
            'left_handle_offset': {'setter': {'node': 'Set Handle Positions',
                                                'socket': 'Offset',
                                                'parameters': {'mode': 'LEFT'}},
                                    'getter': {'node': 'Curve Handle Positions',
                                                'output': 'Left',
                                                'sockets': {'Relative': True}}},
            'right_handle_position': {'setter': {'node': 'Set Handle Positions',
                                                    'socket': 'Position',
                                                    'parameters': {'mode': 'RIGHT'}},
                                        'getter': {'node': 'Curve Handle Positions',
                                                    'output': 'Right',
                                                    'sockets': {'Relative': False}}},
            'right_handle_offset': {'setter': {'node': 'Set Handle Positions',
                                                'socket': 'Offset',
                                                'parameters': {'mode': 'RIGHT'}},
                                    'getter': {'node': 'Curve Handle Positions',
                                                'output': 'Right',
                                                'sockets': {'Relative': True}}},
            'handle_type': {'setter': {'node': 'Set Handle Type',
                                        'parameter': 'handle_type',
                                        'parameters': {'mode': {'LEFT', 'RIGHT'}}}},
            'left_handle_type': {'setter': {'node': 'Set Handle Type',
                                            'parameter': 'handle_type',
                                            'parameters': {'mode': {'LEFT'}}}},
            'right_handle_type': {'setter': {'node': 'Set Handle Type',
                                                'parameter': 'handle_type',
                                                'parameters': {'mode': {'RIGHT'}}}},
            'tilt': {'setter': {'node': 'Set Curve Tilt', 'socket': 'Tilt'}, 'getter': {'node': 'Curve Tilt'}},
            'normal': {'setter': {'node': 'Set Curve Normal',
                                    'socket': 'Normal',
                                    'sockets': {'Mode': 'Free'}}},
            'is_cyclic': {'setter': {'node': 'Set Spline Cyclic', 'socket': 'Cyclic'},
                            'getter': {'node': 'Is Spline Cyclic'}},
            'resolution': {'setter': {'node': 'Set Spline Resolution', 'socket': 'Resolution'},
                            'getter': {'node': 'Spline Resolution'}},
            'type': {'setter': {'node': 'Set Spline Type', 'parameter': 'spline_type'}}},

    'SplinePoint': {'radius': {'setter': {'node': 'Set Curve Radius', 'socket': 'Radius'},
                                'getter': {'node': 'Radius'}}},

    'Instances': {'transform': {'setter': {'node': 'Set Instance Transform', 'socket': 'Transform'},
                                'getter': {'node': 'Instance Transform'}}},

    'GreasePencil': {'stroke_color': {'setter': {'node': 'Set Grease Pencil Color',
                                                'socket': 'Color',
                                                'sockets': {'Mode': 'Stroke'}}},
                    'fill_color': {'setter': {'node': 'Set Grease Pencil Color',
                                                'socket': 'Color',
                                                'sockets': {'Mode': 'Fill'}}},
                    'depth': {'setter': {'node': 'Set Grease Pencil Depth', 'socket': 'Depth Order'}},
                    'softness': {'setter': {'node': 'Set Grease Pencil Softness', 'socket': 'Softness'}}},

    'Corner': {'normal': {'setter': {'node': 'Set Mesh Normal',
                                    'socket': 'Custom Normal',
                                    'parameters': {'mode': 'FREE', 'domain': 'CORNER'}}}}}
}



# ---------------------------------------------------------------------------
# The following nodes are ignored by get_node_implementation
# ---------------------------------------------------------------------------

STATIC_IMPLEMENTATION_ONLY = [

    # Manual implementation

    'GeometryNodeBake',
    'GeometryNodeViewer',
    'NodeGroupInput',
    'NodeGroupOutput',
    'GeometryNodeRepeatInput',
    'GeometryNodeRepeatOutput',
    'GeometryNodeSimulationInput',
    'GeometryNodeSimulationOutput',
    'GeometryNodeForeachGeometryElementInput',
    'GeometryNodeForeachGeometryElementOutput',
    'NodeFrame',
    'NodeReroute',
    'NodeComment',
    'NodeClosureInput',
    'NodeClosureOutput',
    'GeometryNodeGroup',

    # The following nodes are used as Socket constructors

    'FunctionNodeInputBool',
    'GeometryNodeInputCollection',
    'FunctionNodeInputColor',
    'GeometryNodeInputFont',
    'GeometryNodeInputImage',
    'FunctionNodeInputInt',
    'FunctionNodeInputIntVector',
    'GeometryNodeInputMaterial',
    'FunctionNodeInputMenu',
    'GeometryNodeInputObject',
    'FunctionNodeInputRotation',
    'FunctionNodeInputString',
    'ShaderNodeValue',
    'FunctionNodeInputVector',

    # Shader nodes that are interpreted as class properties

    'ShaderNodeHairInfo',
    'ShaderNodePointInfo',

    ]


DOMAINS = ['Point', 'Edge', 'Corner', 'Face', 'Curve', 'Vertex', 'Vertices', 'Instance', 'Spline']

DOMAIN_NAME = {
    'Vertex': 'Vertex',
    'Vertices': 'Vertex',
}

SPECIAL_NODES = {

    # Input Nodes
    
    'Offset Corner in Face' : {
        'class_name': "Face",
        'method_name' : "offset_corner"
        },
    'Offset Point in Curve' : {
        'class_name': ("Curve", "Spline"),
        'method_name': "offset_point",
        },
    'Shortest Edge Paths' : {
        'class_name': "Edge",
        'method_name': "shortest_paths",
        },
    'NURBS Order' : {
        'class_name': "Curve",
        'method_name': "nurbs_order",
        },
    'NURBS Weight' : {
        'class_name': "Curve",
        'method_name': "nurbs_weight",
        },
    'Named Layer Selection' : {
        'class_name': ("GreasePencil", "Layer"),
        'method_name': "named_selection",
        },
    'Mesh Island' : {
        'class_name': "Mesh",
        'method_name': "island",
        },
    'Import Text': {
        'class_name': "String",
        'method_name': "ImportText",
        },
    'Handle Type Selection' : {
        'class_name': "SplinePoint",
        'method_name': "handle_type_selection",
        },
        
    # Geometry nodes

    'Separate Geometry': {
        'jump': False,
        },
    'Distribute Points on Faces': {
        'method_name': 'distribute_points',
        },
    'Mesh Boolean': {
        'class_name': 'Mesh',
        'method_name': 'Boolean',
        },
        
    # Geometry output nodes
    
    'Grid to Mesh': {
        'method_name': 'FromGrid',
        },
    'Grid to Points': {
        'method_name': 'FromGrid',
        },

    # Grid

    'Align Rotation to Vector': {
        'method_name': 'align_to_vector',
    },
    'Blackbody': {
        'class_name': 'Color',
        'method_name': 'Blackbody',
        'is_class_method': True,
    }
}
