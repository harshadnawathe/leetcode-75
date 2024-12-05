from solutions.edit_distance.solution import Solution

tests = [
    ("Example 1", {"args": {"word1": "horse", "word2": "ros"}, "expected": 3}),
    (
        "Example 2",
        {"args": {"word1": "intention", "word2": "execution"}, "expected": 5},
    ),
    (
        "Example 3",
        {"args": {"word1": "", "word2": "a"}, "expected": 1},
    ),
]


def test_edit_distance(args, expected):
    solution = Solution()

    assert solution.minDistance(**args) == expected
