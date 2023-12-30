# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def dfs(s, t):

            if (s == None and t != None) or (t == None and s != None):
                return False
            if t == None and s == None:
                return True
            
            if s.val != t.val:
                return False
            else:
                flip_left = dfs(s.left, t.right)
                flip_right = dfs(s.right, t.left)
                return flip_right and flip_left
        
        return dfs(root.left, root.right)