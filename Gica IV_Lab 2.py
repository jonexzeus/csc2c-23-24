import random

def calculate_fx(x):
    return 4 * x**2 - 9

def calculate_hx(x):
    return (2 * x - 3) / 4

def calculate_inverse(function_output, input_values):
    return [(output, input_val) for output, input_val in zip(function_output, input_values)]

def perform_operations(F, H):
    add = [f + h for f, h in zip(F, H)]
    subtract = [f - h for f, h in zip(F, H)]
    multiply = [f * h for f, h in zip(F, H)]
    division = [round(f / h, 2) if h != 0 else "Undefined" for f, h in zip(F, H)]
    return add, subtract, multiply, division

InputX = [random.randint(-10, 10) for _ in range(20)]
InputX.sort()

# Calculate OutputF and sort it
OutputF = [calculate_fx(x) for x in InputX]
OutputF.sort()

OutputH = [calculate_hx(x) for x in InputX]
OutputH.sort()

# Perform operations
add, subtract, multiply, division = perform_operations(OutputF, OutputH)

# Calculate compositions
F_G = [calculate_hx(y) for y in OutputF]
G_F = [calculate_fx(x) for x in OutputH]

# Calculate inverse functions
inverse_f = calculate_inverse(OutputF, InputX)
inverse_h = calculate_inverse(OutputH, InputX)

# Display the results
print(f"""
Input: {InputX}
Output F: {OutputF}
Output H: {OutputH}

F+H: {add}
F-H: {subtract}
F*H: {multiply}
F/H: {division}

F(G): {F_G}
G(F): {G_F}

Inverse of f: {inverse_f}
Inverse of g: {inverse_h}
""")
