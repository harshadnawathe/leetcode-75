from solutions.counting_bits.solution import Solution

tests = [
    ("Example 1", {"args": {"n": 2}, "expected": [0, 1, 1]}),
    ("Example 2", {"args": {"n": 5}, "expected": [0, 1, 1, 2, 1, 2]}),
]


def test_counting_bits(args, expected):
    solution = Solution()

    assert solution.countBits(**args) == expected
