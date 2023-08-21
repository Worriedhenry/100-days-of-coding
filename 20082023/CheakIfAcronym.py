# Given an array of strings words and a string s, determine if s is an acronym of words.

# The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

# Return true if s is an acronym of words, and false otherwise.

# https://leetcode.com/contest/weekly-contest-359/problems/check-if-a-string-is-an-acronym-of-words/
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        can=""
        for i in words:
            can=can+i[0]
        return can==s
        