import sys

def check_is_heap(heap_size: int, values: list[int]) -> bool:
    for i in range(heap_size // 2):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        if left_child < heap_size and values[i] > values[left_child]:
            return False
            
        if right_child < heap_size and values[i] > values[right_child]:
            return False
            
    return True

def main() -> None:
    data = (int(word) for line in sys.stdin for word in line.split())
    n = next(data, 0)
    print("YES" if check_is_heap(n, list(data)) else "NO")

if __name__ == '__main__':
    main()