from solutions.minimum_flips_to_make_a_or_b_equal_to_c.solution import Solution

tests = [
    ("Example 1", {"args": {"a": 2, "b": 6, "c": 5}, "expected": 3}),
    ("Example 2", {"args": {"a": 4, "b": 2, "c": 7}, "expected": 1}),
    ("Example 3", {"args": {"a": 1, "b": 2, "c": 3}, "expected": 0}),
]


def test_minimum_flips_to_make_a_or_b_equal_to_c(args, expected):
    solution = Solution()

    assert solution.minFlips(**args) == expected
