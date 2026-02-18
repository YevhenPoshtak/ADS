class Solution:
    def findSmallestX(self, target: float = 5.0) -> float:
        low, high = 0.0, 10.0
        eps = 1e-9
        
        def f(x: float) -> float:
            return x**3 + x + 1
        
        while (high - low) > eps:
            mid = low + (high - low) / 2
            
            if f(mid) >= target:
                high = mid
            else:
                low = mid
                
        return low

print(f"Result: {Solution().findSmallestX():.8f}")