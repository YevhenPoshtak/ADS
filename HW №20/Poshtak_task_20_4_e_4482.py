import sys

class SegmentTreeMinMax:
    def __init__(self, array: list[int]) -> None:
        self.n = len(array)
        self.tree_min = [0] * (2 * self.n)
        self.tree_max = [0] * (2 * self.n)
        
        for i in range(self.n):
            self.tree_min[self.n + i] = array[i]
            self.tree_max[self.n + i] = array[i]
            
        for i in range(self.n - 1, 0, -1):
            self.tree_min[i] = min(self.tree_min[2 * i], self.tree_min[2 * i + 1])
            self.tree_max[i] = max(self.tree_max[2 * i], self.tree_max[2 * i + 1])
            
    def update(self, pos: int, value: int) -> None:
        pos += self.n
        self.tree_min[pos] = value
        self.tree_max[pos] = value
        
        pos //= 2
        while pos > 0:
            self.tree_min[pos] = min(self.tree_min[2 * pos], self.tree_min[2 * pos + 1])
            self.tree_max[pos] = max(self.tree_max[2 * pos], self.tree_max[2 * pos + 1])
            pos //= 2
            
    def query(self, left: int, right: int) -> tuple[int, int]:
        left += self.n
        right += self.n
        res_min = 2000000000
        res_max = 0
        
        while left <= right:
            if left % 2 == 1:
                res_min = min(res_min, self.tree_min[left])
                res_max = max(res_max, self.tree_max[left])
                left += 1
            if right % 2 == 0:
                res_min = min(res_min, self.tree_min[right])
                res_max = max(res_max, self.tree_max[right])
                right -= 1
            
            left //= 2
            right //= 2
            
        return res_min, res_max

def main() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    array = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    queries = input_data[n+2:]
    
    st = SegmentTreeMinMax(array)
    
    idx = 0
    result = []
    
    for _ in range(m):
        q = int(queries[idx])
        l = int(queries[idx+1])
        r = int(queries[idx+2])
        idx += 3
        
        if q == 1:
            min_val, max_val = st.query(l - 1, r - 1)
            if min_val == max_val:
                result.append("draw")
            else:
                result.append("wins")
        elif q == 2:
            st.update(l - 1, r)
            
    print('\n'.join(result))

if __name__ == '__main__':
    main()