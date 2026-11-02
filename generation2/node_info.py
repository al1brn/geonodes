"""Node introspection.

TEMPORARY HACK: ShaderNodeOutputLineStyle (Line Style Output) IS NOT PROCESSED.
Its target enum becomes invalid during parameter exploration and floods the
console with RNA warnings. NodeInfo.loop_on_nodes skips it before creating
the wrapper. This exclusion applies to all NodeInfo-based exploration.
Revisit this exclusion after investigating the Blender RNA behavior.
"""

import bpy
import re
from itertools import combinations
from time import perf_counter

from .. import core_module
from . import config, utils
from .node_param import NodeParam
from .node_socket import NodeSocket


class NodeInfo:
    STD_ATTRS = None
    def __init__(self, btree, bnode):
        self.btree = btree
        self.bnode = bnode
        self.inputs = {}
        self.outputs = {}
        self.max_inputs = []
        self.max_outputs = []
        self.param_dependencies = {}
        self.enum_parameters = ()
        self.driving_parameters = ()
        self.configurations = ()
        self.default_implementation_time = 0.0

        self.get_std_attrs()

        #print("DEBUG", self.bnode.name)

        self.get_param_dependencies()

    @classmethod
    def get_std_attrs(cls):
        """Return the standard node attributes, initializing them once."""
        if cls.STD_ATTRS is None:
            cls.STD_ATTRS = set(dir(bpy.types.Node))
            cls.STD_ATTRS.update(bpy.types.Node.bl_rna.properties.keys())
            cls.STD_ATTRS.update((
                'active_item', 'active_index',
                'active_input_index', 'active_output_index',
                'active_generation_index', 'active_main_index',
                'inspection_index', 'ui_shortcut',
                'use_legacy_normal', 'legacy_corner_normals',
            ))
        return cls.STD_ATTRS

    def set_params(self, **params):
        """Set the supplied parameters, leaving other parameters unchanged."""
        for name, value in params.items():
            if getattr(self.bnode, name) != value:
                setattr(self.bnode, name, value)

    def snapshot_params(self):
        """Return parameter values and enum choices in the node's current state."""
        params = {}
        standard = self.get_std_attrs()
        for prop in self.bnode.bl_rna.properties:
            name = prop.identifier
            if name in standard or prop.is_readonly or name.endswith('_items'):
                continue

            param = NodeParam.Parameter(self.bnode, name)
            if param is not None:
                params[name] = {
                    'type': param.param_type,
                    'value': param.value,
                    'enums': param.enums,
                }
        return params

    def get_param_dependencies(self):
        """Explore parameter configurations and store exact socket states.

        Each socket's dependencies maps a tuple of parameter values to
        exists, enabled, UI name and socket_type. Tuple positions follow
        self.driving_parameters after reduction. Exploration includes enum
        flags and booleans as well as ordinary enums.
        The initial node configuration is restored after exploration.
        """
        self.__dict__.pop('_data_type_changes', None)
        initial = self.snapshot_params()
        self.enum_parameters = tuple(
            name for name, param in initial.items()
            if param['type'] in {'ENUM', 'ENUM_FLAG'} or isinstance(param['value'], bool)
        )
        self.configurations = ()
        self.driving_parameters = ()
        self.param_dependencies = {}
        visited = set()
        sockets = self.all_sockets()
        self.inputs = dict(sockets['inputs'])
        self.outputs = dict(sockets['outputs'])
        observations = {}

        def possible_values(param):
            if param['type'] == 'ENUM':
                yield from param['enums']
            elif param['type'] == 'ENUM_FLAG':
                enums = param['enums']
                for size in range(len(enums) + 1):
                    for group in combinations(enums, size):
                        yield set(group)
            elif isinstance(param['value'], bool):
                yield from (False, True)

        def explore(before, before_sockets):
            values = {name: param['value'] for name, param in before.items()}
            restore_values = {}
            for name, param in before.items():
                value = param['value']
                choices = param['enums']
                if choices is not None:
                    if param['type'] == 'ENUM_FLAG':
                        if not value.issubset(choices):
                            continue
                    elif value not in choices:
                        continue
                restore_values[name] = value
            key = tuple(frozenset(values[name]) if isinstance(values[name], set) else values[name]
                        for name in self.enum_parameters)
            if key in visited:
                return
            visited.add(key)
            observations[key] = before_sockets
            for direction, current_sockets in before_sockets.items():
                for identifier, socket in current_sockets.items():
                    getattr(self, direction).setdefault(identifier, socket)

            for driver in self.enum_parameters:
                for value in possible_values(before[driver]):
                    if value == values[driver]:
                        continue
                    try:
                        self.set_params(**{driver: value})
                        after = self.snapshot_params()
                        after_sockets = self.all_sockets()
                        for name, previous in before.items():
                            if name == driver:
                                continue
                            previous_enums = previous['enums']
                            current_enums = after[name]['enums']
                            previous_choices = None if previous_enums is None else set(previous_enums)
                            current_choices = None if current_enums is None else set(current_enums)
                            if previous_choices != current_choices:
                                self.param_dependencies.setdefault(name, set()).add(driver)
                        explore(after, after_sockets)
                    finally:
                        if driver in restore_values:
                            self.set_params(**{driver: restore_values[driver]})
                        self.set_params(**restore_values)

        explore(initial, sockets)
        self.configurations = tuple(observations)
        for direction in ('inputs', 'outputs'):
            for identifier, socket in getattr(self, direction).items():
                for key, observed_sockets in observations.items():
                    observed = observed_sockets[direction].get(identifier)
                    socket.dependencies[key] = {
                        'exists': observed is not None,
                        'enabled': observed.enabled if observed is not None else False,
                        'name': (observed.label or observed.name) if observed is not None else None,
                        'socket_type': observed.socket_type if observed is not None else None,
                        'index': observed.index if observed is not None else None,
                    }
        self._reduce_socket_configurations()
        self.build_max_sockets()
        return self.param_dependencies

    def _reduce_socket_configurations(self):
        """Remove parameter axes that do not distinguish socket configurations."""
        states = {
            key: {
                direction: {
                    identifier: socket.dependencies[key]
                    for identifier, socket in getattr(self, direction).items()
                }
                for direction in ('inputs', 'outputs')
            }
            for key in self.configurations
        }
        indices = list(range(len(self.enum_parameters)))
        for index in range(len(self.enum_parameters)):
            candidate = [i for i in indices if i != index]
            grouped = {}
            for key, state in states.items():
                reduced_key = tuple(key[i] for i in candidate)
                if reduced_key in grouped and grouped[reduced_key] != state:
                    break
                grouped[reduced_key] = state
            else:
                indices = candidate

        self.driving_parameters = tuple(self.enum_parameters[i] for i in indices)
        reduced = {}
        for key, state in states.items():
            reduced_key = tuple(key[i] for i in indices)
            if reduced_key in reduced and reduced[reduced_key] != state:
                raise ValueError(f"Different socket states for reduced configuration {reduced_key!r}")
            reduced[reduced_key] = state

        self.configurations = tuple(reduced)
        for direction in ('inputs', 'outputs'):
            for identifier, socket in getattr(self, direction).items():
                socket.dependencies = {
                    key: state[direction][identifier]
                    for key, state in reduced.items()
                }

    def build_max_sockets(self):
        """Build logical socket lists from the reduced configurations.

        Physical variants may share one logical socket when they share an
        enabled UI name and are never enabled simultaneously. Other sockets,
        including simultaneous homonyms, keep separate list entries.

        enabled lists the configurations that disable the logical socket;
        an empty list means always enabled. Other fields are constants when
        possible, otherwise dictionaries keyed by reduced configuration.
        """
        def build(sockets):
            groups = []
            for socket in sockets.values():
                active = {key for key, state in socket.dependencies.items()
                          if state['exists'] and state['enabled']}
                names = {socket.dependencies[key]['name'] for key in active}
                for group in groups:
                    if (names & group['names'] and not active & group['active']
                            and socket.is_multi_input == group['sockets'][0].is_multi_input):
                        group['sockets'].append(socket)
                        group['names'].update(names)
                        group['active'].update(active)
                        break
                else:
                    groups.append({'sockets': [socket], 'names': names, 'active': active})

            result = []
            for group in groups:
                states = {}
                for key in self.configurations:
                    present = [socket for socket in group['sockets']
                               if socket.dependencies[key]['exists']]
                    active = [socket for socket in present if socket.dependencies[key]['enabled']]
                    selected = (active or present)[0] if present else None
                    state = selected.dependencies[key] if selected is not None else None
                    states[key] = {
                        'exists': bool(present),
                        'enabled': bool(active),
                        'identifier': selected.identifier if selected is not None else None,
                        'name': state['name'] if state is not None else None,
                        'socket_type': state['socket_type'] if state is not None else None,
                        'index': state['index'] if state is not None else None,
                    }

                descriptor = {
                    'enabled': [key for key, state in states.items() if not state['enabled']],
                }
                for prop in ('exists', 'identifier', 'name', 'socket_type', 'index'):
                    # Missing sockets have no identifier, UI name or type.
                    values = {state[prop] for state in states.values()
                              if prop == 'exists' or state['exists']}
                    descriptor[prop] = (next(iter(values)) if len(values) == 1 else
                                        {key: state[prop] for key, state in states.items()})
                result.append(descriptor)
            return result

        self.max_inputs = build(self.inputs)
        self.max_outputs = build(self.outputs)

    def socket_argument_names(self, direction='inputs'):
        """Return unique Python names aligned with the maximum logical sockets.

        Virtual sockets have no argument name. The implementation generator
        uses this naming rule.
        """
        used = set(self.snapshot_params()) | {
            'cls', '_node', '_configuration', 'named_sockets', 'sockets', '_identifier', '_value',
        }
        names = []
        for descriptor in getattr(self, f'max_{direction}'):
            types = descriptor['socket_type']
            types = types.values() if isinstance(types, dict) else (types,)
            if not any(t not in (None, 'CUSTOM') for t in types):
                names.append(None)
                continue
            ui_name = descriptor['name']
            if isinstance(ui_name, dict):
                identifiers = descriptor['identifier']
                identifier = (next(v for v in identifiers.values() if v is not None)
                              if isinstance(identifiers, dict) else identifiers)
                reference = getattr(self, direction)[identifier]
                ui_name = reference.label or reference.name
            base = core_module.utils.snake_case(ui_name) or 'value'
            name = base
            index = 0
            while name in used:
                index += 1
                name = f'{base}_{index}'
            used.add(name)
            names.append(name)
        return names

    def param_filter(self, **kwargs):
        """Return configuration keys matching the supplied parameter values.

        Keys follow driving_parameters. Omitted parameters remain free;
        neutral enum parameters are accepted but do not filter socket states.
        Use the keys to read socket dependencies without modifying the node.
        """
        unknown = kwargs.keys() - set(self.enum_parameters)
        if unknown:
            raise ValueError(f"Unknown enum parameters: {', '.join(sorted(unknown))}")
        filters = {
            self.driving_parameters.index(name): frozenset(value) if isinstance(value, set) else value
            for name, value in kwargs.items()
            if name in self.driving_parameters
        }
        return tuple(key for key in self.configurations
                     if all(key[index] == value for index, value in filters.items()))

    @classmethod
    def socket_class_name(cls, socket_type, name=None):
        """Resolve a class name without using the active runtime environment."""
        if socket_type == 'GEOMETRY':
            try:
                return cls.geometry_class(name)
            except ValueError:
                return 'Geometry'
        if socket_type == 'SHADER' and name == 'Volume':
            return 'VolumeShader'
        return core_module.constants.CLASS_NAMES[socket_type]

    @classmethod
    def geometry_class(cls, name):
        """Resolve a geometry socket name using the legacy explicit mapping."""
        if name in ('Mesh', 'Meshes', 'Mesh 1', 'Mesh 2', 'Bounding Box', 'Convex Hull', 'Dual Mesh'):
            return 'Mesh'
        if name in ('Curve', 'Curves', 'Spline', 'Splines', 'Guide Curves', 'Profile Curve'):
            return 'Curve'
        if name in ('Instance', 'Instances', 'Curve Instances'):
            return 'Instances'
        if name in ('Cloud', 'Points', 'Point Cloud'):
            return 'Cloud'
        if name == 'Volume':
            return 'Volume'
        if name == 'Grease Pencil':
            return 'GreasePencil'
        if name in ('Geometry', 'Geometries', 'Transform', 'Target Geometry', 'Selection',
                    'Inverted', 'Output', '0', '1', 'A', 'B', 'False', 'True', 'Value', 'List',
                    'Component', 'Profile', 'Target', 'Source', 'Item'):
            return 'Geometry'
        raise ValueError(f"Unknown Geometry socket name: {name!r}. Update NodeInfo.geometry_class.")

    @property
    def convert_to_classes(self):
        """Return (source, destination class), or None for a non-conversion.

        The source may be a description such as 'Axis Angle'. Only the
        destination must name a socket class. Match full 'to' words, allowing
        UI spaces in class names such as 'Grease Pencil'.

        Normalize Curves -> Curve, Points -> Cloud, Euler -> Vector and
        Value -> Float on either side:
        'Curves to Grease Pencil' -> ('Curve', 'GreasePencil'),
        'Mesh to Points' -> ('Mesh', 'Cloud'). In every explored configuration,
        the first output must have the destination class, and the first input
        must have a different class. Geometry names refine the generic socket
        type, so Curve -> Mesh is a conversion despite both using GEOMETRY.
        Remaining semantic exceptions are corrected explicitly by the caller,
        not excluded here with node-specific tests.
        """
        parts = re.split(r'\s+to\s+', self.bnode.name.strip(), flags=re.IGNORECASE)
        if len(parts) != 2 or not all(part.strip() for part in parts):
            return None
        classes = set(core_module.constants.CLASS_NAMES.values()) | set(core_module.constants.GEOMETRY_CLASSES)
        classes.discard('Input')
        names = {name.lower(): name for name in classes}
        names.update({'curves': 'Curve', 'points': 'Cloud', 'euler': 'Vector', 'value': 'Float'})

        def resolve(name):
            return names.get(re.sub(r'\s+', '', name).lower())

        source, target = (part.strip() for part in parts)
        target_class = resolve(target)
        if target_class is None:
            return None

        def first_class(direction, config):
            for socket in getattr(self, 'max_' + direction):
                def value(name):
                    item = socket[name]
                    return item[config] if isinstance(item, dict) else item

                if config in socket['enabled'] or not value('exists'):
                    continue
                socket_type, name = value('socket_type'), value('name')
                if socket_type == 'CUSTOM':
                    continue
                if socket_type == 'GEOMETRY':
                    return self.geometry_class(name)
                if socket_type == 'SHADER' and name == 'Volume':
                    return 'VolumeShader'
                return core_module.constants.CLASS_NAMES[socket_type]
            return None

        if not self.configurations:
            return None
        for config in self.configurations:
            if (first_class('outputs', config) != target_class
                    or first_class('inputs', config) == target_class):
                return None
        return resolve(source) or source, target_class

    @property
    def is_convert_to(self):
        """Whether the node name describes a conversion to a socket class."""
        return self.convert_to_classes is not None

    def input_implementation(self):
        """Propose a domain implementation for an INPUT node, or return None.

        Apply these name rules in order, matching whole words and accepting
        singular/plural domain names:

        1. '<subject> of <domain>' targets the domain at the end:
           Corners of Edge -> Edge.corners; Edges of Vertex -> Vertex.edges;
           Face of Corner -> Corner.face; Points of Curve -> Spline.points.
        2. '<subject> in <domain>' uses the same trailing-domain rule:
           Offset Corner in Face -> Face.offset_corner;
           Offset Point in Curve -> Spline.offset_point.
        3. '[Is] <domain> <subject>' targets the leading domain and retains Is:
           Edge Angle -> Edge.angle; Face Area -> Face.area;
           Spline Length -> Spline.length; Instance Bounds -> Instance.bounds;
           Is Edge Smooth -> Edge.is_smooth; Is Face Planar -> Face.is_planar;
           Is Spline Cyclic -> Spline.is_cyclic.

        Domains: Edge, Face, Vertex, Corner, Spline, Instance and Point. Curve
        as a trailing container means Spline (the curve/spline domain), not
        the geometry class Curve. A leading Curve is intentionally ambiguous:
        Curve Tangent and Curve Tilt need explicit choices, like Position,
        Normal, Radius and Selection. Unmatched names have no proposal here.

        INPUT_IMPLEMENTATIONS overrides inferred fields and can also supply a
        class for unmatched names. It may set name=None to omit the Node method.
        The generator creates class methods returning the Node; eligible
        class properties come from output names, not from these name rules.
        No node state, configuration or generated source is modified here.
        """
        if self.color_tag != 'INPUT':
            return None
        domains = {
            'edge': 'Edge', 'edges': 'Edge', 'face': 'Face', 'faces': 'Face',
            'vertex': 'Vertex', 'vertices': 'Vertex', 'corner': 'Corner', 'corners': 'Corner',
            'spline': 'Spline', 'splines': 'Spline', 'instance': 'Instance', 'instances': 'Instance',
            'point': 'Point', 'points': 'Point', 'curve': 'Spline', 'curves': 'Spline',
        }
        alternatives = '|'.join(sorted(domains, key=len, reverse=True))
        name = self.bnode.name
        match = re.fullmatch(r'(.+?)\s+(?:of|in)\s+(' + alternatives + r')', name, flags=re.IGNORECASE)
        inferred = {}
        if match:
            subject, domain = match.groups()
            inferred = {'class_name': domains[domain.lower()],
                        'name': core_module.utils.snake_case(subject)}
        else:
            leading = '|'.join(word for word in domains if word not in ('curve', 'curves'))
            match = re.fullmatch(r'(Is\s+)?(' + leading + r')\s+(.+)', name, flags=re.IGNORECASE)
            if match:
                state, domain, subject = match.groups()
                inferred = {'class_name': domains[domain.lower()],
                            'name': core_module.utils.snake_case(('Is ' if state else '') + subject)}
        explicit = config.INPUT_IMPLEMENTATIONS.get(self.bnode.bl_idname, {})
        if not inferred and not explicit:
            return None
        specification = {**inferred, **explicit}
        if 'class_name' not in specification:
            raise ValueError(f"No target class for INPUT implementation: {name}")
        return specification

    def default_name(self, class_name, kind='METHOD', allow_conversion=True):
        """Name an implementation, omitting redundant class words.

        Constructors use CamelCase, other implementations use snake_case.
        Conversion names use the node's UI words on both sides of 'to'; class
        synonyms determine the target classes, not the FromXxx/to_xxx names.
        This does not rename the low-level nd/snd accessors.
        """
        if kind == 'NONE':
            return None
        replacement = config.REPLACE_DEFAULT_IMPLEMENTATIONS.get(self.bnode.bl_idname, {})
        if 'name' in replacement:
            return replacement['name']
        conversion = self.convert_to_classes if allow_conversion else None
        if conversion is not None:
            source, target = conversion
            if kind == 'CONSTRUCTOR':
                source_label = re.split(r'\s+to\s+', self.bnode.name.strip(), flags=re.IGNORECASE)[0].strip()
                return 'From' + core_module.utils.CamelCase(source_label)
            if class_name == source:
                # Class aliases affect lookup, not the familiar to_points name.
                target = re.split(r'\s+to\s+', self.bnode.name.strip(), flags=re.IGNORECASE)[1].strip()
                target = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', target)
                return 'to_' + core_module.utils.snake_case(target)
        original = self.bnode.name
        name = original
        aliases = {
            'Geometry': ('Geometry', 'Geometries'), 'Mesh': ('Mesh', 'Meshes'),
            'Curve': ('Curve', 'Curves'), 'Instances': ('Instance', 'Instances'),
            'Matrix': ('Matrix', 'Matrices'),
            'Cloud': ('Point Cloud', 'Cloud'),
            'GreasePencil': ('Grease Pencil',), 'VolumeShader': ('Volume Shader',),
        }
        words = aliases.get(class_name, (class_name,) if class_name else ())
        for word in sorted(words, key=len, reverse=True):
            name = re.sub(r'\b' + re.escape(word) + r'\b', '', name, flags=re.IGNORECASE)
        if kind == 'CONSTRUCTOR':
            if self.btree.bl_idname == 'ShaderNodeTree' and name.rstrip().endswith('BSDF'):
                name = name.rstrip()[:-4]
            if class_name == 'Vector' and original == 'Combine XYZ':
                name = 'Combine'
        elif kind in ('GETTER', 'SETTER'):
            name = re.sub(r'^\s*Set\s+', '', name)
        name = ' '.join(name.split()) or original
        return (core_module.utils.CamelCase(name) if kind == 'CONSTRUCTOR' else
                core_module.utils.snake_case(name))

    def default_implementation(self, **parameters):
        """Describe the recommended implementation without generating source.

        Rules for the default proposal (explicit implementations may override
        it). These rules describe the class API, independently of nd/snd:

        Specific nodes listed in config.NO_DEFAULT_IMPLEMENTATION have no
        default implementation (kind NONE, signature None): Group Input,
        Group Output, Bake, Viewer and zone boundaries (Repeat, Simulation,
        For Each Geometry Element, Closure). The dictionary documents each
        exclusion. Their introspection and low-level access are unaffected.

        INPUT color-tag nodes have no default class implementation, except:
        - Names starting with Import and returning Geometry construct the
          refined output class: Import STL -> Mesh.ImportStl.
        - Names ending in Info are methods bound to the first input:
          Object Info -> Object.info, Camera Info -> Object.camera_info.
        Explicit replacements take precedence (Collection Info keeps its
        Instances constructor and adds Collection.info separately).
        Corners of Edge stays available via nd.corners_of_edge. nd/snd class
        properties such as nd.position are independent of this restriction.

        1. Configuration: supplied non-None parameters are fixed; others stay
           arguments. Enum identifiers and UI labels are accepted. Select the
           compatible explored state closest to the current driving values.
           The Blender node itself is never modified.
        2. Constructors:
           - A name starting with Combine constructs the first output class:
             Combine Color -> Color.Combine, Combine XYZ -> Vector.Combine.
           - A first Geometry output with no Geometry input constructs its
             refined geometry class: Ico Sphere -> Mesh.IcoSphere,
             Mesh Line -> Mesh.Line.
           - Shader BSDF nodes construct Shader: Diffuse BSDF -> Shader.Diffuse.
        3. Conversions: a single ' to ' separator and a recognized destination
           class propose Target.FromSource. A recognized source class with a
           matching input also proposes Source.to_target:
           Curve to Mesh -> Mesh.FromCurve / Curve.to_mesh;
           Axis Angle to Rotation -> Rotation.FromAxisAngle only;
           Curves to Grease Pencil -> GreasePencil.FromCurves /
           Curve.to_grease_pencil; Mesh to Points -> Cloud.FromMesh /
           Mesh.to_points; Points to Volume -> Volume.FromPoints /
           Cloud.to_volume; Euler to Rotation -> Rotation.FromEuler /
           Vector.to_rotation; Value to String -> String.FromValue /
           Float.to_string. Curves, Points, Euler and Value normalize to Curve,
           Cloud, Vector and Float for class lookup only. FromXxx and to_xxx retain
           the source and target UI words, respectively.
           The first output must match the destination class and differ from
           the first input in every explored state. Align Rotation to Vector
           is therefore a method, not a conversion (Rotation -> Rotation).
           Remaining false positives such as Split to Instances are left for
           explicit overrides; no node-specific exclusions are applied.
        4. Methods: otherwise bind the first enabled non-virtual input to self.
           Move Fac/Factor last before choosing self: Mix binds A, not Factor.
           The input type, refined by geometry_class for Geometry sockets,
           determines the target class. A fixed domain selects its domain
           class: Extrude Mesh(domain='FACE') targets Face. If its first input
           is not Geometry, the domain implementation is a class method.
        5. Implicit arguments: Selection following a Geometry input is omitted
           for an instance implementation. Fixed parameters are omitted too.
           Virtual sockets count as dynamic arguments, not as an empty input.
           A multi-input bound to self still accepts additional values.
        6. Properties: for eligible nodes, no free arguments and a single
           output permit GETTER: Curve Length -> Curve.length. With no self
           input this is a class property. Other nodes without inputs have kind NONE and
           signature None: Edge Angle remains accessible via nd.edge_angle().
           Constructor rules take precedence over properties.
        7. Return: use the first output, except Separate nodes and nodes with
           virtual outputs, which return the Node to expose all outputs.
           Matching Geometry input/output classes imply a jump:
           Subdivide Mesh -> Mesh.subdivide, updating the wrapped Mesh.
        8. Names: constructors use CamelCase, methods/properties snake_case.
           Omit redundant class words: Fill Curve -> Curve.fill,
           Mesh Line -> Mesh.Line. Conversion names follow rule 3.

        The result contains kind, name, class_name, self_socket (identifier),
        return_socket ('OUT' or None for the Node), is_jump, is_convert_to and
        signature. The signature is a display-only preview: the receiver is
        the UI socket name (cls for class implementations), ... means remaining
        arguments, and the return is the actual class or the word jump.
        Example: 'def subdivide(Mesh, ...) -> jump'. Conversion alternatives
        are separated by ' / '. No source is generated by this method.

        config.REPLACE_DEFAULT_IMPLEMENTATIONS may force a CONSTRUCTOR or
        METHOD and its name. self_socket selects the instance input by Blender
        identifier or UI name: Closure to List binds Closure, leaving Count as
        an argument, and proposes Closure.to_list. A missing or ambiguous
        selection is an error. param_loop requests one proposal per enum value:
        Random Value -> Float.Random, Integer.Random, Vector.Random and
        Boolean.Random. The result then includes param_loop and implementations
        (each with its fixed parameters); signature joins their previews.
        class_name is None on the aggregate because it targets several classes.
        Passing data_type='INT' explicitly returns just Integer.Random.

        config.ADDITIONAL_IMPLEMENTATIONS appends explicit proposals without
        replacing the main one. They are returned in additional_implementations
        and their signatures follow the main signature, separated by ' / '.
        Collection Info -> Instances.CollectionInfo plus Collection.info.
        """
        started = perf_counter()
        try:
            node_id = self.bnode.bl_idname
            replacement = {**self.data_type_implementation(),
                           **config.REPLACE_DEFAULT_IMPLEMENTATIONS.get(node_id, {})}
            result = self._default_implementation(replacement, **parameters)
            additions = config.ADDITIONAL_IMPLEMENTATIONS.get(node_id, [])
            if additions:
                implementations = [self._default_implementation(addition, **parameters) for addition in additions]
                result['additional_implementations'] = implementations
                signatures = [result['signature'], *(impl['signature'] for impl in implementations)]
                result['signature'] = ' / '.join(signature for signature in signatures if signature) or None
            return result
        finally:
            self.default_implementation_time += perf_counter() - started

    def _default_implementation(self, replacement, **parameters):
        """Compute one proposal (or enum loop), without collecting additions."""
        if self.bnode.bl_idname in config.NO_DEFAULT_IMPLEMENTATION:
            return {
                'kind': 'NONE',
                'name': None,
                'class_name': None,
                'self_socket': None,
                'return_socket': None,
                'is_jump': False,
                'is_convert_to': False,
                'signature': None,
            }
        snapshot = self.snapshot_params()
        requested_kind = replacement.get('kind')
        if requested_kind not in (None, 'CONSTRUCTOR', 'METHOD'):
            raise ValueError(f"Unsupported default implementation override: {requested_kind!r}")
        unknown = parameters.keys() - snapshot.keys()
        if unknown:
            raise ValueError(f"Unknown parameters: {', '.join(sorted(unknown))}")
        fixed = {}
        for name, value in parameters.items():
            if value is None:
                continue
            prop = self.bnode.bl_rna.properties[name]
            if prop.type == 'ENUM':
                names = {item.identifier.lower(): item.identifier for item in prop.enum_items}
                names.update({item.name.lower(): item.identifier for item in prop.enum_items})
                value = ({names[v.lower()] for v in value} if prop.is_enum_flag else names[value.lower()])
            fixed[name] = value
        configurations = self.param_filter(**{n: v for n, v in fixed.items() if n in self.enum_parameters})
        if not configurations:
            raise ValueError(f"No socket configuration for {self.bnode.name!r}: {fixed!r}")
        param_loop = replacement.get('param_loop')
        if param_loop is not None and param_loop not in fixed:
            if param_loop not in snapshot or snapshot[param_loop]['type'] != 'ENUM':
                raise ValueError(f"param_loop must name an enum parameter: {param_loop!r}")
            if param_loop in self.driving_parameters:
                index = self.driving_parameters.index(param_loop)
                values = tuple(dict.fromkeys(key[index] for key in configurations))
            else:
                values = snapshot[param_loop]['enums']
            if not values:
                raise ValueError(f"No valid values for {self.bnode.name}.{param_loop}")
            implementations = []
            for value in values:
                implementation = self._default_implementation(replacement, **{**parameters, param_loop: value})
                implementation['parameters'] = {**fixed, param_loop: value}
                implementations.append(implementation)
            result = implementations[0].copy()
            result.update(class_name=None, param_loop=param_loop, implementations=implementations,
                          signature=' / '.join(impl['signature'] for impl in implementations))
            result.pop('parameters')
            return result
        defaults = tuple(frozenset(snapshot[n]['value']) if isinstance(snapshot[n]['value'], set)
                         else snapshot[n]['value'] for n in self.driving_parameters)
        configuration = max(configurations, key=lambda key: sum(a == b for a, b in zip(key, defaults)))

        def sockets(direction):
            result = []
            for descriptor in getattr(self, 'max_' + direction):
                state = {name: value[configuration] if isinstance(value, dict) else value
                         for name, value in descriptor.items() if name != 'enabled'}
                if state['exists'] and configuration not in descriptor['enabled']:
                    result.append(state)
            return sorted(result, key=lambda socket: socket['index'])

        def socket_class(socket):
            socket_type, name = socket['socket_type'], socket['name']
            if socket_type == 'GEOMETRY':
                return self.geometry_class(name)
            if socket_type == 'SHADER' and name == 'Volume':
                return 'VolumeShader'
            return core_module.constants.CLASS_NAMES[socket_type]

        inputs, outputs = sockets('inputs'), sockets('outputs')
        dynamic = any(s['socket_type'] == 'CUSTOM' for s in inputs + outputs)
        inputs = [s for s in inputs if s['socket_type'] != 'CUSTOM']
        outputs = [s for s in outputs if s['socket_type'] != 'CUSTOM']
        # Like get_in_sockets: A.mix(B, factor), not factor.mix(A, B).
        inputs.sort(key=lambda s: s['name'] in ('Factor', 'Fac'))
        self_input = inputs[0] if inputs else None
        if 'self_socket' in replacement:
            requested_socket = replacement['self_socket']
            matches = [s for s in inputs if s['identifier'] == requested_socket]
            if not matches:
                matches = [s for s in inputs if s['name'] == requested_socket]
            if len(matches) != 1:
                raise ValueError(f"Unknown or ambiguous self socket for {self.bnode.name}: {requested_socket!r}")
            self_input = matches[0]
        class_name = socket_class(self_input) if self_input else socket_class(outputs[0]) if outputs else None
        constructor = self_input is None
        conversion = None if replacement.get('typed_class_method') else self.convert_to_classes

        geometry_constructor = (bool(outputs) and outputs[0]['socket_type'] == 'GEOMETRY'
                                and not any(s['socket_type'] == 'GEOMETRY' for s in inputs))
        input_tag = self.color_tag == 'INPUT'
        import_constructor = (input_tag and self.bnode.name.startswith('Import')
                              and bool(outputs) and outputs[0]['socket_type'] == 'GEOMETRY')
        info_method = input_tag and self.bnode.name.endswith('Info') and self_input is not None
        combine_constructor = self.bnode.name.startswith('Combine')
        bsdf_constructor = self.btree.bl_idname == 'ShaderNodeTree' and self.bnode.name.endswith('BSDF')
        if requested_kind == 'METHOD' or (info_method and requested_kind is None):
            if self_input is None:
                raise ValueError(f"No instance input for method {self.bnode.name!r}")
            constructor = False
        elif requested_kind == 'CONSTRUCTOR':
            if not outputs:
                raise ValueError(f"No output class for constructor {self.bnode.name!r}")
            self_input, class_name, constructor = None, socket_class(outputs[0]), True
        elif import_constructor:
            self_input, class_name, constructor = None, socket_class(outputs[0]), True
        elif combine_constructor:
            if not outputs:
                raise ValueError(f"No output class for constructor {self.bnode.name!r}")
            self_input, class_name, constructor = None, socket_class(outputs[0]), True
        elif conversion is not None:
            self_input, class_name, constructor = None, conversion[1], True
        elif geometry_constructor:
            self_input, class_name, constructor = None, socket_class(outputs[0]), True
        elif bsdf_constructor:
            self_input, class_name, constructor = None, 'Shader', True
        if replacement.get('typed_class_method'):
            direction = 'inputs' if replacement.get('class_from') == 'INPUT' else 'outputs'
            for index in self.data_type_socket_changes[direction]:
                descriptor = getattr(self, 'max_' + direction)[index]
                state = {key: value[configuration] if isinstance(value, dict) else value
                         for key, value in descriptor.items() if key != 'enabled'}
                if state['exists'] and configuration not in descriptor['enabled']:
                    class_name = socket_class(state)
                    break
            else:
                raise ValueError(f'No typed {direction} for {self.bnode.name}: {fixed!r}')
        if 'domain' in fixed:
            domains = {'POINT': 'Point', 'FACE': 'Face', 'EDGE': 'Edge', 'CORNER': 'Corner',
                       'CURVE': 'Spline', 'SPLINE': 'Spline', 'INSTANCE': 'Instance',
                       'LAYER': 'Layer', 'AUTO': 'Geometry'}
            class_name = domains[fixed['domain']]
            if self_input is None or self_input['socket_type'] != 'GEOMETRY':
                self_input, constructor = None, True

        free_inputs = [s for s in inputs if s is not self_input]
        # Selection is implicit only when it follows a Geometry input.
        ordered = sockets('inputs')
        implicit_selection = {s['identifier'] for previous, s in zip(ordered, ordered[1:])
                              if s['name'] == 'Selection' and previous['socket_type'] == 'GEOMETRY'}
        if self_input is not None:
            free_inputs = [s for s in free_inputs if s['identifier'] not in implicit_selection]
        free_count = len(free_inputs) + len(snapshot.keys() - fixed.keys()) + int(dynamic)
        if self_input is not None and self.inputs[self_input['identifier']].is_multi_input:
            # The variadic input also accepts values in addition to self.
            free_count += 1
        return_socket = 'OUT' if outputs else None
        if self.bnode.name.startswith('Separate') or any(s['socket_type'] == 'CUSTOM' for s in sockets('outputs')):
            return_socket = None
        getter = free_count == 0 and len(outputs) == 1 and return_socket is not None
        forced_constructor = (requested_kind == 'CONSTRUCTOR' or import_constructor or combine_constructor
                              or geometry_constructor or bsdf_constructor or conversion is not None)
        kind = requested_kind or ('METHOD' if info_method else 'CONSTRUCTOR' if forced_constructor else 'GETTER' if getter else
                                  'CONSTRUCTOR' if constructor else 'METHOD')
        input_without_default = input_tag and not import_constructor and not info_method and not replacement and 'domain' not in fixed
        if input_without_default or (not ordered and not getter and not forced_constructor and 'domain' not in fixed):
            return {
                'kind': 'NONE',
                'name': None,
                'class_name': None,
                'self_socket': None,
                'return_socket': None,
                'is_jump': False,
                'is_convert_to': False,
                'signature': None,
            }
        is_jump = (self_input is not None and self_input['socket_type'] == 'GEOMETRY'
                   and bool(outputs) and outputs[0]['socket_type'] == 'GEOMETRY'
                   and socket_class(self_input) == socket_class(outputs[0])
                   and return_socket is not None)

        receiver = 'cls' if constructor else self_input['name']
        header = receiver + (', ...' if free_count else '')
        naming_class = (socket_class(self_input) if self_input is not None
                        and self_input['socket_type'] == 'GEOMETRY' else class_name)
        name = replacement['name'] if 'name' in replacement else self.default_name(naming_class, kind=kind, allow_conversion=not replacement.get('typed_class_method'))
        returns = 'jump' if is_jump else class_name if kind == 'CONSTRUCTOR' and not replacement.get('typed_class_method') else (
            socket_class(outputs[0]) if return_socket == 'OUT' else 'Node')
        signature = f'def {name}({header}) -> {returns}'
        if conversion is not None:
            source_class, target_class = conversion
            # A descriptor such as Axis Angle has no class method counterpart.
            classes = set(core_module.constants.CLASS_NAMES.values()) | set(core_module.constants.GEOMETRY_CLASSES)
            if source_class in classes:
                source_input = next((s for s in inputs if socket_class(s) == source_class), None)
                if source_input is not None:
                    method_count = free_count - 1
                    method_count -= sum(s['identifier'] in implicit_selection for s in inputs if s is not source_input)
                    if self.inputs[source_input['identifier']].is_multi_input:
                        method_count += 1
                    method_header = source_input['name'] + (', ...' if method_count else '')
                    method_name = self.default_name(source_class, kind='METHOD')
                    signature += f' / def {method_name}({method_header}) -> {target_class}'
        return {
            'kind': kind,
            'name': name,
            'class_name': class_name,
            'self_socket': self_input['identifier'] if self_input is not None else None,
            'return_socket': return_socket,
            'is_jump': is_jump,
            'is_convert_to': conversion is not None,
            'signature': signature,
        }

    @property
    def color_tag(self):
        """Return the Blender node's color category."""
        return self.bnode.color_tag

    @property
    def is_class_property(self):
        """Whether the node is a parameterless input with a single output."""
        if self.has_input_sockets or self.has_parameters or len(self.outputs) != 1:
            return False
        socket = next(iter(self.outputs.values()))
        return all(state['socket_type'] != 'CUSTOM'
                   for state in socket.dependencies.values() if state['exists'])

    @property
    def has_parameters(self):
        """Whether the node exposes any parameters."""
        return bool(self.snapshot_params())

    @property
    def has_input_sockets(self):
        """Whether the node has input sockets, including virtual sockets."""
        return bool(self.inputs)

    @property
    def has_output_sockets(self):
        """Whether the node has output sockets, including virtual sockets."""
        return bool(self.outputs)

    @property
    def has_multi_input(self):
        """Whether any input socket accepts multiple links."""
        return any(socket.is_multi_input for socket in self.inputs.values())

    @property
    def multi_input_socket(self):
        """Return the first multi-input NodeSocket, or None."""
        return next((socket for socket in self.inputs.values() if socket.is_multi_input), None)

    @property
    def has_dynamic_inputs(self):
        """Whether any explored input socket is virtual."""
        return any(socket.socket_type == 'CUSTOM' for socket in self.inputs.values())

    @property
    def has_dynamic_outputs(self):
        """Whether any explored output socket is virtual."""
        return any(socket.socket_type == 'CUSTOM' for socket in self.outputs.values())

    @property
    def has_driving_parameters(self):
        """Whether parameters influence the socket configuration."""
        return bool(self.driving_parameters)

    @property
    def has_data_type_parameter(self):
        """Whether the node exposes data_type or input_type."""
        return bool({'data_type', 'input_type'} & self.snapshot_params().keys())

    @property
    def data_type_socket_changes(self):
        """Logical input/output indices whose types depend on the type enum."""
        if hasattr(self, '_data_type_changes'):
            return self._data_type_changes
        parameter = self.data_type_parameter
        result = {'inputs': (), 'outputs': ()}
        if parameter is not None and parameter.name in self.driving_parameters:
            axis = self.driving_parameters.index(parameter.name)
            for direction in result:
                sockets = getattr(self, 'max_' + direction)
                groups = {}
                ranks = {}
                for key in self.configurations:
                    other = key[:axis] + key[axis + 1:]
                    rank = 0
                    for index, socket in enumerate(sockets):
                        exists = socket['exists']
                        if not (exists[key] if isinstance(exists, dict) else exists) or key in socket['enabled']:
                            continue
                        types = socket['socket_type']
                        socket_type = types[key] if isinstance(types, dict) else types
                        groups.setdefault((other, index), set()).add(socket_type)
                        ranks.setdefault((other, rank), []).append((index, socket_type))
                        rank += 1
                changed = {index for (_, index), types in groups.items() if len(types) > 1}
                # Some types replace a socket with one bearing another UI name,
                # such as Map Range's Result/Vector outputs.
                for values in ranks.values():
                    if len({socket_type for _, socket_type in values}) > 1:
                        changed.update(index for index, _ in values)
                result[direction] = tuple(sorted(changed))
        self._data_type_changes = result
        return result

    @property
    def inferred_data_type_socket(self):
        """Non-first typed argument for an automatically inferred instance method."""
        if self.has_domain_parameter:
            return None
        changes = self.data_type_socket_changes
        if not changes['inputs']:
            return None
        active = [index for index, socket in enumerate(self.max_inputs)
                  if any(key not in socket['enabled'] for key in self.configurations)]
        if changes['inputs'][0] == active[0]:
            return None
        if changes['outputs']:
            first = next((socket for socket in self.bnode.inputs if socket.enabled and socket.type != 'CUSTOM'), None)
            if first is None or first.type != 'GEOMETRY':
                return None
        return self.socket_argument_names('inputs')[changes['inputs'][0]]

    def data_type_implementation(self):
        """Describe the default policy for nodes changing both input and output."""
        if self.has_domain_parameter:
            return {}
        changes = self.data_type_socket_changes
        if not changes['inputs'] or not changes['outputs']:
            return {}
        exception = config.DATA_TYPE_IMPLEMENTATIONS.get(self.bnode.bl_idname, {})
        if exception.get('kind') == 'DEFAULT':
            return {}
        inputs = [socket for socket in self.bnode.inputs if socket.enabled and socket.type != 'CUSTOM']
        inputs.sort(key=lambda socket: (socket.label or socket.name) in ('Factor', 'Fac'))
        first = inputs[0] if inputs else None
        output = next((socket for socket in self.bnode.outputs if socket.enabled and socket.type != 'CUSTOM'), None)

        def controlled(socket, direction):
            if socket is None:
                return False
            for index in changes[direction]:
                identifiers = getattr(self, 'max_' + direction)[index]['identifier']
                if socket.identifier in (identifiers.values() if isinstance(identifiers, dict) else (identifiers,)):
                    return True
            return False

        typed_receiver = controlled(first, 'inputs') and controlled(output, 'outputs')
        geometry_receiver = first is not None and first.type == 'GEOMETRY'
        kind = 'METHOD' if geometry_receiver or typed_receiver else 'CONSTRUCTOR'
        policy = {'kind': kind}
        if typed_receiver and not geometry_receiver:
            policy['param_loop'] = self.data_type_parameter.name
        policy.update(exception)
        if policy['kind'] == 'CONSTRUCTOR':
            policy.update(param_loop=self.data_type_parameter.name, typed_class_method=True)
        elif 'param_loop' not in policy:
            policy.setdefault('self_socket', first.label or first.name)
        return policy

    @property
    def data_type_parameter(self):
        """Return the data_type or input_type NodeParam, or None."""
        parameters = self.snapshot_params()
        for name in ('data_type', 'input_type'):
            if name in parameters:
                return NodeParam.Parameter(self.bnode, name)
        return None

    @property
    def has_domain_parameter(self):
        """Whether the node exposes a domain parameter."""
        return 'domain' in self.snapshot_params()

    @property
    def has_selection(self):
        """Whether Selection follows a Geometry input in the current configuration.

        This is the condition used by the former NodeInfo.get_arguments to
        replace the Selection argument with self.get_selection() in methods.
        """
        previous = None
        for socket in self.bnode.inputs:
            if not socket.enabled or socket.type == 'CUSTOM':
                continue
            if (socket.label or socket.name) == 'Selection' and previous == 'GEOMETRY':
                return True
            previous = socket.type
        return False

    def all_sockets(self):
        """Capture every input/output socket, including disabled sockets."""
        return {
            'inputs': {
                socket.identifier: NodeSocket(socket, index)
                for index, socket in enumerate(self.bnode.inputs)
            },
            'outputs': {
                socket.identifier: NodeSocket(socket, index)
                for index, socket in enumerate(self.bnode.outputs)
            },
        }

    def snapshot_sockets(self):
        """Return only enabled sockets, indexed by identifier."""
        return {
            direction: {identifier: socket for identifier, socket in sockets.items()
                        if socket.enabled}
            for direction, sockets in self.all_sockets().items()
        }

    def snapshot(self):
        """Return parameter and socket snapshots in the current configuration."""
        sockets = self.snapshot_sockets()
        return {
            'params': self.snapshot_params(),
            'inputs': sockets['inputs'],
            'outputs': sockets['outputs'],
        }

    @classmethod
    def loop_on_nodes(cls, func, tree_type="GeometryNodeTree"):
        """Apply func(node_info) to every node type supported by the requested tree.

        Nodes are created in a temporary tree named "Loop on Nodes".
        utils.loop_on_nodes collects them in a dictionary, sorts by UI name,
        then runs the processing callbacks.
        The tree is removed when the loop finishes, including on callback errors.
        config.DEPRECATED_NODES are skipped before creating their NodeInfo wrapper.
        """
        construction_time = signature_time = callback_time = 0.0

        def process(bnode):
            nonlocal construction_time, signature_time, callback_time
            if bnode.bl_idname in config.DEPRECATED_NODES:
                return
            # TEMP HACK documented at the top of this module.
            if bnode.bl_idname == 'ShaderNodeOutputLineStyle':
                return
            started = perf_counter()
            try:
                node = cls(bnode.id_data, bnode)
            finally:
                construction_time += perf_counter() - started
            started = perf_counter()
            before_signature = node.default_implementation_time
            try:
                func(node)
            finally:
                callback_time += perf_counter() - started
                signature_time += node.default_implementation_time - before_signature

        try:
            utils.loop_on_nodes(process, tree_type=tree_type)
        finally:
            print(f"NodeInfo ({tree_type}): construction={construction_time:.3f}s, "
                  f"default_implementation={signature_time:.3f}s, "
                  f"callback remainder (print, etc.)={callback_time - signature_time:.3f}s")
