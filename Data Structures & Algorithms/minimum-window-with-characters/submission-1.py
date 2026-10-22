from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, formed, left = {}, 0, 0
        need = Counter(t)
        best_len, best_l = float('inf'), 0
        for right, char in enumerate(s): 
            have[char] = have.get(char, 0) + 1
            if char in need and have[char] == need[char]: 
                formed += 1
            while formed == len(need): 
                if right - left + 1 < best_len: 
                    best_len, best_l = right - left + 1, left
                out = s[left]
                have[out] -= 1
                if out in need and have[out] < need[out]: 
                    formed -= 1
                left += 1
        return "" if best_len == float('inf') else s[best_l:best_l+best_len]