class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lemap = {}
        for i, v in enumerate(nums): 
            dif = target - v 
            if dif in lemap: 
                return [lemap[dif], i]
            lemap[v] = i