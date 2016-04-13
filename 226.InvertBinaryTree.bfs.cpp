/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include<queue>
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            if(q.front()!=NULL){
                swap(q.front()->left,q.front()->right);
                q.push(q.front()->left);
                q.push(q.front()->right);
                
            }
            q.pop();
        }
        return root;
    }
};