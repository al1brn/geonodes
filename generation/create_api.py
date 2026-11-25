"""Generate the running Blender version's API and its comparison report.

Prepare core_<major>_<minor> by copying an existing API first. Adjust handwritten
classes for new socket types and update generation/api_<major>_<minor>/node_dims.py.
Review the report, adjust the versioned config.py descriptions, regenerate, then
select the newly written config in the destination's constants.py and restart
Blender to test. Do not edit generated wrappers by hand.
"""
import runpy
from importlib import import_module
from pathlib import Path
from shutil import copy2
from tempfile import TemporaryDirectory

import bpy


def main():
    # Reuse the standalone bootstrap so a not-yet-generated version needs no API import.
    folder = Path(__file__).resolve().parent
    load_generator = runpy.run_path(str(folder / 'regenerate_core.py'))['load_generator']
    generator = load_generator()
    destination = generator.target_core()
    old_config, old_version = generator.core_configuration(destination)
    generate = import_module(generator.__name__ + '.generate')
    gen_config = import_module(generator.__name__ + '.gen_config')
    comparisons = import_module(generator.__name__ + '.compare_versions')

    with TemporaryDirectory(prefix='geonodes-comparison-') as temporary:
        reference = Path(temporary) / old_config.name
        reference.write_bytes(old_config.read_bytes())
        for environment in ('geonodes', 'shadernodes'):
            cross_reference = Path(environment) / 'generated' / 'cross_reference.py'
            if (destination / cross_reference).is_file():
                (reference.parent / cross_reference).parent.mkdir(parents=True, exist_ok=True)
                copy2(destination / cross_reference, reference.parent / cross_reference)
        generate.generate()
        gen_config.write_file()
        version_name = bpy.app.version_string.replace('.', '_').replace(' ', '_')
        new_config = destination / f'config_{version_name}.py'
        report = comparisons.render_report(comparisons.compare_versions(reference, new_config))

    report_path = folder / f'comparison_{version_name}.md'
    report_path.write_text(report, encoding='utf-8')
    print(report)
    print('\n' + '=' * 100)
    print('Generation completed')
    print(f'Previous Blender version : {old_version}')
    print(f'Current Blender version  : {bpy.app.version_string}')
    print(f'API destination          : {destination}')
    print(f'Configuration            : {new_config}')
    print(f'Comparison report        : {report_path}')
    print('=' * 100)


if __name__ == '__main__':
    main()
