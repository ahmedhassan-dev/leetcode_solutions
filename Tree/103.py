# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        stack = [(root, 0)]
        ans = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(ans) <= level:
                    ans.append([])
                if level%2==0:
                    ans[level].append(node.val)
                else:
                    ans[level] = [node.val] + ans[level]
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return ans
        