# Determine the Minimum Sum of a k-avoiding Array/
# You are given two integers, n and k.

# An array of distinct positive integers is called a k-avoiding array if there does not exist any pair of distinct elements that sum to k.

# Return the minimum possible sum of a k-avoiding array of length n.

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans=[]
        i=1
        s=0
        if n<=k:
            while(len(ans)!=n):
                if k-i not in ans:
                    ans.append(i)
                    s+=i
                i+=1
            return s
        while(len(ans)!=n or i<k):
            if k-i not in ans:
                ans.append(i)
                s+=i
            i+=1
        for j in range(len(ans),n):
            s+=ans[-1]+1+j
        # print(ans)
        return s
            
        