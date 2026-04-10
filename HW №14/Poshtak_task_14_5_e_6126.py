import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self._size = 0

    def empty(self):
        return self.front is None and self.back is None

    def push(self, item):
        new_node = Node(item)
        if self.empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
            
        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        del current_front
        
        if self.front is None:
            self.back = None
            
        self._size -= 1
        return item

    def get_front(self):
        if self.empty():
            return "error"
        return self.front.item

    def size(self):
        return self._size

    def clear(self):
        while not self.empty():
            current_front = self.front
            self.front = self.front.next
            
            if self.front is None:
                self.back = None
                
            del current_front
            
        self._size = 0
        return "ok"

def main():
    queue = Queue()
    
    commands = {
        "push": queue.push,
        "pop": queue.pop,
        "front": queue.get_front,
        "size": queue.size,
        "clear": queue.clear
    }

    for line in sys.stdin.read().splitlines():
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