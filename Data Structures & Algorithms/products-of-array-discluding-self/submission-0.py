class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = [1] * len(nums)
        rtl = [1] * len(nums)
        out = [1] * len(nums)

        for i in range(1, len(nums)): 
            ltr[i] = nums[i-1] * ltr[i-1]
        
        for i in range(len(nums)-2, -1, -1): 
            rtl[i] = nums[i+1] * rtl[i+1] 

        
        for i in range(len(nums)): 
            out[i] = ltr[i] * rtl[i]

        return out
    