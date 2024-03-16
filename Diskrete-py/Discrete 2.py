import random as r

n = 20
InputX = []
OutputF = []
OutputH = []
add = []
subtract = []
multiply = []
division = []
H = []
F = []

# input list
for _ in range(n):
    num = r.randint(-10, 10)
    InputX.append(num)

# sort the main lists
InputX.sort()

# f(x)
for numberX in InputX:
    values = 4 * (numberX ** 2) - 9
    OutputF.append(values)

OutputF.sort()

# h(x)
for numberH in InputX:
    valueH = (2 * numberH - 3) / 4
    OutputH.append(valueH)

OutputH.sort()

# function operations
for f, h in zip(OutputF, OutputH):
    add.append(f + h)
    subtract.append(f - h)
    multiply.append(f * h)
    # Avoid division by zero
    if h != 0:
        division.append(round(f / h, 2))
    else:
        division.append("Undefined")

# composition of functions
for x in OutputH:
    H.append(4 * (x ** 2) - 9)

for y in OutputF:
    F.append((2 * y - 3) / 4)

# sort the remaining lists
add.sort()
subtract.sort()
multiply.sort()
division.sort()
H.sort()
F.sort()

# inverse functions
inverse_f = [[OutputF[i], InputX[i]] for i in range(n)]
inverse_h = [[OutputH[i], InputX[i]] for i in range(n)]

print(f"""
Input X: {InputX}
Output F: {OutputF}
Output H: {OutputH}

F+H: {add}
F-H: {subtract}
F*H: {multiply}
F/H: {division}

F o G: {F}
G o H: {H}

Inverse of f: {inverse_f}
Inverse of g: {inverse_h}
""")