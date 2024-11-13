import inspect
import warnings


def pytest_generate_tests(metafunc):
    module_name = metafunc.module.__file__

    if "tests" not in metafunc.module.__dict__:
        warnings.warn(
            f"`tests` list is not defined in module '{module_name}'.", UserWarning
        )
        return

    tests = metafunc.module.tests

    # Parameterize tests
    try:
        test_func_params = inspect.signature(metafunc.function).parameters.keys()
        idlist = [test[0] for test in tests]
        argnames = [
            param for param in tests[0][1].keys() if param in test_func_params
        ]  # Filter to relevant parameters
        argvalues = [
            tuple(test[1][param] for param in argnames)
            for test in tests  # Only take matching parameters
        ]

        metafunc.parametrize(argnames, argvalues, ids=idlist)
    except Exception as e:
        warnings.warn(
            f"Module '{module_name}': Parameterization failed due to error: {e}",
            UserWarning,
        )
