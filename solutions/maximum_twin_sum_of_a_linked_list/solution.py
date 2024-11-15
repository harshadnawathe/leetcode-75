from typing import Optional
from commons.list import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head.next.next

        prev = None
        while fast and fast.next:
            next = head.next
            head.next = prev
            prev = head
            head = next

            fast = fast.next.next

        right = head.next
        head.next = prev

        max_sum = 0
        while head and right:
            sum = head.val + right.val

            if max_sum < sum:
                max_sum = sum

            head = head.next
            right = right.next

        return max_sum
