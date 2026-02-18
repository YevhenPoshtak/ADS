class Solution:
    def solveRoot(self, low: float = 0.0, high: float = 2.0) -> float:
        eps = 1e-9
        
        def f(x: float) -> float:
            return x**3 + 4*x**2 + x - 6
        
        while (high - low) > eps:
            mid = low + (high - low) / 2

            if f(mid) < 0:
                low = mid
            else:
                high = mid
                
        return low

print(f"Root: {Solution().solveRoot():.8f}")