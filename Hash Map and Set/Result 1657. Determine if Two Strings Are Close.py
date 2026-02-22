#first condition is to check if the len is same
#second condition is to check if same chars in both str 
#third is to check if each instance of each char is the same
#return if all true
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = dict()
        d2 = dict()
        #counter dict
        for char in word1:
            d1[char] = d1.get(char, 0) + 1

        for char in word2:
            d2[char] = d2.get(char, 0) + 1

        #checks if char are same            checks if frequencies are the same
        return d1.keys() == d2.keys() and sorted(d1.values()) == sorted(d2.values())


c = Solution()
test1 = c.closeStrings("abc", "bca")
print(test1)