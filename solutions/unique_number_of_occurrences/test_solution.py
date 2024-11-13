from solutions.unique_number_of_occurrences.solution import Solution

tests = [
    ("Example 1", {"args": {"arr": [1, 2, 2, 1, 1, 3]}, "expected": True}),
    (
        "Example 2",
        {
            "args": {
                "arr": [1, 2],
            },
            "expected": False,
        },
    ),
    (
        "Example 3",
        {"args": {"arr": [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]}, "expected": True},
    ),
]


def test_unique_number_of_occurrences(args, expected):
    solution = Solution()

    assert solution.uniqueOccurrences(**args) == expected
