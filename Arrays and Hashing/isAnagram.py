class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        # sVal = sum(ord(chr) for chr in s)
        # tVal = sum(ord(chr) for chr in t)

        # if (sVal != tVal):
        #     return False

        # if(set(s) != set(t)):
        #     return False

        d1 = {char : s.count(char) for char in s}
        d2 = {char : t.count(char) for char in t}
        
        if (d1 == d2):
            return True
        else:
            return False
        


        # BEST SOLUTION
        return sorted(s) == sorted(t)

        # BESTEST SOLUTION
        return Counter(s) == Counter(t)

        