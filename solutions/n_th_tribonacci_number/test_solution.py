from solutions.n_th_tribonacci_number.solution import Solution

tests = [
    ("Example 1", {"args": {"n": 4}, "expected": 4}),
    ("Example 2", {"args": {"n": 25}, "expected": 1389537}),
]


def test_n_th_tribonacci_number(args, expected):
    solution = Solution()

    assert solution.tribonacci(**args) == expected
