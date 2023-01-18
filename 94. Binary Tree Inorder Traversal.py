# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        numbers = []
        path = [root]
        while (len(path)):
            current = path.pop()
            if current.left is not None:
                path.extend((current, current.left))
                current.left = None
            elif current.right is not None:
                path.append(current.right)
                numbers.append(current.val)
            else:
                numbers.append(current.val)

        return  numbers