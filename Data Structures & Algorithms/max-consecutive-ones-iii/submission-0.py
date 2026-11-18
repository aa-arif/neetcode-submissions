class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length, zeros = 0, 0 
        l_ptr = 0
        for r_ptr in range(len(nums)): 
            if nums[r_ptr] == 0: 
                zeros += 1

            while(zeros > k):
                if nums[l_ptr] == 0: 
                    zeros -= 1
                l_ptr += 1
            
            max_length = max(max_length, r_ptr - l_ptr + 1)

        return max_length
