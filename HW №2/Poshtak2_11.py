class Task2_11:

    def f(self, n: int) -> int:   
        sum = 0 # O(1)
        for i in range(1, n + 1): # O(n)
            sum = sum + i # O(1)
        return sum # O(1)
    # time complexity: O(n)

    def g(self, n: int) -> int:
        sum = 0 # O(1)
        for i in range(1, n + 1): # O(n)
            sum = sum + i + self.f(i) # O(i) per iteration
        return sum # O(1)
    # time complexity: O(1) + O(1) + O(n) * O(n) = O(n^2) because of the nested summation

    def g_improved(self, n: int) -> int:
        return n * (n + 1) // 2 + n * (n + 1) * (n + 2) // 6  # O(1)
    # time complexity: O(1) 