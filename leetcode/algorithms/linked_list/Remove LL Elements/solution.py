from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        p = prev = head
        while p:
            if p.val == val:
                prev.next = p.next 
            else:
                prev = p
            p = p.next 

        return head
