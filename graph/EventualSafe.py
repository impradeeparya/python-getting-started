class Solution(object):

    def visit_node(self, node, graph, visited_nodes, terminated_nodes):
        visited_nodes[node] = True
        adjacent_nodes = graph[node]
        is_safe = True
        for adjacent_node in adjacent_nodes:
            if visited_nodes.get(adjacent_node, None) is None:
                if terminated_nodes.get(adjacent_node, None) is None:
                    is_safe = self.visit_node(adjacent_node, graph, visited_nodes, terminated_nodes)
                else:
                    is_safe = True
            else:
                is_safe = False

            if not is_safe:
                break
            else:
                visited_nodes[adjacent_node] = None

        if is_safe:
            terminated_nodes[node] = True
            visited_nodes[node] = None
        return is_safe

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        output = []
        terminated_nodes = {}
        for index in range(len(graph)):
            adjacent_nodes = graph[index]
            is_safe = True
            if len(adjacent_nodes) == 0:
                is_safe = True
            else:
                for adjacent_node in adjacent_nodes:
                    visited_nodes = {index: True}
                    if not self.visit_node(adjacent_node, graph, visited_nodes, terminated_nodes):
                        is_safe = False
                        break

            if is_safe:
                terminated_nodes[index] = True
                output.append(index)

        output.sort()
        return output


print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(Solution().eventualSafeNodes([[], [2], [3, 4], [4], []]))
