def g(x, a):
    return (2 * x + a / x ** 2) / 3


def fixed_point_iteration(a):
    tol = 1e-4

    for i in range(1000):
        x_new = g(x, a)
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return None


approx, steps = fixed_point_iteration(1)
print(f"Approximation to √3: {approx:.6f} with {steps} steps")