import numpy as np

def dot_product(x: list, y: list) -> float:
    lenX = len(x)
    lenY = len(y)
    
    ans = 0
    
    for i in range(0, max(lenX, lenY)):
        ans = ans + (x[i]*y[i])

    return float(ans)