import sys

class Node:
    def __init__(self, key=None, fee=0):
        self._key = key
        self.fee = fee

    def empty(self):
        return self._key is None

    def setKey(self, key):
        self._key = key

    def key(self):
        return self._key

class Tree(Node):
    def __init__(self, key=None, fee=0):
        super().__init__(key, fee)
        self.children = []

    def empty(self):
        return super().empty() and len(self.children) == 0

    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, key):
        for child in self.children:
            if child.key() == key:
                self.children.remove(child)
                return True
        return False

    def getChild(self, key):
        for child in self.children:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self.children

def get_min_fee(node: Tree) -> int:
    children = node.getChildren()
    
    if not children:
        return node.fee
    
    min_child_fee = min(get_min_fee(child) for child in children)
    
    return node.fee + min_child_fee

def main():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    
    nodes = {i: Tree(key=i) for i in range(1, N + 1)}
    
    idx = 1
    for i in range(1, N + 1):
        fee = int(input_data[idx])
        k = int(input_data[idx + 1])
        
        nodes[i].fee = fee
        
        for j in range(k):
            child_id = int(input_data[idx + 2 + j])
            nodes[i].addChild(nodes[child_id])
            
        idx += 2 + k
        
    director_node = nodes[1]
    result = get_min_fee(director_node)
    
    print(result)

if __name__ == '__main__':
    main()