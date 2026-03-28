import sys

class Solution:
    def convert_to_base_p(self, A: int, P: int) -> str:
        if A == 0:
            return "0"

        stack = []  

        while A > 0:
            remainder = A % P
            
            if remainder < 10:
                stack.append(str(remainder))
            else:
                stack.append(f"[{remainder}]")
            
            A //= P

        result = ""
        while stack:
            result += stack.pop()  

        return result

    def main(self) -> None:
        input_data = sys.stdin.read().split()
            
        A = int(input_data[0])
        P = int(input_data[1])
            
        print(self.convert_to_base_p(A, P))

if __name__ == "__main__":
    Solution().main()