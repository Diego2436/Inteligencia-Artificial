import numpy as np


def f(x, y):
    term1 = 1.5 - x + x * y
    term2 = 2.25 - x + x * y**2
    term3 = 2.625 - x + x * y**3
    return term1**2 + term2**2 + term3**2


def find_minimum(iterations=10000, x_range=(-4.5, 4.5), y_range=(-4.5, 4.5)):
    min_x = None
    min_y = None
    min_value = float('inf')

    for _ in range(iterations):
        current_x = np.random.uniform(x_range[0], x_range[1])
        current_y = np.random.uniform(y_range[0], y_range[1])
        current_value = f(current_x, current_y)

        if (current_value < min_value):
            min_x, min_y = current_x, current_y
            min_value = current_value

    return min_x, min_y


min_x, min_y = find_minimum()
print(f"Valores mínimos: ({min_x}, {min_y})")
