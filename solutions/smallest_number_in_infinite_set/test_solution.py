from itertools import starmap
from typing import Any, List

from commons.helper import MethodInvoker

from solutions.smallest_number_in_infinite_set.solution import SmallestInfiniteSet

tests = [
    (
        "Example 1",
        {
            "calls": [
                "SmallestInfiniteSet",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
            ],
            "args": [[], [2], [], [], [], [1], [], [], []],
            "expected": [None, None, 1, 2, 3, None, 1, 4, 5],
        },
    ),
    (
        "Example 2",
        {
            "calls": [
                "SmallestInfiniteSet",
                "addBack",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
            ],
            "args": [[], [2], [2], [], [], [], [1], [], [], []],
            "expected": [None, None, None, 1, 2, 3, None, 1, 4, 5],
        },
    ),
]


def test_smallest_number_in_infinite_set(
    calls: List[str], args: List[List[Any]], expected
):
    invoker = MethodInvoker(SmallestInfiniteSet)

    assert list(starmap(invoker.invoke, zip(calls, args))) == expected
