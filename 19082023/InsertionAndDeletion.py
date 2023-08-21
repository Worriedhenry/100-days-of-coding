# Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
class Solution:
	def minOperations(self, s1, s2):
	    dic={}
	    def fun(i,j):
	        if i>len(s1)-1 and j>len(s2)-1:
	            return 0
	        if i>len(s1)-1 or j>len(s2)-1:
	            return abs(len(s1)-i)+abs(len(s2)-j)
	        if (i,j) in dic:
	            return dic[i,j]
	        if s1[i]==s2[j]:
	            dic[i,j]=fun(i+1,j+1)
	            return dic[i,j]
	        dic[i,j]=1+min(fun(i,j+1),fun(i+1,j))
            return dic[i,j]
        return fun(0,0)	
	   