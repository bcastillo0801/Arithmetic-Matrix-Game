import pygame
import random
import sys

# Configuracion inicial del juego
def setup_game():
print("CONFIGURACIÓN DEL JUEGO: MATRIZ ARITMÉTICA")

n = 0
while n < 3:
    n = int(input("Ingrese el tamaño del tablero NxN (donde N debe ser mayor o igual a 3): "))
        
p1_nombre = input("Nombre del Jugador 1: ")
p2_nombre = input("Nombre del Jugador 2: ")

turnos = 0
while turnos < 1:
    turnos = int(input("¿Cuántos turnos jugará cada jugador?: "))
        
return n, p1_nombre, p2_nombre, turnos
# Inicialización de pygame
N, jugador1, jugador2, max_turnos = setup_game()
pygame.init()

Constantes
CELL_SIZE = 80
MARGIN = 10
WIDTH = max(800, N * CELL_SIZE + (N + 1) * MARGIN + 300)
HEIGHT = max(600, N * CELL_SIZE + (N + 1) * MARGIN + 100)

#colores
Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
ROJO = (200, 50, 50)
AZUL = (50, 50, 200)
VERDE = (50, 200, 50)

#Configuración de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matriz Aritmética")
font_large = pygame.font.SysFont("arial", 40, bold=True)
font_medium = pygame.font.SysFont("arial", 28)
font_small = pygame.font.SysFont("arial", 20)

# TAREAS DE 4 A 6
Lógica del juego

Matriz inicializada una sola vez con valores aleatorios entre 0 y 11

matrix = []
used_cells = []
for fila in range(N):
nueva_fila_matrix = []
nueva_fila_usadas = []
for columna in range(N):
nueva_fila_matrix.append(random.randint(0, 11))
nueva_fila_usadas.append(False)
matrix.append(nueva_fila_matrix)
used_cells.append(nueva_fila_usadas)

players = [{"name": jugador1, "score": 0}, {"name": jugador2, "score": 0}]
current_player_idx = 0
current_turn = 1

Estados del juego: "SELECT_CELL", "ANSWERING", "GAME_OVER"

game_state = "SELECT_CELL"

Variables de turno

selected_cell = None
neighbors = []
correct_answer = 0
options = []
time_start = 0
TIME_LIMIT = 25000 # 25 segundos en milisegundos

def get_neighbors(row, col):
"""Devuelve las coordenadas de los vecinos válidos."""
dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
valid_neighbors = []
for dr, dc in dirs:
r, c = row + dr, col + dc
if 0 <= r < N and 0 <= c < N:
valid_neighbors.append((r, c))
return valid_neighbors

def generate_options(correct):
"""Genera 4 opciones de respuesta incluyendo la correcta."""
opts = [correct]
while len(opts) < 4:
# Generar respuestas falsas plausibles
offset = random.randint(-20, 20)
fake_ans = correct + offset
if fake_ans not in opts and fake_ans >= 0:
opts.append(fake_ans)
random.shuffle(opts)
return opts

def draw_grid():
"""Dibuja el tablero en pantalla."""
for row in range(N):
for col in range(N):
rect = pygame.Rect(
MARGIN + col * (CELL_SIZE + MARGIN),
MARGIN + row * (CELL_SIZE + MARGIN) + 50,
CELL_SIZE, CELL_SIZE
)

        # Celda ya utilizada
        if used_cells[row][col] and game_state == "SELECT_CELL":
            pygame.draw.rect(screen, GRIS, rect)
            text = font_large.render("X", True, NEGRO)
            screen.blit(text, (rect.x + 25, rect.y + 15))
        # Durante la fase de respuesta
        elif game_state == "ANSWERING":
            if (row, col) == selected_cell:
                pygame.draw.rect(screen, BLANCO, rect)
                pygame.draw.rect(screen, ROJO, rect, 3)
                val_text = font_large.render(str(matrix[row][col]), True, ROJO)
                screen.blit(val_text, (rect.x + 20, rect.y + 15))
            elif (row, col) in neighbors:
                pygame.draw.rect(screen, BLANCO, rect)
                pygame.draw.rect(screen, AZUL, rect, 3)
                val_text = font_large.render(str(matrix[row][col]), True, AZUL)
                screen.blit(val_text, (rect.x + 20, rect.y + 15))
            else:
                pygame.draw.rect(screen, BLANCO, rect)
                pygame.draw.rect(screen, NEGRO, rect, 2)
                if used_cells[row][col]:
                     text = font_large.render("X", True, NEGRO)
                     screen.blit(text, (rect.x + 25, rect.y + 15))
        # Celdas ocultas por defecto
        else:
            pygame.draw.rect(screen, BLANCO, rect)
            pygame.draw.rect(screen, NEGRO, rect, 2)

# TAREAS DE 7 A 9

def draw_ui(time_left):
"""Dibuja la interfaz lateral y superior"""
# Turno e Información
info_text = font_medium.render(f"Ronda: {current_turn}/{max_turnos}", True, NEGRO)
screen.blit(info_text, (MARGIN, 10))

panel_x = N * (CELL_SIZE + MARGIN) + MARGIN + 20

# Jugador Actual
curr_player = players[current_player_idx]["name"]
player_text = font_large.render(f"Turno: {curr_player}", True, AZUL)
screen.blit(player_text, (panel_x, 50))

# Puntuaciones
y_offset = 120
score_title = font_medium.render("Puntuaciones:", True, NEGRO)
screen.blit(score_title, (panel_x, y_offset))
for p in players:
    y_offset += 35
    score_text = font_small.render(f"{p['name']}: {p['score']} pts", True, NEGRO)
    screen.blit(score_text, (panel_x, y_offset))
    
# Temporizador y Opciones
if game_state == "ANSWERING":
    if time_left < 5:
        color_time = ROJO
    else:
        color_time = NEGRO
    time_text = font_large.render(f"Tiempo: {time_left}s", True, color_time)
    screen.blit(time_text, (panel_x, y_offset + 50))
    
    # Botones de opciones
    btn_y = y_offset + 120
    option_rects = []
    for i in range(len(options)):
        opt = options[i]
        btn_rect = pygame.Rect(panel_x, btn_y + (i * 60), 200, 40)
        pygame.draw.rect(screen, GRIS, btn_rect)
        pygame.draw.rect(screen, NEGRO, btn_rect, 2)
        opt_text = font_medium.render(str(opt), True, NEGRO)
        screen.blit(opt_text, (btn_rect.x + 10, btn_rect.y + 5))
        option_rects.append(btn_rect)
        
    return option_rects
return []


# BUCLE PRINCIPAL 
running = True
clock = pygame.time.Clock()
option_rects = []

while running:
    screen.fill(BLANCO)
    time_left = 0
    
    if game_state == "ANSWERING":
        elapsed_time = pygame.time.get_ticks() - time_start
        time_left = max(0, (TIME_LIMIT - elapsed_time) // 1000)
        
        # El jugador pierde su turno por tiempo
        if time_left == 0:
            used_cells[selected_cell[0]][selected_cell[1]] = True
            if current_player_idx == 0:
                current_player_idx = 1
            else:
                current_player_idx = 0
            if current_player_idx == 0:
                current_turn += 1
            if current_turn <= max_turnos:
                game_state = "SELECT_CELL"
            else:
                game_state = "GAME_OVER"
    
    # Renderizado
    draw_grid()
    if game_state != "GAME_OVER":
        option_rects = draw_ui(time_left)
    else:
        # Pantalla final
        winner = players[0]
        if players[1]['score'] > players[0]['score']:
            winner = players[1]
        if players[0]['score'] == players[1]['score']:
            win_text = font_large.render("¡Es un Empate!", True, VERDE)
        else:
            win_text = font_large.render(f"¡Ganador: {winner['name']}!", True, VERDE)
        screen.blit(win_text, (WIDTH//2 - 150, HEIGHT//2))
    
    pygame.display.flip()
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            
            if game_state == "SELECT_CELL":
                # Detectar clic en la matriz
                col = (mouse_pos[0] - MARGIN) // (CELL_SIZE + MARGIN)
                row = (mouse_pos[1] - MARGIN - 50) // (CELL_SIZE + MARGIN)
                
                if 0 <= row < N and 0 <= col < N:
                    if not used_cells[row][col]:
                        selected_cell = (row, col)
                        neighbors = get_neighbors(row, col)
                        
                        # Cálculo matemático de las reglas
                        sum_neighbors = 0
                        for r, c in neighbors:
                            sum_neighbors = sum_neighbors + matrix[r][c]
                        correct_answer = sum_neighbors * matrix[row][col]
                        
                        options = generate_options(correct_answer)
                        time_start = pygame.time.get_ticks()
                        game_state = "ANSWERING"
                        
            elif game_state == "ANSWERING":
                # Detectar clic en opciones
                for i in range(len(option_rects)):
                    rect = option_rects[i]
                    if rect.collidepoint(mouse_pos):
                        if options[i] == correct_answer:
                            players[current_player_idx]["score"] += 3
                            
                        # Marcar la celda seleccionada con X
                        used_cells[selected_cell[0]][selected_cell[1]] = True
                        
                        # Cambiar de turno
                        if current_player_idx == 0:
                            current_player_idx = 1
                        else:
                            current_player_idx = 0
                        if current_player_idx == 0:
                            current_turn += 1
                            
                        if current_turn <= max_turnos:
                            game_state = "SELECT_CELL"
                        else:
                            game_state = "GAME_OVER"

    clock.tick(30)

pygame.quit()
sys.exit()
