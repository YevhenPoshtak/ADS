def lower_bound(array: list[int], x: int) -> int:
    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(array: list[int], x: int) -> int:
    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

def count_occurrences(array: list[int], x: int) -> int:
    left = lower_bound(array, x)
    right = upper_bound(array, x)
    return right - left

n = int(input())
colors = list(map(int, input().split()))
colors.sort()   
m = int(input())
queries = list(map(int, input().split()))

for q in queries:
    print(count_occurrences(colors, q))