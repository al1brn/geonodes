"""Run in Blender to regenerate core_<major>_<minor>; other versions remain intact."""

import sys
from importlib import import_module
from importlib.machinery import ModuleSpec
from pathlib import Path
from types import ModuleType

import bpy


def load_generator():
    # Works as a standalone .py or as a text inside the generation .blend.
    script_path = Path(globals().get('__file__', '')).resolve()
    if script_path.is_file():
        generation_folder = script_path.parent
    elif bpy.data.filepath:
        generation_folder = Path(bpy.data.filepath).resolve().parent
    else:
        raise RuntimeError('Save the Blender file in the generator folder first.')
    if not (generation_folder / 'gen_config.py').is_file():
        raise RuntimeError('The script or Blender file must be in the generator folder.')
    package_folder = generation_folder.parent
    generator_name = f'geonodes.{generation_folder.name}'

    # Do not initialize the public API just to run the generator.
    if 'geonodes' not in sys.modules:
        package = ModuleType('geonodes')
        package.__package__ = 'geonodes'
        package.__path__ = [str(package_folder)]
        package.__spec__ = ModuleSpec('geonodes', loader=None, is_package=True)
        package.__spec__.submodule_search_locations = package.__path__
        sys.modules['geonodes'] = package

    return import_module(generator_name)


def main():
    """Overwrite only the API named for this Blender major/minor release."""
    generator = load_generator()
    destination = generator.target_core()
    generate = import_module(generator.__name__ + '.generate')
    gen_config = import_module(generator.__name__ + '.gen_config')
    generate.generate()
    gen_config.write_file()
    print(f'Regeneration completed — Blender {bpy.app.version_string}: {destination}')


if __name__ == '__main__':
    main()
