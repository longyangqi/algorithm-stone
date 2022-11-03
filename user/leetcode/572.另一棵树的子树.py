#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            else:
                if root.val == subRoot.val:
                    return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
                else:
                    return False
        
        def dfs(root, subRoot):
            if not root:
                return False
            else:
                if isSame(root, subRoot):
                    return True
                else:
                    return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
# @lc code=end

