from solutions.single_number.solution import Solution

tests = [
    ("Example 1", {"args": {"nums": [2, 2, 1]}, "expected": 1}),
    ("Example 2", {"args": {"nums": [4, 1, 2, 1, 2]}, "expected": 4}),
    ("Example 3", {"args": {"nums": [1]}, "expected": 1}),
]


def test_single_number(args, expected):
    solution = Solution()

    assert solution.singleNumber(**args) == expected
