from solutions.greatest_common_divisor_of_strings.solution import Solution

def test_greatest_common_divisor_of_strings():
    solution = Solution()

    assert solution.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert solution.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert solution.gcdOfStrings("LEET", "CODE") == ""
