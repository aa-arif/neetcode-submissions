from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            abc = [0] * 26
            for l in word: 
                abc[ord(l) - ord('a')] += 1
            key = tuple(abc)
            anagrams[key].append(word)
        return list(anagrams.values())