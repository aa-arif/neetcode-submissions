class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        l_ptr = 0
        longest = 0
        for r_ptr in range(len(s)): 
            while s[r_ptr] in tracker: 
                tracker.remove(s[l_ptr])
                l_ptr += 1
            tracker.add(s[r_ptr])
            longest = max(longest, r_ptr - l_ptr + 1)
        return longest