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
        default_strategy: MergeFn = lambda a, b: a,
        strategies: Strategies | None = None,
    ) -> None:
        if hasattr(self.__class__, "strategies"):
            _strategies = dict(self.__class__.strategies)
        else:
            _strategies = {}

        if strategies:
            _strategies.update(strategies)

        self._strategies = _strategies
        self.default_strategy = default_strategy
