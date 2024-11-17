from commons.tree import TreeNode
from solutions.maximum_depth_of_binary_tree.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"root": TreeNode.from_vals([3, 9, 20, None, None, 15, 7])},
            "expected": 3,
        },
    ),
    (
        "Example 2",
        {
            "args": {"root": TreeNode.from_vals([1, None, 2])},
            "expected": 2,
        },
    ),
]


def test_maximum_depth_of_binary_tree(args, expected):
    solution = Solution()

    assert solution.maxDepth(**args) == expected
