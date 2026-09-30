class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap, tmap = {}, {}
        for w in range(len(s)): 
            smap[s[w]] = smap.get(s[w], 0) + 1
            tmap[t[w]] = tmap.get(t[w], 0) + 1
        return smap == tmap