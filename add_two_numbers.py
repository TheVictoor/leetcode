# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_as_list(l1)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        l1_str = "".join(l1[::-1])
        l2_str = "".join(l2[::-1])
        l1, l2 = int(l1_str), int(l2_str)
        r = l1 + l2
        return r[::-1]