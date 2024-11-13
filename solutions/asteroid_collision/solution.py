from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack
