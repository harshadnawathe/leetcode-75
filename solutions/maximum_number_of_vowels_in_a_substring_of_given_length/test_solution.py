from solutions.maximum_number_of_vowels_in_a_substring_of_given_length.solution import (
    Solution,
)


def test_maximum_number_of_vowels_in_a_substring_of_given_length():
    solution = Solution()

    assert solution.maxVowels("abciiidef", 3) == 3
    assert solution.maxVowels("aeiou", 2) == 2
    assert solution.maxVowels("leetcode", 3) == 2
