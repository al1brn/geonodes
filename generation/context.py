"""Select versioned generation data without initializing a core API."""

import sys
from importlib import import_module, util
from pathlib import Path

import bpy

from .._versions import core_name


def load_kernel(core_folder, module_name):
    """Load only the kernel package; never execute the enclosing core __init__.py."""
    if module_name in sys.modules:
        return sys.modules[module_name]
    folder = Path(core_folder) / 'kernel'
    if not (folder / '__init__.py').is_file():
        raise FileNotFoundError(f'Kernel package not found: {folder}')
    spec = util.spec_from_file_location(
        module_name, folder / '__init__.py', submodule_search_locations=[str(folder)]
    )
    module = util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        for name in list(sys.modules):
            if name == module_name or name.startswith(module_name + '.'):
                del sys.modules[name]
        raise
    return module


_package_folder = Path(__file__).resolve().parent.parent
_core_name = core_name(bpy.app.version)
_data_name = f'api_{bpy.app.version[0]}_{bpy.app.version[1]}'
_data_folder = Path(__file__).resolve().parent / _data_name
if not (_data_folder / '__init__.py').is_file():
    raise FileNotFoundError(f'Generation descriptions not found: {_data_folder}')

config = import_module('.' + _data_name + '.config', __package__)
node_dims = import_module('.' + _data_name + '.node_dims', __package__)
kernel = load_kernel(
    _package_folder / _core_name,
    __package__ + '._' + _core_name + '_kernel',
)

# Explicit engine dependencies, all sourced from the selected version.
ATTRIBUTE_CLASSES = kernel.ATTRIBUTE_CLASSES
CLASS_NAMES = kernel.CLASS_NAMES
CamelCase = kernel.CamelCase
DATA_TYPE_HOMONYMS = kernel.DATA_TYPE_HOMONYMS
DOMAIN_CLASSES = kernel.DOMAIN_CLASSES
GEOMETRY_CLASSES = kernel.GEOMETRY_CLASSES
POINT_DOMAIN_CLASSES = kernel.POINT_DOMAIN_CLASSES
PYTHON_TYPES = kernel.PYTHON_TYPES
SOCKET_SHAPES = kernel.SOCKET_SHAPES
TREE_MODULES = kernel.TREE_MODULES
TREE_TYPES = kernel.TREE_TYPES
get_class_name = kernel.get_class_name
get_param_ui_name = kernel.get_param_ui_name
get_singular = kernel.get_singular
get_socket_type = kernel.get_socket_type
snake_case = kernel.snake_case

ADDITIONAL_IMPLEMENTATIONS = config.ADDITIONAL_IMPLEMENTATIONS
ADD_LOOP = config.ADD_LOOP
AUTO_INPUT_TYPE_NODES = config.AUTO_INPUT_TYPE_NODES
DEFAULT_IMPLEMENTATION = config.DEFAULT_IMPLEMENTATION
DEPRECATED_NODES = config.DEPRECATED_NODES
HANDWRITTEN_IMPLEMENTATIONS = config.HANDWRITTEN_IMPLEMENTATIONS
ITEM_IMPLEMENTATION = config.ITEM_IMPLEMENTATION
LOOP_ONLY = config.LOOP_ONLY
NO_STATIC_CODE = config.NO_STATIC_CODE
PROPERTIES = config.PROPERTIES
REPLACE = config.REPLACE
STATIC_IMPLEMENTATIONS = config.STATIC_IMPLEMENTATIONS
STATIC_IMPLEMENTATION_ONLY = config.STATIC_IMPLEMENTATION_ONLY

