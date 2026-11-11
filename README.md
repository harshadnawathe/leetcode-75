# leetcode-75

[![Build Status](https://github.com/harshadnawathe/leetcode-75/actions/workflows/ci.yaml/badge.svg)](https://github.com/harshadnawathe/leetcode-75/actions/workflows/ci.yaml)

Repository to practice leetcode problems from study plan [Leetcode 75](https://leetcode.com/studyplan/leetcode-75/).

## Requirements

Python@3.14

> [!TIP]
> The version is declared once as `requires-python` in
> [pyproject.toml](./pyproject.toml), which the CI workflow reads. The
> [mise](https://mise.jdx.dev/) [file](./.mise.toml) pins the same version for
> local development.

## Setup

With the assumption that you are in a Python 3.14 virtual environment, run:

```sh
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Project structure

Solutions can be found in the `solutions` package.

Schematic below shows the project structure:

```txt

leetcode-75/
├── commons/                        # Common types / utilities
├── solutions/
│   ├── two_sum/
│   │   ├── solution.py             # Solution code for the problem
│   │   ├── test_solution.py        # Pytest file to test the solution
│   │   └── README.md               # Problem description and LeetCode link
│   ├── add_two_numbers/
│   │   ├── solution.py
│   │   ├── test_solution.py
│   │   └── README.md
│   └── ...                         # Additional problem directories
├── pyproject.toml                  # Project and tool configuration
├── requirements.txt                # Project dependencies
├── requirements-dev.txt            # Project dev dependencies (pytest, etc.)
└── README.md                       # Project-level README
```

> [!NOTE]
>
> The project configures `Python3` the coding environment as mentioned
> [here](https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages)

### Package structure

For each problem there is a separate package that contains,

- README file
- Python source code
- Python test code

#### Generating solution package

The repository provides a simple Python [script](./leetcode.py) to
generate a solution package for a given LeetCode problem.
It reads the problem from the LeetCode GraphQL api, converts the title slug
to snake case, and creates the following structure under the 'solutions/'
directory:

```txt
solutions/<problem_snake_case>/
├── __init__.py                # Empty file to mark as package
├── solution.py                # The Python3 code snippet from LeetCode
├── test_solution.py           # A table driven test for the snippet signature
└── README.md                  # Contains the problem name and link
```

Usage: `leetcode.py <leetcode_problem_url|title_slug>`

Example:

```sh
./leetcode.py "https://leetcode.com/problems/reverse-words-in-a-string/"
./leetcode.py reverse-words-in-a-string
```

The generated `test_solution.py` mirrors the signature found in
`solution.py`: a single call on a `Solution` instance for most problems, and
a [`MethodInvoker`](./commons/helper.py) driven list of calls for design
problems. Every value to be filled in from the problem examples is written as
`...`, which also keeps the scaffolded test red until it is completed.

> [!NOTE]
>
> The script degrades rather than giving up, so a problem can be scaffolded
> even when a precondition does not hold:
>
> - Files that already exist are kept, so the script can be rerun on a half
>   done problem to fill in the gaps without touching solved code.
> - When LeetCode cannot be reached, a bare title slug is enough to write the
>   package, with the code snippet left as a `TODO`.
> - A premium problem, or one without a Python3 snippet, still gets its
>   README and test skeleton.
> - When no solution signature can be parsed, a generic test skeleton is
>   written instead.
>
> Everything that could not be fetched or parsed is reported on stderr. The
> only fatal errors are the ones that leave the script without a directory to
> write into.

> [!TIP]
>
> For information about the script run,
>
> ```sh
> ./leetcode.py help
> ```

## Tests

Tests are written in table-driven style.

An example test code is given below,

```python
# imports omitted for brevity

# The list of tests to be executed
tests = [
    (                        # Test case
      "Example 1",           # Test identifier - must be a string or int
      {
        "args": {            # Arguments passed to the function under test
                             # `args` value is passed to test driver.
          "str1": "ABCABC",  # key must be equal to the parameter name
          "str2": "ABC"
        },
        "expected": "ABC"    # Expected result to verified against the actual
                             # `expected` value is passed to test driver.
      },
    ),
    ("Example 2", {"args": {"str1": "ABABAB", "str2": "ABAB"}, "expected": "AB"}),
    ("Example 3", {"args": {"str1": "LEET", "str2": "CODE"}, "expected": ""}),
]

# Test driver function that runs for the each test defines in the tests with
# corresponding values of `args` and `expected`
def test_greatest_common_divisor_of_strings(args, expected):
    solution = Solution()

    assert solution.gcdOfStrings(**args) == expected
```

> [!NOTE]
>
> - The `pytest_generate_tests` [hook](./conftest.py) will
>   parameterise the test function for each of the test case defined in the list.
> - If the `tests` variable is not found then `pytest` will issue a warning.

### Running tests

To run all tests execute command below.

```sh
pytest
```

To run tests for a specific problem execute command below.

```sh
pytest solutions/greatest_common_divisor_of_strings/
```
