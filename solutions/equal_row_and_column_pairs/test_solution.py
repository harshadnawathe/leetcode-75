from solutions.equal_row_and_column_pairs.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "grid": [[3, 2, 1], [1, 7, 6], [2, 7, 7]],
            },
            "expected": 1,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "grid": [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]],
            },
            "expected": 3,
        },
    ),
]


def test_equal_row_and_column_pairs(expected, args):
    solution = Solution()

    assert solution.equalPairs(**args) == expected


def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    argnames = []
    for test in tests:
        idlist.append(test[0])
        params = test[1]
        argnames = params.keys()
        argvalues.append(params.values())

    metafunc.parametrize(argnames, argvalues, ids=idlist)
