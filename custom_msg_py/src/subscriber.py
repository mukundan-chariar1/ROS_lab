#!/usr/bin/python3
import rospy
import numpy as np

from custom_msg_py.msg import status, count, matrix

def statusCallBack(data):
    rospy.loginfo("Status: %d", data.time.data.secs)
    

def countCallBack(data2):
    rospy.loginfo("Count: %d", data2.int.data)

def matrixCallBack(data3):
    rospy.loginfo("Matrix: ")
    matrix = np.array(data3.data)

    rospy.loginfo(matrix.reshape(data3.len_x, data3.len_y))

def listener():
    status_sub = rospy.Subscriber("custom_msg_topic", status, statusCallBack)
    count_sub = rospy.Subscriber("custom_msg_topic2", count, countCallBack)
    matrix_sub = rospy.Subscriber("custom_msg_topic3", matrix, matrixCallBack)
    


if __name__ == '__main__':
    try:
        rospy.init_node("custom_listener")
        listener()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass