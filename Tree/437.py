# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        self.res = 0
        self.cache = {}
        self.dfs(root, targetSum, 0)
        return self.res
    def dfs(self, root, targetSum, curr_sum):
        if not root:
            return None
        curr_sum = curr_sum + root.val
        if (curr_sum == targetSum):
            self.res += 1
        if (curr_sum - targetSum) in self.cache:
            self.res += self.cache[curr_sum - targetSum]
        if curr_sum in self.cache:
            self.cache[curr_sum] += 1
        else:
            self.cache[curr_sum] = 1
        self.dfs(root.left, targetSum,curr_sum)
        self.dfs(root.right, targetSum,curr_sum)
        self.cache[curr_sum] -= 1

        