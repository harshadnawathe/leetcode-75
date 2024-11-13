from solutions.find_pivot_index.solution import Solution

tests = [
    ("Example 1", {"args": {"nums": [1, 7, 3, 6, 5, 6]}, "expected": 3}),
    ("Example 2", {"args": {"nums": [1, 2, 3]}, "expected": -1}),
    ("Example 3", {"args": {"nums": [2, 1, -1]}, "expected": 0}),
]


def test_find_pivot_index(args, expected):
    solution = Solution()

    assert solution.pivotIndex(**args) == expected
