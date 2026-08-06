# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        l = 0
        while curr is not None:
            curr = curr.next
            l += 1
        target = l-n
        l1 = 0
        curr1 = head
        while l1 < target:
            prev = curr1
            curr1 = curr1.next
            l1 += 1
        if target != 0:
            prev.next = curr1.next
        else:
            head = head.next
        return head


