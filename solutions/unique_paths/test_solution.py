from solutions.unique_paths.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "m": 3,
                "n": 7,
            },
            "expected": 28,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "m": 3,
                "n": 2,
            },
            "expected": 3,
        },
    ),
]


def test_unique_paths(args, expected):
    solution = Solution()

    assert solution.uniquePaths(**args) == expected
