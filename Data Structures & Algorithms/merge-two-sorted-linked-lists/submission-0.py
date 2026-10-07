# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        if list1 == None:
            return list2

        if list2 == None:
            return list1

        if list1 == list2 == None:
            return []

        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        else:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        if list1 is None:
            curr.next = list2
        else:
            curr.next = list1

        return dummy.next
