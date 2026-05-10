import sys
from collections import deque

def find_distances(n: int, x: int, matrix: list[list[int]]) -> list[int]:
    dist = [-1] * n
    dist[x - 1] = 0
    queue = deque([x - 1])
    
    while queue:
        u = queue.popleft()
        for v, connected in enumerate(matrix[u]):
            if connected and dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

def main() -> None:
    data = map(int, sys.stdin.read().split())
    n,x = next(data), next(data)
    
    matrix = [[next(data) for _ in range(n)] for _ in range(n)]
    print(*find_distances(n, x, matrix))

if __name__ == "__main__":
    main()