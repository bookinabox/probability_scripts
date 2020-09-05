from permutation import perm
def combination(n: int, r: int):
    """Calculates the combination of n items, choose r"""
    num = 1
    for i in range(n-r, n):
        num *= i+1
    return num//perm(r)
