from typing import Optional
from commons.list import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow, fast = head, head.next.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if slow.next:
            slow.next = slow.next.next

        return head
