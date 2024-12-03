from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combinations = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(s):
            n = len(s)
            if n == len(digits):
                combinations.append(s)
                return

            for letter in letters[digits[n]]:
                backtrack(s + letter)

        backtrack("")

        return combinations
