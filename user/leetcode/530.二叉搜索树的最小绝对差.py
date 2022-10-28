#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from re import L


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            """return min, max, min_diff"""
            root_min, root_max, root_min_diff = root.val, root.val, float("inf")
            if root.left:
                left_min, left_max, left_min_diff = helper(root.left)
                root_min = left_min
                root_min_diff = min(root_min_diff, left_min_diff, root.val-left_max)
            if root.right:
                right_min, right_max, right_min_diff = helper(root.right)
                root_max = right_max
                root_min_diff = min(root_min_diff, right_min_diff, right_min - root.val)
            return root_min, root_max, root_min_diff
        ans = helper(root)
        return ans[-1]
# @lc code=end

