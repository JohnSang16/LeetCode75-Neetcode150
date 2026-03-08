#create a array of binary nums where 1 represents valid 
#number for a consecutive sequence and 0 represents nonvalid
#return the num of valid nums
#check for valid nums by iterating through
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        binaryArray = [0]*len(nums)
        
        for i in range(len(nums)-1): 
            j = i + 1 
            while j < len(nums):
                #bArr = [1, 0, 1, 0, 1, 1] 
                if binaryArray[i] == 1:
                    continue
                elif (nums[i])+1 == nums[j]:
                    binaryArray[i] = 1
                    binaryArray[j] = 1
                    break
                j += 1

            j = 0
        res = 0
        for ones in binaryArray:
            if ones == 1:
                res += 1 
        
        return res
               
c = Solution()
test1 = c.longestConsecutive([2,20,4,10,3,4,5])
print(test1)