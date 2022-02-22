DUMMY_GRAPH: dict[list] = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H'],
}


def bfs(graph: dict, start_node: str) -> list[str]:
    start_node = start_node.upper()

    visited = list[str]()
    queue = list[str]()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


def dfs(graph: dict, start_node: str) -> list:
    start_node = start_node.upper()

    visited = list[str]()
    stack = list[str]()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited


print("BTS")
print(bfs(DUMMY_GRAPH, 'A'))
print("\nDTS")
print(dfs(DUMMY_GRAPH, 'A'))
