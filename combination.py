from permutation import perm
def combination(n: int, r: int):
    num = 1
    for i in range(n-r, n):
        num *= i+1
    #print(num)
    return num//perm(r)
#print(combination(20, 3))
