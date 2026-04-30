import sys

def calculate_vertex_degrees(n: int, m: int, edges: list[int]) -> list[int]:
    degrees = [0] * n
    
    for i in range(0, 2 * m, 2):
        u = edges[i]
        v = edges[i + 1]
        degrees[u - 1] += 1
        degrees[v - 1] += 1
        
    return degrees

def main() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    edge_list = [int(x) for x in input_data[2:]]
    
    result = calculate_vertex_degrees(n, m, edge_list)
    
    for degree in result:
        print(degree)

if __name__ == "__main__":
    main()