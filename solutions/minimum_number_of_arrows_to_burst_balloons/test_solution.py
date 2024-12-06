from solutions.minimum_number_of_arrows_to_burst_balloons.solution import Solution

tests = [
    (
        "Example 1",
        {"args": {"points": [[10, 16], [2, 8], [1, 6], [7, 12]]}, "expected": 2},
    ),
    (
        "Example 2",
        {"args": {"points": [[1, 2], [3, 4], [5, 6], [7, 8]]}, "expected": 4},
    ),
    (
        "Example 3",
        {"args": {"points": [[1, 2], [2, 3], [3, 4], [4, 5]]}, "expected": 2},
    ),
]


def test_minimum_number_of_arrows_to_burst_balloons(args, expected):
    solution = Solution()

    assert solution.findMinArrowShots(**args) == expected
