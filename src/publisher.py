#!/usr/bin/env python
# license removed for brevity

import rospy
from termi_joystick.msg  import arm_poses   #aca van a ir los mensajes tipo arm_poses

import pygame
import time




def talker():

    pub = rospy.Publisher('chatter', arm_poses, queue_size=6)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz 

    poses=arm_poses()				#inicializacion 
    
    done = False				#Variable que sirve para saber cuando el usuario cerro la ventana del progrma
    subo_o_bajo=False
    posc=[0,0,0,0,0,0]				#posiciones de los ejes (de 0 a 360 en algunos casos)
	
    while done==False or not rospy.is_shutdown():	#mientras que el usuario no cerro la ventana del programaes

        if posc[2]==90:
            subo_o_bajo=True
        elif posc[2]==0:
            subo_o_bajo=False

        if subo_o_bajo==True:
            posc[2]=posc[2]-1
        else:
            posc[2]=posc[2]+1

        poses.theta1 = posc[0]
        poses.theta2 = posc[1]
        poses.theta3 = posc[2]
        poses.theta4 = posc[3]
        poses.theta5 = posc[4]
        poses.theta6 = posc[5]
        
        rospy.loginfo(poses)
        pub.publish(poses)
        r.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

