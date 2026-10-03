class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        post = [1] * len(nums) 
        out = [1] * len(nums)

        for i in range(1, len(nums)): 
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1): 
            post[i] = post[i+1] * nums[i + 1]

        for i in range(len(nums)): 
            out[i] = pref[i] * post[i]

        return out

    
        
        # Input: [1, 2, 4, 6]
        # Pref:  [1, 2, 8, 48]
        # Post:  [48, 48, 24, 6]

        # Pref: [1, 1, 2, 8]
        # Post : [48, 24, 6, 1]
        # Outpt: [48, 24, 12, 8]