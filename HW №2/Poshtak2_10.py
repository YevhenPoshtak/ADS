class Task2_10:
    def f(self, n: int) -> int:   
        sum = 0 # O(1)
        for i in range(1, n + 1): # O(n)
            sum = sum + i # O(1)
        return sum # O(1)
    # time complexity: O(1) + O(n) + O(1) + O(1) = O(n) because of the loop. result is sum of first n natural numbers
    
    def f_improved(self, n: int) -> int:
        return n * (n + 1) // 2  # O(1)
    # time complexity: O(1) 