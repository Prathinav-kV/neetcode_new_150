class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)

        longest = 0
        l = 0
        for i in s:
            if ((i-1) in s ):
                continue
            l = 1

            while ((i+l) in s):
                l += 1
            
            longest = max(longest,l)

        return longest