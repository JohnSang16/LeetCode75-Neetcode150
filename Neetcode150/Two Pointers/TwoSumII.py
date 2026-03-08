class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1
        # numbers = [2,7,11,15], target = 9
        #            L       R 
        
        while left<right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            else:
                if total > target:
                    right -= 1 
                else:
                    left += 1
         