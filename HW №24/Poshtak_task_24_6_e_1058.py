import sys

def get_lake_size(start_cell: tuple, flooded_cells: set, visited: set) -> int:
    queue = [start_cell]
    visited.add(start_cell)
    current_lake_size = 0
    
    while queue:
        current_row, current_col = queue.pop(0)
        current_lake_size += 1
        
        for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_row = current_row + row_offset
            neighbor_col = current_col + col_offset
            neighbor_cell = (neighbor_row, neighbor_col)
            
            if neighbor_cell in flooded_cells and neighbor_cell not in visited:
                visited.add(neighbor_cell)
                queue.append(neighbor_cell)
                
    return current_lake_size

def main() -> None:
    input_data = sys.stdin.read().split()
        
    input_items = iter(input_data)
    rows_count = int(next(input_items))
    cols_count = int(next(input_items))
    flooded_count = int(next(input_items))
    
    flooded_cells = set()
    for _ in range(flooded_count):
        row = int(next(input_items))
        col = int(next(input_items))
        flooded_cells.add((row, col))
        
    max_lake_size = 0
    visited_cells = set()
    
    for cell in flooded_cells:
        if cell not in visited_cells:
            current_size = get_lake_size(cell, flooded_cells, visited_cells)
            if current_size > max_lake_size:
                max_lake_size = current_size
                
    sys.stdout.write(str(max_lake_size) + "\n")

if __name__ == "__main__":
    main()