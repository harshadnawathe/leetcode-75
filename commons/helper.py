from typing import Any, List
from itertools import starmap


class MethodInvoker:
    """Handles method invocation on a target class instance based on method names."""

    def __init__(self, target_class):
        self.target_class = target_class
        self.instance = None

    def invoke(self, method_name: str, args):
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

    def invoke_all(self, method_names: List[str], args: List[List[Any]]):
        return list(starmap(self.invoke, zip(method_names, args)))
