from solutions.climbing_stairs_ii.solution import Solution

tests = [
    ("Example 1", {"args": {"n": 4, "costs": [1, 2, 3, 4]}, "expected": 13}),
    ("Example 2", {"args": {"n": 4, "costs": [5, 1, 6, 2]}, "expected": 11}),
    ("Example 3", {"args": {"n": 3, "costs": [9, 8, 3]}, "expected": 12}),
    ("Example 4", {"args": {"n": 1, "costs": [9]}, "expected": 10}),
]


def test_climbing_stairs_ii(args, expected):
    solution = Solution()

    assert solution.climbStairs(**args) == expected
