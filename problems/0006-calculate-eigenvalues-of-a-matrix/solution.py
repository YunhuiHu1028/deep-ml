import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    eigenvalues = np.linalg.eigvals(matrix)
    
    sorted_eigs = sorted(eigenvalues, key=lambda x: (x.real, x.imag), reverse=True)

    return [float(x.real) if x.imag == 0 else complex(x) for x in sorted_eigs]