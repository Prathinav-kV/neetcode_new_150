class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        start = 0

        countT = {}
        window = {}
        for i in t:
            countT[i] = 1 + countT.get(i,0)

        have = 0
        need = len(countT)

        res = [-1,-1]
        resLen = float("inf")
        
        for end in range(len(s)):
            c = s[end]
            window[c] = 1 + window.get(c,0)
            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if (end - start + 1) < resLen:
                    res = [start,end]
                    resLen = end - start + 1
                
                window[s[start]] = window[s[start]] - 1
                if s[start] in countT and window[s[start]] < countT[s[start]]:
                    have -= 1
                start += 1
        

        start , end = res

        return s[start:end+1] if resLen != float("inf") else ""



def main():
    # s="OUZODYXAZV"
    # t="XYZ"
    # s="ab"
    # t="a"
    s="AAXXXXYYYYYZYZZZ"
    t="XYZZ"
    result = Solution().minWindow(s,t)
    print(result)

if __name__ == "__main__":
    main()
