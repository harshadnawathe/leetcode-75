from solutions.koko_eating_bananas.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "piles": [3, 6, 7, 11],
                "h": 8,
            },
            "expected": 4,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "piles": [30, 11, 23, 4, 20],
                "h": 5,
            },
            "expected": 30,
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "piles": [30, 11, 23, 4, 20],
                "h": 6,
            },
            "expected": 23,
        },
    ),
]


def test_koko_eating_bananas(args, expected):
    solution = Solution()

    assert solution.minEatingSpeed(**args) == expected
