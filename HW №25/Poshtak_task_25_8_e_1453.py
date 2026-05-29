import sys

def bellman_ford(num_vertices: int, edges: list[tuple[int, int, int]], start_vertex: int) -> list[int]:
    distances = [30000] * (num_vertices + 1)
    distances[start_vertex] = 0
    
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in edges:
            if distances[u] != 30000 and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        if not updated:
            break
            
    return distances[1:]

def main() -> None:
    input_data = sys.stdin.read().split()
    
    num_vertices = int(input_data[0])
    num_edges = int(input_data[1])
    
    edges = []
    data_index = 2
    
    for _ in range(num_edges):
        u = int(input_data[data_index])
        v = int(input_data[data_index + 1])
        weight = int(input_data[data_index + 2])
        edges.append((u, v, weight))
        data_index += 3
        
    print(*(bellman_ford(num_vertices, edges, 1)))

if __name__ == '__main__':
    main()
