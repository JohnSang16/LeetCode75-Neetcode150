#use two pointers starting from 0 
#set to store the longest unique substring
#check while the right pointer's val is in the set (found a duplicate)
#l val gets removed and l pointer gets incremented
#otherwise its a new val and we just add r pointer
#get the res by the max of either res or (r-l + 1)
#return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        maxChar = set()
        res = 0

        for r in range(len(s)):
            while s[r]  in maxChar:
                maxChar.remove(s[l])
                l += 1 
            maxChar.add(s[r])
            res = max(res, r - l + 1) 
        return res