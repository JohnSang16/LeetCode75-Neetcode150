class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        ans2 = set()

        d2 = dict(enumerate(nums2))

        for idx, val in enumerate(nums1):
            while idx <= len(nums1)-1:
                if val != d2[idx] and idx == len(nums1)-1:
                    ans1.add(val)
                if d2[idx] != val and idx == len(nums1)-1:
                    ans2.add(d2[idx])
        return list(ans1, ans2)
        

        