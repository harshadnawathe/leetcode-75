from commons.list import ListNode
from solutions.reverse_linked_list.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"head": ListNode.from_vals([1, 2, 3, 4, 5])},
            "expected": ListNode.from_vals([5, 4, 3, 2, 1]),
        },
    ),
    (
        "Example 2",
        {
            "args": {"head": ListNode.from_vals([1, 2])},
            "expected": ListNode.from_vals([2, 1]),
        },
    ),
    (
        "Example 3",
        {
            "args": {"head": ListNode.from_vals([])},
            "expected": ListNode.from_vals([]),
        },
    ),
]


def test_reverse_linked_list(args, expected):
    solution = Solution()

    assert solution.reverseList(**args) == expected
