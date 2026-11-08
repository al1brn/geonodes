"""Resolve concrete socket classes from the active node-tree environment."""
from collections.abc import MutableMapping
from importlib import import_module

READY = False
ROOTS = {}
ENVIRONMENTS = {
    'GeometryNodeTree': 'geonodes',
    'ShaderNodeTree': 'shadernodes',
}


def current_environment():
    from .root.tree import Tree
    tree = Tree.current_tree()
    return ENVIRONMENTS[tree._btree.bl_idname] if tree is not None else 'geonodes'


def concrete_class(name):
    return getattr(import_module('.' + current_environment() + '.generated', __package__), name)


class EnvironmentType(type):
    """Shared roots also act as context-aware public constructors."""
    def __call__(cls, *args, **kwargs):
        if READY and ROOTS.get(cls.__name__) is cls:
            return type.__call__(concrete_class(cls.__name__), *args, **kwargs)
        return super().__call__(*args, **kwargs)

    def __getattribute__(cls, name):
        if READY and not name.startswith('_') and name not in ('SOCKET_TYPE', 'DOMAIN_NAME'):
            class_name = type.__getattribute__(cls, '__name__')
            if ROOTS.get(class_name) is cls:
                return getattr(concrete_class(class_name), name)
        return super().__getattribute__(name)

    def __getattr__(cls, name):
        if READY and ROOTS.get(cls.__name__) is cls:
            return getattr(concrete_class(cls.__name__), name)
        raise AttributeError(name)


class ClassRegistry(MutableMapping):
    """Keep the shared type registry while resolving its concrete classes."""
    def __init__(self):
        self.roots = {}

    def __getitem__(self, key):
        root = self.roots[key]
        if not READY:
            return root
        try:
            return concrete_class(root.__name__)
        except AttributeError:
            raise KeyError(key) from None

    def __setitem__(self, key, value):
        self.roots[key] = value

    def __delitem__(self, key):
        del self.roots[key]

    def __iter__(self):
        if not READY:
            return iter(self.roots)
        generated = import_module('.' + current_environment() + '.generated', __package__)
        return (key for key, root in self.roots.items() if hasattr(generated, root.__name__))

    def __len__(self):
        return sum(1 for _ in self)


class ModuleFacade:
    def __init__(self, module, attribute=None):
        self._MODULE = module
        self._ATTRIBUTE = attribute

    def __getattr__(self, name):
        module = import_module('.' + current_environment() + '.generated.' + self._MODULE, __package__)
        target = getattr(module, self._ATTRIBUTE) if self._ATTRIBUTE else module
        return getattr(target, name)
