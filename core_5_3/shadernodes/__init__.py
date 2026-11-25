"""shadernodes environment; concrete classes are loaded lazily."""
from .shadernodes import ShaderNodes


def __getattr__(name):
    from importlib import import_module
    if name in ('sockets', 'generated'):
        return import_module('.' + name, __name__)
    generated = import_module('.generated', __name__)
    return getattr(generated, name)
