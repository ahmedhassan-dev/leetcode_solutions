"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        cur = head
        while cur is not None:
            cur.next = Node(cur.val, cur.next, None)
            cur = cur.next.next
        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next
        dummy = Node(0)
        cur = head
        cur2 = dummy
        while cur is not None:
            cur2.next = cur.next
            cur.next = cur.next.next
            cur2 = cur2.next
            cur = cur.next
        return dummy.next
        