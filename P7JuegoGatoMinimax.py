import math

# Definir constantes
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = '-'
BOARD_SIZE = 4
MAX_DEPTH = 4  # Limitar la profundidad de búsqueda para la IA


# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


# Inicializar tablero vacío
def create_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# Verificar si un jugador ha ganado
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(BOARD_SIZE):
        # Horizontal and Vertical
        if all([board[i][j] == player for j in range(BOARD_SIZE)]) or all(
                [board[j][i] == player for j in range(BOARD_SIZE)]):
            return True

    # Diagonals
    if all([board[i][i] == player for i in range(BOARD_SIZE)]) or all(
            [board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)]):
        return True

    return False


# Verificar si hay empate
def check_draw(board):
    return all([cell != EMPTY for row in board for cell in row])


# Función para evaluar el estado del tablero
def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1  # Gana X
    elif check_winner(board, PLAYER_O):
        return -1  # Gana O
    else:
        return 0  # Empate o estado no terminal


# Obtener todas las posiciones posibles de jugada
def get_empty_positions(board):
    return [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == EMPTY]


# Implementación del algoritmo Minimax con poda Alfa-Beta
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    # Si el juego termina o alcanzamos la profundidad máxima, devolver la evaluación
    if score != 0 or depth == MAX_DEPTH or check_draw(board):
        return score

    if is_maximizing:
        max_eval = -math.inf
        for (i, j) in get_empty_positions(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (i, j) in get_empty_positions(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# IA para encontrar el mejor movimiento
def find_best_move(board, player):
    best_move = None
    best_value = -math.inf if player == PLAYER_X else math.inf

    for (i, j) in get_empty_positions(board):
        board[i][j] = player
        move_value = minimax(board, 0, player == PLAYER_O, -math.inf, math.inf)
        board[i][j] = EMPTY

        if player == PLAYER_X:
            if move_value > best_value:
                best_value = move_value
                best_move = (i, j)
        else:
            if move_value < best_value:
                best_value = move_value
                best_move = (i, j)

    return best_move


# Función para verificar si el juego ha terminado
def game_over(board):
    return check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O) or check_draw(board)


# Jugar una partida de Humano vs IA, IA vs IA o Humano vs Humano
def play_game(mode='human_vs_human'):
    board = create_board()
    current_player = PLAYER_X

    if mode == 'ia_vs_ia':
        while not game_over(board):
            print_board(board)
            print(f"Turno de {current_player}")
            best_move = find_best_move(board, current_player)
            board[best_move[0]][best_move[1]] = current_player
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    else:
        while not game_over(board):
            print_board(board)
            print(f"Turno de {current_player}")

            if mode == 'human_vs_human' or (mode == 'human_vs_ia' and current_player == PLAYER_X):
                try:
                    row = int(input("Ingrese fila (1-4): ")) - 1
                    col = int(input("Ingrese columna (1-4): ")) - 1
                    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY:
                        board[row][col] = current_player
                    else:
                        print("Movimiento inválido, intente nuevamente.")
                        continue
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
            else:
                best_move = find_best_move(board, current_player)
                board[best_move[0]][best_move[1]] = current_player

            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    print_board(board)
    if check_winner(board, PLAYER_X):
        print("¡X gana!")
    elif check_winner(board, PLAYER_O):
        print("¡O gana!")
    else:
        print("¡Es un empate!")


# Selección de modalidad
if __name__ == "__main__":
    print("Seleccione el modo de juego: ")
    print("1. Humano vs Humano")
    print("2. Humano vs IA")
    print("3. IA vs IA")
    choice = int(input())
    if choice == 1:
        play_game('human_vs_human')
    elif choice == 2:
        play_game('human_vs_ia')
    else:
        play_game('ia_vs_ia')
