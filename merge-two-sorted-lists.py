from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s = None
        c = None
        na = None
        nb = None

        while list1 or list2:
            if list1:
                na = list1.val
            else:
                na = 101

            if list2:
                nb = list2.val
            else:
                nb = 101

            if na <= nb:
                a = ListNode(val=na)
                list1 = list1 and list1.next
            else:
                a = ListNode(val=nb)
                list2 = list2 and list2.next 

            if not c:
                c = a
                s = c
            else:
                c.next = a
                c = a
            
        return s

l1 = ListNode(val=-10, next=ListNode(val=-6, next=ListNode(val=-6)))
l2 = None

x = Solution().mergeTwoLists(l1, l2)

while x:
    print(x.val)
    x = x.next


        