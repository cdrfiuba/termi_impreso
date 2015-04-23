#Programa que lee un joystick USB conectado a la PC y luego usa esa informacion para editar dos vectores de posiciones. El vector llamado "pos_e" es enviado via serie a un microcontrolador. El otro vector llamado "posc" es usado para mostrar en pantalla unos cuadrados (usando Pygame) que dan idea al usuario de el angulo enviado a cada servo.  Autor: Ignacio Carballeda 04/2014

import pygame
import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 115200)     #abrimos conexion serie con micro 
time.sleep(2)                                       #esperamos a que se establezca la conexion...

pygame.init()					#iniciamos Pygame
size = [600, 400]				#medidas de la ventana para mostrar el programa
pantalla = pygame.display.set_mode(size)	#creamos una ventana
pygame.display.set_caption("T-800")		#establecemos titulo de la ventana
done = False					#Variable que sirve para saber cuando el usuario cerro la ventana del progrma
clock = pygame.time.Clock()			#Objeto reloj que sirve luego para establecer la tasa de refresco de la pantalla
pygame.joystick.init()				#Inicializamos joysticks

posc=[0,0,0,0,0,0] 						#posiciones de los ejes (de 0 a 360 en algunos casos)

posc_e=[200,0,201,0,202,0,203,0,204,0,205,0,206,0,207,0,208,0] 	#posc_e = vector de posc a enviar, se intercalan codigos de comprobacion
#indices[  ,1,   ,3,   ,5,   ,7,   ,9,  ,11,  ,13,  ,15,  ,17]
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


#ejes del JoyStick

X=0
Y=1
W=3
Z=4


r1=pygame.Rect(190,20,10,10)	#Creo rectagulos en pantalla en diferentes posiciones
r2=pygame.Rect(190,40,10,10)
r3=pygame.Rect(190,60,10,10)
r4=pygame.Rect(190,80,10,10)
r5=pygame.Rect(190,100,10,10)
r6=pygame.Rect(190,120,10,10)
r7=pygame.Rect(190,140,10,10)
r8=pygame.Rect(190,160,10,10)
r9=pygame.Rect(190,180,10,10)

iterador = 0
def enviar_serie(pos):		#Funcion que envia el vector de posiciones por puerto serie al microcontrolador
    print pos			#Imprimo valores para verlos por pantalla
    print posc
    for i in pos:		#Recorro todo el vector
        if arduino.writable(): 	#escribo solo si buffer esta disponible
            arduino.write(chr(i))




while done==False:					#mientras que el usuario no cerro la ventana del programa
    for event in pygame.event.get(): 			#Recorremos el vector de eventos
        if event.type == pygame.QUIT:			
			done=True 
	
    if event.type == pygame.JOYBUTTONDOWN:		
		print("Joystick button pressed.")

    if event.type == pygame.JOYBUTTONUP:
		print("Joystick button released.")

    joystick = pygame.joystick.Joystick(0)		#instancia objeto joystick conectado (toma el primer Joystick conectado)
    joystick.init()					#inicia joystick

    axes = joystick.get_numaxes()			#ahora variable axes tiene la cantidad de ejes del control conectado

    for i in range( axes ):				#Recorre todos los ejes obteniendo sus estados
        axis = joystick.get_axis( i )
                    
    buttons = joystick.get_numbuttons()			#obtiene cantidad de botones en joystick

    for i in range( buttons ):				#recorre todos los botones y obtiene sus estados
        button = joystick.get_button( i )
        
#--------EJE0--(cadera)-------------------------------------------------

    if joystick.get_axis(X)>0:				#Segun valores del eje X editamos los vectores de posicion
        if posc[0]>=0 and posc[0]<180:
            r1.move_ip(1,0)
            posc_e[1]+=1
            posc[0]+=1
        if posc[0]>=180 and posc[0]<360:
            r1.move_ip(1,0)
            posc_e[3]+=1
            posc[0]+=1
            
    if joystick.get_axis(X)<0:
        if posc[0]>0 and posc[0]<=180:
            r1.move_ip(-1,0)
            posc_e[1]-=1
            posc[0]-=1
        if posc[0]>180 and posc[0]<=360:
            r1.move_ip(-1,0)
            posc_e[3]-=1
            posc[0]-=1

#-------EJE1--(hombro)--------------------------------------------------

    if joystick.get_axis(Y)>0:
        if posc[1]>=0 and posc[1]<180:
            r2.move_ip(1,0)
            posc_e[5]+=1
            posc[1]+=1
            
    if joystick.get_axis(Y)<0:
        if posc[1]>0 and posc[1]<=180:
            r2.move_ip(-1,0)
            posc_e[5]-=1
            posc[1]-=1

#-------EJE2--(codo)----------------------------------------------------

    if joystick.get_axis(Z)>0:
        if posc[2]>=0 and posc[2]<180:
            r3.move_ip(1,0)
            posc_e[7]+=1
            posc[2]+=1
            
    if joystick.get_axis(Z)<0:
        if posc[2]>0 and posc[2]<=180:
            r3.move_ip(-1,0)
            posc_e[7]-=1
            posc[2]-=1
            
#--------EJE3--(munieca giro)---CHEQUEAR SI GIRA 180 usando 360 (servos metalicos)-

    if joystick.get_axis(W)>0:
        if posc[3]>=0 and posc[3]<180:
            r4.move_ip(1,0)
            posc_e[9]+=1
            posc[3]+=1
        if posc[3]>=180 and posc[3]<360:
            r4.move_ip(1,0)
            posc_e[11]+=1
            posc[3]+=1

    if joystick.get_axis(W)<0:
        if posc[3]>0 and posc[3]<=180:
            r4.move_ip(-1,0)
            posc_e[9]-=1
            posc[3]-=1
        if posc[3]>180 and posc[3]<=360:
            r4.move_ip(-1,0)
            posc_e[11]-=1
            posc[3]-=1

#--------EJE4--(munieca cabeceo)-----------------------------------------

    if joystick.get_button(0)==1:
        if posc[4]>=0 and posc[4]<180:
            r5.move_ip(1,0)
            posc_e[13]+=1
            posc[4]+=1

    if joystick.get_button(1)==1:
        if posc[4]>0 and posc[4]<=180:
            r5.move_ip(-1,0)
            posc_e[13]-=1
            posc[4]-=1

#--------EJE5--(pinza)--------------------------------------------------

    if joystick.get_button(2)==1:
        if posc[5]>=0 and posc[5]<90:
            r6.move_ip(1,0)
            posc[5]+=1
            posc_e[15]+=1

    if joystick.get_button(3)==1:
        if posc[5]>0 and posc[5]<=90:
            r6.move_ip(-1,0)
            posc[5]-=1
            posc_e[15]-=1



#-----------------------------------------------------------------------

    enviar_serie(posc_e);		#Enviamos vector de posiciones por puerto serie
    pantalla.fill(blanco)		#Rellenamos la pantalla con color blanco
    pygame.draw.rect(pantalla,azul,r1) 	#Dibujo los rectangulos en pantalla con diferentes colores
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
