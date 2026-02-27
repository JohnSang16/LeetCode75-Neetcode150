# Given an array of strings strs, group all anagrams together into sublists. 
# You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]


#create a dict that will store keys that contain the amount of chars found within each word
#if the keys are the same then add that word 
#return the values of the dict

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            #this intializes empty array of 26 0's representing a-z chars
            count = [0]*26
            for c in s:
                #finds code point of c and subtracts by a, to get proper index for count[]
                count[ord(c)-ord("a")] += 1
            #the res appends values s for the key = count 
            res[tuple(count)].append(s)

        return list(res.values())
                
        
        
        