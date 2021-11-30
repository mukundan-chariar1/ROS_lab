#!/usr/bin/python3
import rospy
import random
import numpy as np

from custom_msg_py.msg import status, count, matrix

def talker(event):
    #Initializing the publishers
    status_pub = rospy.Publisher('custom_msg_topic', status, queue_size=100)
    count_pub = rospy.Publisher('custom_msg_topic2', count, queue_size=100)
    matrix_pub = rospy.Publisher('custom_msg_topic3', matrix, queue_size=100)

    #Initializing messages
    status_msg = status()
    count_msg = count()
    matrix_msg = matrix()

    #Status message
    status_msg.time.data = rospy.Time.now()

    #Count message
    num = random.randint(1, 100)
    count_msg.int.data = num

    #Matrix message
    matrix_msg.len_x = 3
    matrix_msg.len_y = 3
    matrix_msg.data = np.arange(9)


    rospy.loginfo(status_msg)
    rospy.loginfo(count_msg)
    rospy.loginfo(matrix_msg)
    status_pub.publish(status_msg)
    count_pub.publish(count_msg)
    matrix_pub.publish(matrix_msg)

if __name__ == '__main__':
    try:
        rospy.init_node('custom_talker')
        T = rospy.Duration(1)
        timer = rospy.Timer(T, talker)
        rospy.spin() 

    except rospy.ROSInterruptException:
        pass
