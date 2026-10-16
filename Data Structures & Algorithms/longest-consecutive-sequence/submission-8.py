class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref = set(nums)
        max_seq = 0
        for num in ref: 
            count = 0
            target = num
            if target - 1 in ref: 
                continue
            while target + count in ref: 
                count += 1
            max_seq = max(max_seq, count)
        return max_seq
    