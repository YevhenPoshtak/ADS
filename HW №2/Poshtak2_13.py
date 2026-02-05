class Task2_13:
    def task_a(self, n: int) -> int:
        if n == 0:
            return 1
        return self.task_a(n - 1) + 1 if n >= 1 else -1
    # T(n) = T(n-1) + O(1) = T(n-2) + O(1) + O(1) = ... = T(0) + n*O(1) = O(n)

    def task_d(self, n: int, a: int) -> int:
        if n <= a and a > 1:
            return 1
        return a * self.task_d(n - a, a) + 1 if n > a else -1
    # T(n) = a*T(n-a) + O(1) = a^2*T(n-2a) + a + 1 = ... = a^(n/a)*T(const) + O(a^(n/a)) = O(a^(n/a))

    def task_g(self, n: int, a: int) -> int:
        if n == 1:
            return 1
        return a * self.task_g(n // a , a) + 1 if n >= 2 and a >= 2 else -1
    # T(n) = a*T(n/a) + O(1) = a^2*T(n/a^2) + a + 1 = ... = a^(log n)*T(1) + sum(a^i) = O(n)

    def task_h(self, n: int, a: int) -> int:
        if n == 1:
            return 1
        return a * self.task_h(n // a , a) + n if n >= 2 and a >= 2 else -1
    # T(n) = a*T(n/a) + n = a^2*T(n/a^2) + a*(n/a) + n = ... = n + n + ... + n (log n times) = O(n log n)