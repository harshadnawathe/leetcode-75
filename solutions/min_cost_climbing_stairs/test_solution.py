from solutions.min_cost_climbing_stairs.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "cost": [10, 15, 20],
            },
            "expected": 15,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "cost": [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
            },
            "expected": 6,
        },
    ),
]


def test_min_cost_climbing_stairs(args, expected):
    solution = Solution()

    assert solution.minCostClimbingStairs(**args) == expected
