class Solution:
    def bubble_sort(self, array: list[int]) -> int:
        swaps = 0
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swaps += 1
        return swaps

    def solve(self) -> None:
        n = int(input())
        array = list(map(int, input().split()))
        print(self.bubble_sort(array))

if __name__ == "__main__":
    Solution().solve()