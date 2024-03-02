from itertools import permutations, combinations
import random

def calculate_permutations(elements, r):
    perms = list(permutations(elements, r))
    return perms

def calculate_combinations(elements, r):
    combs = list(combinations(elements, r))
    return combs

def check_combination_match(user_input, permutations_list):
    return tuple(map(int, user_input)) in permutations_list

elements = [0, 1, 2, 3, 4, 5]
r = 4

perms = calculate_permutations(elements, r)
combs= calculate_combinations(elements, r)

user_input = input("Enter a 4-digit number: ")

select = random.sample(combs)

if len(user_input) == 4 and user_input.isdigit():
    if check_combination_match(user_input, perms):
        print("Open")
    else:
        print("Please try again.")
else:
    print("Invalid input. Please enter a 4-digit number.")

print("selected comb:", select)
print("Combinations: ", combs)