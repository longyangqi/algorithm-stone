#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if not root:
            return 0
        height_left = self.getHeight(root.left)
        height_right = self.getHeight(root.right)
        if height_left == -1 or height_right == -1:
            return -1
        elif min(height_left, height_right) + 1 < max(height_left, height_right):
            return -1
        else:
            return max(height_left, height_right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) != -1:
            return True
        else:
            return False
        

        

# @lc code=end

