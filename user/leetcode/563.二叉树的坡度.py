#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def traverse(root):
            if not root:
                return
            else:
                left_sum = traverse(root.left)
                right_sum = traverse(root.right)
                cur_tilt = abs(left_sum - right_sum)
                cur_sum = left_sum + right_sum + root.val
                self.ans += cur_tilt
                return cur_sum
        
        traverse(root)
        return self.ans
# @lc code=end

