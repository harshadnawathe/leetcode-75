from solutions.count_ways_to_build_good_strings.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "low": 3,
                "high": 3,
                "zero": 1,
                "one": 1,
            },
            "expected": 8,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "low": 2,
                "high": 3,
                "zero": 1,
                "one": 2,
            },
            "expected": 5,
        },
    ),
]


def test_count_ways_to_build_good_strings(args, expected):
    solution = Solution()

    assert solution.countGoodStrings(**args) == expected
