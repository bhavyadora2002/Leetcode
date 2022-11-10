/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> values = new ArrayList<>();
        traverse(root,values);
        return values;
    }

    public void traverse(TreeNode root,List values) {
        if(root!=null) {
            traverse(root.left,values);
            traverse(root.right,values);
            values.add(root.val);
        }
    }
}