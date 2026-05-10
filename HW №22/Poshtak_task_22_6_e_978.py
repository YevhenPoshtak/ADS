import sys

def build_tree(v: int, adj: list[list[int]], visited: list[bool]) -> None:
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            print(v, u)
            build_tree(u, adj, visited)

def main() -> None:
    data = map(int, sys.stdin.read().split())
    n, m = next(data), next(data)
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = next(data), next(data)
        adj[u].append(v); adj[v].append(u)
    
    build_tree(1, adj, [False] * (n + 1))

if __name__ == "__main__":
    main()