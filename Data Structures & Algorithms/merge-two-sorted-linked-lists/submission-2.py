# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # both are sorted
        # we are using the original nodes so no copies
        tail = dummy = ListNode() # create a dummy output node so we don't have to worry about inserting to an empty list
        while list1 and list2: 
            if list1.val < list2.val:
                # if the value of list1 is less then we can start there so 
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1: 
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

