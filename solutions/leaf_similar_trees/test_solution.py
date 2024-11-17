from commons.tree import TreeNode
from solutions.leaf_similar_trees.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "root1": TreeNode.from_vals([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
                "root2": TreeNode.from_vals(
                    [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
                ),
            },
            "expected": True,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "root1": TreeNode.from_vals([1, 2, 3]),
                "root2": TreeNode.from_vals([1, 3, 2]),
            },
            "expected": False,
        },
    ),
]


def test_leaf_similar_trees(args, expected):
    solution = Solution()

    assert solution.leafSimilar(**args) == expected
