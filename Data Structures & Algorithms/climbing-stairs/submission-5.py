class Solution:

    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if (n in self.memo):
            return self.memo[n]

        # base case
        if (n <= 1):
            result = 1
        else:
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2) #fibonad

        self.memo[n] = result

        return result
        