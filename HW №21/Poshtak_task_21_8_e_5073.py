import sys

def has_multiedges(n: int, m: int, edge_data: list[str]) -> bool:
    seen_edges = set()
    
    for i in range(0, 2 * m, 2):
        u = int(edge_data[i])
        v = int(edge_data[i + 1])
        
        edge = (u, v)
        
        if edge in seen_edges:
            return True
        seen_edges.add(edge)
        
    return False

def main() -> None:
    input_data = sys.stdin.read().split()
        
    n = int(input_data[0])
    m = int(input_data[1])
    edge_data = input_data[2:]
    
    print("YES" if has_multiedges(n, m, edge_data) else "NO" )

if __name__ == "__main__":
    main()