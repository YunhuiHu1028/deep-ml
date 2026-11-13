def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    if not matrix:
        return False
    
    return [[element * scalar for element in row] for row in matrix]