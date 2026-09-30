class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs: 
            letters = [0] * 26
            for letter in word: 
                letters[ord(letter) - ord('a')] += 1
            
            k = tuple(letters)
            anagrams[k] = anagrams.get(k, []) + [word]

        return list(anagrams.values())      
            
            
                        