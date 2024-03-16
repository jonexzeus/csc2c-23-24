import random

# Step 1: Generate 20 random integers from 0 to 10
input_values = [random.randint(0, 10) for _ in range(20)]

# Step 2: Calculate f(x) and g(x) for each input
output_f = [x / 2 for x in input_values]
output_g = [2 * x + 3 for x in input_values]

# Step 3: Calculate the sum of f(x) and g(x)
output_f_add_g = [a + b for a, b in zip(output_f, output_g)]

# Step 4: Calculate the quotient of f(x) and g(x)
output_f_div_g = [a / b if b != 0 else float('inf') for a, b in zip(output_f, output_g)]

# Step 5: Calculate the composition of (f o g)(x)
output_f_compose_g = [output_f[i] + output_g[i] for i in range(len(output_f))]

# Sort the lists
sorted_input = sorted(input_values)
sorted_output_f = sorted(output_f)
sorted_output_g = sorted(output_g)
sorted_output_f_add_g = sorted(output_f_add_g)
sorted_output_f_div_g = sorted(output_f_div_g)
sorted_output_f_compose_g = sorted(output_f_compose_g)

# Display the sorted results
print("Sorted Input:", sorted_input)
print("Sorted OutputF:", sorted_output_f)
print("Sorted OutputG:", sorted_output_g)
print("Sorted FadditionG:", sorted_output_f_add_g)
print("Sorted FdivisionG:", sorted_output_f_div_g)
print("Sorted FcomposeG:", sorted_output_f_compose_g)
