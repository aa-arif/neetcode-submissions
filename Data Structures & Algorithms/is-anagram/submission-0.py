class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        ss, tt = {}, {}
        for i in range(len(s)): 
            ss[s[i]] = ss.get(s[i], 0) + 1
            tt[t[i]] = tt.get(t[i], 0) + 1

        return ss == tt