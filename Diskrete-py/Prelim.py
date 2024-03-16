import random

def calculate_fx(x):
    return 4*x

def calculate_gx(x):
    return 2*x-3

def calculate_inverse(function_output, input_values):
    return [(output, input_val) for output, input_val in zip(function_output, input_values)]

def perform_operations(F, H):
    
    subtract = [f - h for f, h in zip(F, H)]
    
    division = [round(f / h, 2) if h != 0 else "Undefined" for f, h in zip(F, H)]
    return subtract, division

Input = [random.randint(0, 10) for _ in range(10)]



OutputF = [calculate_fx(x) for x in Input]

OutputG = [calculate_gx(x) for x in Input]

subtract, division = perform_operations(OutputF, OutputG)

F_G = [calculate_fx(y) for y in OutputG]


print(f"""
Input: {Input}
Output F: {OutputF}
Output G: {OutputG}


FsubtractionG: {subtract}
FdivisionG: {division}

FcomposeG: {F_G}

""")
