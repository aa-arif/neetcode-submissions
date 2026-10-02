class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        ref = set(nums)
        for num in ref: 
            if (num - 1) not in ref: 
                count = 1
                while(num + count) in ref: 
                    count += 1
                out = max(count, out)
        return out 
            