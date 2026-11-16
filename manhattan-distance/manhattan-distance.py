import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    pass

    ans = 0

    for i in range(0, max(len(x), len(y))):
        ans = ans + abs(x[i] - y[i])
    
    return float(ans)
    