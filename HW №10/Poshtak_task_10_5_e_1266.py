import sys

class Solution:
    def maximizeRecordSpace(self, N: int, tracks: list[int]) -> int:
        n = len(tracks)
        rem_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            rem_sum[i] = rem_sum[i + 1] + tracks[i]
            
        self.best = -1
        self.found = False
        
        def backtrack(idx: int, curr: int) -> None:
            if self.found: return
            
            if curr > self.best:
                self.best = curr
                if curr == N:
                    self.found = True
                    return
                    
            if idx == n or curr + rem_sum[idx] <= self.best:
                return
                
            if curr + tracks[idx] <= N:
                backtrack(idx + 1, curr + tracks[idx])
            backtrack(idx + 1, curr)

        backtrack(0, 0)
        return self.best

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    idx, n_elements = 0, len(data)
    
    while idx < n_elements:
        N, num_tracks = data[idx], data[idx+1]
        tracks = data[idx+2 : idx+2+num_tracks]
        idx += 2 + num_tracks
        print(f"sum:{Solution().maximizeRecordSpace(N, tracks)}")
        