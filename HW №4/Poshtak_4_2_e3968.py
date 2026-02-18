import sys

class Solution:
    def mySqrt(self, c: float) -> float:
        left = 0.0
        right = 100000.0 
        
        eps = 1e-9
        
        while (right - left) > eps:
            mid = (left + right) / 2
            
            val = mid * mid + mid**0.5
            
            if val > c:
                right = mid 
            else:
                left = mid   
                
        return right

def solve()-> None:
    input_data = sys.stdin.read().split()
    
    for item in input_data:
        c = float(item)
        print(f"{Solution().mySqrt(c):.9f}")

if __name__ == '__main__':
    solve()