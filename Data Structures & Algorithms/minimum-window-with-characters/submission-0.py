class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l_ptr = 0 
        window, target = {}, {}

        for char in t: 
            target[char] = target.get(char, 0) + 1
        
        curr, goal = 0, len(target)
        res_window, res_length = [0, 0], float("infinity")

        for r_ptr in range(len(s)): 
            c = s[r_ptr]
            window[c] = window.get(c, 0) + 1
            if c in target and window[c] == target[c]:
                curr += 1
            
            while curr == goal: 
                if (r_ptr - l_ptr + 1) < res_length: 
                    res_window = [l_ptr, r_ptr]
                    res_length = r_ptr - l_ptr + 1
                
                window[s[l_ptr]] -= 1   
                if s[l_ptr] in target and window[s[l_ptr]] < target[s[l_ptr]]: 
                    curr -= 1
                l_ptr += 1
        l_ptr, r_ptr = res_window
        return s[l_ptr: r_ptr + 1] if res_length != float("infinity") else ""
        