class Counter:
    def __init__(self, iterable) -> None:
        self.table = {}  
        if iterable:
            for item in iterable:
                self.add(item)
    
    def add(self, item: str) -> None:
        if item in self.table:
            self.table[item] += 1
        else:
            self.table[item] = 1
    
    def keys(self) -> list:
        result = []
        for key in self.table:  
            result.append(key)
        return result

class Solution:
    def count_unique_contacts(self, N: int, numbers: list[str]) -> int:
        return len(Counter(numbers).keys())    

if __name__ == "__main__":
    N = int(input())
    numbers = input().split()
    print(Solution().count_unique_contacts(N, numbers))