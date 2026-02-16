import sys

class Solution:
    def bus_problem(self, n: int, m: int, input_iterator: iter) -> int:
        all_relative_arrival_times: list = []
        current_offset: int = 0
        
        for _ in range(n):
            dist_to_next: int = int(next(input_iterator))
            k: int = int(next(input_iterator))
            
            for _ in range(k):
                arrival_time: int = int(next(input_iterator))
                all_relative_arrival_times.append(arrival_time - current_offset)
            
            current_offset += dist_to_next
            
        all_relative_arrival_times.sort()
        
        workers_to_take: int = min(len(all_relative_arrival_times), m)
            
        last_worker_relative_time: int = all_relative_arrival_times[workers_to_take - 1]
        
        return max(0, last_worker_relative_time) + current_offset

if __name__ == "__main__":
    input_data: list = sys.stdin.read().split()
    iterator: iter = iter(input_data)
    
    n_in: int = int(next(iterator))
    m_in: int = int(next(iterator))

    print(Solution().bus_problem(n_in, m_in, iterator))