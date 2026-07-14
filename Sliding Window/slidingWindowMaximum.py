from collections import deque
from typing import List


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []

#         for i in range(len(nums)-k+1):
#             w = nums[i:i+k]
#             res.append(max(w))
#         return res
    
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         start = 0
#         w = nums[:k]
#         res = []
#         res.append(max(w))

#         for end in range(len(nums)-k):
#             w = w[1::]
#             w.append(nums[end+k])
#             res.append(max(w))
#         return res
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()  # stores indices, values kept decreasing
        result = []
        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)

            if d[0] <= i - k:
                d.popleft()

            if i >= k - 1:
                result.append(nums[d[0]])

        return result
    
def main():
    nums=[10,9,8,7,6]
    k=3
    result = Solution().maxSlidingWindow(nums,k)
    print(result)
    
if __name__ == "__main__":
    main()
