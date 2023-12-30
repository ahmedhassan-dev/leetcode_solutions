# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        p, fast, slow = None, head, head
        while fast and fast.next:
            p, slow, fast = slow, slow.next, fast.next.next
        p.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1, l2):
        cur = dummy = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next