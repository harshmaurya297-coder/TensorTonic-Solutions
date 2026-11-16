import numpy as np

def mod(x : list) -> float:
    ans = 0

    for i in range(0, len(x)):
        ans = ans + (x[i]*x[i])
    
    return float(ans**0.5)


def dot_product(x: list, y: list) -> float:
   
    ans = 0
    
    for i in range(0, max(len(x), len(y))):
        ans = ans + (x[i]*y[i])

    return float(ans)

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    pass
    if dot_product(a, b) == 0 : 
        return 0.0
    return float(dot_product(a, b)/(mod(a)*mod(b)))