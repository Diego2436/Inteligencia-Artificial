import heapq
import time

# Implementación de Cola de Prioridad (usada en A*)
class ColaPrioridad:
    def __init__(self):
        self.items = []
    
    def insertar(self, item, prioridad):
        heapq.heappush(self.items, (prioridad, item))
    
    def quitar(self):
        if not self.is_empty():
            return heapq.heappop(self.items)[1]  # Devolver solo el elemento, no la prioridad
        return None
    
    def is_empty(self):
        return len(self.items) == 0

# Laberinto con A*
class LaberintoAStar:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.filas = len(maze)
        self.columnas = len(maze[0])
        self.visitados = [[False for _ in range(self.columnas)] for _ in range(self.filas)]
    
    def es_valido(self, fila, col):
        return (0 <= fila < self.filas and
                0 <= col < self.columnas and
                self.maze[fila][col] == 0 and
                not self.visitados[fila][col])
    
    def heuristica_manhattan(self, nodo_actual):
        fila_actual, col_actual = nodo_actual
        fila_meta, col_meta = self.end
        return abs(fila_actual - fila_meta) + abs(col_actual - col_meta)

    def a_star(self):
        cola_prioridad = ColaPrioridad()
        cola_prioridad.insertar((self.start, [self.start], 0), 0)  # Nodo, Camino, Costo g
        
        while not cola_prioridad.is_empty():
            (fila_actual, col_actual), camino, costo_g = cola_prioridad.quitar()

            if (fila_actual, col_actual) == self.end:
                return camino
            
            self.visitados[fila_actual][col_actual] = True

            # Movimientos posibles: arriba, abajo, izquierda, derecha
            movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for mov in movimientos:
                nueva_fila = fila_actual + mov[0]
                nueva_col = col_actual + mov[1]
                
                if self.es_valido(nueva_fila, nueva_col):
                    nuevo_costo_g = costo_g + 1  # Costo de moverse a una nueva celda
                    heuristica = self.heuristica_manhattan((nueva_fila, nueva_col))
                    costo_f = nuevo_costo_g + heuristica  # f = g + h
                    
                    cola_prioridad.insertar(((nueva_fila, nueva_col), camino + [(nueva_fila, nueva_col)], nuevo_costo_g), costo_f)
        
        return None

# Representación del laberinto 1
maze_1 = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
start_maze_1 = (0, 1)
end_maze_1 = (3, 4)

# Representación del laberinto 2
maze_2 = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start_maze_2 = (0, 1)
end_maze_2 = (8, 8)

# Resolviendo el laberinto 1
inicio_tiempo_maze_1 = time.time()

laberinto_solver_1 = LaberintoAStar(maze_1, start_maze_1, end_maze_1)
camino_maze_1 = laberinto_solver_1.a_star()

fin_tiempo_maze_1 = time.time()

if camino_maze_1:
    print("¡Camino encontrado con A* para el laberinto 1!: ", camino_maze_1)
else:
    print("No hay camino posible.")

# Resolviendo el laberinto 2
inicio_tiempo_maze_2 = time.time()

laberinto_solver_2 = LaberintoAStar(maze_2, start_maze_2, end_maze_2)
camino_maze_2 = laberinto_solver_2.a_star()

fin_tiempo_maze_2 = time.time()

if camino_maze_2:
    print("¡Camino encontrado con A* para el laberinto 2!: ", camino_maze_2)
else:
    print("No hay camino posible.")

# Tiempos de cada laberinto
tiempo_total_maze_1 = fin_tiempo_maze_1 - inicio_tiempo_maze_1
tiempo_total_maze_2 = fin_tiempo_maze_2 - inicio_tiempo_maze_2


print(f"El laberinto 1 se resolvió en {tiempo_total_maze_1:.10f}ms.")
print(f"El laberinto 2 se resolvió en {tiempo_total_maze_2:.10f}ms.")
