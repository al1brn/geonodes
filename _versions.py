"""Read supported Blender versions without initializing either API."""

import ast
from pathlib import Path


def core_configuration(core_folder):
    """Read the active config path and Blender version without importing the API."""
    core_folder = Path(core_folder)
    constants = ast.parse((core_folder / 'constants.py').read_text(encoding='utf-8'))
    imports = [node.module for node in constants.body
               if isinstance(node, ast.ImportFrom) and node.level == 1
               and node.module and node.module.startswith('config_')
               and any(alias.name == '*' for alias in node.names)]
    if len(imports) != 1:
        raise RuntimeError(f'Expected one active config import in {core_folder / "constants.py"}.')
    config_path = core_folder / (imports[0] + '.py')
    module = ast.parse(config_path.read_text(encoding='utf-8'))
    versions = [ast.literal_eval(node.value) for node in module.body
                if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == 'blender_version'
                        for target in node.targets)]
    if (len(versions) != 1 or not isinstance(versions[0], tuple)
            or len(versions[0]) != 3
            or any(type(value) is not int for value in versions[0])):
        raise RuntimeError(f'Missing or invalid blender_version in {config_path}.')
    return config_path, versions[0]


def core_name(blender_version):
    """Return the API package name for a Blender major/minor release."""
    major, minor = tuple(blender_version)[:2]
    return f'core_{major}_{minor}'


def select_core(package_folder, blender_version):
    """Load only the package named for Blender's major/minor version."""
    name = core_name(blender_version)
    folder = Path(package_folder) / name
    if not folder.is_dir():
        raise RuntimeError(
            f'No API installed for Blender {blender_version[0]}.{blender_version[1]}: '
            f'missing {name} ({folder}).'
        )
    _, configured_version = core_configuration(folder)
    if tuple(configured_version[:2]) != tuple(blender_version[:2]):
        raise RuntimeError(
            f'{name} contains a configuration for Blender {configured_version}, '
            f'not {tuple(blender_version)}.'
        )
    return name
