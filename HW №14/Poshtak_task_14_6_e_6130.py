import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self._size = 0

    def empty(self):
        return self.front is None and self.back is None

    def push_front(self, item):
        node = Node(item)
        node.next = self.front
        
        if not self.empty():
            self.front.prev = node
        else:
            self.back = node
            
        self.front = node
        self._size += 1
        return "ok"

    def push_back(self, item):
        node = Node(item)
        node.prev = self.back
        
        if not self.empty():
            self.back.next = node
        else:
            self.front = node
            
        self.back = node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self.empty():
            return "error"
            
        node = self.front
        item = node.item
        self.front = node.next
        
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None
            
        del node
        self._size -= 1
        return item

    def pop_back(self):
        if self.empty():
            return "error"
            
        node = self.back
        item = node.item
        self.back = node.prev
        
        if self.back is None:
            self.front = None
        else:
            self.back.next = None
            
        del node
        self._size -= 1
        return item

    def get_front(self):
        if self.empty():
            return "error"
        return self.front.item

    def get_back(self):
        if self.empty():
            return "error"
        return self.back.item

    def size(self):
        return self._size

    def clear(self):
        while not self.empty():
            node = self.front
            self.front = self.front.next
            
            if self.front is None:
                self.back = None
            else:
                self.front.prev = None
                
            del node
            
        self._size = 0
        return "ok"

def main():
    deque = Deque()
    
    commands = {
        "push_front": deque.push_front,
        "push_back": deque.push_back,
        "pop_front": deque.pop_front,
        "pop_back": deque.pop_back,
        "front": deque.get_front,
        "back": deque.get_back,
        "size": deque.size,
        "clear": deque.clear
    }

    for line in sys.stdin.read().splitlines():
        if not line:
            continue
            
        parts = line.split()
        cmd = parts[0]
        
        if cmd == "exit":
            print("bye")
            break
            
        if cmd in commands:
            result = commands[cmd](*parts[1:])
            print(result)

if __name__ == "__main__":
    main()