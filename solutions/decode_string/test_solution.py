from solutions.decode_string.solution import Solution

tests = [
    ("Example 1", {"args": {"s": "3[a]2[bc]"}, "expected": "aaabcbc"}),
    ("Example 2", {"args": {"s": "3[a2[c]]"}, "expected": "accaccacc"}),
    ("Example 3", {"args": {"s": "2[abc]3[cd]ef"}, "expected": "abcabccdcdcdef"}),
    (
        "Example 4",
        {
            "args": {"s": "13[a]12[bc]"},
            "expected": "aaaaaaaaaaaaabcbcbcbcbcbcbcbcbcbcbcbc",
        },
    ),
]


def test_decode_string(args, expected):
    solution = Solution()

    assert solution.decodeString(**args) == expected
