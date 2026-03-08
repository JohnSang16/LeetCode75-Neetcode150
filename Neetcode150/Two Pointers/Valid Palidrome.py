class Solution:
    def isPalindrome(self, s: str) -> bool:
        storedStrForward = ""    
        storedStrBackward = ""    
        for strings in s:
            if strings.isalnum() is not True:
                pass
            else:
                storedStrForward += strings

        for i in range(len(s) -1, -1, -1):
            if s[i].isalnum() is not True:
                pass
            else:
                storedStrBackward += s[i]
            
        if storedStrForward.lower()== storedStrBackward.lower():
            return True
        return False

c = Solution()
Test1 = c.isPalindrome("Was it a car or a cat I saw?")
Test2 = c.isPalindrome("tab a cat")
print(Test1)
print(Test2)