#!/usr/bin/env python3

import os
import re
import sys
from urllib.parse import urlparse, urlunparse


def create_solution_package(url):
    # Step 1: Extract problem name from URL
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")

    if len(path_parts) < 2 or path_parts[0] != "problems":
        print(path_parts)
        print("Error: Invalid LeetCode URL format", file=sys.stderr)
        sys.exit(1)

    problem_name = path_parts[1]  # e.g., 'reverse-words-in-a-string'

    # Step 2: Convert to snake case
    problem_snake_case = re.sub(r"[-\s]", "_", problem_name)

    # Step 3: Create the directory structure
    package_dir = os.path.join("solutions", problem_snake_case)
    try:
        os.makedirs(package_dir, exist_ok=True)
    except OSError as e:
        print(f"Error: Could not create directory {package_dir} - {e}", file=sys.stderr)
        sys.exit(1)

    # Step 4: Create an empty __init__.py file
    init_file = os.path.join(package_dir, "__init__.py")
    open(init_file, "w").close()

    # Step 5: Create an empty solution.py file
    solution_file = os.path.join(package_dir, "solution.py")
    with open(solution_file, "w") as f:
        f.write("class Solution:\n    pass\n")

    # Step 6: Create an empty test_solution.py file
    test_file = os.path.join(package_dir, "test_solution.py")
    with open(test_file, "w") as f:
        test_content = f"""from solutions.{problem_snake_case}.solution import Solution

def test_{problem_snake_case}():
    solution = Solution()

    assert False
    """
        f.write(test_content)

    # Step 7 & 8: Create a README file with the problem name and stripped URL
    readme_file = os.path.join(package_dir, "README.md")
    clean_url = urlunparse(
        (parsed_url.scheme, parsed_url.netloc, parsed_url.path, "", "", "")
    )

    readme_content = f"""# {problem_name}

Click [here]({clean_url})
for the LeetCode problem statement.
"""
    with open(readme_file, "w") as f:
        f.write(readme_content)

    print(f"Solution package created at: {package_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a LeetCode problem URL.", file=sys.stderr)
        sys.exit(1)
    else:
        try:
            create_solution_package(sys.argv[1])
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
