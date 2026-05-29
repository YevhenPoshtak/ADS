import sys

def dijkstra(n: int, start: int, finish: int, matrix: list[list[int]]) -> int:
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    
    visited = [False] * (n + 1)
    
    for _ in range(n):
        min_dist = float('inf')
        u = -1
        
        for v in range(1, n + 1):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                u = v
        
        if u == -1 or u == finish:
            break
            
        visited[u] = True
        
        for v_idx in range(n):
            weight = matrix[u - 1][v_idx]
            v = v_idx + 1
            
            if weight != -1 and not visited[v]:
                distance = distances[u] + weight
                if distance < distances[v]:
                    distances[v] = distance
                    
    return int(distances[finish]) if distances[finish] != float('inf') else -1

def main() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    s = int(input_data[1])
    f = int(input_data[2])
    
    matrix = []
    data_index = 3
    
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(input_data[data_index]))
            data_index += 1
        matrix.append(row)
        
    print(dijkstra(n, s, f, matrix))

if __name__ == '__main__':
    main()