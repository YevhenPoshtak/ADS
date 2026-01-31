class Task1_4:

    def task_a(self, n: int, a: int) -> int:
        if n <= a and a > 0:
            return 1
        return self.task_a(n - a, a) + 1 if n > a else -1
    # T(n) = T(n-a) + 1 = (T(n-2a) + 1) + 1 = ... = T(n-ka) + k. T(n) = T(0) + n/a = 1 + n/a   
    
    def task_b(self, n: int) -> int:
        if n == 0:
            return 1
        return self.task_b(n - 1) + 2 ** n if n >= 1 else -1
    # T(n) = T(n-1) + 2^n = (T(n-2) + 2^(n-1)) + 2^n = ... = T(0) + 2^1 + 2^2 + ... + 2^n = 1 + (2^(n+1) - 2) = 2^(n+1) - 1
    
    def task_c(self, n: int) -> int:
        if n == 1:
            return 1
        return 2*self.task_c(n//2) + 1 if n >= 2 else -1
    # T(n) = 2T(n/2) + 1 = 2(2T(n/4) + 1) + 1 = ... = 2^kT(n/2^k) + (2^k - 1). T(n) = nT(1) + (n - 1) = 2n - 1
    
    def task_d(self, n: int, a: int) -> int:
        if n == 1:
            return 1    
        return a*self.task_d(n//a, a) + n if n >= 2 and a >= 2 else -1
    # T(n) = aT(n/a) + n = a(aT(n/a^2) + n/a) + n = ... = a^kT(n/a^k) + kn. T(n) = nT(1) + nlog(n) = n + nlog(n)