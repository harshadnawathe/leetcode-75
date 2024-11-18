from commons.tree import TreeNode
from solutions.path_sum_iii.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "root": TreeNode.from_vals([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]),
                "targetSum": 8,
            },
            "expected": 3,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "root": TreeNode.from_vals(
                    [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
                ),
                "targetSum": 22,
            },
            "expected": 3,
        },
    ),
]


def test_path_sum_iii(args, expected):
    solution = Solution()

    assert solution.pathSum(**args) == expected
