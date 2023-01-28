# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        postorder = []
        path = [root]
        while (len(path)): 
            current = path.pop()
            if current.left:
                path.extend((current, current.left))
                current.left = None
            elif current.right:
                path.extend((current, current.right))
                current.right = None
            else:
                postorder.append(current.val)
        return postorder