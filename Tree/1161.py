# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        max_sum, level, ans = float('-inf'), 0, 0
        q = collections.deque()
        q.append(root)
        while q:
            level += 1
            current_level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                current_level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum < current_level_sum:
                max_sum, ans = current_level_sum, level
        return ans