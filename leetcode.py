#!/usr/bin/env python3

"""Create the solution package for a LeetCode problem.

The script exists to remove boilerplate, so it degrades instead of giving
up: whatever cannot be fetched or parsed is replaced by a placeholder and
reported on stderr. The only fatal errors are the ones that leave us
without a directory to write into.
"""

import ast
import json
import os
import re
import sys
import urllib.request
from dataclasses import dataclass, field
from urllib.parse import urlparse

SOLUTIONS_DIR = "solutions"
PROBLEM_URL_PREFIX = "https://leetcode.com/problems/"

HELP_MESSAGE = """
Usage: leetcode.py <leetcode_problem_url|title_slug>

This script creates a solution package for a given LeetCode problem. It reads
the problem from the LeetCode GraphQL api and creates the following structure
under the 'solutions/' directory:

solutions/<problem_snake_case>/
├── __init__.py                # Empty file to mark as package
├── solution.py                # The Python3 code snippet from LeetCode
├── test_solution.py           # A table driven test for the snippet signature
└── README.md                  # Contains the problem name and link

Files that already exist are kept, so the script can be rerun on a half done
problem to fill in the gaps. Anything that cannot be fetched or parsed is
replaced by a placeholder and reported on stderr.

Arguments:
  leetcode_problem_url         The URL of the LeetCode problem, or its title
                               slug when LeetCode cannot be reached

Examples:
  ./leetcode.py "https://leetcode.com/problems/reverse-words-in-a-string/"
  ./leetcode.py reverse-words-in-a-string
"""


def warn(*args: object) -> None:
    print(*args, file=sys.stderr)


# ProblemSpec

TITLE_SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROMAN_NUMERAL_RE = re.compile(r"^[ivx]+$")


@dataclass
class ProblemSpec:
    title_slug: str
    title: str = ""
    id: str = ""
    default_code: str = ""

    @property
    def package_name(self) -> str:
        package_name = re.sub(r"\W", "_", self.title_slug)
        if package_name[:1].isdigit():
            # A module name cannot start with a digit, e.g. '3sum'.
            package_name = "_" + package_name
        return package_name

    @property
    def package_dir(self) -> str:
        return os.path.join(SOLUTIONS_DIR, self.package_name)

    @property
    def url(self) -> str:
        return f"{PROBLEM_URL_PREFIX}{self.title_slug}/description/"

    @property
    def heading(self) -> str:
        return f"{self.id}. {self.title}" if self.id else self.title

    @property
    def stub(self) -> str:
        """The body of solution.py: the snippet LeetCode gave us, or somewhere
        to paste it when the fetch degraded."""
        if self.default_code:
            return self.default_code
        return (
            f"# TODO: paste the Python3 code snippet from {self.url}\n"
            "class Solution:\n"
            "    pass"
        )


def title_slug_from(arg: str) -> str:
    """Take the slug from a problem url, or accept a bare slug so the
    scaffolding can still be made when LeetCode is unreachable."""
    if TITLE_SLUG_RE.match(arg):
        return arg

    # .../problems/<slug>[/description/...]
    parts = urlparse(arg).path.strip("/").split("/")
    if len(parts) < 2 or parts[0] != "problems" or not TITLE_SLUG_RE.match(parts[1]):
        raise ValueError(f"not a leetcode problem url: {arg}")

    return parts[1]


def title_from(title_slug: str) -> str:
    """Reconstruct a readable title from the slug alone, for when the real one
    could not be fetched: 'meeting-rooms-iii' -> 'Meeting Rooms III'."""
    words: list[str] = []
    for word in title_slug.split("-"):
        if not word:
            continue
        words.append(word.upper() if ROMAN_NUMERAL_RE.match(word) else word.title())
    return " ".join(words)


# LeetCode serves the problem pages behind a bot challenge, so the question is
# read from the GraphQL api instead of scraped out of the html. The api turns
# down the default urllib user agent, hence the one below.
GRAPHQL_URL = "https://leetcode.com/graphql/"
GRAPHQL_QUERY = """query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    isPaidOnly
    codeSnippets {
      langSlug
      code
    }
  }
}"""
PYTHON_LANG_SLUG = "python3"
USER_AGENT = "leetcode.py (https://github.com/harshadnawathe/leetcode-75)"
TIMEOUT_SECONDS = 30


def fetch_problem_spec(title_slug: str) -> ProblemSpec:
    request = urllib.request.Request(
        GRAPHQL_URL,
        method="POST",
        data=json.dumps(
            {"query": GRAPHQL_QUERY, "variables": {"titleSlug": title_slug}}
        ).encode(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
            "Referer": f"{PROBLEM_URL_PREFIX}{title_slug}/",
        },
    )

    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        result = json.load(response)

    errors = result.get("errors")
    if errors:
        raise RuntimeError(f"leetcode graphql error: {errors[0].get('message')}")

    question = (result.get("data") or {}).get("question")
    if not question:
        raise LookupError(f"no such problem: {title_slug}")

    problem_spec = ProblemSpec(
        title_slug=question["titleSlug"],
        title=question["title"],
        id=question["questionFrontendId"],
    )

    for snippet in question.get("codeSnippets") or []:
        if snippet["langSlug"] == PYTHON_LANG_SLUG:
            problem_spec.default_code = snippet["code"]
            return problem_spec

    # Everything but the stub was fetched, so report the gap and carry on with
    # what we have rather than throwing the question away.
    if question.get("isPaidOnly"):
        warn(f"{title_slug} is a premium problem, no code snippet available.")
    else:
        warn(f"No Python3 code snippet for {title_slug}.")

    return problem_spec


def problem_spec_for(title_slug: str) -> ProblemSpec:
    """Always return a usable spec. If LeetCode cannot be reached the spec
    falls back to what the slug alone tells us, so the directory, the README
    and the test skeleton still get written and only the stub has to be pasted
    in by hand."""
    try:
        return fetch_problem_spec(title_slug)
    except Exception as e:  # noqa: BLE001 - whatever went wrong, degrade
        warn("Cannot fetch problem from leetcode:", e)
        warn("Falling back to minimal scaffolding.")
        return ProblemSpec(title_slug=title_slug, title=title_from(title_slug))


# Solution file

SOLUTION_FILE_NAME = "solution.py"

# The commented out node definitions LeetCode puts above a snippet are already
# written in the commons package, so the import is scaffolded too.
COMMONS_TYPES = {"TreeNode": "commons.tree", "ListNode": "commons.list"}

BLOCK_START_RE = re.compile(
    r"^\s*(async\s+def|def|class|if|elif|else|for|while|try|except|finally|with)\b"
)


def filled_bodies(snippet: str) -> str:
    """LeetCode stubs leave every body empty, which python will not parse. Fill
    the empty bodies with `pass` so the snippet can be written out and read back
    for test generation."""
    lines = [line.rstrip() for line in snippet.splitlines()]

    filled: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        filled.append(line)
        i += 1

        if not line.endswith(":") or not BLOCK_START_RE.match(line):
            continue

        block_indent = len(line) - len(line.lstrip())
        if not has_body(lines[i:], block_indent):
            filled.append(" " * (block_indent + 4) + "pass")

        # A block never opens on a blank line: the one LeetCode leaves is
        # either the empty body, now a `pass`, or padding above the first
        # method of a class.
        if i < len(lines) and not lines[i]:
            i += 1

    return "\n".join(filled).rstrip()


def has_body(lines: list[str], block_indent: int) -> bool:
    for line in lines:
        if not line.strip():
            continue
        return len(line) - len(line.lstrip()) > block_indent
    return False


def commons_types_in(code: str) -> list[str]:
    """The node types the snippet refers to and the commons package defines."""
    uncommented = "\n".join(
        line for line in code.splitlines() if not line.lstrip().startswith("#")
    )
    return [name for name in COMMONS_TYPES if re.search(rf"\b{name}\b", uncommented)]


def without_commented_definition(code: str, name: str) -> str:
    """Drop the commented out definition LeetCode ships for a node type we
    import from the commons package instead."""
    lines = code.splitlines()
    definition_re = re.compile(rf"#\s*class {name}\b")

    block_start = None
    for i, line in enumerate(lines + [""]):
        if line.lstrip().startswith("#"):
            if block_start is None:
                block_start = i
            continue

        if block_start is not None and any(
            definition_re.match(lines[j].lstrip()) for j in range(block_start, i)
        ):
            return "\n".join(lines[:block_start] + lines[i:])

        block_start = None

    return code


def render_solution(problem_spec: ProblemSpec) -> str:
    code = filled_bodies(problem_spec.stub)

    try:
        ast.parse(code)
    except SyntaxError as e:
        # Worth writing anyway: one hand edit beats retyping the snippet.
        warn(f"Cannot parse the code snippet for {problem_spec.title_slug}: {e}")
        return code + "\n"

    imports = ""
    for name in commons_types_in(code):
        imports += f"from {COMMONS_TYPES[name]} import {name}\n"
        code = without_commented_definition(code, name)

    return (f"{imports}\n\n" if imports else "") + code.lstrip("\n") + "\n"


# Solution spec


@dataclass
class MethodSpec:
    name: str
    params: list[str]


@dataclass
class SolutionSpec:
    class_name: str
    init_params: list[str] = field(default_factory=list)
    methods: list[MethodSpec] = field(default_factory=list)

    @property
    def is_design_problem(self) -> bool:
        """A design problem is driven through MethodInvoker, everything else is
        a single call on a Solution instance."""
        return self.class_name != "Solution" or len(self.methods) != 1


def params_of(function: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    # `self` is not an argument of the call under test.
    return [arg.arg for arg in function.args.args[1:]]


def solution_spec_from(solution_file_path: str) -> SolutionSpec:
    with open(solution_file_path) as f:
        module = ast.parse(f.read(), solution_file_path)

    for node in module.body:
        if not isinstance(node, ast.ClassDef):
            continue

        functions = [
            member
            for member in node.body
            if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]

        methods = [
            MethodSpec(name=f.name, params=params_of(f))
            for f in functions
            if not f.name.startswith("_")
        ]
        init_params = [params_of(f) for f in functions if f.name == "__init__"]

        if methods:
            return SolutionSpec(
                class_name=node.name,
                init_params=init_params[0] if init_params else [],
                methods=methods,
            )

    raise ValueError(f"no solution class found in {solution_file_path}")


# Solution test file

SOLUTION_TEST_FILE_NAME = "test_solution.py"

# `...` marks every value that has to be filled in from the examples on the
# problem page. It also keeps the scaffolded test red: an unsolved problem
# must not report a pass.
TODO = "..."

SOLUTION_TEST_TEMPLATE = """from solutions.{package_name}.solution import Solution

tests = [
    ("Example 1", {{"args": {{{args}}}, "expected": {TODO}}}),
]


def test_{package_name}(args, expected):
    solution = Solution()

    assert solution.{method_name}(**args) == expected
"""

DESIGN_TEST_TEMPLATE = """from solutions.{package_name}.solution import {class_name}
from commons.helper import MethodInvoker

tests = [
    (
        "Example 1",
        {{
            "calls": [{calls}],
            "args": [{args}],
            "expected": [{expected}],
        }},
    ),
]


def test_{package_name}(calls, args, expected):
    invoker = MethodInvoker({class_name})

    assert invoker.invoke_all(calls, args) == expected
"""

PLACEHOLDER_TEST_TEMPLATE = """# TODO: import the solution and complete the test for
# {url}

tests = [
    ("Example 1", {{"args": {{}}, "expected": {TODO}}}),
]


def test_{package_name}(args, expected):
    assert False, "TODO: write the test for {heading}"
"""


def render_solution_test(problem_spec: ProblemSpec) -> str:
    solution_file_path = os.path.join(problem_spec.package_dir, SOLUTION_FILE_NAME)
    try:
        solution_spec = solution_spec_from(solution_file_path)
    except Exception as e:  # noqa: BLE001 - whatever went wrong, degrade
        # Without a signature to mirror there is nothing to generate from, but
        # the table driven skeleton is still worth having.
        warn("Cannot read solution.py for test generation:", e)
        return PLACEHOLDER_TEST_TEMPLATE.format(
            package_name=problem_spec.package_name,
            url=problem_spec.url,
            heading=problem_spec.heading,
            TODO=TODO,
        )

    if solution_spec.is_design_problem:
        # The constructor is the first of the calls, as leetcode writes it.
        calls = [solution_spec.class_name] + [m.name for m in solution_spec.methods]
        params = [solution_spec.init_params] + [m.params for m in solution_spec.methods]
        return DESIGN_TEST_TEMPLATE.format(
            package_name=problem_spec.package_name,
            class_name=solution_spec.class_name,
            calls=", ".join(f'"{call}"' for call in calls),
            args=", ".join("[" + ", ".join([TODO] * len(p)) + "]" for p in params),
            # Constructing never returns anything.
            expected=", ".join(["None"] + [TODO] * len(solution_spec.methods)),
        )

    method = solution_spec.methods[0]
    return SOLUTION_TEST_TEMPLATE.format(
        package_name=problem_spec.package_name,
        method_name=method.name,
        args=", ".join(f'"{param}": {TODO}' for param in method.params),
        TODO=TODO,
    )


# ReadMe file

README_FILE_NAME = "README.md"

README_TEMPLATE = """# {heading}

Click [here]({url})
for the LeetCode problem statement.
"""


def render_readme(problem_spec: ProblemSpec) -> str:
    return README_TEMPLATE.format(heading=problem_spec.heading, url=problem_spec.url)


# Package


def create_file(package_dir: str, file_name: str, content: str):
    """Write a file into the solution directory, refusing to clobber what is
    already there. A file that exists is skipped, not an error: rerunning on a
    half done problem should fill in the gaps and leave solved code alone."""
    path = os.path.join(package_dir, file_name)

    try:
        with open(path, "x") as f:
            f.write(content)
    except FileExistsError:
        print("Keeping existing", path)
        return

    print("Created", path)


def create_solution_package(problem_spec: ProblemSpec) -> bool:
    try:
        os.makedirs(problem_spec.package_dir, exist_ok=True)
    except OSError as e:
        warn("Cannot create solution directory:", e)
        return False

    # One failing file must not cost us the others. solution.py is written
    # before the test, which is generated from the signature found in it.
    steps = [
        ("__init__.py", lambda: ""),
        (README_FILE_NAME, lambda: render_readme(problem_spec)),
        (SOLUTION_FILE_NAME, lambda: render_solution(problem_spec)),
        (SOLUTION_TEST_FILE_NAME, lambda: render_solution_test(problem_spec)),
    ]

    created = True
    for file_name, render in steps:
        try:
            create_file(problem_spec.package_dir, file_name, render())
        except Exception as e:  # noqa: BLE001 - whatever went wrong, degrade
            warn(f"Cannot create {file_name}: {e}")
            created = False

    return created


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in {"-h", "--help", "help"}:
        print(HELP_MESSAGE)
        return 0

    try:
        title_slug = title_slug_from(argv[1])
    except ValueError as e:
        warn("Cannot determine problem slug:", e)
        warn("Usage: leetcode.py <https://leetcode.com/problems/two-sum/|two-sum>")
        return 1

    problem_spec = problem_spec_for(title_slug)

    return 0 if create_solution_package(problem_spec) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
