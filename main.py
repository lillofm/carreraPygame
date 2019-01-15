#objetos con pygame
import pygame
import sys#parapoder tirarlo

class Game():
    
    corredores = []
    
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))#creamos la pantalla así
        pygame.display.set_caption("Carrera de bichos")#le ponemos un nombre
        self.background = pygame.image.load("images/background.png")#cargamos la imagen de la pantalla
        
        self.runner = pygame.image.load("images/smallball.png")
        
#Creamos el metodo de los ciclos que consisten en la partida.
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            #comprovacion de los eventos
            for event in pygame.event.get():#para cada evento de la lista pygame. Voy a procesar todos los eventos.se pone a escuchar
                if event.type == pygame.QUIT:#el primero que procesamos es el de salida
                    pygame.quit()#salimos
                    sys.exit()
            #ya hemos comprobado los eventos y ahora renderizamos
            self.__screen.blit(self.background, (0,0))#pinta la pantalla en esta coordenada
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()#refresca
            
            x += 3
            if x >= 250:
                hayGanador = True
                
        pygame.quit()#salimos
        sys.exit()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.competir()
    
    
#DEJAMOS ESTE Y COMENZAMOS DE NUEVO EN CICLOPYGAME