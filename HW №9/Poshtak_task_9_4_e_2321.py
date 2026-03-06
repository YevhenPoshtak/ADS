import sys

def quick_sort(array: list[int], a: int, b: int) -> None:
    if a >= b: 
        return

    pivot = array[a + (b - a) // 2] 
    left = a 
    right = b 

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left <= right: 
            array[left], array[right] = array[right], array[left] 
            left += 1 
            right -= 1 

    if a < right:
        quick_sort(array, a, right)
    if left < b:
        quick_sort(array, left, b)

def main() -> None:
    line1 = sys.stdin.readline()
    n = int(line1.strip())
        
    line2 = sys.stdin.readline()
    array = list(map(int, line2.split()))
        
    if n > 0:
        quick_sort(array, 0, n - 1)
        print(*(array))

if __name__ == "__main__":
    main()