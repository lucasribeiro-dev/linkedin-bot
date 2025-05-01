from typing import Protocol

class ILinkedinRoutineFacade(Protocol):

    def execute(self) -> None: ...