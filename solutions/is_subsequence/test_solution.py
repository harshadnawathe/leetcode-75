from solutions.is_subsequence.solution import Solution


def test_is_subsequence():
    solution = Solution()

    assert solution.isSubsequence(s="abc", t="ahbgdc") is True
    assert solution.isSubsequence(s="axc", t="ahbgdc") is False
