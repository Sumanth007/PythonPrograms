def dfs_topological_sort(adjacency_matrix):
  visited = set()
  stack = []
  topological_sorted_order = []

  for vertex in range(len(adjacency_matrix)):
    if vertex not in visited:
      dfs_topological_sort_helper(adjacency_matrix, vertex, visited, stack)

  while stack:
    vertex = stack.pop()
    topological_sorted_order.append(vertex)

  return topological_sorted_order


def dfs_topological_sort_helper(adjacency_matrix, vertex, visited, stack):
  visited.add(vertex)

  for neighbor in range(len(adjacency_matrix)):
    if adjacency_matrix[vertex][neighbor] == 1 and neighbor not in visited:
      dfs_topological_sort_helper(adjacency_matrix, neighbor, visited, stack)

  stack.append(vertex)

adjacency_matrix = [[0, 1, 0, 1, 0, 0, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0],
[1, 1, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 1, 1],
[1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 0, 1],
[0, 0, 0, 1, 1, 0, 1, 0]
]
topological_sorted_order = dfs_topological_sort(adjacency_matrix)

print("The topological sorted order is:", topological_sorted_order)