class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        window = s2[0:l1]
        if Counter(window) == Counter(s1):
            return True
        for end in range(l2-l1):
            window = window[1 :: ]
            window += s2[end + l1]
            if Counter(window) == Counter(s1):
                return True
        
        return False


