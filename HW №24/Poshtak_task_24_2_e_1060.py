import sys

def parse_matrix(input_items: iter, size: int) -> tuple:
    matrix = []
    start_position = None
    target_position = None
    
    for row_index in range(size):
        row = list(next(input_items))
        matrix.append(row)
        for col_index in range(size):
            if row[col_index] == '@':
                start_position = (row_index, col_index)
            elif row[col_index] == 'X':
                target_position = (row_index, col_index)
                
    return matrix, start_position, target_position

def find_shortest_path(matrix: list, size: int, start: tuple, target: tuple) -> list | None:
    queue = [start]
    parent_cells = {start: None}
    
    while queue:
        current_row, current_col = queue.pop(0)
        
        if (current_row, current_col) == target:
            path = []
            current_cell = target
            while current_cell is not None:
                path.append(current_cell)
                current_cell = parent_cells[current_cell]
            return path[::-1]
            
        for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_row = current_row + row_offset
            neighbor_col = current_col + col_offset
            neighbor_cell = (neighbor_row, neighbor_col)
            
            if 0 <= neighbor_row < size and 0 <= neighbor_col < size and neighbor_cell not in parent_cells:
                if matrix[neighbor_row][neighbor_col] != 'O':
                    parent_cells[neighbor_cell] = (current_row, current_col)
                    queue.append(neighbor_cell)
    return None

def main() -> None:
    input_data = sys.stdin.read().split()
        
    input_items = iter(input_data)
    matrix_size = int(next(input_items))
    
    matrix, start, target = parse_matrix(input_items, matrix_size)
    path = find_shortest_path(matrix, matrix_size, start, target)
    
    if path:
        sys.stdout.write("Y\n")
        for row_index, col_index in path[1:]:
            matrix[row_index][col_index] = '+'
        sys.stdout.write("\n".join("".join(row) for row in matrix) + "\n")
    else:
        sys.stdout.write("N\n")

if __name__ == "__main__":
    main()