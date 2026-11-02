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


NO_DEFAULT_IMPLEMENTATION = {
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
    'GeometryNodeSwitch': {'kind': 'DEFAULT'},  # Switch: handled separately later
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
