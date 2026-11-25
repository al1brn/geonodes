"""Compare generated config files without importing Blender.

Usage: python3 generation/compare_versions.py OLD_CONFIG NEW_CONFIG [-o report.md]
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


def implementation_headers(core_folder, tree_type, identifiers):
    """Read generated signatures without importing either API or Blender."""
    environment = {'GeometryNodeTree': 'geonodes', 'ShaderNodeTree': 'shadernodes'}.get(tree_type)
    path = Path(core_folder) / (environment or '') / 'generated' / 'cross_reference.py'
    references = None
    if environment and identifiers and path.is_file():
        for statement in ast.parse(path.read_text(encoding='utf-8')).body:
            if (isinstance(statement, ast.Assign)
                    and any(isinstance(target, ast.Name) and target.id == 'CROSS_REF'
                            for target in statement.targets)):
                references = ast.literal_eval(statement.value)
                break
        if not isinstance(references, dict):
            raise ValueError(f'{path}: missing or invalid CROSS_REF')

    result = {}
    for identifier in identifiers:
        destinations = {} if references is None else references.get(identifier, {})
        headers = []
        signatures = {}
        for class_name, methods in sorted(destinations.items()):
            for method in methods:
                key = (class_name, method['func_name'], bool(method.get('is_get')),
                       bool(method.get('is_set')), bool(method.get('is_classmethod')))
                signatures[key] = method['signature']
                if class_name == 'nd':
                    continue
                decorator = ('@classproperty ' if method.get('is_get') and method.get('is_classmethod')
                             else '@property ' if method.get('is_get')
                             else '@setter ' if method.get('is_set')
                             else '@classmethod ' if method.get('is_classmethod') else '')
                header = f"{decorator}{class_name}.{method['func_name']}{method['signature']}"
                if header not in headers:
                    headers.append(header)
        result[identifier] = {
            'headers': headers,
            'static_only': not headers and bool(destinations.get('nd')),
            'signatures': signatures,
        }
    return result


def _argument_names(signature):
    """Parse argument order without evaluating defaults or annotations."""
    arguments = ast.parse(f'def function{signature}:\n    pass\n').body[0].args
    names = [argument.arg for argument in (*arguments.posonlyargs, *arguments.args)]
    if names and names[0] in ('self', 'cls'):
        names.pop(0)
    if arguments.vararg:
        names.append('*' + arguments.vararg.arg)
    names.extend(argument.arg for argument in arguments.kwonlyargs)
    if arguments.kwarg:
        names.append('**' + arguments.kwarg.arg)
    return names


def compare_arguments(old_implementations, new_implementations):
    """Classify additions to matching methods, including static nd accessors."""
    before = old_implementations.get('signatures', {})
    after = new_implementations.get('signatures', {})
    changes = []
    for key in sorted(before.keys() & after.keys()):
        old_names = _argument_names(before[key])
        new_names = _argument_names(after[key])
        added = [name for name in new_names if name not in old_names]
        # Appending/inserting requires the old arguments to remain in order.
        # Removals and reorderings remain visible in Old/New version signatures.
        if not added or [name for name in new_names if name in old_names] != old_names:
            continue
        changes.append({
            'method': f'{key[0]}.{key[1]}',
            'kind': 'appended' if new_names[:len(old_names)] == old_names else 'inserted',
            'arguments': added,
        })
    return changes


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
        old_headers = implementation_headers(Path(old_path).parent, tree, changes['modified'])
        new_headers = implementation_headers(
            Path(new_path).parent, tree, changes['added'].keys() | changes['modified'].keys()
        )
        changes['added_implementations'] = {
            identifier: new_headers[identifier] for identifier in changes['added']
        }
        for identifier, entry in changes['modified'].items():
            entry['old_implementations'] = old_headers[identifier]
            entry['new_implementations'] = new_headers[identifier]
            entry['argument_changes'] = compare_arguments(old_headers[identifier], new_headers[identifier])
        result['trees'][tree] = changes
    return result


def _signature_lines(implementations):
    if implementations.get('static_only'):
        return ['- Static only']
    if implementations.get('headers'):
        return [f'- `{header}`' for header in implementations['headers']]
    return ['- Implémentations non renseignées dans les références croisées.']


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
                if key == 'modified':
                    lines.extend([f'#### {name}', '', f'Blender identifier: `{identifier}`', ''])
                    for label, field in (('Old version', 'old_implementations'),
                                         ('New version', 'new_implementations')):
                        lines.extend([f'##### {label}', ''])
                        lines.extend(_signature_lines(entry.get(field, {})))
                        lines.append('')
                    if entry.get('argument_changes'):
                        lines.extend(['##### Argument changes', ''])
                        for change in entry['argument_changes']:
                            label = ('arguments appended' if change['kind'] == 'appended'
                                     else 'CAUTION: arguments inserted')
                            names = ', '.join(f'`{name}`' for name in change['arguments'])
                            lines.append(f"- `{change['method']}` — {label}: {names}")
                        lines.append('')
                    lines.extend(['##### Changes', ''])
                else:
                    lines.append(f'- **{name}** (`{identifier}`)')
                if key == 'added':
                    implementations = groups.get('added_implementations', {}).get(identifier, {})
                    lines.extend('  ' + line for line in _signature_lines(implementations))
                if key == 'modified':
                    for change in entry['changes']:
                        location = ' / '.join(change['path'])
                        values = []
                        for side, label in (('old', 'ancien'), ('new', 'nouveau')):
                            if side in change:
                                value = pformat(change[side], sort_dicts=True, width=10000).replace('\n', ' ')
                                values.append(f'{label}: {value}')
                        lines.append(f"- {location} ({change['kind']}) : {' → '.join(values)}")
                    lines.append('')
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
