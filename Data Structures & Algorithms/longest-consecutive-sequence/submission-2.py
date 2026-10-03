class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        ref = set(nums)
        # [3, 20, 2, 4]
        for n in nums:
            lens = 1
            if n-1 in ref: 
                continue
            while n+lens in ref:
                lens += 1 
            out = max(out, lens)


        return out
