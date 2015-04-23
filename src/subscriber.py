#!/usr/bin/env python                                                      
# license removed for brevity


import time 
import serial
import rospy
from termi_joystick.msg  import arm_poses 

serie = serial.Serial('/dev/ttyUSB0', 115200)     	#abrimos conexion serie con micro 

posc_e=[200,0,201,0,202,0,203,0,204,0,205,0,206,0,207,0,208,0]

def enviar_serie(pos):		#Funcion que envia el vector de posiciones por puerto serie al microcontrolador
    for i in pos:		#Recorro todo el vector
        if serie.writable(): 	#escribo solo si buffer esta disponible
            serie.write(chr(i))

def callback(data):
    global posc_e

    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data) 
    
    posc_e[1]=data.theta1
    posc_e[3]=data.theta2
    posc_e[5]=data.theta3
    posc_e[7]=data.theta4
    posc_e[9]=data.theta5
    posc_e[11]=data.theta6

    enviar_serie(posc_e)
    
def listener():

    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", arm_poses, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()

