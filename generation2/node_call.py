"""Data describing one node implementation and its generation variants."""

from dataclasses import dataclass, field, fields, replace as dataclass_replace, KW_ONLY
from typing import Any, ClassVar

# ====================================================================================================
# Implementation specifications for gen_node_call
# ====================================================================================================

@dataclass
class NodeCall:

    # Core info
    method_type         : str
    method_name         : str

    _: KW_ONLY

    # Destination transmise à l’orchestrateur, non utilisée par gen_node_call.
    class_name          : str | None = None

    # Instance specific
    self_socket         : str | None = None  
    is_jump             : bool = False
    use_geo_selection   : bool = True

    # Returns
    return_kind         : str = 'OUT'
    return_socket       : str | None = None

    # Implementaton options
    auto_data_type      : str | None = None
    fixed_sockets       : dict[str, Any] = field(default_factory=dict)
    last_sockets        : tuple[str, ...] = ()
    parameters          : dict[str, Any] = field(default_factory=dict)

    # Meta
    implement           : bool = True
    #domain_loop         : bool = False
    #data_type_loop      : bool = False

    # Debug
    category            : str | None = None
    rules               : list[str] = field(default_factory=list)

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
    _METHOD_FIELDS = (('self_socket', None), ('is_jump', False), ('use_geo_selection', False))

    def __str__(self):
        return f"<NodeCall {self.method_name} {self.method_type}>"

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
            print(f"- {self.class_name=}")
            print(f"- {self.method_type=}")
            print(f"- {self.method_name=}")
            for r in self.rules:
                print(r)
            print()


        if self.class_name is not None and not isinstance(self.class_name, str):
            dump()
            raise TypeError('class_name must describe one destination or be None')
        if not isinstance(self.method_name, str):
            dump()
            raise TypeError("method_name must describe one function, not multiple variants")
        if self.method_type not in self._FUNC_TYPES:
            dump()
            raise ValueError(f"Unknown implementation type: {self.method_type!r}")
        
        if not self.implement:
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
            **kwargs) -> "NodeCall":
        return cls('FUNCTION', method_name, **kwargs)

    @classmethod
    def static_method(
            cls, 
            method_name: str,
            **kwargs) -> "NodeCall":
        return cls('STATIC_METHOD', method_name, **kwargs)

    @classmethod
    def class_method(
            cls, 
            method_name: str,
            **kwargs) -> "NodeCall":
        return cls('CLASS_METHOD', method_name, **kwargs)

    @classmethod
    def class_property(
            cls, 
            method_name: str,
            **kwargs) -> "NodeCall":
        return cls('CLASS_PROPERTY', method_name, **kwargs)

    @classmethod
    def method(
            cls, 
            method_name: str,
            **kwargs) -> "NodeCall":
        return cls('METHOD', method_name, **kwargs)

    @classmethod
    def getter(
            cls, 
            method_name: str,
            **kwargs) -> "NodeCall":
        return cls('GETTER', method_name, **kwargs)

    @classmethod
    def setter(
            cls, 
            method_name: str,
            **kwargs) -> "NodeCall":
        return cls('SETTER', method_name, **kwargs)

    # ===========================================================================
    # Copy
    # ===========================================================================

    def replace(self, method_type=None, **kwargs) -> "NodeCall":
        if method_type is not None:
            kwargs['method_type'] = method_type
            if method_type not in self._METHOD_TYPES:
                for name, value in self._METHOD_FIELDS:
                    kwargs[name] = value

        return dataclass_replace(self, **kwargs)

    # ===========================================================================
    # Loop
    # ===========================================================================

    def loop(self):
        """Simule NodeCalls.loop
        """
        yield self.replace()

    def __iter__(self):
        return self.loop()
    

# ====================================================================================================
# Implementation loop
# ====================================================================================================

class NodeCalls:
    """Produire des variantes d'une NodeCall, éventuellement depuis une boucle."""

    def __init__(self, node_call: "NodeCall | NodeCalls", *other):
        """Encapsuler node_call sans modifier les descriptions qu'elle produit."""
        if not isinstance(node_call, (NodeCall, NodeCalls)):
            raise TypeError('NodeCalls requires an NodeCall or another NodeCalls')
        self.node_call = node_call
        self._overrides = None
        if len(other):
            self._list = [self.node_call, *other]
            self.count = len(self._list)
        else: 
            self._list = None
            self.count = 1

    def __str__(self):
        if self._list is not None:
            return f"<NodeCalls list of {len(self._bunch)} NodeCalls>"
        else:
            return f"<NodeCalls {self.count} NodeCalls>"

    def __repr__(self):
        return f"{str(self)}:" + "\n    - ".join([""] + [repr(nc) for nc in self])

    @classmethod
    def overrides(cls, node_call: "NodeCall | NodeCalls", overrides) -> "NodeCalls":
        """Construire une boucle depuis une liste de dictionnaires.

        Parameters
        ----------
        node_call : NodeCall | NodeCalls
            Description ou boucle de départ.
        overrides : list[dict]
            Un dictionnaire de remplacements par variante, transmis à
            NodeCall.replace(). Les clés peuvent différer entre dictionnaires.
            class_name désigne la classe de destination portée par NodeCall.
        """
        loop = cls(node_call)
        loop._overrides = [dict(values) for values in overrides]
        allowed = {item.name for item in fields(NodeCall)}
        for values in loop._overrides:
            unknown = values.keys() - allowed
            if unknown:
                raise TypeError(f"Unknown NodeCalls fields: {', '.join(sorted(unknown))}")
        loop.count = len(loop._overrides)
        return loop

    @classmethod
    def attributes(cls, node_call: "NodeCall | NodeCalls", **parameters) -> "NodeCalls":
        """Construire une boucle depuis les valeurs de chaque attribut.

        Parameters
        ----------
        node_call : NodeCall | NodeCalls
            Description ou boucle de départ.
        **parameters
            Une liste par attribut, par exemple method_name=['foo', 'bar'].
            Les listes sont parcourues ensemble et ont la même longueur.
            Une valeur seule ou une liste d'un élément est répétée.
            class_name précise la destination de chaque variante.
        """
        count = max((len(values) if isinstance(values, list) else 1
                     for values in parameters.values()), default=1)
        columns = {}
        for name, values in parameters.items():
            if not isinstance(values, list):
                values = [values]
            if len(values) not in (1, count):
                raise ValueError(
                    f"NodeCalls: {name!r} has {len(values)} values; expected 1 or {count}")
            columns[name] = values * count if len(values) == 1 else list(values)
        return cls.overrides(node_call, [
            {name: values[i] for name, values in columns.items()} for i in range(count)])

    @classmethod
    def bunch(cls, *node_calls):
        return cls(*node_calls)
        

    def replace(self, **parameters) -> "NodeCalls":
        """Appliquer les variations par attribut aux résultats de cette boucle."""
        return type(self).attributes(self, **parameters)

    def loop(self):
        """Produire les NodeCall, chacune portant sa class_name.

        Sans remplacements, transmettre les descriptions de départ à l'identique.
        Sinon, produire une copie par dictionnaire, pour chaque description
        de départ. Les remplacements de cette boucle ont priorité.
        """
        if self._list is not None:
            yield from self._list
            return

        bases = (self.node_call.loop() if isinstance(self.node_call, NodeCalls)
                 else [self.node_call])
        if self._overrides is None:
            yield from bases
            return
        
        for node_call in bases:
            for overrides in self._overrides:
                yield node_call.replace(**overrides)

    def __iter__(self):
        return self.loop()
