import sys
import heapq

def road_problem(iterator: iter) -> None:
    n = int(next(iterator))
    m = int(next(iterator))
    p = int(next(iterator))
    q = int(next(iterator))

    adj = [[] for _ in range(n + 1)]
    target_exists = False
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((w, v))
        adj[v].append((w, u))
        if (u == p and v == q) or (u == q and v == p):
            target_exists = True

    if not target_exists:
        print("NO")
        return

    visited = [False] * (n + 1)
    min_heap = []
    
    visited[1] = True
    for weight, to_node in adj[1]:
        heapq.heappush(min_heap, (weight, 1, to_node))

    mst_edges_count = 0
    found_target_edge = False

    while min_heap and mst_edges_count < n - 1:
        weight, u, v = heapq.heappop(min_heap)
        
        if visited[u] and visited[v]:
            continue

        new_node = v if not visited[v] else u
        visited[new_node] = True
        mst_edges_count += 1

        if (u == p and v == q) or (u == q and v == p):
            found_target_edge = True
            break

        for next_weight, neighbor in adj[new_node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (next_weight, new_node, neighbor))

    if found_target_edge:
        print("YES")
    else:
        print("NO")

def main() -> None:
    input_data = sys.stdin.read().split()
    
    iterator = map(str, input_data)
    t_cases = int(next(iterator))

    for _ in range(t_cases):
        road_problem(iterator)

if __name__ == '__main__':
    main()