class Counter:
    def __init__(self, iterable: list[str]) -> None:
        self.capacity = 100003
        self.table = [[] for _ in range(self.capacity)]
        if iterable:
            for item in iterable:
                self.add(item)

    def _hash(self, key: str) -> int:
        h = 0
        for char in str(key):
            h = (h * 31 + ord(char)) % self.capacity
        return h
    
    def add(self, item: str) -> None:
        index = self._hash(item)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == item:
                self.table[index][i] = (item, pair[1] + 1)
                return
        self.table[index].append((item, 1))

    def keys(self) -> list:
        result = []
        for bucket in self.table:
            for k, v in bucket:
                result.append(k)
        return result

class Solution:
    def count_unique_contacts(self, N: int, numbers: list[str]) -> int:
        return len(Counter(numbers).keys())    

if __name__ == "__main__":
    N = int(input())
    numbers = input().split()
    print(Solution().count_unique_contacts(N, numbers))
