class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        f = [1]*len(nums)

        lp = 1
        for i in range(n):
            f[i] = lp
            lp *= nums[i]
        
        rp = 1
        for i in range(n-1, -1, -1):
            f[i] *= rp
            rp *= nums[i]

        return f
