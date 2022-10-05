# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root, val, depth, isLeft = True):

        if depth != 1:
            if not root: return
            root.left = self.addOneRow(root.left, val,depth-1, True)
            root.right = self.addOneRow(root.right, val,depth-1, False)
            return root 
        
        return TreeNode(val,root) if isLeft else TreeNode(val,None, root)