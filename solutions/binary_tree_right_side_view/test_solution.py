from commons.tree import TreeNode
from solutions.binary_tree_right_side_view.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "root": TreeNode.from_vals([1, 2, 3, None, 5, None, 4]),
            },
            "expected": [1, 3, 4],
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "root": TreeNode.from_vals([1, None, 3]),
            },
            "expected": [1, 3],
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "root": TreeNode.from_vals([]),
            },
            "expected": [],
        },
    ),
]


def test_binary_tree_right_side_view(args, expected):
    solution = Solution()

    assert solution.rightSideView(**args) == expected
