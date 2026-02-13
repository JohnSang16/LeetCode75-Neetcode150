# Given an array of integers nums and an integer target, return indices of
#  the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        secondval = 0
        for i in range(len(nums)):
            d[i] += (nums[i])
    
        for key in d:
            secondval = target - key
            if secondval in d:
                return d[key], d[secondval] 


c = Solution()
print(c.twoSum([2,7,11,15], 9))
print("   runtime approx: , Solved: F    ")
