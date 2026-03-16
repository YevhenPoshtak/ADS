import sys

class Solution:
    def generate_permutations(self, n: int, k: int) -> None:
        def backtrack(curr: list[int]) -> None:
            if len(curr) == k:
                return print(*curr)
            
            for i in range(1, n + 1):
                if i not in curr:
                    backtrack(curr + [i])

        backtrack([])

if __name__ == "__main__":
    n, k = map(int, sys.stdin.read().split())
    Solution().generate_permutations(n, k)