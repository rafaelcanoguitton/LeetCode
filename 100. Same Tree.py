# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return self.areNodesOrNones(p,q)
        path = [(p,q)]
        while(len(path)):
            first,second = path.pop()
            if first.val != second.val:
                return False
            elif not self.areNodesOrNones(first.left,second.left) or not self.areNodesOrNones(first.right,second.right):
                return False
            if first.left is not None:
                path.extend(((first,second),(first.left,second.left)))
                first.left = second.left = None
            elif first.right is not None:
                path.append((first.right,second.right))
        return True

    def areNodesOrNones(self,first,second):
        return (isinstance(first,TreeNode) and isinstance(second,TreeNode)) or (first is None and second is None)