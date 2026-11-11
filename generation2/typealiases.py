"""Collect reusable Literal aliases, independently of the generation environment."""

from __future__ import annotations

import keyword
from collections.abc import Iterable


class TypeAliases:
    """One registry per generation; the caller chooses where to write source.

    Values are Python values, not source expressions. Equivalent Literals share
    an alias regardless of their order or the requested prefix. The first
    registration determines the name and the order used in the generated file.
    """

    def __init__(self, max_len: int = 100):
        self.max_len = max_len
        self._aliases = {}
        self._names = {}
        self._counts = {}

    def __len__(self):
        return len(self._aliases)

    def literal(self, values: Iterable, prefix: str = 'DATA_TYPE') -> str:
        """Register string, bytes, integer, boolean or None literal values.

        Return the existing alias name, or create PREFIX_1, PREFIX_2, etc.
        Boolean and integer values remain distinct (True is not literal 1).
        """
        if not prefix.isidentifier() or keyword.iskeyword(prefix):
            raise ValueError(f'Invalid alias prefix: {prefix!r}')
        if isinstance(values, (str, bytes)):
            raise TypeError('Expected an iterable of literal values, not a single string')

        unique = {}
        for value in values:
            if type(value) not in (str, bytes, int, bool, type(None)):
                raise TypeError(f'Unsupported literal value: {value!r}')
            unique.setdefault((type(value), value), value)
        if not unique:
            raise ValueError('A Literal alias requires at least one value')

        key = frozenset(unique)
        if key in self._names:
            return self._names[key]

        index = self._counts.get(prefix, 0) + 1
        name = f'{prefix}_{index}'
        self._counts[prefix] = index
        self._names[key] = name
        self._aliases[name] = tuple(unique.values())
        return name

    def get_doc_string(self, key):
        """Return an alias's values as '{...}' text, or key unchanged.

        Preserve registration order for stable documentation.
        """
        if not isinstance(key, str) or key not in self._aliases:
            return key
        return '{' + ', '.join(repr(value) for value in self._aliases[key]) + '}'

    @property
    def source(self) -> str:
        """Render the generated module, wrapping long Literal definitions."""
        lines = ['# Generated file. Do not edit.', 'from typing import Literal', '']
        for name, values in self._aliases.items():
            items = [repr(value) for value in values]
            line = f'{name} = Literal[' + ', '.join(items) + ']'
            if len(line) <= self.max_len:
                lines.append(line)
            else:
                lines.append(f'{name} = Literal[')
                lines.extend(f'    {item},' for item in items)
                lines.append(']')
        return '\n'.join(lines) + '\n'
