class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # positive value
        before = []
        for asteroid in asteroids:
            flag = 1
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack:
                    if stack[-1] < -asteroid:
                        stack.pop()
                    elif stack[-1] == -asteroid:
                        flag = 0
                        stack.pop()
                        break
                    else:
                        flag = 0
                        break

                if flag and not stack:
                    before.append(asteroid)
                    continue

        return before + stack

class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and asteroid < 0:
                alive = stack[-1] <-asteroid
                if -asteroid >= stack[-1]:
                    stack.pop()
            if alive:
                stack.append(asteroid)
        return stack

