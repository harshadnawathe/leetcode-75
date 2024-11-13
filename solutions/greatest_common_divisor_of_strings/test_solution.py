from solutions.greatest_common_divisor_of_strings.solution import Solution


tests = [
    ("Example 1", {"args": {"str1": "ABCABC", "str2": "ABC"}, "expected": "ABC"}),
    ("Example 2", {"args": {"str1": "ABABAB", "str2": "ABAB"}, "expected": "AB"}),
    ("Example 3", {"args": {"str1": "LEET", "str2": "CODE"}, "expected": ""}),
]


def test_greatest_common_divisor_of_strings(args, expected):
    solution = Solution()

    assert solution.gcdOfStrings(**args) == expected
