class Solution:
    def decodeString(self, s: str) -> str:
        result = []

        multipliers = []
        results = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                multiplier = ""
                while i < len(s) and s[i].isdigit():
                    multiplier += s[i]
                    i += 1

                multipliers.append(int(multiplier))
            elif s[i] == "[":
                results.append(result)
                result = []
                i += 1
            elif s[i] == "]":
                result = results.pop() + result * multipliers.pop()
                i += 1
            else:
                result.append(s[i])
                i += 1

        return "".join(result)
