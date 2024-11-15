from typing import Iterable, Iterator, Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if self is other:
            return True

        if not isinstance(other, ListNode):
            return False

        node, node_other = self, other

        while node and node_other:
            if node.val != node_other.val:
                return False

            node = node.next
            node_other = node_other.next

        return node is None and node_other is None

    def __iter__(self) -> Iterator:
        node = self
        while node:
            yield node.val
            node = node.next

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self))}]"

    @classmethod
    def from_values(cls, values: Iterable) -> Optional["ListNode"]:
        anchor = cls()

        node = anchor
        for value in values:
            node.next = cls(value)
            node = node.next

        return anchor.next
