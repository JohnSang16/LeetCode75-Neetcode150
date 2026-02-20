# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 
#check if val is unique
#if it is, create new var for that val as a counter
#if it is not find that val's counter var and increment
#at the end check all counters
#make hash set --> key is unique num in arr, val is counter 

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dictForCount = {}

        for num in arr: 
            if num not in dictForCount:
                dictForCount[num] = 1
            else:
                dictForCount[num] += 1
        
        dictVal = list(dictForCount.values())
        seen = set()

        for val in dictVal:
            if val not in seen:
                seen.add(val)
            else:
                pass
        
        if len(seen) != len(dictVal):
            return False
        else:
            return True



c = Solution()

test1 = c.uniqueOccurrences([1,2,2,1,1,3])
print(test1)