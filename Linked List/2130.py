# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        cur = pre = None
        fast = slow = head
        # reverse order of first part of the list
        while fast:
            fast = fast.next.next
            cur = slow
            slow = slow.next
            cur.next = pre
            pre = cur
        # find max twin summ
        maxl = 0
        while slow:
            maxl = max(maxl, pre.val + slow.val)
            slow = slow.next
            pre = pre.next
        return maxl





        
        
