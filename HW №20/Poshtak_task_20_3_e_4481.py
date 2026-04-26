import sys
import math

class SegmentTree:
    def __init__(self, array: list[int]) -> None:
        self.n = len(array)
        self.tree = [0] * (2 * self.n)
        
        for i in range(self.n):
            self.tree[self.n + i] = array[i]
            
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])
            
    def update(self, pos: int, value: int) -> None:
        pos += self.n
        self.tree[pos] = value
        
        pos //= 2
        while pos > 0:
            self.tree[pos] = math.gcd(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2
            
    def query(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        res = 0
        
        while left <= right:
            if left % 2 == 1:
                res = math.gcd(res, self.tree[left])
                left += 1
            if right % 2 == 0:
                res = math.gcd(res, self.tree[right])
                right -= 1
            
            left //= 2
            right //= 2
            
        return res

def main() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    array = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    queries = input_data[n+2:]
    
    st = SegmentTree(array)
    
    idx = 0
    result = []
    
    for _ in range(m):
        q = int(queries[idx])
        l = int(queries[idx+1])
        r = int(queries[idx+2])
        idx += 3
        
        if q == 1:
            ans = st.query(l - 1, r - 1)
            result.append(str(ans))
        elif q == 2:
            st.update(l - 1, r)
            
    print('\n'.join(result))

if __name__ == '__main__':
    main()