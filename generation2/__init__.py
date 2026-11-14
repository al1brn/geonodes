"""Generation utilities and destination selection."""

from pathlib import Path
import bpy

#COMPATIBLE_BLENDER_VERSION = (5, 2, 0)
#BLENDER_VERSION = bpy.app.version


def target_core(folder=None, *, new=True):
    """Resolve the output core, independently of the core used for reading.

    folder may be the geonodes directory or a legacy core/core_new path.
    The destination core must already exist (copy core to core_new first).
    """

    """
    if not new and bpy.app.version > COMPATIBLE_BLENDER_VERSION:
        current = '.'.join(map(str, bpy.app.version))
        supported = '.'.join(map(str, COMPATIBLE_BLENDER_VERSION))
        raise RuntimeError(
            f"Cannot write to core: Blender {current} is newer than its supported "
            f"version {supported}. Generate into core_new instead "
            f"(new_core=True for generate, new=True for write_file). "
            f"To intentionally update core for a minor Blender release, first "
            f"update COMPATIBLE_BLENDER_VERSION in geonodes/__init__.py "
            f"to {bpy.app.version}."
        )
    """
    root = Path(__file__).resolve().parent.parent if folder is None else Path(folder)
    if root.name in ("core", "core_new"):
        root = root.parent
    return root / ("core_new" if new else "core")
