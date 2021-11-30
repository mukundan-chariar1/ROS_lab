#!/usr/bin/env python
import rospy
from pub_sub_lab.msg import status,count,matrix

M = [[1,2,3], [4,5,8], [7,8,9]]

def main():
    rospy.init_node('publisher')
    time_pub = rospy.Publisher('/status', status, queue_size=1)
    count_pub = rospy.Publisher('/counter', count, queue_size=1)
    matrix_pub = rospy.Publisher('/matrix', matrix, queue_size=1)

    time_msg = status()
    count_msg = count()
    count_msg.count = 0
    matrix_msg = matrix()
    matrix_msg.rows = len(M)
    matrix_msg.columns = len(M[0])

    for i in M:
        for j in i:
            matrix_msg.matrix.append(int(j))

    rospy.loginfo('sending messages')
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        time_msg.status = rospy.Time.now()
        time_pub.publish(time_msg)
        count_pub.publish(count_msg)
        count_msg.count += 1
        matrix_pub.publish(matrix_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass