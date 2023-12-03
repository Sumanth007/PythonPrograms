def source_removal_topological_sort(adjacency_matrix):
    indegree = [0] * len(adjacency_matrix)

    for vertex in range(len(adjacency_matrix)):
        for neighbor in range(len(adjacency_matrix)):
            if adjacency_matrix[vertex][neighbor] == 1:
                indegree[neighbor] += 1

    topological_sorted_order = []
    source_vertices = []

    for vertex in range(len(adjacency_matrix)):
        if indegree[vertex] == 0:
            source_vertices.append(vertex)

    while source_vertices:
        vertex = source_vertices.pop(0)
        topological_sorted_order.append(vertex)

        for neighbor in range(len(adjacency_matrix)):
            if adjacency_matrix[vertex][neighbor] == 1:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    source_vertices.append(neighbor)

    return topological_sorted_order.copy()


adjacency_matrix = [[0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0]]
topological_sorted_order = source_removal_topological_sort(adjacency_matrix).copy()

print("The topological sorted order is:", topological_sorted_order)