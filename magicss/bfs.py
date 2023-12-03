def bfs(adjacency_matrix, start_vertex):
  visited = set()
  queue = [start_vertex]
  traversal_order = []

  while queue:
    vertex = queue.pop(0)

    if vertex not in visited:
      traversal_order.append(vertex)
      visited.add(vertex)

      for neighbor in range(len(adjacency_matrix)):
        if adjacency_matrix[vertex][neighbor] == 1 and neighbor not in visited:
          queue.append(neighbor)

  return traversal_order


adjacency_matrix = [[0, 1, 0, 1, 0, 0, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0],
[1, 1, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 1, 1],
[1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 0, 1],
[0, 0, 0, 1, 1, 0, 1, 0]
]
start_vertex = 0

traversal_order = bfs(adjacency_matrix, start_vertex)

print("The BFS traversal order is:", traversal_order)


