from solutions.house_robber.solution import Solution

tests = [
    ("Example 1", {"args": {"nums": [1, 2, 3, 1]}, "expected": 4}),
    ("Example 2", {"args": {"nums": [2, 7, 9, 3, 1]}, "expected": 12}),
]


def test_house_robber(args, expected):
    solution = Solution()

    assert solution.rob(**args) == expected
