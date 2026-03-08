#SORTING IS ESSENTIAL
#fix a number with the outer loop to check, and then use
#two sum solution that used two pointers for the rest of the arr
#append if triplet found and then return


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #checks if the val is greater then 0 since in asorted array 
            #every val that comes after this would also be greater then 0
            if a > 0:
                break
            #checks for duplicates since everything is sorted,  can
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    #to keep looking for more triplets
                    l += 1
                    r -= 1
                    #to reduce duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res