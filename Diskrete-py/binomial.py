import math

def compute_coefficients(binomial):
    degree = int(binomial.split('^')[1])
    coefficients = []
    for k in range(degree + 1):
        coefficient = math.comb(degree, k)
        coefficients.append(coefficient)
    return coefficients

binomials = [
    "(x + 2y)^5",
    "(2x - 2y)^6",
    "(x + 3y)^7",
    "(-3x - y)^8",
    "(4x + 3y)^10",
    "(-5x - 2y)^12",
    "(3x + y)^14",
    "(-x - 2y)^16",
    "(2x + y)^18",
    "(2x - 4y)^20"
]

coefficients_lists = []

for binomial in binomials:
    coefficients_lists.append(compute_coefficients(binomial))

# Print coefficients for each expression
for i, binomial in enumerate(binomials):
    print(f"Coefficients for {binomial}: {coefficients_lists[i]}")
