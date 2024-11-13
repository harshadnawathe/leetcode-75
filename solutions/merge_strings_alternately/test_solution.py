from solutions.merge_strings_alternately.solution import Solution

tests = [
    ("Example 1", {"args": {"word1": "abc", "word2": "pqr"}, "expected": "apbqcr"}),
    ("Example 2", {"args": {"word1": "ab", "word2": "pqrs"}, "expected": "apbqrs"}),
    ("Example 3", {"args": {"word1": "abcd", "word2": "pq"}, "expected": "apbqcd"}),
]


def test_merge_alternately(args, expected):
    solution = Solution()

    assert solution.mergeAlternately(**args) == expected
