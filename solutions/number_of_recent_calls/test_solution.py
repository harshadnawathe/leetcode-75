from itertools import starmap
from typing import Any, List, Optional

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


class MethodInvoker:
    """Handles method invocation on a target class instance based on method names."""

    def __init__(self, target_class):
        self.target_class = target_class
        self.instance = None

    def call(self, method_name: str, args) -> Optional[int]:
        """
        Invokes the specified method with given arguments.
        Handles constructor calls by creating a new instance.
        """
        if method_name == self.target_class.__name__:
            self.instance = self.target_class()
            return None

        if not hasattr(self.instance, method_name):
            raise ValueError(f"Unknown method: {method_name}")

        method = getattr(self.instance, method_name)
        return method(*args)


def test_number_of_recent_calls(calls: List[str], args: List[List[Any]], expected):
    invoker = MethodInvoker(RecentCounter)

    assert list(starmap(invoker.call, zip(calls, args))) == expected
