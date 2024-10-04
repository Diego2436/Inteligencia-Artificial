import heapq

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

# Representación del laberinto
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
start = (0, 1)
end = (3, 4)

laberinto_solver = LaberintoAStar(maze, start, end)
camino = laberinto_solver.a_star()

if camino:
    print("¡Camino encontrado con A*!: ", camino)
else:
    print("No hay camino posible.")
