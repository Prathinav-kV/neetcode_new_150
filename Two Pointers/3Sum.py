class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        ln = len(nums)
        for i in range(ln):
            
            if (nums[i] > 0):
                break

            if (i>0 and nums[i-1]==nums[i]):
                continue

            l = i+1
            r = ln-1

            while(l<r):
                if (nums[i]+nums[l]+nums[r] == 0):
                   result.append([nums[i],nums[l],nums[r]])
                   l+=1
                   r-=1
                   while nums[l] == nums[l-1] and l < r :
                    l+=1
                elif (nums[i]+nums[l]+nums[r] < 0):
                    l+=1
                elif (nums[i]+nums[l]+nums[r] > 0):
                    r-=1

        
        return result