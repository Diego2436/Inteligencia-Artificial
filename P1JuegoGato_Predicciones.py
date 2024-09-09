import tkinter as tk
import random

# Inicializar el tablero
def inicializar_tablero():
    return [[' ' for _ in range(4)] for _ in range(4)]

# Comprobar si hay un ganador
def comprobar_ganador(tablero, jugador):
    # Comprobar filas y columnas
    for i in range(4):
        if all(tablero[i][j] == jugador for j in range(4)) or \
           all(tablero[j][i] == jugador for j in range(4)):
            return True

    # Comprobar diagonales
    if all(tablero[i][i] == jugador for i in range(4)) or \
       all(tablero[i][3-i] == jugador for i in range(4)):
        return True

    return False

# Comprobar si hay un empate
def comprobar_empate(tablero):
    return all(tablero[i][j] != ' ' for i in range(4) for j in range(4))

# Manejar el movimiento del jugador
def movimiento_jugador(tablero, botones, fila, columna):
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = 'X'
        botones[fila][columna].config(text='X', state='disabled')
        if comprobar_ganador(tablero, 'X'):
            mostrar_resultado("¡Felicidades! Has ganado.")
        elif comprobar_empate(tablero):
            mostrar_resultado("El juego es un empate.")
        else:
            movimiento_computadora(tablero, botones)

# Movimiento de la computadora (estrategia simple)
def movimiento_computadora(tablero, botones):
    # Buscar si la computadora puede ganar en el próximo movimiento
    if buscar_ganar_o_bloquear(tablero, botones, 'O'):
        if comprobar_ganador(tablero, 'O'):
            print("La computadora ha ganado")
            mostrar_resultado("La computadora ha ganado.")
        return

    # Bloquear si el jugador está a punto de ganar
    if buscar_ganar_o_bloquear(tablero, botones, 'X'):
        if comprobar_ganador(tablero, 'O'):
            print("La computadora ha ganado")
            mostrar_resultado("La computadora ha ganado.")
        return

    # Si no hay oportunidad de ganar o necesidad de bloquear, elegir al azar
    posiciones_vacias = [(i, j) for i in range(4) for j in range(4) if tablero[i][j] == ' ']
    if posiciones_vacias:
        fila, columna = random.choice(posiciones_vacias)
        tablero[fila][columna] = 'O'
        botones[fila][columna].config(text='O', state='disabled')
        if comprobar_ganador(tablero, 'O'):
            print("La computadora ha ganado")
            mostrar_resultado("La computadora ha ganado.")
        elif comprobar_empate(tablero):
            mostrar_resultado("El juego es un empate.")

# Función para buscar ganar o bloquear
def buscar_ganar_o_bloquear(tablero, botones, jugador):
    # Comprobar filas y columnas
    for i in range(4):
        # Comprobar si faltan movimientos para completar una fila
        if tablero[i].count(jugador) == 3 and tablero[i].count(' ') == 1:
            columna = tablero[i].index(' ')
            tablero[i][columna] = 'O'
            botones[i][columna].config(text='O', state='disabled')
            return True
        # Comprobar si faltan movimientos para completar una columna
        columna = [tablero[j][i] for j in range(4)]
        if columna.count(jugador) == 3 and columna.count(' ') == 1:
            fila = columna.index(' ')
            tablero[fila][i] = 'O'
            botones[fila][i].config(text='O', state='disabled')
            return True

    # Comprobar diagonales
    diagonal1 = [tablero[i][i] for i in range(4)]
    diagonal2 = [tablero[i][3 - i] for i in range(4)]
    if diagonal1.count(jugador) == 3 and diagonal1.count(' ') == 1:
        indice = diagonal1.index(' ')
        tablero[indice][indice] = 'O'
        botones[indice][indice].config(text='O', state='disabled')
        return True
    if diagonal2.count(jugador) == 3 and diagonal2.count(' ') == 1:
        indice = diagonal2.index(' ')
        tablero[indice][3 - indice] = 'O'
        botones[indice][3 - indice].config(text='O', state='disabled')
        return True

    return False

# Mostrar el resultado del juego y habilitar el botón de reinicio
def mostrar_resultado(mensaje):
    resultado_label.config(text=mensaje)
    for fila in botones:
        for boton in fila:
            boton.config(state='disabled')  # Deshabilitar todos los botones

# Reiniciar el juego
def reiniciar_juego():
    global tablero
    tablero = inicializar_tablero()  # Reinicializa el tablero
    resultado_label.config(text="")  # Limpia el mensaje de resultado
    for i in range(4):
        for j in range(4):
            botones[i][j].config(text=' ', state='normal')  # Limpia y reactiva los botones

# Crear la ventana del juego
def crear_ventana():
    global botones, resultado_label, boton_reiniciar, tablero
    ventana = tk.Tk()
    ventana.title("Gato - Cuatro en Línea")
    
    tablero = inicializar_tablero()
    botones = []

    # Crear botones del tablero
    for i in range(4):
        fila_botones = []
        for j in range(4):
            boton = tk.Button(ventana, text=' ', width=6, height=3, 
                              command=lambda i=i, j=j: movimiento_jugador(tablero, botones, i, j))
            boton.grid(row=i, column=j, padx=5, pady=5)
            fila_botones.append(boton)
        botones.append(fila_botones)

    # Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana, text="", font=('Arial', 14))
    resultado_label.grid(row=4, column=0, columnspan=4, pady=10)

    # Botón para reiniciar el juego (siempre visible)
    boton_reiniciar = tk.Button(ventana, text="Reiniciar juego", font=('Arial', 12), command=reiniciar_juego)
    boton_reiniciar.grid(row=5, column=0, columnspan=4, pady=10)  # Siempre visible

    ventana.mainloop()

# Iniciar el juego
crear_ventana()
