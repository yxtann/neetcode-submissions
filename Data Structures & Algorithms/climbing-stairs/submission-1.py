class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:

        # There is exactly 1 way to climb <= 0 steps, which is not taking any steps
        if n <= 0:
            return 1
        elif n == 1:
            return 1

        if n not in self.cache:
            self.cache[n] = 0
        else:
            return self.cache[n]

        ways = self.climbStairs(n-2) + self.climbStairs(n-1)
        self.cache[n] = ways

        return ways