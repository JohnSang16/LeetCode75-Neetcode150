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
        maxsum = 0
        res = 0
        #gets the num of vowels from 0 to k and stores in maxsum
        for char in range(k): 
            if self.isVowel(s[char]):
                maxsum += 1 
        res = maxsum

        #immediately return maxsum if it equals k since k is also the max amount of vowels it can hold
        if maxsum == k:
            return maxsum 
        
        point1 = 0
        point2 = k 
        
        while point2 < len(s):
            #if the first value is a vowel when you iterate up you lose a vowel from maxsum
            if self.isVowel(s[point1]):
                maxsum -= 1
            #if the next value is a vowel you earn a maxsum value 
            if self.isVowel(s[point2]):
                maxsum += 1
            
            point1 += 1
            point2 += 1
            
            #check if new maxsum is greater than old maxsum
            res = max(maxsum, res)
        return res
            
                    
    def isVowel(self, char):
        vowellst = 'aeiouAEIOU'
        if char in vowellst:
            return True

        

print("")
            
obj1 = Solution()
test1 = obj1.maxVowels("abciiidef", 3)
test2 = obj1.maxVowels("aeiou", 2)
test3 = obj1.maxVowels("leetcode", 3)
print("---------------Test Cases:---------------")
print(f"test1 output:{test1}, expected output: 3")
print(f"test2 output:{test2}, expected output: 2")
print(f"test3 output:{test3}, expected output: 2")
print("   runtime approx: 87ms, Solved: T     ")