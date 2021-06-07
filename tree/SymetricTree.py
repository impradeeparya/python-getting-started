# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_child_symmetric(self, children):
        is_symmetric = True
        left_index = 0
        right_index = len(children) - 1

        while left_index < right_index:
            if children[left_index] is None and children[right_index] is None:
                is_symmetric = True
            elif (children[left_index] is None and children[right_index] is not None) or (
                    children[left_index] is not None and children[right_index] is None) or (
                    children[left_index].val != children[right_index].val):
                is_symmetric = False
                break
            left_index += 1
            right_index -= 1

        if is_symmetric:
            children_nodes = []
            is_leaf_level = True
            for index in range(len(children)):
                children_nodes.append(children[index].left if children[index] is not None else None)
                children_nodes.append(children[index].right if children[index] is not None else None)
                if children[index] is not None:
                    is_leaf_level = False
            if not is_leaf_level:
                is_symmetric = self.is_child_symmetric(children_nodes)

        return is_symmetric

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_symmetric = True
        if root is not None:
            if root.left is not None and root.right is not None and root.left.val == root.right.val:
                is_symmetric = self.is_child_symmetric([root.left, root.right])
            elif root.left != root.right:
                is_symmetric = False

        return is_symmetric


left = TreeNode(2, None, TreeNode(3))
right = TreeNode(2, None, TreeNode(3))
root = TreeNode(1, left, right)

print(Solution().isSymmetric(root))
