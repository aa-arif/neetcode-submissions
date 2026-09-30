class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range (len(nums) + 1)] 

        counts = {}
        for n in nums: 
            counts[n] = counts.get(n, 0) + 1

        for num in counts:
            buckets[counts[num]].append(num)

        pre_out = []
        for val in reversed(buckets):
            pre_out.append(val)

        out = []
        for i in pre_out:
            if len(out) == k: 
                break 
            for n in i: 
                    out.append(n)

        return out