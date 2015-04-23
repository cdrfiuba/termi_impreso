#!/usr/bin/env python
# license removed for brevity

import rospy
from termi_joystick.msg  import arm_poses   #aca van a ir los mensajes tipo arm_poses
import pygame
import time




def talker():
    

    ### DEBUG
    print "start code"

    pub = rospy.Publisher('chatter', arm_poses, queue_size=6)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz 

    msg=arm_poses()				#inicializacion 
    pygame.init()				#iniciamos Pygame
    
    done = False				#Variable que sirve para saber cuando el usuario cerro la ventana del progrma
    clock = pygame.time.Clock()			#Objeto reloj que sirve luego para establecer la tasa de refresco de la pantalla
    pygame.joystick.init()			#Inicializamos joysticks
    posc=[0,0,0,0,0,0]				#posiciones de los ejes (de 0 a 360 en algunos casos)

    #ejes del JoyStick
    X=0
    Y=1
    W=3
    Z=4

    print "Start joystick capture"

    while done==False or not rospy.is_shutdown():	#mientras que el usuario no cerro la ventana del programa
        joystick_refresh()

        print posc

        msg = posc
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

    pygame.quit ()



# Codigo que actualiza el estado del joystick

def joystick_refresh():

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
            posc[0]+=1
        if posc[0]>=180 and posc[0]<360:
            posc[0]+=1
            
    if joystick.get_axis(X)<0:
        if posc[0]>0 and posc[0]<=180:
            posc[0]-=1
        if posc[0]>180 and posc[0]<=360:
            posc[0]-=1

#-------EJE1--(hombro)--------------------------------------------------

    if joystick.get_axis(Y)>0:
        if posc[1]>=0 and posc[1]<180:
            posc[1]+=1
            
    if joystick.get_axis(Y)<0:
        if posc[1]>0 and posc[1]<=180:
            posc[1]-=1

#-------EJE2--(codo)----------------------------------------------------

    if joystick.get_axis(Z)>0:
        if posc[2]>=0 and posc[2]<180:
            posc[2]+=1
            
    if joystick.get_axis(Z)<0:
        if posc[2]>0 and posc[2]<=180:
            posc[2]-=1
            
#--------EJE3--(munieca giro)---CHEQUEAR SI GIRA 180 usando 360 (servos metalicos)-

    if joystick.get_axis(W)>0:
        if posc[3]>=0 and posc[3]<180:
            posc[3]+=1
        if posc[3]>=180 and posc[3]<360:
            posc[3]+=1

    if joystick.get_axis(W)<0:
        if posc[3]>0 and posc[3]<=180:
            posc[3]-=1
        if posc[3]>180 and posc[3]<=360:
            posc[3]-=1

#--------EJE4--(munieca cabeceo)-----------------------------------------

    if joystick.get_button(0)==1:
        if posc[4]>=0 and posc[4]<180:
            posc[4]+=1

    if joystick.get_button(1)==1:
        if posc[4]>0 and posc[4]<=180:
            posc[4]-=1

#--------EJE5--(pinza)--------------------------------------------------

    if joystick.get_button(2)==1:
        if posc[5]>=0 and posc[5]<90:
            posc_e[15]+=1

    if joystick.get_button(3)==1:
        if posc[5]>0 and posc[5]<=90:
            posc_e[15]-=1

#-----------------------------------------------------------------------
    return posc

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

