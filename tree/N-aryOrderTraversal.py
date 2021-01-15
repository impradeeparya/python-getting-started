# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def level(self, children):
        if children is None:
            return None
        level_order_traversal = []
        order_traversal = []
        children_traversal = []
        children_level = []

        for node in children:
            order_traversal.append(node.val)
            if node.children is not None and len(node.children) > 0:
                children_traversal.extend(node.children)

        if len(children_traversal) > 0:
            children_level = self.level(children_traversal)

        if len(order_traversal) > 0:
            level_order_traversal.append(order_traversal)
        if len(children_level) > 0:
            level_order_traversal.extend(children_level)
        return level_order_traversal

    def levelOrder(self, root):
        if root is None:
            return
        order_traversal = [[root.val]]
        order_traversal.extend(self.level(root.children))
        return order_traversal


children_3 = [Node(5), Node(6)]
node_3 = Node(3, children_3)
node_1 = Node(1, [node_3, Node(2), Node(4)])
print(Solution().levelOrder(node_1))
