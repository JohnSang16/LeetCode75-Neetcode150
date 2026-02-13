#Given a string s and an integer k, return the maximum number of vowel letters
#  in any substring of s with length k.

#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        point1 = 0
        point2 = k 
        maxsum = 0
        res = 0
        for char in range(k): 
            if self.isVowel(s[char]):
                maxsum += 1 
        if maxsum == k:
            return maxsum 
        elif maxsum < k:
            while point1 < len(s)-k and point2 < len(s):
                res = maxsum
                if res == k:
                    return res
                elif self.isVowel(s[point1]) and self.isVowel(s[point2]):
                    pass
                elif self.isVowel(s[point1]) is not True and self.isVowel(s[point2]) is not True:
                    pass
                elif self.isVowel(s[point1]) is not True and self.isVowel(s[point2]):
                    maxsum += 1
                    res = max(res, maxsum) 
                elif self.isVowel(s[point1]) and self.isVowel(s[point2]) is not True:
                    maxsum -= 1 
                    res = max(res, maxsum)
            point1 += 1 
            point2 += 1
        return res
            
                    
    def isVowel(self, char):
        vowellst = 'aeiouAEIOU'
        if char in vowellst:
            return True
            
obj1 = Solution()
test1 = obj1.maxVowels('leetcode', 3)
print(test1)