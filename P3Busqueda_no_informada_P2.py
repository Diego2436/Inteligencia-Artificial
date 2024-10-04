# Implementación de Pila
class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Implementación de Cola
class Cola:
    def __init__(self):
        self.items = []
    
    def insertar(self, item):
        self.items.append(item)
    
    def quitar(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def recorrer(self):
        return self.items
    
    def buscar(self, item):
        return item in self.items
    
    def is_empty(self):
        return len(self.items) == 0

# Implementación de Lista Genérica
class ListaGenerica:
    def __init__(self):
        self.items = []
    
    def insertar(self, item):
        self.items.append(item)
    
    def buscar(self, item):
        return item in self.items

class Puzzle4:
    def __init__(self, tablero, vacio):
        self.tablero = tablero
        self.vacio = vacio  # Posición del espacio vacío (fila, columna)

    def movimientos_validos(self):
        fila, col = self.vacio
        movimientos = []
        if fila > 0: movimientos.append((-1, 0))  # Mover arriba
        if fila < 1: movimientos.append((1, 0))   # Mover abajo
        if col > 0: movimientos.append((0, -1))   # Mover izquierda
        if col < 1: movimientos.append((0, 1))    # Mover derecha
        return movimientos
    
    def mover(self, direccion):
        fila, col = self.vacio
        nueva_fila = fila + direccion[0]
        nueva_col = col + direccion[1]
        
        nuevo_tablero = [fila[:] for fila in self.tablero]
        nuevo_tablero[fila][col], nuevo_tablero[nueva_fila][nueva_col] = nuevo_tablero[nueva_fila][nueva_col], nuevo_tablero[fila][col]
        
        return Puzzle4(nuevo_tablero, (nueva_fila, nueva_col))
    
    def es_objetivo(self):
        return self.tablero == [[1, 2], [3, 0]]
    
    def __str__(self):
        return str(self.tablero)

def resolver_puzzle_4_bfs(puzzle_inicial):
    cola = Cola()
    cola.insertar(puzzle_inicial)
    visitados = set()

    while not cola.is_empty():
        estado_actual = cola.quitar()
        if str(estado_actual.tablero) in visitados:
            continue
        visitados.add(str(estado_actual.tablero))
        
        if estado_actual.es_objetivo():
            print("¡Puzzle resuelto!")
            print(estado_actual)
            return
        
        for movimiento in estado_actual.movimientos_validos():
            nuevo_estado = estado_actual.mover(movimiento)
            cola.insertar(nuevo_estado)
    
    print("No se pudo resolver el puzzle.")

class LaberintoBFS:
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
    
    def bfs(self):
        cola = Cola()
        cola.insertar((self.start, [self.start]))
        
        while not cola.is_empty():
            # Imprimir la cola antes de quitar un elemento
            print("Cola actual:", [item[0] for item in cola.items])
            
            (fila_actual, col_actual), camino = cola.quitar()
            
            if (fila_actual, col_actual) == self.end:
                return camino
            
            self.visitados[fila_actual][col_actual] = True
            
            # Movimientos posibles: arriba, abajo, izquierda, derecha
            movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for mov in movimientos:
                nueva_fila = fila_actual + mov[0]
                nueva_col = col_actual + mov[1]
                
                if self.es_valido(nueva_fila, nueva_col):
                    cola.insertar(((nueva_fila, nueva_col), camino + [(nueva_fila, nueva_col)]))
        
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

laberinto_solver = LaberintoBFS(maze, start, end)
camino = laberinto_solver.bfs()

if camino:
    print("¡Camino encontrado!: ", camino)
else:
    print("No hay camino posible.")
