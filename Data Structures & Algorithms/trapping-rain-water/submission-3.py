class Solution:
    def trap(self, height: List[int]) -> int:
        #[0, 2, 0, 3, 1, 0, 1, 3, 2, 1] inputs
        #[0, 0, 2, 2, 3, 3, 3, 3, 3, 3] max from left
        #[3, 3, 3, 3, 3, 3, 3, 2, 1, 0] max from right
        #[0, 2, 0, 3, 1, 0, 1, 3, 2, 1] inputs
        # ^                          ^
        #left_max = 0
        #right_max = 0
        #[0, 0, 2, 0, 2, 3, 2, 0, 0, 0] water per height
        l_ptr, r_ptr = 0, len(height) - 1
        l_max, r_max, out = height[l_ptr], height[r_ptr], 0
        while l_ptr < r_ptr: 
            if l_max < r_max: 
                out += max(0, min(l_max, r_max) - height[l_ptr])
                l_ptr += 1
                l_max = max(l_max, height[l_ptr])
            else: 
                out += max(0, min(l_max, r_max) - height[r_ptr])
                r_ptr -= 1
                r_max = max(r_max, height[r_ptr])
        return out




        