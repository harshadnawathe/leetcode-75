from solutions.online_stock_span.solution import StockSpanner
from commons.helper import MethodInvoker

tests = [
    (
        "Example 1",
        {
            "calls": [
                "StockSpanner",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
            ],
            "args": [[], [100], [80], [60], [70], [60], [75], [85]],
            "expected": [None, 1, 1, 1, 2, 1, 4, 6],
        },
    ),
    (
        "Example 2",
        {
            "calls": ["StockSpanner", "next", "next", "next", "next", "next"],
            "args": [[], [31], [41], [48], [59], [79]],
            "expected": [None, 1, 2, 3, 4, 5],
        },
    ),
    (
        "Example 3",
        {
            "calls": [
                "StockSpanner",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
            ],
            "args": [[], [28], [14], [28], [35], [46], [53], [66], [80], [87], [88]],
            "expected": [None, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10],
        },
    ),
]


def test_online_stock_span(calls, args, expected):
    invoker = MethodInvoker(StockSpanner)

    assert invoker.invoke_all(calls, args) == expected
