def permutations(num : int):
	if num <= 0: return("Error, only positive integers supported.")
	cnt=1
	while num>0:
		cnt *= num
		num -= 1
	return cnt

number = int(input())
print(permutations(number))
