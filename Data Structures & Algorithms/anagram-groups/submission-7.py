class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        tracker = defaultdict(list)
        for word in strs:
            alphabet_tracking = [0] * 26
            for letter in word:  
                alphabet_tracking[ord(letter) - ord('a')] += 1
            tracker[tuple(alphabet_tracking)].append(word)
        return list(tracker.values())
        