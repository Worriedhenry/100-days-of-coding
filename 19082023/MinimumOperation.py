# Given a number N. Find the minimum number of operations required to reach N starting from 0. You have 2 operations available:

# Double the number
# Add one to the number

class Solution:
    def minOperation(self, n):
        def fun(i):
            if i==1:
                return 1
            if i%2!=0:
                return 2+fun(i//2)
            return 1+fun(i//2)
        return fun(n)