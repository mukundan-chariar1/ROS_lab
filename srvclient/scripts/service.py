#!/usr/bin/python3
#author: muks
import rospy
from std_srvs.srv import SetBool, SetBoolResponse

class server:
	def __init__(self, srv_name):
		rospy.init_node("server_node")
		rospy.Service(srv_name, SetBool, self.srvHandler)

	def srvHandler(self, request):
		print("Recieved Data: ", request.data)
		response=SetBoolResponse()
		response.success=True
		response.message="Data Recieved"
		return response
if __name__=='__main__':
		s=server("boolcall")
		rospy.spin()