# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        left = head
        while prev:
            if left.val != prev.val: return False
            left, prev = left.next, prev.next
        return True
