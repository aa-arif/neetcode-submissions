class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        tracker = defaultdict(list)
        for word in strs: 
            key = [0] * 26
            for w in word: 
                key[ord(w) - ord('a')] += 1
            tracker[tuple(key)].append(word)
        return list(tracker.values())