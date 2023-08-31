# BFS and DFS implement problem

from collections import deque

# Given graph
# Start node: A
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS - Use queue
def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            neighbor = graph[node]
            queue.extend(list(set(neighbor) - set(visited)))
    print()

# DFS - Use stack(python list - only use append, pop, top(index [-1]))
def dfs(graph, start):
    stack = [start]
    visited = [start]
    print(start, end=' ')

    while stack:
        neighbor = graph[stack[-1]]
        neighbor_not_visited = list(set(neighbor) - set(visited))
        if neighbor_not_visited:
            node = neighbor_not_visited[0]
            stack.append(node)
            visited.append(node)
            print(node, end=' ')
        else:
            stack.pop()
    print()

if __name__ == '__main__':
    bfs(graph, 'A')
    dfs(graph, 'A')