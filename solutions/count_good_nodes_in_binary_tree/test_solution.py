from commons.tree import TreeNode
from solutions.count_good_nodes_in_binary_tree.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"root": TreeNode.from_vals([3, 1, 4, 3, None, 1, 5])},
            "expected": 4,
        },
    ),
    (
        "Example 2",
        {
            "args": {"root": TreeNode.from_vals([3, 3, None, 4, 2])},
            "expected": 3,
        },
    ),
    (
        "Example 3",
        {
            "args": {"root": TreeNode.from_vals([1])},
            "expected": 1,
        },
    ),
]


def test_count_good_nodes_in_binary_tree(args, expected):
    solution = Solution()

    assert solution.goodNodes(**args) == expected
