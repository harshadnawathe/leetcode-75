from solutions.reverse_words_in_a_string.solution import Solution


def test_reverse_words_in_a_string():
    solution = Solution()

    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"
