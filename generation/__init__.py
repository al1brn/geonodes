"""Generation utilities and Blender-version destination selection."""

from pathlib import Path
import bpy

from .._versions import core_configuration, core_name


def target_core(folder=None):
    """Write only to the existing core_<major>_<minor> for running Blender."""
    root = Path(__file__).resolve().parent.parent if folder is None else Path(folder)
    name = core_name(bpy.app.version)
    if root.name.startswith('core_'):
        if root.name != name:
            raise RuntimeError(f'Blender {tuple(bpy.app.version)} must generate into {name}, not {root.name}.')
        root = root.parent
    destination = root / name
    if not destination.is_dir():
        raise FileNotFoundError(
            f'Destination does not exist: {destination}. '
            'Copy an existing versioned core here before generating a new version.'
        )
    return destination


def __getattr__(name):
    # Keep simple public imports while storing their data in api_<major>_<minor>.
    if name in ('config', 'node_dims', 'kernel'):
        from . import context
        return getattr(context, name)
    raise AttributeError(f'{__name__!r} has no attribute {name!r}')
