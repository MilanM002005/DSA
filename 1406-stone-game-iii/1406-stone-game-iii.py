class Solution(object):
    def stoneGameIII(self, stones):
        n = len(stones)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            op1 = op2 = op3 = stones[i]

            if i + 1 < n:
                op1 -= dp[i + 1]
                op2 += stones[i + 1]
                op3 += stones[i + 1]

            if i + 2 < n:
                op2 -= dp[i + 2]
                op3 += stones[i + 2]

            if i + 3 < n:
                op3 -= dp[i + 3]

            dp[i] = max(op1, op2, op3)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"