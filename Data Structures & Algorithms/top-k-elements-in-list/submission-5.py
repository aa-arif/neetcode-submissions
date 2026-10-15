class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        frequency_map = {}
        frequency_tracker = [[] for _ in range(len(nums) + 1)]
        for number in nums: 
            frequency_map[number] = frequency_map.get(number, 0) + 1
        # {number: frequency}
        for num, freq in frequency_map.items():
            frequency_tracker[freq].append(num)

        for freq in reversed(frequency_tracker): 
            for num in freq: 
                out.append(num)
                if len(out) == k: 
                    return out