class Task2_12:

    def f(self, n: int) -> int:   
        sum = 0 # O(1)
        for i in range(1, n + 1): # O(n)
            sum = sum + i # O(1)
        return sum # O(1)
    # time complexity: O(n) 
    
    def g(self, n: int) -> int:
        sum = 0 # O(1)
        for i in range(1, n + 1): # O(n)
            sum += i + self.f(i) # O(i)
        return sum # O(1)
    # time complexity: O(n^2) 

    def h(self, n: int) -> int:
        return self.f(n) + self.g(n) # O(n^2) because g(n) dominates f(n)
    # time complexity: O(n^2)

    def h_improved(self, n: int) -> int:
        return n * (n + 1) * (n + 8) // 6 # O(1)
    # time complexity: O(1)