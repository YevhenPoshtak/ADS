import sys

def calculate_degrees(n: int, edges: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    in_degree = [0] * n
    out_degree = [0] * n
    
    for u, v in edges:
        out_degree[u - 1] += 1
        in_degree[v - 1] += 1
        
    return in_degree, out_degree

def main() -> None:
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    for i in range(m):
        u = int(input_data[2 + i * 2])
        v = int(input_data[3 + i * 2])
        edges.append((u, v))
        
    in_deg, out_deg = calculate_degrees(n, edges)
    
    for i in range(n):
        print(f"{in_deg[i]} {out_deg[i]}")

if __name__ == "__main__":
    main()