# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        path = [root]
        while(len(path)): 
            current = path.pop()
            if current:
                preorder.append(current.val)
                path.append(current.right)
                path.append(current.left)
        return preorder