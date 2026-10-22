import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for index, node in enumerate(lists):
            if node:  
                heapq.heappush(heap, (node.val, index, node))
        
        start = ListNode()
        curr = start

        while heap: 
            val, index, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node: 
                heapq.heappush(heap, (node.val, index, node))

        return start.next