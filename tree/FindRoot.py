#
# Complete the 'findRoot' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY nodes as parameter.
#

def findRoot(nodes):
    # Write your code here
    child_parent = {}
    root = -1
    is_processed = True
    elements = set()
    for index in range(len(nodes)):
        bst = nodes[index]
        parent = bst[0]
        left_child = bst[1]
        right_child = bst[2]

        elements.add(parent)
        elements.add(left_child)
        elements.add(right_child)
        if (left_child == -1 or left_child < parent) and (right_child == -1 or right_child > parent):
            if left_child == -1:
                parents = child_parent.get(left_child, None)
                if parents is None:
                    child_parent[left_child] = [parent]
                else:
                    parents.append(parent)
                    child_parent[left_child] = parents
            else:
                parents = child_parent.get(left_child, None)
                if parents is None:
                    child_parent[left_child] = [parent]
                else:
                    is_processed = False
                    break

            if right_child == -1:
                parents = child_parent.get(right_child, None)
                if parents is None:
                    child_parent[right_child] = [parent]
                else:
                    parents.append(parent)
                    child_parent[right_child] = parents
            else:
                parents = child_parent.get(right_child, None)
                if parents is None:
                    child_parent[right_child] = [parent]
                else:
                    is_processed = False
                    break
        else:
            is_processed = False
            break

    roots = []
    if is_processed:
        for element in elements:
            element_parent = child_parent.get(element, None)
            if element_parent is None:
                roots.append(element)
    return roots[0] if len(roots) == 1 and is_processed else root


print(findRoot([[17, -1, -1], [15, 13, 17], [7, -1, -1], [13, -1, -1], [5, 3, 7], [3, 4, -1], [10, 5, 15]]))  # -1
print(findRoot([[17, -1, -1], [15, 13, 17], [7, -1, -1], [13, -1, -1], [5, 3, 7], [3, -1, -1], [10, 5, 15]]))  # 10
