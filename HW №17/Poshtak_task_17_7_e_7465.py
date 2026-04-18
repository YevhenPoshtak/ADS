import sys

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: int) -> None:
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_recursive(self.root, val)

    def insert_recursive(self, current: Node, val: int) -> None:
        if val < current.val:
            if current.left is None:
                current.left = Node(val)
            else:
                self.insert_recursive(current.left, val)
        else:
            if current.right is None:
                current.right = Node(val)
            else:
                self.insert_recursive(current.right, val)

    def is_same_node(self, node1: Node, node2: Node) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        
        return (self.is_same_node(node1.left, node2.left) and 
                self.is_same_node(node1.right, node2.right))

    def is_same_tree(self, other: 'BinaryTree') -> int:
        if self.is_same_node(self.root, other.root):
            return 1
        return 0

def main() -> None:
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    tree1 = BinaryTree()
    idx = 1
    for _ in range(n):
        tree1.insert(int(input_data[idx]))
        idx += 1
        
    m = int(input_data[idx])
    idx += 1
    tree2 = BinaryTree()
    for _ in range(m):
        tree2.insert(int(input_data[idx]))
        idx += 1
        
    print(tree1.is_same_tree(tree2))

if __name__ == '__main__':
    main()