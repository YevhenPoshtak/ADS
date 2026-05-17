import sys

def parse_graph(items: iter, vertices_count: int, edges_count: int) -> list:
    graph = [[] for _ in range(vertices_count + 1)]
    
    for edge_id in range(1, edges_count + 1):
        u = int(next(items))
        v = int(next(items))
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))
        
    return graph

def check_connectivity(graph: list, vertices_count: int, ignored_edges: list) -> bool:
    queue = [1]
    visited = [False] * (vertices_count + 1)
    visited[1] = True
    visited_count = 1
    
    while queue:
        current_vertex = queue.pop(0)
        
        for neighbor, edge_id in graph[current_vertex]:
            if edge_id not in ignored_edges:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    visited_count += 1
                    queue.append(neighbor)
                    
    return visited_count == vertices_count

def process_queries(items: iter, graph: list, vertices_count: int, queries_count: int) -> list:
    results = []
    
    for _ in range(queries_count):
        ignored_count = int(next(items))
        
        ignored_edges = []
        for _ in range(ignored_count):
            ignored_edges.append(int(next(items)))
            
        res = "Connected" if check_connectivity(graph, vertices_count, ignored_edges) else "Disconnected"
        results.append(res)
            
    return results

def main():
    input_data = sys.stdin.read().split()
    items = iter(input_data)
    
    vertices_count = int(next(items))
    edges_count = int(next(items))
    
    graph = parse_graph(items, vertices_count, edges_count)
    
    queries_count = int(next(items))
    results = process_queries(items, graph, vertices_count, queries_count)
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()