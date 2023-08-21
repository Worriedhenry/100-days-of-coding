# You are given a 0-indexed integer array nums and an integer k.

# A subarray is called equal if all of its elements are equal. Note that the empty subarray is an equal subarray.

# Return the length of the longest possible equal subarray after deleting at most k elements from nums.

# A subarray is a contiguous, possibly empty sequence of elements within an array.
# https://leetcode.com/contest/weekly-contest-359/problems/find-the-longest-equal-subarray/

class Solution:
    def longestEqualSubarray(self, nums, k: int) -> int:
        current={}
        ans=0
        i=0
        prev=0
        for j in range(len(nums)):
            if nums[j] in current:
                current[nums[j]]+=1
            else:
                current[nums[j]]=1
            if current[nums[j]]>current[nums[prev]]:
                    prev=j
            if j-i+1>current[nums[prev]]+k:
                # print(j,i,prev,ans)
                current[nums[i]]-=1
                i+=1
            ans=max(ans,current[nums[prev]])
        return ans
            