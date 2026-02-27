#create a counter dict with the keys being the num in nums
#the vals of the dict will be the count
#freq will be list of lists that contain 0-len(nums)+1 lists, and
#for every index the list contains the vals that correspond by 
#having an equal count as the index num 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counterdict = dict()
        freq = [[] for i in range(len(nums) + 1)]
        #[[],[],[],[],[],[],[]]
        for num in nums:
            counterdict[num] = counterdict.get(num, 0) + 1 
        #counterdict = [1:1, 2:2, 3:3]
        for num, count in counterdict.items():
            freq[count].append(num)
        #freq = [[],[1],[2],[3],[],[],[]]

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res




        