import random

def function(x):
    return 2 * x + 1

def function1(h):
    return h**2 + 2

def function2(a):
    return function(a) + function1(a)

def function3(s):
    return function(s) - function1(s)

def function4(m):
    return function(m) * function1(m)

def function5(d):
    if function1(d) != 0:
        return function(d) / function1(d)
    else:
        return "Error: Division by zero"

def compose_f_h(n):
    return function(function1(n))

def compose_h_f(n):
    return function1(function(n))

random_numbers = [random.randint(-10, 10) for _ in range(5)]

Output_f = [function(num) for num in random_numbers]
Output_h = [function1(num) for num in random_numbers]
Output_a = [function2(num) for num in random_numbers]
Output_s = [function3(num) for num in random_numbers]
Output_m = [function4(num) for num in random_numbers]
Output_d = [function5(num) for num in random_numbers]
Output_f_h = [compose_f_h(num) for num in random_numbers]
Output_h_f = [compose_h_f(num) for num in random_numbers]

# Sort the input and output lists
sorted_numbers = sorted(random_numbers)
sorted_results_f = sorted(Output_f)
sorted_results_h = sorted(Output_h)
sorted_results_a = sorted(Output_a)
sorted_results_s = sorted(Output_s)
sorted_results_m = sorted(Output_m)
sorted_results_d = Output_d 
sorted_results_f_h = sorted(Output_f_h)
sorted_results_h_f = sorted(Output_h_f)


ordered_pairs = [(x, fx) for x, fx in zip(sorted_numbers, sorted_results_f)]
ordered_pairs1 = [(h, fh) for h, fh in zip(sorted_numbers, sorted_results_h)]

inverse_ordered_pairs = [(fx, x) for x, fx in ordered_pairs]
inverse_ordered_pairs1 = [(fh, h) for h, fh in ordered_pairs1]

print("Input_x:", sorted_numbers)
print("Output_(f):", sorted_results_f)
print("Output_(h):", sorted_results_h)
print("Output_(a):", sorted_results_a)
print("Output_(s):", sorted_results_s)
print("Output_(m):", sorted_results_m)
print("Output_(d):", sorted_results_d)
print("Output_(f o h):", sorted_results_f_h)
print("Output_(h o f):", sorted_results_h_f)
print("Ordered Pairs(f) (x, f(x)):", ordered_pairs)
print("Inverse Ordered Pairs(f) (f(x), x):", inverse_ordered_pairs)
print("Ordered Pairs(h) (h, f(h)):", ordered_pairs1)
print("Inverse Ordered Pairs(h) (f(h), h:", inverse_ordered_pairs1)