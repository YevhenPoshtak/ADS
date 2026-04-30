import sys

def is_complete_graph(n: int, m: int, edge_data: list[str]) -> bool:
    if n == 1:
        return True
    
    unique_edges = set()
    
    for i in range(0, 2 * m, 2):
        u = int(edge_data[i])
        v = int(edge_data[i + 1])
        
        if u != v:
            edge = (min(u, v), max(u, v))
            unique_edges.add(edge)
    
    required_edges = n * (n - 1) // 2
    return len(unique_edges) == required_edges

def main() -> None:
    input_raw = sys.stdin.read().split()
        
    n = int(input_raw[0])
    m = int(input_raw[1])
    edge_data = input_raw[2:]

    print("YES" if is_complete_graph(n, m, edge_data) else "NO")

if __name__ == "__main__":
    main()