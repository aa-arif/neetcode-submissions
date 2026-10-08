class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        left, right = 0, len(nums) - 1 
        while left < len(nums) - 2:
            if left > 0 and nums[left] == nums[left-1]: 
                left += 1
                continue
            right = len(nums) - 1
            lefty = left + 1
            while lefty < right: 
                if nums[lefty] + nums[right] == -nums[left]: 
                    out.append([nums[lefty], nums[right], nums[left]])
                    lefty += 1
                    right -= 1
                    while lefty < right and nums[lefty] == nums[lefty-1]:
                        lefty += 1
                    while lefty < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[lefty] + nums[right] < -nums[left]: 
                    lefty += 1
                elif nums[lefty] + nums[right] > -nums[left]: 
                    right -= 1
            left += 1
        return out

               