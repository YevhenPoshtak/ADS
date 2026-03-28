import sys

class Solution:
    def valid_parentheses(self, s: str) -> str:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return "no"
            else:
                stack.append(char)
        
        return "yes" if not stack else "no"

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    
    for s in input_data:
        print(Solution().valid_parentheses(s))