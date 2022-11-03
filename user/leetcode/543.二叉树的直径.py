#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def getDiameter(root):
            if not root:
                return 0, 0
            else:
                left_diameter, left_height = getDiameter(root.left)
                right_diameter, right_height = getDiameter(root.right)
                cur_diameter = max(left_diameter, right_diameter, \
                                    left_height+right_height+1)
                cur_height = max(left_height, right_height) + 1
                return cur_diameter, cur_height
        
        return getDiameter(root)[0]-1

                


# @lc code=end

