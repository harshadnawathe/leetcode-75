# leetcode-75

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

### Package structure

For each problem there is a separate package that contains,

- README file
- Python source code
- Python test code

## Running tests

To run all tests execute command below.

```sh
pytest
```

To run tests for a specific problem execute command below.

```sh
pytest solutions/two_sum/test_solution.py
```
