from typing import Protocol

class IConnectWithPeopleManager(Protocol):
    def connect_with_targets(self,max_connections: int = 10) -> None: ...