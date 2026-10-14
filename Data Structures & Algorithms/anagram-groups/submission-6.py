class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        reference = defaultdict(list)
        for string in strs: 
            alphabet_tracker = [0] * 26
            for letter in string: 
                alphabet_tracker[ord(letter) - ord('a')] += 1
            key = tuple(alphabet_tracker)
            reference[key].append(string)
        return list(reference.values())
