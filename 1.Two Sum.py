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


#thoughts:
#create a dict enumerated with all the values and their corresponding indices
#have a secondval var that holds the value of target - nth element if its smaller than target
#return the indices if the second val is found

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict(enumerate(nums))
        secondvallst = []

        for num in nums: 
            if target-num > 0:
                secondvallst += target-num
        for i in range (len(secondvallst)):
            if secondvallst[i] in d.values():
                return i 


c = Solution()
print(c.twoSum([2,7,11,15], 9))
print("   runtime approx: , Solved: F    ")
