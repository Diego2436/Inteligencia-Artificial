import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Definir la función de Himmelblau
def himmelblau(X):
    x, y = X
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Limites para x e y
bounds = [(-5, 5), (-5, 5)]

# Puntos iniciales para probar el algoritmo de optimización
initial_guesses = [
    (-3, -3),
    (3, 3),
    (-3, 3),
    (3, -3),
    (0, 0)
]

# Optimización para encontrar los mínimos locales dentro de los límites
for guess in initial_guesses:
    res = minimize(himmelblau, guess, method='L-BFGS-B', bounds=bounds)
    print(f"Punto inicial: {guess}, Mínimo encontrado: {res.x}, Valor de la función: {res.fun}")

# Gráfico de la función de Himmelblau
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = himmelblau([X, Y])

plt.contour(X, Y, Z, levels=np.logspace(0, 5, 35), cmap='jet')
plt.title('Función de Himmelblau con -5<=x,y<=5')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
