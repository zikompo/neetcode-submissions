# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        curr = head
        while curr is not None:
            new = ListNode(curr.val)
            new.next = new_list
            new_list = new
            curr = curr.next
        return new_list
        
        