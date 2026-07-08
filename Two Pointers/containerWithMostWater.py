class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        v = []
        l = 0
        r = len(heights) - 1

        while l < r:
            v.append( min(heights[l],heights[r])*(r-l))
            if ( heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        
        return max(v)