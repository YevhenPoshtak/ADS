import sys

class Stos:
    def __init__(self) -> None:
        self.items = []

    def push(self, n: int) -> str:
        self.items.append(n)
        return "ok"

    def pop(self) -> str:
        if not self.is_empty():
            return str(self.items.pop())
        return "error"

    def back(self) -> str:
        if not self.is_empty():
            return str(self.items[-1])
        return "error"

    def size(self) -> int:
        return len(self.items)

    def clear(self) -> str:
        self.items.clear()
        return "ok"

    def is_empty(self) -> bool:
        return len(self.items) == 0


def main() -> None:
    stos = Stos()
    
    for line in sys.stdin:
        parts = line.split()
            
        command = parts[0]
        
        if command == "push":
            n = int(parts[1])
            print(stos.push(n))
            
        elif command == "pop":
            print(stos.pop())
                
        elif command == "back":
            print(stos.back())
                
        elif command == "size":
            print(stos.size())
            
        elif command == "clear":
            print(stos.clear())
            
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()