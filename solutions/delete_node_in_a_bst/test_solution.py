from commons.tree import TreeNode
from solutions.delete_node_in_a_bst.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"root": TreeNode.from_vals([5, 3, 6, 2, 4, None, 7]), "key": 3},
            "expected": TreeNode.from_vals([5, 2, 6, None, 4, None, 7]),
        },
    ),
    (
        "Example 2",
        {
            "args": {"root": TreeNode.from_vals([5, 3, 6, 2, 4, None, 7]), "key": 0},
            "expected": TreeNode.from_vals([5, 3, 6, 2, 4, None, 7]),
        },
    ),
    (
        "Example 3",
        {
            "args": {"root": None, "key": 0},
            "expected": None,
        },
    ),
]


def test_delete_node_in_a_bst(args, expected):
    solution = Solution()

    assert solution.deleteNode(**args) == expected
