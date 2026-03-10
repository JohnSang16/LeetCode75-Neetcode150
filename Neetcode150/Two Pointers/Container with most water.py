class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxh = 0
        #height is w * h[i]
        while l < r: 
            if heights[l] >= heights[r]:
                currh = (r-l)*heights[r]
                maxh = max(maxh, currh)
                r -= 1
            if heights[l] <= heights[r]:
                currh = (r-l)*heights[l]
                maxh = max(maxh, currh)
                l += 1
        return maxh