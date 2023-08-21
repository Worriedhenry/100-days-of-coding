# Maximize the Profit as the Salesman
# You are given an integer n representing the number of houses on a number line, numbered from 0 to n - 1.

# Additionally, you are given a 2D integer array offers where offers[i] = [starti, endi, goldi], indicating that ith buyer wants to buy all the houses from starti to endi for goldi amount of gold.

# As a salesman, your goal is to maximize your earnings by strategically selecting and selling houses to buyers.

# Return the maximum amount of gold you can earn.

# Note that different buyers can't buy the same house, and some houses may remain unsold.
# https://leetcode.com/contest/weekly-contest-359/problems/maximize-the-profit-as-the-salesman/
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        dp = [0] * (len(offers) + 1)
        
        for i in range(len(offers) - 1, -1, -1):
            dp[i] = max(dp[i + 1], offers[i][2])
            j = bisect.bisect_left(offers, [offers[i][1] + 1])
            if j <= len(offers):
                dp[i] = max(dp[i], offers[i][2] + dp[j])
        
        return dp[0]