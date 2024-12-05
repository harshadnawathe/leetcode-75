from solutions.domino_and_tromino_tiling.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "n": 3,
            },
            "expected": 5,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "n": 1,
            },
            "expected": 1,
        },
    ),
]


def test_domino_and_tromino_tiling(args, expected):
    solution = Solution()

    assert solution.numTilings(**args) == expected
