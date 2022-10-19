/*
 * @lc app=leetcode.cn id=101 lang=cpp
 *
 * [101] 对称二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isMirror(TreeNode* p, TreeNode* q){
        if(p==nullptr && q==nullptr){
            return true;
        }else if (p==nullptr || q==nullptr)
        {
            return false;
        }else if (p->val != q->val)
        {
            return false;
        }else
        {
            return isMirror(p->left, q->right) && isMirror(p->right, q->left);
        }
        
    }

    bool isSymmetric(TreeNode* root) {
        if(root == nullptr){
            return true;
        }else
        {
            return isMirror(root->left, root->right);
        }
        
        
    }
};
// @lc code=end

