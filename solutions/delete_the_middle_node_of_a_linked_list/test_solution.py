from solutions.delete_the_middle_node_of_a_linked_list.solution import Solution
from commons.list import ListNode

tests = [
    (
        "Example 1",
        {
            "args": {
                "head": ListNode.from_vals([1, 3, 4, 7, 1, 2, 6]),
            },
            "expected": ListNode.from_vals([1, 3, 4, 1, 2, 6]),
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "head": ListNode.from_vals([1, 2, 3, 4]),
            },
            "expected": ListNode.from_vals([1, 2, 4]),
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "head": ListNode.from_vals([2, 1]),
            },
            "expected": ListNode.from_vals([2]),
        },
    ),
]


def test_delete_the_middle_node_of_a_linked_list(args, expected):
    solution = Solution()

    assert solution.deleteMiddle(**args) == expected
