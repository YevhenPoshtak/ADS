class Solution:
    def insertion_sort(self, array: list[int]) -> None:
        already_sorted = True
        
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            changed = False
            
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
                changed = True
            
            array[j + 1] = key
            
            if changed:
                already_sorted = False
                print(*array)

    def solve(self) -> None:
        n = int(input())
        array = list(map(int, input().split()))
        self.insertion_sort(array)

if __name__ == "__main__":
    Solution().solve()