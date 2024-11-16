from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None

    @classmethod
    def from_vals(cls, vals: Iterable) -> Optional["ListNode"]:
        anchor = cls()

        node = anchor
        for val in vals:
            node.next = cls(val)
            node = node.next

        return anchor.next
