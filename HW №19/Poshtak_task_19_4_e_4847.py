import sys

class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        self.pos = {}

    def swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i][1]] = i
        self.pos[self.heap[j][1]] = j

    def sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][0] > self.heap[parent][0]:
                self.swap(idx, parent)
                idx = parent
            else:
                break

    def sift_down(self, idx: int) -> None:
        n = len(self.heap)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            
            if largest != idx:
                self.swap(idx, largest)
                idx = largest
            else:
                break

    def add(self, item_id: str, priority: int) -> None:
        self.heap.append([priority, item_id])
        idx = len(self.heap) - 1
        self.pos[item_id] = idx
        self.sift_up(idx)

    def pop(self) -> str | None:
        if not self.heap:
            return None
        
        max_priority, max_id = self.heap[0]
        del self.pos[max_id]

        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self.pos[last_item[1]] = 0
            self.sift_down(0)
        
        return f"{max_id} {max_priority}"

    def change(self, item_id: str, new_priority: int) -> None:
        idx = self.pos[item_id]
        old_priority = self.heap[idx][0]
        self.heap[idx][0] = new_priority
        
        if new_priority > old_priority:
            self.sift_up(idx)
        elif new_priority < old_priority:
            self.sift_down(idx)

def main() -> None:
    heap = MaxHeap()
    
    commands = {
        "ADD": lambda p: heap.add(p[1], int(p[2])),
        "POP": lambda p: print(res) if (res := heap.pop()) else None,
        "CHANGE": lambda p: heap.change(p[1], int(p[2]))
    }
    
    for line in sys.stdin:
        parts = line.strip().split()
        if parts and parts[0] in commands:
            commands[parts[0]](parts)

if __name__ == '__main__':
    main()