import numpy as np
import matplotlib.pyplot as plt


# Definir la función de Himmelblau
def himmelblau(X):
    x, y = X
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


# Parámetros del algoritmo de recocido simulado
def simulated_annealing(func, bounds, temp, cooling_rate, max_iter):
    # Iniciar con una solución aleatoria
    current_solution = np.random.uniform(bounds[0][0], bounds[0][1], size=2)
    current_value = func(current_solution)

    best_solution = current_solution
    best_value = current_value

    for i in range(max_iter):
        # Generar una nueva solución aleatoria cerca de la actual
        new_solution = current_solution + np.random.uniform(-1, 1, size=2)
        # Asegurarse de que esté dentro de los límites
        new_solution = np.clip(new_solution, [bounds[0][0], bounds[1][0]], [bounds[0][1], bounds[1][1]])
        new_value = func(new_solution)

        # Calcular el cambio en la calidad de la solución
        delta = new_value - current_value

        # Si la nueva solución es mejor, aceptarla
        if delta < 0 or np.random.rand() < np.exp(-delta / temp):
            current_solution = new_solution
            current_value = new_value

        # Actualizar la mejor solución encontrada
        if current_value < best_value:
            best_solution = current_solution
            best_value = current_value

        # Reducir la temperatura
        temp *= cooling_rate

    return best_solution, best_value


# Parámetros del algoritmo
bounds = [(-5, 5), (-5, 5)]  # Límites de x e y
initial_temp = 1000  # Temperatura inicial
cooling_rate = 0.99  # Tasa de enfriamiento
max_iter = 10000  # Número máximo de iteraciones

# Ejecutar recocido simulado
best_solution, best_value = simulated_annealing(himmelblau, bounds, initial_temp, cooling_rate, max_iter)
print(f"Mínimo encontrado: {best_solution}, Valor de la función: {best_value}")

# Gráfico de la función de Himmelblau
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = himmelblau([X, Y])

plt.contour(X, Y, Z, levels=np.logspace(0, 5, 35), cmap='jet')
plt.title('Función de Himmelblau con -5<=x,y<=5')
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(best_solution[0], best_solution[1], color='red', label='Mínimo encontrado')
plt.legend()
plt.show()
