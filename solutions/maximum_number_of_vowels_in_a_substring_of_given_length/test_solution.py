from solutions.maximum_number_of_vowels_in_a_substring_of_given_length.solution import (
    Solution,
)

tests = [
    ("Example 1", {"args": {"s": "abciiidef", "k": 3}, "expected": 3}),
    ("Example 2", {"args": {"s": "aeiou", "k": 2}, "expected": 2}),
    ("Example 3", {"args": {"s": "leetcode", "k": 3}, "expected": 2}),
]


def test_maximum_number_of_vowels_in_a_substring_of_given_length(args, expected):
    solution = Solution()

    assert solution.maxVowels(**args) == expected
