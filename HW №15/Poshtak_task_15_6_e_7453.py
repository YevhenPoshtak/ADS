import sys

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def AddToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def RotateRight(self, k: int) -> None:
        if self.size <= 1:
            return
            
        k = k % self.size
        if k == 0:
            return
            
        steps_to_new_tail = self.size - k - 1
        new_tail = self.head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        self.tail.next = self.head
        self.head = new_head
        self.tail = new_tail
        self.tail.next = None
        
    def Print(self) -> None:
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

def main() -> None:
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    linked_list = List()
    
    for i in range(1, n + 1):
        linked_list.AddToTail(int(input_data[i]))
        
    for i in range(n + 1, len(input_data)):
        k = int(input_data[i])
        linked_list.RotateRight(k)
        linked_list.Print()

if __name__ == '__main__':
    main()