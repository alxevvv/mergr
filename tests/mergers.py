from types import NoneType
from typing import ClassVar

from mergr.merger import Merger, Strategies


class NoneReplacer(Merger):
    strategies: ClassVar[Strategies] = {
        NoneType: lambda _, b: b,
    }
