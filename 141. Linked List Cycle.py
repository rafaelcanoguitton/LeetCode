# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        while(pointer):
            if hasattr(pointer,'visited'):
                return True
            else:
                pointer.visited = True
            pointer = pointer.next
        return False