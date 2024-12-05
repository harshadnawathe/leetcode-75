from solutions.search_suggestions_system.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "products": ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
                "searchWord": "mouse",
            },
            "expected": [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "products": ["havana"],
                "searchWord": "havana",
            },
            "expected": [
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
                ["havana"],
            ],
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "products": ["havana"],
                "searchWord": "tatiana",
            },
            "expected": [[], [], [], [], [], [], []],
        },
    ),
]


def test_search_suggestions_system(args, expected):
    solution = Solution()

    assert solution.suggestedProducts(**args) == expected
