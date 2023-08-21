# Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
# Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required. 
class Solution:
    def minPartition(self, N):
        curr=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        ans=[]
        dummy=[]
        for i in reversed(curr):
            temp=N//i
            if temp!=0:
                dummy=[i]*(temp)
                ans=ans+dummy
            if N%i==0:
                return ans
            N=N%i
        return ans
