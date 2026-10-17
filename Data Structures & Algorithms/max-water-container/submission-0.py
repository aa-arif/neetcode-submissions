class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1, 7, 2, 5, 4, 7, 3, 6]
        # ^                    ^  
        #1) 7 * min(1, 6) = 7        
        #2) If 
        left, right = 0, len(heights) - 1
        out = min(heights[left], heights[right]) * (right - left)
        while left < right: 
            if heights[left] > heights[right]: 
                right -= 1
            elif heights[left] < heights[right]: 
                left += 1
            elif heights[left] == heights[right]: 
                left += 1
            out = max(out, min(heights[left], heights[right]) * (right - left))
        return out