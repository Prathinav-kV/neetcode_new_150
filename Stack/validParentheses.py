class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {"}":"{",
                       ")":"(",
                       "]":"["}
        
        d = []

        for c in s:
            if c in closeToOpen:
                if d and d[-1] == closeToOpen[c]:
                    d.pop()
                else:
                    return False
            else:
                d.append(c)
        
        return not d
