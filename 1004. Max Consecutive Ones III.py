# Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
# in the array if you can flip at most k 0's.


# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

#thought process:
#check if substr of 1's has less then k amount of 0's in between the next substr of 1's
#if so flip 0's
#keep doing this until k is 0 
#see how long that substr is and compare with another version doing the same with the next set of kth zeroes


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i = 0
        iterator = 0
        maxlen = 0
        initk = k
        while i < len(nums):
            if nums[i] == 1:
                iterator += 1 
            else:
                iterator += 1 
                k -= 1

            if k == 0:
                maxlen = max(maxlen, iterator)
                iterator = 0
                k = initk
            
            i += 1 
        return maxlen
    

c = Solution()
c.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(f"test one: {c}")