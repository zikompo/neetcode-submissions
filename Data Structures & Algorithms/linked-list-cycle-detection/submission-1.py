# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        curr2 = head.next
        while curr and curr2:
            if curr is curr2:
                return True
            curr = curr.next
            if curr2.next and curr2.next.next:
                curr2 = curr2.next.next
            else:
                return False
        return False