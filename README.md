# leetcode-75

[![Build Status](https://github.com/harshadnawathe/leetcode-75/actions/workflows/ci.yaml/badge.svg)](https://github.com/harshadnawathe/leetcode-75/actions/workflows/ci.yaml)

Repository to practice leetcode problems from study plan [Leetcode 75](https://leetcode.com/studyplan/leetcode-75/).

## Requirements

Python@3.11

> [!TIP]
> Refer to [mise](https://mise.jdx.dev/) [file](./.mise.toml) for exact version.

## Setup

With the assumption that you are in a Python 3.11 virtual environment, run:

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
generate a solution package for a given LeetCode problem URL.
It extracts the problem name from the URL, converts it to snake case,
and creates the following structure under the 'solutions/' directory:

```txt
solutions/<problem_snake_case>/
├── __init__.py                # Empty file to mark as package
├── solution.py                # Contains an initial Solution class
├── test_solution.py           # Contains a sample test function for Solution
└── README.md                  # Contains the problem description and link
```

Usage: `leetcode.py <leetcode_problem_url>`

Example:

```sh
./leetcode.py "https://leetcode.com/problems/reverse-words-in-a-string/"
```

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
