import math

class Solution:
    def findRoot(self, low: float = 1.6, high: float = 3.0) -> float:
        eps = 1e-9
        
        def f(x: float) -> float:
            return math.sin(x) - (x / 3.0)
        
        while (high - low) > eps:
            mid = low + (high - low) / 2

            if f(mid) > 0:
                low = mid
            else:
                high = mid
                
        return low

print(f"Root: {Solution().findRoot():.8f}")