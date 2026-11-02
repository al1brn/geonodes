"""Shared handwritten roots, exported lazily to avoid import cycles."""
from importlib import import_module

_CLASSES = {'Socket': 'socket', 'Input': 'socket', 'NodeCache': 'socket', 'Node': 'node', 'Group': 'node', 'G': 'node', 'ColorRamp': 'node', 'NodeCurves': 'node', 'Tree': 'tree', 'Layout': 'tree', 'Panel': 'tree', 'Geometry': 'geometry', 'Boolean': 'boolean', 'Bundle': 'bundle', 'Closure': 'closure', 'Collection': 'collection', 'Color': 'color', 'Float': 'float', 'Font': 'font', 'Image': 'image', 'Integer': 'integer', 'Material': 'material', 'Matrix': 'matrix', 'Menu': 'menu', 'Object': 'object', 'Rotation': 'rotation', 'String': 'string', 'Texture': 'texture', 'Vector': 'vector', 'Shader': 'shader', 'VolumeShader': 'shader', 'Sound': 'sound'}


def __getattr__(name):
    if name not in _CLASSES:
        raise AttributeError(name)
    return getattr(import_module('.' + _CLASSES[name], __name__), name)
