#!/usr/bin/env python
from __future__ import print_function
import rospy
from pub_sub_lab.msg import status,count,matrix

def count_callback(msg):
    global ctr
    ctr = msg.count

def time_callback(msg):
    global tm
    tm = msg.status

def matrix_callback(msg):
    global M,r,c, M_st
    M = []
    M_st = ''
    temp = []
    r = msg.rows
    c = msg.columns
    j = 0
    for i in msg.matrix:
        temp.append(i)
        M_st = M_st + str(i) + " "
        j += 1
        if j == c:
            M.append(temp)
            M_st += "\n"
            j = 0
            temp = []

def main():
    rospy.init_node('subscriber')
    rospy.Subscriber('/status', status, time_callback)
    rospy.Subscriber('/counter', count, count_callback)
    rospy.Subscriber('/matrix', matrix, matrix_callback)
    while not 'M' in globals() or not 'ctr' in globals() or not 'tm' in globals():
        rospy.loginfo('waiting for publisher')

    while True:
        message = "\n---messages recieved---\ntime = "+str(tm)+"\ncounter = "+str(ctr)+"\nmatrix = \n"+M_st+"\n"
        rospy.loginfo(message)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        sys.exit(1)
        pass