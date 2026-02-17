#make leftside be 0 and rightside the sum of the array
#for every idx subtract the value at that idx from rightsum and check if this equals the leftside
#if it doesn't add the value to leftside and retry
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftside = 0
        #rightide is the sum of nums
        rightside = sum(nums)
        #this stores the index values of nums in idx and the actual values into val using enumerate
        for idx, val in enumerate(nums):
            #subtract the val at the index from rightside
            rightside -= val
            if leftside == rightside:
                return idx
            #add the val at the index to rightside
            leftside += val
        #if no pivot is found return -1
        return -1

        
    
c = Solution()
test1 = c.pivotIndex([1,7,3,6,5,6])
print(test1)