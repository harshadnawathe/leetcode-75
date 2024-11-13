from solutions.removing_stars_from_a_string.solution import Solution

tests = [
    ("Example 1", {"args": {"s": "leet**cod*e"}, "expected": "lecoe"}),
    ("Example 2", {"args": {"s": "erase*****"}, "expected": ""}),
]


def test_removing_stars_from_a_string(args, expected):
    solution = Solution()

    assert solution.removeStars(**args) == expected
