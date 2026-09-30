class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        out = defaultdict(list)
        for word in strs:
            abc = [0] * 26
            for letter in word: 
                abc[ord(letter) - ord('a')] += 1

            key = tuple(abc)
            out[key].append(word)

        return list(out.values())


