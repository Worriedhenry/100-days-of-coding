# Given two strings s and t. Return the minimum number of operations required to convert s to t.
# The possible operations are permitted:

# Insert a character at any position of the string.
# Remove any character from the string.
# Replace any character from the string with any other character.
class Solution:
	def editDistance(self, s, t):
		# Code here
		dic={}
		def fun(i,j):
		    if i>=len(s) and j>=len(t):
		        return 0
		    if i>=len(s) or j>=len(t):
		        return abs(len(s)-i)+abs(len(t)-j)
		    if (i,j) in dic:
		        return dic[i,j]
		    if s[i]==t[j]:
		        dic[i,j]=fun(i+1,j+1)
		        return dic[i,j]
		    replace=1+fun(i+1,j+1)
		    delete=1+fun(i+1,j)
		    insert=1+fun(i,j+1)
		    dic[i,j]=min(replace,delete,insert)
		    return dic[i,j]
	    return fun(0,0)