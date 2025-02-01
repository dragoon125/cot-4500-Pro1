import math

# Approximation Algorithm 2.1
x0 = 1.5
tol = 0.000001

iter = 0
diff = x0
x = x0

print(f"{iter} : {x}")

while diff >= tol:
    iter += 1
    y = x

    x = (x / 2) + (1 / x)
    print(f"{iter} : {x}")

    diff = abs(x - y)

print(f"\nConvergence after {iter} iterations")

# Bisection Method 2.1
def f(x):
    return ((x ** 3) - (4 * x) - 9)

tol = 0.000001
left = 2
right = 3

max = 50
i = 0

while abs(right - left) > tol and i < max:
    i += 1
    p = (left + right) / 2

    if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
        right = p
    else:
        left = p

print(f"\n The approximate root: {p:.6f}\n")

# Fixed-Point Iteration 2.2
p0 = 1.5
result = "Failure"
tol = 0.000001
NO = 50

i = 1
p = 0

while i <= NO:
    p = p0 - p0*p0*p0 -4*p0*p0 + 10
    #p = math.sqrt(10 - p0*p0*p0) / 2

    if math.isnan(p):
        print("\nResult diverges")
        break

    print(f"{i} : {p}")

    if abs(p - p0) < tol:
        result = "Success"
        break

    i += 1
    p0 = p

print(f"\n{result} after {i} iterations\n")

#Newton-Raphson Method 2.3
def f(x):
    return x**3 - 4*x - 9

def f2(x):
    return 3*x**2 - 4

p_prev = 2.0
TOL = 0.000001
N0 = 50

i = 1

while i <= N0:
    if f2(p_prev) == 0:
        print("Derivative is zero. Newton's method fails.")
        break

    p_next = p_prev - f(p_prev) / f2(p_prev)

    if abs(p_next - p_prev) < TOL:
        print(f"Success, the approximate root: {p_next:.6f}")
        break

    i += 1
    p_prev = p_next

else:
    print("Max iterations performed")
