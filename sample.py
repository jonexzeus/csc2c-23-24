from itertools import permutations

W = 'HOPE'


all_permutations = permutations(W)

permed = []

for perm in all_permutations:
    sorted = ''.join(perm)
    permed.append(sorted)


print("Permutations of the letters in the word 'HOPE':", permed)
