import sys
from collections import deque

def topological_sort(n: int, graph: list, in_degree: list) -> list:
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    sorted_order = []
    
    while queue:
        u = queue.popleft()
        sorted_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    return sorted_order if len(sorted_order) == n else [-1]

def main() -> None:
    input_data = sys.stdin.read().split()
        
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        graph[u].append(v)
        in_degree[v] += 1
        
    result = topological_sort(n, graph, in_degree)
    print(*(result if result != [-1] else [-1]))

if __name__ == '__main__':
    main()