import pygame
import time

pygame.init()							#iniciamos Pygame
size = [600, 400]						#medidas de la ventana para mostrar el programa
pantalla = pygame.display.set_mode(size)			#creamos una ventana
pygame.display.set_caption("T-800")				#establecemos titulo de la ventana
done = False							#Variable que sirve para saber cuando el usuario cerro la ventana del progrma
clock = pygame.time.Clock()					#Objeto reloj que sirve luego para establecer la tasa de refresco de la pantalla
pygame.joystick.init()						#Inicializamos joysticks

blanco=(255,255,255)    					#Algunos Colores para los cuadrados a mostrar por pantalla
azul=(0,0,255)
rojo=(220,10,10)
verde=(0,200,20)
negro=(200,200,200)
azul2=(0,100,255)
rojo2=(220,10,100)
verde2=(0,200,200)
negro2=(100,100,100)
azul3=(100,100,255)

posc=[0,0,0,0,0,0] 						#posiciones de los ejes (de 0 a 360 en algunos casos)

r1=pygame.Rect(190,20,10,10)					#Creo rectagulos en pantalla en diferentes posiciones
r2=pygame.Rect(190,40,10,10)
r3=pygame.Rect(190,60,10,10)
r4=pygame.Rect(190,80,10,10)
r5=pygame.Rect(190,100,10,10)
r6=pygame.Rect(190,120,10,10)
r7=pygame.Rect(190,140,10,10)
r8=pygame.Rect(190,160,10,10)
r9=pygame.Rect(190,180,10,10)


while done==False:						#mientras que el usuario no cerro la ventana del programa
    for event in pygame.event.get(): 				#Recorremos el vector de eventos
        if event.type == pygame.QUIT:			
			done=True 
	

while done==False:
	pantalla.fill(blanco)					#Rellenamos la pantalla con color blanco
	pygame.draw.rect(pantalla,azul,r1) 			#Dibujo los rectangulos en pantalla con diferentes colores
	pygame.draw.rect(pantalla,rojo,r2)
	pygame.draw.rect(pantalla,verde,r3)
	pygame.draw.rect(pantalla,negro,r4)
	pygame.draw.rect(pantalla,azul2,r5)
	pygame.draw.rect(pantalla,rojo2,r6)
	pygame.draw.rect(pantalla,verde2,r7)
	pygame.draw.rect(pantalla,negro2,r8)
	pygame.draw.rect(pantalla,negro2,r9)

	pygame.display.update()		#Refrescamos pantalla
	clock.tick(20)			#Establecemos velocidad de refresco a 20 FPS (frames per second)

pygame.quit ()
