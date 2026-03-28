import sys

class Solution:
    def prefix_to_infix(self, expression: str) -> str:

        stack = []
        priority_map = {'+': 1, '-': 1, '*': 2, '/': 2}

        for char in reversed(expression):
            if char.isalpha():
                stack.append((char, 3))
            else:
                left_operand, left_prec = stack.pop()
                right_operand, right_prec = stack.pop()
                
                curr_prec = priority_map[char]
                
                left_part = left_operand
                if left_prec < curr_prec:
                    left_part = f"({left_operand})"
                
                right_part = right_operand
                if right_prec < curr_prec or (right_prec == curr_prec and char in ('-', '/')):
                    right_part = f"({right_operand})"
                
                stack.append((f"{left_part}{char}{right_part}", curr_prec))
        
        return stack[0][0]

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    print(Solution().prefix_to_infix(input_data))