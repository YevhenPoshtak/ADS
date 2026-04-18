import sys

class BinaryTree:
    def __init__(self, key: str) -> None:
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key: str) -> None:
        if key < self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def pre_order(self) -> list[str]:
        result = [self.key]
        if self.left is not None:
            result.extend(self.left.pre_order())
        if self.right is not None:
            result.extend(self.right.pre_order())
        return result

def main() -> None:
    input_data = sys.stdin.read().split()

    chars = []
    for line in input_data:
        if line == '*':
            break
        chars.append(line)
        
    reversed_sequence = "".join(chars)[::-1]
        
    root = BinaryTree(reversed_sequence[0])
    
    for char in reversed_sequence[1:]:
        root.insert(char)
        
    print("".join(root.pre_order()))

if __name__ == "__main__":
    main()