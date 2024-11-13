from solutions.find_the_highest_altitude.solution import Solution

tests = [
    ("Example 1", {"args": {"gain": [-5, 1, 5, 0, -7]}, "expected": 1}),
    ("Example 2", {"args": {"gain": [-4, -3, -2, -1, 4, 3, 2]}, "expected": 0}),
]


def test_find_the_highest_altitude(args, expected):
    solution = Solution()

    assert solution.largestAltitude(**args) == expected
