from solutions.merge_strings_alternately.solution import Solution


def test_merge_alternately():
    solution = Solution()

    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
