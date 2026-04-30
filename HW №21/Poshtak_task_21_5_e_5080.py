import sys

def count_pendant_vertices(n: int, matrix_data: list[int]) -> int:
    pendant_count = 0
    
    for i in range(n):
        start_idx = i * n
        end_idx = (i + 1) * n
        row = matrix_data[start_idx : end_idx]
        
        degree = sum(int(val) for val in row)
        
        if degree == 1:
            pendant_count += 1
            
    return pendant_count

def main() -> None:
    input_raw = sys.stdin.read().split()
    n = int(input_raw[0])
    
    matrix_elements = input_raw[1:]
    print(count_pendant_vertices(n, matrix_elements))

if __name__ == "__main__":
    main()