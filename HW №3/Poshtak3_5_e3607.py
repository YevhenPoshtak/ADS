import sys

def sorting_by_height()-> None:
    for line in sys.stdin:
        n = int(line)
        heights = list(map(int, next(sys.stdin).split()))
        a, b = map(int, next(sys.stdin).split())
        print(sum(a <= h <= b for h in heights))
    return None

if __name__ == "__main__":
    sorting_by_height()