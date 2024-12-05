from solutions.longest_common_subsequence.solution import Solution

tests = [
    ("Example 1", {"args": {"text1": "abcde", "text2": "ace"}, "expected": 3}),
    ("Example 2", {"args": {"text1": "abc", "text2": "abc"}, "expected": 3}),
    ("Example 3", {"args": {"text1": "abc", "text2": "def"}, "expected": 0}),
    ("Example 4", {"args": {"text1": "bl", "text2": "yby"}, "expected": 1}),
]


def test_longest_common_subsequence(args, expected):
    solution = Solution()

    assert solution.longestCommonSubsequence(**args) == expected
