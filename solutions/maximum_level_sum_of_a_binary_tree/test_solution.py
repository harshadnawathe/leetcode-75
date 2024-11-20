from commons.tree import TreeNode
from solutions.maximum_level_sum_of_a_binary_tree.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"root": TreeNode.from_vals([1, 7, 0, 7, -8, None, None])},
            "expected": 2,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "root": TreeNode.from_vals(
                    [989, None, 10250, 98693, -89388, None, None, None, -32127]
                )
            },
            "expected": 2,
        },
    ),
]


def test_maximum_level_sum_of_a_binary_tree(args, expected):
    solution = Solution()

    assert solution.maxLevelSum(**args) == expected
