import pygame
import time

serie = serial.Serial('/dev/ttyUSB0', 115200)     	#abrimos conexion serie con micro 
time.sleep(2)                                       	#esperamos a que se establezca la conexion...
				
posc=[0,0,0,0,0,0] 		#posiciones de los ejes (de 0 a 360 en algunos casos)

def enviar_serie(pos):		#Funcion que envia el vector de posiciones por puerto serie al microcontrolador
    for i in pos:		#Recorro todo el vector
        if serie.writable(): 	#escribo solo si buffer esta disponible
            serie.write(chr(i))

enviar_serie(posc)

pygame.quit ()
