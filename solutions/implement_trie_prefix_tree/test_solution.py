from commons.helper import MethodInvoker
from solutions.implement_trie_prefix_tree.solution import Trie

tests = [
    (
        "Example 1",
        {
            "calls": [
                "Trie",
                "insert",
                "search",
                "search",
                "startsWith",
                "insert",
                "search",
            ],
            "args": [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            "expected": [None, None, True, False, True, None, True],
        },
    ),
    (
        "Example 2",
        {
            "calls": [
                "Trie",
                "startsWith",
            ],
            "args": [[], ["a"]],
            "expected": [None, False],
        },
    ),
]


def test_implement_trie_prefix_tree(calls, args, expected):
    invoker = MethodInvoker(Trie)

    assert invoker.invoke_all(calls, args) == expected
