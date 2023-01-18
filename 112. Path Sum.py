# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        path = [root]
        while (len(path)):
            current = path.pop()
            if current.val == targetSum and current.right is None and current.left is None:
                return True
            if current.left is not None:
                current.left.val = current.val + current.left.val
                path.append(current.left)
            if current.right is not None:
                current.right.val = current.val + current.right.val
                path.append(current.right)
        return  False