from dataclasses import dataclass, field, fields, replace as dataclass_replace, KW_ONLY
from typing import Any, ClassVar

# ====================================================================================================
# Implementation specifications for gen_source_code
# ====================================================================================================

@dataclass
class NodeCall:

    # Core info
    method_type         : str
    method_name         : str

    _: KW_ONLY

    # Destination transmise à l’orchestrateur, non utilisée par gen_source_code.
    class_name          : str | None = None

    # Instance specific
    self_socket         : str | None = None  
    is_jump             : bool = False
    geo_selection   : bool = True

    # Returns
    return_kind         : str = 'OUT'
    return_socket       : str | None = None

    # Implementaton options
    auto_data_type      : str | None = None
    fixed_sockets       : dict[str, Any] = field(default_factory=dict)
    last_sockets        : tuple[str, ...] = ()
    parameters          : dict[str, Any] = field(default_factory=dict)

    # inline code
    in_line             : str | None = None

    # Meta
    implement           : bool = True

    # Debug
    category            : str | None = None
    rules               : str = ""

    _FUNC_TYPES: ClassVar[dict[str, tuple[str | None, str | None]]] = {
        'FUNCTION'          : (None, None),
        'STATIC_METHOD'     : ('@staticmethod', None),
        'CLASS_METHOD'      : ('@classmethod', 'cls'),
        'CLASS_PROPERTY'    : ('@utils.classproperty', 'cls'),
        'METHOD'            : (None, 'self'),
        'GETTER'            : ('@property', 'self'),
        'SETTER'            : (None, 'self'),
    }
    _METHOD_TYPES = ('METHOD', 'GETTER', 'SETTER')
    _CLASS_TYPES = ('CLASS_METHOD', 'CLASS_PROPERTY')

    def __str__(self):
        return f"<NodeCall {self.method_name} {self.method_type}>"

    def __repr__(self):
        lines = ["NodeCall"]
        for f in fields(self):
            if f.name not in ["rules"]:
                lines.append(f"{f.name:15}: {getattr(self, f.name)!r}")

        s = "\n- ".join(lines)

        return s + "\n> ".join([" "] + self.rules.split("\n")) + "\n"

    # ===========================================================================
    # Make sure method fields are compatible with non methodtypes
    # ===========================================================================

    def __post_init__(self):
        if self.method_type not in self._METHOD_TYPES:
            self.self_socket = None
            self.is_jump = False
            self.geo_selection = False    


    # ===========================================================================
    # Properties
    # ===========================================================================

    @property
    def first_arg(self) -> str | None:
        return self._FUNC_TYPES[self.method_type][1]

    @property
    def has_self(self) -> bool:
        return self.first_arg == 'self'

    @property
    def is_class_method(self):
        return self.method_type in self._CLASS_TYPES

    @property
    def is_instance_method(self):
        return self.method_type in self._METHOD_TYPES

    @property
    def is_function(self):
        return self.method_type == 'FUNCTION'

    @property
    def decorator(self) -> str | None:
        """Decorator source for this implementation."""
        if self.method_type == 'SETTER':
            return f'@{self.method_name}.setter'
        return self._FUNC_TYPES[self.method_type][0]

    # ===========================================================================
    # Consistency check
    # ===========================================================================

    def _check(self):

        def dump():
            print("Node call error")
            print('-'*30)
            print(">", "\n> ".join(self.rules.split("\n")))
            print()
            print(f"- {self.class_name=}")
            print(f"- {self.method_type=}")
            print(f"- {self.method_name=}")
            
            print()


        if self.class_name is not None and not isinstance(self.class_name, str):
            dump()
            raise TypeError(f'class_name must describe one destination or be None, not {self.class_name!r}')
        if not isinstance(self.method_name, str):
            dump()
            raise TypeError("method_name must describe one function, not multiple variants")
        if self.method_type not in self._FUNC_TYPES:
            dump()
            raise ValueError(f"Unknown implementation type: {self.method_type!r}")
        
        if (not self.implement) or (self.in_line is not None):
            return self
        
        if self.has_self:
            if self.self_socket is None:
                dump()
                raise ValueError(f"{self.method_name}: self_socket is required for {self.method_type}")
            
        else:
            if self.self_socket is not None:
                dump()
                raise ValueError(f"{self.method_name}: self_socket requires an instance method")
            if self.is_jump:
                dump()
                raise ValueError(f"{self.method_name}: is_jump requires an instance method")

        return self
    
    # ===========================================================================
    # Constructors
    # ===========================================================================

    @classmethod
    def function(
            cls, 
            method_name: str,
            in_line: str | None = None,
            **kwargs) -> "NodeCall":
        return cls('FUNCTION', method_name, in_line=in_line, **kwargs)

    @classmethod
    def static_method(
            cls,
            method_name: str,
            in_line: str | None = None,
            **kwargs) -> "NodeCall":
        return cls('STATIC_METHOD', method_name, in_line=in_line, **kwargs)

    @classmethod
    def class_method(
            cls, 
            method_name: str,
            in_line: str | None = None,
            **kwargs) -> "NodeCall":
        return cls('CLASS_METHOD', method_name, in_line=in_line, **kwargs)

    @classmethod
    def class_property(
            cls, 
            method_name: str,
            in_line: str | None = None,
            **kwargs) -> "NodeCall":
        return cls('CLASS_PROPERTY', method_name, in_line=in_line, **kwargs)

    @classmethod
    def method(
            cls, 
            method_name: str,
            in_line: str | None = None,
            **kwargs) -> "NodeCall":
        return cls('METHOD', method_name, in_line=in_line, **kwargs)

    @classmethod
    def getter(
            cls, 
            method_name: str,
            in_line: str | None = None,
            **kwargs) -> "NodeCall":
        return cls('GETTER', method_name, in_line=in_line, **kwargs)

    @classmethod
    def setter(
            cls, 
            method_name: str,
            in_line: str | None = None,
            **kwargs) -> "NodeCall":
        return cls('SETTER', method_name, in_line=in_line, **kwargs)

    # ===========================================================================
    # Replace
    # ===========================================================================

    def replace(self, **kwargs) -> "NodeCall":

        updates = {}

        for name, value in kwargs.items():
            current = getattr(self, name)

            if name in ('fixed_sockets', 'parameters'):
                updates[name] = current | value

            elif name == 'last_sockets':
                updates[name] = current + tuple(value)

            else:
                updates[name] = value

        return dataclass_replace(self, **updates)
    
    
# ====================================================================================================
# Implementation loop
# ====================================================================================================

class NodeCalls(list):

    def __init__(self, *node_calls):
        
        super().__init__()

        for node_call in node_calls:
            if isinstance(node_call, NodeCall):
                self.append(node_call)
            elif isinstance(node_call, NodeCalls):
                self.extend(node_call)
            else:
                raise ValueError(f"{node_call} is not in (NodeCall, NodeCalls)")

    def __str__(self):
        return f"<List of {len(self)} NodeCall>"

    def __repr__(self):
        return f"{str(self)}:" + "\n    - ".join([""] + [repr(nc) for nc in self])

    # ===========================================================================
    # A field can be a single value or a list of values
    # ===========================================================================

    @staticmethod
    def expand_dict(**kwargs) -> list[dict]:

        lengths = [len(v) for v in kwargs.values() if isinstance(v, list)]
        count = max(lengths, default=1)

        assert all(n in (1, count) for n in lengths), \
            f"Incompatible list lengths: {lengths}"

        return [
            {
                key: value[i if len(value) > 1 else 0]
                    if isinstance(value, list) else value
                for key, value in kwargs.items()
            }
            for i in range(count)
        ]    

    # ===========================================================================
    # Constructors
    # ===========================================================================

    # ---------------------------------------------------------------------------
    # Central constructor
    # ---------------------------------------------------------------------------

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(*(NodeCall(**values) for values in cls.expand_dict(**kwargs)))    

    # ---------------------------------------------------------------------------
    # Specialized constructors
    # ---------------------------------------------------------------------------

    @classmethod
    def function(cls, method_name, in_line=None, **kwargs):
        return cls.from_dict(
            method_type='FUNCTION',
            method_name=method_name,
            in_line=in_line,
            **kwargs,
        )

    @classmethod
    def static_method(cls, method_name, in_line=None, **kwargs):
        return cls.from_dict(
            method_type='STATIC_METHOD',
            method_name=method_name,
            in_line=in_line,
            **kwargs,
        )

    @classmethod
    def class_method(cls, method_name, in_line=None, **kwargs):
        return cls.from_dict(
            method_type='CLASS_METHOD',
            method_name=method_name,
            in_line=in_line,
            **kwargs,
        )

    @classmethod
    def class_property(cls, method_name, in_line=None, **kwargs):
        return cls.from_dict(
            method_type='CLASS_PROPERTY',
            method_name=method_name,
            in_line=in_line,
            **kwargs,
        )

    @classmethod
    def method(cls, method_name, in_line=None, **kwargs):
        return cls.from_dict(
            method_type='METHOD',
            method_name=method_name,
            in_line=in_line,
            **kwargs,
        )

    @classmethod
    def getter(cls, method_name, in_line=None, **kwargs):
        return cls.from_dict(
            method_type='GETTER',
            method_name=method_name,
            in_line=in_line,
            **kwargs,
        )

    @classmethod
    def setter(cls, method_name, in_line=None, **kwargs):
        return cls.from_dict(
            method_type='SETTER',
            method_name=method_name,
            in_line=in_line,
            **kwargs,
        )

    # ===========================================================================
    # Replace / overrides : one dict or more to replace some field
    # ===========================================================================

    def replace(self, **kwargs) -> "NodeCalls":
        node_calls = type(self)()

        for values in type(self).expand_dict(**kwargs):
            node_calls.extend(
                node_call.replace(**values)
                for node_call in self
            )

        return node_calls

    def overrides(self, overrides: dict[str, Any] | list[dict]) -> "NodeCalls":

        if isinstance(overrides, dict):
            overrides = [overrides]

        node_calls = type(self)()
        for override in overrides:
            node_calls.extend(self.replace(**override))

        return node_calls 

    # ===========================================================================
    # Loop on a field
    # ===========================================================================

    def loop_on_field(self,
            field_name, 
            field_values, 
            call_back = lambda field, **kw: kw, 
            **kwargs):

        assert field_name not in kwargs, f"But why ???? {field_name} in {tuple(kwargs.keys())}"

        node_calls = NodeCalls()
        for field_value in field_values:
            for node_call in self:
                node_calls.append(node_call.replace(**{field_name: field_value, **call_back(field_value, **kwargs)}))

        return node_calls

