import sys

class Stack:
    def __init__(self) -> None:
        self.items: list[int] = []

    def push(self, n: int) -> None:
        self.items.append(n)

    def pop(self) -> int:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


def main() -> None:
    iterator = iter(int(x) for x in sys.stdin.read().split())
    
    for n in iterator:
        if n == 0:
            break
            
        while True:
            first_car_in_B = next(iterator, 0)
            if first_car_in_B == 0:
                print()
                break
                
            target_B_order = [first_car_in_B]
            for _ in range(n - 1):
                target_B_order.append(next(iterator))
                
            station = Stack()
            car_from_A = 1
            is_possible = True
            
            for next_needed_in_B in target_B_order:
                while car_from_A <= next_needed_in_B:
                    station.push(car_from_A)
                    car_from_A += 1
                    
                if not station.is_empty() and station.top() == next_needed_in_B:
                    station.pop()
                else:
                    is_possible = False
                    break
                    
            if is_possible:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()