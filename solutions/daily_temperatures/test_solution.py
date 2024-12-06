from solutions.daily_temperatures.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]},
            "expected": [1, 1, 4, 2, 1, 1, 0, 0],
        },
    ),
    (
        "Example 2",
        {
            "args": {"temperatures": [30, 40, 50, 60]},
            "expected": [1, 1, 1, 0],
        },
    ),
    (
        "Example 3",
        {
            "args": {"temperatures": [30, 60, 90]},
            "expected": [1, 1, 0],
        },
    ),
]


def test_daily_temperatures(args, expected):
    solution = Solution()

    assert solution.dailyTemperatures(**args) == expected
