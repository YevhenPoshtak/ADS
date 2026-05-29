import sys

def floyd_warshall(num_vertices: int, adjacency_matrix: list[list[int]]) -> list[list[int]]:
    distances = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                distances[i][j] = 0
                if adjacency_matrix[i][j] < 0:
                    distances[i][j] = adjacency_matrix[i][j]
            elif adjacency_matrix[i][j] != 0:  
                distances[i][j] = adjacency_matrix[i][j]
                
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distances[i][k] < float('inf') and distances[k][j] < float('inf'):
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        
    result_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if distances[i][j] == float('inf'):
                result_matrix[i][j] = 0
            else:
                has_negative_cycle = False
                for t in range(num_vertices):
                    if (distances[i][t] < float('inf') and 
                        distances[t][j] < float('inf') and 
                        distances[t][t] < 0):
                        has_negative_cycle = True
                        break
                
                result_matrix[i][j] = 2 if has_negative_cycle else 1
                
    return result_matrix

def main() -> None:
    input_data = sys.stdin.read().split()\
        
    num_vertices = int(input_data[0])
    adjacency_matrix = []
    data_index = 1
    
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            row.append(int(input_data[data_index]))
            data_index += 1
        adjacency_matrix.append(row)
    
    for row in floyd_warshall(num_vertices, adjacency_matrix):
        print(*(row))

if __name__ == '__main__':
    main()