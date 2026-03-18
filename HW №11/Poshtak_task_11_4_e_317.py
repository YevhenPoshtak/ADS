import sys
sys.set_int_max_str_digits(500000)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.karatsuba(int(num1), int(num2)))

    def karatsuba(self, x: int, y: int) -> int:
        if x < 10 or y < 10:
            return x * y
        
        n = max(len(str(x)), len(str(y)))
        m = n // 2
        
        high1, low1 = divmod(x, 10**m)
        high2, low2 = divmod(y, 10**m)
        
        z0 = self.karatsuba(low1, low2)
        z2 = self.karatsuba(high1, high2)
        z1 = self.karatsuba(low1 + high1, low2 + high2)
        
        return (z2 * 10**(2 * m)) + ((z1 - z2 - z0) * 10**m) + z0

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        print(Solution().multiply(input_data[0], input_data[1]))