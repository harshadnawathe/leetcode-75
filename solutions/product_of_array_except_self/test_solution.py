from solutions.product_of_array_except_self.solution import Solution

tests = [
    ("Example 1", {"args": {"nums": [1, 2, 3, 4]}, "expected": [24, 12, 8, 6]}),
    ("Example 2", {"args": {"nums": [-1, 1, 0, -3, 3]}, "expected": [0, 0, 9, 0, 0]}),
]


def test_product_of_array_except_self(args, expected):
    solution = Solution()

    assert solution.productExceptSelf(**args) == expected
