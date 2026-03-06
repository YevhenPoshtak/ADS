import sys

def merge_sort(array: list[int]) -> list[int]:
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][0] <= righthalf[j][0]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1
    
    return array 

def main() -> None:
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    robots = []
    
    for idx in range(n):
        main = int(input_data[2 * idx + 1])
        aux = int(input_data[2 * idx + 2])
        robots.append((main, aux))
    
    sys.stdout.write("\n".join(f"{r[0]} {r[1]}" for r in merge_sort(robots)) + "\n")

if __name__ == "__main__":
    main()
