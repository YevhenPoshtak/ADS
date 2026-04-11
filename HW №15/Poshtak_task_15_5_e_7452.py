import sys

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None
        self.prev: [Node | None] = None  

class List:
    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" " if current.next else "")
            current = current.next
        print() 

    def PrintReverse(self) -> None:
        current = self.tail
        while current:
            print(current.data, end=" " if current.prev else "")
            current = current.prev
        print()

def main() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    numbers = input_data[1:n+1]
    
    linked_list = List()
    
    for num in numbers:
        linked_list.addToTail(int(num))
    
    linked_list.Print()
    linked_list.PrintReverse()

if __name__ == "__main__":
    main()