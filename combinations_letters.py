from permutation import perm

def comb_letters(word: str):
    letters = {l for l in word}
    divisor = 1
    for i in letters:
        divisor *= perm(word.count(i))
    return perm(len(word)) // divisor
print(comb_letters(input()))
