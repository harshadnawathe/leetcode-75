from typing import Optional
from commons.list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr is not None:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next

        return prev
