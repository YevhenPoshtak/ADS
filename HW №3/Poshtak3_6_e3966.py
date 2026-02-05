def binary_search(array: list, x: int) -> str:
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == x:
            return "YES"
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return "NO"

n = int(input())
butterfly_types = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

for query in queries:
    print(binary_search(butterfly_types, query))