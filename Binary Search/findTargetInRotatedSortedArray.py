from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0,len(nums)-1

        while start < end:
            mid = (start+end)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        smallest = start
        
        def bs(start:int, end:int) -> int:
            while start <= end:
                mid = (start+end)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return -1
        
        result = bs(smallest,len(nums)-1)
        if result != -1:
            return result
        return bs(0,smallest-1)

def main():
    nums = [3,4,5,6,1,2]
    target = 1
    result = Solution().search(nums,target)
    print(result)
    
if __name__ == "__main__":
    main()
