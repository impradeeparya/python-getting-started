def dependentCount(dependents, dependencies):
    dependent_set = set()
    if dependents is not None:
        for dependent in dependents:
            dependent_set.add(dependent)
            temp = dependentCount(dependencies.get(dependent, None), dependencies)
            for value in temp:
                dependent_set.add(value)

    return dependent_set


def costsOfNode(lines):
    dependencies = {}
    for line in lines:
        nodes = line.split(",")
        for index, node in enumerate(nodes):
            if index == 0:
                if dependencies.get(node, None) is None:
                    dependencies[node] = None
            else:
                dependent = dependencies.get(node, None)
                if dependent is None:
                    dependent = [nodes[0]]
                else:
                    dependent.append(nodes[0])
                dependencies[node] = dependent
    cost_list = []
    for key, value in dependencies.items():
        dependents = dependentCount(value, dependencies)
        dependents.add(key)
        cost_list.append(key + "," + str(len(dependents)))
    cost_list.sort()
    return cost_list


print(costsOfNode(["A,E,N,S", "S,H,N", "E,N", "H", "N"]))
