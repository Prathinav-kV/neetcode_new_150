class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a = ""

        for i in s:
            if (i.isalnum()):
                a += i.lower()
        
        return a == a[::-1]


class Solution:
    def isPallindrome(self, s:str) -> bool:

        newStr = [c.lower() for c in s if c.isalnum()]

        l = 0
        r = len(newStr) - 1

        while l < r:
            if newStr[l] != newStr[r]:
                return False
            
            l += 1
            r -= 1

        return True