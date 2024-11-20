from commons.tree import TreeNode
from solutions.lowest_common_ancestor_of_a_binary_tree.solution import Solution

tree1 = TreeNode.from_vals([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
assert tree1 is not None
tree2 = TreeNode.from_vals([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
assert tree2 is not None
tree3 = TreeNode.from_vals([1, 2])
assert tree3 is not None


tests = [
    (
        "Example 1",
        {
            "args": {
                "root": tree1,
                "p": tree1.get_node_with_val(5),
                "q": tree1.get_node_with_val(1),
            },
            "expected": tree1.get_node_with_val(3),
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "root": tree2,
                "p": tree2.get_node_with_val(5),
                "q": tree2.get_node_with_val(4),
            },
            "expected": tree2.get_node_with_val(5),
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "root": tree3,
                "p": tree3.get_node_with_val(1),
                "q": tree3.get_node_with_val(2),
            },
            "expected": tree3.get_node_with_val(1),
        },
    ),
]


def test_lowest_common_ancestor_of_a_binary_tree(args, expected):
    solution = Solution()

    assert solution.lowestCommonAncestor(**args) == expected
