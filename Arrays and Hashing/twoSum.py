class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s = 0

        for i in range(len(nums)):
            a = nums[i] 
            for j in range(i+1,len(nums)):
                if (a + nums[j] == target):
                    return [i,j]

#FASTEST SOLUTION
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = dict();

        for i, num in enumerate(nums):
            diff = target - num;
            if diff in pos:
                return [pos[diff], i]

            pos[num] = i;

        return [];
