class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iton = {}
        for i in range(len(nums)): 
            if (target-nums[i]) in iton: 
                return [iton[target-nums[i]], i]
            iton[nums[i]] = i
