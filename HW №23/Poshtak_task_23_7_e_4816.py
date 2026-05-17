import sys
from collections import deque

def get_components(n: int, graph: list) -> list:
    visited = [False] * (n + 1)
    components = []
    
    for start_node in range(1, n + 1):
        if visited[start_node]:
            continue
            
        current_component = []
        queue = deque([start_node])
        visited[start_node] = True
        
        while queue:
            u = queue.popleft()
            current_component.append(u)
            
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    
        components.append(current_component)
        
    return components

def main() -> None:
    input_data = sys.stdin.read().split()
        
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        graph[u].append(v)
        graph[v].append(u)
        
    components = get_components(n, graph)
    
    output_lines = [str(len(components))]
    for component in components:
        output_lines.append(str(len(component)))
        output_lines.append(" ".join(map(str, component)))
        
    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == '__main__':
    main()