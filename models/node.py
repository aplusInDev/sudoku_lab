from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class Node:
    state: List[List[int]]
    parent: Optional['Node'] = None
    depth: int = 0
    cost: float = 0
    heuristic: float = 0
    position: Tuple[int, int] = (-1, -1)  # Position of last filled cell

    def __lt__(self, other: 'Node') -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def get_path(self) -> List['Node']:
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return path[::-1]
