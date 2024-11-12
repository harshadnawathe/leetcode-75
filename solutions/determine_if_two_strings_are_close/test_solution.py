from solutions.determine_if_two_strings_are_close.solution import Solution
import pytest

tests = [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True),
    ("uau", "ssx", False),
    ("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff", False),
]


@pytest.mark.parametrize("word1, word2, want", tests)
def test_determine_if_two_strings_are_close(word1: str, word2: str, want: bool):
    solution = Solution()

    assert solution.closeStrings(word1, word2) == want
