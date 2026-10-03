class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = [[] for _ in range(len(nums)+1)]

        for n in nums: 
            counts[n] = counts.get(n, 0) + 1
    
        for num, count in counts.items(): 
            freqs[count].append(num) 
        
        out = []
        for i in reversed(freqs): 
            for n in i: 
                out.append(n)
                if len(out) == k: 
                    return out
        
