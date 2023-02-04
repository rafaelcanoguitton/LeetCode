# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        path = [root]
        while(len(path)):
            current = path.pop()
            if current is None:
                continue
            temp = current.left
            current.left = current.right
            current.right = temp
            path.extend([current.left,current.right])
        return root

