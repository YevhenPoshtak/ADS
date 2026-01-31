import math
class Task2_7:

    def f(self, n: int) -> float:
        return 3 * n**2 - n + 4

    def g(self, n: int) -> float:
        return n * math.log10(n) + 5  

    def task(self, c: float = 1.0,n0: int = 1, limit: int = 10000) -> bool:
        for n in range(n0, limit):
            if c*self.g(n) > self.f(n):
                return False
        return True

print("∀ n ≥ 1 : g(n) ≤ c*f(n) is", Task2_7().task())
