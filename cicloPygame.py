#objetos con pygame
import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width, height))#para crear la pantalla
screen.fill((255, 148, 48))#para poner la pantalla de color naranja de fondo
pygame.display.set_caption("ciclo basico de pygame")#le ponemos un nombre

pygame.init()#si el sistema es mas anituo y no funciona, se pone pygame.font.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    pygame.display.flip()#para refrescar la pantalla
            
pygame.quit()#cierra pygame. sie el juego es muy complejo, es posible que tarde en cerrase o incluso se quede colgado mientras intenta cerrar
sys.exit()#cierra python y nos aseguramos de cerrarlo