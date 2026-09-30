class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for index, number in enumerate(nums): 
            sec = target - number
            if sec in ref: 
                return [ref[sec], index]
            ref[number] = index
