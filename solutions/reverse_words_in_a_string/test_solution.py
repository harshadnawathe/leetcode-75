from solutions.reverse_words_in_a_string.solution import Solution

tests = [
    ("Example 1", {"args": {"s": "the sky is blue"}, "expected": "blue is sky the"}),
    ("Example 2", {"args": {"s": "  hello world  "}, "expected": "world hello"}),
    ("Example 3", {"args": {"s": "a good   example"}, "expected": "example good a"}),
]


def test_reverse_words_in_a_string(args, expected):
    solution = Solution()

    assert solution.reverseWords(**args) == expected
