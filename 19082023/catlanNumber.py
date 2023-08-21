# Given a number N. The task is to find the Nth catalan number.
# The first few Catalan numbers for N = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

# Catalan Number for N is equal to the number of expressions containing N pairs of paranthesis that are correct matched, i.e., for each of the N '(' there exist N ')' on there right and vice versa.

# Since answer can be huge return answer modulo 1e9+7.

# Note: Positions start from 0 as shown above.
class Solution:
    def findCatalan(self, n : int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
            dp[i]=dp[i]%(10**9+7)
        return dp[n]%(10**9+7)
                