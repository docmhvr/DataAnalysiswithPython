import numpy as np

def calculate(list):
    import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of columns
            matrix.mean(axis=1).tolist(),  # Mean of rows
            matrix.mean().tolist()  # Mean of entire matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),  # Variance of columns
            matrix.var(axis=1).tolist(),  # Variance of rows
            matrix.var().tolist()  # Variance of entire matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),  # Standard deviation of columns
            matrix.std(axis=1).tolist(),  # Standard deviation of rows
            matrix.std().tolist()  # Standard deviation of entire matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),  # Max of columns
            matrix.max(axis=1).tolist(),  # Max of rows
            matrix.max().tolist()  # Max of entire matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),  # Min of columns
            matrix.min(axis=1).tolist(),  # Min of rows
            matrix.min().tolist()  # Min of entire matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),  # Sum of columns
            matrix.sum(axis=1).tolist(),  # Sum of rows
            matrix.sum().tolist()  # Sum of entire matrix
        ]
    }

    return calculations