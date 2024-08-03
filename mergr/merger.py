from collections.abc import Callable
from typing import Any, ClassVar, TypeAlias

MergeFn: TypeAlias = Callable[[Any, Any], Any]
Strategies: TypeAlias = dict[type | tuple[type, ...], MergeFn]


class Merger:
    strategies: ClassVar[Strategies]
    default_strategy: MergeFn

    _strategies: Strategies

    def __init__(
        self,
        strategies: Strategies | None = None,
        default_strategy: MergeFn = lambda a, b: a,
    ) -> None:
        if hasattr(self.__class__, "strategies"):
            _strategies = dict(self.__class__.strategies)
        else:
            _strategies = {}

        if strategies:
            _strategies.update(strategies)

        self._strategies = _strategies
        self.default_strategy = default_strategy

    def pick_strategy(self, a: Any) -> MergeFn:
        exact_type_strategy = self._strategies.get(type(a))

        if exact_type_strategy:
            return exact_type_strategy
        else:
            for types, strategy in self._strategies.items():
                if type(types) is tuple and type(a) in types:
                    return strategy

        return self.default_strategy
