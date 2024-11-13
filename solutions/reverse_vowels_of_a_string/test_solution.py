from solutions.reverse_vowels_of_a_string.solution import Solution

tests = [
    ("Example 1", {"args": {"s": "IceCreAm"}, "expected": "AceCreIm"}),
    ("Example 2", {"args": {"s": "leetcode"}, "expected": "leotcede"}),
]


def test_reverse_vowels_of_a_string(args, expected):
    solution = Solution()

    assert solution.reverseVowels(**args) == expected
