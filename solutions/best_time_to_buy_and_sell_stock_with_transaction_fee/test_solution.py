from solutions.best_time_to_buy_and_sell_stock_with_transaction_fee.solution import (
    Solution,
)

tests = [
    ("Example 1", {"args": {"prices": [1, 3, 2, 8, 4, 9], "fee": 2}, "expected": 8}),
    ("Example 2", {"args": {"prices": [1, 3, 7, 5, 10, 3], "fee": 3}, "expected": 6}),
]


def test_best_time_to_buy_and_sell_stock_with_transaction_fee(args, expected):
    solution = Solution()

    assert solution.maxProfit(**args) == expected
