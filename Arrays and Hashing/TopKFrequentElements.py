class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        
        d_sorted = sorted(d, key=lambda x:d[x], reverse=True)

        return d_sorted[:k]