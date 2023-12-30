# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

        # result = []
        # def inorder_dfs(curr_node):
        #     if curr_node:
        #         inorder_dfs(curr_node.left)
        #         result.append(curr_node.val)
        #         inorder_dfs(curr_node.right)
        # inorder_dfs(root)
        # return result

        