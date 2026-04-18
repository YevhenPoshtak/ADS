import sys

class Node:
    def __init__(self, key=None):
        self._key = key

    def empty(self):
        return self._key is None

    def setKey(self, key):
        self._key = key

    def key(self):
        return self._key

class Tree(Node):
    def __init__(self, key=None):
        super().__init__(key)
        self._children = []

    def empty(self):
        return super().empty() and len(self._children) == 0

    def addChild(self, child):
        self._children.append(child)

    def removeChild(self, key):
        for child in self._children:
            if child.key() == key:
                self._children.remove(child)
                return True
        return False

    def getChild(self, key):
        for child in self._children:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self._children

    def sortChildren(self):
        self._children.sort(key=lambda x: x.key())
        for child in self._children:
            child.sortChildren()

def print_tree(node, depth):
    if node.key() is not None:
        print(" " * depth + node.key())
        next_depth = depth + 1
    else:
        next_depth = 0
        
    for child in node.getChildren():
        print_tree(child, next_depth)

def main():
    input_data = sys.stdin.read().splitlines()
    n = int(input_data[0].strip())
        
    root = Tree(None)
    
    for i in range(1, min(n + 1, len(input_data))):
        path = input_data[i].strip()
            
        parts = path.split('\\')
        curr = root
        
        for part in parts:
            child = curr.getChild(part)
            if child is None:
                child = Tree(part)
                curr.addChild(child)
            curr = child
            
    root.sortChildren()
    print_tree(root, 0)

if __name__ == '__main__':
    main()