class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #ref = {}
        #for i in range(len(nums)): 
        #    if (target-nums[i]) in ref: 
        #        return [ref[target-nums[i]], i]
        #    ref[nums[i]] = i

        num_to_index = {}
        for i, num in enumerate(nums):
            if (target-nums[i]) in num_to_index:
                return [num_to_index[target - nums[i]], i]
            num_to_index[num] = i
            
