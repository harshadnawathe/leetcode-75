from solutions.container_with_most_water.solution import Solution

tests = [
    ("Example 1", {"args": {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}, "expected": 49}),
    ("Example 2", {"args": {"height": [1, 1]}, "expected": 1}),
]


def test_container_with_most_water(args, expected):
    solution = Solution()

    assert solution.maxArea(**args) == expected
