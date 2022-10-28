#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, value, target):
            if not root:
                return False
            elif not root.left and not root.right:
                return value + root.val == targetSum
            
            else:
                return dfs(root.left, value+root.val, target) or \
                    dfs(root.right, value+root.val, target)

        return dfs(root, 0, targetSum)

# @lc code=end

