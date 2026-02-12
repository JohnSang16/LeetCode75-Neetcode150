
#1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        merged_string = ""
        n = 0
        if(len(word1)>=len(word2)):
            n = len(word1)
        else:
             n = len(word2)
        for i in range(n):
            if i < len(word1):
                merged_string += word1[i]
            if i < len(word2):
                merged_string += word2[i]
        return merged_string
            
        
