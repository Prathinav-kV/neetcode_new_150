class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        for i in strs:

            a = sorted(i)
            c = ""
            for k in a:
                c += k
            d[c] = d.get(c,[]) + [i]
        
        f = []
        for i in d.values():
            t = [] + i
            f.append(t)
        return f



#Better solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        for i in strs:
            c = "".join(sorted(i))
            d[c] = d.get(c,[]) + [i]
        
        return list(d.values())