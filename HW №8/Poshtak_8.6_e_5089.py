class Solution:
    def selection_sort(self, array: list[int]) -> list[int]:
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array

    def solve(self) -> None:
        n = int(input())
        words = []
        
        for _ in range(n):
            words.append(input().strip())
        
        self.selection_sort(words)
        
        for word in words:
            print(word)

if __name__ == "__main__":
    Solution().solve()