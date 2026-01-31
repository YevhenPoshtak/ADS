class Task2_13:
    def task_a(self, n: int) -> int:
        if n == 0:
            return 1
        return self.task_a(n - 1) + 1 if n >= 1 else -1
    # T(n) = T(n-1) + O(1) = T(n-2) + O(1) + O(1) = ... = T(0) + n*O(1) = O(n)

    def task_d(self, n: int, a: int) -> int:
        if n <= a and a > 1:
            return 1
        return a*self.task_d(n - a, a) + 1 if n > a else -1
    # T(n) = T(n-a) + O(1) = T(n-2a) + O(1) + O(1) = ... = T(k) + (n/a)*O(1) = O(n/a) = O(n)

    def task_g(self, n: int, a: int) -> int:
        if n == 1:
            return 1
        return a*self.task_g(n // a , a) + 1 if n >= 2 and a >= 2 else -1
    # T(n) = T(n/a) + O(1) = T(n/a^2) + O(1) + O(1) = ... = T(1) + log_a(n)*O(1) = O(log_a(n)) = O(log n)

    def task_h(self, n: int, a: int) -> int:
        if n == 1:
            return 1
        return a*self.task_h(n // a , a) + n if n >= 2 and a >= 2 else -1
    # T(n) = T(n/a) + O(n) = T(n/a^2) + O(n/a) + O(n) = ... = T(1) + n*(1 + 1/a + 1/a^2 + ... + 1/a^(log_a(n)-1)) = O(n)