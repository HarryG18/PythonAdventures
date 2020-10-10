import numpy as np
def id_mtrx(n):
    # if type(n) is not int:
    #     return "Error"
    return "Error" if type(n) is not int else np.identity(n, dtype=int).tolist() if n > 0 else np.fliplr(np.identity(-n, dtype= int)).tolist()

print(id_mtrx(2))