from solutions.reverse_vowels_of_a_string.solution import Solution


def test_reverse_vowels_of_a_string():
    solution = Solution()

    assert solution.reverseVowels("IceCreAm") == "AceCreIm"
    assert solution.reverseVowels("leetcode") == "leotcede"
