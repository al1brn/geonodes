"""Compare generated config files without importing Blender.

Usage: python3 generation2/compare_versions.py OLD_CONFIG NEW_CONFIG [-o report.md]
"""

import argparse
import ast
from pathlib import Path
from pprint import pformat


def read_config(path):
    """Read only literal version and node tables, without executing the file."""
    wanted = {'blender_version', 'NODE_NAMES', 'NODE_INFO'}
    values = {}
    for statement in ast.parse(Path(path).read_text(encoding='utf-8')).body:
        if isinstance(statement, ast.Assign):
            for target in statement.targets:
                if isinstance(target, ast.Name) and target.id in wanted:
                    values[target.id] = ast.literal_eval(statement.value)
    for name in ('NODE_NAMES', 'NODE_INFO'):
        if name not in values or not isinstance(values[name], dict):
            raise ValueError(f'{path}: missing or invalid {name}')
    return values


def _changes(old, new, path=()):
    if isinstance(old, dict) and isinstance(new, dict):
        result = []
        for key in sorted(old.keys() | new.keys(), key=str):
            location = (*path, str(key))
            if key not in old:
                result.append({'path': location, 'kind': 'added', 'new': new[key]})
            elif key not in new:
                result.append({'path': location, 'kind': 'removed', 'old': old[key]})
            else:
                result.extend(_changes(old[key], new[key], location))
        return result
    if type(old) is not type(new) or old != new:
        return [{'path': path, 'kind': 'modified', 'old': old, 'new': new}]
    return []


def compare_versions(old_path, new_path, *, include_dimensions=False):
    """Return added, removed and modified nodes per tree, keyed by bl_idname."""
    old, new = read_config(old_path), read_config(new_path)
    result = {'old_version': old.get('blender_version'),
              'new_version': new.get('blender_version'), 'trees': {}}
    for tree in sorted(old['NODE_NAMES'].keys() | new['NODE_NAMES'].keys()):
        before = {identifier: name for name, identifier in old['NODE_NAMES'].get(tree, {}).items()}
        after = {identifier: name for name, identifier in new['NODE_NAMES'].get(tree, {}).items()}
        changes = {'removed': {}, 'added': {}, 'modified': {}}
        for identifier in sorted(before.keys() - after.keys()):
            changes['removed'][identifier] = before[identifier]
        for identifier in sorted(after.keys() - before.keys()):
            changes['added'][identifier] = after[identifier]
        for identifier in sorted(before.keys() & after.keys()):
            descriptions = []
            for config, names in ((old, before), (new, after)):
                if identifier not in config['NODE_INFO']:
                    raise ValueError(f'Missing NODE_INFO for {tree}/{identifier}')
                info = dict(config['NODE_INFO'][identifier])
                if not include_dimensions:
                    info.pop('dims', None)
                descriptions.append({'name': names[identifier], 'info': info})
            details = _changes(*descriptions)
            if details:
                changes['modified'][identifier] = {'name': after[identifier], 'changes': details}
        result['trees'][tree] = changes
    return result


def render_report(comparison):
    lines = [f"# Comparaison Blender {comparison['old_version']} → {comparison['new_version']}", '']
    for tree, groups in comparison['trees'].items():
        lines.extend([f'## {tree}', ''])
        for key, title in (('removed', 'Nœuds supprimés'), ('added', 'Nœuds ajoutés'),
                           ('modified', 'Nœuds modifiés')):
            lines.extend([f'### {title} ({len(groups[key])})', ''])
            if not groups[key]:
                lines.extend(['Aucun.', ''])
            for identifier, entry in groups[key].items():
                name = entry['name'] if key == 'modified' else entry
                lines.append(f'- **{name}** (`{identifier}`)')
                if key == 'modified':
                    for change in entry['changes']:
                        location = ' / '.join(change['path'])
                        values = []
                        for side, label in (('old', 'ancien'), ('new', 'nouveau')):
                            if side in change:
                                value = pformat(change[side], sort_dicts=True, width=10000).replace('\n', ' ')
                                values.append(f'{label}: {value}')
                        lines.append(f"  - {location} ({change['kind']}) : {' → '.join(values)}")
            lines.append('')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('old_config', type=Path)
    parser.add_argument('new_config', type=Path)
    parser.add_argument('-o', '--output', type=Path)
    parser.add_argument('--include-dimensions', action='store_true')
    args = parser.parse_args()
    report = render_report(compare_versions(args.old_config, args.new_config,
                                           include_dimensions=args.include_dimensions))
    if args.output:
        args.output.write_text(report, encoding='utf-8')
    else:
        print(report)


if __name__ == '__main__':
    main()
