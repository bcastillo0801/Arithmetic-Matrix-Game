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
