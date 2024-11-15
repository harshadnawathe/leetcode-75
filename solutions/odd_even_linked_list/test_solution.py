from commons.list import ListNode
from solutions.odd_even_linked_list.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"head": ListNode.from_values([1, 2, 3, 4, 5])},
            "expected": ListNode.from_values([1, 3, 5, 2, 4]),
        },
    ),
    (
        "Example 2",
        {
            "args": {"head": ListNode.from_values([2, 1, 3, 5, 6, 4, 7])},
            "expected": ListNode.from_values([2, 3, 6, 7, 1, 5, 4]),
        },
    ),
]


def test_odd_even_linked_list(args, expected):
    solution = Solution()

    assert solution.oddEvenList(**args) == expected
