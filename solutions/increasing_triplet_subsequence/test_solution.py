from solutions.increasing_triplet_subsequence.solution import Solution


tests = [
    ("Example 1", {"args": {"nums": [1, 2, 3, 4, 5]}, "expected": True}),
    ("Example 2", {"args": {"nums": [5, 4, 3, 2, 1]}, "expected": False}),
    ("Example 3", {"args": {"nums": [2, 1, 5, 0, 4, 6]}, "expected": True}),
]


def test_increasing_triplet_subsequence(args, expected):
    solution = Solution()

    assert solution.increasingTriplet(**args) == expected
