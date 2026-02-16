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
#use a start and end pointer as a sliding window
#the movement of the window is determined by k
#if k becomes less then 0 by flipping 0's, then the start moves up until it sits on the next 0
#store maxlen in a max method
#return maxlen

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start = 0
        end = 0
        maxlen = 0
        #end determines when while loop ends
        while end < len(nums):
            #checks if end sits on a 0 if so subtract k (flipping 0)
            if nums[end] == 0:
                k-=1

            #if k becomes < 0 then move start up til next 0 
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start +=1

            maxlen = max(maxlen, end - start + 1)
            end += 1
        return maxlen

 
c = Solution()
testone = c.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
testtwo = c.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
testthree = c.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
testfour = c.longestOnes([0,0,1,1,1,0,0],0) 

print("---------------Test Cases:---------------")
print(f"test one: {testone}, expected: 6")
print(f"test two: {testtwo}, expected: 10")
print(f"test three: {testthree}, expected: 6")
print(f"test four: {testfour}, expected: 3")
print("   runtime approx: 71ms, Solved: T     ")