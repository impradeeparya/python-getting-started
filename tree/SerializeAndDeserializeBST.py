# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file
# or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another
# computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized
# to a string, and this string can be deserialized to the original tree structure.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return max(left_height, right_height) + 1

    def populate_tree_array(self, node: TreeNode, index: int, tree_array: []):
        if node is not None:
            tree_array[index] = node.val

            if node.left is not None:
                self.populate_tree_array(node.left, 2 * index + 1, tree_array)

            if node.right is not None:
                self.populate_tree_array(node.right, 2 * index + 2, tree_array)

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        tree_height = self.height(root) - 1
        number_of_nodes = 2 ** (tree_height + 1) - 1
        tree_array = [-1 for nodes in range(number_of_nodes)]

        self.populate_tree_array(root, 0, tree_array)

        output = ""
        for element in tree_array:
            if element == -1:
                output = output + '-,'
            else:
                output = output + str(element) + ','

        return output[0:len(output) - 1]

    def populate_child_nodes(self, node: TreeNode, data: [], index: int, n: int):

        if index < n:
            if data[index] == '-':
                return None
            node = TreeNode()
            node.val = data[index]
            node.left = self.populate_child_nodes(node.left, data, 2 * index + 1, n)
            node.right = self.populate_child_nodes(node.right, data, 2 * index + 2, n)

        return node

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []
        nodes = data.split(',')
        if nodes[0] == '-':
            return []

        root = TreeNode()
        root.val = nodes[0]
        n = len(nodes)

        self.populate_child_nodes(root, nodes, 0, n)

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
