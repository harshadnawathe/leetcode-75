class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        multipler = 0

        stack = []

        for char in s:
            if char.isdigit():
                multipler = 10 * multipler + int(char)
            elif char == "[":
                stack.append((result, multipler))
                result = ""
                multipler = 0
            elif char == "]":
                r, m = stack.pop()
                result = r + result * m
            else:
                result += char

        return result
