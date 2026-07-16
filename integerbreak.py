class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1 
        for i in range(2, n+1):
            for j in range(1, i):
                prev = j * (i - j)      
                new = j * dp[i - j]     
            
                dp[i] = max(dp[i], prev, new)
                
        return dp[n]
