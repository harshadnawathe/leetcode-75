from commons.list import ListNode
from solutions.maximum_twin_sum_of_a_linked_list.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"head": ListNode.from_vals([5, 4, 2, 1])},
            "expected": 6,
        },
    ),
    (
        "Example 2",
        {
            "args": {"head": ListNode.from_vals([4, 2, 2, 3])},
            "expected": 7,
        },
    ),
    (
        "Example 3",
        {
            "args": {"head": ListNode.from_vals([1, 100000])},
            "expected": 100001,
        },
    ),
]


def test_maximum_twin_sum_of_a_linked_list(args, expected):
    solution = Solution()

    assert solution.pairSum(**args) == expected
