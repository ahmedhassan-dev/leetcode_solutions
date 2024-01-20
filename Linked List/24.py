# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head: return head
        dummy = ListNode(None)
        dummy.next = head
        p, p1 = dummy, head

        while p.next and p.next.next:
            p1 = p.next
            p2 = p.next.next
            p1.next = p2.next
            p2.next = p1
            p.next = p2
            p = p1

        return dummy.next
