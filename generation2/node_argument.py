"""Contextual wrappers for socket and parameter generation.

NodeInfo prepares names, receiver selection and argument ordering;
NodeImplementation assembles the contributions. The wrappers never mutate their
introspection source. ``NodeParameter`` is currently named ``NodeParam``.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from .node_socket import NodeSocket
    from .node_param import NodeParam
    from .typealiases import TypeAliases

_UNSET = object()


@dataclass
class NodeCallArguments:
    """Python expressions to assemble into one Node call.

    Dictionary values are source expressions, not runtime values. Socket keys
    and parameter names remain ordinary strings so the assembler handles their
    serialization only once. Expansion lists contain bare expressions: the
    assembler adds ** inside named_sockets or among the node's keywords.
    """

    positional: list[str] = field(default_factory=list)
    named_sockets: dict[str, str] = field(default_factory=dict)
    parameters: dict[str, str] = field(default_factory=dict)
    named_socket_expansions: list[str] = field(default_factory=list)
    parameter_expansions: list[str] = field(default_factory=list)


@dataclass
class NodeArgument:
    """One socket or parameter as used by a particular generated function.

    ``name`` is the final Python name, already deduplicated by the caller.
    ``aliases`` contains (socket UI name, final Python name) pairs, in resolution
    order; the last non-None argument wins, as in gen_node_call.
    FIXED accepts Python values, including None. COMPUTED accepts a Python
    expression in ``value`` and optional preparation statements in ``computation``.
    A multi-input SELF still exposes *name for additional values.
    NAMED_ITEMS and ANONYMOUS_ITEMS have source=None: they describe a dynamic
    collection rather than an introspected socket/parameter. Named items expose
    name={} and **kwargs_name; anonymous items expose *name.
    """

    source: NodeSocket | NodeParam | None
    name: str
    role: Literal['ARGUMENT', 'SELF', 'FIXED', 'COMPUTED', 'NAMED_ITEMS', 'ANONYMOUS_ITEMS'] = 'ARGUMENT'
    value: Any = _UNSET
    computation: str = ''
    aliases: tuple[tuple[str, str], ...] = ()
    socket_name: str | None = None
    kwargs_name: str = 'named_items'
    _is_socket: bool = field(init=False, repr=False)

    def __post_init__(self):
        self._is_socket = hasattr(self.source, 'identifier')
        if self.role in ('NAMED_ITEMS', 'ANONYMOUS_ITEMS'):
            if self.source is not None or self.aliases or self.value is not _UNSET or self.computation:
                raise ValueError('Items roles do not wrap a socket/parameter or carry a value/computation')
            return
        if self._is_socket and self.socket_name is None:
            self.socket_name = self.source.socket_name
        if not self._is_socket and not hasattr(self.source, 'param_type'):
            raise TypeError('source must describe a NodeSocket or NodeParam')
        if self.role not in ('ARGUMENT', 'SELF', 'FIXED', 'COMPUTED'):
            raise ValueError(f'Unknown argument role: {self.role!r}')
        if self.role == 'SELF' and not self._is_socket:
            raise ValueError('Only a socket can be the receiver')
        if self.role in ('FIXED', 'COMPUTED') and self.value is _UNSET:
            raise ValueError(f'{self.role} requires a value')
        if self.role == 'COMPUTED' and not isinstance(self.value, str):
            raise TypeError('A computed value must be a Python source expression')
        if self.aliases and (not self._is_socket or self.source.is_multi or self.role != 'ARGUMENT'):
            raise ValueError('Aliases require an ordinary, non-multi socket argument')

    def get_typing(self, type_aliases: TypeAliases | None = None) -> str | None:
        """Render intrinsic typing, optionally registering enum type aliases."""
        if self.role in ('NAMED_ITEMS', 'ANONYMOUS_ITEMS'):
            return 'Socket'
        typing = (self.source.class_name or 'Socket') if self._is_socket else self.source.typing
        if isinstance(typing, list):
            if type_aliases is not None:
                return type_aliases.literal(typing, prefix=f'T_{self.name.upper()}')
            return 'Literal[' + ', '.join(repr(value) for value in typing) + ']'
        return typing

    def _exposed_names(self):
        if self.aliases:
            return self.aliases
        return ((self.socket_name, self.name),) if self._is_socket else ((self.source.name, self.name),)

    def get_header(self, type_aliases: TypeAliases | None = None) -> list[str]:
        """Return argument fragments; the assembler supplies self/cls separately."""
        if self.role == 'NAMED_ITEMS':
            return [f'{self.name}={{}}', f'**{self.kwargs_name}']
        if self.role == 'ANONYMOUS_ITEMS':
            return [f'*{self.name}']
        if self.role in ('FIXED', 'COMPUTED'):
            return []
        typing = self.get_typing(type_aliases)
        annotation = f': {typing}' if typing else ''
        if self._is_socket:
            if self.source.is_multi:
                return [f'*{self.name}{annotation}']
            if self.role == 'SELF':
                return []
            return [f'{name}{annotation}=None' for _, name in self._exposed_names()]
        return [f'{self.name}{annotation}={self.source.value!r}']

    def get_arg_doc(self) -> list[str]:
        """Return NumPy-style documentation blocks for exposed arguments."""
        if self.role == 'NAMED_ITEMS':
            return [f'{self.name} : dict, optional\n    Dynamic sockets supplied by name.',
                    f'**{self.kwargs_name} : Socket\n    Dynamic sockets supplied by keyword.']
        if self.role == 'ANONYMOUS_ITEMS':
            return [f'*{self.name} : Socket\n    Values for anonymous dynamic sockets.']
        if not self.get_header():
            return []
        typing = self.get_typing() or 'object'
        if self._is_socket:
            multiple = self.source.is_multi
            suffix = ' (multiple values)' if multiple else ' (default: None)'
            optional = '' if multiple else ', optional'
            identifier = f', identifier {self.source.identifier!r}' if self.aliases else ''
            return [f'{name} : {typing}{optional}\n'
                    f'    Socket {ui_name!r}{identifier}{suffix}'
                    for ui_name, name in self._exposed_names()]
        if self.source.enums:
            typing = '{' + ', '.join(repr(value) for value in self.source.enums) + '}'
            if self.source.param_type == 'ENUM_FLAG':
                typing = f'set[{typing}]'
        return [f'{self.name} : {typing}, optional\n'
                f'    Node parameter {self.source.name!r} (default: {self.source.value!r})']

    def get_fixed_doc(self) -> list[str]:
        """Return fixed-value/receiver descriptions, without section headings."""
        if self.role == 'SELF':
            multi = 'multi ' if self.source.is_multi else ''
            return [f'self on {multi}socket {self.socket_name!r}']
        if self.role != 'FIXED':
            return []
        if self._is_socket:
            return [f'Socket {self.socket_name!r} set to {self.value!r}']
        return [f'parameter {self.source.name!r} = {self.value!r}']

    def get_computed_doc(self) -> list[str]:
        """Describe computed expressions separately from fixed Python values."""
        if self.role != 'COMPUTED':
            return []
        name = self.socket_name if self._is_socket else self.source.name
        return [f'{name!r} computed as {self.value}' +
                (f' ({self.computation})' if self.computation else '')]

    def get_code(self, *, socket_mapping: str = 'named_sockets') -> list[str]:
        """Return preparation statements before Node creation.

        Alias resolution runs after the assembler initializes socket_mapping
        with the contributions from get_node_call. Other computations can run
        before that initialization.
        """
        if self.role == 'COMPUTED':
            return self.computation.splitlines()
        if not self.aliases:
            return []
        target = f'{socket_mapping}[{self._socket_key()!r}]'
        return [f'{target} = None'] + [
            f'if {name} is not None: {target} = {name}' for _, name in self.aliases]

    def _socket_key(self):
        return self.source.group_name or f'ID_{self.source.identifier}'

    def get_node_call(self) -> NodeCallArguments:
        """Return structured contributions, preserving the existing call rules."""
        result = NodeCallArguments()
        if self.role == 'NAMED_ITEMS':
            result.named_socket_expansions.append(self.name)
            result.parameter_expansions.append(self.kwargs_name)
            return result
        if self.role == 'ANONYMOUS_ITEMS':
            result.positional.append(f'*{self.name}')
            return result
        if self.role == 'FIXED':
            value = repr(self.value)
        elif self.role == 'COMPUTED':
            value = self.value
        elif self.role == 'SELF':
            value = 'self'
        else:
            value = self.name

        if not self._is_socket:
            result.parameters[self.source.name] = value
        elif self.role in ('ARGUMENT', 'SELF') and self.source.is_multi:
            result.positional = (['self'] if self.role == 'SELF' else []) + [f'*{self.name}']
        elif self.role in ('FIXED', 'COMPUTED'):
            result.named_sockets[self.socket_name] = value
        else:
            result.named_sockets[self._socket_key()] = 'None' if self.aliases else value
        return result
