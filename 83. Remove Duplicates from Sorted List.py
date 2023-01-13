# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        setOfNumbers = set()
        pointer = ListNode(next=head)
        while(pointer.next):
            if pointer.next.val in setOfNumbers:
                pointer.next = pointer.next.next
            else:
                setOfNumbers.add(pointer.next.val)
                pointer = pointer.next
        return head