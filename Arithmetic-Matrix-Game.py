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