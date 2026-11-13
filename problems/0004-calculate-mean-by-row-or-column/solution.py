def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix:
        return False
    
    means = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    if mode == 'row':
        for r in range(rows):
            sums = 0
            mean = 0
            sums = sum(matrix[r][c] for c in range(cols))
            mean = sums / cols
            means.append(mean)
    
    elif mode == 'column':
        for c in range(cols):
            sums = 0
            mean = 0
            sums = sum(matrix[r][c] for r in range(rows))
            mean = sums / rows
            means.append(mean)

    return means