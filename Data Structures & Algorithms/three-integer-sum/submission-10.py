class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for target in range(len(nums) - 2): 
            if nums[target] == nums[target - 1] and target != 0: 
                continue
            left, right = target + 1, len(nums) - 1
            while left < right: 
                if nums[left] + nums[right] < -nums[target]: 
                    left += 1 
                elif nums[left] + nums[right] > -nums[target]: 
                    right -= 1
                elif nums[left] + nums[right] == -nums[target]: 
                    out.append([nums[left], nums[right], nums[target]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
                    while nums[right] == nums[right + 1] and left < right: 
                        right -= 1
        return out
        