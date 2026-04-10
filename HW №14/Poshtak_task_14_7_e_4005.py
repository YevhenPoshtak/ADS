import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def push(self, item):
        new_node = Node(item)
        if self.empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node

    def pop(self):
        if self.empty():
            return "error"
            
        node = self.front
        item = node.item
        self.front = self.front.next
        
        if self.front is None:
            self.back = None
            
        del node
        return item

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    deck1 = Queue()
    deck2 = Queue()
    
    for x in input_data[1 : n // 2 + 1]:
        deck1.push(int(x))
        
    for x in input_data[n // 2 + 1 : n + 1]:
        deck2.push(int(x))
        
    moves = 0
    max_moves = 200000
    
    while not deck1.empty() and not deck2.empty() and moves < max_moves:
        c1 = deck1.pop()
        c2 = deck2.pop()
        
        if c1 == 0 and c2 == n - 1:
            p1_wins = True
        elif c2 == 0 and c1 == n - 1:
            p1_wins = False
        elif c1 > c2:
            p1_wins = True
        else:
            p1_wins = False
            
        if p1_wins:
            deck1.push(c1)
            deck1.push(c2)
        else:
            deck2.push(c1)
            deck2.push(c2)
            
        moves += 1
        
    if deck1.empty():
        print(f"second {moves}")
    elif deck2.empty():
        print(f"first {moves}")
    else:
        print("draw")

if __name__ == "__main__":
    main()