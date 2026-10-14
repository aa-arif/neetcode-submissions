class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_ref = {}
        for i in range(len(nums)): 
            if target - nums[i] in nums_ref: 
                return [nums_ref[target-nums[i]], i]
            nums_ref[nums[i]] = i
