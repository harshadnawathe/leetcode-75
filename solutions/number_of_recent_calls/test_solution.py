from itertools import starmap
from typing import Any, List
from commons.helper import MethodInvoker
from solutions.number_of_recent_calls.solution import RecentCounter

tests = [
    (
        "Example 1",
        {
            "calls": ["RecentCounter", "ping", "ping", "ping", "ping"],
            "args": [
                [],
                [1],
                [100],
                [3001],
                [3002],
            ],
            "expected": [None, 1, 2, 3, 3],
        },
    ),
]


def test_number_of_recent_calls(calls: List[str], args: List[List[Any]], expected):
    invoker = MethodInvoker(RecentCounter)

    assert list(starmap(invoker.invoke, zip(calls, args))) == expected
