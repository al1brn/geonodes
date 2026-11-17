# Key words with space to avoid match with a true parrameter value
ADD_LOOP = 'ADD LOOP'       # sample(..., mode=...), sample_factor(...), sample_length(...) for instance
LOOP_ONLY = 'LOOP ONLY'     # sample_factor(...), sample_length(...) 
REPLACE = 'REPLACE'         # "sample_REPLACE"

# Generation configuration

DOMAINS = ['Point', 'Edge', 'Corner', 'Face', 'Curve', 'Vertex', 'Vertices', 'Instance', 'Spline']
DOMAIN_NAME = {
    'Vertex': 'Vertex',
    'Vertices': 'Vertex',
}


# Nodes with dynamic inputs accepting dynamic inputs
AUTO_INPUT_TYPE_NODES = [
    'GeometryNodeMenuSwitch',
    'GeometryNodeIndexSwitch',
    'GeometryNodeSwitch',    
]

DEPRECATED_NODES = {
    'FunctionNodeAlignEulerToVector': 'Use Align Rotation to Vector',  # Align Euler to Vector
    'FunctionNodeRotateEuler': 'Use Rotate Rotation',  # Rotate Euler
    'FunctionNodeInputIntVector': 'Integer Vector', # Future versions ???
}

# Handwritten APIs registered for documentation without emitting their source.
HANDWRITTEN_IMPLEMENTATIONS = {
    'GeometryNodeIndexSwitch': {'Socket': ('index_switch',)},
    'GeometryNodeMenuSwitch': {'Socket': ('MenuSwitch', 'menu_switch')},
}


# ====================================================================================================
# Adjustments for algorithm operated by NodeImplementation.get_default_implementation
# ====================================================================================================

REPLACE_DEFAULT_IMPLEMENTATIONS_DEPR = {
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

# ====================================================================================================
# Adjustments for algorithm operated by NodeImplementation.get_default_implementation
# ====================================================================================================

DEFAULT_IMPLEMENTATION = {

    # Input Nodes
    
    'Offset Corner in Face' : {
        'class_name': "Face",
        'method_name' : "offset_corner"
        },
    'Offset Point in Curve' : {
        'class_name': ["Curve", "Spline"],
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
        'class_name': ["GreasePencil", "Layer"],
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
        'is_jump': False,
        },
    'Distribute Points on Faces': {
        'method_name': 'distribute_points',
        },
    'Mesh Boolean': {
        'class_name': 'Mesh',
        'method_name': 'Boolean',
        },
    'Sample Curve': {
        'parameters': {'mode': ADD_LOOP},
        'method_name': f"sample_{REPLACE}",
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
        'method_type': 'CLASS_METHOD',
    },

    # Random Value
    'Random Value': {
        'method_type' : 'CLASS_METHOD',
        'self_socket' : None,
        'is_jump'     : False,
    },

    # Combine List
    #'Combine List': {
    #    'parameters' : LOOP_ONLY,
    #},

    #'Menu Switch': {
    #    'last_sockets': ('Menu',),
    #}

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
    'common': {
        'Map Range': {
                'method_type': 'METHOD',
                'class_name': 'LOOP data_type',
                'method_name' : 'interpolate_NEW',
                'fixed_sockets': {'From Min': 0.0, 'From Max': 1.0},
            },
        'Switch': {
                'method_type': 'METHOD',
                'class_name': 'LOOP input_type',
                'method_name': 'switch_false',
                'self_socket': 'True',
        },
    },
    'ShaderNodeTree': {
    },
    'GeometryNodeTree': {
        'Sample Curve' : [{
            'class_name'  : 'Curve',
            'method_type' : 'METHOD',
            'method_name' : 'sample_factor',
            'self_socket' : 'Curves',
            'is_jump'     : True,
            'parameters'  : {'mode' : 'FACTOR'},
            'auto_data_type'  : 'Value',
        }, {
            'class_name'  : 'Curve',
            'method_type' : 'METHOD',
            'method_name' : 'sample_length',
            'self_socket' : 'Curves',
            'is_jump'     : True,
            'parameters'  : {'mode' : 'LENGTH'},
            'auto_data_type'  : 'Value',
        }],
    }
}

"""
        'Map Range OLD': [{
                'class_name': 'Float',
                'method_name' : 'map_range',
                'parameters': {'data_type': 'FLOAT'},
            }, {
                'class_name': 'Vector',
                'method_name' : 'map_range',
                'parameters': {'data_type': 'VECTOR'},
            }],

"""
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
    'common': {},
    
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
# The following nodes are ignored by get_default_node_calls
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

    # Only static
    'GeometryNodeTool3DCursor',             # 3D Cursor
    'GeometryNodeToolActiveElement',        # Active Element
    'GeometryNodeCubeGridTopology',         # Cube Grid Topology
    'GeometryNodeCurveEndpointSelection',   # Endpoint Selection
    'GeometryNodeInputID',                  # ID
    'GeometryNodeInputIndex',               # Index
    'GeometryNodeIsViewport',               # Is Viewport
    'GeometryNodeInputMaterialIndex',       # Material Index
    'GeometryNodeToolMousePosition',        # Mouse Position
    'GeometryNodeInputNamedAttribute',      # Named Attribute
    'GeometryNodeInputNormal',              # Normal
    'GeometryNodeInputPosition',            # Position
    'GeometryNodeInputRadius',              # Radius
    'GeometryNodeInputSceneTime',           # Scene Time
    'GeometryNodeToolSelection',            # Selection
    'FunctionNodeInputSpecialCharacters',   # Special Characters
    'GeometryNodeUVTangent',                # UV Tangent
    'GeometryNodeViewportTransform',        # Viewport Transform
    'GeometryNodeInputVoxelIndex',          # Voxel Index

    # Shader nodes that are interpreted as class properties

    'ShaderNodeHairInfo',
    'ShaderNodePointInfo',

    # Special

    'ShaderNodeMix',

    ]

