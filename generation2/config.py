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

# Do not generate static code for these nodes
# Note : theses nodes are also excluded from default_implementation
NO_STATIC_CODE = [
    'GeometryNodeForeachGeometryElementInput',
    'GeometryNodeForeachGeometryElementOutput',
    'GeometryNodeSimulationInput',
    'GeometryNodeSimulationOutput',
    'GeometryNodeRepeatInput',
    'GeometryNodeRepeatOutput',
    'NodeReroute',
    'GeometryNodeGroup',
    'NodeGroupInput',
    'NodeGroupOutput',
]

# Adjustements for static implementations
STATIC_IMPLEMENTATIONS = {

    'Get Bundle Item': {
        'method_name': 'get_item',
        'is_jump': True,
        'return_socket': 'Item',
    },
    'Store Bundle Item': {
        'method_name': 'set_item',
        'is_jump': True,
    },
    'Switch': {
        'is_jump': True,
    },
    'Normal': {
        'method_type': 'CLASS_PROPERTY',
        'method_name': ['normal', 'true_normal'],
        'return_socket': ['Normal', 'True Normal'],
    },    
}

# Handwritten APIs registered for documentation without emitting their source.
HANDWRITTEN_IMPLEMENTATIONS = {
    #'GeometryNodeIndexSwitch': {'Socket': ('index_switch',)},
    #'GeometryNodeMenuSwitch': {'Socket': ('MenuSwitch', 'menu_switch')},
}


# Adjustments to NodeImplementation.get_default_node_calls.
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

    'Domain Size': {
        'class_name': ['Geometry', 'Mesh', 'Cloud', 'Curve', 'Instances', 'GreasePencil'],
        'parameters': {'component': ADD_LOOP},
        'return_kind': 'NODE',
    },
    'Separate Geometry': {
        'is_jump': False,
        'return_kind' : 'cls',
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
    'Realize Instances': {
        'method_name': 'realize',
        'is_jump': False,
    },
    'Separate Components': {
        'return_kind': 'NODE',
    },
    'Instance on Points': {
        'class_name': 'Geometry',
    },
    'Mesh to Points': {
        'class_name': ['Geometry', 'Vertex', 'Edge', 'Face', 'Corner'],
        'parameters' : {'mode': ADD_LOOP},
    },
    'Geometry Proximity': {
        'class_name': 'Geometry',
        'parameters' : {'target_element': ADD_LOOP},
        'method_name' : f"proximity_{REPLACE}",
    },
    'Trim Curve': {
        'parameters' : {'mode': ADD_LOOP},
        'method_name' : f"trim_{REPLACE}",
    },
    'Capture Attribute' : {
        'return_kind' : 'SECOND_OUT',
    },
    'Extrude Mesh' : {
        'class_name' : ['Mesh', 'Vertex', 'Edge', 'Face'],
        'parameters' : {'mode': ADD_LOOP},
    },
    'Remove Named Attribute': {
        'method_name' : ['remove', 'remove_named_attribute'],
    },
    'String to Curves': { # First output is geo -> Instances.CurvesFromSring
        'method_type' : 'METHOD',
        'class_name': 'String',
        'method_name': 'to_curves',
        'self_socket' : 'String',
    }, 
        
    # Geometry output nodes
    
    'Grid to Mesh': {
        'method_name': 'FromGrid',
        },
    'Grid to Points': {
        'method_name': 'FromGrid',
        },

    # Other

    'Align Rotation to Vector': {
        'method_name': 'align_to_vector',
    },

    'Rotate Vector': {
        'method_name' : ['rotate', 'rotate_vector'],
        'class_name': ['Vector', 'Rotation'],
        'self_socket' : ['Vector', 'Rotation'],
    },
    #'Invert Matrix': {
    #    'method_name': 'invert',
    #},

    'Blackbody': {
        'class_name': 'Color',
        'method_name': 'Blackbody',
        'method_type': 'CLASS_METHOD',
    },

    # Random Value
    'Random Value': {
        'method_type' : 'CLASS_METHOD',
        'method_name' : 'Random',
        'self_socket' : None,
        'is_jump'     : False,
    },

    #
    'Warning': {
        'method_name': REPLACE,
        'parameters': {'warning_type': LOOP_ONLY},
    },    

}



# Extra proposals, without replacing the inferred/default implementation.
# Each node may have several additions, using the same keys as replacements.
ADDITIONAL_IMPLEMENTATIONS = {
    'common': {
        'Map Range': {
                'method_type': 'METHOD',
                'class_name': None,
                'method_name' : 'interpolate',
                'fixed_sockets': {'From Min': 0.0, 'From Max': 1.0, 'Steps': None},
                'parameters': {'data_type': LOOP_ONLY},
            },
        'Switch': [{
                'method_type': 'METHOD',
                'class_name': None,
                'method_name': 'switch_false',
                'self_socket': 'True',
                'is_jump' : True,
                'parameters': {'input_type': LOOP_ONLY}
        }, {
                'method_type': 'CLASS_METHOD',
                'class_name': None,
                'method_name': 'Switch',
                'return_kind': 'cls',
                'parameters': {'input_type': LOOP_ONLY}
        }],
        'Special Characters': {
            'method_type': 'CLASS_PROPERTY',
            'class_name': 'String',
            'method_name': ['line_break', 'tab'],
            'return_socket': ['Line Break', 'Tab'],
        },        
    },
    'ShaderNodeTree': {
    },
    'GeometryNodeTree': {
        'Align Rotation to Vector': {
            'method_type' : 'METHOD',
            'class_name' : 'Rotation',
            'self_socket' : 'Rotation',
            'method_name' : f"align_{REPLACE}_to_vector",
            'parameters' : {'axis': ADD_LOOP},
        },
    'Store Named Attribute' : {
        'method_type' : 'METHOD',
        'class_name' : 'Corner',
        'method_name' : 'store_uv',
        'self_socket' : 'Geometry',
        'is_jump' : True,
        'parameters' : {'data_type': 'FLOAT2', 'domain': 'CORNER'},
        },
    'Separate Components': {
        'class_name': 'Geometry',
        'method_type': 'METHOD',
        'self_socket': 'Geometry',
        'method_name': [
            'separate_mesh',
            'separate_curve',
            'separate_point_cloud',
            'separate_instances',
            'separate_volume',
            'separate_grease_pencil',
        ],
        'return_socket': [
            'Mesh',
            'Curve',
            'Point Cloud',
            'Instances',
            'Volume',
            'Grease Pencil',
        ],
        'is_jump': False,
        },        
    },
}

# Implements __getitem__ __setitem__
ITEM_IMPLEMENTATION = {
    #'Get Bundle Item': {'kind': 'get'},
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
    'ShaderNodeAmbientOcclusion',          # Ambient Occlusion
    'ShaderNodeAttribute',                 # Attribute
    'ShaderNodeBevel',                     # Bevel
    'ShaderNodeCameraData',                # Camera Data
    'ShaderNodeRGB',                       # Color
    'ShaderNodeVertexColor',               # Color Attribute
    'ShaderNodeFresnel',                   # Fresnel
    'ShaderNodeNewGeometry',               # Geometry
    'ShaderNodeLayerWeight',               # Layer Weight
    'ShaderNodeLightEvaluation',           # Light Evaluation
    'ShaderNodeLightInfo',                 # Light Info
    'ShaderNodeLightPath',                 # Light Path
    'ShaderNodeObjectInfo',                # Object Info
    'ShaderNodeParticleInfo',              # Particle Info
    'ShaderNodeRaycast',                   # Raycast
    'ShaderNodeShadowRaycast',             # Shadow Raycast
    'ShaderNodeTangent',                   # Tangent
    'ShaderNodeTexCoord',                  # Texture Coordinate
    'ShaderNodeUVAlongStroke',             # UV Along Stroke
    'ShaderNodeUVMap',                     # UV Map
    'ShaderNodeVolumeInfo',                # Volume Info
    'ShaderNodeWireframe',                 # Wireframe

    # Shader nodes that are interpreted as class properties

    'ShaderNodeHairInfo',
    'ShaderNodePointInfo',

    # Special

    'ShaderNodeMix',

    ]

