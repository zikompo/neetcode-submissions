# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        head = None
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val <= l2.val:
                if new_list is None:
                    new_list = ListNode(l1.val)
                    head = new_list
                else:
                    new_list.next = ListNode(l1.val)
                    new_list = new_list.next
                l1 = l1.next
            else:
                if new_list is None:
                    new_list = ListNode(l2.val)
                    head = new_list
                else:
                    new_list.next = ListNode(l2.val)
                    new_list = new_list.next
                l2 = l2.next
        if l1:
            while l1:
                if new_list is None:
                    new_list = ListNode(l1.val)
                    head = new_list
                else:
                    new_list.next = ListNode(l1.val)
                    new_list = new_list.next
                l1 = l1.next
        elif l2:
            while l2:
                if new_list is None:
                    new_list = ListNode(l2.val)
                    head = new_list
                else:
                    new_list.next = ListNode(l2.val)
                    new_list = new_list.next
                l2 = l2.next
        return head