from commons.tree import TreeNode
from solutions.search_in_a_binary_search_tree.solution import Solution

tree1 = TreeNode.from_vals([4, 2, 7, 1, 3])
assert tree1 is not None

tests = [
    (
        "Example 1",
        {"args": {"root": tree1, "val": 2}, "expected": tree1.get_node_with_val(2)},
    ),
    (
        "Example 2",
        {
            "args": {"root": TreeNode.from_vals([4, 2, 7, 1, 3]), "val": 5},
            "expected": None,
        },
    ),
]


def test_search_in_a_binary_search_tree(args, expected):
    solution = Solution()

    assert solution.searchBST(**args) == expected
