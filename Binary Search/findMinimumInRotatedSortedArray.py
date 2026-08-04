from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        smallest = float('inf')
        start,end = 0,len(nums)-1
        while start <= end :
            s = nums[start]
            e = nums[end]
            mid = start + (end - start)//2
            m = nums[mid]
            smallest = min(smallest,m,s,e)
            if s >= e >= m or e >= m >= s:
                end = mid - 1
            elif m >= s >= e:
                start = mid + 1
            
        return smallest

class EfficientSolution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0,len(nums)-1
        while start < end:
            mid = (end + start)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
    
def main():
    arr = [3,4,1,2]
    smallest = Solution().findMin(arr)
    efficient_smallest = EfficientSolution().findMin(arr)
    print(smallest)
    print(efficient_smallest)
    
if __name__ == "__main__":
    main()

