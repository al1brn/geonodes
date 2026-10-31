"""Function builders for Geometry Nodes and shader trees.

Decorated functions expose explicit construction and node insertion::

    @geo_group("Create Plank")
    def create_plank():
        Mesh.Cube().out()

    create_plank.build(rebuild=False)
    # Inside another tree: create_plank() inserts a Group node.

Tree options belong to the decorator. Use .build() to execute the Python builder
inside its tree context; its rebuild argument overrides the decorator policy.
Call the decorated object inside a tree to insert a Group node using the same
socket interface as G(). Existing trees are preserved without executing the
builder when rebuild is false; missing trees are always built. Outputs still
use socket.out(). Material builders support .build() only.
"""

from functools import update_wrapper
import bpy

from .geonodes import GeoNodes
from .shadernodes import ShaderNodes
from .treeclass import Tree
from .nodeclass import G
from .scripterror import NodeError
from .utils import snake_case

__all__ = ["geo_group", "geo_modifier", "shader_group", "shader_material", "Package"]


class _TreeBuilder:
    """A Python construction function and its callable Blender group interface."""

    _building = set()

    def __init__(self, function, tree_class, name, is_group, options):
        update_wrapper(self, function)
        self.function = function
        self.tree_class = tree_class
        self.is_group = is_group
        self.options = dict(options)
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
        return f"{prefix} {self.name}" if prefix else self.name

    @property
    def _build_key(self):
        namespace = "material" if self.tree_class is ShaderNodes and not self.is_group else "node_group"
        return namespace, self.full_name

    def build(self, *args, rebuild=None, **kwargs):
        """Execute the construction function, forwarding Python arguments."""
        options = dict(self.options)
        policy = "replace_material" if self.tree_class is ShaderNodes and not self.is_group else "rebuild"
        if policy == "replace_material" and "rebuild" in options:
            options[policy] = options.pop("rebuild")
        if rebuild is not None:
            options[policy] = rebuild

        key = self._build_key
        if key in self._building:
            raise NodeError(f"Circular build dependency for '{self.full_name}'.")
        self._building.add(key)
        try:
            result = None
            with self.tree_class(self.name, is_group=self.is_group, **options) as tree:
                if tree._rebuild:
                    result = self.function(*args, **kwargs)
            return result
        finally:
            self._building.remove(key)

    def rebuild(self, *args, **kwargs):
        """Force construction, forwarding Python arguments to the builder."""
        kwargs["rebuild"] = True
        return self.build(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """Insert a Group node, with the positional/keyword socket API of G."""
        if self.tree_class is ShaderNodes and not self.is_group:
            raise TypeError(f"'{self.full_name}' is a material; use .build() to construct it.")
        if Tree.current_tree() is None:
            raise NodeError(f"Calling '{self.full_name}' requires an active tree. Use .build() to construct it.")
        if self._build_key in self._building:
            raise NodeError(f"Circular build dependency for '{self.full_name}'.")
        if bpy.data.node_groups.get(self.full_name) is None:
            self.build(rebuild=False)
        return G._call_group(self.full_name, *args, **kwargs)


def _tree_decorator(tree_class, name, is_group, options):
    def decorate(function):
        return _TreeBuilder(function, tree_class, name, is_group, options)
    return decorate


def geo_group(name=None, **options):
    """Declare a Geometry Nodes group with .build() and a callable socket interface.

    Options are forwarded to GeoNodes, with is_group=True. If omitted, the
    tree name is derived from the function name: my_group becomes My Group,
    and _my_group becomes .My Group. Explicit names are kept unchanged.
    The construction function's return value is preserved by .build();
    a skipped build returns None.
    """
    return _tree_decorator(GeoNodes, name, True, options)


def geo_modifier(name=None, **options):
    """Declare a Geometry Nodes modifier, with GeoNodes options and is_group=False."""
    return _tree_decorator(GeoNodes, name, False, options)


def shader_group(name=None, **options):
    """Declare a shader group, with ShaderNodes options and is_group=True."""
    return _tree_decorator(ShaderNodes, name, True, options)


def shader_material(name=None, **options):
    """Declare a material, with ShaderNodes options and is_group=False.

    Both rebuild and replace_material are accepted as decorator options.
    The call-time rebuild argument overrides either option.
    """
    return _tree_decorator(ShaderNodes, name, False, options)


class Package:
    """Register tree builders and build them in declaration order.

    Declare the package and its decorated functions at module level::

        furniture = Package("Furniture")

        @furniture.geo_group("Create Plank")
        def create_plank():
            Mesh.Cube().out()

        @furniture.geo_modifier("Add Plank")
        def add_plank():
            create_plank().out()

        def demo(rebuild=False):
            furniture.build(rebuild=rebuild)

    Registration does not execute the builders. Each has .build() for individual
    reconstruction and a direct group-call interface inside other trees.
    Construction functions must have no required arguments for package.build();
    use defaults or enclosing variables for their Python configuration.
    """

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

    def geo_group(self, name=None, **options):
        """Register a Geometry Nodes group, with the options of geo_group."""
        return self._register(geo_group(name, **options))

    def geo_modifier(self, name=None, **options):
        """Register a modifier, with the options of geo_modifier."""
        return self._register(geo_modifier(name, **options))

    def shader_group(self, name=None, **options):
        """Register a shader group, with the options of shader_group."""
        return self._register(shader_group(name, **options))

    def shader_material(self, name=None, **options):
        """Register a material, with the options of shader_material."""
        return self._register(shader_material(name, **options))

    def build(self, rebuild=None):
        """Build all registered trees and display their cumulative statistics.

        With rebuild=None, each decorator keeps its own build policy. Passing
        True or False overrides that policy for every builder in the package.
        Dependencies must be declared before the builders that use them.
        """
        Tree._init_package(self.name)
        for builder in self._builders:
            builder.build(rebuild=rebuild)
        Tree._display_counter(f"{self.name} built")

    def rebuild(self):
        """Force reconstruction of every registered tree."""
        return self.build(rebuild=True)
