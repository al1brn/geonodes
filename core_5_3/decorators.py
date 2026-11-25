"""Function builders for Geometry Nodes and shader trees.

Decorated functions expose explicit construction and node insertion::

    @group("Create Plank")
    def create_plank():
        Mesh.Cube().out()

    create_plank.build()
    # Inside another tree: create_plank() inserts a Group node.

Tree options belong to the decorator. Use .build() to force construction.
Pass full=True to rebuild dependencies once each as well. Internal ._build()
preserves existing trees unless reconstruction is requested.
Call the decorated object inside a tree to insert a Group node using the same
socket interface as G(). Existing trees are preserved without executing the
builder when rebuild is false; missing trees are always built. Outputs still
use socket.out(). Material builders support .build() only. When a tree is built,
the construction function's nonempty docstring becomes a Comment node.
"""

from functools import update_wrapper
from inspect import getdoc, signature, Parameter
from math import isfinite
from contextlib import contextmanager
from copy import copy
from typing import get_type_hints
import bpy

from .geonodes import GeoNodes
from .shadernodes import ShaderNodes
from .root.tree import Tree
from .root.node import G, Node
from .common.scripterror import NodeError
from .common.utils import snake_case, get_socket_class
from .common.sockettype import SocketType

__all__ = ["group", "modifier", "tool", "shader_group", "shader", "Package"]


def _validate_build_options(rebuild, full):
    if not isinstance(rebuild, bool) or not isinstance(full, bool):
        raise TypeError('rebuild and full must be bools.')


@contextmanager
def _build_session(full):
    """Share recursive policy and completed dependencies across one operation."""
    previous = _TreeBuilder._session
    if previous is None:
        _TreeBuilder._session = {'full': full, 'built': set()}
    session = _TreeBuilder._session
    previous_full = session['full']
    session['full'] |= full
    try:
        yield session
    finally:
        session['full'] = previous_full
        _TreeBuilder._session = previous


def _comment_docstring(function):
    """Extract comment text, appearance and arrangement metadata."""
    doc = getdoc(function)
    if not doc:
        return '', None, None, 'left', 'outer_top'
    color = None
    width = None
    horizontal = 'left'
    vertical = 'outer_top'
    lines = []
    for line in doc.splitlines():
        if line.strip().startswith(':color:'):
            color = line.strip()[len(':color:'):].strip()
        elif line.strip().startswith(':width:'):
            value = line.strip()[len(':width:'):].strip()
            try:
                width = float(value)
            except ValueError:
                raise ValueError(f'{function.__qualname__}: :width: expects a positive number, got {value!r}.') from None
            if not isfinite(width) or width <= 0:
                raise ValueError(f'{function.__qualname__}: :width: expects a positive number, got {value!r}.')
        elif line.strip().startswith(':horizontal:'):
            horizontal = line.strip()[len(':horizontal:'):].strip()
        elif line.strip().startswith(':vertical:'):
            vertical = line.strip()[len(':vertical:'):].strip()
        else:
            lines.append(line)
    return '\n'.join(lines).strip('\n'), color, width, horizontal, vertical


class _TreeBuilder:
    """A Python construction function and its callable Blender group interface."""

    _building = set()
    _session = None

    def __init__(self, function, tree_class, name, is_group, options, is_tool=False):
        update_wrapper(self, function)
        self.function = function
        self.tree_class = tree_class
        self.is_group = is_group
        self.is_tool = is_tool
        self.options = dict(options)
        self._package_prefix = ''
        if name is None:
            python_name = function.__name__
            name = python_name.lstrip('_').replace('_', ' ').title()
            if python_name.startswith('_'):
                name = '.' + name
        self.name = name

    @property
    def full_name(self):
        prefix = self.options.get("prefix")
        prefix = "" if prefix is None else str(prefix)
        prefix = ' '.join(value for value in (self._package_prefix, prefix) if value)
        if prefix and self.name.startswith('.'):
            return f".{prefix} {self.name[1:]}"
        return f"{prefix} {self.name}" if prefix else self.name

    @property
    def _build_key(self):
        namespace = "material" if self.tree_class is ShaderNodes and not self.is_group else "node_group"
        return namespace, self.full_name

    def _build_inputs(self):
        """Create symbolic group inputs from annotations or Python defaults."""
        sig = signature(self.function)
        hints = get_type_hints(self.function)
        values = {}
        python_types = {float: 'VALUE', int: 'INT', bool: 'BOOLEAN', str: 'STRING'}
        for name, parameter in sig.parameters.items():
            if parameter.kind in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD):
                raise TypeError(f'{self.function.__qualname__}: variadic socket inputs are not supported.')
            default = None if parameter.default is Parameter.empty else parameter.default
            annotation = hints.get(name, parameter.annotation)
            if annotation is Parameter.empty:
                if default is None:
                    raise TypeError(f'{self.function.__qualname__}: input {name!r} needs a type annotation or a default value.')
                socket_type = SocketType(default)
            else:
                socket_type = SocketType.from_type(python_types.get(annotation, annotation))
            factory = (annotation if isinstance(annotation, type) and
                       getattr(annotation, 'SOCKET_TYPE', None) else
                       get_socket_class(socket_type.type))
            values[name] = factory(default, name=name)
        positional = [values[name] for name, p in sig.parameters.items()
                      if p.kind == Parameter.POSITIONAL_ONLY]
        bound = sig.bind(*positional, **{name: value for name, value in values.items()
                                       if sig.parameters[name].kind != Parameter.POSITIONAL_ONLY})
        return bound.args, bound.kwargs

    def _build(self, rebuild: bool = False, full: bool = False):
        """Build if missing, optionally forcing this tree and its dependencies."""
        _validate_build_options(rebuild, full)
        with _build_session(full) as session:
            return self._build_tree(rebuild, session)

    def _build_tree(self, rebuild, session):
        options = dict(self.options)
        options['rebuild'] = session['full'] or rebuild is True
        if self._package_prefix:
            local_prefix = options.get('prefix')
            options['prefix'] = ' '.join(value for value in
                                         (self._package_prefix, str(local_prefix or '')) if value)

        name = self.name
        if options.get('prefix') and name.startswith('.'):
            options['prefix'] = '.' + str(options['prefix'])
            name = name[1:]

        key = self._build_key
        if key in self._building:
            raise NodeError(f"Circular build dependency for '{self.full_name}'.")
        if session['full'] and key in session['built']:
            return None
        self._building.add(key)
        try:
            result = None
            if self.is_tool:
                prefix = options.pop('prefix', None)
                name = f'{prefix} {name}' if prefix else name
                context = self.tree_class.Tool(name, **options)
            else:
                context = self.tree_class(name, is_group=self.is_group, **options)
            with context as tree:
                if tree._rebuild:
                    doc, color, width, horizontal, vertical = _comment_docstring(self.function)
                    if doc and doc.strip():
                        comment = Node('Comment', text=doc)
                        if color is not None:
                            comment._color = color
                        if width is not None:
                            comment._node_width = width
                        comment._set_arrange(horizontal=horizontal, vertical=vertical)
                    args, kwargs = self._build_inputs()
                    result = self.function(*args, **kwargs)
            session['built'].add(key)
            return result
        finally:
            self._building.remove(key)

    def build(self, full: bool = False):
        """Rebuild this tree, optionally including dependencies once each."""
        return self._build(rebuild=True, full=full)

    def __call__(self, *args, **kwargs):
        """Insert a Group node, with the positional/keyword socket API of G."""
        if self.tree_class is ShaderNodes and not self.is_group:
            raise TypeError(f"'{self.full_name}' is a material; use .build() to construct it.")
        if Tree.current_tree() is None:
            raise NodeError(f"Calling '{self.full_name}' requires an active tree. Use .build() to construct it.")
        if self._build_key in self._building:
            raise NodeError(f"Circular build dependency for '{self.full_name}'.")
        session = _TreeBuilder._session
        if session is not None and session['full']:
            self._build(rebuild=True)
        elif bpy.data.node_groups.get(self.full_name) is None:
            self._build()
        return G._call_group(self.full_name, *args, **kwargs)


def _tree_decorator(tree_class, name, is_group, options, is_tool=False):
    def decorate(function):
        return _TreeBuilder(function, tree_class, name, is_group, options, is_tool=is_tool)
    return decorate


def group(name=None, **options):
    """Declare a Geometry Nodes group with .build() and a callable socket interface.

    Options are forwarded to GeoNodes, with is_group=True. If omitted, the
    tree name is derived from the function name: my_group becomes My Group,
    and _my_group becomes .My Group. Explicit names are kept unchanged.
    The construction function's return value is preserved by ._build();
    a skipped build returns None. Function parameters become symbolic input
    sockets during construction; calls inside a tree supply their actual values.
    """
    return _tree_decorator(GeoNodes, name, True, options)


def modifier(name=None, **options):
    """Declare a Geometry Nodes modifier, with GeoNodes options and is_group=False."""
    return _tree_decorator(GeoNodes, name, False, options)


def tool(name=None, **options):
    """Declare a Geometry Nodes tool, forwarding options to GeoNodes.Tool."""
    return _tree_decorator(GeoNodes, name, False, options, is_tool=True)


def shader_group(name=None, **options):
    """Declare a shader group, with ShaderNodes options and is_group=True."""
    return _tree_decorator(ShaderNodes, name, True, options)


def shader(name=None, *, target='ALL', **options):
    """Declare a material, with ShaderNodes options and is_group=False.

    target selects the default Material Output target: ALL, EEVEE or CYCLES.
    Rebuilding a material replaces its node tree.
    """
    return _tree_decorator(ShaderNodes, name, False, dict(options, target=target))


class Package:
    """Organize static builders in a class, or register them on an instance.

    Class packages need no instance or self/cls parameter::

        class Project(Package):
            prefix = "Body"

            @group()
            def move(mesh: Mesh, offset: Vector = (0, 0, 0)):
                mesh.set_position(offset=offset).out()

        Project.move.build(full=True)

    An existing instance registration API remains available:

    Declare the package and its decorated functions at module level::

        furniture = Package("Furniture")

        @furniture.group("Create Plank")
        def create_plank():
            Mesh.Cube().out()

        @furniture.modifier("Add Plank")
        def add_plank():
            create_plank().out()

        def demo():
            furniture.build()

    Registration does not execute the builders. Each has .build() for individual
    reconstruction and a direct group-call interface inside other trees.
    Function parameters define sockets, not Python build-time options.
    """

    prefix = ''
    _class_builders = {}

    def __init_subclass__(cls, **kwargs):
        """Collect static builders without binding a self or cls argument."""
        super().__init_subclass__(**kwargs)
        for name in ('_build', 'build'):
            if name in cls.__dict__:
                raise TypeError(f'{cls.__name__}.{name} is reserved by Package.')
        if isinstance(cls.__dict__.get('prefix'), _TreeBuilder):
            raise TypeError(f'{cls.__name__}.prefix is reserved for the package prefix.')
        builders = {}
        for parent in reversed(cls.__mro__[1:]):
            builders.update(getattr(parent, '_class_builders', {}))
        for name, value in cls.__dict__.items():
            if isinstance(value, _TreeBuilder):
                builders[name] = value
            else:
                builders.pop(name, None)
        cls._class_builders = {}
        for name, builder in builders.items():
            local = copy(builder)
            local.options = dict(builder.options)
            local._package_prefix = str(cls.prefix or '')
            cls._class_builders[name] = local
            setattr(cls, name, local)
        cls._build = classmethod(Package._build_class)
        cls.build = classmethod(Package._force_build_class)

    @staticmethod
    def _build_class(cls, rebuild: bool = False, full: bool = False):
        return Package._build_members(cls.__name__, cls._class_builders.values(), rebuild, full)

    @staticmethod
    def _force_build_class(cls, full: bool = False):
        return cls._build(rebuild=True, full=full)

    @staticmethod
    def _build_members(name, builders, rebuild, full):
        _validate_build_options(rebuild, full)
        with _build_session(full):
            Tree._init_package(name)
            for builder in builders:
                builder._build(rebuild=rebuild, full=full)
            Tree._display_counter(f"{name} built")

    def __init__(self, name, prefix=""):
        self.name = name
        self.prefix = "" if prefix is None else str(prefix)
        self._builders = []
        self._members = {}

    def __getattr__(self, name):
        """Expose registered builders by their unprefixed tree name."""
        members = self.__dict__.get("_members", {})
        if name in members:
            return members[name]
        raise AttributeError(f"Package '{self.name}' has no builder '{name}'")

    def _register(self, decorator):
        def register(function):
            builder = decorator(function)
            if self.prefix:
                local_prefix = builder.options.get("prefix")
                local_prefix = "" if local_prefix is None else str(local_prefix)
                builder.options["prefix"] = (
                    f"{self.prefix} {local_prefix}" if local_prefix else self.prefix
                )
            self._builders.append(builder)
            self._members[snake_case(builder.name)] = builder
            return builder

        return register

    def group(self, name=None, **options):
        """Register a Geometry Nodes group, with the options of group."""
        return self._register(group(name, **options))

    def modifier(self, name=None, **options):
        """Register a modifier, with the options of modifier."""
        return self._register(modifier(name, **options))

    def tool(self, name=None, **options):
        """Register a Geometry Nodes tool in this mixed package."""
        return self._register(tool(name, **options))

    def shader_group(self, name=None, **options):
        """Register a shader group, with the options of shader_group."""
        return self._register(shader_group(name, **options))

    def shader(self, name=None, *, target='ALL', **options):
        """Register a material, with the options of shader."""
        return self._register(shader(name, target=target, **options))

    def _build(self, rebuild: bool = False, full: bool = False):
        """Build registered trees and display their cumulative statistics."""
        return self._build_members(self.name, self._builders, rebuild, full)

    def build(self, full: bool = False):
        """Rebuild all registered trees, optionally including dependencies."""
        return self._build(rebuild=True, full=full)
