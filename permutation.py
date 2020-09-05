def perm(num : int):
    """Calculates the permutation of int num, given num >= 0"""
	if num < 0: return("Error, only non-negative integers supported.")
        elif num == 0: return 1
	cnt=1
	while num>0:
		cnt *= num
		num -= 1
	return cnt
