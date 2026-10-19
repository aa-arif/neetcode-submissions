class Solution:
    def trap(self, height: List[int]) -> int:
        #[0, 2, 0, 3, 1, 0, 1, 3, 2, 1] inputs
        #[0, 0, 2, 2, 3, 3, 3, 3, 3, 3] max from left
        #[3, 3, 3, 3, 3, 3, 3, 2, 1, 0] max from right
        #[0, 0, 2, 0, 2, 3, 2, 0, 0, 0] water per height
        left_max, right_max = 0, 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        out = 0
        for i in range(1, len(height), 1): 
            left_max = max(left_max, height[i-1])
            prefix[i] = left_max

        for i in range(len(height)-2, -1, -1): 
            right_max = max(right_max, height[i+1])
            suffix[i] = right_max

        for i in range(len(height)-1): 
            out += max(0, min(prefix[i], suffix[i]) - height[i])

        return out

        