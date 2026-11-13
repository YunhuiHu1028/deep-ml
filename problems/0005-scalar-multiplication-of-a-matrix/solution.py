def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    if not matrix:
        return False
    
    rows = len(matrix)

    for r in range(rows):
        return [[element * scalar for element in rows] for rows in matrix]