import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        end = max(piles)
        n = len(piles)
        start = 1
        min_rate = end 
        while start <= end:
            mid_rate = start + (end - start)//2
            time = 0
            for i in piles:
                time += math.ceil(i/mid_rate)
            if time > h:
                start = mid_rate + 1
            elif time <= h:
                min_rate = min(min_rate,mid_rate)
                end = mid_rate - 1
        return min_rate

def main():
    piles = [25,10,23,4]
    h = 4
    min_rate = Solution().minEatingSpeed(piles,h)
    print(min_rate)

if __name__ == "__main__":
    main()
