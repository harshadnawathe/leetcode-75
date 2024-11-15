from typing import Optional
from commons.list import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = odd = ListNode(next=head)
        even_head = even = ListNode()

        is_odd = True
        while head is not None:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next

            head = head.next
            is_odd = not is_odd

        odd.next = even_head.next
        even.next = None

        return odd_head.next
