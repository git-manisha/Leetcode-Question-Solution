# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.helper(root,res)
        return res
    
    def helper(self,root,res):
        if root:
            res.append(root.val)
            self.helper(root.left,res)
            self.helper(root.right,res)

        