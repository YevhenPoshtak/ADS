import sys
import math

def underground_cables(points: list) -> float:
    n = len(points)
    if n == 0:
        return 0.0
        
    min_dist = [float('inf')] * n
    visited = [False] * n
    min_dist[0] = 0.0
    total_length = 0.0

    for _ in range(n):
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_dist[v] < min_dist[u]):
                u = v

        visited[u] = True
        total_length += min_dist[u]

        ux, uy = points[u]
        for v in range(n):
            if not visited[v]:
                vx, vy = points[v]
                dist = math.sqrt((ux - vx) ** 2 + (uy - vy) ** 2)
                if dist < min_dist[v]:
                    min_dist[v] = dist

    return total_length

def main() -> None:
    input_data = sys.stdin.read().split()

    iterator = iter(input_data)
    while True:
        n_str = next(iterator)
            
        n = int(n_str)
        if n == 0:
            break

        points = []
        for _ in range(n):
            x = int(next(iterator))
            y = int(next(iterator))
            points.append((x, y))

        result = underground_cables(points)
        print(f"{result:.2f}")

if __name__ == "__main__":
    main()