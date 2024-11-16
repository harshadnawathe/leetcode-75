from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None

    @classmethod
    def from_values(cls, values: Iterable) -> Optional["ListNode"]:
        anchor = cls()

        node = anchor
        for value in values:
            node.next = cls(value)
            node = node.next

        return anchor.next
