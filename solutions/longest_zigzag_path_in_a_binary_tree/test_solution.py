from commons.tree import TreeNode
from solutions.longest_zigzag_path_in_a_binary_tree.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "root": TreeNode.from_vals(
                    [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
                )
            },
            "expected": 3,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "root": TreeNode.from_vals(
                    [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
                )
            },
            "expected": 4,
        },
    ),
    (
        "Example 3",
        {
            "args": {"root": TreeNode.from_vals([1])},
            "expected": 0,
        },
    ),
    (
        "Example 4",
        {
            "args": {"root": TreeNode.from_vals([1, 1, 1])},
            "expected": 1,
        },
    ),
]


def test_longest_zigzag_path_in_a_binary_tree(args, expected):
    solution = Solution()

    assert solution.longestZigZag(**args) == expected
